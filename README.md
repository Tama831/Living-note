# 🌱 ikita-note — 生きたノート

**関心を宣言すると、論文が自分で集まり、1枚のノートが編み直され続ける。**

ikita-note は、医学文献の「生きたレビュー」を個人サイズで回すための小さな道具箱です。

- 関心領域を1行の検索式で宣言する (例: 虫垂炎)
- 週1回、PubMed の新着を自動収集する (無認証 API・鍵不要・Python 標準ライブラリのみ)
- AI (織り手) がノート全体を**編み直す** — 追記の羅列ではなく、頭の「5行サマリ」と
  テーマ別の「横断まとめ」が常に現在地を映す
- 本文が読みたくなったら、**合法なオープンアクセス全文だけ**を取得してローカルに貯める
- ノートはただの Markdown — NotebookLM に入れれば引用付き Q&A、AI チャットに貼れば相談相手になる

> **30秒ストーリー**: 2026-08-07、蔵書3本の虫垂炎ノートに初回実行をかけたところ、直近180日の
> 新着30本が集まり、12分後には33本構成の横断まとめに自動成長しました。POCUS の使いどころ、
> 小児の「抗菌薬は本当に要るか」論争、interval appendectomy の判断軸の移動まで編み込まれた
> 状態で、です。→ 実物: [notes/example-appendicitis.md](notes/example-appendicitis.md)

## ふたつの入口

### 🚪 入口1: コードを書かない人 (医療者・研究者)

ノート (.md ファイル) さえ手元にあれば、この道具は要りません。

1. ノートを受け取る (このリポジトリのサンプルでも、誰かが運用しているノートでも)
2. [NotebookLM (Gemini Notebook)](https://notebooklm.google.com/) にソースとして追加する
3. 「妊婦の虫垂炎、画像評価は？」のように**日本語で質問する** — 引用ジャンプ付きで答えが返ります

→ 詳しい手順: [docs/notebooklm-guide.md](docs/notebooklm-guide.md)

### 🚪 入口2: 自走させたい人

Python 3.10+ と (あれば) LLM CLI で、収集→織り→全文取得のパイプラインが動きます。

```bash
git clone https://github.com/Tama831/ikita-note.git && cd ikita-note
cp config/living-notes.example.json config/living-notes.json  # 検索式を自分の関心に
cp notes/template.md notes/appendicitis.md
python3 scripts/living_notes_update.py --dry-run --force       # まず素振り
python3 scripts/living_notes_update.py --force                 # 収集+織り
```

→ 定期実行・LLM の差し替え・全文レイヤー: [docs/setup.md](docs/setup.md)

Claude Code を使っている人は、このリポジトリはそのままプラグインとしても働きます
(`/living-note` — [skills/living-note/SKILL.md](skills/living-note/SKILL.md))。

## しくみ

```
関心の宣言 (config)                     ┌── 🛏️ --sleep でいつでも停止 (ノートは残る)
   │                                    │
   ▼        7日ゲート                    │
PubMed 新着収集 ──→ 重複判定 (手持ち文献と照合) ──→ 新着ログに追記 (⏳)
                                                     │
                              織り手 (LLM) がノート全体を編み直す (⏳→✅)
                              失敗しても収集分は残る (fail-soft)
                                                     │
                                                     ▼
                    📌 5行サマリ / 🧵 横断まとめ / 📚 文献リスト が更新される
                                                     │
                (任意) 合法OA全文の取得 → ローカル全文ストア → 「その中から解答」
```

## 設計原則

- **単一の蔵書 + ビューとしてのノート** — ノートブックごとに情報が分断されない。蔵書はひとつ、ノートは関心ごとの「窓」
- **合法 OA のみ** — 全文取得は Unpaywall 経由のオープンアクセス版だけ。ペイウォール迂回はしない
- **fail-soft** — 外部 API や LLM が落ちても、定期実行を道連れにしない。収集済みは必ず残る
- **降ろしても失われない** — `--sleep` で収集は止まるが、ノートは読み物として生き続ける
- **ただの Markdown** — ロックインなし。どの AI にも、どのエディタにも、10年後の自分にも読める

## ⚠️ 医療情報についての断り

このツールが生成するノートは **AI による文献要約であり、医学的助言ではありません**。
内容には誤りが含まれえます。臨床判断は必ず原著論文・ガイドライン・各現場の判断に
基づいてください。ノート内の全記述には出典リンクが付きます — 原文に当たれることを
信頼性の根拠にしてください。

## English

**ikita-note** ("living note" in Japanese) is a tiny personal pipeline for living
literature reviews: declare a topic as a PubMed query, and a weekly job collects new
papers, dedupes against your library, and has an LLM *re-weave* a single Markdown
note — top summary, cross-cutting synthesis, bibliography — so the note always
reflects the current state of evidence. Notes are plain Markdown: drop them into
NotebookLM for cited Q&A, or paste into any AI chat. Full texts are fetched via
Unpaywall (legal OA only). Stdlib-only Python, fail-soft by design.
As of our survey (Aug 2026), no existing tool combines autonomous collection,
continuous single-note re-synthesis, personal-corpus Q&A, and casual PDF intake —
that gap is why this exists. Not medical advice; every claim links to its source.

## ライセンス

MIT — 自由に使い、直し、配ってください。
