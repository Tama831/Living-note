---
topic: IgG4関連疾患 / igg4-related-disease
slug: igg4-related-disease
updated: 2026-08-07
---

# 🌱 生きたノート: IgG4関連疾患

> このノートは自動更新されます。定期的に PubMed の新着を収集し (`scripts/living_notes_update.py`)、
> 織り手が「📌 5行サマリ」「🧵 横断まとめ」「📚 文献リスト」を編み直します。
> ⏳ = 収集済み・織り待ち / ✅ = 本文に編み込み済み。
> 内容は AI が論文から編んだ要約です。重要な判断は必ず出典リンクから原文に当たってください。

## 📌 5行サマリ
<!-- LN:SUMMARY:START -->
- IgG4-RD は腫瘤を作る全身性の線維炎症疾患。最頻フェノタイプは膵・肝胆道型で**死亡2倍・悪性腫瘍合併増**という重みを持ち (Lee & Culver 2026)、解剖領域として最も高頻度に侵されるのは頭頸部 (唾液腺・涙腺・鼻副鼻腔・喉頭・甲状腺・中耳・眼窩・頸部LN, Wang M 2026)。子宮・前立腺・頸動脈・硬膜まで「どこにでも出る」
- 病態は Th2 だけでは説明しきれない — オリゴクローナルに増殖した **CD4+ 細胞傷害性T細胞**が組織破壊と線維化を同時に駆動する主役として前面に出た (Yi 2026)。アレルギー合併 44%・好酸球増多 22%・高IgE 73% (32研究メタ解析, Li Z 2026)
- 診断は臨床・画像・血清・病理の統合が原則で、**血清 IgG4 単独では決まらない** — 喉頭病変では生検確定例でも正常値が頻繁、硬化性胆管炎では術前正常→術後 >1,600 mg/dL の逆転例まである (Shinnawi 2026 / Yang Y 2026)
- 画像の新しい軸は 68Ga-FAPI と 18F-FDG PET/CT の **"flip-flop"** (FAPI=線維化・実質臓器、FDG=炎症・リンパ節)、FAPI/FDG 比 ≥1.5 が再発リスクを予測 (Cai 2026)。眼窩 IgG4-ROD vs MALT リンパ腫では AI/radiomics が台頭中だが外部検証は未達 (Weng W 2026)
- 治療地図が塗り替わった年 — グルココルチコイドは依然第一選択 (仏ガイドライン 0.4-0.6 mg/kg/日、寛解 >90%) だが再発 30-50%。**抗CD19 イネビリズマブが MITIGATE 試験を経て初の承認薬**となり (米・欧・日)、リツキシマブ/トシリズマブ/デュピルマブ等が続く (Hernández-Molina 2026)
<!-- LN:SUMMARY:END -->

## 🧵 横断まとめ
<!-- LN:SYNTHESIS:START -->
### 疾患の輪郭 — フェノタイプという見取り図
IgG4-RD は「多臓器に腫瘤様病変を作る免疫介在性の線維炎症疾患」であり、臨床像は
**4つのフェノタイプ**に整理できる — 肝胆膵型・全身型・頭頸部型・後腹膜型 (Porr 2026)。
この分類は単なる整理棚ではなく、予後と治療強度の指標として使われ始めている。最頻の
**膵・肝胆道型**は1型自己免疫性膵炎 (AIP1)・IgG4関連胆管炎 (IgG4-SC)・IgG4関連肝症・
胆嚢炎を束ねるが、その代償は軽くない: **死亡率が約2倍、固形癌やリンパ腫の合併も高頻度**で、
「単一の診断検査が存在しない」ことによる診断遅延が複数の総合診療医・専門医受診を経て
治療開始を遅らせる (Lee & Culver 2026)。解剖学的な出現頻度で見ると**頭頸部が最も多く侵される
領域**で、大唾液腺・涙腺・鼻腔副鼻腔・喉頭/声門下・甲状腺・中耳・眼窩・頸部リンパ節に及ぶ
(Wang M 2026)。

フェノタイプは相互排他ではないが、**重なりの薄い複数型が一人に同居する**ことがある — 急性
腎盂腎炎様に受診した47歳女性で、膵炎 (肝胆膵型)・眼窩偽腫瘍 (頭頸部型)・静脈血栓 (後腹膜型) が
順に露見した症例報告は、「一つ見つけたら全身を探せ」を実例で示した (Vijay Krishnan 2026)。

### 病態 — Th2 パラダイムの先へ
従来 IL-4/IL-10 を軸とする Th2 サイトカイン説が病態の中心に置かれてきたが、**それでは組織破壊と
進行性線維化を説明しきれない**という不足が明示的に指摘されるようになった。代わって前面に出たのが
病変深部に**オリゴクローナルに増殖して浸潤する CD4+ 細胞傷害性T細胞 (CD4+ CTL)** で、直接的な
細胞傷害・線維化促進因子の分泌・B細胞との相互作用という三経路で「慢性炎症から線維化へ」の橋を
架ける。SLAMF7 等を含むこの系列は疾患活動性バイオマーカーおよび治療標的の候補として評価されつつ
ある (Yi 2026)。頭頸部領域の総説も同じ枠組みを採り、**クローナル増殖した CD4+ CTL と活性化濾胞
ヘルパーT細胞**が Th2 偏倚環境下で IgG4 クラススイッチと形質芽球の増殖を駆動し、炎症浸潤から
線維性リモデリングへ移行すると整理する — ただし亜部位ごとに炎症優位/線維優位のバランスが違い、
その差は上皮特性・自然免疫応答性・常在線維芽細胞の性質といった局所微小環境に由来する可能性が
示唆される (機序自体は未確立, Wang M 2026)。

