"""CARE deep-dive code — the PICOS-targeted, implementation-weighted review layer.

This package owns everything specific to the CARE workstream:

    queries.py    the 3 intervention blocks + the implementation-pass filters
    scoring.py    implementation-relevance ranking (additive over the core scorer)
    retrieval.py  Stage 1 orchestrator — MA + SR + IMPL passes, per block
    pipeline.py   Stages 3-10 — corpus, full text, cards, merge, assemble

It *reuses* the core pipeline as infrastructure (`code.pubmed_client`,
`code.dedup`, `code.fulltext_all`, …) rather than duplicating it, so the two
stay in sync. Core modules carry no deep-dive logic.

Because the core package is imported absolutely (`from code.…`), the repo root
must be on sys.path. Both entry points handle that; if importing directly, do:

    import sys; sys.path.insert(0, "<repo-root>")
    from CARE_review.code.pipeline import assemble
"""

import os as _os
import sys as _sys

# Ensure the repo root is importable so `from code.…` resolves when this package
# is loaded directly (e.g. by the entry-point scripts).
_REPO_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
if _REPO_ROOT not in _sys.path:
    _sys.path.insert(0, _REPO_ROOT)
