"""fulltext_fetch.py の unit tests (2026-08-07)。ネットワークは触らない。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import fulltext_fetch as ff


def test_extract_refs_pairs_and_dedupes_case_insensitive():
    note = (
        "1. **A.** PMID [111](https://pubmed.ncbi.nlm.nih.gov/111/) / [DOI](https://doi.org/10.1/AAA)\n"
        "2. **B.** PMID [222](https://pubmed.ncbi.nlm.nih.gov/222/)\n"
        "- log line duplicate: [DOI](https://doi.org/10.1/aaa)\n"
        "3. 素のテキスト行 (リンクなし)\n"
    )
    refs = ff.extract_refs(note)
    assert refs == [{"pmid": "111", "doi": "10.1/aaa"}, {"pmid": "222", "doi": ""}]


def test_doi_slug_safe_chars():
    assert ff.doi_slug("10.1007/s00423-026-04113-3") == "10.1007_s00423-026-04113-3"
    assert "/" not in ff.doi_slug("10.1017/S0029665126105047")
