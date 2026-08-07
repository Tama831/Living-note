#!/usr/bin/env python3
"""fulltext_fetch.py — 生きたノートの文献リストから合法 OA 全文を取得してテキスト化する。

設計 (2026-08-07, living-notes 層③「その中から解答」の土台):
- ノート .md から PMID / DOI を抽出 → Unpaywall API で OA 版の所在を引く (合法 OA のみ、
  ペイウォール迂回はしない) → PDF を取得 → pdftotext で .txt 化
- 置き場: data/fulltext/ (**.gitignore 対象** — 全文は著作権物なので repo に push しない。
  ローカル grep + AI セッションでの読解が用途)
- manifest.jsonl に来歴 (doi/pmid/取得元/日時/結果) を記録。再実行は取得済みをスキップ (冪等)

使い方:
    export UNPAYWALL_EMAIL=you@example.com   # 初回のみ (認証ではなく利用者識別)
    python3 scripts/fulltext_fetch.py --note notes/appendicitis.md
    python3 scripts/fulltext_fetch.py --doi 10.7759/cureus.107410
    python3 scripts/fulltext_fetch.py --note ... --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORE = ROOT / "data/fulltext"
MANIFEST = STORE / "manifest.jsonl"
# Unpaywall は利用者特定のため email パラメータを要求する (認証ではない・登録不要)。
# 各自のアドレスを環境変数で: export UNPAYWALL_EMAIL=you@example.com
UNPAYWALL_EMAIL = os.environ.get("UNPAYWALL_EMAIL", "")
UA = "Mozilla/5.0 (Macintosh) living-notes-fulltext/1.0"


def extract_refs(note_text: str) -> list[dict]:
    """ノート .md の各行から PMID / DOI を対で拾う (行内に共起する前提の文献リスト形式)。"""
    refs, seen = [], set()
    for line in note_text.splitlines():
        pmid_m = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", line)
        doi_m = re.search(r"doi\.org/(10\.[^)\s]+)", line)
        if not pmid_m and not doi_m:
            continue
        # DOI は case-insensitive — 小文字に正規化しないと大文字違いが dedupe をすり抜ける
        doi = (doi_m.group(1) if doi_m else "").rstrip(".,;").lower()
        pmid = pmid_m.group(1) if pmid_m else ""
        key = doi or f"pmid:{pmid}"
        if key in seen:
            continue
        seen.add(key)
        refs.append({"pmid": pmid, "doi": doi})
    return refs


def doi_slug(doi: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", doi)


def unpaywall_lookup(doi: str) -> dict | None:
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  [unpaywall] {doi}: {e}", file=sys.stderr)
        return None


def download(url: str, dest: Path) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
    except Exception as e:
        print(f"  [download] {url[:80]}: {e}", file=sys.stderr)
        return False
    if not data.startswith(b"%PDF"):
        print(f"  [download] PDF でない応答 (HTML壁の可能性): {url[:80]}", file=sys.stderr)
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return True


def pdf_to_text(pdf: Path, txt: Path) -> bool:
    r = subprocess.run(["pdftotext", str(pdf), str(txt)], capture_output=True, text=True)
    if r.returncode != 0 or not txt.exists() or txt.stat().st_size < 500:
        print(f"  [pdftotext] failed/too-short: {pdf.name}", file=sys.stderr)
        return False
    return True


def log_manifest(entry: dict) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def fetch_one(ref: dict, dry_run: bool) -> str:
    """戻り値: 'ok' | 'exists' | 'no_oa' | 'failed' | 'no_doi'"""
    doi, pmid = ref.get("doi", ""), ref.get("pmid", "")
    if not doi:
        return "no_doi"
    slug = doi_slug(doi)
    txt = STORE / f"{slug}.txt"
    if txt.exists():
        return "exists"
    up = unpaywall_lookup(doi)
    time.sleep(1.0)
    loc = (up or {}).get("best_oa_location") or {}
    pdf_url = loc.get("url_for_pdf") or ""
    if not pdf_url:
        return "no_oa"
    if dry_run:
        print(f"  [dry-run] would fetch {doi} <- {pdf_url[:80]}")
        return "ok"
    pdf = STORE / "pdf" / f"{slug}.pdf"
    if not download(pdf_url, pdf):
        return "failed"
    if not pdf_to_text(pdf, txt):
        return "failed"
    log_manifest({"doi": doi, "pmid": pmid, "source_url": pdf_url,
                  "license": loc.get("license") or "", "txt": str(txt.relative_to(ROOT)),
                  "fetched_at": datetime.now().isoformat(timespec="seconds")})
    print(f"  [ok] {doi} -> {txt.name} ({txt.stat().st_size // 1000}KB)")
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--note", help="生きたノート .md から文献を抽出して一括取得")
    ap.add_argument("--doi", action="append", default=[], help="単発 DOI (複数可)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not UNPAYWALL_EMAIL:
        print("UNPAYWALL_EMAIL が未設定です: export UNPAYWALL_EMAIL=you@example.com\n"
              "(Unpaywall API の利用者識別に使われるだけで、登録や認証は不要です)", file=sys.stderr)
        return 1

    refs: list[dict] = [{"pmid": "", "doi": d} for d in args.doi]
    if args.note:
        refs += extract_refs((ROOT / args.note).read_text(encoding="utf-8"))
    if not refs:
        print("nothing to fetch (--note か --doi を指定)", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    for ref in refs:
        status = fetch_one(ref, args.dry_run)
        counts[status] = counts.get(status, 0) + 1
    print(f"done: {counts} (合法OAのみ。no_oa はペイウォール内 = 取得しない)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
