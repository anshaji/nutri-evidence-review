# Phase 1 → Intervention Shortlist Prompt

**Stage:** between Phase 1 (evidence) and Phase 2 (cost-effectiveness).
**Input:** `data/top_papers_for_review.json`
**Your single deliverable:** `data/shortlist.json`

You are an evidence-synthesis reviewer. You are handed the **top 200 ranked
papers** from a population-targeted literature search for nutrition
interventions in LMICs. Read across them, identify the distinct interventions
the evidence actually supports, and write the shortlist that drives the Phase 2
cost-effectiveness search.

> **Scope — do only this.**
> - ✅ Identify and shortlist evidence-backed interventions for **children under 5** and **women of reproductive age (WRA)**.
> - ❌ Do **not** rate cost-effectiveness — Phase 1 contains **no** CEA data.
> - ❌ Do **not** write the final synthesis — that is a later, separate step.

---

## Input: `data/top_papers_for_review.json`

A JSON array of up to 200 paper objects, already ranked by `relevance_score`
(descending). Read these fields per paper:

| Field | Use it to… |
|-------|------------|
| `title`, `abstract`, `fulltext` | understand what was studied (full text present when `fulltext_source == "pmc"`) |
| `mesh_terms[]`, `publication_type[]`, `journal` | **verify** the intervention, population, and study type — do not guess from the title |
| `study_type`, `tier` | weight evidence (meta-analysis > systematic review) |
| `pmid`, `publication_year`, `cited_by_count` | cite and date the evidence |
| `cochrane_id`, `superseded_by` | detect Cochrane review versions (see Rule 2) |
| `query_origin` | the domain that surfaced the paper (a hint, not a label) |

---

## Task

1. **Read across ALL papers.** Use `mesh_terms` + `journal` + `publication_type`
   to establish what each paper actually studies and in which population.
2. **Extract every distinct intervention**, then **GROUP variants under one
   heading** — e.g. preventive + therapeutic zinc → one *zinc supplementation*;
   SAM + MAM treatment → one *management of acute malnutrition*; salt iodization
   + flour fortification → one *large-scale food fortification*.
3. **Select the evidence-backed interventions** (see Rule 1). For each, gather
   its representative supporting PMIDs from the corpus.
4. For each selected intervention define: `name`, `synonyms`, `mesh`,
   `population`, and `_evidence` (the supporting PMIDs).
5. **Write `data/shortlist.json`** in the schema below.

---

## HARD rules

> **Rule 1 — Evidence-backed only.**
> Shortlist an intervention **only if it is supported by ≥ 2 meta-analyses /
> systematic reviews in this corpus.** Record those PMIDs in `_evidence`. An
> intervention resting on a single paper is **not** shortlisted (note it under
> "considered but excluded" in your message, not in the JSON).

> **Rule 2 — Version ≠ evidence.**
> Cochrane review updates sharing a `cochrane_id` (e.g. CD008524, 2017 & 2022)
> are the **same review**. The pipeline already collapsed superseded versions
> (`superseded_by`). Never count versions as independent evidence when judging
> "≥ 2 reviews".

> **Rule 3 — Study type is verbatim.**
> Judge evidence strength from the **`journal` + `publication_type`** fields, not
> the title. A review is "Cochrane" only if `journal` is *The Cochrane Database
> of Systematic Reviews*.

> **Rule 4 — Population fit.**
> Shortlist only interventions for **children under 5 or WRA** (pregnancy /
> lactation count as WRA). The corpus is pre-filtered, but drop any off-target
> paper that slipped in (e.g. school-age-only, adult-only).

> **Rule 5 — Distinct & non-overlapping.**
> Merge variants so two entries don't trigger near-identical Phase 2 searches.
> One intervention = one CEA question.

> **Rule 6 — Unambiguous synonyms.**
> `name` + `synonyms` feed Phase 2's **free-text OpenAlex** search. Avoid short
> ambiguous abbreviations (e.g. "VAS" also means *Visual Analog Scale*; "MMS"
> alone is weak) — prefer full phrases; add an abbreviation only alongside a
> disambiguating full term.

> **Rule 7 — Stay in corpus.**
> Every PMID in `_evidence` **must** be a paper present in
> `data/top_papers_for_review.json`. Do not add PMIDs from memory.

---

## Output: `data/shortlist.json`

Copy `data/shortlist.template.json` and fill it. Schema:

```json
{
  "generated_from": "data/top_papers_for_review.json",
  "review_date": "YYYY-MM-DD",
  "interventions": [
    {
      "name": "vitamin A supplementation in children",
      "synonyms": ["retinol supplementation", "vitamin A capsule", "neonatal vitamin A supplementation"],
      "mesh": ["Vitamin A", "Vitamin A Deficiency"],
      "population": "under-5",
      "_evidence": ["21868478", "35294044", "21501438"]
    }
  ]
}
```

Field contract (consumed by Phase 2 / `code/12_cea_client.py`):

- **`name`** *(required)* — the primary intervention phrase. Used in PubMed `[tiab]`, OpenAlex search, and registry matching.
- **`synonyms`** *(optional)* — additional `[tiab]` / free-text terms OR-ed into the search. Keep unambiguous (Rule 6).
- **`mesh`** *(optional)* — valid MeSH descriptors, OR-ed in on the PubMed side only.
- **`population`** — `"under-5"` or `"WRA"` (informational; Phase 2 does not re-filter by it).
- **`_evidence`** — supporting corpus PMIDs (Rule 1 / Rule 7). Traceability for the later synthesis.

---

## Before you finish — checklist

- [ ] Every shortlisted intervention has **≥ 2** corpus MA/SR PMIDs in `_evidence`.
- [ ] Variants are **merged**; no two entries pose the same CEA question.
- [ ] No Cochrane **version** double-counted toward the ≥ 2 threshold.
- [ ] Every intervention targets **under-5 or WRA**.
- [ ] Synonyms are **unambiguous** for free-text search.
- [ ] Every `_evidence` PMID exists in `data/top_papers_for_review.json`.
- [ ] You listed, in your message, the interventions you **considered but excluded** and why (too thin, off-population, duplicate).

Then: `cp data/shortlist.template.json data/shortlist.json`, write your shortlist
into it, and run Phase 2 with `python3 code/15_run_cea.py`.
