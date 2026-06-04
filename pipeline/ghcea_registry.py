"""Optional local CEA-registry enrichment for Phase 2 (no network).

Research spike finding: neither the Tufts/CEVR Global Health CEA Registry nor
DCP3 exposes a stdlib-urllib-reachable API — the registry is a client-side JS
app and DCP3's cost data is a PDF supplement. So the registry is consumed here
as an OPTIONAL local CSV that a human downloads once (see data/README.md). If
the file is absent, Phase 2 still produces complete output from the PubMed/
OpenAlex CEA backbone — this module just returns no matches.
"""

from __future__ import annotations

import csv
import os
import sys

from .config import GHCEA_LOCAL_PATH, DCP3_LOCAL_PATH

# Tolerant column-name aliases → canonical key. Registry exports vary.
_COLUMN_ALIASES = {
    "intervention": "intervention",
    "intervention name": "intervention",
    "title": "intervention",
    "description": "intervention",
    "country": "country",
    "countries": "country",
    "cost per daly": "cost_per_daly",
    "cost/daly": "cost_per_daly",
    "costperdaly": "cost_per_daly",
    "icer": "cost_per_daly",
    "year": "year",
    "publication year": "year",
    "reference": "reference",
    "citation": "reference",
    "author": "reference",
}


def _normalize_row(row: dict) -> dict:
    """Map a raw CSV row's columns onto canonical keys (tolerant of naming)."""
    out = {"_raw": dict(row)}
    for k, v in row.items():
        if k is None:
            continue
        canon = _COLUMN_ALIASES.get(k.strip().lower())
        if canon and canon not in out:
            out[canon] = (v or "").strip()
    return out


def _load_csv(path: str, source: str) -> list[dict]:
    if not path or not os.path.isfile(path):
        return []
    rows = []
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            for raw in csv.DictReader(f):
                norm = _normalize_row(raw)
                norm["_source"] = source
                rows.append(norm)
    except Exception as e:
        print(f"  [registry] failed to read {path}: {e}", file=sys.stderr)
        return []
    print(f"  [registry] loaded {len(rows)} rows from {path}", file=sys.stderr)
    return rows


def load_registry() -> list[dict]:
    """Load the local CEA registry CSV(s) if present, else return []."""
    rows = _load_csv(GHCEA_LOCAL_PATH, "ghcea") + _load_csv(DCP3_LOCAL_PATH, "dcp3")
    if not rows:
        print(
            "  [registry] no local CEA registry file found "
            f"({GHCEA_LOCAL_PATH}); relying on the PubMed/OpenAlex CEA backbone. "
            "See data/README.md to add one.",
            file=sys.stderr,
        )
    return rows


def match_intervention(registry_rows: list[dict], intervention: dict) -> list[dict]:
    """Case-insensitive substring match of name + synonyms against registry rows."""
    if not registry_rows:
        return []
    keys = [intervention["name"]] + intervention.get("synonyms", [])
    keys = [k.lower() for k in keys if k]
    matches = []
    for row in registry_rows:
        hay = (row.get("intervention", "") + " " + row.get("_raw", {}).get("Intervention", "")).lower()
        if not hay.strip():
            # Fall back to scanning all raw values if no canonical intervention col
            hay = " ".join(str(v) for v in row.get("_raw", {}).values()).lower()
        if any(k in hay for k in keys):
            matches.append({
                "intervention": row.get("intervention", ""),
                "country": row.get("country", ""),
                "cost_per_daly": row.get("cost_per_daly", ""),
                "year": row.get("year", ""),
                "reference": row.get("reference", ""),
                "source": row.get("_source", ""),
            })
    return matches
