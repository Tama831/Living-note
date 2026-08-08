---
name: living-note
description: Operate Living-note living literature notes. Triggers - "make a living note for X", "ask the notes", "update the notes", "put the X note to sleep / wake it". Handles topic creation, PubMed collection + weave runs, cited Q&A over notes and the full-text store, and pause/resume.
---

# living-note — operating the living notes

This skill defines operations inside the Living-note repository (this repository).
All paths are repo-root relative.

## Intents

### "Make a living note for TOPIC"
1. Pick a slug (lowercase, hyphens). Copy `notes/template.md` (English) or
   `notes/template.ja.md` (Japanese) to `notes/<slug>.md`
2. Fill in the frontmatter (topic/slug/lang) and title
3. Add {slug, title, queries, note, lang} to `topics` in `config/living-notes.json`.
   Discuss the query with the user (too broad = noise, too narrow = silence; a good start:
   `<topic>[Title] AND (systematic[sb] OR guideline[pt] OR randomized controlled trial[pt] OR review[pt])`)
4. First run: `python3 scripts/living_notes_update.py --topic <slug> --force`
5. Report briefly: how many papers landed, and the summary

### "Update the notes"
`python3 scripts/living_notes_update.py --force` (all topics) or `--topic <slug>`.
Afterwards report only the arrival count and what changed in the five-line summary.

### "Ask the notes" / "What do we know about X?"
1. Read the relevant note's 📌 summary and 🧵 synthesis first
2. If more depth is needed, grep `data/fulltext/*.txt` and read the matching passages
   (if no full text exists, offer `python3 scripts/fulltext_fetch.py --note notes/<slug>.md`)
3. **Always answer with sources (PMID/DOI links).** Never fill gaps from your own knowledge —
   if the corpus doesn't cover it, say so
4. For medical content, add: clinical decisions belong with the original papers and treating clinicians

### "Put the X note to sleep" / "Wake it"
`--sleep <slug>` / `--wake <slug>`. When sleeping, always mention the note remains readable.

### "Fetch the full texts"
Requires `export UNPAYWALL_EMAIL=...` (ask the user if unset).
`python3 scripts/fulltext_fetch.py --note notes/<slug>.md`.
Legal OA only — report unfetched papers as "paywalled (a legitimate limit)".

## Principles

- Hand-editing notes is fine, but never delete the 8 `<!-- LN:...-->` anchors (machine-edit markers)
- Keep reports short: counts, what changed, and the one paper worth reading next
- Never create silent gaps — surface what was dropped, and what the corpus doesn't contain
