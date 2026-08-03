#!/usr/bin/env python3
"""Entry point for the CARE deep-dive Phase-1 retrieval (evidence only).

Usage:
    python3 code/28_run_deepdive.py                  # all blocks
    python3 code/28_run_deepdive.py breastfeeding    # one block (re-run)

Runs PICOS-targeted retrieval for the 3 partner interventions (blocks: cmam,
breastfeeding, mms — breastfeeding facility/community is tagged at extraction),
implementation-weighted, cost excluded. Writes ranked per-block evidence sets
to CARE_review/data/.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from code.deepdive import run_deepdive

if __name__ == "__main__":
    only = sys.argv[1:] or None
    run_deepdive(only=only)
