#!/usr/bin/env python3
"""
Nutrition Evidence Synthesis Pipeline v3.0 — PHASE 1 (Evidence)

Multi-source retrieval (PubMed + OpenAlex) with MeSH-based scoring, targeting
nutrition interventions for children under 5 and women of reproductive age in
LMICs. Cost-effectiveness is handled separately in Phase 2 (run_cea.py).

Usage:
    # Set your API key in .env or export it:
    export NCBI_API_KEY=your_key_here
    python3 fetch_papers.py

Tracks:
    A (PubMed): Meta-analyses & systematic reviews on nutrition interventions
    C (OpenAlex): Nutrition-sensitive interventions (cash transfers, social protection)

Output: top_papers_for_review.json (top 200 with full text) → review in-conversation,
author shortlist.json, then run Phase 2 with `python3 run_cea.py`.
"""

import sys
import os

# Add parent directory to path for package imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline.main import run_phase1

if __name__ == "__main__":
    run_phase1()
