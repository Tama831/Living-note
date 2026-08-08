# Operations in practice / 運用の実際

What README and [setup.md](setup.md) don't tell you: what you physically need, what actually runs
and when, and which weaver LLMs make weekly operation realistic. This is the last layer of
"assumptions that only existed in the author's environment", written down.

README と [setup.md](setup.md) が教えてくれないこと — 物理的に何が必要か、いつ何が動いていて
リアルタイムに何をしておく必要があるか、そしてどの織り手 LLM なら週次運用が現実的か。
「作者の環境にだけ在った前提」の最後の層を明文化したものです。

## 1. Physical requirements / 物理要件

Collection is stdlib-only HTTP against PubMed — **a Raspberry Pi-class machine is enough**. If the
weave is delegated to a cloud LLM CLI, no local compute is needed at all; if you run a local LLM,
the requirements are whatever that model needs (see §4 for a measured example). **Always-on is not
required**: the machine only needs to be awake when the daily cron/launchd tick happens to land,
and a missed tick self-heals (§2).

収集は標準ライブラリの HTTP だけで PubMed を叩くので、**Raspberry Pi 級のマシンで十分**です。
織りをクラウド LLM CLI に任せるなら計算資源は一切不要。ローカル LLM を使うなら、そのモデルの
要件がそのまま必要です (実測例は §4)。**常時稼働は必須ではありません** — 毎日の cron/launchd の
呼び出し時刻にマシンが起きていればよく、逃した回は自然回復します (§2)。

## 2. What actually runs, and when / スケジュールの実態

The scheduler calls the script **once a day**; the built-in 7-day gate means it actually works
**once a week** per topic — measured at ~30 seconds of collection plus a few minutes of weaving
(4–7 min with `claude -p`, ~5 min with the Gemini wrapper, on 2026-08-07 runs). If the machine is
asleep at tick time, that day is simply skipped and the next day's tick picks it up — the gate
compares against `last_run`, so nothing breaks and nothing is lost.

**Real-time obligations are close to zero by design.** The honest full list:

1. **Monthly-ish**: check that your LLM CLI login hasn't expired (a dead weaver degrades gracefully —
   ⏳ entries accumulate, nothing is lost, but nothing gets woven either)
2. **Only if you use library integration**: re-export your .bib occasionally after adding papers (optional)
3. **If ⏳ entries linger** in a note: run a manual weave (`--print-weave-prompt` → paste into any AI chat)

スケジューラはスクリプトを**毎日1回**呼びますが、内蔵の7日ゲートにより実働はトピックあたり
**週1回** — 実測で収集約30秒+織り数分 (2026-08-07 の実測: `claude -p` で4〜7分、Gemini ラッパーで
約5分) です。呼び出し時刻にマシンが寝ていればその回はスキップされ、翌日の呼び出しが拾います —
ゲートは `last_run` 基準の比較なので、壊れも取りこぼしもしません。

**リアルタイムの義務は設計上ほぼゼロ**です。正直な全リスト:

1. **月1程度**: LLM CLI のログインが切れていないか確認 (織り手が死んでも劣化は緩やか —
   ⏳ が溜まるだけで失われはしないが、織られもしない)
2. **蔵書連携を使う人のみ**: 論文を足したら .bib をたまに再 export (任意)
3. **⏳ が残り続けていたら**: 手動織りで回収 (`--print-weave-prompt` → 任意の AI チャットに貼る)

## 3. Weaver requirements & options / 織り手の要件と選択肢 (as of 2026-08)

A weaver LLM needs three things / 織り手 LLM に必要なのは3つ:

1. **Headless execution** — prompt as an argument, full output to stdout
   / **ヘッドレス実行** — プロンプトを引数で受け、stdout に全出力
2. **Long input/output** — the full note (30–60 KB) goes in, a full note comes out
   / **長文入出力** — ノート全文 (30-60KB) が入り、ノート全文が出てくる
3. **Flat-rate plan coverage, or free/local** — weekly weaves on metered billing are technically
   fine but psychologically corrosive; a weaver that rides an existing subscription (or runs free
   locally) is what makes "leave it alone" real
   / **定額プラン枠に乗る、または無料/ローカル** — 従量課金でも週次は技術的には回るが、
   「放っておける」を心理的に成立させるのは既存サブスクの枠内か無料ローカルで動く織り手

