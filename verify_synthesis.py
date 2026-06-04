#!/usr/bin/env python3
"""
Nutrition Evidence Synthesis Pipeline v3.0 — Claim verification (audit fix #3)

Lints a finished synthesis markdown against the retrieved corpus, flagging:
  - claims cited to a PMID that is NOT in the corpus (misattribution / leak)
  - numeric claims whose value is not found in the cited paper's abstract
  - numeric claims with no PMID at all

Usage:
    python3 verify_synthesis.py output/FULL_INTERVENTION_SYNTH.md
    python3 verify_synthesis.py <synthesis.md> [corpus1.json corpus2.json ...]

With no corpus paths it defaults to papers_database.json + cea_by_intervention.json.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pipeline.verify import verify_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    md_path = sys.argv[1]
    corpus_paths = sys.argv[2:] or None
    report = verify_file(md_path, corpus_paths)
    # Non-zero exit if anything needs review (useful in CI / pre-commit)
    bad = [c for c in report["pmid_claims"] if c["status"] == "NOT_IN_CORPUS"]
    sys.exit(1 if (bad or report["unsourced_numeric"]) else 0)
