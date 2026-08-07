---
name: living-note
description: 生きたノート (ikita-note) の操作。「◯◯をノートにして」「ノートに聞く」「ノート更新して」「◯◇ノートおやすみ/起こして」で発動。関心トピックの新設・PubMed収集と織りの実行・ノートと全文ストアからの根拠付きQ&A・休眠/再開を担う。
---

# living-note — 生きたノートの操作

このスキルは ikita-note リポジトリ (このリポジトリ) 内での操作を定義する。
パスはすべてリポジトリルート相対。

## インテント別の手順

### 「◯◯をノートにして」(トピック新設)
1. slug を決める (英小文字ハイフン)。`notes/template.md` を `notes/<slug>.md` にコピー
2. frontmatter (topic/slug) とタイトルを書き換える
3. `config/living-notes.json` の `topics` に {slug, title, queries, note} を追記。
   検索式はユーザーと相談して絞る (広すぎると雑音、狭すぎると空振り。
   例: `<topic>[Title] AND (systematic[sb] OR guideline[pt] OR randomized controlled trial[pt] OR review[pt])`)
4. `python3 scripts/living_notes_update.py --topic <slug> --force` で初回実行
5. 結果 (何本入ったか・サマリ) を短く報告する

### 「ノート更新して」
`python3 scripts/living_notes_update.py --force` (全トピック) または `--topic <slug>`。
実行後、新着件数と5行サマリの変化点だけ報告する。

### 「ノートに聞く」「◯◯ってどうだっけ」(Q&A)
1. まず該当ノートの 📌 サマリと 🧵 横断まとめを読む
2. 足りなければ `data/fulltext/*.txt` を grep して全文の該当箇所を読む
   (全文が無ければ `python3 scripts/fulltext_fetch.py --note notes/<slug>.md` を提案)
3. **必ず出典 (PMID/DOI リンク) 付きで**回答する。ノートに無い知識で埋めない —
   蔵書に無いことは「蔵書には無い」と言う
4. 医学的内容には「臨床判断は原著と現場の判断で」を添える

### 「◯◯ノートおやすみ」/「起こして」
`--sleep <slug>` / `--wake <slug>`。おやすみ時は「ノートは残っていて読めます」を必ず添える。

### 「全文取ってきて」
`export UNPAYWALL_EMAIL=...` が必要 (未設定ならユーザーに聞く)。
`python3 scripts/fulltext_fetch.py --note notes/<slug>.md`。
取得は合法 OA のみ — 取れなかった分は「ペイウォール内 (正当な限界)」と報告する。

## 原則

- ノートの手編集は自由だが、8つの `<!-- LN:...-->` アンカーは消さない (機械編集の目印)
- 報告は短く: 件数・変化点・次に読むべき1本、まで
- 収集も回答も、静かな欠落を作らない (取り漏らしは明示、蔵書に無いことも明示)
