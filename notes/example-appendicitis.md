---
topic: 虫垂炎 / appendicitis
slug: appendicitis
updated: 2026-09-13
lang: en
---

# 🌱 Living note: Appendicitis (live translated mirror)

> **Live translated mirror** — the author's working note is the Japanese
> [example-appendicitis.ja.md](example-appendicitis.ja.md); each weekly collection & re-weave is
> machine-translated into English here by the weaver AI. **Last check: 2026-09-13 JST.**
> **The content is an AI-woven summary of the literature — do not take it at face value.**
> Clinical decisions must follow the original papers and the judgment of treating
> clinicians. ⏳ = collected, awaiting weave / ✅ = woven into the body.
> (This note began as a frozen one-shot sample on 2026-08-07 and became a live
> translated mirror on 2026-09-07.)

## 📌 Five-line summary
<!-- LN:SUMMARY:START -->
- Appendicitis is the most common surgical acute abdomen. Lifetime risk 6-9%, peak at 10-19 years. Beyond the "nutrition-microbiome-genetic axis," uncomplicated and complicated disease may be "two different diseases" with distinct cytokine profiles (Ryoo / Han 2026)
- Diagnosis is converging on "**don't decide with one test, don't decide at one time point**": Alvarado cannot be used alone (specificity 57-76%), the continuous pARC model beats fixed point-scoring, and for early equivocal cases the move is to **observe and re-measure** — the AUROC of a single AAS, 0.629, jumps to 0.936 for the final AAS and 0.932 for ∆AAS (Tchouala Tchakoute / Lastunen 2026)
- On imaging, in-hospital CT is strongest, MRI is the pillar in pregnancy (sensitivity 0.95 / specificity 0.97), and POCUS is rule-in only. The arena has shifted from a contest over accuracy to **"who triages, and where, and how to cut overuse (imaging, referral)"**, with an implementation RCT of a prediction rule + CRP POCT in primary care now underway (Hogervorst 2026, NCT06762275)
- For non-perforated disease, surgery vs antibiotics is shared decision-making — but **the picture changes along the time axis**: with follow-up beyond 2 years (median 33.6 months), NOM failure is 38.9%, 44.4% when restricted to RCTs, and 36.3% end up undergoing appendectomy; meanwhile the cost advantage of €1535 holds even in the long run (Kahana 2026)
- For complicated disease, the decision axis for interval appendectomy has moved to "age-linked neoplasm risk" (colorectal neoplasm after appendicitis in those aged 40 or older: 0.5-34.6%; no established follow-up standard). The library has gone from 3 to 37 papers — a pace that demands a "living review" of the same kind as the living evidence map (Kleindienst 2026)
<!-- LN:SUMMARY:END -->

## 🧵 Cross-cutting synthesis
<!-- LN:SYNTHESIS:START -->
### Diagnosis
The conclusion of the AHRQ systematic review that comprehensively covered diagnostic accuracy for right
lower quadrant pain (Dahabreh 2015, over 1000 studies) — **"symptoms, physical findings, and blood tests
are not powerful enough on their own; confirmation comes from imaging"** — is still the skeleton. CT is the
strongest across every target population, with sensitivity 0.96-1.0 and specificity 0.91-1.0. In pregnancy,
MRI is the alternative pillar (Danawar 2026) — and that position has now gained **quantitative backing of
sensitivity 0.95 and specificity 0.97 (AUC 0.961)** in an updated meta-analysis of 34 studies (Habiro Alves
2026), reaching the point of being recommended as "the standard second-line choice after inconclusive
ultrasound." The familiar caveat that "US is operator-dependent" has been quantified in the POCUS era:
POCUS performed by emergency physicians has sensitivity 0.78 and specificity 0.89, meaning **a positive
scan can be used to rule in but a negative scan cannot exclude**, and accuracy shifts with whether the
operator has fellowship training (Kamal 2026, meta-analysis of 15 studies).

The standing of clinical scores has likewise been clarified, from "adjunct" to **"not to be used alone — one
component of a stepwise, multimodal approach."** According to a review comparing Alvarado with alternative
tools in children (Tchouala Tchakoute 2026, literature from 2016-2026), Alvarado has good sensitivity but
**specificity of only 57-76% at a cutoff of ≥7**, and so cannot stand alone. Among pediatric-specific scores,
**PAS wins on sensitivity and AIR on specificity, and AIR is also strong at discriminating complicated
disease such as gangrene, phlegmon, and perforation**. Furthermore, **a continuous risk model (pARC)
outperforms fixed point-scoring in pediatric cohorts** — a move that shifts scoring from "adding up points"
to "estimating a probability." Layering CRP, the neutrophil-to-lymphocyte ratio (NLR), and selective
ultrasound on top of this, and deploying CT only for indeterminate cases, is the optimal solution — that is
this review's conclusion.

The 2026-09 arrival adds **a dimension of time** to this move away from scores used alone. According to a
secondary analysis of the observation arm of the DIAMOND trial, restricted to adults with early, difficult-to-
judge presentations (early equivocal) (Lastunen 2026, 83 patients), **a single Adult Appendicitis Score (AAS)
at presentation has an AUROC of 0.629 (95%CI 0.498-0.760), barely usable**, whereas the **final AAS
re-scored after a short period of observation reaches 0.936 (0.886-0.987), and ∆AAS, the change in score
during observation, 0.932 (0.868-0.996)** (∆CRP sits in between at 0.796). Cut at the thresholds given in the
abstract (low ≤ -2 / intermediate -1 to 0 / high ≥ 1), the **negative predictive value in the low-probability
group is 97% and the positive predictive value in the high-probability group is 94%**. In other words, for
early equivocal abdominal pain there are situations where **"measure again and look at the difference"**
works better than adding another test — and that is simultaneously a strategy for **reducing overdiagnosis
and radiation exposure from early CT**. That said, this is a secondary analysis of a single trial with n=83, the
thresholds were derived from the ROC on the same data (no external validation), and the optimal observation
interval is not specified. This two-step migration of scoring — from "adding up points" → "estimating a
probability" → **"a function of time"** — is another face of the same design philosophy as the "don't decide
with one test" stance of the primary-care strategy described below.

New biomarker forces have also assembled: IL-6, promising in children (Tan & Bo 2026), is now backed by
prospective adult data — in an analysis of 48 cytokines, complicated appendicitis showed significantly higher
IL-6, HGF, and MCP-1, with IL-6 alone predicting complicated disease at AUC 0.785 (Han 2026) — followed by
AI models (AUC 0.85-0.96, with CT deep learning most accurate but predominantly retrospective, single-
center, and lacking external validation; Ismayilzada 2026).

