# Design notes — why this shape

> 🇯🇵 日本語版: [design.ja.md](design.ja.md)

## The two wishes this started from

> "I want to declare an interest area and have related papers collect themselves, get re-woven
> into one cross-cutting summary whenever something new arrives, updated on a schedule — a
> **living note**. With a short summary at the top."

> "A service where I can just dump paper PDFs and AI organizes them and answers from them — like
> NotebookLM, but without being split into notebooks."

## Prior-art survey (14 tools, as of 2026-08)

No existing tool satisfied all four conditions at once — **autonomous collection / continuous
re-synthesis into a single note / Q&A over a personal corpus / tolerance for casually dumped
PDFs**.

| Tool family | Autonomous collection | Continuous re-synthesis | Corpus Q&A | PDF dump |
|---|---|---|---|---|
| Scholar / PubMed alerts | ✅ | ❌ (a growing list arrives) | ❌ | ❌ |
| Elicit (Alerts + Notebooks) | ✅ | ⚠️ integration is manual | ✅ | ✅ |
| LivingMeta | ✅ | ✅ | ✅ | ❌ (field-level, no personal PDFs) |
| NotebookLM / Gemini Notebook | ❌ | ❌ | ✅ (within one notebook) | ✅ |
| PaperQA2 / Zotero+GPT / SciSpace | ❌ | ❌ | ✅ | ✅ |
| ResearchRabbit / Litmaps | ✅ | ❌ | ❌ | ❌ |
| Living-systematic-review tooling (RobotReviewer etc.) | ✅ | ✅ | ❌ | ❌ (team-scale, heavyweight) |

NotebookLM in particular remains **siloed per notebook** in 2026 — "the version without notebook
walls" cannot be built inside it. Living-note answers the wish from the opposite direction:
**one corpus as a single pool, with notes as views onto it**.

## Architectural choices

### Why Markdown with HTML-comment anchors
- A note is simultaneously a human document, a machine-edit target, and an LLM-rewrite target.
  The smallest structure where those three don't collide turned out to be "eight anchor comments
  placed outside the headings"
- `<!-- LN:SUMMARY/SYNTHESIS/BIB/LOG:START/END -->` — the machine only appends inside LOG; the
  LLM rewrites everything but is **checked by a validation gate for anchor preservation** before
  its output is accepted
- Output that fails validation is discarded and the collected log survives (fail-soft). Never
  trust AI output before verifying it.

### Why bare PubMed E-utilities HTTP
- Keyless, no auth, stdlib-only → runs as-is in thin cron/launchd environments
- Depending on MCP servers or SDKs invites silent no-ops in headless contexts (a lesson from
  real measurements)

### Why the window never advances past a backlog (no silent loss)
- Overflow beyond the per-run cap (max_per_run) carries to the next run. If the search window
  (last_edat) advanced anyway, the overflow would fall outside the window and **silently
  disappear** — a real bug caught during first-day live verification, fixed as the rule "the
  window stays put while a backlog remains"
- Silent gaps corrode trust in a list. "Not losing things" is this tool's reason to exist.

### Why legal OA only
- Full texts come exclusively from Unpaywall's `best_oa_location`. No paywall circumvention
  (no Sci-Hub)
- A tool clinicians can hand to colleagues in the open needs legitimacy of acquisition as a
  functional requirement

### Why no vector database
- The full text of a personal library (hundreds to a thousand papers) is tens of megabytes —
  **grep finishes instantly at this scale**
- "Grep to locate, then let the LLM read the matching files" delivers PaperQA2-style cited answers,
  confirmed in practice (a pregnancy-imaging question answered from fetched full texts)
- Embeddings, indexes and their sync costs are not paid until scale demands them

### Why letting go loses nothing
- Interests drift. When stopping is expensive, people either hoard or discard with guilt
- `--sleep` stops only collection; the note lives on as a document. Resuming is one word
  (`--wake`). Tasks close; notes stay open.

## Room to grow (not yet built)

- Collectors beyond PubMed (arXiv / medRxiv / conference abstracts) — same esearch/efetch shape
- Full-text retry for 403-ing publishers, PMC fallback
- Automatic topic routing for dumped PDFs
- Cross-links between notes (a single corpus makes cross-topic references natural)
