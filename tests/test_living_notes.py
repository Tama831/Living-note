"""living_notes_update.py の unit tests (2026-08-07)。

外部 I/O (E-utilities / claude -p) は monkeypatch で断ち、
アンカー編集・dedupe・ゲート・XMLパース・weave検証・dry-run 無書き込みを検証する。
"""
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import living_notes_update as ln


def make_note(updated: str = "2026-01-01") -> str:
    return (
        "---\n"
        f"topic: テスト\nslug: t\nupdated: {updated}\n"
        "---\n\n"
        "# 🌱 生きたノート: テスト\n\n"
        "## 📌 5行サマリ\n<!-- LN:SUMMARY:START -->\n- 要点\n<!-- LN:SUMMARY:END -->\n\n"
        "## 🧵 横断まとめ\n<!-- LN:SYNTHESIS:START -->\n### 診断\n本文\n<!-- LN:SYNTHESIS:END -->\n\n"
        "## 📚 文献リスト (蔵書)\n<!-- LN:BIB:START -->\n1. 既存文献\n<!-- LN:BIB:END -->\n\n"
        "## 🆕 新着ログ\n<!-- LN:LOG:START -->\n### ✅ 2025-12-01 収集分 (1件・織り待ち)\n- 旧新着\n<!-- LN:LOG:END -->\n"
    )


SAMPLE_XML = """<?xml version="1.0"?>
<PubmedArticleSet>
 <PubmedArticle>
  <MedlineCitation>
   <PMID Version="1">12345678</PMID>
   <Article>
    <Journal>
      <ISOAbbreviation>N Engl J Med</ISOAbbreviation>
      <Title>The New England Journal of Medicine</Title>
      <JournalIssue><PubDate><Year>2026</Year></PubDate></JournalIssue>
    </Journal>
    <ArticleTitle>Appendicitis in the era of <i>antibiotics</i>-first.</ArticleTitle>
    <Abstract>
      <AbstractText Label="BACKGROUND">Part one.</AbstractText>
      <AbstractText Label="METHODS">Part two.</AbstractText>
    </Abstract>
    <AuthorList>
      <Author><LastName>Smith</LastName><Initials>J</Initials></Author>
      <Author><CollectiveName>CODA Group</CollectiveName></Author>
    </AuthorList>
   </Article>
  </MedlineCitation>
  <PubmedData>
    <ArticleIdList>
      <ArticleId IdType="pubmed">12345678</ArticleId>
      <ArticleId IdType="doi">10.1000/TEST.1</ArticleId>
    </ArticleIdList>
    <ReferenceList>
      <Reference>
        <ArticleIdList><ArticleId IdType="doi">10.9999/SOMEONE.ELSES.PAPER</ArticleId></ArticleIdList>
      </Reference>
    </ReferenceList>
  </PubmedData>
 </PubmedArticle>
 <PubmedArticle>
  <MedlineCitation>
   <PMID>99999999</PMID>
   <Article>
    <Journal>
      <Title>Plain Journal</Title>
      <JournalIssue><PubDate><MedlineDate>2025 Jan-Feb</MedlineDate></PubDate></JournalIssue>
    </Journal>
    <ArticleTitle>Plain title without markup</ArticleTitle>
   </Article>
  </MedlineCitation>
 </PubmedArticle>
</PubmedArticleSet>
"""


# ── XML パース ──────────────────────────────────────────────

def test_parse_efetch_xml_fields():
    arts = ln.parse_efetch_xml(SAMPLE_XML)
    assert len(arts) == 2
    a = arts[0]
    assert a["pmid"] == "12345678"
    assert a["title"] == "Appendicitis in the era of antibiotics-first."
    assert a["journal"] == "N Engl J Med"
    assert a["year"] == "2026"
    assert a["authors"] == ["Smith J", "CODA Group"]
    assert a["abstract"] == "Part one. Part two."
    assert a["doi"] == "10.1000/test.1"  # 小文字化 + 参考文献のDOIに汚染されない (10/23件化けた実害バグのregression)


def test_parse_efetch_xml_childless_title_not_dropped():
    # Element は子要素ゼロで falsy になる罠の regression test
    b = ln.parse_efetch_xml(SAMPLE_XML)[1]
    assert b["title"] == "Plain title without markup"
    assert b["year"] == "2025"  # MedlineDate フォールバック
    assert b["doi"] == ""


# ── アンカー編集 ────────────────────────────────────────────

