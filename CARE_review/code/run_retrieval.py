#!/usr/bin/env python3
"""Entry point — CARE deep-dive Stage 1 retrieval (evidence only).

Usage (from the repo root):
    python3 CARE_review/code/run_retrieval.py                  # all blocks
    python3 CARE_review/code/run_retrieval.py breastfeeding    # one block (re-run)

Runs PICOS-targeted retrieval for the 3 partner interventions (blocks: cmam,
breastfeeding, mms — breastfeeding facility/community is tagged at extraction,
not retrieval), implementation-weighted, cost excluded. Writes ranked per-block
evidence sets to CARE_review/data/.
"""

import os
import sys

# repo root on sys.path so both `code.…` (core) and `CARE_review.code.…` resolve
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from CARE_review.code.retrieval import run_deepdive

if __name__ == "__main__":
    only = sys.argv[1:] or None
    run_deepdive(only=only)
