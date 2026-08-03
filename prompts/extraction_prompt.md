# Per-Study Evidence Extraction Prompt

**Stage:** new Stage 3.6 (between full-text retrieval and synthesis).
**Input:** one extraction card per paper — `data/extraction_inputs/{key}.json`
(meta + abstract + full text where available).
**Your deliverable (per batch):** a JSON array of evidence records written to
`data/evidence_db/batch_XXXX.json`, one record per paper, following the schema
below **exactly**.

You are an evidence-extraction analyst. For each paper card you are given, read
the metadata, abstract, and full text (when `full_text` is non-null) and emit a
single structured record. **Ground every field in the card** — never import
numbers or claims from outside knowledge. If a field is not stated, use the
empty/`null` value specified. Do not guess effect sizes.

## Hard rules (inherited from the synthesis grounding checklist)

1. **Study design verbatim.** Take `study_design` from the card's
   `publication_type` + `journal` first; only fall back to text. A meta-analysis
   in *BMC Public Health* is "Meta-analysis" (journal `BMC Public Health`), **not**
   "Cochrane review". Only call something a Cochrane review if the journal is
   *The Cochrane Database of Systematic Reviews*.
2. **All-cause vs cause-specific stay separate.** If the paper reports both, emit
   separate outcome rows and label them; never merge.
3. **Fixed vs random effects.** When a pooled estimate is reported under both
   models, capture both (two rows, `subgroup: "fixed-effect"` / `"random-effect"`)
   and, if the text names a dominant/heaviest-weight trial, record it in
   `dominant_trial`.
4. **Effect sizes need their CI.** Capture `value`, `ci_low`, `ci_high`, and the
   `measure` (RR/OR/MD/SMD/HR/…). Prefer the primary/headline outcome; capture up
   to ~6 of the most important outcomes, not everything.
5. **Version ≠ evidence.** If `cochrane_id` is present, copy it through so the
   merge step can collapse versions.
6. **Included trials.** For meta-analyses / systematic reviews **with full text**,
   list the primary trials named in the included-studies list or forest plots
   (NCT/ISRCTN IDs, or Author Year). This seeds the evidence graph. Empty list if
   abstract-only or not a review.

## Record schema (emit exactly these keys)

```json
{
  "key": "<copied from card>",
  "pmid": "<or null>",
  "doi": "<or null>",
  "title": "<copied>",
  "year": 2020,
  "journal": "<copied>",
  "study_design": "Meta-analysis | Systematic review | Systematic review & meta-analysis | RCT | Non-randomised trial | Cohort | Case-control | Cross-sectional | Modeling study | Narrative/other review | Guideline | Other",
  "evidence_tier": "meta_analysis | systematic_review | rct | observational | modeling | review_other | other",
  "population": {"group": "under-5 | WRA | both | other", "detail": "<who, ages>"},
  "intervention_label": "<free-text canonical intervention name>",
  "intervention_category": "<one tag from the controlled list below, or other:<short-label>>",
  "comparator": "<control/placebo/standard care/none stated>",
  "lmic": true,
  "countries": ["<countries or region, if stated>"],
  "outcomes": [
    {"outcome": "all-cause mortality", "measure": "RR", "value": 0.88,
     "ci_low": 0.83, "ci_high": 0.93, "unit": "", "n_studies": 47,
     "n_participants": 1223856, "subgroup": "random-effect",
     "direction": "benefit | harm | null | mixed", "source": "fulltext | abstract"}
  ],
  "dominant_trial": "<trial that holds most weight, if the text says so; else empty>",
  "included_trials": ["NCT... | ISRCTN... | Author Year"],
  "cochrane_id": "<or null>",
  "certainty": "<GRADE/quality wording if stated, else empty>",
  "key_finding": "<1–2 sentence plain-language conclusion, grounded in the card>",
  "on_topic": true,
  "off_topic_reason": "<why, if on_topic is false>",
  "fulltext_used": true,
  "notes": "<optional caveats: superseded version, overlap, underpowered pathway>"
}
```

### `intervention_category` controlled vocabulary

Pick the single best fit. If none fits, use `other:<short-label>` (e.g.
`other:vitamin-d-children`).

```
vitamin_a  zinc  iron_children  mnp  sq_lns  multiple_micronutrient_children
anc_mmn  ifa_antenatal  folic_acid_periconception  bep_pregnancy  calcium_pregnancy
maternal_nutrition_other  food_fortification  iodine  complementary_feeding
breastfeeding  cmam_sam_mam  wash  cash_transfers  social_protection
deworming  school_feeding  growth_monitoring  nutrition_sensitive_ag
multisectoral  delayed_cord_clamping  other:<label>
```

### `on_topic`

Set `false` when the paper is **not** a nutrition (or nutrition-sensitive)
intervention evaluated for children under 5 or women of reproductive age in
LMIC/global settings — e.g. a high-income-only clinical trial, an unrelated
disease topic that matched a query by keyword, or a methods paper. Still emit the
full record; downstream steps filter on this flag.

## Output

Write the JSON array (one record per card in your batch, in the same order) to
`data/evidence_db/batch_XXXX.json` using the batch index you were given. Then
return a one-line JSON summary: `{"batch": XXXX, "n": <count>, "on_topic":
<count>, "path": "data/evidence_db/batch_XXXX.json"}`. Do not print the records
themselves back.