| Weaver / 織り手 | Billing / 課金形態 | Headless | Status / 検証状態 |
|---|---|---|---|
| **Claude Code `claude -p`** (default / 既定) | flat-rate within Pro/Max plans / Pro・Max プランの定額枠内 | ✅ | ✅ **verified** — default weaver, all samples woven with it / 実証済み (全サンプルの織り手) |
| **Gemini API wrapper** (~30-line script) | metered API key. Measured weave = 30–60 KB prompt + full-note output; at Aug-2026 flash-tier list prices ($0.10–1.50 /M input, $0.40–7.50 /M output)¹ that is roughly **$0.01–0.10 per weave** / 従量 (API キー)。実測サイズ×公表単価で **1織り約$0.01-0.1** | ✅ | ✅ **verified** (2026-08-07, `gemini-flash-latest`) / 実証済み |
| Gemini CLI | ⚠️ free & AI-Pro/Ultra serving **discontinued 2026-06-18**; now enterprise Code Assist seats or metered API key only² / 無料・AI Pro/Ultra 向け提供は **2026-06-18 終了**、現在はエンタープライズ契約か API 従量のみ | ✅ | ❌ not tested / 未検証 |
| OpenAI Codex CLI | flat-rate within ChatGPT plans (CLI included on all tiers incl. Free/Go/Plus, shares the plan's usage limits)³ / ChatGPT 全プランの定額枠内 (CLI は Free/Go/Plus 含む全プラン同梱、プランの利用上限を共有) | ✅ (`codex exec`) | ❌ not tested / 未検証 |
| **Ollama local (Gemma)** | free, local / 無料・ローカル | ⚠️ HTTP API wrapper required — bare `ollama run` pollutes stdout / 素の `ollama run` は不可、HTTP API ラッパー必須 | ⚠️ **verified for small notes only** (163 s on CPU), full-size unproven — see §4 / 小ノートのみ実証 (§4) |

Sources / 出典 (2026-08-08 checked):
¹ [Gemini API flash-tier pricing](https://www.aipricing.guru/google-ai-pricing/) ([alt](https://pricepertoken.com/pricing-page/model/google-gemini-3.5-flash))
² [Gemini CLI pricing changes](https://www.tembo.io/blog/gemini-cli-pricing) ([alt](https://nerova.ai/costs-roi/gemini-cli-pricing-explained-2026))
³ [Codex rate card (OpenAI Help)](https://help.openai.com/en/articles/20001106-codex-rate-card) ([alt](https://www.cloudzero.com/blog/openai-codex-pricing/))

"Not tested" means exactly that: it should satisfy the three requirements on paper, but we have
not run a weave through it. / 「未検証」は文字通りの意味です — 紙の上では3要件を満たすはずですが、
実際に織りを通してはいません。

## 4. Local LLM, measured: Gemma / ローカルLLM実測: Gemma

**Setup**: Ollama on a CPU-only Proxmox LXC (8 cores of an AMD Ryzen 7 6800H, 7 GB RAM), model
`gemma4:e4b-it-qat` (6.1 GB quantized). **Fair-sized input**: a small note (2.4 KB — 1 bibliography
entry, short synthesis) plus 3 new arrivals with abstracts; weave prompt 2.8 KB total.

**設定**: CPU のみの Proxmox LXC (AMD Ryzen 7 6800H の8コア・RAM 7GB) 上の Ollama、モデルは
`gemma4:e4b-it-qat` (量子化 6.1GB)。**公平な入力サイズ**: 小さめのノート (2.4KB — 文献1件+短い
横断まとめ) + 抄録付き新着3件、織りプロンプト計 2.8KB。

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

**結果 (2026-08-08 実測)** — 2回の試行を正直に:

| 試行 | 配管 | 時間 | 検証ゲート |
|---|---|---|---|
| 1 | `ollama run` CLI 直 (stdout リダイレクト) | 292秒 | ❌ **FAIL** — stdout に「Thinking...」の思考前置きと端末制御コードが混入し、出力が frontmatter で始まらなかった。正しく棄却され、何も失われていない |
| 2 | Ollama HTTP API (`/api/generate`, `stream:false`, `think:false`) | **163秒** (出力1,509トークン) | ✅ **PASS** — アンカー8/8保存・frontmatter 正常・新着3件がサマリと横断まとめに正しく編入・⏳→✅ |

**結論**: 無料のローカル 6GB モデルでも**織れる** — ただし素の `ollama run` ではだめで、
HTTP API を叩く20行程度のラッパー (Gemini ラッパーと同型) を `weave_command` に指定する必要が
ある。**未検証で正直に不明な点**: フルサイズのノート。この実測は 2.8KB プロンプトであり、
本番の 30-60KB は CPU では比例して遅くなり、小型モデルの文脈長と規律への負荷も大きい。
ローカル織りは「小さいノートで実証済み・フルスケールは未証明」として扱うこと。

Either way, the pipeline's fail-soft holds: a weave that fails the validation gate (missing
anchors, truncation) is discarded, the collected ⏳ entries remain in the note, and the next run —
or a manual weave — picks them up. A weak local weaver costs you polish, never data.

どちらに転んでも、パイプラインの fail-soft は成立します: 検証ゲート (アンカー欠落・途切れ) に
落ちた織りは破棄され、収集済みの ⏳ はノートに残り、次回実行か手動織りが回収します。非力な
ローカル織り手で失うのは仕上がりの質だけで、データは失われません。
