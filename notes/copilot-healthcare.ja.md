---
topic: Copilot活用 (ヘルスケア) / copilot in healthcare
slug: copilot-healthcare
updated: 2026-09-01
mode: hybrid (エビデンス=PubMed自動収集・週次 / 製品・制度・活用術=手織り)
---

# 🩺 生きたノート: Copilot活用 (ヘルスケア重点) (ライブミラー)

> **これは作者の実稼働インスタンスのライブミラーです** — 本家で週1回の自動収集
> (PubMed) と織り直しが走るたび、このノートと鼓動 ([heartbeat](../data/heartbeat.json))
> がここに push されます。**最終チェック: 2026-09-01 JST — ノート更新あり。**
> **内容は AI が論文から編んだ要約であり、鵜呑みにしないでください。** 臨床判断は必ず
> 原著と主治医・現場の判断に従ってください。各記述の出典リンクから原文に当たれます。
> ⏳ = 収集済み・織り待ち / ✅ = 本文に編み込み済み。

## 📌 5行サマリ
<!-- LN:SUMMARY:START -->
- 「Copilot」は単一製品ではなく**ファミリー名**。医療で効くのは主に3系統 — 臨床文書の Dragon Copilot (ambient AI scribe)、事務・運営の Microsoft 365 Copilot、開発・研究の GitHub Copilot。混同が導入事故と契約ミスの元
- ambient AI scribe は「実験段階」を脱しつつある: Dragon Copilot は10万人超の臨床医が利用、NHS England は M365 Copilot を**50.5万人に全面展開**(2026年10月完了予定、試験で平均43分/日の事務時間削減)
- 査読エビデンスの現在地は「**burnout には効く・時間短縮は控えめ・効果はツール固有**」: 6医療システム263人で burnout 51.9%→38.8%、1,800人規模の実測では文書作成短縮は8時間診療あたり16分、primary care の比較実測ではツール間で効果に明確な差。幻覚(~7%の報告)と記載漏れは未解決で、**サイン前の全文レビューが安全弁**
- 日本では Dragon Copilot は本格展開前。使えるのは M365 Copilot での事務・会議・資料作成が中心で、規範は**3省2ガイドライン + 医療・ヘルスケア分野生成AI利用ガイドライン第2版 (2025-07)**。患者特定情報を入れない・下書きとして扱うが2大原則
- 家庭医の机では「紹介状の骨子・委員会議事録・勉強会資料・データ集計」から小さく始めるのが定石。**匿名化してから渡す→出典を要求する→必ず自分の目で確認する**の3点セットを型にする
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

### 2. 臨床ドキュメンテーション — Dragon Copilot と ambient AI scribe の現在地
「診察の会話を聞いてカルテの下書きを作る」ambient AI scribe は、臨床 AI の中で最も速く普及した部類に入る。