IgG4-SC では病因論がさらに具体化しており、**遺伝的素因＋環境曝露 (工業蒸気・粉塵・ガス・煤煙・
アスベスト)** を背景に、Th2/Tfh/Treg 優位の CD4+ T細胞応答が B細胞活性化と IgG4+ 形質芽球の
オリゴクローナル増殖を招く。加えて **annexin A11 と laminin 511-E8 に対する IgG4/IgG1 自己抗体**の
発見が、直接的な病原機序への手がかりとして報告されている (Ren 2026)。

**アレルギーとの関係は定量化された** — 32研究のメタ解析で、IgG4-RD 患者におけるアレルギー合併は
プール割合 0.44 (95%CI 0.39-0.49, n=8233)、好酸球増多 0.22 (n=4376)、高IgE 0.73 (n=2353)。ただし
著者らは「一般集団や他疾患と比べて本当に高いのか」を確かめる対照研究が要ると釘を刺しており、
因果の向きはまだ開いたままである (Li Z 2026)。この共存関係は病態総説でも繰り返し取り上げられて
いる (Porr 2026)。

### 診断 — 血清 IgG4 では決まらない
診断は**臨床病理学的診断** — 臨床・検査・画像・組織を突き合わせ、similar な似姿を除外して初めて
成立する (El-Feghi 2026)。組織像の骨格は変わらず、**IgG4陽性形質細胞に富む密なリンパ球形質細胞
浸潤・花筵状 (storiform) 線維化・閉塞性静脈炎**の三つ組。血清 IgG4 上昇は支持材料にはなるが
**感度も特異度も高くない**ため、血清が正常な症例では免疫染色が決定的になる (Porr 2026)。

この「血清では決まらない」は今回の新着で複数方向から補強された。喉頭 IgG4-RD の系統的レビュー
(27報32例) では、**生検確定例でも血清 IgG4 が正常であることが頻繁**で、表層生検が非診断的に終わる
ため深部粘膜下生検や再生検を要した (Shinnawi 2026)。IgG4-SC の症例では**術前 IgG4 が正常だったのに
術後に >1,600 mg/dL へ跳ね上がり**、最終診断は病理で確定した — 「血清マーカーだけに依らず組織像を
統合せよ」という結論が付されている (Yang Y 2026)。逆に閾値を精緻化する方向の整理もあり、IgG4-SC では
**血清 IgG4 >2×ULN が示唆的・>4×ULN が高特異的、IgG4/IgG1 比 >0.24** が補助指標として使われ、
他臓器病変 (特に AIP1)・ステロイド速効性と合わせた多面的診断が推奨される (Ren 2026)。仏ガイドラインも
多形性の高い臨床像に対して**多職種評価**を求め、多クローン性高ガンマグロブリン血症・血清 IgG4 高値・
補体消費といった検査所見の探索と、原則として臓器生検による確認を置く (Schleinitz 2026)。

画像診断では**膵胆道の CT/MRI 所見と現行診断基準の整理**が進み、AIP と IgG4-SC がしばしば同期発症
すること、それぞれ膵管癌・胆管癌に化けることが差分診断の軸として提示されている (Miguez González 2026;
Kleger 2026)。核医学では **68Ga-FAPI と 18F-FDG PET/CT の頭対頭比較**が3研究 (n=90) でプールされ、
FAPI は実質臓器 (膵・唾液腺) で SUVmax と TBR が有意に高く病変コントラストに優れる (P<0.001) 一方、
FDG はリンパ節活動性をより多く捉える。総病変数は **FAPI 136 対 FDG 78**。病理対応では FAPI が線維化、
FDG が炎症に相関する **"flip-flop" パターン**が定義され、**FAPI/FDG 比 ≥1.5 が再発リスクを予測**した
— 両者は競合ではなく相補で、線維炎症活動性の多モーダル評価と個別化管理に使える (Cai 2026)。眼窩領域では
**IgG4-ROD と眼窩 MALT リンパ腫の鑑別に radiomics/深層学習**が投入されつつあるが、小標本・後ろ向き
単施設・データばらつき・解釈可能性・外部検証の不足という壁が率直に列挙されており、まだ臨床実装前の
段階にある (Weng W 2026)。

### 似姿との鑑別 — 除外こそが本体
IgG4-RD の診断作業は、実質的に**除外の勝負**である。腎病変で挙がる mimic は感染・悪性腫瘍・ANCA関連
疾患・特発性多中心性 Castleman 病・Rosai-Dorfman-Destombes 病・Sjögren 症候群。後腹膜線維症では
リンパ腫・Erdheim-Chester 病 (ECD)・特発性 RPF (El-Feghi 2026)。

この列のうち **ECD との鑑別に専用の枠組み**が用意された: 両者は後腹膜線維症・中枢神経病変・IgG4陽性
形質細胞浸潤を共有して誤診を生むが、ECD 側の指標は**長管骨の骨硬化・"hairy kidneys"・coated aorta・
尿崩症・BRAF V600E / MAPK 経路変異**、IgG4-RD 側は AIP・唾液腺炎・血清 IgG4 高値・花筵状線維化・
閉塞性静脈炎。FDG-PET と MRI での骨・小脳集積は ECD に特徴的で IgG4-RD では通常みられない。さらに
**治療反応そのものが診断の手がかり**になる — ECD は BRAF/MEK 阻害薬を要し、IgG4-RD はステロイド・
リツキシマブ・イネビリズマブに応じる (Gurugubelli 2026)。

