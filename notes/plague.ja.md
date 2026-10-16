---
topic: ペスト / plague (Yersinia pestis)
slug: plague
updated: 2026-10-16
---

# 🌱 生きたノート: ペスト（Yersinia pestis） (ライブミラー)

> **これは作者の実稼働インスタンスのライブミラーです** — 本家で週1回の自動収集
> (PubMed) と織り直しが走るたび、このノートと鼓動 ([heartbeat](../data/heartbeat.json))
> がここに push されます。**最終チェック: 2026-10-16 JST — ノート更新あり。**
> **内容は AI が論文から編んだ要約であり、鵜呑みにしないでください。** 臨床判断は必ず
> 原著と主治医・現場の判断に従ってください。各記述の出典リンクから原文に当たれます。
> ⏳ = 収集済み・織り待ち / ✅ = 本文に編み込み済み。

## 📌 5行サマリ
<!-- LN:SUMMARY:START -->
- ペストは「終わった病気」ではなく**診断の遅れが死因になる現役の疾患**。WHO によれば 2019–2025 年の報告例はコンゴ民主共和国とマダガスカルに集中し、マダガスカルでは 9月〜4月の流行期にほぼ毎年腺ペストが出る ([WHO fact sheet, 2026-09-29 更新](https://www.who.int/news-room/fact-sheets/detail/plague))
- 致死率の落差がすべてを語る: 腺ペストは**未治療 66% → 抗菌薬治療で 13%**、抗菌薬以前は全病型で 66–93% だった (CDC/MMWR 2021)。肺ペストは早期治療がなければほぼ致死的で、WHO は「発症から24時間以内の治療開始なら回復率は高い」と書く — 治療の窓が**時間単位**
- 病型は腺 (80–90%)・敗血症型 (約10%)・肺の3つで、潜伏期は 2–7日 (肺は24時間まで短縮しうる)。厚労省の届出基準は肺ペストを「鮮紅色の泡立った血痰を伴う重篤な肺炎像を示し、２〜３日で死亡する」と記す ([厚労省 届出基準](https://www.mhlw.go.jp/bunya/kenkou/kekkaku-kansenshou11/01-01-05.html))
- 治療は**疑った時点で開始**するもので、検査確定を待たない — 待てる検査が無いからでもある。流行地の前向き研究で**現場実施のF1抗原迅速検査は特異度74%**にとどまり、著者らは「臨床の症例管理の判断には頼れない」と結論した (Raberahona 2026)。成人第一選択はゲンタマイシン/ストレプトマイシン・フルオロキノロン、腺型ではドキシサイクリンも第一選択。重症の肺・敗血症型は**異なる2クラスの併用**で開始し改善後に単剤へ。全病型 **10–14日** (Nelson 2021 MMWR)
- 日本では**一類感染症**（感染症法 第6条第2項第5号）で、患者・疑似症患者・無症状病原体保有者・死体のいずれも**直ちに届出**（第12条第1項）。疑似症の判断材料として「流行地への渡航歴」「齧歯類に寄生しているノミによる咬傷」が明記されている — つまり**病歴聴取が届出要件そのもの**
<!-- LN:SUMMARY:END -->

## 🧵 横断まとめ
<!-- LN:SYNTHESIS:START -->
### 1. どこで今も起きているか — 「疑う」の前提になる疫学

WHO のファクトシート（2026-09-29 更新）によれば、ヒトのペストは複数の国で今も地域流行しており、1990年代以降は報告例の多くがアフリカに集まっている。2019–2025 年に関しては**コンゴ民主共和国とマダガスカルが報告例の大半**を占める。マダガスカルでは腺ペストが**ほぼ毎年、9月から4月の流行期**に記録される。アメリカ西部にも自然界の宿主（地上性齧歯類）が定着していて、CDC は米国内でも自然発生があると明記している。

**中央アジアの流行地も押さえておくと渡航者診療で効く**。モンゴルでは**マーモット（タルバガン）由来の腺ペスト**が毎年のように出ており、国立人獣共通感染症センター（NCZD）によれば **21省のうち17省がペストのリスク地域**に分類されている。高リスクとされるのは西部のバヤンウルギー・ゴビアルタイ・ホブド・ウブスで、政府は3万2千人超の接種を計画していると報じられた。直近の確定例は **2026年7月のホブド省**で、患者は隣接するバヤンウルギー省ウランフス郡を訪れた際に**マーモットの肉を食べて**感染した（細菌学的検査で確定。NCZD 発表・Xinhua 報）。マーモット猟は法律で禁じられているが、珍味として扱われるため密猟が続いているとされる。中国内モンゴル自治区でも同型の症例が出る。

つまりモンゴル方面の渡航者では、**ノミ咬傷だけでなく「野生齧歯類の肉を食べたか」が問診項目になる**。感染経路として経口摂取・調理時の接触が実際に機能しており、夏季（人が草原に出る季節）に増える。

ここが家庭医にとっての実装ポイントになる。ペストは「渡航外来の珍しい話」ではなく、**渡航歴＋野外曝露＋急速に進む発熱**という組み合わせを見たときに鑑別リストに載せるべき疾患である。逆に、曝露の文脈がまったくない発熱に対してペストを疑う必要は基本的にない。鍵は疾患頻度ではなく**曝露歴の有無**で、これは厚労省の届出基準が疑似症の判断材料として渡航歴とノミ咬傷を名指ししている構造と一致する。

### 2. 三つの病型と時間の軸 — なぜ「遅れ」が死因になるか

厚労省の届出基準にある臨床的特徴は、病型ごとの時間感覚まで書き込んでいて実用的である。

| 病型 | 割合 | 潜伏期 | 臨床像（届出基準の記載） | 未治療の帰結 |
|---|---|---|---|---|
| 腺ペスト | ヒトペストの 80–90% | 2–7日 | 感染部のリンパ節が痛みとともに腫れる。菌は血流を介して全身のリンパ節・肝・脾でも繁殖 | 「多くは１週間くらいで死亡」/ CFR 66%（MMWR）・30–60%（WHO） |
| 敗血症ペスト | 約 10% | — | 時に局所症状がないまま敗血症症状が先行、皮膚に出血斑が生じて全身が黒色となる | 腺ペストより高い致死率（MMWR は数値を示さず） |
| 肺ペスト | — | 24時間〜 | 強烈な頭痛・嘔吐・39〜41℃の弛張熱・急激な呼吸困難・鮮紅色の泡立った血痰 | 「２〜３日で死亡」/ ほぼ常に致死的（MMWR） |

注目すべきは**腺ペストに「痛み」が明記されている**こと。無痛性のリンパ節腫脹とは像が違い、強い疼痛を伴う急速な腫脹（バボ）が特徴になる。そして敗血症型は**局所所見が先行しないことがある** — つまり「バボを探して見つからないから違う」という除外のしかたは危険である。

CDC/MMWR 2021 が示す数値はこの時間軸の意味を定量化している。腺ペストは未治療 66% が抗菌薬治療で **13%** に落ちる。一方で肺ペストには「治療すればこの率」という安心できる数字が置かれていない。WHO は「発症から24時間以内に治療すれば回復率は高い」と書くので、肺ペストの予後を決めているのは薬剤選択よりも**治療開始までの時間**だと読める。これは「検査確定を待って治療を始める」という平時の作法が、この疾患では致命的になるという意味でもある。

### 3. 疑うとき — 病歴の三点セットと鑑別

厚労省の届出基準が疑似症患者の診断にあたって参考にせよと書くのは次の3つである:「臨床所見」「ペスト流行地への渡航歴」「齧歯類に寄生しているノミによる咬傷の有無」。渡航歴とノミ咬傷が**法令由来の届出要件に組み込まれている**のは珍しく、問診がそのまま公衆衛生の手続きに直結している例といえる。

鑑別も届出基準が親切に名指ししている。**類鼻疽（メリオイドーシス）は臨床症状が肺ペストと類似**し、**野兎病（ツラレミア）は腺ペストに類似し、かつ共通抗原決定基を持つ**。後者は重要で、抗原を共有するということは**血清学的検査が交差する**可能性を含む。熱帯・亜熱帯の渡航後に急速進行する肺炎やリンパ節炎を見たときは、この3つを並べて考えるのが筋ということになる。

### 4. 診断 — 検体と検査、そして「検査室への事前連絡」

届出基準は検査方法と検査材料の対応を表で定めている。実務ではこの対応がそのまま検体オーダーの設計図になる。

| 検査方法 | 検査材料 |
|---|---|
| 分離・同定による病原体の検出（塗抹標本の染色鏡検も参考となる） | 血液、リンパ節腫吸引物、喀痰、病理組織 |
| 蛍光抗体法によるエンベロープ抗原（Fraction 1 抗原）の検出 | 同上 |
| PCR 法による病原体の遺伝子の検出 | 同上 |
| 赤血球凝集反応による F1 抗原に対する抗体の検出（16倍以上） | 血清 |

**F1（Fraction 1）抗原**が繰り返し出てくるのは、これが *Y. pestis* の莢膜抗原で、診断の標的として実用化されているためである（Demeure 2019 のレビューは F1 と免疫原性タンパクが診断目的に利用されていると整理している）。WHO は **F1 を検出するラボ検証済みのラピッドディップスティック**がアフリカと南米で広く使われていると記載している。日本の届出基準に迅速検査は含まれていないので、国内では分離・同定／PCR／蛍光抗体法／血清抗体の4本立てになる。

#### 4-1. その検査は実際どれだけ当たるのか — 流行地で初めて測られた（2025-12）

この節でいちばん大事な論文がこれである。**Raberahona ら（*Clin Microbiol Infect* 2026;32(4):638-643、オンライン2025-12-11）**は、マダガスカルの IMASOY 治験（NCT04110340）に組み込んだ**前向き精度サブ研究**で、WHO ガイドラインが挙げる確認検査（培養・PCR・血清）とF1抗原ラテラルフロー迅速検査（**F1RDT**）の実力を、流行地の現場で測った。疑い例 **438例**が対象で、培養またはPCR陽性（参照基準RS1）が184例（42%）、血清も含めると（RS2）211例（48%）だった。

結果は、教科書の序列を2か所で書き換える。

| 検査 | 確定例のうち検出できた割合 | 読み方 |
|---|---|---|
| 血清（IgG F1 抗体） | 197/211 = **93%** | 最も多く拾うが、D1/D11/D21 の採血が要り**ルーチンには非現実的** |
| PCR | 179/211 = **85%** | **培養を上回る** — 従来の参照基準が逆転した |
| 培養 | 137/211 = **65%** | 旧・参照基準。3分の1を取りこぼす |
| PCR + 培養 | **87%** | 残る13%は**血清でしか捕まらない** |

そしてF1RDTの数字が効く。**現場（on-site）で行ったF1RDTは感度94%（95%CI 89.6-97.0）だが特異度74%（68.2-79.3）**にとどまり（RS1 比較）、著者らは **「臨床の症例管理の判断に現場F1RDTを頼ることはできない」**と結論した。同じ検査を**中央検査室の条件で行うと特異度97.6%（94.9-99.1）**まで跳ね上がる。つまり問題は検査キットの原理ではなく**実施環境**であり、F1RDTの使いどころは**治療判断ではなくサーベイランス**（資源制約下の周辺検査室）だ、という位置づけになった。

これは臨床的にかなり重い。特異度74%ということは、**本当は陰性の人の約4人に1人が陽性に出る**。致死的な疾患なので偽陽性でも治療を始める判断自体は妥当だが、「現場の迅速検査が陰性だから大丈夫」も「陽性だから確定」も**どちらも成り立たない**。この研究にはブラジル Fiocruz のグループから書簡（Amancio ら, PMID 42190949）が出て、**バイオハザード封じ込め・移動検査室・POCT**の観点から論点が足されており、著者回答（PMID 42486302）も出ている — **現在進行中の論争**として読むのが正しい。

#### 4-2. 核酸増幅検査の技術地図（2026-07・⚠️抄録のみ確認）

診断技術の側は動いている。**Khosrojerdi ら（*J Microbiol Methods* 2026;248:107618）**の技術レビューは、*Y. pestis* の核酸増幅検査（NAAT）を**従来PCR → リアルタイムPCR → 等温増幅（LAMP・RPA）→ droplet digital PCR → CRISPR基盤**という系譜で整理し、検出限界・感度・特異度、ヒト検体での臨床検証、そして **point-of-care としての成熟度**を比較している。将来方向としてAI統合デバイス・ウェアラブルセンサー・**凍結乾燥CRISPR検査**を挙げる。

⚠️ **この論文は本文を取得できていない**（出版社ページの取得が通らず、抄録のみ確認）。4つの比較表が本体なので、**具体的な数値は未確認**として扱う。中身が要るときは大学図書館経由か著者請求で取る。

標的遺伝子については別の一次資料から具体像が取れる。**Wang ら（*PLoS One* 2026;21(6):e0350660）**は *Y. pestis* の4標的 — **caf1（F1莢膜抗原）・pla（プラスミノゲン活性化因子）・ymt（マウス毒素）・ypo-1094** — を同時に見る四重リアルタイムPCRを構築し、他菌核酸との交差反応なし、検出下限 12.09×10⁻⁴ ng/µL、臨床血清検体で陽性例をすべて同定したと報告している。**複数標的を並べるのは、単一標的だと近縁 *Yersinia* 種や標的欠失株で外すことがある**ためで、ここは本体ノート §4 の「一つの検査で決めない」と同じ思想である。

#### 4-3. バボの大きさを治療効果の指標にしない（2026-03）

おまけだが実務的に効く。**Bourner ら（*PLoS Negl Trop Dis* 2026;20(3):e0014133）**は、マダガスカルの農村保健センター3か所で腺ペスト疑い例に**携帯エコー**を当て、D1/D4/D11 でバボの形態と大きさを追った（登録16例・確定12例）。結果は、**臨床的に改善してもバボの形態・大きさはほとんど変わらず、バボのサイズや形態と臨床状態に相関はなかった**。さらに**デジタルキャリパーでの計測はエコーと大きく乖離**した（訓練した臨床医はサイズ計測ならエコーで放射線科医と良好に一致するが、構造の評価は一致度が低い）。

n=12 の小規模研究なので確定ではないが、示唆は明確である。**「バボが小さくならないから抗菌薬が効いていない」と判断してはいけない**。治療反応は全身状態と解熱で見る。数世紀にわたって触診と観察だけで語られてきた所見に、初めて画像で物差しを当てたらこうなった、という話でもある。

実務上もう一つ大きいのは、**検査室に事前に伝える**ことである。*Y. pestis* は感染症法上の**一種病原体等**（第6条の「エルシニア属ペスティス（別名ペスト菌）」）に挙げられており、取り扱いには所持等の規制がかかる。培養を知らずに通常のワークフローに流すのは検査技師の曝露リスクになるため、疑った段階で検査室と保健所の双方に声をかけるのが順序になる（CDC も実験室曝露を曝露後予防の対象に挙げている）。

### 5. 治療 — 成人のクラスと用量

以下は CDC/MMWR 2021（Nelson ら、自然発生例の表1・表2）の成人推奨。**用量は肺/敗血症型（表1）と腺/咽頭型（表2）で同一**で、違いは第一選択の位置づけだけである。

| 薬剤 | 成人用量 | 肺/敗血症型 | 腺/咽頭型 |
|---|---|---|---|
| ゲンタマイシン | 5 mg/kg 24時間毎 IV or IM | 第一選択 | 第一選択 |
| ストレプトマイシン | 1 g 12時間毎 IV or IM | 第一選択 | 第一選択 |
| シプロフロキサシン | 400 mg 8時間毎 IV / 750 mg 12時間毎 PO | 第一選択 | 第一選択 |
| レボフロキサシン | 750 mg 24時間毎 IV or PO | 第一選択 | 第一選択 |
| モキシフロキサシン | 400 mg 24時間毎 IV or PO | 第一選択 | 第一選択 |
| ドキシサイクリン | 200 mg 負荷 → 100 mg 12時間毎 IV or PO | 代替 | **第一選択** |
| クロラムフェニコール | 12.5–25 mg/kg 6時間毎 IV（上限 1 g/回） | 代替 | 代替 |

運用の骨格は4つ。**(1)** 重症の肺・敗血症型は**異なる2クラスの併用**で開始し、臨床的改善後に単剤へ絞る。**(2)** 腺型・咽頭型はドキシサイクリンが第一選択で、大きなバボには代替薬や併用を考慮してよい。**(3)** 治療期間は**全病型 10–14日**、発熱の持続など懸念があれば延長。**(4)** 静注で開始しても**臨床的改善が明らかになれば経口へ切り替え可**。

ややこしい注記も押さえておくとよい。ゲンタマイシン・ストレプトマイシン・クロラムフェニコールは**ペストに対する FDA 承認がない**（適応外使用）。ストレプトマイシンの静注製剤は未承認で供給も限られる。シプロフロキサシンは経腸の代替ルート（経鼻胃管など）が使えない。日本ではクロラムフェニコール静注やストレプトマイシンの入手性がさらに問題になりうるので、**実際に疑った場面では保健所経由で専門医療機関（第一種感染症指定医療機関）に相談する**のが現実的な道筋になる。

なお Sebbane & Lemaître のレビュー（2021, Biomolecules）は、**併用療法が前臨床研究や症例報告で明確な上乗せ効果を示していない**ことを指摘し、現行の推奨は基本的に単剤である、と整理している。CDC が重症例に2クラス併用を置く理由は耐性への備えという別の文脈にあるため、両者は矛盾ではなく**想定する場面が違う**。薬剤耐性については CDC が「自然発生の耐性はきわめてまれで、米国内では報告がない」と記している。

### 6. 髄膜炎・小児・妊娠

**髄膜炎**: 髄膜炎の徴候があるときは**クロラムフェニコール + モキシフロキサシンまたはレボフロキサシン**の2剤で開始する。幼児でクロラムフェニコールが使えない・望ましくない場合はモキシフロキサシン/レボフロキサシンで代替する。二次性髄膜炎なら既存レジメンにクロラムフェニコール（またはモキシ/レボ）を追加し、**さらに10日間**続ける。髄液への到達性でレジメンが決まる点は他の重症感染と同じ発想である。

**小児**: モキシフロキサシンは小児（生後3か月〜17歳）では第一選択でなく代替（小児への FDA 承認がなく QTc 延長の報告率が高い）。プラゾマイシンは小児データ不足で非推奨。**8歳未満でもドキシサイクリンを使う** — 生命を脅かす感染では利益が歯牙着色などのリスクを上回るという判断である。テトラサイクリン・ミノサイクリンは他の選択肢を使い切ったときに回す。

**妊娠**: 妊娠中でも、胎児リスクがあっても適応があれば治療・予防を行う。**ゲンタマイシンがストレプトマイシンより優先**（ストレプトマイシンは胎児の聴器毒性リスク）。推奨レジメンは**ゲンタマイシン + シプロフロキサシンまたはレボフロキサシン**で、初期は非経口を優先。妊娠中は腎クリアランスが上がるためシプロフロキサシンはより頻回の投与が必要になる。曝露後予防では TMP-SMX がどの妊娠期でも支持されるが、**第3三半期の曝露は新生児の高ビリルビン血症リスクを担当チームに伝える**。肺ペストや第2・第3三半期では入院を考慮する。

### 7. 感染対策と曝露後予防 — 「飛沫」で足りるという設計

標準予防策は全例に。**肺ペストが疑われる/確定した例には飛沫予防策を追加**する。解除の条件は明確で、**抗菌薬を48時間以上投与し、臨床的改善があり、喀痰産生が著明に減少**したとき。バボ穿刺などの手技ではマスク・眼の防護・フェイスシールドを用いる。**N95 は通常のケアには不要**で、エアロゾル発生手技では考慮してよい。

曝露前予防は、標準+飛沫予防策を維持している初期対応者や医療者には**不要**。マスク不足・過密・換気不良といった状況では考慮し、**最後の曝露から48時間後に中止**する。曝露後予防は、**適切な個人防護なしに肺ペスト患者と 2m 以内の持続的接触**があった場合や、一定の実験室・動物曝露で考慮し、**7日間**行う（成人: ドキシサイクリン 100 mg 12時間毎 PO / シプロフロキサシン 500–750 mg 12時間毎 PO / レボフロキサシン 500–750 mg 24時間毎 PO、代替として TMP-SMX 5 mg/kg〈TMP 成分〉12時間毎 PO）。WHO も肺ペスト患者に曝露した医療者・濃厚接触者・腺ペスト患者の同居家族に**7日間の化学予防**を助言しており、国際的に数字は揃っている。

公衆衛生側の作法で面白いのは WHO の順序指定である。**齧歯類より先にノミを制御する** — 先に齧歯類を殺すと、宿主を失ったノミが新しい宿主（＝ヒト）を探すからである。ワクチンについては WHO は検査室職員や医療者といった高リスク群を除いて推奨していない。

### 8. 日本の制度 — 一類感染症・直ちに届出

感染症法（平成十年法律第百十四号）第6条第2項は一類感染症を列挙し、その第五号が**ペスト**である（他はエボラ出血熱・クリミア・コンゴ出血熱・痘そう・南米出血熱・マールブルグ病・ラッサ熱）。第12条第1項は、一類感染症の患者を診断したときは**「直ちに」**氏名・年齢・性別等を**最寄りの保健所長を経由して都道府県知事に届け出なければならない**と定める（第1号。7日以内でよいのは一部の五類のみ）。一類は氏名まで届出対象に入る点が五類以下と異なる。

届出の対象区分は5つ: **患者（確定例）/ 無症状病原体保有者 / 疑似症患者 / 感染症死亡者の死体 / 感染症死亡疑い者の死体**。すべて「直ちに」である。注目すべきは**疑似症患者と「死亡疑い者の死体」は検査確定を要しない** — 臨床所見と曝露歴から疑った段階で届出義務が生じる設計になっている。つまり制度の側も「確定を待つな」と言っている。

届出後の流れも押さえておくとよい。都道府県知事は第18条により就業制限の通知を行いうるし、第19条により**特定感染症指定医療機関または第一種感染症指定医療機関への入院を勧告**できる。家庭医の側の仕事は確定診断でも入院先の確保でもなく、**疑って、治療を始めて、直ちに保健所に繋ぐ**ところまでである。

### 9. 家庭医としての持ち帰り（5行）

1. **渡航歴（流行地＝コンゴ民主共和国・マダガスカル・米国西部など）と齧歯類/ノミ曝露**を、急速進行する発熱・リンパ節炎・肺炎で必ず聞く。これは届出要件そのもの
2. **強い疼痛を伴うリンパ節腫脹**はバボを疑う。ただし敗血症型は局所所見が先行しないので、バボ不在は除外根拠にならない
3. 鑑別は**類鼻疽（肺型に類似）と野兎病（腺型に類似・抗原共有）**を並べる
4. **疑った時点で治療を開始**し確定を待たない。成人はゲンタマイシンまたはフルオロキノロン（腺型はドキシサイクリンも第一選択）、重症は2クラス併用、10–14日
5. 同時に**検査室に事前連絡**し、**直ちに保健所へ届出**。肺型が疑わしければ飛沫予防策を追加、濃厚接触者には7日間の曝露後予防を検討

最終判定はたまさんが読んで決めてください。特に国内の薬剤入手性（クロラムフェニコール静注・ストレプトマイシン）と、実際の第一種感染症指定医療機関への繋ぎ方は、岐阜/地域の実情で埋める必要がある部分です。
<!-- LN:SYNTHESIS:END -->

## 📚 文献リスト
<!-- LN:REFS:START -->
### 一次資料（原文を開いて確認済み）
- ✅ **Nelson CA, Meaney-Delman D, Fleck-Derderian S, Cooley KM, Yu PA, Mead PS.** Antimicrobial Treatment and Prophylaxis of Plague: Recommendations for Naturally Acquired Infections and Bioterrorism Response. *MMWR Recomm Rep* 2021;70(RR-3):1-27. PMID 34264565 / [DOI](https://doi.org/10.15585/mmwr.rr7003a1) / [全文](https://www.cdc.gov/mmwr/volumes/70/rr/rr7003a1.htm) — 用量表・期間・妊娠・小児・曝露後予防の出典。本ノートの治療節はここに依拠
- ✅ **WHO** — [Plague fact sheet](https://www.who.int/news-room/fact-sheets/detail/plague)（2026-09-29 更新）。2019–2025 の報告集中国、病型、CFR 30–60%、F1 ラピッド検査、7日間化学予防、ノミ先行制御
- ✅ **厚生労働省** — [感染症法に基づく医師及び獣医師の届出について ５ ペスト](https://www.mhlw.go.jp/bunya/kenkou/kekkaku-kansenshou11/01-01-05.html)。定義・臨床的特徴・届出基準5区分・検査方法と検査材料の表・鑑別疾患（類鼻疽/野兎病）
- ✅ **感染症の予防及び感染症の患者に対する医療に関する法律**（平成十年法律第百十四号）第6条第2項第5号（一類感染症）・第6条（一種病原体等「エルシニア属ペスティス」）・第12条第1項（直ちに届出）・第18条（就業制限）・第19条（入院勧告）。e-Gov 法令 API で原文確認

### レビュー（PubMed 経由で抄録確認済み）
- ✅ **Sebbane F, Lemaître N.** Antibiotic Therapy of Plague: A Review. *Biomolecules* 2021;11(5):724. PMID 34065940 / [DOI](https://doi.org/10.3390/biom11050724) — 併用療法に明確な上乗せ効果が示されていないこと、各クラスの in vitro/動物データの食い違い、臨床試験の少なさ
- ✅ **Demeure CE, Dussurget O, Mas Fiol G, Le Guern AS, Savin C, Pizarro-Cerdá J.** *Yersinia pestis* and plague: an updated view on evolution, virulence determinants, immune subversion, vaccination, and diagnostics. *Genes Immun* 2019;20(5):357-370. PMID 30940874 / [DOI](https://doi.org/10.1038/s41435-019-0065-0) — F1 抗原を含む診断標的、無治療での死亡までの時間（腺 <1週 / 肺 <48時間）
- ⏳ **Sun W.** Plague Vaccines: Status and Future. *Adv Exp Med Biol* 2016;918:313-360. PMID 27722869 / [DOI](https://doi.org/10.1007/978-94-024-0890-4_12) — ワクチン開発の現状。次回織り直し時にワクチン節を立てるか判断

### モンゴル・中央アジアの疫学（§1 の出典）— ⚠️ワイヤー経由の二次情報
モンゴルについては**アクセスできる一次資料が実質無い**（NCZD 英語サイトは最新記事が2018年）。以下はワイヤーサービス経由で、年を本文の内部証拠で確かめたものだけを採った。
- ⚠️ [Xinhua (2026-07-25)](https://english.news.cn/asiapacific/20260725/52ed7127c5df463bbf87b8dd272f6e13/c.html) — **2026年7月のホブド省確定例**。細菌学的検査で確定、バヤンウルギー省ウランフス郡でマーモット肉を摂食。NCZD 発表として報道
- ⚠️ [Adnkronos (2026-07-22)](https://english.adnkronos.com/2026/07/22/mongolia-a-suspected-case-of-bubonic-plague-in-the-west/) — 同例の疑い段階（PCR 実施中）の報。確定前後の流れが追える
- ⚠️ [Outbreak News Today (2026-07-26)](https://outbreaknewstoday.substack.com/p/mongolia-human-plague-confirmed-in) — **21省中17省がリスク地域**、マーモット猟の法的禁止と密猟、夏季に増える季節性
- ⚠️ 17省・3万2千人接種計画の数字は Xinhua 系の二次報（[tbsnews 転載](https://www.tbsnews.net/node/107707)）。**原記事の日付が確定できず**、数字は参考値として扱う

### 診断の実力 — §4 の土台（2026-10-08 の初回収集から織り込み）
- ✅ **Raberahona M, Rajerison M, Edwards T, ... Randremanana RV, Olliaro P.** Performance of diagnostic procedures for bubonic plague in endemic settings in Madagascar: a prospective test accuracy sub-study within the IMASOY trial. *Clin Microbiol Infect* 2026;32(4):638-643. PMID 41389991 / [DOI](https://doi.org/10.1016/j.cmi.2025.12.002) — **本ノート §4-1 の出典**。疑い例438、PCR 85% > 培養 65%、血清が残り13%を拾う、**現場F1RDT 感度94%/特異度74%で臨床判断に使えない**、中央検査室条件なら特異度97.6%。NCT04110340
- ✅ **Amancio JGC, Gomes MM, Duarte BM, Almeida AMP, Bezerra MF.** Re: 'Performance of diagnostic procedures for bubonic plague in endemic settings in Madagascar' by Raberahona et al. *Clin Microbiol Infect* 2026. PMID 42190949 / [DOI](https://doi.org/10.1016/j.cmi.2026.05.022) — ブラジル Fiocruz からの書簡。論点は**バイオハザード封じ込め・移動検査室・POCT**（キーワードより）
- ✅ **Raberahona M, Olliaro P.** （同上への）author's response. *Clin Microbiol Infect* 2026. PMID 42486302 / [DOI](https://doi.org/10.1016/j.cmi.2026.07.027) — 著者回答。**論争は進行中**
- ✅ **Wang W, Zhang X, Yu H, Wang Z.** Establishment and application of a quadruple target real-time PCR assay for detecting *Yersinia pestis*. *PLoS One* 2026;21(6):e0350660. PMID 42224226 / [DOI](https://doi.org/10.1371/journal.pone.0350660) — **§4-2 の標的遺伝子の出典**。caf1・pla・ymt・ypo-1094 の4標的、交差反応なし、検出下限 12.09×10⁻⁴ ng/µL
- ✅ **Bourner J, Dwivedi R, Randremanana RV, ... Raberahona M, Olliaro P.** A prospective cohort study to describe the morphology of buboes in patients with bubonic plague using ultrasound imaging. *PLoS Negl Trop Dis* 2026;20(3):e0014133. PMID 41838707 / [DOI](https://doi.org/10.1371/journal.pntd.0014133) — **§4-3 の出典**。確定12例、**バボのサイズ・形態は臨床状態と相関せず**、キャリパー計測はエコーと乖離
- ⚠️ **Khosrojerdi M, Hashemi SA, Besharati R, Azimian A.** Nucleic acid amplification tests for *Yersinia pestis* detection: A comprehensive technical and field-oriented review. *J Microbiol Methods* 2026;248:107618. PMID 42413880 / [DOI](https://doi.org/10.1016/j.mimet.2026.107618) — **抄録のみ確認・本文未取得**（出版社ページの取得が通らず）。従来PCR→リアルタイムPCR→等温法(LAMP/RPA)→ddPCR→CRISPR基盤の技術比較と POC 成熟度。**4つの比較表が本体なので具体的数値は未確認**。要るときは図書館経由で取る
- ⏳ **Peng W, et al.** Protective outcomes of high-affinity monoclonal antibodies against drug-resistant plague strains. *Front Immunol* 2026;17:1835695. PMID 42416072 / [DOI](https://doi.org/10.3389/fimmu.2026.1835695) — F1抗原標的のモノクローナル抗体のマウス実験（ストレプトマイシン耐性株想定）。**前臨床・ヒト適用未確立**なので本文には入れていない
### おまけ（歴史編の出典は別ファイル）
- 📖 [ペスト・歴史編](plague-history.ja.md) — 三度のパンデミック / quarantine の語源 / 菌の発見をめぐる競争 / 黒死病と ERAP2

*（PubMed から取得した情報を含みます。各論文の DOI リンクを併記しています。）*
<!-- LN:REFS:END -->

## 🪵 更新ログ
<!-- LN:LOG:START -->

### ⏳ 2026-10-16 収集分 (11件・織り待ち)

- **Quarantine, diplomacy, and epidemics: Jean-Étienne-Justin Schneider and the Bubonic Plague of Sīstān in 1906.** — Arabian S, Zargaran A, Sadr M et al. *J Med Ethics Hist Med* (2026). PMID [42859662](https://pubmed.ncbi.nlm.nih.gov/42859662/) / [DOI](https://doi.org/10.18502/jmehm.v19i10.22301)
  - 抄録: The 1906 Sīstān bubonic plague was one of the most significant public health crises of the late Qājār period. This study examines the role of Jean-Étienne-Justin Schneider (1854-1917), head of the Central Sanitary Council (Majles-e Ḥefẓ al-Ṣeḥḥa), in implementing quarantine policies and their impact…
- **Clinical Characterization and Outcomes of Pneumonic Plague in Madagascar: A Case Series.** — Raberahona M, Razananaivo LH, Edwards T et al. *Open Forum Infect Dis* (2026). PMID [42851858](https://pubmed.ncbi.nlm.nih.gov/42851858/) / [DOI](https://doi.org/10.1093/ofid/ofag635)
  - 抄録: Pneumonic plague is rare compared to bubonic plague; data on clinical presentation and treatment outcomes are scant. We report on 13 prospectively-enrolled suspected pneumonic plague cases (7 laboratory-confirmed, one probable, 5 not-plague) treated with aminoglycoside plus ciprofloxacin for 10 days…
- **Evolutionary trends of plague research from 2016 to 2025: A bibliometric analysis.** — Niu Y, Zhang Y, Zhou S et al. *PLoS Negl Trop Dis* (2026). PMID [42127162](https://pubmed.ncbi.nlm.nih.gov/42127162/) / [DOI](https://doi.org/10.1371/journal.pntd.0014337)
  - 抄録: Plague is a severe zoonotic disease caused by Yersinia pestis, a pathogen characterized by high infectivity and mortality rates. Historically, three global pandemics have inflicted heavy disasters on human society. Despite improvements in control measures and the application of antibiotics, plague h…
- **The impact of the COVID-19 pandemic on healthy volunteer motivations: a mixed-methods study of participants in plague vaccine trials in the UK and Uganda.** — Stuart AS, Muhumuza R, Kusemererwa S et al. *BMC Public Health* (2026). PMID [42104293](https://pubmed.ncbi.nlm.nih.gov/42104293/) / [DOI](https://doi.org/10.1186/s12889-026-27297-1)
  - 抄録: The COVID-19 pandemic led to unprecedented interest and participation in vaccine trials globally, and a concurrent increase in vaccine hesitancy. Whether this impacted recruitment of healthy volunteers to subsequent non-COVID vaccine trials is not well studied. We explored the impact of the COVID-19…
- **Epidemic imaginaries in literature and film: a comparative study of narrative responses to plague and pandemic.** — Bhatt BR, Dwivedi P *Med Humanit* (2026). PMID [42103463](https://pubmed.ncbi.nlm.nih.gov/42103463/) / [DOI](https://doi.org/10.1136/medhum-2025-013615)
  - 抄録: Epidemics have historically been both biomedical disasters and cultural stories that societies interpret and recount. This study explores the epidemic imaginary, examining how literature and cinema symbolically depict contagion by analysing narratives of contagion produced during the Plague era in l…
- **Genetic Diversity and Spatial Distribution of Yersinia pestis by Core Genome-Based Multilocus Sequence Typing Analysis.** — Appelt S, Rohleder AM, Schmidt K et al. *Microorganisms* (2026). PMID [42075294](https://pubmed.ncbi.nlm.nih.gov/42075294/) / [DOI](https://doi.org/10.3390/microorganisms14040898)
  - 抄録: Yersinia pestis is the etiological agent of plague, a severe and often fatal disease in humans when left untreated. Because of the high genetic clonality of Y. pestis, high-resolution genotyping assays are necessary to differentiate between individual strains. Here, we report on the development and …
- **Targeted mutagenesis of the ICP4 transactivation domain generates a protective DIVA vaccine against duck plague.** — Yang Q, Pan C, Wang L et al. *Poult Sci* (2026). PMID [42061247](https://pubmed.ncbi.nlm.nih.gov/42061247/) / [DOI](https://doi.org/10.1016/j.psj.2026.106960)
  - 抄録: Duck plague, caused by duck plague virus (DPV), causes significant economic losses to the global waterfowl industry. The control of this disease is hampered by the limitations of conventional vaccines, which include the risk of virulence reversion, short-lived immunity, and the inability to differen…
- **Avian herpesvirus-specific LORF5 is a late gene, interacts with 19 viral and 111 host proteins, critical for virulence of Duck plague virus.** — Li H, Cheng A, Wang M et al. *Poult Sci* (2026). PMID [42048789](https://pubmed.ncbi.nlm.nih.gov/42048789/) / [DOI](https://doi.org/10.1016/j.psj.2026.106924)
  - 抄録: Duck plague virus (DPV) poses a major threat to the waterfowl industry. Its genome encodes multiple avian herpesvirus-specific genes with unknown functions, which hinders the understanding of the mechanism underlying DPV pathogenesis. LORF5 is among the more conserved genes, yet the properties and b…
- **The Role of Polymorphism of HLA Class II Genes in Postvaccination Plague Immunity.** — Korytov KM, Dubrovina VI, Pyatyidesyatnikova AB et al. *Bull Exp Biol Med* (2026). PMID [42036551](https://pubmed.ncbi.nlm.nih.gov/42036551/) / [DOI](https://doi.org/10.1007/s10517-026-06656-3)
  - 抄録: We evaluated the association of alleles of human leukocyte antigen (HLA) class II genes and the levels of secretion of IL-4 and IFNγ in the blood of individuals vaccinated/revaccinated with a live plague vaccine and living in the Gorno-Altai high-mountain and Tuvinian mountain natural plague foci. S…
- **The plague of Athens (430-427 BC): Integration of historical, clinical, and ancient DNA data supports an invasive non-typhoidal Salmonella enterica etiology.** — Trakatelli CM, Kitsios K, Agathangelidi-Trakatelli M et al. *Int J Infect Dis* (2026). PMID [42034283](https://pubmed.ncbi.nlm.nih.gov/42034283/) / [DOI](https://doi.org/10.1016/j.ijid.2026.108728)
  - 抄録: The Plague of Athens represents one of the earliest and most detailed descriptions of a large-scale epidemic in recorded history. Emerging in 430 BC during the second year of the Peloponnesian War, it caused extensive mortality, including the death of Pericles, the leader of Athenian democracy at th…
- **Nursing the colonised: the politics of representation of the Western nurse in plague-stricken Bombay.** — Koshy R *Med Hist* (2026). PMID [42026837](https://pubmed.ncbi.nlm.nih.gov/42026837/) / [DOI](https://doi.org/10.1017/mdh.2026.10061)
  - 抄録: The 1896 Bombay plague outbreak prompted the colonial government to recruit trained British nurses from England to serve the afflicted Indians of the Presidency. Studying this relatively under-explored aspect of British colonial nursing, this paper examines the politics of representation of the West…

### ⏳ 2026-10-09 収集分 (20件・織り待ち)

- **Russia plague outbreak: Epidemic risk is low, says WHO.** — Wise J *BMJ* (2026). PMID [42843840](https://pubmed.ncbi.nlm.nih.gov/42843840/) / [DOI](https://doi.org/10.1136/bmj-2026-101084)
- **Russia plague outbreak after reported death of lab worker: what you need to know.** — Wise J *BMJ* (2026). PMID [42833683](https://pubmed.ncbi.nlm.nih.gov/42833683/) / [DOI](https://doi.org/10.1136/bmj-2026-101046)
- **Bayesian Parameter Estimation and Stochastic Extinction Analysis in a Seasonal Bubonic Plague Transmission Model.** — Kumari S, Mandal PS *Bull Math Biol* (2026). PMID [42782382](https://pubmed.ncbi.nlm.nih.gov/42782382/) / [DOI](https://doi.org/10.1007/s11538-026-01762-9)
  - 抄録: Mathematical models of plague dynamics provide insight into zoonotic transmission processes and epidemic persistence but often neglect stochastic effects and seasonal variability. In this study, we examine how seasonal variability influences zoonotic disease transmission through a rat-flea-human pla…
- **The Last Great Plague of Istanbul, 1812: An Overture to Biopolitics in the Ottoman Empire.** — Wigen E, Topal AE, Trombino C *J Hist Med Allied Sci* (2026). PMID [42770908](https://pubmed.ncbi.nlm.nih.gov/42770908/) / [DOI](https://doi.org/10.1093/jhmas/jrag031)
  - 抄録: Starting in 1812, a plague epidemic killed a third of the population in Istanbul and a third of the population of Izmir. It lasted at least until 1819 and killed some 500,000 people across the Balkans and the eastern and southern coasts of the Mediterranean, including Malta, Algiers, and Bucharest. …
- **Rational attenuation of duck plague virus by targeting the ICP4 DNA-binding domain generates a safe and efficacious live vaccine candidate.** — Wu Y, He Y, Wang C et al. *Poult Sci* (2026). PMID [42679716](https://pubmed.ncbi.nlm.nih.gov/42679716/) / [DOI](https://doi.org/10.1016/j.psj.2026.107474)
  - 抄録: Duck plague (DP) is an acute, highly lethal disease of waterfowl caused by duck plague virus (DPV). Viral latency and reactivation pose persistent threats, and current vaccines lack DIVA capability while risking insufficient immunogenicity or reversion to virulence. We targeted the DPV ICP4 DNA-bind…
- **The 1820 Mallorca plague was not a classic bubonic outbreak.** — Puig P, Pujadas-Mora JM *Proc Natl Acad Sci U S A* (2026). PMID [42607223](https://pubmed.ncbi.nlm.nih.gov/42607223/) / [DOI](https://doi.org/10.1073/pnas.2536892123)
  - 抄録: The 1820 plague outbreak in eastern Mallorca-long treated as a local episode and traditionally classified as a late bubonic manifestation of the Second Plague Pandemic-offers a unique opportunity to reassess transmission dynamics in a prebacteriological context. Using a previously unexamined primary…
- **Reply to the Letter to the Editor concerning "The plague of Athens (430-427 BC): Integration of historical, clinical, and ancient DNA data supports an invasive nontyphoidal Salmonella enterica a etiology".** — Trakatelli CM, Kitsios K, Agathangelidi-Trakatelli M et al. *Int J Infect Dis* (2026). PMID [42580511](https://pubmed.ncbi.nlm.nih.gov/42580511/) / [DOI](https://doi.org/10.1016/j.ijid.2026.109042)
- **Genomic Characterization of an Emergent Cross-Border Recombinant Duck Plague Virus With High Pathogenicity and Reduced Vaccine Efficacy in Guangxi, China.** — Yang S, Xu S, Wang K et al. *Transbound Emerg Dis* (2026). PMID [42576545](https://pubmed.ncbi.nlm.nih.gov/42576545/) / [DOI](https://doi.org/10.1155/tbed/8379232)
  - 抄録: Duck plague virus (DPV) is a major pathogen causing recurrent outbreaks in waterfowl. This study reports the comprehensive characterization of a novel DPV strain, designated GXGG240520, isolated from clinically diseased ducks in Guangxi, China. The strain was confirmed as a virulent DPV by PCR targe…
- **Early-life stress at the time of the plague in Northern Italy (17th century): The case of two individuals with severe hypoplastic defects from Lazzaretto Vecchio (Venice).** — Magri S, Higgins OA, Figus C et al. *Arch Oral Biol* (2026). PMID [42531995](https://pubmed.ncbi.nlm.nih.gov/42531995/) / [DOI](https://doi.org/10.1016/j.archoralbio.2026.106706)
  - 抄録: This study investigates two cases of severe enamel hypoplasia observed in individuals buried at Lazzaretto Vecchio (Venice, Italy) likely during the 1575-1630 plague outbreak. By integrating histological and geochemical evidence, we assess whether severe hypoplastic defects correspond to alterations…
- **Epidemiological and Epizootological Monitoring and Spatiotemporal Dynamics of Plague in Natural Foci of Kazakhstan.** — Abdel Z, Zhumadilova Z, Mussagalieva R et al. *Pathogens* (2026). PMID [42515012](https://pubmed.ncbi.nlm.nih.gov/42515012/) / [DOI](https://doi.org/10.3390/pathogens15070685)
  - 抄録: Plague remains a significant natural focal zoonotic infection with continuing epidemiological relevance in the Republic of Kazakhstan. This study provides a comprehensive assessment of epizootological dynamics in natural plague foci during 2020-2025 through the integration of historical epidemiologi…
- **Famine, plague, and slaughters: The fleeing famine hypothesis of anorexia nervosa reconsidered.** — Udupa NS, Velimirović M, Robison M et al. *Psychol Rev* (2026). PMID [42475006](https://pubmed.ncbi.nlm.nih.gov/42475006/) / [DOI](https://doi.org/10.1037/rev0000643)
  - 抄録: The fleeing famine hypothesis (FFH) posits that a genetically and evolutionarily based predisposition for food restriction and hyperactivity is activated among susceptible humans and nonhumans upon experiencing a prolonged energy deficit. Such circumstances manifest in the counterintuitive responses…
- **Letter to the editor on "The plague of Athens (430-427 BC): integration of historical, clinical, and ancient DNA data supports an invasive nontyphoidal Salmonella enterica etiology," by Trakatelli et al., 2026.** — Rojo-Marcos G *Int J Infect Dis* (2026). PMID [42468736](https://pubmed.ncbi.nlm.nih.gov/42468736/) / [DOI](https://doi.org/10.1016/j.ijid.2026.108991)
- **Vascular-associated bacterial burden and neuroinflammatory transcriptional responses observed in models of pneumonic plague.** — Smith BA, Klimko CP, Rodriguez CI et al. *Front Microbiol* (2026). PMID [42422735](https://pubmed.ncbi.nlm.nih.gov/42422735/) / [DOI](https://doi.org/10.3389/fmicb.2026.1865125)
  - 抄録: Yersinia pestis is the etiologic agent of plague, and the disease is categorized into several forms, including bubonic, septicemic, and pneumonic. Plague meningitis is a rare but severe complication and estimated to occur in 6-11% of documented cases. It is most frequently observed in bubonic plague…
- **A field-deployable high-resolution SNP genotyping platform for rapid surveillance of Yersinia pestis.** — Liu Y, Huang Q, Wu Y et al. *Virulence* (2026). PMID [42418343](https://pubmed.ncbi.nlm.nih.gov/42418343/) / [DOI](https://doi.org/10.1080/21505594.2026.2700072)
  - 抄録: Yersinia pestis, the causative agent of plague, poses a persistent global health threat due to its rapid transmission and high mortality. To enable rapid, field-deployable surveillance, we developed a high-resolution, culture-independent genotyping assay for precise identification of Y. pestis linea…
- **In Vitro Selection of Antibodies Targeting Yersinia pestis Membrane Lipids Using Nanodisc-Based Antigen Presentation.** — Bolding MR, Mozden SC, Pimentel OR et al. *Pathogens* (2026). PMID [42347263](https://pubmed.ncbi.nlm.nih.gov/42347263/) / [DOI](https://doi.org/10.3390/pathogens15060651)
  - 抄録: Proteins are the most common targets for antibody discovery and vaccine development, but their sequence variability can limit the breadth of resulting antigens. Lipids represent an alternative class of antigens due to their structural conservation and roles in host-pathogen interactions. Here, we de…
- **Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago.** — Macleod R, Seersholm FV, De Sanctis B et al. *Nature* (2026). PMID [42310115](https://pubmed.ncbi.nlm.nih.gov/42310115/) / [DOI](https://doi.org/10.1038/s41586-026-10540-5)
  - 抄録: Plague is among the most devastating diseases in human history1. However, early strains of the plague-causing bacterium Yersinia pestis lacked virulence factors that are required for the bubonic form until around 3,800 years ago2,3. Consequently, the morbidity and mortality of early plague strains r…
- **Bills of Mortality and the Birth of Epidemic Surveillance: Evidence, Uncertainty, and Decision-Making in Defoe's Plague Narrative.** — Tatsiou E, Karamanou M *Cureus* (2026). PMID [42266286](https://pubmed.ncbi.nlm.nih.gov/42266286/) / [DOI](https://doi.org/10.7759/cureus.108532)
  - 抄録: By drawing parallels rather than following events exactly, we interpret Daniel Defoe's most important work as a literary response to the Bills of Mortality that foreshadows enduring concerns of epidemic surveillance. These include the aggregation of deaths in time and space, the interpretation of tr…
- **An Overview of the Genetic Diversity and Epidemiological Potential of Yersinia pestis Populations in Natural Plague Foci of Kazakhstan.** — Abdirassilova A, Yessimseit D, Kassenova A et al. *Pathogens* (2026). PMID [42198677](https://pubmed.ncbi.nlm.nih.gov/42198677/) / [DOI](https://doi.org/10.3390/pathogens15050551)
  - 抄録: This review provides a comprehensive overview of the genetic diversity and epidemiological potential of Yersinia pestis in Kazakhstan's natural plague foci, emphasizing the link between genotypic variation and outbreak capacity. Integrating historical epidemiological records with contemporary microb…
- **A Likely Plague Epizootic Involving Wild Lagomorphs in the Mojave Desert of California: Public Health and Ecological Implications.** — Davis RM, Biggins DE *Vector Borne Zoonotic Dis* (2026). PMID [42138633](https://pubmed.ncbi.nlm.nih.gov/42138633/) / [DOI](https://doi.org/10.1177/15303667261451608)
  - 抄録: Plague is a disease that poses serious threats to public and ecosystem health. Its causative bacterium, Yersinia pestis, was transported to North America around 1900, where it quickly became established in native rodent populations and spread throughout the western half of the United States by the m…
- **[Optimization and applicability evaluation of pretreatment method for rapid detection of Yersinia pestis in clinical samples by the up-converting phosphor technology-based immunochromatographic assay].** — Tang Z, Zhang YY, Shen XN et al. *Zhonghua Yu Fang Yi Xue Za Zhi* (2026). PMID [42128683](https://pubmed.ncbi.nlm.nih.gov/42128683/) / [DOI](https://doi.org/10.3760/cma.j.cn112150-20250508-00401)
  - 抄録: Objective: To optimize the pretreatment method of clinical samples in the up-converting phosphor technology-based immunochromatographic assay (UPT-ICA) for Yersinia pestis and evaluate its applicability. Methods: A total of 464 clinical samples (including 215 serum samples, 60 cerebrospinal fluid sa…
- **2026-10-08** 初織り。向きは臨床・公衆衛生（たまさん選択）。一次資料は MMWR 2021 全文・WHO ファクトシート・厚労省届出基準（Shift_JIS を iconv で復号して原文確認）・感染症法原文（e-Gov API）。歴史編は別ファイルに分離（公開版では上のリンク先）。週次の自動収集の対象トピックとして登録済み
- **2026-10-08（2回目・同日）** §4 診断を全面改稿。初回収集でヒットした Raberahona 2026（IMASOY 精度サブ研究）が**「PCR > 培養」「現場F1RDTは臨床判断に使えない（特異度74%）」**という土台の書き換えだったため、4-1/4-2/4-3 に分節。5行サマリの治療行にも反映。NAAT レビュー（Khosrojerdi 2026）は**本文未取得**のため ⚠️ 扱いで数値は載せず

- **2026-10-13（2回目）** §1 疫学に**モンゴル・中央アジア**を追加（たまさんの持ち込みから）。21省中17省がリスク地域、直近確定例は2026年7月のホブド省、経路は**マーモット肉の摂食** — つまり問診項目に「野生齧歯類を食べたか」が加わる。モンゴルは一次資料が実質無く（NCZD 英語サイトは2018年止まり）ワイヤー依存である旨も明記。公開版の更新ログから本家のファイル名表記を外した
- **2026-10-08（4回目・同日）** 公開ミラーの仕組みを拡張。本文を丸ごと写す設計だったため「一部の節だけ本家に留める」が表現できなかったので、`living_note_public_sync.py` に private ブロック除外機構を TDD で追加（テスト5本・先に落ちることを確認済み）。**このノートの公開版は、本家から一部の節を除いたものである**
<!-- LN:LOG:END -->