However, this accuracy debate has consistently **presumed patients who have already reached a hospital or
ER**. The 2026-08 arrival moves the arena upstream — to **the entrance of primary care**. In Dutch general
practice, a hybrid type 1 (effectiveness × implementation) cluster RCT has begun, comparing usual care with a
diagnostic strategy bundling an externally validated 7-item prediction rule, CRP POCT, and risk-stratified
management advice (Hogervorst 2026, NCT06762275). Children aged 4-18 with acute abdominal pain (onset
within 7 days) are stratified into low, intermediate, and high risk; low risk gets safety netting, high risk
immediate referral, and only the intermediate group is triaged with CRP POCT (CRP <10 mg/L → safety netting;
10-50 mg/L → either re-evaluation or immediate referral, chosen by the GP's clinical judgement together with
the child's and parents' preference; ≥50 mg/L → immediate referral). What is new is that the primary outcome
is neither sensitivity nor specificity but **"referral efficiency" = the proportion of children without appendicitis
who avoided referral over 30 days (target 88%→95% among 566 children without appendicitis)** — the question
posed is not a competition over imaging accuracy but a primary-care one: **can over-referral be reduced without
raising the threshold for missed cases?** Running an implementation evaluation (reach / adoption / implementation
/ maintenance) in parallel is likewise a pre-emptive move against the "accuracy achieved but never lands in
practice" problem. Results are not yet reported (protocol stage). This structure — **placing low risk into safety
netting to make time an ally, then triaging at re-evaluation** — is continuous with Lastunen 2026's "observe and
re-measure," different settings (primary care vs ER) notwithstanding: both answer in the same way, by **using
time to cut overuse (referral, imaging)**.

Differentials and pitfalls have also accumulated: pinworm (Enterobius vermicularis) in children mimicking
appendicitis (Jaffry 2026), a misdiagnosed case of idiopathic encapsulating peritoneal sclerosis (abdominal
cocoon) (Martzivanou 2026), and the fact that **stump appendicitis can occur even after a previous
appendectomy** (Gupta 2026, 25-year review) — "already had an appendectomy" does not rule appendicitis out.

### Treatment
**Uncomplicated (non-perforated)**: both appendectomy and antibiotics-first are options, with shared
decision-making informed by the presence or absence of an appendicolith as the standard form (Talan &
Di Saverio 2021) — that skeleton is unchanged, but the 2026 arrivals deepened the debate in three
directions. (1) A meta-analysis of RCTs of antibiotics vs surgery has appeared for **children and
adolescents** as well (Allocati 2026), though it drew a comment questioning the robustness of the
conclusion once prediction intervals are considered (Nasri & Dziri 2026). (2) Going a step further, a
**meta-analysis of antibiotics vs observation without medication, asking whether the antibiotics
themselves are needed** has emerged (Lin 2026), followed by a comparison of optimal pediatric
regimens (Kakar 2026). (3) On **cost-effectiveness**, conservative treatment is superior (surgery costs
16.5-83% more, Farhad 2026). Patient selection and algorithms are being organized in a cluster of
narrative reviews (Rincon Mora / Baana / Lehovsky & Hall / Hong for children, all 2026), and in children
**endoscopic retrograde appendicitis therapy (ERAT) is starting to be discussed as a third option
alongside surgery and antibiotics** (Hong 2026). Because the evidence is growing too fast, an evidence
map tracking the whole field as a living systematic review (Kleindienst 2026) has even appeared. Surgery
still holds first-line position, with laparoscopy the standard (Vidarsdottir 2025).

And now **a fourth axis, time**, has joined this debate. Most previous RCTs spoke of non-inferiority at
1 year, but **a meta-analysis restricted to studies with follow-up of 2 years or more** (Kahana 2026, 1635
studies screened down to 9 studies, 3883 patients, of which 3 were RCTs and 5 were pediatric; median
follow-up 33.6 months, maximum 312 months) returns a different picture: **long-term NOM failure rate
38.9% (95%CI 31.1-46.7), 44.4% (41.4-47.4) when restricted to RCTs, and 36.3% (28.9-43.7) eventually
undergoing appendectomy after NOM**. In other words, the "80% success at 1 year" story is **replaced,
over a horizon of several years, by "around 40% end up having surgery after all"** — the very numbers
handed to patients in SDM change. Cost, on the other hand, keeps favouring NOM even long term
(**difference €1535, 95%CI -1892 to -1178**), extending Farhad 2026's "capped at 12 months" limitation by
one notch. Appendiceal neoplasms found during NOM run at about 0.3%, connecting to the neoplasm-risk
axis discussed below. That said, 6 of the studies are non-randomized and the definition of "failure" varies
between studies, so this 40% figure should be kept in mind as **a coarse metric unaccompanied by the
severity of recurrence, quality of life, or satisfaction**.

**Complicated**: in children, laparoscopy is safe even in cases complicated by abscess (Wang 2026,
prospective cohort). After conservative treatment, **the decision axis for interval appendectomy has moved
from "recurrence prevention" to "selection based on age-linked neoplasm risk plus imaging findings"**
(Gosavi 2026; for children, the APSA systematic review Sulkowski 2026). This neoplasm-risk axis extends
beyond interval appendectomy as well: **in those aged 40 or older, detection rates of colorectal neoplasm
after appendicitis of 0.5-34.6% and risk increases of 1.2-38.5-fold** have been reported (Spota 2026,
scoping review of 17 studies), but all are retrospective and fall short of supporting a recommended
follow-up standard, stopping at a proposed framework for prospective research. In perioperative
management, single-dose antibiotics may be equivalent to continued postoperative therapy in
non-perforated gangrenous appendicitis (Ozen 2026, antibiotic stewardship); postoperative intra-abdominal
abscess remains the major complication in pediatric perforated disease (Borca 2026); and an RCT of a
modified ERAS protocol shortened length of stay (Calderón-Alvarado 2026) — optimization of "after the cut"
is advancing, and an **evidence-based synthesis of nursing care** covering pain management, infection
prevention, and discharge support (Stansell 2026) has joined this line.

