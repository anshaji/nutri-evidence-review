---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Palatino', 'Georgia', serif;
    color: #1a1a2e;
    background: #fafafa;
    padding: 40px 60px;
  }
  section.title {
    background: #0f1b2d;
    color: #ffffff;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  section.title h1 { color: #7ec8c8; font-size: 2.2em; margin-bottom: 0.1em; }
  section.title h2 { color: #cccccc; font-weight: normal; font-size: 1.1em; }
  section.title p { color: #8899aa; font-size: 0.75em; }
  section.dark {
    background: #0f1b2d;
    color: #e0e0e0;
  }
  section.dark h1, section.dark h2 { color: #7ec8c8; }
  section.dark table th { background: #1a3a5c; color: #ffffff; }
  section.dark table td { background: #152238; color: #e0e0e0; border-color: #2a3a54; }
  h1 { color: #1b365d; font-size: 1.5em; border-bottom: 2px solid #0e7c7b; padding-bottom: 8px; }
  h2 { color: #2e5c8a; font-size: 1.15em; }
  h3 { color: #0e7c7b; font-size: 1.0em; }
  table { font-size: 0.65em; border-collapse: collapse; margin: 0.3em 0; }
  th { background: #1b365d; color: white; padding: 6px 10px; text-align: left; }
  td { padding: 5px 10px; border: 1px solid #ddd; }
  tr:nth-child(even) td { background: #edf2f7; }
  .footnote { font-size: 0.55em; color: #5a6c7d; font-style: italic; margin-top: 0.5em; }
  strong { color: #1b365d; }
  em { color: #5a6c7d; }
  img { max-width: 100%; }
---

<!-- _class: title -->

# Nutrition Interventions in LMICs
## Automated Evidence Synthesis & Prioritization

**100** papers reviewed · **57** with PMC full text · **24** interventions ranked · **3** evidence tiers

Pipeline v2.0 — PubMed + OpenAlex systematic search — May 2026

---

# Automated Evidence Synthesis Pipeline

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│   STAGE 1            │     │   STAGE 2            │     │   STAGE 3.5          │     │   STAGE 4            │
│   Retrieval          │     │   Scoring            │     │   Full-Text          │     │   LLM Review         │
│                      │     │                      │     │                      │     │                      │
│ • PubMed: 12 domains │────▶│ • 3-phase dedup      │────▶│ • PMID → PMCID       │────▶│ • Batched review     │
│   × 2 passes (MA+SR) │     │   (PMID, OA ID, DOI) │     │   conversion         │     │   (top 40, then      │
│ • OpenAlex: 4 econ/  │     │ • 7-component score  │     │ • PMC XML fetch +    │     │    41–100)           │
│   development queries │     │   (0–85 points)      │     │   structured parsing │     │ • Effect sizes with  │
│ • Track B: CEA       │     │ • MeSH + pub. type   │     │ • Results, tables,   │     │   confidence intervals│
│                      │     │   based ranking       │     │   subgroup data      │     │ • Tier assignment    │
│   ~3,900 papers      │     │   2,700 ranked        │     │   57/100 full text   │     │   24 interventions   │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘     └─────────────────────┘
```

**Scoring Components** *(max 85 pts)*: Study Design (0–20) · Topic Relevance (0–25) · Setting (0–10) · Recency (0–10) · Citation Impact (0–12) · Open Access (0–3) · Tier Bonus (0–5)

---

# Evidence Prioritization Framework

**Figure 1.** Twenty-four nutrition interventions positioned by evidence strength & effect size (x-axis) against implementation readiness — a composite of cost-effectiveness and proven scalability (y-axis). Dashed lines delineate four action quadrants. Dot colour indicates evidence tier.

```
    Implementation Readiness ↑
    (cost-effectiveness + scalability)

    High ┤                           ● Fortification (A)
         │  ○ CCTs (B)               ● VAS (A)     ● IFA (A)
         │  ○ Nutrition ed. (B+)     ● MMS (A)
         │  ○ IMCI (B)              ● Breastfeeding (A)
         │  ○ Iron school (B+)      ● Zinc ther. (A)
         │  ○ Calcium (B)
         │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
         │                           ◆ MNP (A)
         │                           ◆ Comp. feeding (A)
         │  ◇ WASH (B)              ◆ LNS (A)    ◆ CMAM (A)
         │  ◇ Protein-energy (B)    ◆ Prenatal LNS (B+)
         │  ◇ Vitamin D (C+)        ◆ Zinc prev. (A)
         │  ◇ Agricultural (C)      ◆ MAM mgmt (B+)
    Low  ┤  ◇ GMP (C)  ◇ Egg (C+)
         └────────────────────┤──────────────────────────────▶
              Low                                    High
                    Evidence Strength & Effect Size

    Legend:  ● Quadrant I  — Scale Now (Evidence A, high readiness)
             ○ Quadrant II — Monitor & Evaluate (B/B+, good platforms)
             ◇ Quadrant III— Research Priority (C/C+, insufficient)
             ◆ Quadrant IV — Invest to Scale (A, needs infrastructure)
```

*See HTML version (evidence_review_slides.html) for the full SVG scatter-plot rendering.*

---

# Evidence Prioritization Framework — Axis Definitions

### Axis Composition

| Axis | Composite of | High | Low |
|------|-------------|------|-----|
| **Evidence Strength & Effect Size** (x) | GRADE certainty, # Cochrane reviews, pooled effect magnitude, cross-population consistency | ≥2 meta-analyses, GRADE mod.–high, consistent direction | ≤1 meta-analysis, GRADE low–very low, inconsistent |
| **Implementation Readiness** (y) | Cost-effectiveness, delivery platform maturity, # countries with national programmes | <$500 per healthy year gained, proven national in ≥3 LMICs | >$1,500 per healthy year gained or no large-scale evidence |

### Quadrant Decision Rules

| Quadrant | Action | Criteria |
|----------|--------|----------|
| **I. Scale Now** (●) | Immediate government-led expansion | Evidence A + Proven national + High cost-effectiveness |
| **II. Monitor & Evaluate** (○) | Continue with robust M&E | Delivery platforms exist, evidence moderate (B/B+) |
| **III. Research Priority** (◇) | Prioritize for research funding | Emerging evidence (C/C+), insufficient for policy |
| **IV. Invest to Scale** (◆) | Infrastructure investment needed | Evidence A but higher cost or subnational only |

<div class="footnote">

Cost-effectiveness thresholds adapted from WHO-CHOICE and Disease Control Priorities (DCP3). "Healthy year gained" = one year of full health gained through the intervention — equivalent to one disability-adjusted life year (DALY) averted.

</div>

---

# Children Under 5 — Intervention Prioritization

**Figure 2.** Child nutrition interventions (6–59 months) positioned by effect size on primary outcome (x-axis) against annual cost per child (y-axis, inverted — lower cost = higher). All shown carry Evidence Rating A. Dot size ∝ evidence base breadth.

```
    Cost-Effectiveness ↑
    (lower cost = higher)

  <$5/yr ┤  ● Zinc prev.           ● Zinc ther.
         │     RR 0.87                RR 0.73 at day 7
         │     $1-2/yr                $0.50/course
         │                          ● VAS
         │  ● MNP                     RR 0.88 mortality
         │     RR 0.82 anaemia        $1-3/yr
         │     $3.60/yr
         │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
         │  ● Comp. feeding
 $50+/yr │     SMD 0.22 HAZ
         │
         │  ◆ LNS (6-23 mo)
         │     RR 0.93 stunting       ◆ CMAM / RUTF
         │     $50-60/yr                RR 0.52 SAM mortality
  $200+  ┤                              $200/child
         └────────────────────┤──────────────────────────────▶
              Moderate                               Large
                    Effect Size (Mortality / Morbidity Reduction)
```

| Intervention | Key Effect | 95% CI | Cost | Source |
|---|---|---|---|---|
| VAS (6–59 mo) | RR 0.88 mortality | 0.83–0.93 | $1–3/yr | PMID 35294044 |
| Zinc (therapeutic) | RR 0.73 at day 7 | 0.61–0.88 | $0.50/course | PMID 27996088 |
| MNP | RR 0.82 anaemia | 0.76–0.90 | $3.60/yr | PMID 32107773 |
| Zinc (preventive) | RR 0.87 diarrhoea | 0.85–0.89 | $1–2/yr | PMID 24826920 |
| LNS (6–23 mo) | RR 0.93 stunting | 0.88–0.98 | $50–60/yr | PMID 31046132 |
| CMAM / RUTF | RR 0.52 mortality | 0.43–0.64 | $200/child | PMID 24564235 |

---

# Pregnant Women — Intervention Prioritization

**Figure 3.** Maternal nutrition interventions positioned by effect size (x-axis) against cost per pregnancy (y-axis, inverted). Dot colour = evidence rating.

```
    Cost-Effectiveness ↑

   <$2  ┤                           ● IFA (A)
        │                              RR 0.52 anaemia
        │  ○ Nutrition ed. (B+)        $0.50-2/pregnancy
        │     OR 2.80 compliance
   <$5  ┤                           ● MMS (A)
        │                              RR 0.88 LBW
        │  ○ Calcium (B)              $1.50-3.50
        │     RR 0.30 pre-eclampsia
        │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
        │                           ◆ Prenatal LNS (B+)
        │  ◇ Protein-energy (B)       +49g birthweight
        │     SMD 0.20 BW
        │
        │  ◇ Vitamin D (C+)
  $10+  ┤     Limited LMIC data
        └────────────────────┤──────────────────────────────▶
              Moderate                               Large
                    Effect Size (LBW / Anaemia Reduction)

    Legend:  ● Evidence A   ○ Evidence B/B+   ◇ Evidence C/C+   ◆ Invest to scale
```

**Key policy insight:** MMS costs only $1–2 more than IFA per pregnancy but prevents **12% more LBW births**. WHO conditionally recommended MMS transition in 2020. Compliance is the primary bottleneck — nutrition education **triples adherence** (OR 2.80).

---

# Population-Level Interventions — Evidence vs. Reach

**Figure 4.** Population-level and nutrition-sensitive interventions positioned by evidence strength (x-axis) against implementation coverage (y-axis). Dot size ∝ number of countries with programmes.

```
    Coverage ↑

  National ┤               ○ CCTs (B)     ● Fortification (A)
  (≥3 LMICs)                HAZ +0.20       >120 countries
           │               ○ IMCI (B)     ● Breastfeeding (A)
           │                >100 countries   >150 BFHI countries
           │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  Subnational│
           │  ◇ WASH (B)
           │     HAZ SMD 0.14
           │     borderline
           │
  Pilot    ┤  ◇ Agricultural (C)
           │     No anthropometric effect
           └────────────────────┤──────────────────────────────▶
                Low (C)                                High (A)
                           Evidence Strength

    Legend:  ● Evidence A   ○ Evidence B/B+   ◇ Evidence C/C+
```

**Cross-cutting:** 76% of studies combining multisectoral policies with nutritional supplementation successfully reduced stunting vs. variable results for single-sector approaches.

**The Anaemia Paradox:** Iron deficiency explains only **25%** of anaemia in preschool children — far below the assumed 50%. Inflammation, malaria, and helminth infections must be addressed concurrently.

---

# Interventions by Delivery Platform & Evidence Tier

**Table 5.** All 24 interventions classified by delivery mechanism and evidence strength. Community-based platforms concentrate the largest number of Evidence A interventions.

| Delivery Platform | Evidence A (Strong) | Evidence B/B+ (Moderate) | Evidence C/C+ (Emerging) |
|---|---|---|---|
| **Health Facility** *(ANC/Postnatal)* | Iron–folic acid · MMS · Zinc therapeutic | Calcium · Nutrition education · Iron (school-age) · Prenatal LNS | Vitamin D |
| **Community-Based** *(CHW Delivery)* | Vitamin A · MNP · CMAM · Comp. feeding · Breastfeeding · Zinc preventive | WASH · Community case mgmt · MAM management | Growth monitoring · Egg suppl. |
| **Food System** *(Fortification/Prod.)* | Large-scale fortification | — | Agricultural · Biofortification |
| **Cash / Social Protection** | — | CCTs · IMCI | — |

<div class="footnote">

6 of 10 Evidence A interventions are deliverable through CHW networks — the primary scaling vehicle for child nutrition in LMICs.

</div>

---

# Vitamin A Supplementation — What the Pipeline Did Well

The automated pipeline synthesized evidence across **3 Cochrane review generations** (2011, 2017, 2022), detecting temporal trends and population-specific signals that would typically require manual expert review.

| Capability | Finding | Data |
|---|---|---|
| **Temporal tracking** | Effect attenuation over time | RR 0.76 (2017) → RR 0.88 (2022); post-2000: RR 0.96 (NS) |
| **Subgroup detection** | Asia vs Africa differential | Asia RR 0.69 vs Africa RR 0.85 |
| **Age-specificity** | Neonatal VAS ≠ child VAS | Neonatal: RR 0.97 (NS); possible harm in Africa: RR 1.06 |
| **Adverse effects** | Safety signals flagged | Vomiting RR 1.97; bulging fontanelle <6 mo: RR 1.55 |
| **Effect size extraction** | CIs from full-text | 7 distinct pooled estimates across outcomes |
| **Policy nuance** | Declining absolute benefit | Nepal: only 3 fewer deaths per 1,000 children supplemented |
| **IPD meta-analysis** | Individual participant data | 11 trials, n=163,567 |

---

# Vitamin A Supplementation — Pipeline Limitations

These are **structural pipeline gaps**, not LLM reasoning failures. Addressing them requires architectural changes.

| Gap | Description | Consequence |
|---|---|---|
| **CEA blind spot** | Zero cost-effectiveness papers retrieved for VAS | "$1–3/child/yr" from LLM training data, not evidence |
| **External knowledge leak** | Cost figures injected from LLM priors | Cost-effectiveness confidence not calibrated to database |
| **Misattribution** | "823,000 deaths" cited from PMID 26869575 | That paper is the Lancet *Breastfeeding* Series, not VAS |
| **Statistical model tension** | RR 0.88 (fixed-effect) vs RR 0.76 (random-effects) | Divergence is methodological, not flagged as such |
| **Overlapping studies** | Same RCTs in multiple Cochrane reviews | Risk of double-counting primary trials |
| **Publication bias** | Cannot assess funnel plot asymmetry | May inflate effect estimates |
| **No alternatives** | Biofortification not compared | Food-based approaches not evaluated as substitutes |

**The CEA Blind Spot:** The search included a dedicated cost-effectiveness track but retrieved zero papers for VAS. All cost claims rely on LLM external knowledge.

**The Statistical Model Tension:** Fixed-effect assumes one true effect; random-effects allows heterogeneity. The true effect likely lies between RR 0.76 and 0.88 — the choice of model matters more than additional trials.

---

<!-- _class: dark -->

# Summary & Key Takeaways

### Pipeline Performance

**3,900** retrieved → **2,700** deduplicated → **100** reviewed → **57** full text → **24** interventions ranked

### Top 5 "Scale Now" Interventions

| # | Intervention | Key Effect (95% CI) | Cost | Evidence |
|---|---|---|---|---|
| 1 | Vitamin A suppl. (6–59 mo) | RR 0.88 all-cause mortality (0.83–0.93) | $1–3/child/yr | A — 3 Cochrane |
| 2 | Iron–folic acid (pregnancy) | RR 0.52 maternal anaemia (0.41–0.66) | $0.50–2/pregnancy | A |
| 3 | Multiple micronutrient suppl. | RR 0.88 low birthweight (0.85–0.91) | $1.50–3.50/pregnancy | A — Cochrane |
| 4 | Large-scale fortification | RR 0.66 anaemia (0.59–0.74) | $0.05–0.50/person/yr | A |
| 5 | Exclusive breastfeeding promo. | 823K under-5 deaths preventable/yr | Very low per beneficiary | A |

### Key Limitations

1. **No cost-effectiveness papers retrieved** despite dedicated search track — all cost ratings rely on LLM external knowledge
2. **43/100 papers abstract-only** — effect sizes not independently verified from full text for nearly half the evidence
3. **Geographic concentration** in South Asia and East/West Africa — Latin America, Central Asia, Pacific Islands underrepresented
