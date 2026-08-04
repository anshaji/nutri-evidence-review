#!/usr/bin/env python3
"""Entry point — CARE deep-dive pipeline stages (post-retrieval).

Usage (from the repo root):
    python3 CARE_review/code/run_pipeline.py corpus            # merge blocks → corpus DB
    python3 CARE_review/code/run_pipeline.py fulltext [limit]  # full text (shared cache)
    python3 CARE_review/code/run_pipeline.py cards             # extraction cards + batches
    python3 CARE_review/code/run_pipeline.py merge             # batches → evidence DB + rollup
    python3 CARE_review/code/run_pipeline.py assemble          # sections → deep-dive review
"""

import os
import sys

# repo root on sys.path so both `code.…` (core) and `CARE_review.code.…` resolve
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from CARE_review.code.pipeline import (
    build_corpus, run_fulltext, build_cards, merge_evidence, assemble,
)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "corpus"
    if cmd == "corpus":
        build_corpus()
    elif cmd == "fulltext":
        lim = int(sys.argv[2]) if len(sys.argv) > 2 else None
        run_fulltext(limit=lim)
    elif cmd == "cards":
        build_cards()
    elif cmd == "merge":
        merge_evidence()
    elif cmd == "assemble":
        assemble()
    else:
        raise SystemExit(f"unknown command: {cmd} "
                         "(use: corpus | fulltext | cards | merge | assemble)")