### Epidemiology and pathophysiology
Lifetime risk ranges across sources from 6-7% (Vidarsdottir 2025) to 7-9% (Kleindienst 2026), with a peak at
10-19 years. Regional variation, diet, and socioeconomic status have long been implicated, and now a review
has appeared that pushes this dietary hypothesis into mechanism and formulates it as **the "nutrition-
microbiome-genetic axis"** (Ryoo 2026) — a pathophysiological model that complements rather than replaces
the luminal-obstruction theory. Resonating with that overview, **cytokine profiles have been shown to differ
clearly between uncomplicated and complicated disease** (IL-6, HGF, and MCP-1 elevated in complicated
disease; Han 2026, prospective, 113 patients), immunologically reinforcing the view that "complicated
appendicitis is not merely a progressed form of uncomplicated disease but a different disease" — the
theoretical foundation on which NOM works for uncomplicated cases. In children, the relationship between
nutritional status and perforation risk has also been examined: **obesity and BMI alone do not predict
perforation, whereas low body weight and albumin/prealbumin-type indicators are more consistently
associated with complicated disease** (Borca 2026, 14 studies). The clinical essential — that because
progression to perforation and abscess formation occurs, prompt diagnosis determines prognosis — is
unchanged. And once one takes into account the primary-care denominator that "most children with acute
abdominal pain have a benign, self-limiting condition" (the referral efficiency of usual care assumed by
Hogervorst 2026 is 88%), the very gap between prevalence as discussed in hospital populations and
prevalence as seen in primary care becomes a design variable for diagnostic strategy. The fact that findings
shift depending on the point in time between onset and presentation (which is exactly why ∆AAS works,
Lastunen 2026) is likewise evidence that we are looking not at "appendicitis as a single disease image" but at
**a process that moves as a function of time**.

### Open questions
- Recurrence rate, QOL, and satisfaction **beyond 5 years** in the antibiotics-first arm — the beyond-2-year gap has been filled by Kahana 2026 (failure 38.9%, median 33.6 months), but
  the definition of "failure" varies between studies, and the severity of recurrence and the patient experience remain a black box
- A large RCT of antibiotics vs observation without medication (raised by Lin 2026) — a re-examination of the content of "antibiotics-first" itself
- Robustness of the pediatric NOM recommendation — replication clearing the prediction-interval problem (Nasri & Dziri 2026). Integration with the 40% long-term failure rate (Kahana 2026, 5 of 9 studies pediatric) is also needed
- External validation and transportability of the continuous risk model pARC — whether the finding that it outperforms fixed point-scoring (Tchouala Tchakoute 2026)
  holds outside Europe/North America and in adults, and whether it can actually be deployed in an EHR (on the adult side, repeated AAS measurement is filling the same gap by another route)
- **External validation of ∆AAS (observe and re-measure)** — the optimal observation interval, the validity of the thresholds (Lastunen 2026 is a secondary analysis of a single trial with n=83 and
  thresholds derived from internal data), transportability to children and pregnant patients, and whether the "temporal difference" can be built into a pARC-type continuous model
- The place of ERAT (endoscopic retrograde appendicitis therapy) in children — comparative trials against surgery and antibiotics (raised by Hong 2026)
- Quantification of the age threshold and imaging findings that determine indications for interval appendectomy (stratification by neoplasm risk)
- Colonoscopic follow-up after appendicitis in those aged 40 or older — prospective validation of indications and timing (Spota 2026 proposes a framework)
- Predictors of failure other than appendicolith — preoperative discrimination of complicated disease via biomarkers such as IL-6 (+HGF/MCP-1) × imaging × AI
- Multicenter, prospective external validation and implementation of AI diagnostic models (EHR/PACS integration)
- Whether a primary-care prediction rule + CRP POCT actually reduces over-referral without increasing delayed diagnosis — awaiting the results of Hogervorst 2026 (NCT06762275). Extrapolability to free-access health systems without gatekeeping (including Japan) has not been examined
<!-- LN:SYNTHESIS:END -->

