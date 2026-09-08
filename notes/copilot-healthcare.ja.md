---
topic: Copilot活用 (ヘルスケア) / copilot in healthcare
slug: copilot-healthcare
updated: 2026-09-08
mode: hybrid (エビデンス=PubMed自動収集・週次 / 製品・制度・活用術=手織り)
---

# 🩺 生きたノート: Copilot活用 (ヘルスケア重点) (ライブミラー)

> **これは作者の実稼働インスタンスのライブミラーです** — 本家で週1回の自動収集
> (PubMed) と織り直しが走るたび、このノートと鼓動 ([heartbeat](../data/heartbeat.json))
> がここに push されます。**最終チェック: 2026-09-08 JST — ノート更新あり。**
> **内容は AI が論文から編んだ要約であり、鵜呑みにしないでください。** 臨床判断は必ず
> 原著と主治医・現場の判断に従ってください。各記述の出典リンクから原文に当たれます。
> ⏳ = 収集済み・織り待ち / ✅ = 本文に編み込み済み。

## 📌 5行サマリ
<!-- LN:SUMMARY:START -->
- 「Copilot」は単一製品ではなく**ファミリー名**。医療で効くのは主に3系統 — 臨床文書の Dragon Copilot (ambient AI scribe)、事務・運営の Microsoft 365 Copilot、開発・研究の GitHub Copilot。混同が導入事故と契約ミスの元
- 普及は「実験」を脱した: Dragon Copilot は10万人超の臨床医、NHS England は M365 Copilot を**50.5万人へ全面展開**(2026年10月完了予定・試験で平均43分/日削減)。スペイン語外来での**230万回利用**の実地評価も出て、検証は英語圏の外へ広がった
- 査読エビデンスは「**burnout には効く・時間短縮は控えめ・効果はツール固有**」で安定 (burnout 51.9%→38.8%、文書時間は8時間診療あたり16分)。一方2026年の焦点は先へ進み、**署名後のノートが下流でどう変形するか・通訳誤りの伝播・監督する側の認知負荷**が新しい安全課題。サイン前の全文レビューは依然として最後の安全弁
- 日本では Dragon Copilot は本格展開前。使えるのは M365 Copilot での事務・会議・資料作成が中心で、規範は**3省2ガイドライン + 医療・ヘルスケア分野生成AI利用ガイドライン第2版 (2025-07)**。患者特定情報を入れない・下書きとして扱うが2大原則
- 家庭医の机では「紹介状の骨子・議事録・勉強会資料・データ集計」から小さく始める。**匿名化→出典要求→自分の目で全文確認**の3点セットに加え、**浮いた時間の使い道を先に決めておく**(削減分は放っておくと患者にも自分にも還らない)
<!-- LN:SUMMARY:END -->

## 🧵 横断まとめ
<!-- LN:SYNTHESIS:START -->

### 1. 「Copilot」という言葉の地図 — まずファミリーを見分ける
Microsoft は多数の AI 製品に Copilot の名を与えており、**どの Copilot の話かを特定しないと契約もガバナンスも噛み合わない**。医療現場に関係するのは主に:

| 名前 | 何者か | 医療での主な出番 |
|---|---|---|
| **Dragon Copilot** | 音声入力 (Dragon Medical One) + ambient AI (DAX) を統合した臨床ワークフロー特化アシスタント | 診察会話からのカルテ自動下書き、オーダー・紹介状、ICD-10 コーディング支援 |
| **Microsoft 365 Copilot** | Word/Excel/Outlook/Teams に組み込まれる業務アシスタント (組織テナント内で動く) | 会議録、文書下書き、メール、データ集計 — 医療機関の**事務・運営**サイド |
| **Copilot Chat / 無料版 Copilot** | Web グラウンディングのチャット (Entra ID サインインで企業データ保護) | 文献下調べ・一般調査。**患者情報は入れない** |
| **GitHub Copilot** | コーディングアシスタント | 臨床研究のデータ解析、FHIR 連携アプリ、informatics |
| **Copilot Studio** | ノーコードでカスタムエージェントを作る基盤 | 事前承認 (prior auth)・予約案内など定型業務エージェント |

