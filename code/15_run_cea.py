#!/usr/bin/env python3
"""
Nutrition Evidence Synthesis Pipeline v3.0 — PHASE 2 (Cost-Effectiveness)

Runs a targeted cost-effectiveness search for each intervention in a shortlist
that you author after the Phase 1 evidence review.

Usage:
    python3 run_cea.py                      # uses ./shortlist.json
    python3 run_cea.py path/to/shortlist.json

Prereqs:
    1. Run Phase 1: python3 fetch_papers.py
    2. Review top_papers_for_review.json in-conversation, shortlist interventions
    3. Copy shortlist.template.json -> shortlist.json and fill it in
    4. (Optional) drop a CEA registry CSV at data/ghcea_registry.csv (see data/README.md)
"""

import sys
import os

# Add project root to path so the 'code' package is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from code.cea_main import run_phase2
from code.config import SHORTLIST_PATH

if __name__ == "__main__":
    shortlist = sys.argv[1] if len(sys.argv) > 1 else SHORTLIST_PATH
    run_phase2(shortlist)
