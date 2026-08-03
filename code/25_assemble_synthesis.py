#!/usr/bin/env python3
"""Assemble the final tiered synthesis document from per-intervention sections.

Inputs:
  - data/synthesis_ratings.json  — list of per-intervention rating dicts returned
    by the synthesis workflow (category, display_name, population, evidence_grade,
    cost_effectiveness, scalability, tier, one_line, headline_effect, key_ids,
    section_path).
  - data/synthesis_sections/{category}.md — the section bodies.
  - data/synthesis_inputs/index.json — for the re-shortlist delta + below-threshold list.
  - data/cross_cutting.md (optional) — cross-cutting findings written in-conversation.

Output: output/FULL_INTERVENTION_SYNTH_FULLCORPUS.md

Usage: python3 code/25_assemble_synthesis.py
"""

import json
import os

OUTPUT_DIR = "./data"
SECTIONS = os.path.join(OUTPUT_DIR, "synthesis_sections")
RATINGS = os.path.join(OUTPUT_DIR, "synthesis_ratings.json")
INDEX = os.path.join(OUTPUT_DIR, "synthesis_inputs", "index.json")
CROSS = os.path.join(OUTPUT_DIR, "cross_cutting.md")
OUT = "./output/FULL_INTERVENTION_SYNTH_FULLCORPUS.md"

GRADE_ORDER = {"A": 0, "B": 1, "C": 2}
CE_SHORT = {"Very High": "Very High", "High": "High", "Moderate": "Moderate", "Unknown": "Unknown"}


def _load(p, d):
    return json.load(open(p)) if os.path.isfile(p) else d


def main():
    ratings = _load(RATINGS, [])
    idx = _load(INDEX, {})

    # de-dup by category (keep last), attach paper counts from the index
    cat_n = {c["category"]: c.get("n_papers", 0) for c in idx.get("categories", [])}
    by_cat = {}
    for r in ratings:
        by_cat[r["category"]] = r
    items = list(by_cat.values())
    for it in items:
        it["n_papers"] = cat_n.get(it["category"], 0)

    # order: tier, then evidence grade, then paper count desc
    items.sort(key=lambda r: (r.get("tier", 9),
                              GRADE_ORDER.get(r.get("evidence_grade", "C"), 3),
                              -r.get("n_papers", 0)))

    lines = []
    lines.append("# Nutrition Intervention Synthesis — Full-Corpus Run")
    lines.append("")
    lines.append("*Children under 5 and women of reproductive age (WRA) in LMICs. "
                 "Interventions rated on evidence strength, cost-effectiveness, and "
                 "scalability, and tiered accordingly.*")
    lines.append("")

    # ── methodology note ─────────────────────────────────────────────────────
    n_syn = len(items)
    lines.append("## How this was produced")
    lines.append("")
    lines.append(
        "This synthesis scales the pipeline beyond the original top-200 review to a "
        "**1,000-paper working set** drawn from the full corpus of 1,996 retrieved "
        "papers. Pipeline: (1) retrieve evidence (PubMed + OpenAlex, population-"
        "targeted); (2) **full-text retrieval for the whole corpus** — 1,378/1,996 "
        "(69%) via PMC (PMID *and* DOI→PMCID) with an Unpaywall→PDF fallback; "
        "(3) **per-study structured extraction** into an evidence database "
        "(study design, population, effect sizes with CIs, included trials, dominant "
        "trial, Cochrane accession) via a fan-out of extraction agents; (4) cap to a "
        "**1,000-paper set selected independently of the relevance ranking** (592 "
        "already-extracted + 408 uniformly random, seed 20260709); (5) **per-"
        "intervention synthesis** grounded in the extraction DB + Phase-2 CEA, one "
        "agent per intervention, under the standing grounding rules (corpus citation "
        "on every number, verbatim study type, all-cause vs cause-specific split, "
        "fixed/random + dominant trial, version≠evidence, CEA-rating guard); "
        "(6) automated claim verification.")
    lines.append("")
    lines.append(f"**{n_syn} interventions** met the evidence threshold for a full "
                 "section. Cost-effectiveness is rated **only** where a Phase-2 CEA "
                 "record exists (`cea_rating_allowed`), else **Unknown**.")
    lines.append("")

    # ── summary table ────────────────────────────────────────────────────────
    lines.append("## Summary table")
    lines.append("")
    lines.append("| Tier | Intervention | Population | Evidence | Cost-effectiveness | Scalability | Papers |")
    lines.append("|------|--------------|-----------|:--------:|:-----------------:|-------------|:------:|")
    for it in items:
        lines.append(
            f"| {it.get('tier','?')} | {it.get('display_name', it['category'])} "
            f"| {it.get('population','')} | {it.get('evidence_grade','')} "
            f"| {CE_SHORT.get(it.get('cost_effectiveness',''), it.get('cost_effectiveness',''))} "
            f"| {it.get('scalability','')} | {it.get('n_papers','')} |")
    lines.append("")

    # ── tiered sections ──────────────────────────────────────────────────────
    tier_titles = {
        1: "Tier 1 — Strong evidence, cost-effective, scalable now",
        2: "Tier 2 — Strong or mixed evidence, scalable with investment",
        3: "Tier 3 — Promising or indirect, plausible pathway",
    }
    cur_tier = None
    for it in items:
        t = it.get("tier", 3)
        if t != cur_tier:
            cur_tier = t
            lines.append("")
            lines.append(f"# {tier_titles.get(t, f'Tier {t}')}")
            lines.append("")
        sec_path = it.get("section_path") or os.path.join(SECTIONS, it["category"] + ".md")
        if os.path.isfile(sec_path):
            lines.append(open(sec_path, encoding="utf-8").read().rstrip())
        else:
            lines.append(f"## {it.get('display_name', it['category'])}\n*(section file missing)*")
        lines.append("")

    # ── cross-cutting findings (written in-conversation) ─────────────────────
    if os.path.isfile(CROSS):
        lines.append("")
        lines.append(open(CROSS, encoding="utf-8").read().rstrip())
        lines.append("")

    # ── re-shortlist delta ───────────────────────────────────────────────────
    new_cats = [c for c in idx.get("categories", [])
                if c.get("synthesized") and not c.get("in_original_shortlist")]
    below = [c["category"] for c in idx.get("categories", []) if not c.get("synthesized")]
    lines.append("")
    lines.append("# Appendix A — Full-corpus re-shortlist delta")
    lines.append("")
    lines.append("Interventions that earned a full section here but were **not** in the "
                 "original 15-item (top-200-derived) shortlist — i.e. surfaced only by "
                 "reading deeper into the corpus:")
    lines.append("")
    for c in new_cats:
        lines.append(f"- **{c['category']}** — {c['n_papers']} papers "
                     f"(cost-effectiveness {'ratable' if c.get('cea_rating_allowed') else 'Unknown — no CEA record'})")
    lines.append("")
    lines.append(f"A further {len(below)} categories appeared below the "
                 "evidence threshold (mostly observational determinant/surveillance "
                 "studies and health-systems topics rather than discrete nutrition "
                 "interventions); they are recorded in the evidence database but not "
                 "given sections.")
    lines.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Assembled {n_syn} interventions → {OUT}")
    tiers = {}
    for it in items:
        tiers[it.get("tier", "?")] = tiers.get(it.get("tier", "?"), 0) + 1
    print(f"  tiers: {dict(sorted(tiers.items()))}")


if __name__ == "__main__":
    main()
