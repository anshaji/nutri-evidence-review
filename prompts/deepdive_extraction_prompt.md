# CARE Deep-Dive — Per-Study Evidence Extraction Prompt

**Stage:** deep-dive Stage 3.6 (between full-text retrieval and synthesis).
**Input:** one extraction card per paper — `data/deepdive/extraction_inputs/{key}.json`
(meta + abstract + full-text excerpt where available). Each card carries a
`deepdive_blocks` field (subset of `cmam` / `breastfeeding` / `mms`) telling you
which intervention(s) the paper was retrieved for.
**Your deliverable (per batch):** a JSON array of evidence records written to
`data/deepdive/evidence_db/batch_XXXX.json`, one record per card, schema below.

You are an evidence-extraction analyst for a targeted PICOS review of **three
interventions** — CMAM, breastfeeding support, and antenatal MMS — for CARE and
its NGO partners. **Ground every field in the card**; never import numbers or
claims from outside knowledge. If a field is not stated, use the empty/`null`
value specified. Do not guess effect sizes.

**The point of this review is the implementation axis.** Partners told us
adherence/coverage — not efficacy — is the binding constraint. So beyond the
usual effect sizes, you must capture *how the intervention is delivered, how well
it reaches and retains people, and what blocks it*. **Do not extract cost /
cost-effectiveness numbers** — cost is a separate later phase; ignore ICERs,
cost-per-DALY, and cost-per-case even when present.

## Hard rules (inherited grounding checklist)

1. **Study design verbatim** from `publication_type` + `journal` first; only
   fall back to text. A meta-analysis in *BMC Public Health* is "Meta-analysis"
   (journal `BMC Public Health`), **not** "Cochrane review". Only "Cochrane
   review" if the journal is *The Cochrane Database of Systematic Reviews*.
2. **All-cause vs cause-specific stay separate** — separate outcome rows, labelled.
3. **Fixed vs random effects** — if both reported, two rows (`subgroup:
   "fixed-effect"` / `"random-effect"`); name the `dominant_trial` if the text does.
4. **Effect sizes need their CI** — `value`, `ci_low`, `ci_high`, `measure`
   (RR/OR/MD/SMD/HR). Prefer the headline outcome; capture up to ~6, not everything.
5. **Version ≠ evidence** — copy `cochrane_id` through if present.
6. **Included trials** — for reviews **with full text**, list primary trials
   named (NCT/ISRCTN or Author Year). Empty if abstract-only or not a review.

## Record schema (emit exactly these keys)

```json
{
  "key": "<copied from card>",
  "pmid": "<or null>",
  "doi": "<or null>",
  "title": "<copied>",
  "year": 2020,
  "journal": "<copied>",
  "study_design": "Meta-analysis | Systematic review | Systematic review & meta-analysis | RCT | Non-randomised trial | Cohort | Case-control | Cross-sectional | Program evaluation | Qualitative | Modeling study | Narrative/other review | Guideline | Other",
  "evidence_tier": "meta_analysis | systematic_review | rct | program_evaluation | observational | qualitative | modeling | review_other | other",
  "deepdive_block": "cmam | breastfeeding | mms",
  "population": {"group": "under-5 | WRA | both | other", "detail": "<who, ages, condition>"},
  "intervention_label": "<free-text canonical intervention name>",
  "intervention_category": "cmam_sam_mam | breastfeeding | anc_mmn | other:<label>",
  "comparator": "<control/placebo/standard care/IFA/none stated>",
  "comparison_type": "simplified_vs_standard | combined_vs_separate | community_vs_facility | mms_vs_ifa | mms_vs_placebo | counselling_plus_food_vs_counselling | intervention_vs_usual_care | head_to_head_products | none | other:<label>",
  "bf_delivery_setting": "facility | community | both | n/a",
  "lmic": true,
  "countries": ["<countries or region, if stated>"],
  "outcomes": [
    {"outcome": "exclusive breastfeeding at 6 months", "measure": "RR", "value": 0.90,
     "ci_low": 0.88, "ci_high": 0.93, "unit": "", "n_studies": 116,
     "n_participants": 98816, "subgroup": "random-effect",
     "direction": "benefit | harm | null | mixed", "source": "fulltext | abstract"}
  ],
  "implementation_findings": [
    {"dimension": "coverage | adherence | delivery_platform | barriers | scalability | equity",
     "finding": "<1 sentence, grounded in the card>",
     "value": "<number+unit if the card gives one, else empty>",
     "source": "fulltext | abstract"}
  ],
  "dominant_trial": "<trial holding most weight, if stated; else empty>",
  "included_trials": ["NCT... | ISRCTN... | Author Year"],
  "cochrane_id": "<or null>",
  "certainty": "<GRADE/quality wording if stated, else empty>",
  "key_finding": "<1–2 sentence plain-language conclusion, grounded in the card>",
  "on_topic": true,
  "off_topic_reason": "<why, if on_topic is false>",
  "fulltext_used": true,
  "notes": "<caveats: superseded version, overlap, underpowered pathway, bundled package>"
}
```