見分けの実務ポイント: **個人アカウントの Copilot と組織テナントの Copilot は別物**。前者に業務情報を入れるのは情報漏洩に相当する。組織版 M365 Copilot はテナント境界内で動き、米国では BAA (HIPAA 事業提携契約) の対象に含められる ([EPC Group 解説](https://www.epcgroup.net/answers/healthcare-microsoft-copilot-hipaa-2026))。

なお「Copilot」という語は Microsoft の商標を超えて**臨床 AI アシスタント一般の比喩**としても使われ始めた。院内 LLM をオンプレミス配備して眼科手術記録を human-in-the-loop で生成する試み ([Int J Med Inform, PMID 42570565](https://pubmed.ncbi.nlm.nih.gov/42570565/))、通信も専門家相談も断たれた現場で救急手技を支える first response 用アシスタント ([Mil Med, PMID 42560246](https://pubmed.ncbi.nlm.nih.gov/42560246/)) はいずれも Microsoft 製品ではない。**「Copilot と呼ばれている＝Microsoft 製」ではない**ことも見分けに含める。

### 2. 臨床ドキュメンテーション — Dragon Copilot と ambient AI scribe の現在地
「診察の会話を聞いてカルテの下書きを作る」ambient AI scribe は、臨床 AI の中で最も速く普及した部類に入る。

- **規模**: Dragon Copilot は10万人超の臨床医が日常利用、Dragon 系 ambient 技術は650以上の医療組織に導入済み ([Microsoft Cloud Blog, HIMSS 2026](https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2026/03/05/unify-simplify-scale-microsoft-dragon-copilot-meets-the-moment-at-himss-2026/))。[Mount Sinai](https://www.mountsinai.org/about/newsroom/2025/mount-sinai-health-system-to-roll-out-microsoft-dragon-copilot) など大規模システムの採用が続く
- **機能の広がり (HIMSS 2026 発表)**: 58言語対応、ICD-10 コーディング支援、パートナーアプリ市場 (Optum・Regard 等のエージェントを Copilot 画面内で起動)。**看護向け**にはベッドサイド会話からフローシート項目への構造化入力、放射線科向け機能も ([HIT Consultant](https://hitconsultant.net/2026/03/05/microsoft-dragon-copilot-himss-2026-agentic-clinical-ai-nurses-radiologists/))
- **外来 EHR への浸透**: athenahealth が athenaOne への組み込みを発表 (2026年上半期提供) ([Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/athenahealth-integrates-dragon-copilot-ai-assistant-microsoft-moves-deeper))。Epic とは以前から深い統合
- **市場評価**: KLAS Research (2026年1月) は ambient AI を「実験的な珍しさから、測定可能なリターンを持つ運用ツールへ移行した」と評価 (上記 Microsoft ブログ経由の二次情報)
- **大規模展開の設計図が論文化され始めた**: Cleveland Clinic はベンダー協業による enterprise 展開の4本柱 (ガバナンス・研修とオンボーディング・…) を公開 ([PMID 42581183](https://pubmed.ncbi.nlm.nih.gov/42581183/))。DAX Copilot のマルチサイト大規模実装での EHR 効率・well-being への効果検証も出た ([PMID 42618038](https://pubmed.ncbi.nlm.nih.gov/42618038/))。設計図づくりは「どう入れるか」から「**入れる前に何を測るか**」へ進み、学術界と産業界の視点を突き合わせた採用の概念モデル — 実地性能は施設ごとに大きくばらつくという前提から、どの性能指標が採用判断に効くかを整理する試み — が提案された ([JMIR Med Inform, PMID 42684418](https://pubmed.ncbi.nlm.nih.gov/42684418/))
- **地理的な広がり**: カナダでも診療所への浸透が急速で、オンタリオ州会計検査院の報告を機に便益とリスクの公開論争が始まっている ([PMID 42605518](https://pubmed.ncbi.nlm.nih.gov/42605518/))。英国では規制当局が医師の AI scribe 利用に関する見解を更新 ([BMJ, PMID 42575564](https://pubmed.ncbi.nlm.nih.gov/42575564/))。そして**英語圏の外**では、スペインの外来診療で**累計230万回**の利用に基づく実地評価が報告され (臨床医の体験・原文との意味的一致・ワークフロー効率を同時に測定) ([Front Digit Health, PMID 42518737](https://pubmed.ncbi.nlm.nih.gov/42518737/))、非英語環境での大規模検証が現実に可能になったことを示した

⚠️ ベンダー・導入施設発の数字 (例: オタワ病院の「burnout 70%削減・患者満足97%」) は宣伝文脈を含む。次節の査読研究と分けて読む。

### 3. エビデンスの現在地 — 効くこと・効かないこと・危ないこと
査読文献・独立調査ベースでは、絵はもう少し陰影がある。2026年後半の文献は問いを一段進めて、「効くのか」ではなく「**どこに効き、代わりに何を支払っているのか**」を測り始めた:

- **burnout・主観的負担には一貫して効く**: 6医療システム263人の前後比較で burnout 有病率 51.9%→38.8% (30日間、正味13.9ポイント改善) — JAMA Network Open 掲載研究として複数の独立レビューが引用 ([IHS 解説](https://www.ihsonline.org/post/ambient-ai-medical-scribes-efficiency-gains-burnout-uncertainty-and-governance-risks))。この方向は領域を問わず再現しており、**家庭医療の研修医**を対象としたパイロット ([PRiMER, PMID 42518625](https://pubmed.ncbi.nlm.nih.gov/42518625/))、リウマチ科の実地報告 ([EULAR Rheumatol Open, PMID 42540133](https://pubmed.ncbi.nlm.nih.gov/42540133/))、緩和ケアのパイロット調査 ([PMC12427878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12427878/)) が同じ絵を描く
- **客観的な時間短縮は控えめ**: 5大学医療センター1,800人・2023-2025年の大規模実測で、8時間の診療あたり文書作成 -16分・EHR 滞在 -13分。利用は断続的な医師が多い ([STAT, 2026-04](https://www.statnews.com/2026/04/01/ai-ambient-scribes-modest-time-savings-clinical-documentation/))。測定の対象も広がり、人工関節外来では**外来フローそのもの**への前向き評価 (EHR 導入で文書時間が診療時間の16%→28%に膨らんだ歴史を背景に) ([Arthroplast Today, PMID 42564601](https://pubmed.ncbi.nlm.nih.gov/42564601/))、救急では「誰がいつ実際に使うか」という実地の採用パターン ([Ann Emerg Med, PMID 42524795](https://pubmed.ncbi.nlm.nih.gov/42524795/)) が主題になった。「劇的な時間革命」ではなく「夜間持ち帰り仕事 (pajama time) の目に見える圧縮」と読むのが誠実
- **支払っている対価は「監督する側の認知負荷」**: 医療者が AI と協働するときの認知負荷・精神的負担を扱った系統的レビュー＋メタ解析が登場した ([J Med Internet Res, PMID 42550089](https://pubmed.ncbi.nlm.nih.gov/42550089/))。ambient 文書・画像診断 AI・CDSS が日常に入る一方で、**それを監督する側の負担はほとんど研究されてこなかった** — 「時間は減ったのに疲れは減らない」という現場感覚を説明しうる変数として、今後の中心論点になる
- **RCT も出始めた**: 2種の ambient AI scribe を比較するランダム化試験 (文書効率と burnout を主要評価) が preprint 段階から査読へ ([medRxiv 2025](https://www.medrxiv.org/content/10.1101/2025.07.10.25331333.full.pdf))
- **安全性の焦点が「下書きの精度」から「サイン後」へ移った**: 記載漏れ (omission) の多さと幻覚 (fabrication) 約7% — 14本に1本の下書きに事実でない内容が混入しうる — は未解決のまま (二次情報: [IHS](https://www.ihsonline.org/post/ambient-ai-medical-scribes-efficiency-gains-burnout-uncertainty-and-governance-risks))。ただし2026年の議論はその先へ進んだ:
  - **署名済みノートは静的ではない**。コピー・要約・コーディング・下流 AI への再投入を経て変形していくため、評価指標を「初稿の品質」から「**署名後に何が起きたか**」へ移すべきという主張 ([JMIR Med Inform, PMID 42574720](https://pubmed.ncbi.nlm.nih.gov/42574720/))。一度混入した誤りが下流で増幅される経路まで見なければ安全性は測れない
  - **通訳を介する診療では、通訳の誤りがそのままノートへ転写される**。英語・スペイン語の模擬診察で、話者の役割とエラー型によって伝播パターンが変わることが示された ([JMIR Med Inform, PMID 42520279](https://pubmed.ncbi.nlm.nih.gov/42520279/))。58言語対応の裏面であり、在留外国人診療を持つ日本の現場にも直結する
  - **診断プロセス自体が静かにずれる**: AI は受診前・臨床推論中・記録生成後の3点で診察に入り込み、その各点で解釈を歪めうる (interpretive drift) という論考 ([Diagnosis (Berl), PMID 42703752](https://pubmed.ncbi.nlm.nih.gov/42703752/))。診断エクセレンスの測り方を AI 時代に合わせて作り直す取り組み ([CODEX, PMID 42581404](https://pubmed.ncbi.nlm.nih.gov/42581404/)) と対になる論点
  - **失敗は技術単独では起きない**: 文書化の失敗を生む社会技術的メカニズムの質的研究でも、品質・安全の知見は「mixed」([PMID 42594260](https://pubmed.ncbi.nlm.nih.gov/42594260/))
- **効果はツール固有**: primary care で3種のアーキテクチャ (タブレット型・EHR統合型・スタンドアロン型) を比較した実測で、効率・文書負担・生産性への効果に**ツール固有の差と経時変化**が観察された ([JAMIA Open, PMID 42583084](https://pubmed.ncbi.nlm.nih.gov/42583084/))。「ambient AI 一般」ではなく製品単位で評価する時代へ
- **専門科別の地図が埋まってきた**: 救急14施設ネットワークの後ろ向きコホート ([PMID 42628943](https://pubmed.ncbi.nlm.nih.gov/42628943/))・救急の scoping review ([PMID 42585863](https://pubmed.ncbi.nlm.nih.gov/42585863/)) に加え、泌尿器科・整形外科・院内薬剤部・小児消化器 ([PMID 42548074](https://pubmed.ncbi.nlm.nih.gov/42548074/)・[PMID 42499718](https://pubmed.ncbi.nlm.nih.gov/42499718/))・リウマチ科へ実装報告が広がる。逆に**精神科は明確に遅れており**、その理由 (記録の性質・同意・秘匿性) を他科と対比した scoping review が出た ([Sante Ment Que, PMID 42550434](https://pubmed.ncbi.nlm.nih.gov/42550434/))
- **患者側の受容は「概ね好意的・しかし条件つき」**: 外来患者の受容性と信頼の規定要因 ([PMID 42648708](https://pubmed.ncbi.nlm.nih.gov/42648708/)) に続き、皮膚科外来の横断調査では**82.1%が快適と回答する一方、半数超が懸念を表明**した (事前の接触経験はほとんど無い状態で) ([Australas J Dermatol, PMID 42504001](https://pubmed.ncbi.nlm.nih.gov/42504001/))。小児病院では**導入前**の段階で医療者が「ケアの質」への影響をどう予期しているかが調べられた ([J Healthc Qual Res, PMID 42497486](https://pubmed.ncbi.nlm.nih.gov/42497486/))。快適さと懸念は同居する — 同意取得は形式でなく説明の設計問題
- **「浮いた時間」の行き先が政策論に**: 削減された文書時間 (attention dividend) は自動的には患者に還元されない — 回収された臨床能力の配分を健康政策の資源問題として扱う議論 ([PMID 42582985](https://pubmed.ncbi.nlm.nih.gov/42582985/)) に対し、看護からは鋭い警告が出た。「時間が浮く」の証明は、そのまま**人員配置を締める根拠 (staffing trap) に転用されうる** ([Appl Clin Inform, PMID 42705617](https://pubmed.ncbi.nlm.nih.gov/42705617/))。導入の交渉では**削減分の使途を先に文書化しておく**のが実務的な防御
- **「書くこと」は何だったのかという問い**: Lancet は ambient scribe を「物語の技術 (narrative technologies)」と捉え、現在の使われ方が患者中心の医療を損ないうる**見過ごされたリスク**を論じた ([PMID 42612661](https://pubmed.ncbi.nlm.nih.gov/42612661/))。さらに一歩踏み込んで、カルテを書く行為は要約・伝達の作業に留まらず**臨床家の道徳的形成 (moral formation) の場**であり、丸ごと外注すると何が失われるかを論じる寄稿も ([J Gen Intern Med, PMID 42675252](https://pubmed.ncbi.nlm.nih.gov/42675252/))。教育側では、研修医の**臨床推論の筋力が AI scribe で衰えないためのガードレール** ([PMID 42624999](https://pubmed.ncbi.nlm.nih.gov/42624999/))、および AI 支援フィードバックにおける記載の質と教育的価値を測る研究 ([JMIR Med Educ, PMID 42684426](https://pubmed.ncbi.nlm.nih.gov/42684426/)、著者名から国内グループと見られる) が現れた。**指導医が「下書きを直す」役から「思考を育てる」役へ戻れるか**が分岐点
- **総説と5年の答え合わせ**: 技術・効果・実装をまとめた narrative review ([PMID 41815573](https://pubmed.ncbi.nlm.nih.gov/41815573/))、変革可能性と責任ある統合を論じる論説 ([PMC12316405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12316405/)) が入口として良い。さらに2020年の EIT Health / McKinsey 予測 (事務自動化と画像から入り、遠隔モニタリングと NLP が続く) を5年後の実績と突き合わせた検証も出た ([Int J Med Inform, PMID 42697156](https://pubmed.ncbi.nlm.nih.gov/42697156/)) — 予測と現実のズレ方を知っておくと、いまの誇大広告の割引率が見積もれる

### 4. 事務・運営サイド — M365 Copilot の使いどころ (NHS が実証台)
臨床記録より先に投資対効果が見えやすいのが**非臨床業務**。ここでの最大の実証例が NHS England:

- **30,000人・90組織での試験**で平均**43分/日**の事務時間削減 (年換算で1人あたり約5週間分) → **505,000人の臨床・支援スタッフへ全面展開**、2026年10月完了予定 ([TheStreet](https://www.thestreet.com/health/microsoft-and-copilot-just-hit-a-jackpot-in-healthcare-ai-nhs))
- 使い方の中心は: 会議の要約 (Teams)、定型文書・報告書の下書き、メール処理、人事・財務・調達の事務支援、経営会議資料の作成
- 医療機関向けのシナリオ集は [Microsoft Adoption の Healthcare ライブラリ](https://adoption.microsoft.com/en-us/scenario-library/healthcare/) に整理されている (スケジューリング、患者向け文書の平易化、症例カンファ準備など)
- **「臨床ノート以外の医療文書」も射程に入った**: 看護主導で ambient AI を**医療安全のインシデント調査報告書**に適用した Project NARRATE は、導入前後の文書品質を比較し、自由記述では欠けがちだった完全性・可読性・詳細度の改善を報告した ([JMIR Nurs, PMID 42574744](https://pubmed.ncbi.nlm.nih.gov/42574744/))。院内で「書式が定まらず質がばらつく文書」(インシデント報告・委員会記録・研修評価) は、患者カルテより先に手を付けられる領域

日本の医療機関でも同型のユースケース (委員会議事録、院内文書、研修資料、シフト・集計業務) は今日から成立する。**臨床判断に直結しない業務から始める**のが NHS 型の導入順序でもある。

### 5. 開発・研究サイド — GitHub Copilot / Copilot Studio
- **GitHub Copilot**: 臨床研究のデータクリーニング・統計スクリプト・可視化コードの下書きに有効。R/Python の解析コードを「書ける人」から「読める人」へ裾野を広げる。ただし**生成コードの品質は課題依存で一様でない** — 7種のコーディングアシスタント (GitHub Copilot 含む) に金融予測用の LSTM 実装を書かせて品質と効率を比較した研究では、アシスタント間の差と再現性の問題が浮かんだ ([Front Artif Intell, PMID 42534975](https://pubmed.ncbi.nlm.nih.gov/42534975/))。医学統計でも同じ構図と考えるのが安全で、**解析結果の妥当性は使用者が担保する**(seed 固定・手計算との突合・生成コードの逐行読解)
- **Copilot Studio**: 事前承認・予約案内・院内 FAQ など定型対話業務のカスタムエージェントをノーコードで構築する基盤。米国では Dragon Copilot のパートナーマーケットプレイスと接続し、収益サイクル管理や prior auth のエージェントが実装され始めている
- **自前配備という選択肢**: 眼科手術記録の生成をローカル配備 LLM + human-in-the-loop で行い、商用クラウド型と比較した報告 ([Int J Med Inform, PMID 42570565](https://pubmed.ncbi.nlm.nih.gov/42570565/))。データを院内から出せない事情がある日本の施設にとって、「クラウド Copilot か、諦めるか」の二択でないことを示す実例。過酷環境での手技支援 copilot ([Mil Med, PMID 42560246](https://pubmed.ncbi.nlm.nih.gov/42560246/)) も含め、**scribe の外側**にアシスタントの用途が広がりつつある

### 6. ガバナンス — 日本で使うときの規範レイヤー
日本の医療機関で Copilot 系を使う場合、参照すべき規範は概ね4層:

1. **3省2ガイドライン**: 厚労省「医療情報システムの安全管理に関するガイドライン 第6.0版」(2023-05) + 経産省・総務省ガイドライン。クラウドサービス選定・委託管理の土台
2. **[医療・ヘルスケア分野における生成AI利用ガイドライン 第2版](https://haip-cip.org/assets/documents/nr_20241002_02.pdf)** (医療AIプラットフォーム技術研究組合、2025-07、厚労科研の成果): 医療機関・薬局での生成AI利用の実務上の注意点を用例ベースで整理。**現場ルール作りの一次参照**
3. **個人情報保護法**: 診療情報は要配慮個人情報。プロンプトに患者特定情報を入れない・入れる場合は匿名加工と契約 (学習利用の有無、データ所在) の確認が前提。ambient 録音には**患者への説明と同意**の設計が要る
4. **制度の追い風**: AI 推進法 (2025年成立)、2026年度診療報酬改定での AI・ICT 活用促進の明記 (二次情報: [医療AI規制の2026年時点解説](https://hirotsu.clinic/blog/%E5%8C%BB%E7%99%82ai%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%AB%E3%81%AF%E3%81%A9%E3%81%86%E3%81%AA%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%EF%BC%9F2026%E5%B9%B4%E6%99%82%E7%82%B9%E3%81%AE%E6%97%A5%E6%9C%AC%E3%81%AE%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%A8%E6%B3%95%E8%A6%8F%E5%88%B6%E3%82%92%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F%E8%A7%A3%E8%AA%AC/)。原文未確認のため参考情報)

⚠️ よくある事故パターン: ①個人契約の Copilot/ChatGPT に症例を貼る ②AI 下書きを未レビューでカルテ確定 ③議事録 AI に人事・懲戒等の機微会議を無断で聞かせる — いずれも技術でなく**運用ルールの不在**が原因。1枚ものの院内利用ルール (してよい業務・禁止業務・確認手順) が最小の防具。

海外の規範議論も動いている。英国では規制当局が医師の AI scribe 利用に関する見解を更新 ([BMJ, PMID 42575564](https://pubmed.ncbi.nlm.nih.gov/42575564/))。精神科領域では「AI scribe は録音・転記・生成という異なる操作を一括りにしている」として、臨床的監督・同意・規制を分けて設計すべきとの論考 ([Lancet Psychiatry, PMID 42586083](https://pubmed.ncbi.nlm.nih.gov/42586083/))。そして2026年に出てきた**問いの立て直し**が実務的に効く — 「法的に何が許されるか」「商業的に何が行われているか」の手前に、**その録音は何のためにあるのか**を院内で先に決めよという政策論で、ambient AI を医療安全と臨床監査 (clinical audit) の枠組みに接続することを提案する ([Front Digit Health, PMID 42676690](https://pubmed.ncbi.nlm.nih.gov/42676690/))。録音を「文書作成の副産物」でなく「監査可能な診療記録」と位置づけるなら、保存期間・アクセス権・患者の閲覧請求まで設計が変わる。感受性の高い診療科 (精神科・小児思春期 [PMID 42592885](https://pubmed.ncbi.nlm.nih.gov/42592885/)) ほど同意設計と成果への説明責任が重くなる。

### 7. 家庭医の机の上での使い方 — 実践の型
「大病院の導入プロジェクト」を待たなくても、M365 環境があれば今日から使える型:

- **紹介状・報告書の骨子**: 「50代、2型糖尿病、○○の精査目的で消化器内科へ紹介。紹介状の骨子を敬体で」→ 骨子だけ作らせ、臨床内容は自分で埋める。**患者名・ID・生年月日等の特定情報は入れない**
- **委員会・カンファの議事録**: Teams 録画から要約と TODO 抽出 → 叩き台にして自分の言葉で確定。録音対象者への周知が前提
- **勉強会・患者説明資料**: 「研修医向けに○○の勉強会スライド構成案を10枚で」「この説明を中学生にも分かる言葉に」— 教材の初速が大きく変わる (患者向け要約は読みやすさが独立の課題: [PMID 42622804](https://pubmed.ncbi.nlm.nih.gov/42622804/))
- **データ集計**: Excel Copilot に「この列から月別の件数推移を」— 関数とピボットの下書きに。数値の検算は自分で
- **文献下調べ**: Copilot Chat には**必ず出典リンクを要求**し、原文に当たってから引用する。要約の孫引きはしない
- **3点セットの型 (全用途共通)**: ①匿名化してから渡す ②出力は「下書き」と宣言して扱う ③自分の目で全文確認してから使う

将来 ambient scribe が国内でも使えるようになったときのために、英国の一般診療で始まった「**助けか妨げか**」の論争は先に読んでおく価値がある ([Br J Gen Pract, PMID 42532861](https://pubmed.ncbi.nlm.nih.gov/42532861/))。争点は精度ではなく**診察の質**にある — 沈黙や言い淀みが要約から落ちること、患者が「記録される」と意識して語りを変えること、要約という行為が持つ選別の権力。家庭医療の研修現場のパイロット ([PRiMER, PMID 42518625](https://pubmed.ncbi.nlm.nih.gov/42518625/)) と合わせて読むと、実務上の備えは2つに絞れる: **録音を止める判断を自分の手に残しておくこと**と、**浮いた時間を何に使うかを先に決めておくこと** (§3 の staffing trap)。

### 8. 日本での現在地と見通し (要ウォッチ)
- **Dragon Copilot の国内提供は本格化前** (2026-09時点)。2025年3月の発表は日本語でも行われたが ([Windows Blog Japan](https://blogs.windows.com/japan/2025/03/17/a-deeper-look-at-microsoft-dragon-copilot-transforming-clinical-workflow-with-ai/))、一般提供は米国・カナダから段階展開中。58言語対応の進展と国内電子カルテベンダーとの接続が普及の鍵
- **非英語圏の先例が出た意味**: スペイン語外来での230万回規模の実地評価 ([PMID 42518737](https://pubmed.ncbi.nlm.nih.gov/42518737/)) は、言語対応が「翻訳できるか」ではなく「**その言語の臨床語彙と診療様式に馴染むか**」の問題であることを、意味的一致という指標で測って見せた。日本語版が来たときの評価軸としてそのまま使える。逆に通訳介在時の誤り伝播 ([PMID 42520279](https://pubmed.ncbi.nlm.nih.gov/42520279/)) は、多言語対応が進むほど検証負担が増えることを示す
- 国内では **AmiVoice 系の医療音声認識**や **ユビーの AI 問診**など、部分機能を担う国産勢が先行。ambient scribe 型の国産サービスも出始めており、Copilot 一強ではない。院内オンプレ配備という第三の道 ([PMID 42570565](https://pubmed.ncbi.nlm.nih.gov/42570565/)) も選択肢に入る
- **電子カルテ情報共有サービスは2026年度冬頃の全国展開開始を目指す**段階 (モデル事業9地域の課題対応中) — 標準型電子カルテ・情報共有基盤が整うほど、ambient AI の書き込み先としての価値が上がる。制度と製品の交点を継続ウォッチ。制度側の詳細は姉妹ノート [ehr-sharing-service](ehr-sharing-service.md) へ
<!-- LN:SYNTHESIS:END -->

## 📚 文献リスト
<!-- LN:BIB:START -->
- Razaghi ら. Transforming clinical documentation with ambient artificial intelligence (AI) scribes: a narrative review of technology, impact, and implementation. Cardiovasc Diagn Ther. [PMID: 41815573](https://pubmed.ncbi.nlm.nih.gov/41815573/)
- AI Scribes in Health Care: Balancing Transformative Potential With Responsible Integration. [PMC12316405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12316405/)
- Ambient Artificial Intelligence Scribes: A Pilot Survey of Perspectives on the Utility and Documentation Burden in Palliative Medicine. [PMC12427878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12427878/)
- A Randomized-Clinical Trial of Two Ambient Artificial Intelligence Scribes: Measuring Documentation Efficiency and Physician Burnout. medRxiv (preprint). [doi:10.1101/2025.07.10.25331333](https://doi.org/10.1101/2025.07.10.25331333)

初回収集 2026-09-01 (25件):
- Svetly A ら. Large-Scale Implementation of Ambient AI Documentation (DAX Copilot) and Its Effects on EHR Efficiency and Clinician Well-Being. *Appl Clin Inform* (2026). [PMID 42618038](https://pubmed.ncbi.nlm.nih.gov/42618038/)
- Moura L ら. Comparative effectiveness of ambient documentation tools in primary care — tool-specific variations. *JAMIA Open* (2026). [PMID 42583084](https://pubmed.ncbi.nlm.nih.gov/42583084/)
- Kashiouris MG ら. The Effect of Ambient AI Documentation on Clinician Workload, Efficiency, and Patient Experience in a Multisite ED Network. *Appl Clin Inform* (2026). [PMID 42628943](https://pubmed.ncbi.nlm.nih.gov/42628943/)
- Gancz L ら. Ambient AI Scribes in the Emergency Department: A Scoping Review. *J Emerg Med* (2026). [PMID 42585863](https://pubmed.ncbi.nlm.nih.gov/42585863/)
- Nguyen OT ら. Ambient AI Scribes in Ambulatory Care: Patient Acceptability and Trust. *Appl Clin Inform* (2026). [PMID 42648708](https://pubmed.ncbi.nlm.nih.gov/42648708/)
- Merlino A ら. Accelerating ambient AI scribe enterprise-scale deployment: Cleveland Clinic's approach. *Npj Health Syst* (2026). [PMID 42581183](https://pubmed.ncbi.nlm.nih.gov/42581183/)
- Ostherr K ら. Ambient scribes as narrative technologies. *Lancet* (2026). [PMID 42612661](https://pubmed.ncbi.nlm.nih.gov/42612661/)
- Roth AS ら. AI scribe functions in psychiatric practice: clinical oversight, consent, and regulation. *Lancet Psychiatry* (2026). [PMID 42586083](https://pubmed.ncbi.nlm.nih.gov/42586083/)
- Armstrong S. AI scribes: UK regulator issues update on use of technology by doctors. *BMJ* (2026). [PMID 42575564](https://pubmed.ncbi.nlm.nih.gov/42575564/)
- Atiku S ら. Socio-Technical Mechanisms Shaping AI Scribe Documentation Failures: A Netnographic Study. *J Eval Clin Pract* (2026). [PMID 42594260](https://pubmed.ncbi.nlm.nih.gov/42594260/)
- Shono Y. Governing the attention dividend: AI-reclaimed clinician capacity as a health policy resource. *Health Aff Sch* (2026). [PMID 42582985](https://pubmed.ncbi.nlm.nih.gov/42582985/)
- Togunwa TO ら. Ambient AI Scribes as Emerging Infrastructure in the Learning Health System. *Learn Health Syst* (2026). [PMID 42578243](https://pubmed.ncbi.nlm.nih.gov/42578243/)
- Glauser W. AI Scribes Move Quickly Into Canadian Care Settings. *J Med Internet Res* (2026). [PMID 42605518](https://pubmed.ncbi.nlm.nih.gov/42605518/)
- Abernethy J ら. Integrating AI Scribes into Medical Education: Guardrails for Preserving Clinical Reasoning (Correction). *J Gen Intern Med* (2026). [PMID 42624999](https://pubmed.ncbi.nlm.nih.gov/42624999/)
- Robinson EJ ら. Ambient AI Scribes in Urology: Early Lessons From a Single-System Implementation. *Urol Pract* (2026). [PMID 42647682](https://pubmed.ncbi.nlm.nih.gov/42647682/)
- Adan FO ら. AI Scribes in Orthopaedic Surgery: A Narrative Review. *JAAOS Glob Res Rev* (2026). [PMID 42627719](https://pubmed.ncbi.nlm.nih.gov/42627719/)
- Schlesinger N ら. Physician burnout in rheumatology: are medical scribes part of the solution? *Clin Rheumatol* (2026). [PMID 42576096](https://pubmed.ncbi.nlm.nih.gov/42576096/)
- Misa Garcia A ら. Beyond documentation: could AI scribes transform hospital pharmacy practice? *Eur J Hosp Pharm* (2026). [PMID 42595442](https://pubmed.ncbi.nlm.nih.gov/42595442/)
- Huang YH ら. Ambient voice technology in CAMHS — from documentation relief to outcome-accountable implementation. *Child Adolesc Ment Health* (2026). [PMID 42592885](https://pubmed.ncbi.nlm.nih.gov/42592885/)
- Paulus MP ら. Responsible and innovative AI for mental health care: five priority themes. *NPP Digit Psychiatry Neurosci* (2026). [PMID 42624890](https://pubmed.ncbi.nlm.nih.gov/42624890/)
- Rosner B ら. The CODEX action incubator: diagnostic excellence measures in the context of AI. *Diagnosis (Berl)* (2026). [PMID 42581404](https://pubmed.ncbi.nlm.nih.gov/42581404/)
- Canagarajah H ら. Perceptions, knowledge and adoption of AI in rheumatology: BSR survey. *Rheumatology (Oxford)* (2026). [PMID 42623131](https://pubmed.ncbi.nlm.nih.gov/42623131/)
- Major EL ら. Readability of AI-Generated Patient Visit Summaries in Orthopedic Surgery. *J Med Internet Res* (2026). [PMID 42622804](https://pubmed.ncbi.nlm.nih.gov/42622804/)
- Husen M ら. [AI in the preparation of clinical expert opinions in orthopedic assessment]. *Orthopadie (Heidelb)* (2026). [PMID 42616095](https://pubmed.ncbi.nlm.nih.gov/42616095/)
- Tietze M ら. Implementing America's AI Action Plan in Health Care: Impact on EHR Education. *Nurs Adm Q* (2026). [PMID 42659608](https://pubmed.ncbi.nlm.nih.gov/42659608/)

第2回収集 2026-09-08 (25件):
- Lee SY ら. Ambient AI's Value for Nursing: Will "Saving Time" Be a "Staffing Trap"? *Appl Clin Inform* (2026). [PMID 42705617](https://pubmed.ncbi.nlm.nih.gov/42705617/) / [doi:10.1055/a-2947-2383](https://doi.org/10.1055/a-2947-2383)
- Feren AP. The AI arc and interpretive drift. *Diagnosis (Berl)* (2026). [PMID 42703752](https://pubmed.ncbi.nlm.nih.gov/42703752/) / [doi:10.1515/dx-2026-0162](https://doi.org/10.1515/dx-2026-0162)
- Maher M ら. From prediction to reality: Five years of AI in healthcare — adoption, impact, and the road ahead. *Int J Med Inform* (2026). [PMID 42697156](https://pubmed.ncbi.nlm.nih.gov/42697156/) / [doi:10.1016/j.ijmedinf.2026.106685](https://doi.org/10.1016/j.ijmedinf.2026.106685)
- Endo A ら. Documentation Quality and Educational Value in AI-Assisted Feedback. *JMIR Med Educ* (2026). [PMID 42684426](https://pubmed.ncbi.nlm.nih.gov/42684426/) / [doi:10.2196/105029](https://doi.org/10.2196/105029)
- Biro J ら. A Conceptual Model for Ambient AI Adoption: Perspectives From Academia and Industry. *JMIR Med Inform* (2026). [PMID 42684418](https://pubmed.ncbi.nlm.nih.gov/42684418/) / [doi:10.2196/91098](https://doi.org/10.2196/91098)
- Misrai V ら. Using ambient AI in clinical consultations: reframing policy around clinical audit and patient safety. *Front Digit Health* (2026). [PMID 42676690](https://pubmed.ncbi.nlm.nih.gov/42676690/) / [doi:10.3389/fdgth.2026.1918841](https://doi.org/10.3389/fdgth.2026.1918841)
- Briscoe J ら. In Defense of Note Writing: Moral Formation and the Use of AI Scribes. *J Gen Intern Med* (2026). [PMID 42675252](https://pubmed.ncbi.nlm.nih.gov/42675252/) / [doi:10.1007/s11606-026-10771-2](https://doi.org/10.1007/s11606-026-10771-2)
- Teo KY ら. Nurse-Led Ambient AI Scribe for Patient Safety Incident Investigation Reports (Project NARRATE). *JMIR Nurs* (2026). [PMID 42574744](https://pubmed.ncbi.nlm.nih.gov/42574744/) / [doi:10.2196/100775](https://doi.org/10.2196/100775)
- Sorin V, Klang E. AI Scribe Safety: Measuring What Happens After Signing. *JMIR Med Inform* (2026). [PMID 42574720](https://pubmed.ncbi.nlm.nih.gov/42574720/) / [doi:10.2196/103162](https://doi.org/10.2196/103162)
- Zhang C ら. AI as a Clinical Co-Pilot: a locally deployed human-in-the-loop framework for ophthalmic surgical record generation. *Int J Med Inform* (2026). [PMID 42570565](https://pubmed.ncbi.nlm.nih.gov/42570565/) / [doi:10.1016/j.ijmedinf.2026.106651](https://doi.org/10.1016/j.ijmedinf.2026.106651)
- Grand Z ら. Optimizing Hip and Knee Arthroplasty Clinic Flow: A Prospective Evaluation of AI Scribe Technology. *Arthroplast Today* (2026). [PMID 42564601](https://pubmed.ncbi.nlm.nih.gov/42564601/) / [doi:10.1016/j.artd.2026.102095](https://doi.org/10.1016/j.artd.2026.102095)
- Zhuo Y ら. An Artificial Intelligence Copilot for First Response Medicine. *Mil Med* (2026). [PMID 42560246](https://pubmed.ncbi.nlm.nih.gov/42560246/) / [doi:10.1093/milmed/usag065](https://doi.org/10.1093/milmed/usag065)
- Daignault C ら. The use of AI scribes across medical fields and why psychiatry is lagging behind: a scoping review. *Sante Ment Que* (2026). [PMID 42550434](https://pubmed.ncbi.nlm.nih.gov/42550434/)
- Gong EJ ら. Cognitive Workload and Mental Burden in Health Care Professionals Interacting With AI: Systematic Review and Meta-Analysis. *J Med Internet Res* (2026). [PMID 42550089](https://pubmed.ncbi.nlm.nih.gov/42550089/) / [doi:10.2196/93618](https://doi.org/10.2196/93618)
- Jazayeri A, Huang JS. Incorporating ambient AI scribes into pediatric gastroenterology documentation: key considerations. *J Pediatr Gastroenterol Nutr* (2026). [PMID 42548074](https://pubmed.ncbi.nlm.nih.gov/42548074/) / [doi:10.1002/jpn3.70518](https://doi.org/10.1002/jpn3.70518)
- Knitza J, Aries P. Ambient AI scribes in rheumatology: early real-world clinician and patient experience. *EULAR Rheumatol Open* (2026). [PMID 42540133](https://pubmed.ncbi.nlm.nih.gov/42540133/) / [doi:10.1016/j.ero.2025.12.002](https://doi.org/10.1016/j.ero.2025.12.002)
- Gharmili M ら. Measuring the quality and efficiency of AI-generated codes for financial markets prediction with LSTM. *Front Artif Intell* (2026). [PMID 42534975](https://pubmed.ncbi.nlm.nih.gov/42534975/) / [doi:10.3389/frai.2026.1861067](https://doi.org/10.3389/frai.2026.1861067)
- Ladds E ら. Ambient scribes in general practice — help or hindrance? *Br J Gen Pract* (2026). [PMID 42532861](https://pubmed.ncbi.nlm.nih.gov/42532861/) / [doi:10.3399/bjgp.2026.0097](https://doi.org/10.3399/bjgp.2026.0097)
- Sangal RB ら. Real-World Adoption of Ambient Artificial Intelligence Documentation in Emergency Medicine. *Ann Emerg Med* (2026). [PMID 42524795](https://pubmed.ncbi.nlm.nih.gov/42524795/) / [doi:10.1016/j.annemergmed.2026.06.032](https://doi.org/10.1016/j.annemergmed.2026.06.032)
- Rabotin A ら. Propagation of Interpreter Errors by Ambient AI Scribes: Study Using Simulated Clinical Encounters. *JMIR Med Inform* (2026). [PMID 42520279](https://pubmed.ncbi.nlm.nih.gov/42520279/) / [doi:10.2196/88734](https://doi.org/10.2196/88734)
- Alcázar-Peral JM ら. Real-world evaluation of an ambient AI scribe in Spanish outpatient care after 2.3 million uses. *Front Digit Health* (2026). [PMID 42518737](https://pubmed.ncbi.nlm.nih.gov/42518737/) / [doi:10.3389/fdgth.2026.1874919](https://doi.org/10.3389/fdgth.2026.1874919)
- Anderson W, Koran-Scholl JB. The Impact of Ambient AI on Resident Documentation and Well-Being: A Pilot Study. *PRiMER* (2026). [PMID 42518625](https://pubmed.ncbi.nlm.nih.gov/42518625/) / [doi:10.22454/primer.2026.393770](https://doi.org/10.22454/primer.2026.393770)
- Tran V ら. Patient Acceptability, Perceptions and Concerns Regarding AI Scribes in Outpatient Dermatology Clinics. *Australas J Dermatol* (2026). [PMID 42504001](https://pubmed.ncbi.nlm.nih.gov/42504001/) / [doi:10.1111/ajd.70186](https://doi.org/10.1111/ajd.70186)
- Agrawal A ら. Assessing pediatric gastroenterologists' use of AI in clinical and professional tasks. *JPGN Rep* (2026). [PMID 42499718](https://pubmed.ncbi.nlm.nih.gov/42499718/) / [doi:10.1002/jpr3.70202](https://doi.org/10.1002/jpr3.70202)
- Launes C ら. [Perception of the impact of AI medical scribes on quality of care: cross-sectional study in pre-implementation phase in a pediatric hospital]. *J Healthc Qual Res* (2026). [PMID 42497486](https://pubmed.ncbi.nlm.nih.gov/42497486/) / [doi:10.1016/j.jhqr.2026.101227](https://doi.org/10.1016/j.jhqr.2026.101227)
<!-- LN:BIB:END -->

## 🔗 実務リソース (論文以外の一次資料)
- [Microsoft Dragon Copilot 製品ページ](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot)
- [Microsoft Adoption — Healthcare シナリオライブラリ](https://adoption.microsoft.com/en-us/scenario-library/healthcare/)
- [医療・ヘルスケア分野における生成AI利用ガイドライン 第2版 (HAIP, 2025-07)](https://haip-cip.org/assets/documents/nr_20241002_02.pdf)
- 厚生労働省「医療情報システムの安全管理に関するガイドライン 第6.0版」(2023-05)

## 🆕 新着ログ
<!-- LN:LOG:START -->

### ✅ 2026-09-08 収集分 (25件・編み込み済み)

- **Ambient AI's Value for Nursing: Will "Saving Time" Be a "Staffing Trap"?** — Lee SY, Wyse RJ, Jeffery AD *Appl Clin Inform* (2026). PMID [42705617](https://pubmed.ncbi.nlm.nih.gov/42705617/) / [DOI](https://doi.org/10.1055/a-2947-2383)
- **The AI arc and interpretive drift.** — Feren AP *Diagnosis (Berl)* (2026). PMID [42703752](https://pubmed.ncbi.nlm.nih.gov/42703752/) / [DOI](https://doi.org/10.1515/dx-2026-0162)
  - 抄録: Artificial intelligence now enters the clinical encounter at three points: before the visit, during clinical reasoning, and after it, when ambient tools generate the note. AI has the potential to adversely influence the diagnostic process at each of these steps. This opinion piece names interpretive…
- **From prediction to reality: Five years of AI in healthcare. Adoption, impact, and the road ahead.** — Maher M, Khan I, ElFouly I *Int J Med Inform* (2026). PMID [42697156](https://pubmed.ncbi.nlm.nih.gov/42697156/) / [DOI](https://doi.org/10.1016/j.ijmedinf.2026.106685)
  - 抄録: The 2020 EIT Health & McKinsey report Transforming Healthcare with AI was among the most cited forecasts shaping expectations for AI adoption in healthcare. It predicted early gains in administrative automation and medical imaging, then remote monitoring and natural language processing (NLP), and ev…
- **Documentation Quality and Educational Value in AI-Assisted Feedback.** — Endo A, Kimura T, Kataoka Y *JMIR Med Educ* (2026). PMID [42684426](https://pubmed.ncbi.nlm.nih.gov/42684426/) / [DOI](https://doi.org/10.2196/105029)
- **A Conceptual Model for Ambient AI Adoption: Perspectives From Academia and Industry.** — Biro J, Pines JM, Jayaraman S et al. *JMIR Med Inform* (2026). PMID [42684418](https://pubmed.ncbi.nlm.nih.gov/42684418/) / [DOI](https://doi.org/10.2196/91098)
  - 抄録: Ambient AI technologies are increasingly marketed as solutions to reduce clinician burden and improve care efficiency; however, real-world performance varies widely across clinical settings. Health care provider organizations face challenges in determining which aspects of ambient AI performance mat…
- **Using ambient AI in clinical consultations: reframing policy around clinical audit and patient safety.** — Misrai V, Bruchon A, Dasgupta P et al. *Front Digit Health* (2026). PMID [42676690](https://pubmed.ncbi.nlm.nih.gov/42676690/) / [DOI](https://doi.org/10.3389/fdgth.2026.1918841)
  - 抄録: Recent work has mapped what is legally permitted, commercially practiced, and technically coming for ambient AI in clinical care, yet it has not addressed the prior question of what the recording is for. This Perspective offers a policy argument, not an empirical evaluation. Documentation, workflow …
- **In Defense of Note Writing: Moral Formation and the Use of AI Scribes.** — Briscoe J, Elmore M, Tanzillo D et al. *J Gen Intern Med* (2026). PMID [42675252](https://pubmed.ncbi.nlm.nih.gov/42675252/) / [DOI](https://doi.org/10.1007/s11606-026-10771-2)
  - 抄録: Current discourse surrounding the use of AI note-writing scribes has focused primarily on questions of privacy, accuracy, and efficiency. Such analyses view note-writing as primarily serving summative and communicative purposes-tasks that can be offloaded to AI to relieve clinicians' documentation b…
- **Nurse-Led Ambient AI Scribe for Patient Safety Incident Investigation Reports (Project NARRATE): Retrospective Pre-Post Comparative Document-Quality Study.** — Teo KY, Huang L, Woh KCY et al. *JMIR Nurs* (2026). PMID [42574744](https://pubmed.ncbi.nlm.nih.gov/42574744/) / [DOI](https://doi.org/10.2196/100775)
  - 抄録: Patient safety investigation reports support organizational learning only when they are complete, usable, and sufficiently detailed. Conventional free-text reports are often inconsistent and may omit information needed for review and learning. Project NARRATE (Nursing AI-Refined for Accurate Transcr…
- **AI Scribe Safety: Measuring What Happens After Signing.** — Sorin V, Klang E *JMIR Med Inform* (2026). PMID [42574720](https://pubmed.ncbi.nlm.nih.gov/42574720/) / [DOI](https://doi.org/10.2196/103162)
  - 抄録: Coiera and Fraile-Navarro question whether AI scribes are being evaluated on metrics that truly impact care. While current evaluations focus on the quality of the initial draft, signed clinical notes are dynamic, as their content can be copied, summarized, coded, and re-ingested by downstream AI too…
- **AI as a Clinical Co-Pilot: A Comparative Evaluation of a Locally Deployed Human-in-the-Loop Framework for Ophthalmic Surgical Record Generation.** — Zhang C, Mao W, Chen H et al. *Int J Med Inform* (2026). PMID [42570565](https://pubmed.ncbi.nlm.nih.gov/42570565/) / [DOI](https://doi.org/10.1016/j.ijmedinf.2026.106651)
- **Optimizing Hip and Knee Arthroplasty Clinic Flow: A Prospective Evaluation of Artificial Intelligence Scribe Technology.** — Grand Z, Brutti J, Greer K et al. *Arthroplast Today* (2026). PMID [42564601](https://pubmed.ncbi.nlm.nih.gov/42564601/) / [DOI](https://doi.org/10.1016/j.artd.2026.102095)
  - 抄録: The increasing burden of clinical documentation contributes to physician inefficiency and burnout, with electronic health record implementation significantly increasing documentation time from 16% to 28% of clinical time. While human medical scribes have shown benefits, artificial intelligence (AI) …
- **An Artificial Intelligence Copilot for First Response Medicine.** — Zhuo Y, Radman M, Zhang E et al. *Mil Med* (2026). PMID [42560246](https://pubmed.ncbi.nlm.nih.gov/42560246/) / [DOI](https://doi.org/10.1093/milmed/usag065)
  - 抄録: First responders in emergency medicine often work in austere conditions where expert consultation is limited, communication networks are unreliable, and rapid decision-making is essential. In these environments, procedural precision directly impacts patient outcomes. To address these challenges, we …
- **The use of AI scribes across medical fields and why psychiatry is lagging behind: A scoping review.** — Daignault C, Audelin-Rinfret J, Désilets M et al. *Sante Ment Que* (2026). PMID [42550434](https://pubmed.ncbi.nlm.nih.gov/42550434/)
  - 抄録: Objective This scoping review aimed to examine the current available literature on the use of artificial intelligence (AI) scribes across all medical fields compared to their use in psychiatry. Methods A scoping review was conducted following the Preferred Reporting Items for Systematic Reviews and …
- **Cognitive Workload and Mental Burden in Health Care Professionals Interacting With AI: Systematic Review and Meta-Analysis.** — Gong EJ, Bang CS, Lee JJ *J Med Internet Res* (2026). PMID [42550089](https://pubmed.ncbi.nlm.nih.gov/42550089/) / [DOI](https://doi.org/10.2196/93618)
  - 抄録: AI adoption in health care has accelerated rapidly, with ambient documentation tools, diagnostic imaging AI, and clinical decision support systems (CDSSs) entering routine practice. However, the cognitive demands placed on clinicians supervising these systems remain understudied. Specifically, the c…
- **Incorporating ambient artificial intelligence scribes into pediatric gastroenterology documentation: Key considerations.** — Jazayeri A, Huang JS *J Pediatr Gastroenterol Nutr* (2026). PMID [42548074](https://pubmed.ncbi.nlm.nih.gov/42548074/) / [DOI](https://doi.org/10.1002/jpn3.70518)
- **Ambient AI scribes in rheumatology: early real-world clinician and patient experience.** — Knitza J, Aries P *EULAR Rheumatol Open* (2026). PMID [42540133](https://pubmed.ncbi.nlm.nih.gov/42540133/) / [DOI](https://doi.org/10.1016/j.ero.2025.12.002)
- **Measuring the quality and efficiency of AI-generated codes for financial markets prediction with LSTM.** — Gharmili M, Aatif Y, Abdelkamel A *Front Artif Intell* (2026). PMID [42534975](https://pubmed.ncbi.nlm.nih.gov/42534975/) / [DOI](https://doi.org/10.3389/frai.2026.1861067)
  - 抄録: Generative AI coding assistants are increasingly used to write machine-learning code, yet their ability to produce reliable LSTM implementations for financial prediction remains underexplored. This study evaluates the LSTM code generated by seven assistants ChatGPT 4.5, GitHub Copilot, Deepseek 3, P…
- **Ambient scribes in general practice - help or hindrance?** — Ladds E, Barry E, Dixon S et al. *Br J Gen Pract* (2026). PMID [42532861](https://pubmed.ncbi.nlm.nih.gov/42532861/) / [DOI](https://doi.org/10.3399/bjgp.2026.0097)
- **Real-World Adoption of Ambient Artificial Intelligence Documentation in Emergency Medicine.** — Sangal RB, Lin KZ, Rothenberg C et al. *Ann Emerg Med* (2026). PMID [42524795](https://pubmed.ncbi.nlm.nih.gov/42524795/) / [DOI](https://doi.org/10.1016/j.annemergmed.2026.06.032)
- **Propagation of Interpreter Errors by Ambient AI Scribes: Study Using Simulated Clinical Encounters.** — Rabotin A, Aguilar E, Sandoval Gonzalez S et al. *JMIR Med Inform* (2026). PMID [42520279](https://pubmed.ncbi.nlm.nih.gov/42520279/) / [DOI](https://doi.org/10.2196/88734)
  - 抄録: In simulated English and Spanish clinical encounters, ambient AI scribes propagated interpreter errors into clinical notes, with patterns varying by speaker role and error type. These findings highlight the need for further evaluation of AI-scribe performance in multilingual and interpreter-mediated…
- **Real-world evaluation of an ambient AI scribe in Spanish outpatient care after 2.3 million uses: impact on clinician experience, semantic agreement, and workflow efficiency.** — Alcázar-Peral JM, Álvaro-de la Parra JA, Blanco D et al. *Front Digit Health* (2026). PMID [42518737](https://pubmed.ncbi.nlm.nih.gov/42518737/) / [DOI](https://doi.org/10.3389/fdgth.2026.1874919)
  - 抄録: Ambient artificial intelligence (AI) documentation systems have emerged as a promising strategy to reduce electronic health record burden and support patient-centered, value-based healthcare (VBHC). Early studies report gains in efficiency and clinician well-being, but large-scale evaluations outsid…
- **The Impact of Ambient AI on Resident Documentation and Well-Being: A Pilot Study.** — Anderson W, Koran-Scholl JB *PRiMER* (2026). PMID [42518625](https://pubmed.ncbi.nlm.nih.gov/42518625/) / [DOI](https://doi.org/10.22454/primer.2026.393770)
  - 抄録: Burnout among family medicine residents remains a significant challenge, often exacerbated by electronic health record (EHR) documentation burden.1 Emerging technologies such as ambient artificial intelligence (AI), may reduce clinical documentation time while simultaneously enhancing work satisfact…
- **Patient Acceptability, Perceptions and Concerns Regarding Artificial Intelligence Scribes in Outpatient Dermatology Clinics.** — Tran V, Lau LDW, Lee S et al. *Australas J Dermatol* (2026). PMID [42504001](https://pubmed.ncbi.nlm.nih.gov/42504001/) / [DOI](https://doi.org/10.1111/ajd.70186)
  - 抄録: This cross-sectional survey assessed patient acceptability, perceptions and concerns regarding ambient artificial intelligence (AI) scribes in an outpatient dermatology clinic. Most patients reported comfort with AI scribe use (82.1%) despite limited prior exposure, although over half expressed conc…
- **Assessing pediatric gastroenterologists' use of artificial intelligence in clinical and professional tasks.** — Agrawal A, Guntupalli V, Teitelbaum JE et al. *JPGN Rep* (2026). PMID [42499718](https://pubmed.ncbi.nlm.nih.gov/42499718/) / [DOI](https://doi.org/10.1002/jpr3.70202)
  - 抄録: Artificial intelligence (AI) has demonstrated potential to enhance clinical efficiency. However, its real-world adoption among pediatric gastroenterologists (GIs) remains poorly characterized. The primary objective of this study was to assess how pediatric GIs are currently utilizing AI. Secondary o…
- **[Perception of the impact of AI medical scribes on quality of care: cross-sectional study in pre-implementation phase in a pediatric hospital].** — Launes C, González-Grado C, Codorniu J et al. *J Healthc Qual Res* (2026). PMID [42497486](https://pubmed.ncbi.nlm.nih.gov/42497486/) / [DOI](https://doi.org/10.1016/j.jhqr.2026.101227)
  - 抄録: Ambient artificial intelligence scribes (AI scribes) are emerging as tools to optimize clinical documentation, although the need persists to evaluate their comprehensive impact on quality of care beyond operational efficiency. The aim of this study is to explore the perception of medical professiona…

### ✅ 2026-09-01 収集分 (25件・初回の織りで編み込み済み)

- **Implementing America's AI Action Plan in Health Care: Impact on Student and Practice-Based EHR Education.** — Tietze M, Tellson A, Varghese A et al. *Nurs Adm Q* (2026). PMID [42659608](https://pubmed.ncbi.nlm.nih.gov/42659608/) / [DOI](https://doi.org/10.1097/naq.0000000000000776)
  - 抄録: National artificial intelligence (AI) policy in the United States is accelerating rapidly through initiatives such as America's AI Action Plan, creating urgency for health care organizations to respond. Although these policies are not health care-specific, their implementation has immediate implicat…
- **Ambient Artificial Intelligence Scribes in Ambulatory Care: Patient Acceptability and Trust.** — Nguyen OT, Afshar M, Jaeb MA et al. *Appl Clin Inform* (2026). PMID [42648708](https://pubmed.ncbi.nlm.nih.gov/42648708/) / [DOI](https://doi.org/10.1055/a-2936-9935)
  - 抄録: BACKGROUND: Ambient artificial intelligence (AI) scribes may improve clinician-level outcomes (e.g., documentation burden) and patient experience. However, patients must agree to allow clinicians to use ambient AI scribes for these benefits to materialize. What motivates patients to agree to these t…
- **Ambient Artificial Intelligence Scribes in Urology: Early Lessons From a Single-System Implementation.** — Robinson EJ, Chen IK, Baecker AS et al. *Urol Pract* (2026). PMID [42647682](https://pubmed.ncbi.nlm.nih.gov/42647682/) / [DOI](https://doi.org/10.1097/upj.0000000000001070)
- **The Effect of Ambient AI Documentation on Clinician Workload, Efficiency, and Patient Experience in a Multisite Emergency Department Network.** — Kashiouris MG, Miner A, Saleh S et al. *Appl Clin Inform* (2026). PMID [42628943](https://pubmed.ncbi.nlm.nih.gov/42628943/) / [DOI](https://doi.org/10.1055/a-2939-3038)
  - 抄録: Evaluation of ambient AI on patient experience, documentation efficiency, clinician workload, and clinical throughput across a large emergency department (ED) network. Retrospective, observational cohort study of ambient AI rollout across 14 EDs (May 2024-June 2025). Clinicians applied the tool on a…
- **Artificial Intelligence Scribes in Orthopaedic Surgery: A Narrative Review.** — Adan FO, Agoro KS, Rao V et al. *J Am Acad Orthop Surg Glob Res Rev* (2026). PMID [42627719](https://pubmed.ncbi.nlm.nih.gov/42627719/) / [DOI](https://doi.org/10.5435/jaaosglobal-d-25-00398)
  - 抄録: The growing applications of artificial intelligence (AI) is transforming the healthcare landscape by reshaping diagnostics, workflow operations, and clinical decision making. Among its most promising application in surgery is the development of AI scribes designed to reduce the burden of documentati…
- **Correction: Integrating AI Scribes into Medical Education: Guardrails for Preserving Clinical Reasoning.** — Abernethy J, Shah A, Chen B et al. *J Gen Intern Med* (2026). PMID [42624999](https://pubmed.ncbi.nlm.nih.gov/42624999/) / [DOI](https://doi.org/10.1007/s11606-026-10726-7)
- **Responsible and innovative AI for mental health care: five priority themes.** — Paulus MP, Torous J, Perlis RH et al. *NPP Digit Psychiatry Neurosci* (2026). PMID [42624890](https://pubmed.ncbi.nlm.nih.gov/42624890/) / [DOI](https://doi.org/10.1038/s44277-026-00068-x)
  - 抄録: Artificial intelligence (AI) has entered psychiatry at scale, yet its clinical impact remains constrained by a sizable gap between technical validation and real-world implementation. The central barriers are no longer computational, but infrastructural: unreliable measurement systems, incomplete gov…
- **Perceptions, knowledge and adoption of artificial intelligence in rheumatology: results from a British Society for Rheumatology survey.** — Canagarajah H, Saha P, Tsigarides J et al. *Rheumatology (Oxford)* (2026). PMID [42623131](https://pubmed.ncbi.nlm.nih.gov/42623131/) / [DOI](https://doi.org/10.1093/rheumatology/keag454)
  - 抄録: Artificial intelligence (AI) and machine learning applications are rapidly expanding across healthcare. Successful implementation of AI technologies in rheumatology will depend not only on technical performance but also on the perceptions and preparedness of end-users. This study evaluated the curre…
- **Readability of AI-Generated Patient Visit Summaries in Orthopedic Surgery: Retrospective Analysis.** — Major Iii EL, Shah VP, Carroll AN et al. *J Med Internet Res* (2026). PMID [42622804](https://pubmed.ncbi.nlm.nih.gov/42622804/) / [DOI](https://doi.org/10.2196/87283)
  - 抄録: Patient visit summaries (PVS) are patient-facing documents intended to reinforce communication and promote patient education after clinical encounters. Despite national recommendations that patient education materials be written at or below a sixth-grade reading level, most orthopedic materials subs…
- **Large-Scale Implementation of Ambient AI Documentation and Its Effects on EHR Efficiency and Clinician Well-Being.** — Svetly A, Razzouk E, McLean M et al. *Appl Clin Inform* (2026). PMID [42618038](https://pubmed.ncbi.nlm.nih.gov/42618038/) / [DOI](https://doi.org/10.1055/a-2936-7516)
  - 抄録: Ambient clinical documentation tools are increasingly used to reduce administrative burden and improve provider experience. However, evidence describing their effects at scale across large, multi-site health systems remains limited. To evaluate the effect of Dragon Ambient eXperience (DAX) Copilot o…
- **[Artificial intelligence in the preparation of clinical expert opinions : Current evidence, use cases, and limitations in orthopedic assessment].** — Husen M, Gaidzik PW, Schiltenwolf M *Orthopadie (Heidelb)* (2026). PMID [42616095](https://pubmed.ncbi.nlm.nih.gov/42616095/) / [DOI](https://doi.org/10.1007/s00132-026-04876-z)
  - 抄録: Generative AI, large language models, and ambient AI systems are rapidly being integrated into documentation-related processes in medicine. However, the data available for orthopedic expert reports is significantly less extensive than that or general clinical documentation. What evidence exists by J…
- **Ambient scribes as narrative technologies.** — Ostherr K, Engebretsen E, Woods A *Lancet* (2026). PMID [42612661](https://pubmed.ncbi.nlm.nih.gov/42612661/) / [DOI](https://doi.org/10.1016/s0140-6736(26)01381-4)
  - 抄録: Ambient scribes, also known as artificial intelligence-powered voice-to-text technology, are widely cited as time-saving tools that reduce administrative burden for clinicians. Yet, in their current use, these tools pose substantial, often unacknowledged risks that threaten to undermine patient-cent…
- **AI Scribes Move Quickly Into Canadian Care Settings.** — Glauser W *J Med Internet Res* (2026). PMID [42605518](https://pubmed.ncbi.nlm.nih.gov/42605518/) / [DOI](https://doi.org/10.2196/108859)
  - 抄録: Increasing use of AI scribes in clinics and health care settings in Canada and the release of the recent Auditor General of Ontario report have sparked ongoing debate. In this News and Perspectives article, JMIR Correspondent Wendy Glauser reports on physician perspectives about the potential benefi…
- **Beyond documentation: could artificial intelligence (AI) scribes transform hospital pharmacy practice?** — Misa Garcia A, Ferro Rodríguez S *Eur J Hosp Pharm* (2026). PMID [42595442](https://pubmed.ncbi.nlm.nih.gov/42595442/) / [DOI](https://doi.org/10.1136/ejhpharm-2026-005272)
- **Evaluation of Socio-Technical Mechanisms Shaping AI Scribe Documentation Failures: A Netnographic Study.** — Atiku S, Owolanke K, Olakotan O *J Eval Clin Pract* (2026). PMID [42594260](https://pubmed.ncbi.nlm.nih.gov/42594260/) / [DOI](https://doi.org/10.1111/jep.70554)
  - 抄録: Artificial Intelligence (AI) scribes are increasingly adopted to address electronic health record (EHR) documentation burden. Although early evaluations report perceived efficiency gains and reduced after-hours work, findings on documentation quality and safety remain mixed. Reported issues, includi…
- **Letter to the Editor: Ambient voice technology in CAMHS - from documentation relief to outcome-accountable implementation.** — Huang YH, Wei LC *Child Adolesc Ment Health* (2026). PMID [42592885](https://pubmed.ncbi.nlm.nih.gov/42592885/) / [DOI](https://doi.org/10.1111/camh.70119)
  - 抄録: Ambient voice technology has been proposed as a promising approach to reduce documentation burden in child and adolescent mental health services and neurodevelopmental settings. In response to Dineley and colleagues' discussion of responsible implementation and evidence gaps, this letter argues that…
- **AI scribe functions in psychiatric practice: clinical oversight, consent, and regulation.** — Roth AS, Ayers NB *Lancet Psychiatry* (2026). PMID [42586083](https://pubmed.ncbi.nlm.nih.gov/42586083/) / [DOI](https://doi.org/10.1016/s2215-0366(26)00201-4)
  - 抄録: Ambient artificial intelligence (AI) documentation tools, known as AI scribes, have entered psychiatric clinical practice, bundling at least three operations into a single workflow, without sufficient attention to the differences among them. In this Personal View, we argue that AI-generated clinical…
- **Ambient Artificial Intelligence Scribes in the Emergency Department: A Scoping Review of Current Evidence.** — Gancz L, Duffy EI, Mathies I et al. *J Emerg Med* (2026). PMID [42585863](https://pubmed.ncbi.nlm.nih.gov/42585863/) / [DOI](https://doi.org/10.1016/j.jemermed.2026.05.043)
  - 抄録: Burnout affects nearly half of physicians in the United States, with emergency physicians (EPs) at particularly high risk. Documentation burden contributes to burnout. Artificial intelligence (AI) ambient scribes have emerged as a potential strategy to reduce documentation workload. While benefits h…
- **Comparative effectiveness of ambient documentation tools in primary care tool-specific variations in efficiency, documentation burden, and productivity over time.** — Moura L, Mishuris RG, Metlay JP et al. *JAMIA Open* (2026). PMID [42583084](https://pubmed.ncbi.nlm.nih.gov/42583084/) / [DOI](https://doi.org/10.1093/jamiaopen/ooag155)
  - 抄録: To evaluate the comparative effectiveness of ambient documentation tools (ADTs) with distinct architectures (Tablet-Based Virtual Human-Assisted Ambient [Tool A], EHR-Integrated Ambient [Tool B], and Standalone Ambient [Tool C]) on provider efficiency, documentation burden, and productivity in prima…
- **Governing the attention dividend: AI-reclaimed clinician capacity as a health policy resource.** — Shono Y *Health Aff Sch* (2026). PMID [42582985](https://pubmed.ncbi.nlm.nih.gov/42582985/) / [DOI](https://doi.org/10.1093/haschl/qxag197)
  - 抄録: Ambient artificial intelligence (AI) is reducing documentation burden in primary care, with real but modest and variable effects: reclaimed minutes in some settings, reduced cognitive load in others, and no guarantee that either reaches patients. This article argues that the resulting capacity-the a…
- **The CODEX action incubator: a consensus-driven approach to identify and implement diagnostic excellence measures in the context of artificial intelligence.** — Rosner B, Hammer M, Tabacco A et al. *Diagnosis (Berl)* (2026). PMID [42581404](https://pubmed.ncbi.nlm.nih.gov/42581404/) / [DOI](https://doi.org/10.1515/dx-2026-0112)
  - 抄録: Diagnostic errors are a substantial source of patient harm. As artificial intelligence (AI) integrates into clinical workflows, opportunities are emerging to assess their impacts on diagnostic excellence (DxEx). The Coordinating Center for Diagnostic Excellence (CODEX) at the University of Californi…
- **Accelerating ambient AI scribe enterprise-scale deployment: Cleveland Clinic's novel approach to health system-industry partnership.** — Merlino A, Blue A, Boose E et al. *Npj Health Syst* (2026). PMID [42581183](https://pubmed.ncbi.nlm.nih.gov/42581183/) / [DOI](https://doi.org/10.1038/s44401-026-00144-6)
  - 抄録: Artificial intelligence scribes are increasingly common in clinical settings, but a blueprint for deploying them efficiently at scale is lacking. We share information about the Cleveland Clinic's vendor-health system deployment partnership consisting of four pillars: governance, training and onboard…
- **Ambient AI Scribes as Emerging Infrastructure in the Learning Health System.** — Togunwa TO, Platt J *Learn Health Syst* (2026). PMID [42578243](https://pubmed.ncbi.nlm.nih.gov/42578243/) / [DOI](https://doi.org/10.1002/lrh2.70115)
  - 抄録: Ambient artificial intelligence (AI) scribes are systems that automatically generate clinical documentation from clinician-patient conversations and are being deployed at accelerating pace across US health systems. Early evaluations report reduced documentation burden, improved clinician well-being,…
- **Physician burnout in rheumatology: are medical scribes part of the solution?** — Schlesinger N, Kaufmann D, Workman M et al. *Clin Rheumatol* (2026). PMID [42576096](https://pubmed.ncbi.nlm.nih.gov/42576096/) / [DOI](https://doi.org/10.1007/s10067-026-08349-8)
  - 抄録: Retention of highly qualified physicians remains a critical priority in rheumatology and the broader medical field due to persistent physician shortages in the United States. Addressing physician well-being and burnout is therefore essential. An optimal approach to addressing burnout in the United S…
- **AI scribes: UK regulator issues update on use of technology by doctors.** — Armstrong S *BMJ* (2026). PMID [42575564](https://pubmed.ncbi.nlm.nih.gov/42575564/) / [DOI](https://doi.org/10.1136/bmj-2026-100540)
<!-- LN:LOG:END -->