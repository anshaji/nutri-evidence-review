#!/usr/bin/env python3
"""
Nutrition Evidence Synthesis Pipeline v2.0

Multi-source retrieval (PubMed + OpenAlex) with MeSH-based scoring.

Usage:
    export NCBI_API_KEY=your_key_here  # Optional but recommended (10x faster)
    python3 fetch_papers.py

Tracks:
    A (PubMed): Meta-analyses & systematic reviews on nutrition interventions in LMICs
    B (PubMed): Cost-effectiveness analyses
    C (OpenAlex): Nutrition-sensitive interventions (cash transfers, social protection)
"""

import sys
import os

# Add parent directory to path for package imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline.main import run_pipeline

if __name__ == "__main__":
    run_pipeline()