腫瘍との境界もあらためて問題になった。**濾胞樹状細胞肉腫 (FDCS) と IgG4-RD の併存**が初めて報告され
(肝・食道・胃)、ステロイドと免疫抑制で消化管病変は改善したのに肝病変だけが進行し、最終的に病理・
免疫染色で FDCS と確定した — IgG4陽性形質細胞浸潤は FDCS 側にも起こりうるため、**「治療に応じない
一臓器」は再生検の適応**という教訓になる (Yao 2026)。眼窩では**成人眼窩黄色肉芽腫性疾患 (AOXD)** との
重なりが3症例＋文献レビューで検討され、IgG4 に富む炎症は AOXD に随伴しうるが**全身性 IgG4-RD の基準
(2019 ACR/EULAR) を満たさないことが多く、現代基準を当てると真の併存はむしろ稀**と結論された。
IgG4 が AOXD で果たす役割が本態か随伴現象かは未解決である (Barros da Silva 2026)。そして胆道では
**IgG4-SC が肝門部胆管癌に化ける**古典的落とし穴が続いており、不必要な外科手術を避けるために診断精度が
critical と繰り返し強調される (Yang Y 2026; Ren 2026)。

### 治療 — ステロイドから B細胞標的へ、地図が書き換わった
**グルココルチコイドは依然として第一選択**である。仏ガイドラインは経口 GC **0.4-0.6 mg/kg/日を2-4週**、
以後漸減し可能なら**3ヶ月で中止**という具体的レジメンを示し、**90%超で寛解導入**が得られるとする。
ただし再発は一般的で、免疫抑制薬を要することがある。管理は薬だけでなく、症状・警告徴候・治療有害事象・
ワクチン・食事・運動についての患者教育と、定期診察・画像・血清 IgG4 を含む検査によるフォローを含む
包括的な枠組みとして提示されている (Schleinitz 2026)。再発率は臓器で異なり、**IgG4-SC では 30-50%**と
高く、維持療法 (アザチオプリン・ミコフェノール酸モフェチル、あるいは B細胞除去) がしばしば必要になる
(Ren 2026; Kleger 2026)。

その先の地図が今回大きく動いた。**抗CD19 モノクローナル抗体イネビリズマブが MITIGATE 試験
(フレア減少・GC フリー寛解率上昇) を経て IgG4-RD で初の承認薬**となり、米国・欧州・日本で承認された
(Hernández-Molina 2026; Lee & Culver 2026)。従来の csDMARD (MMF・レフルノミド・アザチオプリン・MTX) は
ステロイド減量目的で広く使われるが**比較エビデンスは限定的**、リツキシマブは初回治療でも難治・再発例でも
高い有効性を示すが**多くの地域で適応外**という位置づけ。新興の選択肢として obinutuzumab・obexelimab・
CAR-T・デュピルマブ・トシリズマブが挙がるが、いずれも**エビデンスは限定的**である (Hernández-Molina 2026)。
腎病変の総説は、**B細胞標的療法 (リツキシマブ・イネビリズマブ・obexelimab) はステロイドより強力かつ
低毒性**と踏み込み、シグナル経路や免疫細胞を標的とする新薬の試験が進行中であること、そして**早期発見・
早期治療が不可逆的臓器障害の回避に決定的**であることを強調する (El-Feghi 2026)。頭頸部の総説も同じ列に
立ち、リツキシマブは難治・再発例で有効、イネビリズマブは第III相 RCT で有意な benefit を示した一方、
**デュピルマブ (IL-4/IL-13 軸) は症例報告と小規模シリーズにとどまり前向き検証が要る**と線を引いている
(Wang M 2026)。

実地の難治例では代替経路が試されている。GC とメトトレキサートに反応不良だった頸動脈・迷走神経病変が
**トシリズマブ併用で持続寛解**に至った例 (Ding 2026)、ステロイド漸減で再燃した IgG4関連肥厚性硬膜炎が
**リツキシマブで長期安定**を得た例 (Wang Y 2026)、子宮・骨盤内リンパ節病変に**デキサメタゾン＋
シクロホスファミド＋ボルテゾミブ**を用いて血清 IgG4 が大きく低下した例 (Qingyun G 2026) — いずれも n=1 だが、
「B細胞・形質細胞を落とす」という共通の方向を向いている。

### 臓器別の顔と「稀な場所」
**腎・後腹膜** — 腎病変 (IgG4-RKD) の最多は尿細管間質性腎炎 (TIN) だが、**膜性腎症 (MGN)** や
IgG4関連 TIN の組織亜型としての**急性間質性腎炎 (AIN)** としても現れる。IgG4関連後腹膜線維症 (IgG4-RPF) は
実質病変の有無にかかわらず**閉塞性腎障害**を起こしうる (El-Feghi 2026)。

**膵・肝胆道** — AIP1 と IgG4-SC が二大表現で、しばしば同期発症し、それぞれ膵管癌・胆管癌に化ける。
構造化された診断 (悪性腫瘍・感染の優先的除外 → 血清・画像・組織・臓器パターンによる症候群分類) と、
再発を織り込んだリスク適応型の予防・経過観察が要ると整理されている (Kleger 2026; Miguez González 2026)。