def test_insert_after_anchor_newest_first():
    text = make_note()
    out = ln.insert_after_anchor(text, "<!-- LN:LOG:START -->", "### ⏳ 2026-08-07 収集分\n- 新規\n")
    start = out.index("<!-- LN:LOG:START -->")
    assert out.index("### ⏳ 2026-08-07", start) < out.index("### ✅ 2025-12-01", start)
    assert out.count("<!-- LN:LOG:START -->") == 1


def test_insert_after_anchor_missing_raises():
    try:
        ln.insert_after_anchor("no anchors here\n", "<!-- LN:LOG:START -->", "x")
        assert False, "should raise"
    except ValueError:
        pass


def test_bump_updated_only_frontmatter():
    text = make_note("2026-01-01") + "\nupdated: 9999-99-99 (本文中の偽物)\n"
    out = ln.bump_updated(text, "2026-08-07")
    assert "updated: 2026-08-07" in out
    assert "updated: 9999-99-99" in out  # count=1 なので本文側は無傷


# ── dedupe / ゲート ─────────────────────────────────────────

def test_filter_new_drops_seen_and_library():
    entries = [
        {"pmid": "1", "doi": "10.1/a"},
        {"pmid": "2", "doi": "10.1/b"},
        {"pmid": "3", "doi": ""},
        {"pmid": "4", "doi": "10.1/d"},
    ]
    lib = {"doi:10.1/b", "pmid:3"}
    fresh = ln.filter_new(entries, seen_pmids={"1"}, lib=lib)
    assert [e["pmid"] for e in fresh] == ["4"]


def test_should_run_gate():
    now = datetime(2026, 8, 7, 12, 0)
    assert ln.should_run({}, 7, force=False, now=now)  # 初回
    recent = {"last_run": "2026-08-05T00:00:00"}
    assert not ln.should_run(recent, 7, force=False, now=now)
    assert ln.should_run(recent, 7, force=True, now=now)
    old = {"last_run": "2026-07-01T00:00:00"}
    assert ln.should_run(old, 7, force=False, now=now)


# ── ログブロック整形 ────────────────────────────────────────

def test_format_log_block_links_and_snippet():
    e = {"pmid": "42", "doi": "10.1/x", "title": "T", "authors": ["A B", "C D", "E F", "G H"],
         "journal": "J", "year": "2026", "abstract": "x" * 400}
    block = ln.format_log_block([e], "2026-08-07")
    assert "### ⏳ 2026-08-07 収集分 (1件・織り待ち)" in block
    assert "https://pubmed.ncbi.nlm.nih.gov/42/" in block
    assert "https://doi.org/10.1/x" in block
    assert "et al." in block
    assert ("x" * 300 + "…") in block and ("x" * 301) not in block


# ── weave 検証 ──────────────────────────────────────────────

def test_weave_note_rejects_missing_anchor_and_errors():
    note = make_note()
    assert ln.weave_note(note, "T", runner=lambda p: "アンカーの無い出力") is None
    def boom(p):
        raise RuntimeError("claude down")
    assert ln.weave_note(note, "T", runner=boom) is None


def test_weave_note_accepts_valid_and_strips_fence():
    note = make_note()
    woven_body = note.replace("- 要点", "- 更新された要点")
    fenced = "```markdown\n" + woven_body + "\n```"
    out = ln.weave_note(note, "T", runner=lambda p: fenced)
    assert out is not None
    assert "更新された要点" in out
    assert not out.startswith("```")
    for a in ln.ANCHORS:
        assert a in out


# ── 稼働制御 / ログ肥大化ガード ─────────────────────────────

def _note_with_log(blocks: str) -> str:
    base = make_note()
    line_end = base.index("\n", base.index("<!-- LN:LOG:START -->")) + 1
    j = base.index("<!-- LN:LOG:END -->")
    return base[:line_end] + blocks + base[j:]


def test_prune_log_keeps_newest_and_pending():
    blocks = ""
    for d in range(10, 4, -1):  # ✅ 10日..5日 (新しい順)
        blocks += f"### ✅ 2026-01-{d:02d} 収集分 (1件・編み込み済み)\n- item{d}\n\n"
    blocks += "### ⏳ 2026-01-04 収集分 (1件・織り待ち)\n- pending\n\n"
    blocks += "### ✅ 2026-01-03 収集分 (1件・編み込み済み)\n- item3\n\n"
    blocks += "### ✅ 2026-01-02 収集分 (1件・編み込み済み)\n- item2\n\n"
    text = _note_with_log(blocks)
    pruned, overflow = ln.prune_log(text, keep=6)
    # ✅は計8個 → 新しい6個が残り、古い2個 (01-03, 01-02) があふれる
    assert "2026-01-03" in overflow and "2026-01-02" in overflow
    assert "2026-01-03" not in pruned and "2026-01-02" not in pruned
    assert "⏳ 2026-01-04" in pruned  # 織り待ちは keep に関係なく残る
    for a in ln.ANCHORS:
        assert a in pruned
    # あふれ無しなら無変更
    same, none = ln.prune_log(pruned, keep=6)
    assert same == pruned and none == ""


