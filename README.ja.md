# 🌱 Living-note — 生きたノート

![living heartbeat](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FTama831%2FLiving-note%2Fmain%2Fdata%2Fheartbeat.json)

> 🇬🇧 English (primary) → **[README.md](README.md)**

**関心を宣言すると、論文が自分で集まり、1枚のノートが編み直され続ける。**

Living-note は、医学文献の「生きたレビュー」を個人サイズで回すための小さな道具箱です。

- 関心領域を1行の検索式で宣言する (例: 虫垂炎)
- 週1回、PubMed の新着を自動収集する (無認証 API・鍵不要・Python 標準ライブラリのみ)
- AI (織り手) がノート全体を**編み直す** — 追記の羅列ではなく、頭の「5行サマリ」と
  テーマ別の「横断まとめ」が常に現在地を映す
- 本文が読みたくなったら、**合法なオープンアクセス全文だけ**を取得してローカルに貯める
- ノートはただの Markdown — NotebookLM に入れれば引用付き Q&A、AI チャットに貼れば相談相手になる

> **30秒ストーリー**: 蔵書3本の虫垂炎ノートに初回実行をかけたところ、直近180日の新着30本が
> 集まり、12分後には33本構成の横断まとめに自動成長しました。POCUS の使いどころ、小児の
> 「抗菌薬は本当に要るか」論争、interval appendectomy の判断軸の移動まで編み込まれた状態で、です。

## 📓 サンプルノート

すべて実際にこのパイプラインで生成されたものです。生きた原本は日本語 (作者の作業言語) で、
2本には照合検証済みの英語スナップショットがあります。

| 日本語 (原本) | English snapshot | 領域 | 更新 |
|---|---|---|---|
| [虫垂炎](notes/example-appendicitis.ja.md) | [Appendicitis](notes/example-appendicitis.md) | 救急・外科 — 診断/抗菌薬 vs 手術/小児 | 🫀 live (毎週自動) |
| [GLP-1受容体作動薬](notes/glp1.ja.md) | — | 代謝 — いま最速で動く領域の定点観測 | 🫀 live (毎週自動) |
| [フッ化水素酸曝露](notes/hydrofluoric-acid.ja.md) | — | 救急・中毒 — HF曝露の治療とマネジメント | 🫀 live (毎週自動) |
| [感染性心内膜炎](notes/infective-endocarditis.ja.md) | [Infective endocarditis](notes/infective-endocarditis.md) | 感染症・循環器 — 診断基準/経口スイッチ/デバイス感染 | 凍結サンプル |
| [IgG4関連疾患](notes/igg4-related-disease.ja.md) | — | 免疫・リウマチ | 凍結サンプル |
| [脂質異常症](notes/dyslipidemia.ja.md) | — | プライマリケア・予防 | 凍結サンプル |
| [コーヒーの楽しみ方](notes/coffee.ja.md) | — | 番外編 (医学外) — 初心者〜上級者 | ☕ 手織り (依頼ベース) |

**🫀 live 行の更新のしくみ (自動同期)**: 作者の実稼働インスタンスが週1回 PubMed 新着を収集して
ノートを織り直し、その結果をこのリポへ直接 push します。新着ゼロの週も鼓動 (heartbeat) commit が
打たれるので、「更新がない」と「死んでいる」が外から区別できます。commit 履歴がそのまま
「生きている証拠」、冒頭のバッジが最終チェック日。GLP-1 ノートはわざと進歩の激しい領域を
選んでいます — 初回スキャンだけで対象論文が180日で約100本 (25本収集・75本持ち越し)。
バックログが毎週消化されていく様子を、そのまま定点観測できます。

コーヒーノートは**手織りの番外編** ☕ — PubMed 収集なし、ノートの「型」だけを趣味に転用
したもの (作者の依頼ベースで織り直し)。この形が医学以外のどんな関心にも使える、という見本です。

## ふたつの入口

### 🚪 入口1: コードを書かない人 (医療者・研究者)