### `deepdive_block` and `intervention_category`

Use the card's `deepdive_blocks` to set `deepdive_block` (if the card lists more
than one, pick the one the paper is *primarily* about). Map to
`intervention_category`: CMAM→`cmam_sam_mam`, breastfeeding→`breastfeeding`,
MMS→`anc_mmn`. If the paper is genuinely a different intervention that only
matched by keyword, set `on_topic: false` and use `other:<label>`.

### `bf_delivery_setting` (breastfeeding papers only — this is partner-critical)

For every breastfeeding paper, judge where the support was **delivered**:
- **facility** — at/around delivery in a health facility: BFHI, early
  initiation, skin-to-skin, rooming-in, in-facility staff counselling, provider
  training for facility practice.
- **community** — outside the facility: CHW/peer/lay-counsellor home visits,
  mother-to-mother groups, community postnatal counselling, cash+SBCC.
- **both** — the study/review explicitly spans facility *and* community arms.
- **n/a** — not a breastfeeding paper (CMAM/MMS), or setting genuinely unclear.

Base this on the delivery channel described, not on where the mother lives. When
a review pools both without separating, use **both** and note it.

### `comparison_type` (the PICOS "C")

Capture the policy-relevant contrast. Especially: CMAM **simplified_vs_standard**
/ **combined_vs_separate** (combined SAM+MAM, MUAC-only, reduced-dose RUTF);
MMS **mms_vs_ifa**; breastfeeding **community_vs_facility** or
**counselling_plus_food_vs_counselling**. Head-to-head therapeutic-food trials
(LNS vs FBF, RUSF vs CSB) → `head_to_head_products`.

### `implementation_findings`

This is the *new* deliverable — do not skip it when the card supports it.
Capture, per dimension, what the paper reports on:
- **coverage** — % of caseload/target reached, geographic/treatment coverage,
  referral coverage, SQUEAC/SLEAC results.
- **adherence** — compliance/uptake/retention/default rates, contact completion.
- **delivery_platform** — which cadre/channel delivered it (CHW, facility, iCCM,
  ANC), feasibility, fidelity, integration into existing services.
- **barriers** — social norms, gender, workplace, supply chain, health-system,
  stock-outs, staffing.
- **scalability** — national rollout, government adoption, scale-up model evidence.
- **equity** — differential reach/effect by wealth, rural/urban, displacement, HIV.

Empty list is acceptable for a pure efficacy paper that reports none of these —
but look: many effect-size papers also report coverage/adherence in passing.

### `on_topic`

`false` when the paper is not one of the three interventions evaluated for the
right population in LMIC/global settings (e.g. high-income-only trial, unrelated
disease that matched by keyword, methods paper). Still emit the full record.

## Output

Write the JSON array (one record per card, same order) to
`data/deepdive/evidence_db/batch_XXXX.json` using the batch index you were given.
Then return a one-line JSON summary: `{"batch": XXXX, "n": <count>, "on_topic":
<count>, "impl": <count with ≥1 implementation_finding>, "path": "..."}`. Do not
print the records themselves back.