def test_process_topic_dormant_skips_without_fetch(monkeypatch, tmp_path):
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    topic["status"] = "dormant"

    def boom(*a, **k):
        raise AssertionError("dormant 中に fetch してはいけない")
    monkeypatch.setattr(ln, "esearch", boom)
    before = note.read_text(encoding="utf-8")
    n = ln.process_topic(topic, cfg, {}, lib=set(), dry_run=False, force=True, weave=False)
    assert n == 0
    assert note.read_text(encoding="utf-8") == before


# ── process_topic (E2E, 外部I/Oはfake) ──────────────────────

def _fake_fetchers(monkeypatch, hits, articles):
    monkeypatch.setattr(ln, "esearch", lambda q, mindate, maxdate, retmax=100: list(hits))
    monkeypatch.setattr(ln, "efetch", lambda pmids: [a for a in articles if a["pmid"] in pmids])


def _topic_env(monkeypatch, tmp_path):
    monkeypatch.setattr(ln, "ROOT", tmp_path)
    note = tmp_path / "note.md"
    note.write_text(make_note(), encoding="utf-8")
    topic = {"slug": "t", "title": "テスト", "queries": ["q"], "note": "note.md"}
    cfg = {"interval_days": 7, "initial_lookback_days": 30, "max_per_run": 25}
    return topic, cfg, note


ARTICLES = [
    {"pmid": "111", "doi": "10.1/aaa", "title": "New paper one", "authors": ["A B"],
     "journal": "J1", "year": "2026", "abstract": "abs one"},
    {"pmid": "222", "doi": "", "title": "New paper two", "authors": [],
     "journal": "J2", "year": "2026", "abstract": ""},
]


def test_process_topic_dry_run_writes_nothing(monkeypatch, tmp_path):
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    _fake_fetchers(monkeypatch, ["111", "222"], ARTICLES)
    before = note.read_text(encoding="utf-8")
    state = {}
    n = ln.process_topic(topic, cfg, state, lib=set(), dry_run=True, force=True, weave=False)
    assert n == 2
    assert note.read_text(encoding="utf-8") == before
    assert "seen_pmids" not in state.get("t", {})


def test_process_topic_real_run_then_idempotent(monkeypatch, tmp_path):
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    _fake_fetchers(monkeypatch, ["111", "222"], ARTICLES)
    state = {}
    n1 = ln.process_topic(topic, cfg, state, lib=set(), dry_run=False, force=True, weave=False)
    assert n1 == 2
    text = note.read_text(encoding="utf-8")
    assert "New paper one" in text and "New paper two" in text
    assert "updated: " in text and "updated: 2026-01-01" not in text
    assert state["t"]["seen_pmids"] == ["111", "222"]
    assert state["t"]["weave_pending"] is True
    # 2周目: 同じヒットなら何も増えない (冪等)
    n2 = ln.process_topic(topic, cfg, state, lib=set(), dry_run=False, force=True, weave=False)
    assert n2 == 0
    assert note.read_text(encoding="utf-8") == text


def test_process_topic_backlog_keeps_window_open(monkeypatch, tmp_path):
    # max_per_run 超過の積み残しがある間は last_edat を進めない (積み残し消失バグの regression)
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    cfg["max_per_run"] = 1
    _fake_fetchers(monkeypatch, ["111", "222"], ARTICLES)
    state = {}
    n1 = ln.process_topic(topic, cfg, state, lib=set(), dry_run=False, force=True, weave=False)
    assert n1 == 1
    assert "last_edat" not in state["t"]  # 窓は開いたまま
    n2 = ln.process_topic(topic, cfg, state, lib=set(), dry_run=False, force=True, weave=False)
    assert n2 == 1  # 積み残しが同じ窓で回収される
    assert "last_edat" in state["t"]  # 全部さばけたので窓が進む
    text = note.read_text(encoding="utf-8")
    assert "New paper one" in text and "New paper two" in text