ノート (.md) さえ手元にあれば、この道具は要りません。上のサンプルをダウンロードして
[NotebookLM](https://notebooklm.google.com/) にソースとして入れ、日本語で質問するだけ。
引用ジャンプ付きで答えが返り、ノートブックのリンク共有で同僚にも配れます。
→ **5分ガイド: [docs/notebooklm-guide.ja.md](docs/notebooklm-guide.ja.md)**

### 🚪 入口2: 自走させたい人

以下のクイックスタートへ。Claude Code を使っている人は、このリポジトリはそのまま
プラグインとしても働きます (`/living-note` — [skills/living-note/SKILL.md](skills/living-note/SKILL.md))。

## 🚀 クイックスタート (ゼロから再現する手順)

### 0. 必要なもの

| 項目 | 用途 | 入れ方 |
|---|---|---|
| Python 3.10+ | 収集スクリプト (追加ライブラリ不要) | macOS/Linux は大抵入っています: `python3 --version` |
| LLM CLI (任意) | 織りの自動化 | 例: [Claude Code](https://claude.com/claude-code)。**無くても動く** (手順4)。選択肢と費用の実際: [docs/operations.ja.md](docs/operations.ja.md) |
| pdftotext (任意) | 全文レイヤー | macOS: `brew install poppler` / Ubuntu: `sudo apt install poppler-utils` |

### 1. 取得して、関心を宣言する

```bash
git clone https://github.com/Tama831/Living-note.git
cd Living-note
cp config/living-notes.example.json config/living-notes.json
cp notes/template.ja.md notes/my-topic.md      # 英語ノートなら notes/template.md
```

`config/living-notes.json` を開き、`topics` を自分の関心に書き換えます (サンプル4本の設定が
そのまま入っているので、真似して1個足すだけでもOK)。検索式は PubMed の記法です — まず
`<病名>[Title] AND (systematic[sb] OR guideline[pt] OR randomized controlled trial[pt] OR review[pt])` から始めるのがおすすめ。

### 2. 素振り (何も書き込まずに確認)

```bash
python3 scripts/living_notes_update.py --dry-run --force
```

ヒット数と新規候補の一覧が出れば成功です。`new candidates=0` なら検索式が狭すぎます
(→ 下の「困ったとき」)。※スクリプトの画面出力は英語です (国際公開のため)。

### 3. 初回実行

```bash
python3 scripts/living_notes_update.py --topic my-topic --force
```

(`--topic` を外すと同梱サンプル4本も更新されます — 織りは1本あたり数分かかるので、
まずは自分のトピックだけで試すのがおすすめ)

新着がノートの「🆕 新着ログ」に ⏳ 付きで入り、LLM CLI があればそのまま織りが走って
5行サマリ・横断まとめ・文献リストが書き上がります (⏳→✅)。

### 4. LLM CLI が無い場合の織り (手動)

```bash
python3 scripts/living_notes_update.py --force --no-weave
python3 scripts/living_notes_update.py --print-weave-prompt my-topic
```

出てきたプロンプトを ChatGPT / Claude / Gemini に貼り、返ってきた Markdown でノートを
上書きすれば、それが「織り」です。

### 5. あとは放っておく

```bash
python3 scripts/living_notes_update.py            # 毎日呼んでOK — 7日ゲートで週1回だけ動く
python3 scripts/living_notes_update.py --status   # 状態確認
python3 scripts/living_notes_update.py --sleep my-topic   # 🛏️ 休止 (ノートは残る)
python3 scripts/living_notes_update.py --wake  my-topic   # 🟢 再開
```

cron / launchd への登録例と全文レイヤーの設定は [docs/setup.ja.md](docs/setup.ja.md) に
そのまま貼れる形で置いてあります。

### 検証済み環境 (2026-08-07)

- **macOS (開発機)** — 全手順 + 織り (Claude Code) + 全文レイヤー
- **まっさらの Debian 12 LXC** — apt 前提→clone→テスト→素振り→収集→cron 実発火→織り手差し替えまで通し確認
- **織り手の互換性** — `claude -p` (既定) と Gemini ラッパーの両方で織り上がりを実証。検証落ち時も
  収集分は保全 (fail-soft)。ローカル Gemma の実測は [docs/operations.ja.md §4](docs/operations.ja.md)

## しくみ

```
関心の宣言 (config)                     ┌── 🛏️ --sleep でいつでも停止 (ノートは残る)
   │                                    │
   ▼        7日ゲート                    │
PubMed 新着収集 ──→ 蔵書と重複判定 ──→ 新着ログに追記 (⏳)
                                                     │
                     織り手 (LLM) がノート全体を編み直す (⏳→✅)。
                     失敗しても収集分は残る (fail-soft)
                                                     │
                                                     ▼
                    📌 5行サマリ / 🧵 横断まとめ / 📚 文献リスト が更新される
                                                     │
        (任意) 合法OA全文 → ローカル全文ストア → 「その中から解答」
```

## 🔗 自分の文献管理ツールとつなぐ (Paperpile / Zotero)

手持ちの文献リスト (BibTeX export) を置くと、Living-note は**あなたの蔵書**とつながります。
export の作り方 — Paperpile: 論文を選択 → Export → BibTeX / Zotero: File → Export Library →
BibTeX。できた .bib を `library/my-library.bib` などに置き、config の `dedupe_sources` に登録します。

つながると、トピックごとに**3つのモード**が選べます (`"mode"`):

| mode | 何をするか |
|---|---|
| `latest` (既定) | PubMed の新着を集めて織る —「最新の知見を中心に」 |
| `library` | **自分が集めた蔵書の中だけ**から該当分を拾って織る。PubMed は見ない |
| `both` | 融合 — 蔵書を土台に、新着がその上に編み込まれていく |

```json
{
  "dedupe_sources": ["library/my-library.bib"],
  "topics": [
    {
      "slug": "appendicitis",
      "title": "虫垂炎",
      "mode": "both",
      "library_query": "appendicitis|appendix",
      "queries": ["appendicitis[Title] AND (systematic[sb] OR review[pt])"],
      "note": "notes/appendicitis.md"
    }
  ]
}
```

- `library_query` は蔵書から拾う条件 (正規表現・大文字小文字無視、タイトル+keywords に当たる)。
  英語文献には英語で書きます
- `latest` モードでも `dedupe_sources` は効きます — 蔵書済みの論文は新着として二重取り込みしない
- 蔵書由来の論文は新着ログで「from library」と表示され、区別が付きます
- 正直な注意: .bib は**手動 export** です — 論文を足したらたまに export し直してください
  (管理ツール側に公開 API がまだ無いための制約)

## 🔧 困ったとき

| 症状 | 対処 |
|---|---|
| `new candidates=0` (新規候補なし) | 検索式を広げる (`[Title]`→`[Title/Abstract]`)、`initial_lookback_days` を 365 に |
| ヒットが多すぎ・雑音だらけ | `[Title]` に絞る、`AND (systematic[sb] OR guideline[pt] ...)` で種別を絞る |
| ⏳ が残ったまま (織りが走らない) | LLM CLI 未検出。`--print-weave-prompt` で手動織り、または `weave_command` に手持ちの CLI を設定 |
| 織りの出力が捨てられた | 仕様です — アンカー欠落など検証に落ちた出力は採用しません。収集分は残っていて次回また織られます |
| NotebookLM に .md が上がらない | 中身を Google ドキュメントに貼り、それをソース指定 (同じ効果) |
| 全文が取れない (`no_oa`) | ペイウォール内 = 正当な限界。OA 率は分野により3〜7割 |

## 設計原則

- **単一の蔵書 + ビューとしてのノート** — 情報がノートブック単位で分断されない。蔵書はひとつ、ノートは関心ごとの「窓」
- **合法 OA のみ** — 全文取得は Unpaywall 経由のオープンアクセス版だけ。ペイウォール迂回はしない
- **fail-soft** — 外部 API や LLM が落ちても、定期実行を道連れにしない。収集済みは必ず残る
- **降ろしても失われない** — `--sleep` で収集は止まるが、ノートは読み物として生き続ける
- **ただの Markdown** — ロックインなし。どの AI にも、どのエディタにも、10年後の自分にも読める

なぜこの形か (先行14ツールの比較表つき): [docs/design.ja.md](docs/design.ja.md)

## ⚠️ 医療情報についての断り

このツールが生成するノートは **AI による文献要約であり、医学的助言ではありません**。誤りが
含まれえます。臨床判断は必ず原著論文・ガイドライン・各現場の判断に基づいてください。ノート内の
全記述には出典リンクが付きます — 「原文に当たれること」を信頼性の根拠にしてください。

## ライセンス

MIT — 自由に使い、直し、配ってください。
