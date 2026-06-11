"""Phase 2 orchestrator: cost-effectiveness search per shortlisted intervention.

Reads the human-authored shortlist.json (produced after the Phase 1 evidence
review), and for each intervention runs a targeted CEA search (PubMed + OpenAlex)
plus an optional local-registry lookup. Writes cea_by_intervention.json for the
final in-conversation synthesis.

Enforces the CEA-rating guard (#2b): an intervention with no CEA papers AND no
registry matches gets cea_rating_allowed=False — the synthesis must record its
cost-effectiveness as "Unknown" rather than inventing one.
"""

from __future__ import annotations

import json
import os
import sys

from .config import SHORTLIST_PATH, CEA_OUTPUT_PATH, OUTPUT_DIR
from .cea_client import fetch_cea_for_intervention
from .ghcea_registry import load_registry, match_intervention


def _load_shortlist(path: str) -> list[dict]:
    if not os.path.isfile(path):
        print(
            f"ERROR: shortlist not found at {path}\n"
            "Create it from shortlist.template.json after reviewing "
            "top_papers_for_review.json (Phase 1).",
            file=sys.stderr,
        )
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    interventions = data.get("interventions", [])
    valid = []
    for iv in interventions:
        if not iv.get("name"):
            print(f"  [shortlist] skipping entry with no 'name': {iv}", file=sys.stderr)
            continue
        valid.append(iv)
    if not valid:
        print("ERROR: shortlist has no valid interventions (each needs a 'name').", file=sys.stderr)
        sys.exit(1)
    return valid


def run_phase2(shortlist_path: str = SHORTLIST_PATH) -> dict:
    """Execute Phase 2: targeted CEA retrieval for each shortlisted intervention."""
    print("=" * 70)
    print("NUTRITION EVIDENCE SYNTHESIS PIPELINE v3.0 — PHASE 2 (COST-EFFECTIVENESS)")
    print("=" * 70)

    interventions = _load_shortlist(shortlist_path)
    print(f"\nShortlist: {len(interventions)} intervention(s) from {shortlist_path}")

    registry_rows = load_registry()
    registry_available = bool(registry_rows)

    records = []
    for i, iv in enumerate(interventions, 1):
        name = iv["name"]
        print(f"\n{'─' * 70}")
        print(f"[{i}/{len(interventions)}] {name}")
        print(f"{'─' * 70}")

        cea_papers = fetch_cea_for_intervention(iv)
        registry_matches = match_intervention(registry_rows, iv)

        cea_rating_allowed = bool(cea_papers) or bool(registry_matches)
        records.append({
            "name": name,
            "synonyms": iv.get("synonyms", []),
            "mesh": iv.get("mesh", []),
            "population": iv.get("population", ""),
            "num_cea_papers": len(cea_papers),
            "num_registry_matches": len(registry_matches),
            "registry_available": registry_available,
            "cea_rating_allowed": cea_rating_allowed,
            "cea_papers": cea_papers,
            "registry_matches": registry_matches,
        })
        print(f"  → {len(cea_papers)} CEA paper(s), {len(registry_matches)} registry match(es), "
              f"rating_allowed={cea_rating_allowed}")

    out_path = os.path.join(OUTPUT_DIR, os.path.basename(CEA_OUTPUT_PATH)) \
        if OUTPUT_DIR not in (".", "") else CEA_OUTPUT_PATH
    output = {
        "generated_from": shortlist_path,
        "registry_available": registry_available,
        "interventions": records,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False, default=str)

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("PHASE 2 SUMMARY")
    print(f"{'=' * 70}")
    print(f"{'Intervention':<45s} {'CEA':>4s} {'Reg':>4s} {'Rating?':>8s}")
    for r in records:
        flag = "OK" if r["cea_rating_allowed"] else "UNKNOWN"
        print(f"{r['name'][:44]:<45s} {r['num_cea_papers']:>4d} "
              f"{r['num_registry_matches']:>4d} {flag:>8s}")
    print(f"\nRegistry available: {registry_available}")
    print(f"Wrote {out_path}")
    print(f"{'=' * 70}")

    return output