**頭頸部・眼窩** — 亜部位ごとに炎症優位/線維優位のバランスと重症度・リスクが異なる (Wang M 2026)。
**喉頭病変**は 27報32例の系統的レビューで輪郭が描かれた: 中年・やや女性優位、嗄声・呼吸困難・
stridor で発症、声門上と声門下が優位で**約1/3 は多層性の気道病変**。内視鏡・画像上は
**(a) 特発性声門下狭窄に似た線維狭窄性の全周性狭小化**と **(b) 腫瘍を模す腫瘤様/ポリープ様病変**の
2パターン。多くが全身 GC ＋追加免疫抑制と内視鏡的拡張/気道手術を受けるが、**再発と固定した線維狭窄への
進行が多い** — 原因不明の喉頭狭窄や粘膜下腫瘤では鑑別に挙げ、十分に深い生検を取ることが推奨される
(Shinnawi 2026)。

**神経・血管** — 中枢神経病変、とくに肥厚性硬膜炎 (HP) は稀。67歳男性の IgG4関連 HP に**反復する
脳静脈血栓症 (CVT)** が合併した報告は、高用量ステロイドに一旦反応するも漸減で再燃し、B細胞除去
(リツキシマブ) で長期安定に至った経過を示し、この稀な組み合わせの文献を横断整理している (Wang Y 2026)。
血管では**頸動脈と迷走神経の孤立病変**が嗄声と失神で発症した例があり、造影頸部 MRI と頸動脈生検で確定した
(Ding 2026)。

**稀少部位** — **子宮＋腹部骨盤リンパ節**病変が月経延長で発症し、PET/CT の高集積から悪性腫瘍が疑われて
子宮全摘に至った例 (病理で花筵状線維化・閉塞性静脈炎・IgG4陽性形質細胞、血清 IgG4/IgG も著明高値,
Qingyun G 2026)。**前立腺**については、系統的レビュー「IgG4関連前立腺炎」をめぐる comment とその reply が
同時に収載され、スペクトラム拡張の妥当性が誌上で議論されている (Suzuki 2026 / Pamfil 2026)。
共通するメッセージは一つ — **非典型部位こそ誤診が起きる**。慢性炎症性・腫瘤形成性の病変を見たら、
場所が想定外でも IgG4-RD を鑑別から落とさない (Vijay Krishnan 2026; Qingyun G 2026)。
<!-- LN:SYNTHESIS:END -->

