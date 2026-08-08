# Operations in practice

> 🇯🇵 日本語版: [operations.ja.md](operations.ja.md)

What the README and [setup.md](setup.md) don't tell you: what you physically need, what actually
runs and when, and which weaver LLMs make weekly operation realistic. This is the last layer of
"assumptions that only existed in the author's environment", written down.

## 1. Physical requirements

Collection is stdlib-only HTTP against PubMed — **a Raspberry Pi-class machine is enough**. If the
weave is delegated to a cloud LLM CLI, no local compute is needed at all; if you run a local LLM,
the requirements are whatever that model needs (see §4 for a measured example). **Always-on is not
required**: the machine only needs to be awake when the daily cron/launchd tick happens to land,
and a missed tick self-heals (§2).

## 2. What actually runs, and when

The scheduler calls the script **once a day**; the built-in 7-day gate means it actually works
**once a week** per topic — measured at ~30 seconds of collection plus a few minutes of weaving
(4–7 min with `claude -p`, ~5 min with the Gemini wrapper, on 2026-08-07 runs). If the machine is
asleep at tick time, that day is simply skipped and the next day's tick picks it up — the gate
compares against `last_run`, so nothing breaks and nothing is lost.

**Real-time obligations are close to zero by design.** The honest full list:

1. **Monthly-ish**: check that your LLM CLI login hasn't expired (a dead weaver degrades
   gracefully — ⏳ entries accumulate, nothing is lost, but nothing gets woven either)
2. **Only if you use library integration**: re-export your .bib occasionally after adding papers (optional)
3. **If ⏳ entries linger** in a note: run a manual weave (`--print-weave-prompt` → paste into any AI chat)

## 3. Weaver requirements & options (as of 2026-08)

A weaver LLM needs three things:

1. **Headless execution** — prompt as an argument, full output to stdout
2. **Long input/output** — the full note (30–60 KB) goes in, a full note comes out
3. **Flat-rate plan coverage, or free/local** — weekly weaves on metered billing are technically
   fine but psychologically corrosive; a weaver that rides an existing subscription (or runs free
   locally) is what makes "leave it alone" real

| Weaver | Billing | Headless | Status |
|---|---|---|---|
| **Claude Code `claude -p`** (default) | flat-rate within Pro/Max plans | ✅ | ✅ **verified** — default weaver, all samples woven with it |
| **Gemini API wrapper** (~30-line script) | metered API key. Measured weave = 30–60 KB prompt + full-note output; at Aug-2026 flash-tier list prices ($0.10–1.50 /M input, $0.40–7.50 /M output)¹ that is roughly **$0.01–0.10 per weave** | ✅ | ✅ **verified** (2026-08-07, `gemini-flash-latest`) |
| Gemini CLI | ⚠️ free & AI-Pro/Ultra serving **discontinued 2026-06-18**; now enterprise Code Assist seats or metered API key only² | ✅ | ❌ not tested |
| OpenAI Codex CLI | flat-rate within ChatGPT plans (CLI included on all tiers incl. Free/Go/Plus, shares the plan's usage limits)³ | ✅ (`codex exec`) | ❌ not tested |
| **Ollama local (Gemma)** | free, local | ⚠️ HTTP API wrapper required — bare `ollama run` pollutes stdout | ⚠️ **verified for small notes only** (163 s on CPU), full-size unproven — see §4 |

Sources (checked 2026-08-08):
¹ [Gemini API flash-tier pricing](https://www.aipricing.guru/google-ai-pricing/) ([alt](https://pricepertoken.com/pricing-page/model/google-gemini-3.5-flash))
² [Gemini CLI pricing changes](https://www.tembo.io/blog/gemini-cli-pricing) ([alt](https://nerova.ai/costs-roi/gemini-cli-pricing-explained-2026))
³ [Codex rate card (OpenAI Help)](https://help.openai.com/en/articles/20001106-codex-rate-card) ([alt](https://www.cloudzero.com/blog/openai-codex-pricing/))

"Not tested" means exactly that: it should satisfy the three requirements on paper, but we have
not run a weave through it.

## 4. Local LLM, measured: Gemma

**Setup**: Ollama on a CPU-only Proxmox LXC (8 cores of an AMD Ryzen 7 6800H, 7 GB RAM), model
`gemma4:e4b-it-qat` (6.1 GB quantized). **Fair-sized input**: a small note (2.4 KB — 1 bibliography
entry, short synthesis) plus 3 new arrivals with abstracts; weave prompt 2.8 KB total.

**Result (measured 2026-08-08)** — two attempts, honestly reported:

| Attempt | Plumbing | Time | Validation gate |
|---|---|---|---|
| 1 | `ollama run` CLI, stdout redirected | 292 s | ❌ **FAIL** — stdout contained a "Thinking..." reasoning preamble and terminal control sequences, so the output did not begin with the note's frontmatter. Correctly rejected; nothing was lost |
| 2 | Ollama HTTP API (`/api/generate`, `stream:false`, `think:false`) | **163 s** (1,509 output tokens) | ✅ **PASS** — 8/8 anchors preserved, valid frontmatter, the 3 arrivals correctly woven into summary and synthesis, ⏳→✅ |

**Conclusion**: a free, local 6 GB model **can** weave — but not through bare `ollama run`; it needs
a ~20-line wrapper hitting the HTTP API (same pattern as the Gemini wrapper) set as
`weave_command`. **Untested and honestly unknown**: full-size notes. This test used a 2.8 KB prompt;
production notes are 30–60 KB, which on CPU would be proportionally slower and pushes harder on a
small model's context and discipline. Treat local weaving as "verified for small notes, unproven at
full scale".

Either way, the pipeline's fail-soft holds: a weave that fails the validation gate (missing
anchors, truncation) is discarded, the collected ⏳ entries remain in the note, and the next run —
or a manual weave — picks them up. A weak local weaver costs you polish, never data.