## 📚 Bibliography (library)
<!-- LN:BIB:START -->
1. **Talan DA, Di Saverio S.** Treatment of Acute Uncomplicated Appendicitis. *N Engl J Med* 2021;385(12):1116-1123. PMID [34525287](https://pubmed.ncbi.nlm.nih.gov/34525287/) / [DOI](https://doi.org/10.1056/NEJMcp2107675) — library key `Talan2021-hm`
2. **Dahabreh IJ, et al.** Diagnosis of Right Lower Quadrant Pain and Suspected Acute Appendicitis. AHRQ Comparative Effectiveness Review No.157, 2015. [Full text (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK355441/) — library key `Dahabreh2015-cr`
3. **Vidarsdottir GM, Vidarsdottir H, Moller PH.** Appendicitis – review. *Laeknabladid* 2025;111(9):366-373. PMID [40853752](https://pubmed.ncbi.nlm.nih.gov/40853752/) / [DOI](https://doi.org/10.17992/lbl.2025.09.853) — imported from team citations on 8/7
4. **Jaffry K, Tran A, Hyune MA et al.** Enterobius vermicularis as a Mimic of Acute Appendicitis: A Case Report and Updated Systematic Review. *Cureus* 2026. PMID [42559549](https://pubmed.ncbi.nlm.nih.gov/42559549/) / [DOI](https://doi.org/10.7759/cureus.112171)
5. **Kakar M, Kulibaba G, Merchant Z et al.** Comparison of Two Antibiotic Combinations for Conservative Treatment of Non-Complicated Appendicitis in Children. *Medicina (Kaunas)* 2026. PMID [42512941](https://pubmed.ncbi.nlm.nih.gov/42512941/) / [DOI](https://doi.org/10.3390/medicina62071399)
6. **Nasri S, Dziri C.** Comment to: Nonoperative Management of Uncomplicated Acute Appendicitis — "Importance of Prediction Interval". *World J Surg* 2026. PMID [42489860](https://pubmed.ncbi.nlm.nih.gov/42489860/) / [DOI](https://doi.org/10.1002/wjs.70510)
7. **Ryoo MC, Hwang DL, Roura E.** Nutritional and dietary drivers in the pathogenesis of acute appendicitis: the nutrition-microbiome-genetic axis. *Proc Nutr Soc* 2026. PMID [42396694](https://pubmed.ncbi.nlm.nih.gov/42396694/) / [DOI](https://doi.org/10.1017/S0029665126105047)
8. **Ozen C, Yalcinkaya A, Eberhard MC et al.** Antibiotic stewardship in non-perforated gangrenous appendicitis: single-dose versus postoperative therapy. *Langenbecks Arch Surg* 2026. PMID [42393469](https://pubmed.ncbi.nlm.nih.gov/42393469/) / [DOI](https://doi.org/10.1007/s00423-026-04129-9)
9. **Kleindienst D, Mohr J, Maurer K et al.** Evidence map of appendicitis — a living systematic review with meta-analyses. *Langenbecks Arch Surg* 2026. PMID [42384223](https://pubmed.ncbi.nlm.nih.gov/42384223/) / [DOI](https://doi.org/10.1007/s00423-026-04113-3)
10. **Allocati E, Gerardi C, Ceresoli M et al.** Nonoperative Management of Uncomplicated Acute Appendicitis in Children and Adolescents: Systematic Review and Meta-Analysis of RCTs. *World J Surg* 2026. PMID [42251641](https://pubmed.ncbi.nlm.nih.gov/42251641/) / [DOI](https://doi.org/10.1002/wjs.70439)
11. **Wang B, Liu M, Li Z et al.** Laparoscopic appendectomy for complicated appendicitis with periappendiceal abscess versus without abscess in children: a prospective cohort study. *Surg Endosc* 2026. PMID [42209857](https://pubmed.ncbi.nlm.nih.gov/42209857/) / [DOI](https://doi.org/10.1007/s00464-026-12891-6)
12. **Danawar NA, Almohamad MM, Alkhoms KA et al.** Assessment of Acute Appendicitis in Pregnant Women: A Systematic Review of Current Evidence. *Cureus* 2026. PMID [42170145](https://pubmed.ncbi.nlm.nih.gov/42170145/) / [DOI](https://doi.org/10.7759/cureus.107410)
13. **Gupta A.** Stump Appendicitis: A 25-Year Review of Pathophysiology, Diagnosis, and Management (2000-2025). *Cureus* 2026. PMID [42158785](https://pubmed.ncbi.nlm.nih.gov/42158785/) / [DOI](https://doi.org/10.7759/cureus.107297)
14. **Stetson A, Orlas C, Li R et al.** Corrigendum to "Surgery or no surgery for pediatric uncomplicated appendicitis?" *Surgery* 2026. PMID [42115105](https://pubmed.ncbi.nlm.nih.gov/42115105/) / [DOI](https://doi.org/10.1016/j.surg.2026.110226)
15. **Lin WT, Huang YN, Wang JH et al.** Effect of antibiotic therapy versus no antibiotics on nonoperative management outcomes in uncomplicated appendicitis: systematic review and meta-analysis. *Int J Colorectal Dis* 2026. PMID [42105101](https://pubmed.ncbi.nlm.nih.gov/42105101/) / [DOI](https://doi.org/10.1007/s00384-026-05147-1)
16. **Tan L, Bo C.** The value of interleukin-6 in predicting acute appendicitis in children and distinguishing complicated appendicitis: systematic review and meta-analysis. *Front Immunol* 2026. PMID [42079617](https://pubmed.ncbi.nlm.nih.gov/42079617/) / [DOI](https://doi.org/10.3389/fimmu.2026.1790229)
17. **Borca CI, Cindrea AC, Margan MM et al.** Post-Appendectomy Intra-Abdominal Abscess in Children with Perforated Appendicitis: A Narrative Review. *Medicina (Kaunas)* 2026. PMID [42075558](https://pubmed.ncbi.nlm.nih.gov/42075558/) / [DOI](https://doi.org/10.3390/medicina62040686)
18. **Rincon Mora SA.** Current Management of Uncomplicated Acute Appendicitis: A Narrative Review of Nonoperative and Surgical Strategies. *Cureus* 2026. PMID [42064497](https://pubmed.ncbi.nlm.nih.gov/42064497/) / [DOI](https://doi.org/10.7759/cureus.106086)
19. **Lehovsky K, Hall NJ.** Is Appendicectomy Outdated in the Management of Paediatric Appendicitis? *Br J Hosp Med (Lond)* 2026. PMID [42053000](https://pubmed.ncbi.nlm.nih.gov/42053000/) / [DOI](https://doi.org/10.31083/BJHM53108)
20. **Gosavi R, McMurrick P, Teoh W et al.** Interval Appendicectomy after Conservative Management of Complicated Appendicitis: Balancing Recurrence, Neoplasm Risk, and Surveillance Strategies. *Dig Surg* 2026. PMID [42048268](https://pubmed.ncbi.nlm.nih.gov/42048268/) / [DOI](https://doi.org/10.1159/000552093)
21. **Sulkowski JP, Huerta CT, Tashiro J et al.** Interval appendectomy practices for complicated appendicitis in children: systematic review (APSA Outcomes and Evidence-Based Practice Committee). *Pediatr Surg Int* 2026. PMID [42043565](https://pubmed.ncbi.nlm.nih.gov/42043565/) / [DOI](https://doi.org/10.1007/s00383-026-06445-z)
22. **Baana M, Singh M, Banfa M et al.** Non-operative Management of Uncomplicated Appendicitis: A Review of Indications, Safety, and Clinical Algorithms. *Cureus* 2026. PMID [41994787](https://pubmed.ncbi.nlm.nih.gov/41994787/) / [DOI](https://doi.org/10.7759/cureus.105154)
23. **Calderón-Alvarado AB, Ambriz-González G, Fuentes-Orozco C et al.** Modified ERAS protocol for pediatric complicated appendicitis: a randomized clinical trial. *Pediatr Surg Int* 2026. PMID [41984227](https://pubmed.ncbi.nlm.nih.gov/41984227/) / [DOI](https://doi.org/10.1007/s00383-026-06422-6)
24. **Borca CI, Ivan CS, Fira-Mladinescu C et al.** Nutritional Status as a Risk Factor for Appendiceal Perforation in Pediatric Acute Appendicitis: Systematic Review. *Children (Basel)* 2026. PMID [41897039](https://pubmed.ncbi.nlm.nih.gov/41897039/) / [DOI](https://doi.org/10.3390/children13030326)
25. **Martzivanou EC, Atmatzidis S, Voloudakis N et al.** Idiopathic Encapsulating Peritoneal Sclerosis Mimicking Acute Appendicitis: A Case Report and Systematic Literature Review. *Am J Case Rep* 2026. PMID [41894320](https://pubmed.ncbi.nlm.nih.gov/41894320/) / [DOI](https://doi.org/10.12659/AJCR.951103)
26. **Farhad I, Khan MA, Kler A et al.** The Cost-Effectiveness of Conservatively Managed Acute Appendicitis Versus Appendicectomy: A Systematic Review. *Surg Laparosc Endosc Percutan Tech* 2026. PMID [41880556](https://pubmed.ncbi.nlm.nih.gov/41880556/) / [DOI](https://doi.org/10.1097/SLE.0000000000001454)
27. **Ismayilzada K.** Artificial intelligence for acute appendicitis diagnosis: A systematic review of current evidence, challenges, and future directions. *Medicine (Baltimore)* 2026. PMID [41861187](https://pubmed.ncbi.nlm.nih.gov/41861187/) / [DOI](https://doi.org/10.1097/MD.0000000000048094)
28. **Kamal MM, Al Reshidi BM, Bedier HM et al.** Diagnostic Accuracy of Point-of-Care Ultrasound (POCUS) for Suspected Acute Appendicitis in Pediatric and Adult Emergency Departments: A Systematic Review and Meta-Analysis. *Cureus* 2026. PMID [41841098](https://pubmed.ncbi.nlm.nih.gov/41841098/) / [DOI](https://doi.org/10.7759/cureus.103503)
29. **Habiro Alves L, Machado GF, Martin GCC et al.** Accuracy of magnetic resonance imaging for acute appendicitis in pregnant women: an updated diagnostic systematic review and meta-analysis. *Abdom Radiol (NY)* 2026. PMID [41801387](https://pubmed.ncbi.nlm.nih.gov/41801387/) / [DOI](https://doi.org/10.1007/s00261-026-05416-1)
30. **Hong B, Zhao K, Zhu G.** Operative and non-operative management of acute appendicitis in children: a narrative review. *Pediatr Surg Int* 2026. PMID [41746383](https://pubmed.ncbi.nlm.nih.gov/41746383/) / [DOI](https://doi.org/10.1007/s00383-026-06358-x)
31. **Stansell P, Francis-Johnson P.** Appendicitis: Integrating evidence-based nursing care into clinical practice. *Nursing* 2026;56(3):29-36. PMID [41725098](https://pubmed.ncbi.nlm.nih.gov/41725098/) / [DOI](https://doi.org/10.1097/NSG.0000000000000356)
32. **Han T, Borman T, Vanhatalo S et al.** Uncomplicated and Complicated Acute Appendicitis Induce Different Cytokine Patterns. *APMIS* 2026;134(2):e70168. PMID [41711118](https://pubmed.ncbi.nlm.nih.gov/41711118/) / [DOI](https://doi.org/10.1111/apm.70168)
33. **Spota A, Englesakis M, Chadi S et al.** Acute Appendicitis as a Harbinger of Colorectal Neoplasms in Patients Aged 40 or Older: A Scoping Review. *Surg Laparosc Endosc Percutan Tech* 2026. PMID [41707661](https://pubmed.ncbi.nlm.nih.gov/41707661/) / [DOI](https://doi.org/10.1097/SLE.0000000000001451)
34. **Hogervorst EM, Venekamp RP, Knol-de Vries GE et al.** Impact of a diagnostic strategy for appendicitis in children with acute abdominal pain in primary care: study protocol for a hybrid type 1 cluster randomised controlled trial. *Diagn Progn Res* 2026;10(1). PMID [42596001](https://pubmed.ncbi.nlm.nih.gov/42596001/) / [DOI](https://doi.org/10.1186/s41512-026-00234-x) — ClinicalTrials.gov [NCT06762275](https://clinicaltrials.gov/study/NCT06762275)
35. **Tchouala Tchakoute P, Iuhas A, Nechita VI et al.** Comparison of the Alvarado Score with Alternative Diagnostic Tools in Pediatric Acute Appendicitis: A Literature Review. *Pediatr Rep* 2026;18(4):115. PMID [42646659](https://pubmed.ncbi.nlm.nih.gov/42646659/) / [DOI](https://doi.org/10.3390/pediatric18040115) — [PMC13516179](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13516179/) (free full text)
36. **Kahana N, Boaz E, Emile SH et al.** Long-term outcomes of non-operative compared to operative management of acute uncomplicated appendicitis — a systematic review and meta-analysis. *Am J Surg* 2026;261:117203. PMID [42636733](https://pubmed.ncbi.nlm.nih.gov/42636733/) / [DOI](https://doi.org/10.1016/j.amjsurg.2026.117203)
37. **Lastunen KS, Leppäniemi AK, Mentula PJ.** Repeated scoring with the adult appendicitis score improves the sensitivity and the specificity of appendicitis diagnosis in patients with early equivocal signs of appendicitis: a secondary analysis. *Eur J Trauma Emerg Surg* 2026;52(1). PMID [42690425](https://pubmed.ncbi.nlm.nih.gov/42690425/) / [DOI](https://doi.org/10.1007/s00068-026-03326-x) — [PMC13541895](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13541895/) (free full text) · secondary analysis of the observation arm of the DIAMOND trial [NCT02742402](https://clinicaltrials.gov/study/NCT02742402)

> ※ Nos. 4-28 are the first batch of 2026-08-07, Nos. 29-33 the second batch that same day, No. 34 the 2026-08-14 batch, Nos. 35-36 the 2026-08-29 batch,
> and No. 37 the portion woven in from the 2026-09-13 batch. All bibliographic records have been cross-checked in full against PubMed metadata (get_article_metadata).
> On the collection-log side, DOIs belonging to other papers had been mixed into 9 entries in the first batch (corresponding to Nos. 5, 10, 11, 15, 16, 17, 21, 23, 24) and
> 2 entries in the second batch as well (corresponding to Nos. 29, 30), so this list has been corrected to the PubMed-verified values. For the 2026-08-14 batch (No. 34), the 2026-08-29 batch
> (Nos. 35-36), and the 2026-09-13 batch (No. 37), both PMID and DOI agree between the collection log and the PubMed-verified values — **three consecutive batches with no contamination**.
> The DOI extraction in `living_notes_update.py` (suspected of mis-picking from the references section) is still formally unrepaired, but the contamination is confined to the first and second batches
> (2026-08-07), and it is likely to have resolved on its own through a change in the collection logic or on the source side. If the next batch also agrees, it can be downgraded to
> "no repair needed — monitoring only."

<!-- LN:BIB:END -->

## 🆕 Arrivals log
<!-- LN:LOG:START -->

### ✅ Collected 2026-09-13 (1 item · woven in)

- **Repeated scoring with the adult appendicitis score improves the sensitivity and the specificity of appendicitis diagnosis in patients with early equivocal signs of appendicitis: a secondary analysis.** — Lastunen KS, Leppäniemi AK, Mentula PJ *Eur J Trauma Emerg Surg* (2026). PMID [42690425](https://pubmed.ncbi.nlm.nih.gov/42690425/) / [DOI](https://doi.org/10.1007/s00068-026-03326-x)
  - Abstract: The utilization of computed tomography in the early stage of acute appendicitis may result in overdiagnosis and unnecessarily expose patients to ionising radiation. The Adult Appendicitis Score (AAS) can be used to select patients for imaging. Observation and re-scoring in the DIAMOND trial reduced …

### ✅ Collected 2026-08-29 (2 items · woven in)

- **Comparison of the Alvarado Score with Alternative Diagnostic Tools in Pediatric Acute Appendicitis: A Literature Review.** — Tchouala Tchakoute P, Iuhas A, Nechita VI et al. *Pediatr Rep* (2026). PMID [42646659](https://pubmed.ncbi.nlm.nih.gov/42646659/) / [DOI](https://doi.org/10.3390/pediatric18040115)
  - Abstract: Acute appendicitis is a leading pediatric surgical emergency. Timely diagnosis remains challenging, particularly in young children with atypical presentations. Clinical evaluation alone yields variable diagnostic performance, prompting the use of risk stratification tools. To evaluate and compare th…
- **Long-term outcomes of non-operative compared to operative management of acute uncomplicated appendicitis - a systematic review and meta-analysis.** — Kahana N, Boaz E, Emile SH et al. *Am J Surg* (2026). PMID [42636733](https://pubmed.ncbi.nlm.nih.gov/42636733/) / [DOI](https://doi.org/10.1016/j.amjsurg.2026.117203)
  - Abstract: We evaluated long-term outcomes of non-operative management (NOM) versus surgical management of acute uncomplicated appendicitis. Systematic review of studies comparing NOM versus surgery with ≥2 years follow-up. Primary outcome was long-term failure rate. 9/1635 studies were included (3 RCTs; 6 non…

### ✅ Collected 2026-08-14 (1 item · woven in)

- **Impact of a diagnostic strategy for appendicitis in children with acute abdominal pain in primary care: study protocol for a hybrid type 1 cluster randomised controlled trial.** — Hogervorst EM, Venekamp RP, Knol-de Vries GE et al. *Diagn Progn Res* (2026). PMID [42596001](https://pubmed.ncbi.nlm.nih.gov/42596001/) / [DOI](https://doi.org/10.1186/s41512-026-00234-x)
  - Abstract: Children with acute abdominal pain pose a diagnostic challenge for general practitioners (GPs), as it can be difficult to distinguish appendicitis from self-limiting conditions due to overlapping symptoms. To support GPs, a diagnostic strategy for appendicitis was developed that integrates an extern…

### ✅ Collected 2026-08-07 (5 items · woven in)

- **Accuracy of magnetic resonance imaging for acute appendicitis in pregnant women: an updated diagnostic systematic review and meta-analysis.** — Habiro Alves L, Machado GF, Martin GCC et al. *Abdom Radiol (NY)* (2026). PMID [41801387](https://pubmed.ncbi.nlm.nih.gov/41801387/) / [DOI](https://doi.org/10.1007/s00261-026-05416-1)
  - Abstract: Diagnosing acute appendicitis during pregnancy is challenging due to physiological changes and concerns regarding fetal radiation exposure from Computed Tomography (CT). This systematic review and meta-analysis evaluates the diagnostic accuracy and safety of Magnetic Resonance Imaging (MRI) for susp…
- **Operative and non-operative management of acute appendicitis in children: a narrative review.** — Hong B, Zhao K, Zhu G *Pediatr Surg Int* (2026). PMID [41746383](https://pubmed.ncbi.nlm.nih.gov/41746383/) / [DOI](https://doi.org/10.1007/s00383-026-06358-x)
  - Abstract: Appendicitis represents a prevalent medical condition among pediatric and adolescent populations, often necessitating emergency surgical procedures. For nearly two hundred years, the management of appendicitis has been conceptualized as a surgical challenge. In contemporary practice, minimally invas…
- **Appendicitis: Integrating evidence-based nursing care into clinical practice.** — Stansell P, Francis-Johnson P *Nursing* (2026). PMID [41725098](https://pubmed.ncbi.nlm.nih.gov/41725098/) / [DOI](https://doi.org/10.1097/nsg.0000000000000356)
  - Abstract: Appendicitis is a global disease that affects people of all ages, but occurs most often between ages 5 and 45 years. It is one of the most common causes of acute abdominal surgery and, if left untreated, it is a surgical emergency that requires prompt intervention. Nurses play a vital role in managi…
- **Uncomplicated and Complicated Acute Appendicitis Induce Different Cytokine Patterns.** — Han T, Borman T, Vanhatalo S et al. *APMIS* (2026). PMID [41711118](https://pubmed.ncbi.nlm.nih.gov/41711118/) / [DOI](https://doi.org/10.1111/apm.70168)
  - Abstract: Although acute appendicitis is one of the most common reasons for emergency surgery, the immunopathogenesis of appendicitis is unclear. The aim of this prospective pre-defined subgroup analysis study was to characterize serum cytokine profiles and their diagnostic potential in distinguishing between…
- **Acute Appendicitis as a Harbinger of Colorectal Neoplasms in Patients Aged 40 or Older: A Scoping Review.** — Spota A, Englesakis M, Chadi S et al. *Surg Laparosc Endosc Percutan Tech* (2026). PMID [41707661](https://pubmed.ncbi.nlm.nih.gov/41707661/) / [DOI](https://doi.org/10.1097/sle.0000000000001451)
  - Abstract: Current guidelines on follow-up for acute appendicitis (AA) neglect the risk of colorectal cancer after AA. Heterogeneous and low-level evidence hinders drawing recommendations on follow-up of 40-year-old or older patients after AA, looking for colorectal neoplasms. This study aims to summarize exis…

### ✅ Collected 2026-08-07 (25 items · woven in)

- **Enterobius vermicularis as a Mimic of Acute Appendicitis: A Case Report and Updated Systematic Review.** — Jaffry K, Tran A, Hyune MA et al. *Cureus* (2026). PMID [42559549](https://pubmed.ncbi.nlm.nih.gov/42559549/) / [DOI](https://doi.org/10.7759/cureus.112171)
  - Abstract: A 12-year-old premenarchal female patient presented with right iliac fossa pain, perianal pruritus, urticaria, angioedema, arthralgia, peripheral eosinophilia, and an initially undetectable C-reactive protein. Serial ultrasonography demonstrated increasing intra-abdominal free fluid. Diagnostic lapa…
- **Comparison of Two Antibiotic Combinations for Conservative Treatment of Non-Complicated Appendicitis in Children.** — Kakar M, Kulibaba G, Merchant Z et al. *Medicina (Kaunas)* (2026). PMID [42512941](https://pubmed.ncbi.nlm.nih.gov/42512941/) / [DOI](https://doi.org/10.3390/medicina62071399)
  - Abstract: Background and Objectives: Acute appendicitis is the most common surgical emergency in children. The standard of care has been appendectomy for many years. However, in recent years, studies investigating antibiotic therapy alone have increased rapidly, suggesting that non-operative management may be…
- **Comment to: Nonoperative Management of Uncomplicated Acute Appendicitis: A Systematic Review and Meta-Analysis of Randomized Clinical Trials Comparing Antibiotic Treatment and Appendectomy in Children and Adolescents: "Importance of Prediction Interval".** — Nasri S, Dziri C *World J Surg* (2026). PMID [42489860](https://pubmed.ncbi.nlm.nih.gov/42489860/) / [DOI](https://doi.org/10.1002/wjs.70510)
- **Nutritional and dietary drivers in the pathogenesis of acute appendicitis: the nutrition-microbiome-genetic axis.** — Ryoo MC, Hwang DL, Roura E *Proc Nutr Soc* (2026). PMID [42396694](https://pubmed.ncbi.nlm.nih.gov/42396694/) / [DOI](https://doi.org/10.1017/s0029665126105047)
  - Abstract: Acute appendicitis is one of the leading causes of surgical emergency hospitalizations. However, the mechanisms leading to the development of appendicitis are poorly understood. Current knowledge suggests an interplay probably led by dietary habits with impact on the microbiome which elicits respons…
- **Antibiotic stewardship in non-perforated gangrenous appendicitis: outcomes of single-dose versus postoperative therapy in a retrospective cohort study.** — Ozen C, Yalcinkaya A, Eberhard MC et al. *Langenbecks Arch Surg* (2026). PMID [42393469](https://pubmed.ncbi.nlm.nih.gov/42393469/) / [DOI](https://doi.org/10.1007/s00423-026-04129-9)
  - Abstract: Nonperforated gangrenous appendicitis (NGA) is a severe inflammatory condition without perforation, and the optimal duration of postoperative antibiotic therapy remains debated. This study aimed to compare outcomes between single-dose antibiotic therapy (SDAT) and postoperative antibiotic therapy (P…
- **Evidence map of appendicitis - a living systematic review with meta-analyses.** — Kleindienst D, Mohr J, Maurer K et al. *Langenbecks Arch Surg* (2026). PMID [42384223](https://pubmed.ncbi.nlm.nih.gov/42384223/) / [DOI](https://doi.org/10.1007/s00423-026-04113-3)
  - Abstract: Appendicitis is one of the most common diseases of the gastrointestinal tract with a lifetime incidence of 7 to 9%. Appendectomy is one of the most performed emergency surgeries. Recently, non-operative treatments are emerging. It is almost impossible to keep the overview on the large and growing bo…
- **Nonoperative Management of Uncomplicated Acute Appendicitis: A Systematic Review and Meta-Analysis of Randomized Clinical Trials Comparing Antibiotic Treatment and Appendectomy in Children and Adolescents.** — Allocati E, Gerardi C, Ceresoli M et al. *World J Surg* (2026). PMID [42251641](https://pubmed.ncbi.nlm.nih.gov/42251641/) / [DOI](https://doi.org/10.1002/wjs.70439)
  - Abstract: This systematic review with meta-analysis aims to evaluate the current evidence comparing antibiotic therapy with the surgical gold standard (appendectomy) for the treatment of uncomplicated acute appendicitis (UAA) in children and adolescents. This systematic review and meta-analysis followed PRISM…
- **Laparoscopic appendectomy for complicated appendicitis with periappendiceal abscess versus without abscess in children: a prospective cohort study.** — Wang B, Liu M, Li Z et al. *Surg Endosc* (2026). PMID [42209857](https://pubmed.ncbi.nlm.nih.gov/42209857/) / [DOI](https://doi.org/10.1007/s00464-026-12891-6)
  - Abstract: To date, no prospective studies have focused on laparoscopic treatment for complicated appendicitis in children with or without abscess. This study aimed to evaluate the safety and efficacy of laparoscopic treatment for complicated appendicitis in children with and without abscess prospectively. A s…
- **Assessment of Acute Appendicitis in Pregnant Women: A Systematic Review of Current Evidence.** — Danawar NA, Almohamad MM, Alkhoms KA et al. *Cureus* (2026). PMID [42170145](https://pubmed.ncbi.nlm.nih.gov/42170145/) / [DOI](https://doi.org/10.7759/cureus.107410)
  - Abstract: The most frequent nonobstetric surgical emergency during pregnancy is acute appendicitis (AA); however, diagnosing it is still difficult because of anatomical and physiological changes. While magnetic resonance imaging (MRI) has emerged as a possible substitute, traditional methods such as clinical …
- **Stump Appendicitis: A 25-Year Review of Pathophysiology, Diagnosis, and Management (2000-2025).** — Gupta A *Cureus* (2026). PMID [42158785](https://pubmed.ncbi.nlm.nih.gov/42158785/) / [DOI](https://doi.org/10.7759/cureus.107297)
  - Abstract: Acute appendicitis is one of the most common causes of right lower quadrant (RLQ) abdominal pain, and appendectomy remains the standard treatment. However, residual appendiceal tissue may persist after surgery and subsequently become inflamed, resulting in stump appendicitis, a rare but clinically s…
- **Corrigendum to "Surgery or no surgery for pediatric uncomplicated appendicitis? A systematic review and meta-analysis to inform management" [Surgery 188 (2025) 109728].** — Stetson A, Orlas C, Li R et al. *Surgery* (2026). PMID [42115105](https://pubmed.ncbi.nlm.nih.gov/42115105/) / [DOI](https://doi.org/10.1016/j.surg.2026.110226)
- **Effect of antibiotic therapy versus no antibiotics on nonoperative management outcomes in uncomplicated appendicitis: A systematic review and meta-analysis.** — Lin WT, Huang YN, Wang JH et al. *Int J Colorectal Dis* (2026). PMID [42105101](https://pubmed.ncbi.nlm.nih.gov/42105101/) / [DOI](https://doi.org/10.1007/s00384-026-05147-1)
  - Abstract: Although antibiotics are a recognized alternative to appendectomy for uncomplicated appendicitis, their specific benefit over observation alone remains unclear. This systematic review and meta-analysis aimed to isolate the antibiotic effect by directly contrasting antibiotics with observation in pat…
- **The value of interleukin-6 in predicting acute appendicitis in children and distinguishing complicated appendicitis: a systematic review and meta-analysis.** — Tan L, Bo C *Front Immunol* (2026). PMID [42079617](https://pubmed.ncbi.nlm.nih.gov/42079617/) / [DOI](https://doi.org/10.3389/fimmu.2026.1790229)
  - Abstract: The identification of new, easily measurable biomarkers may assist clinicians in diagnosing and managing acute appendicitis. Although inflammatory markers have been applied in pediatric appendicitis diagnosis, the diagnostic and disease assessment value of interleukin-6 (IL-6) as a key inflammatory …
- **Post-Appendectomy Intra-Abdominal Abscess in Children with Perforated Appendicitis: A Narrative Review.** — Borca CI, Cindrea AC, Margan MM et al. *Medicina (Kaunas)* (2026). PMID [42075558](https://pubmed.ncbi.nlm.nih.gov/42075558/) / [DOI](https://doi.org/10.3390/medicina62040686)
  - Abstract: Post-appendectomy intra-abdominal abscess (PAA) is a common and problematic complication in children with perforated appendicitis, contributing to prolonged hospitalization, readmissions, and increased healthcare costs. Despite advances in surgical and antimicrobial management, substantial heterogen…
- **Current Management of Uncomplicated Acute Appendicitis: A Narrative Review of Nonoperative and Surgical Strategies.** — Rincon Mora SA *Cureus* (2026). PMID [42064497](https://pubmed.ncbi.nlm.nih.gov/42064497/) / [DOI](https://doi.org/10.7759/cureus.106086)
  - Abstract: Acute appendicitis remains one of the most common surgical emergencies worldwide and has traditionally been treated with appendectomy. However, growing evidence from randomized trials and international guidelines has challenged this paradigm, suggesting that nonoperative management with antibiotics …
- **Is Appendicectomy Outdated in the Management of Paediatric Appendicitis?** — Lehovsky K, Hall NJ *Br J Hosp Med (Lond)* (2026). PMID [42053000](https://pubmed.ncbi.nlm.nih.gov/42053000/) / [DOI](https://doi.org/10.31083/bjhm53108)
  - Abstract: Appendicitis is the most common emergency surgical presentation and is particularly prevalent in the paediatric population. At present, the majority of children are managed with surgical removal of the inflamed appendix, a procedure that was established centuries ago, before the widespread availabil…
- **Interval Appendicectomy after Conservative Management of Complicated Appendicitis: Balancing Recurrence, Neoplasm Risk, and Surveillance Strategies.** — Gosavi R, McMurrick P, Teoh W et al. *Dig Surg* (2026). PMID [42048268](https://pubmed.ncbi.nlm.nih.gov/42048268/) / [DOI](https://doi.org/10.1159/000552093)
  - Abstract: Non-operative management (NOM) of complicated appendicitis is increasingly accepted, but the role of interval appendicectomy (IA) remains contentious. Contemporary evidence has shifted decision-making from recurrence risk alone toward age-linked neoplasm risk and radiological features. Recurrence af…
- **Interval appendectomy practices for complicated appendicitis in children: a systematic review from the APSA Outcomes and Evidence-Based Practice Committee.** — Sulkowski JP, Huerta CT, Tashiro J et al. *Pediatr Surg Int* (2026). PMID [42043565](https://pubmed.ncbi.nlm.nih.gov/42043565/) / [DOI](https://doi.org/10.1007/s00383-026-06445-z)
  - Abstract: BACKGROUND: This review summarizes considerations within the existing recent literature that guide the practice of interval appendectomy (IA) after initial non-operative management (NOM) of complicated appendicitis (CA) in children. METHODS: A systematic review of English language articles published…
- **Non-operative Management of Uncomplicated Appendicitis: A Review of Indications, Safety, and Clinical Algorithms.** — Baana M, Singh M, Banfa M et al. *Cureus* (2026). PMID [41994787](https://pubmed.ncbi.nlm.nih.gov/41994787/) / [DOI](https://doi.org/10.7759/cureus.105154)
  - Abstract: Acute uncomplicated appendicitis has traditionally been managed with appendectomy, yet accumulating evidence supports antibiotic-only treatment as a safe alternative in carefully selected patients. This narrative review synthesizes current data on the indications, safety, treatment protocols and cli…
- **Modified enhanced recovery after surgery protocol for pediatric complicated appendicitis in a Mexican tertiary hospital: a randomized clinical trial.** — Calderón-Alvarado AB, Ambriz-González G, Fuentes-Orozco C et al. *Pediatr Surg Int* (2026). PMID [41984227](https://pubmed.ncbi.nlm.nih.gov/41984227/) / [DOI](https://doi.org/10.1007/s00383-026-06422-6)
  - Abstract: BACKGROUND/OBJECTIVES: Acute appendicitis often requires emergency surgery and leads to prolonged length of hospital stay (LOS). Enhanced recovery after surgery (ERAS) protocol promotes rapid recovery and shorter hospital stays, revolutionizing the management of pediatric surgery. The aim of the stu…
- **Nutritional Status as a Risk Factor for Appendiceal Perforation in Pediatric Acute Appendicitis: Systematic Review.** — Borca CI, Ivan CS, Fira-Mladinescu C et al. *Children (Basel)* (2026). PMID [41897039](https://pubmed.ncbi.nlm.nih.gov/41897039/) / [DOI](https://doi.org/10.3390/children13030326)
  - Abstract: The association between nutritional status and perforation or complicated appendicitis in children remains uncertain. To review evidence on anthropometric and biochemical nutritional indicators in relation to perforation and complicated appendicitis in pediatric acute appendicitis. PubMed, Scopus, a…
- **Idiopathic Encapsulating Peritoneal Sclerosis Mimicking Acute Appendicitis: A Case Report and Systematic Literature Review.** — Martzivanou EC, Atmatzidis S, Voloudakis N et al. *Am J Case Rep* (2026). PMID [41894320](https://pubmed.ncbi.nlm.nih.gov/41894320/) / [DOI](https://doi.org/10.12659/ajcr.951103)
  - Abstract: BACKGROUND Encapsulating peritoneal sclerosis (EPS), also known as abdominal cocoon syndrome (ACS), is a rare pathological entity that is difficult to diagnose. The syndrome can be idiopathic or secondary, and is mainly associated with peritoneal dialysis or abdominal tuberculosis. Patients with EPS…
- **The Cost-Effectiveness of Conservatively Managed Acute Appendicitis Versus Appendicectomy: A Systematic Review.** — Farhad I, Khan MA, Kler A et al. *Surg Laparosc Endosc Percutan Tech* (2026). PMID [41880556](https://pubmed.ncbi.nlm.nih.gov/41880556/) / [DOI](https://doi.org/10.1097/sle.0000000000001454)
  - Abstract: Appendicectomy remains the gold standard treatment for acute appendicitis. While there is continued debate as to the clinical benefit of conservative treatment in acute appendicitis, the cost-effectiveness of each treatment is a critical consideration. The aim of this study is to evaluate the curren…
- **Artificial intelligence for acute appendicitis diagnosis: A systematic review of current evidence, challenges, and future directions.** — Ismayilzada K *Medicine (Baltimore)* (2026). PMID [41861187](https://pubmed.ncbi.nlm.nih.gov/41861187/) / [DOI](https://doi.org/10.1097/md.0000000000048094)
  - Abstract: Acute appendicitis remains one of the most common surgical emergencies, yet its diagnosis continues to pose challenges due to overlapping clinical presentations and variable imaging findings. Artificial intelligence (AI) has recently emerged as a promising tool to enhance diagnostic accuracy, assist…
- **Diagnostic Accuracy of Point-of-Care Ultrasound (POCUS) for Suspected Acute Appendicitis in Pediatric and Adult Emergency Departments: A Systematic Review and Meta-Analysis.** — Kamal MM, Al Reshidi BM, Bedier HM et al. *Cureus* (2026). PMID [41841098](https://pubmed.ncbi.nlm.nih.gov/41841098/) / [DOI](https://doi.org/10.7759/cureus.103503)
  - Abstract: Acute appendicitis is a common surgical emergency that often requires diagnostic imaging. While computed tomography (CT) is highly accurate, it involves ionizing radiation and potential delays. Point-of-care ultrasound (POCUS), performed by emergency physicians, offers a rapid, radiation-free altern…
<!-- LN:LOG:END -->