## 📚 文献リスト
<!-- LN:BIB:START -->
1. **El-Feghi M, Cornell LD, Geldenhuys L et al.** IgG4-Related Kidney Disease and IgG4-Related Retroperitoneal Fibrosis: An Update on Diagnosis and Treatment. *Kidney Int Rep* 2026;11(8):106630. PMID [42440422](https://pubmed.ncbi.nlm.nih.gov/42440422/) / [DOI](https://doi.org/10.1016/j.ekir.2026.106630)
2. **Wang M, Weng Y, Ma J et al.** From inflammatory initiation to fibrotic remodeling: mechanisms and precision therapeutic strategies in otorhinolaryngologic involvement of IgG4-related disease. *Front Med (Lausanne)* 2026;13:1859866. PMID [42428274](https://pubmed.ncbi.nlm.nih.gov/42428274/) / [DOI](https://doi.org/10.3389/fmed.2026.1859866)
3. **Lee H, Motta RV, Culver EL.** Clinical Updates in IgG4-Related Pancreatic and Hepatobiliary Disease. *Br J Hosp Med (Lond)* 2026;87(6):55132. PMID [42411531](https://pubmed.ncbi.nlm.nih.gov/42411531/) / [DOI](https://doi.org/10.31083/BJHM55132)
4. **Shinnawi S, Khoury M, Zhalka A et al.** Laryngeal IgG4-Related Disease: A Systematic Review of Clinical Features and Management. *Laryngoscope* 2026. PMID [42381230](https://pubmed.ncbi.nlm.nih.gov/42381230/) / [DOI](https://doi.org/10.1002/lary.70714)
5. **Miguez González J, Oliveira Caiafa R, Valls Mellado M et al.** Diagnostic Imaging of Pancreatic and Biliary Involvement in IgG4-Related Disease: Key Imaging Features, Diagnostic Criteria and Differential Diagnosis. *Diagnostics (Basel)* 2026;16(12):1806. PMID [42351465](https://pubmed.ncbi.nlm.nih.gov/42351465/) / [DOI](https://doi.org/10.3390/diagnostics16121806)
6. **Yao Y, Bai Y, Liu G et al.** Follicular dendritic cell sarcoma associated with IgG4-related disease: a case report and literature review. *Front Immunol* 2026;17:1685017. PMID [42292403](https://pubmed.ncbi.nlm.nih.gov/42292403/) / [DOI](https://doi.org/10.3389/fimmu.2026.1685017)
7. **Schleinitz N, Audia S, Cohen F et al.** French protocol for diagnosis and management (guidelines) of IgG4-related disease. *Rev Med Interne* 2026;47(7):362-383. PMID [42276880](https://pubmed.ncbi.nlm.nih.gov/42276880/) / [DOI](https://doi.org/10.1016/j.revmed.2026.05.013)
8. **Cai X, Wang Q, Hao Q et al.** Complementary roles of 68Ga-FAPI and 18F-FDG PET/CT in evaluating IgG4-related disease: a systematic review and pooled analysis. *EJNMMI Res* 2026. PMID [42268509](https://pubmed.ncbi.nlm.nih.gov/42268509/) / [DOI](https://doi.org/10.1186/s13550-026-01452-6)
9. **Kleger A.** [Autoimmune pancreatitis and IgG4-related disease] (独語). *Inn Med (Heidelb)* 2026;67(7):760-771. PMID [42257733](https://pubmed.ncbi.nlm.nih.gov/42257733/) / [DOI](https://doi.org/10.1007/s00108-026-02125-1)
10. **Porr C, Vidrighin A, Harris DM et al.** Correlations between IgG4-related disease, autoimmune pancreatitis, and allergic diseases. *Front Immunol* 2026;17:1718303. PMID [42238580](https://pubmed.ncbi.nlm.nih.gov/42238580/) / [DOI](https://doi.org/10.3389/fimmu.2026.1718303)
11. **Pamfil C, Cabău G, Damian L et al.** Reply to the comment on: IgG4-related prostatitis: expanding the spectrum of IgG4-related disease. A systematic review. *Clin Exp Rheumatol* 2026;44(7):1452. PMID [42154659](https://pubmed.ncbi.nlm.nih.gov/42154659/) / [DOI](https://doi.org/10.55563/clinexprheumatol/o69u7n)
12. **Suzuki K, Akiyama M, Horie H et al.** Comment on: IgG4-related prostatitis: expanding the spectrum of IgG4-related disease: a systematic review. *Clin Exp Rheumatol* 2026;44(7):1450-1451. PMID [42154652](https://pubmed.ncbi.nlm.nih.gov/42154652/) / [DOI](https://doi.org/10.55563/clinexprheumatol/vsnxbl)
13. **R VK, Seshadri H, Balachandran S et al.** Immunoglobulin-G4 Related Disease: A Rare Entity with Many Clinical Faces - Literature Review and Case Illustration. *Mediterr J Rheumatol* 2026;37(1):126-135. PMID [42100065](https://pubmed.ncbi.nlm.nih.gov/42100065/) / [DOI](https://doi.org/10.31138/mjr.150825.era)
14. **Hernández-Molina G, Anaya-Macías BU, Martín-Nares E.** Management of IgG4-Related Disease. *Curr Rheumatol Rep* 2026;28(1). PMID [42096015](https://pubmed.ncbi.nlm.nih.gov/42096015/) / [DOI](https://doi.org/10.1007/s11926-026-01224-0)
15. **Yang Y, Hou Y, Wang Y et al.** Diagnostic pitfalls in IgG4-related sclerosing cholangitis presenting as perihilar cholangiocarcinoma: case report with literature review. *Front Immunol* 2026;17:1684445. PMID [42079574](https://pubmed.ncbi.nlm.nih.gov/42079574/) / [DOI](https://doi.org/10.3389/fimmu.2026.1684445)
16. **Barros da Silva P, Duarte A, Almadhi NH et al.** Exploring the intersection: adult orbital xanthogranulomatous disease and IgG4-related disease - report of 3 cases and literature review. *Orbit* 2026;45(4):593-602. PMID [41949590](https://pubmed.ncbi.nlm.nih.gov/41949590/) / [DOI](https://doi.org/10.1080/01676830.2026.2644630)
17. **Qingyun G, Yuanyuan W.** Clinicopathological Characteristics of IgG4-Related Disease Involving Uterus and Abdominopelvic Lymph Nodes: A Case Report. *Int J Surg Pathol* 2026;34(6):1579-1585. PMID [41918074](https://pubmed.ncbi.nlm.nih.gov/41918074/) / [DOI](https://doi.org/10.1177/10668969261433178)
18. **Li Z, Zhang J, Xu H et al.** The risk of allergy in patients with IgG4-related disease: A systematic review and meta-analysis. *Autoimmun Rev* 2026;25(5):104050. PMID [41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/) / [DOI](https://doi.org/10.1016/j.autrev.2026.104050)
19. **Ding X, Tao J, Xu C et al.** Tocilizumab in the treatment of IgG4-related disease involving the carotid artery - case report and literature review. *Front Immunol* 2026;17:1734761. PMID [41909711](https://pubmed.ncbi.nlm.nih.gov/41909711/) / [DOI](https://doi.org/10.3389/fimmu.2026.1734761)
20. **Wang Y, Zhao Y, Lu C et al.** Recurrent cerebral venous thrombosis associated with IgG4-related hypertrophic pachymeningitis: Case report and literature review. *BMC Neurol* 2026;26(1). PMID [41808071](https://pubmed.ncbi.nlm.nih.gov/41808071/) / [DOI](https://doi.org/10.1186/s12883-026-04734-7)
21. **Yi J, Jia L, Mao T et al.** Beyond the Th2 paradigm: CD4+ cytotoxic T lymphocytes as key drivers of tissue damage and fibrosis in IgG4-related disease. *Front Immunol* 2026;17:1781462. PMID [41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/) / [DOI](https://doi.org/10.3389/fimmu.2026.1781462)
22. **Weng W, Chen Y, Jin R et al.** Application of artificial intelligence in differentiating IgG4-related ophthalmic disease and orbital MALT lymphoma: a review of radiomics and deep learning advances. *Front Immunol* 2026;17:1722733. PMID [41756276](https://pubmed.ncbi.nlm.nih.gov/41756276/) / [DOI](https://doi.org/10.3389/fimmu.2026.1722733)
23. **Gurugubelli S, Korra RN, Meda VSA et al.** A Systematic Review of Erdheim-Chester Disease and IgG4-Related Disease: Building a Diagnostic Framework for the Rheumatologist. *J Clin Rheumatol* 2026;32(2):59-64. PMID [41728905](https://pubmed.ncbi.nlm.nih.gov/41728905/) / [DOI](https://doi.org/10.1097/RHU.0000000000002299)
24. **Ren X, Jin X, Liu L et al.** IgG4-related sclerosing cholangitis: navigating diagnostic dilemmas and the challenge of relapse. *Front Med (Lausanne)* 2026;13:1732637. PMID [41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/) / [DOI](https://doi.org/10.3389/fmed.2026.1732637)

> ※ No.1-24 は 2026-08-07 収集分の全件 (24/24) を編み込んだもの。書誌は **PubMed メタデータ
> (get_article_metadata) と全件照合済み**で、雑誌名・巻号頁・DOI は PubMed 側の値を正とした。
> 収集ログ側の DOI は **13件 (No.1, 2, 5, 6, 9, 10, 14, 15, 19, 20, 21, 22, 23) で別論文の DOI が混入**して
> おり (No.23 は `doi.org/0` と空値)、本リストでは PubMed 照合値に訂正した。虫垂炎ノートでも同種の
> 混入が出ているため、`living_notes_update.py` の DOI 抽出 (参考文献欄からの誤拾い疑い) は引き続き要修理。
> No.11・12 は抄録なしのレター (comment / reply) で、本文の記述はタイトルと誌上の位置づけのみに基づく。

<!-- LN:BIB:END -->

## 🆕 新着ログ
<!-- LN:LOG:START -->

### ✅ 2026-08-07 収集分 (24件・編み込み済み)

- **IgG4-Related Kidney Disease and IgG4-Related Retroperitoneal Fibrosis: An Update on Diagnosis and Treatment.** — El-Feghi M, Cornell LD, Geldenhuys L et al. *Kidney Int Rep* (2026). PMID [42440422](https://pubmed.ncbi.nlm.nih.gov/42440422/) / [DOI](https://doi.org/10.1016/j.ekir.2026.106630)
  - 抄録: Renal involvement of IgG4-related disease (IgG4-RD), collectively termed IgG4-related kidney disease (IgG4-RKD), most commonly manifests as tubulointerstitial nephritis (TIN) but can also manifest as membranous glomerulonephritis (MGN) and acute interstitial nephritis (AIN) as a histologic subtype o…
- **From inflammatory initiation to fibrotic remodeling: mechanisms and precision therapeutic strategies in otorhinolaryngologic involvement of IgG4-related disease.** — Wang M, Weng Y, Ma J et al. *Front Med (Lausanne)* (2026). PMID [42428274](https://pubmed.ncbi.nlm.nih.gov/42428274/) / [DOI](https://doi.org/10.3389/fmed.2026.1859866)
  - 抄録: IgG4-related disease (IgG4-RD) is a systemic fibroinflammatory disorder characterized by complex immune-mediated mechanisms and broad organ involvement that remains substantially underdiagnosed in clinical practice. The head and neck region is one of the most commonly involved anatomical domains, en…
- **Clinical Updates in IgG4-Related Pancreatic and Hepatobiliary Disease.** — Lee H, Motta RV, Culver EL *Br J Hosp Med (Lond)* (2026). PMID [42411531](https://pubmed.ncbi.nlm.nih.gov/42411531/) / [DOI](https://doi.org/10.31083/bjhm55132)
  - 抄録: Immunoglobulin G4-related disease (IgG4-RD) is a systemic fibro-inflammatory immune-mediated condition. The Pancreato-Hepato-Biliary subtype is the most frequent phenotype. The subtype encompasses immunoglobulin G4 (IgG4)-related pancreatitis (autoimmune pancreatitis type 1), IgG4-related cholangiti…
- **Laryngeal IgG4-Related Disease: A Systematic Review of Clinical Features and Management.** — Shinnawi S, Khoury M, Zhalka A et al. *Laryngoscope* (2026). PMID [42381230](https://pubmed.ncbi.nlm.nih.gov/42381230/) / [DOI](https://doi.org/10.1002/lary.70714)
  - 抄録: To synthesize clinical presentation, anatomic patterns, diagnostic evaluation, and treatment outcomes of laryngeal IgG4-related disease (IgG4-RD) and highlight features that may support earlier diagnosis in unexplained laryngeal stenosis or mass-like lesions. Systematic searches of PubMed/MEDLINE, E…
- **Diagnostic Imaging of Pancreatic and Biliary Involvement in IgG4-Related Disease: Key Imaging Features, Diagnostic Criteria and Differential Diagnosis.** — Miguez González J, Oliveira Caiafa R, Valls Mellado M et al. *Diagnostics (Basel)* (2026). PMID [42351465](https://pubmed.ncbi.nlm.nih.gov/42351465/) / [DOI](https://doi.org/10.3390/diagnostics16121806)
  - 抄録: IgG4-related disease (IgG4-RD) is a systemic fibroinflammatory disorder characterised by elevated serum levels of IgG4 and multiorgan damage. Its diagnosis is challenging and requires a careful integration of clinical, radiological, serological and histological data. Pancreatic and biliary involveme…
- **Follicular dendritic cell sarcoma associated with IgG4-related disease: a case report and literature review.** — Yao Y, Bai Y, Liu G et al. *Front Immunol* (2026). PMID [42292403](https://pubmed.ncbi.nlm.nih.gov/42292403/) / [DOI](https://doi.org/10.3389/fimmu.2026.1685017)
  - 抄録: Follicular dendritic cell sarcoma (FDCS) is a rare malignant tumor involving lymph nodes and extranodal sites, classified into conventional and inflammatory pseudotumor (IPT)-like variants. The IPT-like variant predominantly involves the liver and spleen. Immunoglobulin G4-related disease (IgG4-RD) …
- **French protocol for diagnosis and management (guidelines) of IgG4-related disease.** — Schleinitz N, Audia S, Cohen F et al. *Rev Med Interne* (2026). PMID [42276880](https://pubmed.ncbi.nlm.nih.gov/42276880/) / [DOI](https://doi.org/10.1016/j.revmed.2026.05.013)
  - 抄録: IgG4-related disease (IgG4-RD) is a recently described entity comprising pseudo-tumoral and inflammatory conditions that were previously considered separately. It is characterised by specific histological abnormalities, including polyclonal lymphoplasmacytic infiltration, fibrosis and contingent of …
- **Complementary roles of 68Ga-FAPI and 18 F-FDG PET/CT in evaluating IgG4-related disease: a systematic review and pooled analysis.** — Cai X, Wang Q, Hao Q et al. *EJNMMI Res* (2026). PMID [42268509](https://pubmed.ncbi.nlm.nih.gov/42268509/) / [DOI](https://doi.org/10.1186/s13550-026-01452-6)
  - 抄録: IgG4-related disease (IgG4-RD) lacks standardized imaging criteria. This study systematically reviewed head-to-head comparisons of 68Ga-FAPI and 18F-FDG PET/CT to clarify their complementary roles in diagnosing and staging IgG4-RD. Three high-quality studies (n = 90) were pooled. 68Ga-FAPI showed si…
- **[Autoimmune pancreatitis and IgG4-related disease].** — Kleger A *Inn Med (Heidelb)* (2026). PMID [42257733](https://pubmed.ncbi.nlm.nih.gov/42257733/) / [DOI](https://doi.org/10.1007/s00108-026-02125-1)
  - 抄録: Immunoglobulin G4-related disease (IgG4-RD) is an immune-mediated systemic disease that causes organ-specific inflammation and fibrosis patterns and also frequently has tumor-like effects. In the pancreaticobiliary setting type 1 autoimmune pancreatitis (AIP1) and IgG4-related cholangitis (IAC) are …
- **Correlations between IgG4-related disease, autoimmune pancreatitis, and allergic diseases.** — Porr C, Vidrighin A, Harris DM et al. *Front Immunol* (2026). PMID [42238580](https://pubmed.ncbi.nlm.nih.gov/42238580/) / [DOI](https://doi.org/10.3389/fimmu.2026.1718303)
  - 抄録: IgG4-related disease (IgG4-RD) is a relatively recently described condition whose etiology and pathophysiology remain unclear. Histopathological features include dense lymphoplasmacytic tissue infiltration with numerous IgG4-positive plasma cells, storiform fibrosis, and obliterative phlebitis. Most…
- **Reply to the comment on: IgG4-related prostatitis: expanding the spectrum of IgG4-related disease. A systematic review.** — Pamfil C, Cabău G, Damian L et al. *Clin Exp Rheumatol* (2026). PMID [42154659](https://pubmed.ncbi.nlm.nih.gov/42154659/) / [DOI](https://doi.org/10.55563/clinexprheumatol/o69u7n)
- **Comment on: IgG4-related prostatitis: expanding the spectrum of IgG4-related disease: a systematic review.** — Suzuki K, Akiyama M, Horie H et al. *Clin Exp Rheumatol* (2026). PMID [42154652](https://pubmed.ncbi.nlm.nih.gov/42154652/) / [DOI](https://doi.org/10.55563/clinexprheumatol/vsnxbl)
- **Immunoglobulin-G4 Related Disease: A Rare Entity with Many Clinical Faces - Literature Review and Case Illustration.** — R VK, Seshadri H, Balachandran S et al. *Mediterr J Rheumatol* (2026). PMID [42100065](https://pubmed.ncbi.nlm.nih.gov/42100065/) / [DOI](https://doi.org/10.31138/mjr.150825.era)
  - 抄録: Immunoglobulin-G4 Related Disease (IgG4-RD) is a group of multi-system, fibro-inflammatory conditions characterised by elevated IgG4 levels and unique histopathological features. Clinical presentations of the disease are highly variable, albeit there exist distinct phenotypes in the presentations of…
- **Management of IgG4-Related Disease.** — Hernández-Molina G, Anaya-Macías BU, Martín-Nares E *Curr Rheumatol Rep* (2026). PMID [42096015](https://pubmed.ncbi.nlm.nih.gov/42096015/) / [DOI](https://doi.org/10.1007/s11926-026-01224-0)
  - 抄録: IgG4-related disease (IgG4-RD) is a chronic immune-mediated fibroinflammatory condition characterized by tumefactive lesions in multiple organs. Although glucocorticoids remain the cornerstone of therapy, high relapse rates and treatment-related toxicity have prompted the development of steroid-spar…
- **Diagnostic pitfalls in IgG4-related sclerosing cholangitis presenting as perihilar cholangiocarcinoma: case report with literature review.** — Yang Y, Hou Y, Wang Y et al. *Front Immunol* (2026). PMID [42079574](https://pubmed.ncbi.nlm.nih.gov/42079574/) / [DOI](https://doi.org/10.3389/fimmu.2026.1684445)
  - 抄録: IgG4-related sclerosing cholangitis (IgG4-SC) is an uncommon autoimmune biliary disorder that often closely mimics malignant perihilar cholangiocarcinoma, posing significant diagnostic challenges. This case is notable for initially normal preoperative IgG4 levels, followed by profound postoperative …
- **Exploring the intersection: adult orbital xanthogranulomatous disease and IgG4-related disease - report of 3 cases and literature review.** — Barros da Silva P, Duarte A, Almadhi NH et al. *Orbit* (2026). PMID [41949590](https://pubmed.ncbi.nlm.nih.gov/41949590/) / [DOI](https://doi.org/10.1080/01676830.2026.2644630)
  - 抄録: To examine the clinical, radiologic, and histopathologic overlap between adult orbital xanthogranulomatous disease (AOXD) and IgG4-related disease (IgG4-RD)/IgG4-related ophthalmic disease (IgG4-ROD), illustrated by three representative cases and a literature review. We retrospectively characterized…
- **Clinicopathological Characteristics of IgG4-Related Disease Involving Uterus and Abdominopelvic Lymph Nodes: A Case Report.** — Qingyun G, Yuanyuan W *Int J Surg Pathol* (2026). PMID [41918074](https://pubmed.ncbi.nlm.nih.gov/41918074/) / [DOI](https://doi.org/10.1177/10668969261433178)
  - 抄録: Immunoglobulin G4-related disease (IgG4-RD) is a systemic fibroinflammatory disorder that commonly affects multiple organs and may be misdiagnosed when presenting at atypical sites. We report an example of IgG4-RD involving the uterus and abdominopelvic lymph nodes and review the literature to clari…
- **The risk of allergy in patients with IgG4-related disease: A systematic review and meta-analysis.** — Li Z, Zhang J, Xu H et al. *Autoimmun Rev* (2026). PMID [41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/) / [DOI](https://doi.org/10.1016/j.autrev.2026.104050)
  - 抄録: IgG4-related disease (IgG4-RD) is an immune-mediated condition characterized by multi-organ involvement. Substantial evidence suggests a close link between allergy and IgG4-RD, supported by the high prevalence of allergic comorbidities in patients and shared immunological features such as eosinophil…
- **Tocilizumab in the treatment of IgG4-related disease involving the carotid artery-case report and literature review.** — Ding X, Tao J, Xu C et al. *Front Immunol* (2026). PMID [41909711](https://pubmed.ncbi.nlm.nih.gov/41909711/) / [DOI](https://doi.org/10.3389/fimmu.2026.1734761)
  - 抄録: IgG4-related disease (IgG4-RD) is an autoimmune disorder characterized by fibroinflammatory infiltration of affected organs. This systemic condition can involve multiple organs, including the pancreas, bile ducts, salivary glands, kidneys and lungs. However, IgG4-related disease demonstrates substan…
- **Recurrent cerebral venous thrombosis associated with IgG4-related hypertrophic pachymeningitis: Case report and literature review.** — Wang Y, Zhao Y, Lu C et al. *BMC Neurol* (2026). PMID [41808071](https://pubmed.ncbi.nlm.nih.gov/41808071/) / [DOI](https://doi.org/10.1186/s12883-026-04734-7)
  - 抄録: IgG4-related disease (IgG4-RD) is a systemic inflammatory condition marked by tissue infiltration of IgG4-positive plasma cells, often resulting in fibrosis. While IgG4-RD commonly affects organs such as the pancreas and salivary glands, central nervous system involvement, particularly hypertrophic …
- **Beyond the Th2 paradigm: CD4+ cytotoxic T lymphocytes as key drivers of tissue damage and fibrosis in IgG4-related disease.** — Yi J, Jia L, Mao T et al. *Front Immunol* (2026). PMID [41766862](https://pubmed.ncbi.nlm.nih.gov/41766862/) / [DOI](https://doi.org/10.3389/fimmu.2026.1781462)
  - 抄録: IgG4-related disease (IgG4-RD) is a distinctive immune-mediated disorder characterized by multi-organ involvement, dense IgG4+ plasma cell infiltration, and storiform fibrosis. While pathogenesis has traditionally been attributed primarily to T helper type(Th) 2 cytokines (e.g., Interleukin(IL)-4/IL…
- **Application of artificial intelligence in differentiating IgG4-related ophthalmic disease and orbital MALT lymphoma: a review of radiomics and deep learning advances.** — Weng W, Chen Y, Jin R et al. *Front Immunol* (2026). PMID [41756276](https://pubmed.ncbi.nlm.nih.gov/41756276/) / [DOI](https://doi.org/10.3389/fimmu.2026.1722733)
  - 抄録: The differentiation between Immunoglobulin G4-related ophthalmic disease (IgG4-ROD) and orbital lymphoma, particularly the mucosa-associated lymphoid tissue (MALT) subtype, presents a significant clinical challenge due to overlapping imaging features and similar presentations. Recent advances in art…
- **A Systematic Review of Erdheim-Chester Disease and IgG4-Related Disease: Building a Diagnostic Framework for the Rheumatologist.** — Gurugubelli S, Korra RN, Meda VSA et al. *J Clin Rheumatol* (2026). PMID [41728905](https://pubmed.ncbi.nlm.nih.gov/41728905/) / [DOI](https://doi.org/0)
  - 抄録: Erdheim-Chester disease (ECD) and immunoglobulin G4-related disease (IgG4-RD) are both rare, multisystem disorders with overlapping clinical, radiologic, and histopathologic features. This overlap leads to delays or misdiagnoses. Early diagnosis with proper distinction is critical for treatment and …
- **IgG4-related sclerosing cholangitis: navigating diagnostic dilemmas and the challenge of relapse.** — Ren X, Jin X, Liu L et al. *Front Med (Lausanne)* (2026). PMID [41728618](https://pubmed.ncbi.nlm.nih.gov/41728618/) / [DOI](https://doi.org/10.3389/fmed.2026.1732637)
  - 抄録: Immunoglobulin G4-related sclerosing cholangitis (IgG4-SC), also termed IgG4-related cholangitis (IRC), is a challenging immune-mediated biliary disease, frequently mimicking malignancies such as cholangiocarcinoma (CCA) or other sclerosing cholangitides like primary sclerosing cholangitis (PSC). Ac…
<!-- LN:LOG:END -->