def test_process_topic_respects_library_dedupe(monkeypatch, tmp_path):
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    _fake_fetchers(monkeypatch, ["111", "222"], ARTICLES)
    state = {}
    n = ln.process_topic(topic, cfg, state, lib={"doi:10.1/aaa"}, dry_run=False, force=True, weave=False)
    assert n == 1  # 111 は蔵書済み扱い
    text = note.read_text(encoding="utf-8")
    assert "New paper one" not in text and "New paper two" in text
    # 蔵書済みでも seen には積む (次回以降 fetch し直さない)
    assert state["t"]["seen_pmids"] == ["111", "222"]


# ── 蔵書モード ──────────────────────────────────────────────

BIB_SAMPLE = """
@ARTICLE{Talan2021-hm,
  title   = {Treatment of acute uncomplicated appendicitis},
  author  = {Talan, David A and Di Saverio, Salomone},
  journal = {The New England Journal of Medicine},
  year    = 2021,
  doi     = {10.1056/NEJMcp2107675},
  pmid    = 34525287,
  keywords = {appendix}
}

@ARTICLE{Other2020-x,
  title   = {Completely unrelated cardiology paper},
  author  = {Someone, Else},
  journal = {J Unrelated},
  year    = 2020,
  doi     = {10.1/xyz}
}
"""


def test_parse_bib_entries_fields():
    es = ln.parse_bib_entries(BIB_SAMPLE)
    assert len(es) == 2
    a = es[0]
    assert a["title"] == "Treatment of acute uncomplicated appendicitis"
    assert a["doi"] == "10.1056/nejmcp2107675"  # 小文字化
    assert a["pmid"] == "34525287"
    assert a["authors"][0] == "Talan, David A"
    assert a["year"] == "2021"


def test_library_mode_seeds_from_bib_and_is_idempotent(monkeypatch, tmp_path):
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    (tmp_path / "lib.bib").write_text(BIB_SAMPLE, encoding="utf-8")
    cfg["dedupe_sources"] = ["lib.bib"]
    topic["mode"] = "library"
    topic["library_query"] = "appendicitis|appendix"

    def boom(*a, **k):
        raise AssertionError("library モードで PubMed を呼んではいけない")
    monkeypatch.setattr(ln, "esearch", boom)
    state = {}
    n1 = ln.process_topic(topic, cfg, state, lib=set(), dry_run=False, force=True, weave=False)
    assert n1 == 1  # マッチは appendicitis の1本だけ
    text = note.read_text(encoding="utf-8")
    assert "Treatment of acute uncomplicated appendicitis" in text
    assert "蔵書より" in text
    assert "Completely unrelated" not in text
    n2 = ln.process_topic(topic, cfg, state, lib=set(), dry_run=False, force=True, weave=False)
    assert n2 == 0  # 蔵書の再スキャンで増えない (冪等)


def test_format_log_block_without_pmid():
    e = {"pmid": "", "doi": "10.1/x", "title": "T", "authors": ["A"],
         "journal": "J", "year": "2020", "abstract": ""}
    block = ln.format_log_block([e], "2026-08-07", source="蔵書より")
    assert "pubmed.ncbi.nlm.nih.gov" not in block
    assert "doi.org/10.1/x" in block
    assert "蔵書より" in block


def test_note_contents_count_as_seen(monkeypatch, tmp_path):
    # fresh clone (state無し) でも、ノートに既に載っている論文は再収集しない
    topic, cfg, note = _topic_env(monkeypatch, tmp_path)
    text = note.read_text(encoding="utf-8")
    text = text.replace(
        "1. 既存文献",
        "1. 既存A PMID [111](https://pubmed.ncbi.nlm.nih.gov/111/)\n"
        "2. 既存B [DOI](https://doi.org/10.1/AAA)",
    )
    note.write_text(text, encoding="utf-8")
    articles = ARTICLES + [{"pmid": "333", "doi": "10.1/aaa", "title": "Doi dup", "authors": [],
                            "journal": "J", "year": "2026", "abstract": ""}]
    _fake_fetchers(monkeypatch, ["111", "222", "333"], articles)
    n = ln.process_topic(topic, cfg, {}, lib=set(), dry_run=False, force=True, weave=False)
    assert n == 1  # 111 は PMID で、333 は DOI でノート済み → 追加は 222 のみ
    out = note.read_text(encoding="utf-8")
    assert "New paper two" in out and "New paper one" not in out and "Doi dup" not in out
