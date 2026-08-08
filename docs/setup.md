# Setup — for people who run it themselves

> 🇯🇵 日本語版: [setup.ja.md](setup.ja.md)
>
> Physical requirements, the operational schedule, and weaver LLM options with real billing facts
> and measurements live in [operations.md](operations.md).

## What you need

- Python 3.10+ (no dependencies — standard library only)
- To automate the weave (the AI rewrite of the note): an LLM CLI
  - Default: the `claude` command from [Claude Code](https://claude.com/claude-code)
  - Swap in any CLI via `"weave_command"` in the config (e.g. `["gemini", "-p"]`)
  - **Works without one** — run collection with `--no-weave` and weave manually (below)
- For the full-text layer: `pdftotext` (macOS: `brew install poppler` / Ubuntu: `apt install poppler-utils`)

## Initial configuration

```bash
cp config/living-notes.example.json config/living-notes.json
cp notes/template.md notes/appendicitis.md   # file name should match the slug
```

Edit `config/living-notes.json`:

| Key | Meaning |
|---|---|
| `topics[].slug` | topic identifier (lowercase, hyphens) |
| `topics[].queries` | PubMed query. Tags like `[Title]` and `systematic[sb]` work |
| `topics[].note` | note path (repo-relative) |
| `interval_days` | run-interval gate (default 7 — call it daily, it works weekly) |
| `initial_lookback_days` | how far the first run looks back (default 180) |
| `max_per_run` | per-run intake cap. Overflow is never lost — it carries to the next run |
| `dedupe_sources` | your reference lists (.bib / .jsonl). Drop a Paperpile/Zotero export here and papers you already own are never re-imported; also feeds library mode |
| `topics[].mode` | `latest` (default, PubMed arrivals) / `library` (only your own collection) / `both`. See README "Connect your reference manager" |
| `topics[].library_query` | what to pick from your library (regex over titles + keywords). Write it in English for English-language papers |
| `topics[].lang` | `ja` (default) / `en` — `en` uses `notes/template.md` conventions and switches the weave prompt and log labels to English |
| `library_sources` | only if you want library-mode sources separate from dedupe (defaults to dedupe_sources) |
| `weave_command` | weaver LLM CLI (default: `claude -p`) |

## Running

```bash
python3 scripts/living_notes_update.py --dry-run --force   # rehearsal: see what would be collected
python3 scripts/living_notes_update.py --force             # first real run (collect + weave)
python3 scripts/living_notes_update.py --status            # state check
```

### Weaving manually (no LLM CLI)

```bash
python3 scripts/living_notes_update.py --force --no-weave        # collection only
python3 scripts/living_notes_update.py --print-weave-prompt appendicitis
```

Paste the printed prompt into ChatGPT / Claude / Gemini and overwrite the note with the returned
Markdown — that *is* the weave.

### Pausing and resuming

```bash
python3 scripts/living_notes_update.py --sleep appendicitis   # 🛏️ stop collecting (the note remains)
python3 scripts/living_notes_update.py --wake appendicitis    # 🟢 resume
```

## Scheduling

The script carries its own 7-day gate, so **calling it once a day** gives you weekly operation.

**Linux (cron)**:
```
30 21 * * * cd /path/to/living-note && python3 scripts/living_notes_update.py >> ~/living-note.log 2>&1
```

**macOS (launchd)** — `~/Library/LaunchAgents/com.example.living-note.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.example.living-note</string>
  <key>ProgramArguments</key><array>
    <string>/usr/bin/python3</string>
    <string>/path/to/living-note/scripts/living_notes_update.py</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>21</integer><key>Minute</key><integer>30</integer></dict>
  <key>StandardOutPath</key><string>/tmp/living-note.log</string>
  <key>StandardErrorPath</key><string>/tmp/living-note.log</string>
</dict></plist>
```
```bash
launchctl load ~/Library/LaunchAgents/com.example.living-note.plist
```

## Full-text layer (optional)

Fetches **legal open-access versions only** of the papers in a note's bibliography and converts
them to text. No paywall circumvention.

```bash
export UNPAYWALL_EMAIL=you@example.com   # Unpaywall API user identification (no signup, no auth)
python3 scripts/fulltext_fetch.py --note notes/appendicitis.md
```

Texts accumulate in `data/fulltext/` (**gitignored** — copyrighted content never gets pushed to a
public repo) for grep and AI-session reading — "answers from my own corpus".
Rule of thumb: 30–70% of recent papers are retrievable as OA, depending on the field.

## Tests

```bash
python3 -m pytest tests/ -q   # 24 tests, no network required
```

pytest is the only piece outside the standard library (not needed for the pipeline itself):
macOS `pip3 install pytest` / Debian & Ubuntu `sudo apt install python3-pytest`

## Verification note (2026-08-07)

This document was reproduced end-to-end on a clean Debian 12 LXC: apt prerequisites → clone →
tests → dry run → `--no-weave` collection → cron registration (real firing confirmed) →
`weave_command` swap. Weavers verified: claude (default) and a Gemini wrapper. The fail-soft
path — weave pending (⏳) while collection continues in an LLM-less environment — was also
observed in practice.