- **規模**: Dragon Copilot は10万人超の臨床医が日常利用、Dragon 系 ambient 技術は650以上の医療組織に導入済み ([Microsoft Cloud Blog, HIMSS 2026](https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2026/03/05/unify-simplify-scale-microsoft-dragon-copilot-meets-the-moment-at-himss-2026/))。[Mount Sinai](https://www.mountsinai.org/about/newsroom/2025/mount-sinai-health-system-to-roll-out-microsoft-dragon-copilot) など大規模システムの採用が続く
- **機能の広がり (HIMSS 2026 発表)**: 58言語対応、ICD-10 コーディング支援、パートナーアプリ市場 (Optum・Regard 等のエージェントを Copilot 画面内で起動)。**看護向け**にはベッドサイド会話からフローシート項目への構造化入力、放射線科向け機能も ([HIT Consultant](https://hitconsultant.net/2026/03/05/microsoft-dragon-copilot-himss-2026-agentic-clinical-ai-nurses-radiologists/))
- **外来 EHR への浸透**: athenahealth が athenaOne への組み込みを発表 (2026年上半期提供) ([Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/athenahealth-integrates-dragon-copilot-ai-assistant-microsoft-moves-deeper))。Epic とは以前から深い統合
- **市場評価**: KLAS Research (2026年1月) は ambient AI を「実験的な珍しさから、測定可能なリターンを持つ運用ツールへ移行した」と評価 (上記 Microsoft ブログ経由の二次情報)
- **大規模展開の設計図が論文化され始めた**: Cleveland Clinic はベンダー協業による enterprise 展開の4本柱 (ガバナンス・研修とオンボーディング・…) を公開 ([PMID 42581183](https://pubmed.ncbi.nlm.nih.gov/42581183/))。DAX Copilot のマルチサイト大規模実装での EHR 効率・well-being への効果検証も出た ([PMID 42618038](https://pubmed.ncbi.nlm.nih.gov/42618038/))
- **地理的な広がり**: カナダでも診療所への浸透が急速で、オンタリオ州会計検査院の報告を機に便益とリスクの公開論争が始まっている ([PMID 42605518](https://pubmed.ncbi.nlm.nih.gov/42605518/))。英国では規制当局が医師の AI scribe 利用に関する見解を更新 ([BMJ, PMID 42575564](https://pubmed.ncbi.nlm.nih.gov/42575564/))

⚠️ ベンダー・導入施設発の数字 (例: オタワ病院の「burnout 70%削減・患者満足97%」) は宣伝文脈を含む。次節の査読研究と分けて読む。

### 3. エビデンスの現在地 — 効くこと・効かないこと・危ないこと
査読文献・独立調査ベースでは、絵はもう少し陰影がある:

- **burnout・主観的負担には一貫して効く**: 6医療システム263人の前後比較で burnout 有病率 51.9%→38.8% (30日間、正味13.9ポイント改善) — JAMA Network Open 掲載研究として複数の独立レビューが引用 ([IHS 解説](https://www.ihsonline.org/post/ambient-ai-medical-scribes-efficiency-gains-burnout-uncertainty-and-governance-risks))。緩和ケア領域のパイロット調査でも文書負担の主観的軽減 ([PMC12427878](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12427878/))
- **客観的な時間短縮は控えめ**: 5大学医療センター1,800人・2023-2025年の大規模実測で、8時間の診療あたり文書作成 -16分・EHR 滞在 -13分。利用は断続的な医師が多い ([STAT, 2026-04](https://www.statnews.com/2026/04/01/ai-ambient-scribes-modest-time-savings-clinical-documentation/))。「劇的な時間革命」ではなく「夜間持ち帰り仕事 (pajama time) の目に見える圧縮」と読むのが誠実
- **RCT も出始めた**: 2種の ambient AI scribe を比較するランダム化試験 (文書効率と burnout を主要評価) が preprint 段階から査読へ ([medRxiv 2025](https://www.medrxiv.org/content/10.1101/2025.07.10.25331333.full.pdf))
- **未解決の安全性課題**: 記載漏れ (omission) の頻度が高く、幻覚 (fabrication) は約7% — 14本に1本の下書きに事実でない内容が混入しうるとの報告 (二次情報: [IHS](https://www.ihsonline.org/post/ambient-ai-medical-scribes-efficiency-gains-burnout-uncertainty-and-governance-risks))。**医師のサイン前レビューを省略した瞬間に安全モデルが崩れる**
- **総説の到達点**: 技術・効果・実装をまとめた narrative review ([PMID 41815573](https://pubmed.ncbi.nlm.nih.gov/41815573/)) と、変革可能性と責任ある統合のバランスを論じる論説 ([PMC12316405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12316405/)) が入口として良い。共通する結論は「小規模・方法論多様でエビデンスはまだ限定的、標準化された評価が必要」
- **2026年の新着で解像度が上がった論点** (初回収集 2026-09-01 より):
  - **ツールによって効果が違う**: primary care で3種のアーキテクチャ (タブレット型・EHR統合型・スタンドアロン型) を比較した実測で、効率・文書負担・生産性への効果に**ツール固有の差と経時変化**が観察された ([JAMIA Open, PMID 42583084](https://pubmed.ncbi.nlm.nih.gov/42583084/))。「ambient AI 一般」でなく製品単位で評価する時代へ
  - **専門科別の検証が進む**: 救急14施設ネットワークでの後ろ向きコホート ([PMID 42628943](https://pubmed.ncbi.nlm.nih.gov/42628943/))、救急領域の scoping review ([PMID 42585863](https://pubmed.ncbi.nlm.nih.gov/42585863/))、泌尿器科・整形外科・精神科・緩和ケアでの実装報告が相次ぐ
  - **患者側の受容**: 外来患者の受容性と信頼の規定要因を調べた研究が登場 ([PMID 42648708](https://pubmed.ncbi.nlm.nih.gov/42648708/)) — 「患者が同意しなければ便益は実現しない」という当たり前の前提がようやく研究対象に
  - **批判的視点も一級誌に**: Lancet は ambient scribe を「物語の技術 (narrative technologies)」と捉え、現在の使われ方には患者中心の医療を損ないうる**見過ごされたリスク**があると論じた ([PMID 42612661](https://pubmed.ncbi.nlm.nih.gov/42612661/))。文書化の失敗を生む社会技術的メカニズムの質的研究でも品質・安全の知見は「mixed」([PMID 42594260](https://pubmed.ncbi.nlm.nih.gov/42594260/))
  - **「浮いた時間」の行き先が政策論に**: 削減された文書時間 (attention dividend) は自動的には患者に還元されない — 回収された臨床能力をどう配分するかを健康政策の資源問題として扱う議論が始まった ([PMID 42582985](https://pubmed.ncbi.nlm.nih.gov/42582985/))

### 4. 事務・運営サイド — M365 Copilot の使いどころ (NHS が実証台)
臨床記録より先に投資対効果が見えやすいのが**非臨床業務**。ここでの最大の実証例が NHS England:

- **30,000人・90組織での試験**で平均**43分/日**の事務時間削減 (年換算で1人あたり約5週間分) → **505,000人の臨床・支援スタッフへ全面展開**、2026年10月完了予定 ([TheStreet](https://www.thestreet.com/health/microsoft-and-copilot-just-hit-a-jackpot-in-healthcare-ai-nhs))
- 使い方の中心は: 会議の要約 (Teams)、定型文書・報告書の下書き、メール処理、人事・財務・調達の事務支援、経営会議資料の作成
- 医療機関向けのシナリオ集は [Microsoft Adoption の Healthcare ライブラリ](https://adoption.microsoft.com/en-us/scenario-library/healthcare/) に整理されている (スケジューリング、患者向け文書の平易化、症例カンファ準備など)

日本の医療機関でも同型のユースケース (委員会議事録、院内文書、研修資料、シフト・集計業務) は今日から成立する。**臨床判断に直結しない業務から始める**のが NHS 型の導入順序でもある。

### 5. 開発・研究サイド — GitHub Copilot / Copilot Studio
- **GitHub Copilot**: 臨床研究のデータクリーニング・統計スクリプト・可視化コードの下書きに有効。R/Python の解析コードを「書ける人」から「読める人」へ裾野を広げる。生成コードの検証責任は使用者に残る (解析結果の妥当性は自分で担保する)
- **Copilot Studio**: 事前承認・予約案内・院内 FAQ など定型対話業務のカスタムエージェントをノーコードで構築する基盤。米国では Dragon Copilot のパートナーマーケットプレイスと接続し、収益サイクル管理や prior auth のエージェントが実装され始めている

### 6. ガバナンス — 日本で使うときの規範レイヤー
日本の医療機関で Copilot 系を使う場合、参照すべき規範は概ね4層:

1. **3省2ガイドライン**: 厚労省「医療情報システムの安全管理に関するガイドライン 第6.0版」(2023-05) + 経産省・総務省ガイドライン。クラウドサービス選定・委託管理の土台
2. **[医療・ヘルスケア分野における生成AI利用ガイドライン 第2版](https://haip-cip.org/assets/documents/nr_20241002_02.pdf)** (医療AIプラットフォーム技術研究組合、2025-07、厚労科研の成果): 医療機関・薬局での生成AI利用の実務上の注意点を用例ベースで整理。**現場ルール作りの一次参照**
3. **個人情報保護法**: 診療情報は要配慮個人情報。プロンプトに患者特定情報を入れない・入れる場合は匿名加工と契約 (学習利用の有無、データ所在) の確認が前提。ambient 録音には**患者への説明と同意**の設計が要る
4. **制度の追い風**: AI 推進法 (2025年成立)、2026年度診療報酬改定での AI・ICT 活用促進の明記 (二次情報: [医療AI規制の2026年時点解説](https://hirotsu.clinic/blog/%E5%8C%BB%E7%99%82ai%E3%81%AE%E3%83%AB%E3%83%BC%E3%83%AB%E3%81%AF%E3%81%A9%E3%81%86%E3%81%AA%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%EF%BC%9F2026%E5%B9%B4%E6%99%82%E7%82%B9%E3%81%AE%E6%97%A5%E6%9C%AC%E3%81%AE%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3%E3%81%A8%E6%B3%95%E8%A6%8F%E5%88%B6%E3%82%92%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F%E8%A7%A3%E8%AA%AC/)。原文未確認のため参考情報)

⚠️ よくある事故パターン: ①個人契約の Copilot/ChatGPT に症例を貼る ②AI 下書きを未レビューでカルテ確定 ③議事録 AI に人事・懲戒等の機微会議を無断で聞かせる — いずれも技術でなく**運用ルールの不在**が原因。1枚ものの院内利用ルール (してよい業務・禁止業務・確認手順) が最小の防具。

海外の規範議論も動いている (2026-09 収集分): 英国では規制当局が医師の AI scribe 利用に関する見解を更新 ([BMJ, PMID 42575564](https://pubmed.ncbi.nlm.nih.gov/42575564/))。精神科領域では「AI scribe は録音・転記・生成という異なる操作を一括りにしている」として、臨床的監督・同意・規制を分けて設計すべきとの論考 ([Lancet Psychiatry, PMID 42586083](https://pubmed.ncbi.nlm.nih.gov/42586083/))。医学教育側からは、研修医の**臨床推論の筋力が AI scribe で衰えないためのガードレール**という新しい論点も ([J Gen Intern Med, PMID 42624999](https://pubmed.ncbi.nlm.nih.gov/42624999/))。感受性の高い診療科 (精神科・小児思春期) ほど同意設計と成果への説明責任が重くなる。

### 7. 家庭医の机の上での使い方 — 実践の型
「大病院の導入プロジェクト」を待たなくても、M365 環境があれば今日から使える型:

- **紹介状・報告書の骨子**: 「50代、2型糖尿病、○○の精査目的で消化器内科へ紹介。紹介状の骨子を敬体で」→ 骨子だけ作らせ、臨床内容は自分で埋める。**患者名・ID・生年月日等の特定情報は入れない**
- **委員会・カンファの議事録**: Teams 録画から要約と TODO 抽出 → 叩き台にして自分の言葉で確定。録音対象者への周知が前提
- **勉強会・患者説明資料**: 「研修医向けに○○の勉強会スライド構成案を10枚で」「この説明を中学生にも分かる言葉に」— 教材の初速が大きく変わる
- **データ集計**: Excel Copilot に「この列から月別の件数推移を」— 関数とピボットの下書きに。数値の検算は自分で
- **文献下調べ**: Copilot Chat には**必ず出典リンクを要求**し、原文に当たってから引用する。要約の孫引きはしない
- **3点セットの型 (全用途共通)**: ①匿名化してから渡す ②出力は「下書き」と宣言して扱う ③自分の目で全文確認してから使う

### 8. 日本での現在地と見通し (要ウォッチ)
- **Dragon Copilot の国内提供は本格化前** (2026-09時点)。2025年3月の発表は日本語でも行われたが ([Windows Blog Japan](https://blogs.windows.com/japan/2025/03/17/a-deeper-look-at-microsoft-dragon-copilot-transforming-clinical-workflow-with-ai/))、一般提供は米国・カナダから段階展開中。58言語対応の進展と国内電子カルテベンダーとの接続が普及の鍵
- 国内では **AmiVoice 系の医療音声認識**や **ユビーの AI 問診**など、部分機能を担う国産勢が先行。ambient scribe 型の国産サービスも出始めており、Copilot 一強ではない
- **電子カルテ情報共有サービスが2026年冬から全国運用開始**予定 — 標準型電子カルテ・情報共有基盤が整うほど、ambient AI の書き込み先としての価値が上がる。制度と製品の交点を継続ウォッチ
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
<!-- LN:BIB:END -->

## 🔗 実務リソース (論文以外の一次資料)
- [Microsoft Dragon Copilot 製品ページ](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot)
- [Microsoft Adoption — Healthcare シナリオライブラリ](https://adoption.microsoft.com/en-us/scenario-library/healthcare/)
- [医療・ヘルスケア分野における生成AI利用ガイドライン 第2版 (HAIP, 2025-07)](https://haip-cip.org/assets/documents/nr_20241002_02.pdf)
- 厚生労働省「医療情報システムの安全管理に関するガイドライン 第6.0版」(2023-05)

## 🆕 新着ログ
<!-- LN:LOG:START -->

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
