#!/usr/bin/env python3
"""Merge + validate per-batch extraction outputs into the evidence database.

Reads every data/evidence_db/batch_*.json produced by the extraction workflow,
validates each record, and writes:
  - data/evidence_db.json          — one flat, validated record per paper
  - data/evidence_by_intervention.json — rollup grouped by intervention_category
                                          (feeds the re-shortlist + synthesis)

Also reports which corpus papers are still MISSING a record (so the workflow can
be re-run for just those batches).

Usage: python3 code/22_merge_evidence_db.py
"""

import glob
import json
import os
import sys
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from code.fulltext_all import paper_key

OUTPUT_DIR = "./data"
DB_PATH = os.path.join(OUTPUT_DIR, "papers_database.json")
BATCH_GLOB = os.path.join(OUTPUT_DIR, "evidence_db", "batch_*.json")
MERGED_PATH = os.path.join(OUTPUT_DIR, "evidence_db.json")
ROLLUP_PATH = os.path.join(OUTPUT_DIR, "evidence_by_intervention.json")

REQUIRED = ["key", "study_design", "evidence_tier", "intervention_category",
            "on_topic", "outcomes", "key_finding"]
TIER_ORDER = {"meta_analysis": 0, "systematic_review": 1, "rct": 2,
              "observational": 3, "modeling": 4, "review_other": 5, "other": 6}


# Stray per-outcome annotation keys some extraction agents emitted; collapsed
# into the schema's single `note` field (schema/evidence_record.schema.json).
_OUTCOME_NOTE_KEYS = ("note", "notes", "note_inline", "notes_inline",
                      "note_range", "certainty_inline")


def _norm_record(r: dict) -> dict:
    r.setdefault("outcomes", [])
    r.setdefault("countries", [])
    r.setdefault("included_trials", [])
    r.setdefault("on_topic", True)
    r.setdefault("evidence_tier", "other")
    r.setdefault("intervention_category", "other")
    if not isinstance(r.get("outcomes"), list):
        r["outcomes"] = []
    # ids: keep as strings (some agents emit an int pmid)
    for k in ("pmid", "doi", "cochrane_id"):
        if r.get(k) is not None and not isinstance(r[k], str):
            r[k] = str(r[k])
    # free-text string fields: schema expects "" (not null) when absent
    for k in ("title", "journal", "study_design", "intervention_label",
              "comparator", "dominant_trial", "certainty", "key_finding",
              "off_topic_reason", "notes"):
        if r.get(k) is None:
            r[k] = ""
    for o in r["outcomes"]:
        if not isinstance(o, dict):
            continue
        vals = [str(o[k]).strip() for k in _OUTCOME_NOTE_KEYS if o.get(k) not in (None, "")]
        for k in _OUTCOME_NOTE_KEYS:
            o.pop(k, None)
        if vals:
            o["note"] = "; ".join(vals)
        for k in ("outcome", "unit", "subgroup", "note"):
            if o.get(k) is None:
                o[k] = ""
    return r


def main(db_path: str = DB_PATH, batch_glob: str = BATCH_GLOB,
         merged_path: str = MERGED_PATH, rollup_path: str = ROLLUP_PATH,
         output_dir: str = OUTPUT_DIR):
    db = json.load(open(db_path))
    corpus_keys = {paper_key(p): p for p in db}

    records: dict[str, dict] = {}
    bad_files, invalid = [], []
    for path in sorted(glob.glob(batch_glob)):
        try:
            arr = json.load(open(path))
        except Exception as e:
            bad_files.append((os.path.basename(path), str(e)))
            continue
        if not isinstance(arr, list):
            bad_files.append((os.path.basename(path), "not a JSON array"))
            continue
        for r in arr:
            if not isinstance(r, dict) or "key" not in r:
                invalid.append((os.path.basename(path), "missing key"))
                continue
            missing = [k for k in REQUIRED if k not in r]
            if missing:
                invalid.append((r.get("key", "?"), f"missing {missing}"))
            records[r["key"]] = _norm_record(r)

    # cross-check coverage against the corpus
    missing_keys = [k for k in corpus_keys if k not in records]
    extra_keys = [k for k in records if k not in corpus_keys]

    merged = list(records.values())
    with open(merged_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    # ── rollup by intervention_category (on-topic only) ──────────────────────
    groups: dict[str, list] = defaultdict(list)
    for r in records.values():
        if r.get("on_topic", True):
            cat = r.get("intervention_category", "other") or "other"
            # normalise "other:foo" → keep label but group under its own bucket
            groups[cat].append(r)

    rollup = []
    for cat, recs in groups.items():
        tiers = Counter(r.get("evidence_tier", "other") for r in recs)
        pops = Counter(r.get("population", {}).get("group", "other")
                       if isinstance(r.get("population"), dict) else "other"
                       for r in recs)
        # strongest-first sample of keys for the synthesis
        recs_sorted = sorted(recs, key=lambda r: (
            TIER_ORDER.get(r.get("evidence_tier", "other"), 9),
            -(r.get("year") or 0)))
        rollup.append({
            "intervention_category": cat,
            "n_papers": len(recs),
            "n_meta_analyses": tiers.get("meta_analysis", 0),
            "n_systematic_reviews": tiers.get("systematic_review", 0),
            "n_rcts": tiers.get("rct", 0),
            "tiers": dict(tiers),
            "populations": dict(pops),
            "labels": list({r.get("intervention_label", "") for r in recs})[:8],
            "top_keys": [r["key"] for r in recs_sorted[:40]],
        })
    rollup.sort(key=lambda g: (-g["n_meta_analyses"] - g["n_systematic_reviews"],
                               -g["n_papers"]))
    with open(rollup_path, "w", encoding="utf-8") as f:
        json.dump({"n_records": len(records),
                   "n_on_topic": sum(len(v) for v in groups.values()),
                   "groups": rollup}, f, ensure_ascii=False, indent=2)

    # ── report ───────────────────────────────────────────────────────────────
    print(f"Merged records:     {len(records)} / {len(corpus_keys)} corpus papers")
    print(f"  on-topic:         {sum(len(v) for v in groups.values())}")
    print(f"  missing (no record): {len(missing_keys)}")
    print(f"  extra (not in corpus): {len(extra_keys)}")
    if bad_files:
        print(f"  BAD batch files ({len(bad_files)}): {bad_files[:5]}")
    if invalid:
        print(f"  records w/ missing fields: {len(invalid)} (first: {invalid[:3]})")
    print(f"\n  {merged_path}")
    print(f"  {rollup_path}")
    print(f"\nIntervention groups (by MA+SR weight):")
    for g in rollup[:30]:
        print(f"  {g['intervention_category']:<34s} n={g['n_papers']:<4d} "
              f"MA={g['n_meta_analyses']:<3d} SR={g['n_systematic_reviews']:<3d} "
              f"RCT={g['n_rcts']:<3d}")

    if missing_keys:
        miss_path = os.path.join(output_dir, "evidence_db_missing.json")
        with open(miss_path, "w") as f:
            json.dump(missing_keys, f)
        print(f"\n  wrote {len(missing_keys)} missing keys → {miss_path}")


if __name__ == "__main__":
    main()
