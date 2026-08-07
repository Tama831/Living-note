#!/usr/bin/env python3
"""living_notes_update.py — 生きたノート: 関心領域の新着論文を収集し、ノートを織り直す。

設計:
- config/living-notes.json にトピックを登録 (slug / queries / note path)
- cron / launchd から毎日呼んでよい — スクリプト自身が interval_days ゲートを持つ
- 収集は PubMed E-utilities の素の HTTP API (無認証・鍵不要)。依存は Python 標準ライブラリのみ
- 重複判定は PMID / DOI を、手持ちの文献リスト (config の dedupe_sources: .bib / .jsonl) と
  既収集分 (state の seen_pmids) の両方に対して行う
- 織り (weave) = LLM CLI (既定: claude -p) にノート全文+新着を渡して編み直す。失敗しても
  収集済みの新着ログは残る (fail-soft — 定期実行を道連れにしない)。LLM CLI が無い環境は
  --no-weave で収集だけ回し、--print-weave-prompt で出るプロンプトを任意の AI チャットに貼る

使い方:
    python3 scripts/living_notes_update.py                # 通常 (7日ゲートあり)
    python3 scripts/living_notes_update.py --force        # ゲート無視で今すぐ
    python3 scripts/living_notes_update.py --dry-run      # 書き込みなしで新着候補を表示
    python3 scripts/living_notes_update.py --no-weave     # 収集のみ (織りは後でセッションで)
    python3 scripts/living_notes_update.py --status       # 保存済みの状態を表示
    python3 scripts/living_notes_update.py --topic SLUG   # 1トピックだけ処理
    python3 scripts/living_notes_update.py --sleep SLUG   # 🛏️休眠 (収集停止、ノートは残る)
    python3 scripts/living_notes_update.py --wake SLUG    # 🟢再稼働
    python3 scripts/living_notes_update.py --print-weave-prompt SLUG  # 織りプロンプトを表示
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

try:  # NCBI は信頼先だが、XXE/entity-expansion 対策で defusedxml があれば使う
    import defusedxml.ElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config/living-notes.json"
STATE = ROOT / "data/status/living-notes-state.json"

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
HTTP_PAUSE = 0.34  # NCBI 無キー上限 3 req/s を守る

ANCHORS = [
    "<!-- LN:SUMMARY:START -->", "<!-- LN:SUMMARY:END -->",
    "<!-- LN:SYNTHESIS:START -->", "<!-- LN:SYNTHESIS:END -->",
    "<!-- LN:BIB:START -->", "<!-- LN:BIB:END -->",
    "<!-- LN:LOG:START -->", "<!-- LN:LOG:END -->",
]

# 既定の織り手 = claude CLI。launchd/cron の細い PATH でも見つかるよう絶対パスも探す。
# config の "weave_command" (例: ["gemini", "-p"]) で任意の LLM CLI に差し替え可
CLAUDE_CANDIDATES = [
    shutil.which("claude"),
    str(Path.home() / ".local/bin/claude"),
    "/opt/homebrew/bin/claude",
    "/usr/local/bin/claude",
]


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def library_ids(cfg: dict) -> set[str]:
    """手持ち文献リストの識別子集合 (`doi:...` / `pmid:...`、小文字)。dedupe の基準。

    config の "dedupe_sources" に .bib (BibTeX export) / .jsonl ({"doi": ...} 行) の
    パスを並べる。Paperpile / Zotero など管理ツールを問わず export ファイルがあれば動く。"""
    ids: set[str] = set()
    for rel in cfg.get("dedupe_sources", []):
        path = ROOT / rel
        if not path.exists():
            continue
        if path.suffix == ".bib":
            text = path.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r'doi\s*=\s*[{"]([^}"]+)[}"]', text):
                ids.add("doi:" + m.group(1).strip().lower())
            for m in re.finditer(r'pmid\s*=\s*[{"]?(\d+)', text):
                ids.add("pmid:" + m.group(1))
        elif path.suffix == ".jsonl":
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if e.get("doi"):
                    ids.add("doi:" + str(e["doi"]).strip().lower())
                if e.get("pmid"):
                    ids.add("pmid:" + str(e["pmid"]))
    return ids


def _http_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "living-notes/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def _http_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "living-notes/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def esearch(query: str, mindate: str, maxdate: str, retmax: int = 100) -> list[str]:
    """PubMed 検索。日付は entry date (edat) 基準 = 「PubMed に載った日」の窓。"""
    params = urllib.parse.urlencode({
        "db": "pubmed", "retmode": "json", "term": query,
        "datetype": "edat", "mindate": mindate, "maxdate": maxdate,
        "retmax": str(retmax), "sort": "date",
    })
    time.sleep(HTTP_PAUSE)
    data = _http_json(f"{EUTILS}/esearch.fcgi?{params}")
    return list(data.get("esearchresult", {}).get("idlist", []))


def parse_efetch_xml(xml_text: str) -> list[dict]:
    """efetch XML → [{pmid, doi, title, authors, journal, year, abstract}]"""
    out = []
    root = ET.fromstring(xml_text)
    for art in root.iter("PubmedArticle"):
        cite = art.find("MedlineCitation")
        if cite is None:
            continue
        pmid = (cite.findtext("PMID") or "").strip()
        a = cite.find("Article")
        if a is None or not pmid:
            continue
        # 注意: Element は子要素ゼロだと falsy なので `or` フォールバック禁止 (is None で判定)
        t_el = a.find("ArticleTitle")
        title = "".join(t_el.itertext()).strip() if t_el is not None else ""
        journal = (a.findtext("Journal/ISOAbbreviation")
                   or a.findtext("Journal/Title") or "").strip()
        year = (a.findtext("Journal/JournalIssue/PubDate/Year")
                or (a.findtext("Journal/JournalIssue/PubDate/MedlineDate") or "")[:4]).strip()
        authors = []
        for au in a.iter("Author"):
            last = au.findtext("LastName")
            if last:
                authors.append(f"{last} {au.findtext('Initials') or ''}".strip())
            elif au.findtext("CollectiveName"):
                authors.append(au.findtext("CollectiveName").strip())
        abstract = " ".join(
            "".join(t.itertext()).strip() for t in a.iter("AbstractText")).strip()
        doi = ""
        for aid in art.iter("ArticleId"):
            if aid.get("IdType") == "doi":
                doi = (aid.text or "").strip().lower()
        out.append({"pmid": pmid, "doi": doi, "title": title, "authors": authors,
                    "journal": journal, "year": year, "abstract": abstract})
    return out


def efetch(pmids: list[str]) -> list[dict]:
    if not pmids:
        return []
    params = urllib.parse.urlencode({"db": "pubmed", "retmode": "xml", "id": ",".join(pmids)})
    time.sleep(HTTP_PAUSE)
    return parse_efetch_xml(_http_text(f"{EUTILS}/efetch.fcgi?{params}"))


def filter_new(entries: list[dict], seen_pmids: set[str], lib: set[str]) -> list[dict]:
    fresh = []
    for e in entries:
        if e["pmid"] in seen_pmids or ("pmid:" + e["pmid"]) in lib:
            continue
        if e["doi"] and ("doi:" + e["doi"]) in lib:
            continue
        fresh.append(e)
    return fresh


def format_log_block(entries: list[dict], date: str) -> str:
    lines = [f"### ⏳ {date} 収集分 ({len(entries)}件・織り待ち)", ""]
    for e in entries:
        au = ", ".join(e["authors"][:3]) + (" et al." if len(e["authors"]) > 3 else "")
        head = f"- **{e['title']}** — {au} *{e['journal']}* ({e['year']})."
        links = f" PMID [{e['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{e['pmid']}/)"
        if e["doi"]:
            links += f" / [DOI](https://doi.org/{e['doi']})"
        lines.append(head + links)
        if e["abstract"]:
            snippet = e["abstract"][:300] + ("…" if len(e["abstract"]) > 300 else "")
            lines.append(f"  - 抄録: {snippet}")
    lines.append("")
    return "\n".join(lines)


def insert_after_anchor(text: str, anchor: str, block: str) -> str:
    """anchor 行の直後に block を挿入 (新着が上に来る)。anchor が無ければ ValueError。"""
    idx = text.find(anchor)
    if idx < 0:
        raise ValueError(f"anchor not found: {anchor}")
    line_end = text.index("\n", idx)
    return text[: line_end + 1] + "\n" + block + text[line_end + 1:]


def bump_updated(text: str, date: str) -> str:
    return re.sub(r"^updated: .*$", f"updated: {date}", text, count=1, flags=re.M)


def run_claude(prompt: str, timeout: int = 600, cmd: list[str] | None = None) -> str:
    """LLM CLI をヘッドレス実行。既定は claude -p。config "weave_command" で差し替え可。"""
    if cmd:
        argv = [*cmd, prompt]
    else:
        binary = next((c for c in CLAUDE_CANDIDATES if c and Path(c).exists()), None)
        if binary is None:
            raise RuntimeError("LLM CLI not found (claude が無ければ config の weave_command を設定)")
        argv = [binary, "-p", "--output-format", "text", prompt]
    result = subprocess.run(
        argv, capture_output=True, text=True, timeout=timeout, cwd=str(ROOT),
    )
    if result.returncode != 0:
        raise RuntimeError(f"weave LLM failed (rc={result.returncode}): {result.stderr.strip()[:500]}")
    return result.stdout.strip()


def weave_prompt(note_text: str, topic_title: str) -> str:
    return (
        f"あなたは「生きたノート」の織り手です。対象トピック: {topic_title}。\n"
        "以下の Markdown ノートには『⏳織り待ち』の新着ログが含まれます。次の作業をしてください:\n"
        "1. 新着の内容を『🧵 横断まとめ』の該当テーマに編み込む (羅列でなく既存の記述と統合して書き直す)\n"
        "2. 取り込んだ論文を『📚 文献リスト』に追記する (PMID/DOIリンク付き)\n"
        "3. 『📌 5行サマリ』を現時点の全体像で書き直す (5行以内厳守)\n"
        "4. 新着ログの ⏳ を ✅ に変える (ログ自体は履歴として残す)\n"
        "制約: <!-- LN:...:START/END --> の8つのアンカーコメントを一つも消さない・順序を変えない。\n"
        "frontmatter (--- で囲まれた部分) は updated 以外変えない。\n"
        "出力はノート全文の Markdown のみ。前置き・後書き・コードフェンス禁止。\n\n"
        "=== ノート全文 ===\n" + note_text
    )


def weave_note(note_text: str, topic_title: str, runner=run_claude) -> str | None:
    """織り直したノート全文を返す。検証に落ちたら None (呼び元は fail-soft)。"""
    try:
        woven = runner(weave_prompt(note_text, topic_title))
    except Exception as e:
        print(f"  [weave] failed: {e}", file=sys.stderr)
        return None
    # コードフェンスで包んで返す事故への保険
    if woven.startswith("```"):
        woven = re.sub(r"^```[a-z]*\n", "", woven)
        woven = re.sub(r"\n```\s*$", "", woven)
    ok = (all(a in woven for a in ANCHORS)
          and woven.lstrip().startswith("---")
          and len(woven) >= 0.5 * len(note_text))
    if not ok:
        print("  [weave] output failed validation — keeping unwoven note", file=sys.stderr)
        return None
    return woven


def prune_log(text: str, keep: int) -> tuple[str, str]:
    """新着ログの ✅ (編み込み済み) ブロックを新しい順に keep 個だけ残す。

    あふれた分を第2戻り値で返す (呼び元が _archive へ退避)。⏳ (織り待ち) は
    未処理の作業品なので数に関係なく必ず残す。ノート肥大化のガード。"""
    start_a, end_a = "<!-- LN:LOG:START -->", "<!-- LN:LOG:END -->"
    i, j = text.find(start_a), text.find(end_a)
    if i < 0 or j < 0 or keep < 0:
        return text, ""
    sec_start = text.index("\n", i) + 1
    body = text[sec_start:j]
    parts = re.split(r"(?=^### )", body, flags=re.M)
    lead = parts[0] if parts and not parts[0].startswith("### ") else ""
    blocks = [p for p in parts if p.startswith("### ")]
    kept, overflow, done_count = [], [], 0
    for b in blocks:  # ノート内は新しい順に並んでいる
        if b.startswith("### ✅"):
            done_count += 1
            (kept if done_count <= keep else overflow).append(b)
        else:
            kept.append(b)
    if not overflow:
        return text, ""
    return text[:sec_start] + lead + "".join(kept) + text[j:], "".join(overflow)


def atomic_write(path: Path, text: str) -> None:
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, str(path))


def should_run(topic_state: dict, interval_days: int, force: bool, now: datetime) -> bool:
    if force:
        return True
    last = topic_state.get("last_run")
    if not last:
        return True
    return datetime.fromisoformat(last) <= now - timedelta(days=interval_days)


def process_topic(topic: dict, cfg: dict, state: dict, lib: set[str], *,
                  dry_run: bool, force: bool, weave: bool, now: datetime | None = None) -> int:
    now = now or datetime.now()
    slug = topic["slug"]
    if topic.get("status") == "dormant":
        print(f"[{slug}] 🛏️ 休眠中 (since {topic.get('since', '?')}) — 収集スキップ。再開: --wake {slug}")
        return 0
    ts = state.setdefault(slug, {})
    if not should_run(ts, int(cfg.get("interval_days", 7)), force, now):
        print(f"[{slug}] gate: {cfg.get('interval_days', 7)}日未満なのでスキップ (--force で無視可)")
        return 0

    note_path = ROOT / topic["note"]
    if not note_path.exists():
        print(f"[{slug}] note not found: {note_path} — スキップ", file=sys.stderr)
        return 0

    today = now.strftime("%Y-%m-%d")
    maxdate = now.strftime("%Y/%m/%d")
    if ts.get("last_edat"):
        # edat の反映ラグ対策に3日重ねる (重複は seen_pmids が吸収する)
        mindate = (datetime.strptime(ts["last_edat"], "%Y/%m/%d")
                   - timedelta(days=3)).strftime("%Y/%m/%d")
    else:
        mindate = (now - timedelta(days=int(cfg.get("initial_lookback_days", 180)))).strftime("%Y/%m/%d")

    pmids: list[str] = []
    for q in topic["queries"]:
        try:
            pmids.extend(esearch(q, mindate, maxdate))
        except Exception as e:
            print(f"[{slug}] esearch failed: {e}", file=sys.stderr)
    pmids = list(dict.fromkeys(pmids))  # 順序保持で重複除去

    seen = set(ts.get("seen_pmids", []))
    cand_ids = [p for p in pmids if p not in seen]
    max_per_run = int(cfg.get("max_per_run", 25))
    dropped = max(0, len(cand_ids) - max_per_run)
    cand_ids = cand_ids[:max_per_run]

    try:
        entries = efetch(cand_ids)
    except Exception as e:
        print(f"[{slug}] efetch failed: {e}", file=sys.stderr)
        return 0
    fresh = filter_new(entries, seen, lib)

    print(f"[{slug}] 検索窓 {mindate}→{maxdate}: hits={len(pmids)} 新規候補={len(fresh)}"
          + (f" (上限超過で{dropped}件を次回送り)" if dropped else ""))
    if dry_run:
        for e in fresh:
            print(f"  - {e['pmid']} {e['title'][:80]}")
        print(f"[{slug}] dry-run: 書き込みなし")
        return len(fresh)

    if fresh:
        text = note_path.read_text(encoding="utf-8")
        text = insert_after_anchor(text, "<!-- LN:LOG:START -->", format_log_block(fresh, today))
        text = bump_updated(text, today)
        atomic_write(note_path, text)
        ts["weave_pending"] = True
        if weave:
            woven = weave_note(note_path.read_text(encoding="utf-8"), topic.get("title", slug),
                               runner=lambda p: run_claude(p, cmd=cfg.get("weave_command")))
            if woven is not None:
                atomic_write(note_path, bump_updated(woven, today))
                ts["weave_pending"] = False

    # ログ肥大化ガード: ✅ ブロックを新しい順に max_log_blocks 個残し、あふれは _archive へ
    text = note_path.read_text(encoding="utf-8")
    pruned, overflow = prune_log(text, int(cfg.get("max_log_blocks", 8)))
    if overflow:
        arch = note_path.parent / "_archive" / f"{slug}-log.md"
        arch.parent.mkdir(parents=True, exist_ok=True)
        with arch.open("a", encoding="utf-8") as f:
            f.write(overflow if overflow.endswith("\n") else overflow + "\n")
        atomic_write(note_path, pruned)
        print(f"[{slug}] ログ整理: 古い✅ブロックを {arch.relative_to(ROOT)} へ退避")

    # fetch した分だけ seen に積む。上限超過の積み残しがある間は last_edat を進めない —
    # 窓を進めると積み残しが検索窓の外に落ちて静かに消える (2026-08-07 実走で検出したバグ)
    ts["seen_pmids"] = sorted(seen | {e["pmid"] for e in entries})
    ts["last_run"] = now.isoformat(timespec="seconds")
    if dropped == 0:
        ts["last_edat"] = maxdate
    return len(fresh)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="書き込みなしで新着候補を表示")
    ap.add_argument("--force", action="store_true", help="7日ゲートを無視して今すぐ実行")
    ap.add_argument("--no-weave", action="store_true", help="収集のみ (claude 織りを呼ばない)")
    ap.add_argument("--status", action="store_true", help="保存済みの状態を表示して終了")
    ap.add_argument("--topic", help="このslugのトピックだけ処理")
    ap.add_argument("--sleep", metavar="SLUG", help="トピックを🛏️休眠にする (収集停止、ノートは残る)")
    ap.add_argument("--wake", metavar="SLUG", help="休眠トピックを🟢再稼働する")
    ap.add_argument("--print-weave-prompt", metavar="SLUG",
                    help="織りプロンプトを表示 (任意の AI チャットに貼って手動で織る用)")
    args = ap.parse_args()

    cfg = load_json(CONFIG, {})
    state = load_json(STATE, {})

    if args.print_weave_prompt:
        for t in cfg.get("topics", []):
            if t["slug"] == args.print_weave_prompt:
                note = (ROOT / t["note"]).read_text(encoding="utf-8")
                print(weave_prompt(note, t.get("title", t["slug"])))
                return 0
        print(f"unknown topic: {args.print_weave_prompt}", file=sys.stderr)
        return 1

    if args.sleep or args.wake:
        slug = args.sleep or args.wake
        for t in cfg.get("topics", []):
            if t["slug"] == slug:
                if args.sleep:
                    t["status"] = "dormant"
                    t["since"] = datetime.now().strftime("%Y-%m-%d")
                    print(f"🛏️ {slug} を休眠にしました。ノートはそのまま読めます。再開: --wake {slug}")
                else:
                    t.pop("status", None)
                    t.pop("since", None)
                    print(f"🟢 {slug} を再稼働しました。次の nightly (7日ゲート明け) から収集再開")
                CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                return 0
        print(f"unknown topic: {slug}", file=sys.stderr)
        return 1

    if args.status:
        out = {}
        for t in cfg.get("topics", []):
            s = state.get(t["slug"], {})
            out[t["slug"]] = {
                "稼働": (f"🛏️ 休眠 (since {t.get('since', '?')})"
                        if t.get("status") == "dormant" else "🟢 稼働中"),
                **{k: (f"{len(v)}件" if k == "seen_pmids" else v) for k, v in s.items()},
            }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 0

    topics = cfg.get("topics", [])
    if args.topic:
        topics = [t for t in topics if t["slug"] == args.topic]
        if not topics:
            print(f"unknown topic: {args.topic}", file=sys.stderr)
            return 1

    lib = library_ids(cfg)
    total = 0
    for topic in topics:
        total += process_topic(topic, cfg, state, lib, dry_run=args.dry_run,
                               force=args.force, weave=not args.no_weave)
    if not args.dry_run:
        save_state(state)
    print(f"done: 新規 {total} 件")
    return 0


if __name__ == "__main__":
    sys.exit(main())
