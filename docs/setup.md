# セットアップ — 自走させる人向け

## 必要なもの

- Python 3.10+ (依存ライブラリなし・標準ライブラリのみ)
- 織り (AI によるノートの編み直し) を自動化するなら: LLM CLI
  - 既定は [Claude Code](https://claude.com/claude-code) の `claude` コマンド
  - `config` の `"weave_command"` で任意の CLI に差し替え可 (例: `["gemini", "-p"]`)
  - **無くても動きます** — `--no-weave` で収集だけ回し、織りは手動で (後述)
- 全文取得を使うなら: `pdftotext` (macOS: `brew install poppler` / Ubuntu: `apt install poppler-utils`)

## 初期設定

```bash
cp config/living-notes.example.json config/living-notes.json
cp notes/template.md notes/appendicitis.md   # slug と合わせたファイル名に
```

`config/living-notes.json` を編集:

| キー | 意味 |
|---|---|
| `topics[].slug` | トピックの識別子 (英小文字ハイフン) |
| `topics[].queries` | PubMed 検索式。`[Title]` や `systematic[sb]` などのタグが使える |
| `topics[].note` | ノートのパス (リポジトリ相対) |
| `interval_days` | 実行間隔ゲート (既定7日 — 毎日呼んでも週1回しか動かない) |
| `initial_lookback_days` | 初回にさかのぼる日数 (既定180日) |
| `max_per_run` | 1回の取り込み上限。あふれた分は消えず次回に回る |
| `dedupe_sources` | 手持ち文献リスト (.bib / .jsonl) のパス。Paperpile/Zotero の export を置くと既読論文を取り込まない |
| `weave_command` | 織り手 LLM CLI (省略時は `claude -p`) |

## 動かす

```bash
python3 scripts/living_notes_update.py --dry-run --force   # 何が取れるか素振り
python3 scripts/living_notes_update.py --force             # 初回実行 (収集+織り)
python3 scripts/living_notes_update.py --status            # 状態確認
```

### 織りを手動でやる (LLM CLI が無い場合)

```bash
python3 scripts/living_notes_update.py --force --no-weave        # 収集のみ
python3 scripts/living_notes_update.py --print-weave-prompt appendicitis
```

出てきたプロンプトを ChatGPT / Claude / Gemini に貼り、返ってきた Markdown で
ノートを上書きすれば、それが「織り」です。

### 止める・再開する

```bash
python3 scripts/living_notes_update.py --sleep appendicitis   # 🛏️ 収集停止 (ノートは残る)
python3 scripts/living_notes_update.py --wake appendicitis    # 🟢 再開
```

## 定期実行

スクリプトが自分で7日ゲートを持つので、**毎日1回呼ぶだけ**で週次運用になります。

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

## 全文レイヤー (任意)

ノートの文献リストから、**合法なオープンアクセス版だけ**を取得してテキスト化します。
ペイウォールの迂回はしません。

```bash
export UNPAYWALL_EMAIL=you@example.com   # Unpaywall API の利用者識別 (登録・認証不要)
python3 scripts/fulltext_fetch.py --note notes/appendicitis.md
```

取得物は `data/fulltext/` に貯まり (**git 追跡外** — 著作権物を公開リポジトリに
push しないため)、grep や AI セッションでの「本文からの解答」に使えます。
経験則: 直近論文の3〜7割が OA で取得できます (分野による)。

## テスト

```bash
python3 -m pytest tests/ -q   # 18本、ネットワーク不要
```
