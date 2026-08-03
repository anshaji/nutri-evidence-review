#!/usr/bin/env python3
"""Cap the corpus to a 1,000-paper working set — NOT bounded by the ranking.

Rationale: the user capped extraction/synthesis scope to 1,000 papers and asked
that the selection NOT follow the relevance ranking. The 592 papers already
extracted are score-representative (median score ~= the full corpus, only 43/200
of the top-ranked are among them), so they are reused; the set is topped up with
a uniform RANDOM sample (fixed seed) of the remaining papers to reach 1,000.

Outputs:
  - data/extraction_inputs/batches.json      OVERWRITTEN with only the NEW
       papers' batches, indexed from 1000 (so their output files batch_1000.json+
       never collide with the already-written batch_0000..batch_0124.json).
       The original full manifest is backed up to batches_full.json.
  - data/cap_sample_keys.json                the full 1,000-key working set.

Then: run the extraction workflow on the new indices; merge picks up the 592 old
batch files + the ~408 new ones = 1,000 records.

Usage: python3 code/24_cap_sample.py [target_total=1000] [seed=20260709]
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from code.fulltext_all import paper_key

OUTPUT_DIR = "./data"
INPUT_DIR = os.path.join(OUTPUT_DIR, "extraction_inputs")
BATCHES = os.path.join(INPUT_DIR, "batches.json")
BATCHES_FULL = os.path.join(INPUT_DIR, "batches_full.json")
NEW_INDEX_START = 1000
BATCH_TOKEN_TARGET = 70_000
BATCH_MAX_PAPERS = 18


def _est_tokens(key: str) -> int:
    p = os.path.join(INPUT_DIR, key + ".json")
    try:
        c = json.load(open(p))
        words = len((c.get("abstract") or "").split()) + \
            len((c.get("fulltext_excerpt") or "").split()) + 200
        return int(words * 1.3)
    except Exception:
        return 1500


def main():
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20260709

    db = json.load(open(os.path.join(OUTPUT_DIR, "papers_database.json")))
    all_keys = [paper_key(p) for p in db]
    done = [r["key"] for r in json.load(open(os.path.join(OUTPUT_DIR, "evidence_db.json")))]
    done_set = set(done)

    remaining = [k for k in all_keys if k not in done_set]
    n_fill = max(0, target - len(done_set))
    n_fill = min(n_fill, len(remaining))

    rng = random.Random(seed)
    fill = rng.sample(remaining, n_fill)

    working_set = list(done_set) + fill
    json.dump(working_set, open(os.path.join(OUTPUT_DIR, "cap_sample_keys.json"), "w"))

    # bin-pack ONLY the new (fill) papers into batches indexed from NEW_INDEX_START
    fill_sorted = sorted(fill, key=lambda k: -_est_tokens(k))
    batches, cur, cur_tok = [], [], 0
    for k in fill_sorted:
        t = _est_tokens(k)
        if cur and (cur_tok + t > BATCH_TOKEN_TARGET or len(cur) >= BATCH_MAX_PAPERS):
            batches.append(cur); cur, cur_tok = [], 0
        cur.append(k); cur_tok += t
    if cur:
        batches.append(cur)

    manifest = {
        "n_papers": len(fill),
        "n_batches": len(batches),
        "start_index": NEW_INDEX_START,
        "note": "capped 1000-paper run: NEW papers only; 592 already-extracted reused via existing batch files",
        "batches": [{"batch_index": NEW_INDEX_START + i, "keys": b}
                    for i, b in enumerate(batches)],
    }

    # back up the original full manifest once, then overwrite batches.json
    if os.path.isfile(BATCHES) and not os.path.isfile(BATCHES_FULL):
        os.rename(BATCHES, BATCHES_FULL)
    json.dump(manifest, open(BATCHES, "w"), ensure_ascii=False, indent=2)

    idxs = [b["batch_index"] for b in manifest["batches"]]
    print(f"working set (cap): {len(working_set)} papers "
          f"({len(done_set)} reused + {len(fill)} newly sampled, seed={seed})")
    print(f"new batches to run: {len(batches)}  indices {idxs[0]}..{idxs[-1]}")
    print(f"  manifest → {BATCHES}  (original backed up → {BATCHES_FULL})")
    print(f"  working keys → data/cap_sample_keys.json")
    print(f"\nRun extraction with: only = {idxs}")


if __name__ == "__main__":
    main()
