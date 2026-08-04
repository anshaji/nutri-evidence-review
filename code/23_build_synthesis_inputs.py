#!/usr/bin/env python3
"""Build per-intervention synthesis bundles (Stage 4 prep, full-corpus).

For each intervention category discovered by the extraction (Stage 3.6), bundle:
  - all its validated evidence records (from data/evidence_db.json),
  - the matching Phase-2 CEA record (from data/cea_by_intervention.json), matched
    via an explicit shortlist-name → category map,
  - the `cea_rating_allowed` gate (false when no CEA record exists),
  - full-text card paths for its strongest papers (so the synthesis agent can
    Read exact effect sizes / trace dominant trials).

Writes one bundle per category to data/synthesis_inputs/{category}.json plus an
index. Categories present in the extraction but NOT in the original 15-item
shortlist are surfaced here — that is the full-corpus "re-shortlist" delta.

Usage: python3 code/23_build_synthesis_inputs.py [min_papers]
"""

import json
import os
import re
import sys

OUTPUT_DIR = "./data"
EVI_DB = os.path.join(OUTPUT_DIR, "evidence_db.json")
ROLLUP = os.path.join(OUTPUT_DIR, "evidence_by_intervention.json")
CEA = os.path.join(OUTPUT_DIR, "cea_by_intervention.json")
INPUT_CARD_DIR = os.path.join(OUTPUT_DIR, "extraction_inputs")
OUT_DIR = os.path.join(OUTPUT_DIR, "synthesis_inputs")

# shortlist intervention name → extraction category tag
NAME_TO_CAT = {
    "vitamin a supplementation in children": "vitamin_a",
    "zinc supplementation in children": "zinc",
    "micronutrient powders for home fortification": "mnp",
    "small-quantity lipid-based nutrient supplements": "sq_lns",
    "iron supplementation in children": "iron_children",
    "antenatal multiple micronutrient supplementation": "anc_mmn",
    "antenatal iron-folic acid supplementation": "ifa_antenatal",
    "periconception folic acid supplementation": "folic_acid_periconception",
    "balanced energy-protein supplementation in pregnancy": "bep_pregnancy",
    "large-scale food fortification of staple foods": "food_fortification",
    "complementary feeding interventions": "complementary_feeding",
    "breastfeeding promotion and support": "breastfeeding",
    "community-based management of acute malnutrition": "cmam_sam_mam",
    "water sanitation and hygiene interventions for child nutrition": "wash",
    "cash transfers for child nutrition": "cash_transfers",
}


def _load(path, default):
    return json.load(open(path)) if os.path.isfile(path) else default


def main():
    min_papers = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    os.makedirs(OUT_DIR, exist_ok=True)

    records = _load(EVI_DB, [])
    by_key = {r["key"]: r for r in records}
    rollup = _load(ROLLUP, {}).get("groups", [])

    cea_data = _load(CEA, {})
    cea_list = cea_data.get("interventions", cea_data) if isinstance(cea_data, dict) else cea_data
    cat_to_cea = {}
    for c in (cea_list or []):
        name = (c.get("name") or c.get("intervention") or "").strip().lower()
        cat = NAME_TO_CAT.get(name)
        if cat:
            cat_to_cea[cat] = c

    index, built = [], 0
    for g in rollup:
        cat = g["intervention_category"]
        recs = [by_key[k] for k in g.get("top_keys", []) if k in by_key]
        # include ALL records for the category, not just top_keys
        allrecs = [r for r in records
                   if r.get("on_topic", True)
                   and (r.get("intervention_category") or "other") == cat]
        in_shortlist = cat in NAME_TO_CAT.values()
        if len(allrecs) < min_papers and not in_shortlist:
            index.append({"category": cat, "n_papers": len(allrecs),
                          "synthesized": False, "reason": "below threshold"})
            continue

        cea_rec = cat_to_cea.get(cat)
        cea_rating_allowed = bool(cea_rec and (
            cea_rec.get("cea_rating_allowed") or cea_rec.get("num_cea_papers", 0) > 0))

        # strongest-first card paths (meta-analyses/SR first)
        tier_order = {"meta_analysis": 0, "systematic_review": 1, "rct": 2}
        strong = sorted(allrecs, key=lambda r: (
            tier_order.get(r.get("evidence_tier", ""), 9), -(r.get("year") or 0)))
        card_paths = [os.path.join(INPUT_CARD_DIR, r["key"] + ".json")
                      for r in strong[:25]]

        bundle = {
            "category": cat,
            "in_original_shortlist": in_shortlist,
            "n_papers": len(allrecs),
            "tiers": g.get("tiers", {}),
            "populations": g.get("populations", {}),
            "labels": g.get("labels", []),
            "cea_rating_allowed": cea_rating_allowed,
            "cea_record": cea_rec,
            "strong_card_paths": card_paths,
            "records": allrecs,
        }
        with open(os.path.join(OUT_DIR, cat.replace(":", "_") + ".json"), "w",
                  encoding="utf-8") as f:
            json.dump(bundle, f, ensure_ascii=False, indent=2)
        built += 1
        index.append({"category": cat, "n_papers": len(allrecs),
                      "in_original_shortlist": in_shortlist,
                      "cea_rating_allowed": cea_rating_allowed,
                      "synthesized": True})

    index.sort(key=lambda x: (not x.get("synthesized"), -x["n_papers"]))
    with open(os.path.join(OUT_DIR, "index.json"), "w", encoding="utf-8") as f:
        json.dump({"n_synthesized": built, "categories": index}, f,
                  ensure_ascii=False, indent=2)

    new_cats = [x for x in index if x.get("synthesized") and not x.get("in_original_shortlist")]
    print(f"Synthesis bundles built: {built}")
    print(f"  → data/synthesis_inputs/*.json")
    print(f"\nCategories NOT in the original 15-item shortlist (full-corpus delta):")
    for x in new_cats:
        print(f"  + {x['category']:<32s} n={x['n_papers']}  cea_allowed={x['cea_rating_allowed']}")
    dropped = [x for x in index if not x.get("synthesized")]
    if dropped:
        print(f"\nBelow-threshold categories (noted, not full sections): "
              f"{[x['category'] for x in dropped]}")


if __name__ == "__main__":
    main()
