#!/usr/bin/env python3
"""Full-corpus full-text retrieval entry point.

Scales Stage 3.5 from the top-200 to the entire papers_database.json
(PubMed via PMID→PMCID, OpenAlex via DOI→PMCID, Unpaywall PDF fallback).

Usage:
    python3 code/20_fetch_fulltext_all.py          # whole corpus
    python3 code/20_fetch_fulltext_all.py 40       # first 40 papers (smoke test)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from code.fulltext_all import run

if __name__ == "__main__":
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else None
    run(limit=lim)
