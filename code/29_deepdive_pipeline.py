"""CARE deep-dive pipeline: corpus assembly + full-text (Stage 3.5→3.6 prep).

Bridges the deep-dive retrieval (data/deepdive/{block}.json) into the existing
full-corpus machinery (full text → extraction → synthesis), but namespaced so it
never clobbers the main pipeline's data:

  - deep-dive corpus DB  → data/deepdive/deepdive_corpus.json
  - per-paper full text   → data/fulltext/{key}.json   (SHARED — cached/reused)
  - network caches        → data/raw_responses/         (SHARED)

The corpus is the union of the 3 blocks, deduped by paper_key, each paper
tagged with `deepdive_blocks` (a paper on MMS for breastfeeding women can belong
to both). Cost is not involved here — cost is Phase 2, deferred.
"""

import json
import os
import re
from datetime import datetime

from .config import DEEPDIVE_DIR
from .fulltext_all import paper_key, run as run_fulltext_core
from .build_extraction_inputs import main as build_cards_main
from .merge_evidence_db import main as merge_main

BLOCK_KEYS = ["cmam", "breastfeeding", "mms"]
CORPUS_PATH = os.path.join(DEEPDIVE_DIR, "deepdive_corpus.json")
EXTRACTION_INPUT_DIR = os.path.join(DEEPDIVE_DIR, "extraction_inputs")
EVIDENCE_DB_DIR = os.path.join(DEEPDIVE_DIR, "evidence_db")          # batch_*.json
EVIDENCE_DB_PATH = os.path.join(DEEPDIVE_DIR, "evidence_db.json")
ROLLUP_PATH = os.path.join(DEEPDIVE_DIR, "evidence_by_intervention.json")
SYNTH_SECTIONS_DIR = os.path.join(DEEPDIVE_DIR, "synthesis_sections")
REVIEW_OUT = "./CARE_review/CARE_DEEPDIVE_REVIEW.md"

# Section display order + the extraction category each maps to.
SECTION_ORDER = [
    ("cmam_sam_mam", "Community-based Management of Acute Malnutrition (CMAM)"),
    ("breastfeeding", "Breastfeeding Promotion & Support"),
    ("anc_mmn", "Antenatal Multiple Micronutrient Supplementation (MMS)"),
]


def build_corpus() -> str:
    """Merge the per-block retrieval into one deduped corpus DB. Returns its path."""
    by_key: dict[str, dict] = {}
    per_block: dict[str, int] = {}
    for bk in BLOCK_KEYS:
        path = os.path.join(DEEPDIVE_DIR, f"{bk}.json")
        if not os.path.isfile(path):
            print(f"  [warn] missing block file: {path}")
            continue
        papers = json.load(open(path, encoding="utf-8"))
        per_block[bk] = len(papers)
        for p in papers:
            k = paper_key(p)
            if k in by_key:
                # already seen in another block — union block membership,
                # keep the higher relevance score.
                existing = by_key[k]
                if bk not in existing["deepdive_blocks"]:
                    existing["deepdive_blocks"].append(bk)
                if p.get("relevance_score", 0) > existing.get("relevance_score", 0):
                    existing["relevance_score"] = p["relevance_score"]
                    existing["implementation_score"] = p.get("implementation_score", 0)
            else:
                p = dict(p)
                p["deepdive_blocks"] = [bk]
                by_key[k] = p

    corpus = sorted(by_key.values(),
                    key=lambda x: x.get("relevance_score", 0), reverse=True)
    os.makedirs(DEEPDIVE_DIR, exist_ok=True)
    with open(CORPUS_PATH, "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2, default=str)

    overlap = sum(1 for p in corpus if len(p["deepdive_blocks"]) > 1)
    print(f"Deep-dive corpus: {len(corpus)} unique papers "
          f"(from {sum(per_block.values())} across blocks; {overlap} multi-block)")
    for bk in BLOCK_KEYS:
        n = sum(1 for p in corpus if bk in p["deepdive_blocks"])
        print(f"    {bk:16s}: {n}  (retrieved {per_block.get(bk, 0)})")
    print(f"    written → {CORPUS_PATH}")
    return CORPUS_PATH


def run_fulltext(limit: int | None = None):
    """Fetch full text for the deep-dive corpus (shared cache), building the
    corpus first if needed."""
    if not os.path.isfile(CORPUS_PATH):
        build_corpus()
    run_fulltext_core(limit=limit, db_path=CORPUS_PATH)


def build_cards():
    """Build per-paper extraction cards + batches for the deep-dive corpus,
    namespaced under data/deepdive/extraction_inputs/."""
    build_cards_main(db_path=CORPUS_PATH, input_dir=EXTRACTION_INPUT_DIR)


def merge_evidence():
    """Merge deep-dive extraction batches → deep-dive evidence DB + rollup."""
    merge_main(
        db_path=CORPUS_PATH,
        batch_glob=os.path.join(EVIDENCE_DB_DIR, "batch_*.json"),
        merged_path=EVIDENCE_DB_PATH,
        rollup_path=ROLLUP_PATH,
        output_dir=DEEPDIVE_DIR,
    )


def assemble():
    """Stitch the per-intervention synthesis sections into the deliverable.

    Evidence-only (cost = Phase 2, deferred). Reads
    data/deepdive/synthesis_sections/{category}.md and writes the CARE deep-dive
    review to CARE_review/CARE_DEEPDIVE_REVIEW.md.
    """
    os.makedirs(os.path.dirname(REVIEW_OUT), exist_ok=True)
    n_records = 0
    if os.path.isfile(EVIDENCE_DB_PATH):
        n_records = len(json.load(open(EVIDENCE_DB_PATH, encoding="utf-8")))

    parts = [
        "# CARE / ScaleWorks Deep-Dive Evidence Review",
        "",
        "*PICOS-structured review of three partner-selected interventions — "
        "**CMAM**, **Breastfeeding support** (facility + community), and "
        "**Antenatal MMS** — for CARE and IA partners (Save the Children, Mercy Corps).*",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}  ·  "
        f"**Evidence records:** {n_records}  ·  "
        "**Scope:** evidence only — cost / cost-effectiveness is a separate later "
        "phase and is deliberately excluded here.",
        "",
        "> **How to read.** Each intervention is rated on two axes: **Evidence "
        "strength (A/B/C)** and **Implementation readiness (High/Moderate/Low/"
        "Unclear)** — the latter reflects coverage, adherence, delivery-platform "
        "fit, and barriers, because partners identified adherence/coverage (not "
        "efficacy) as the binding constraint. PICOS spec: "
        "`docs/PICOS_specification.md`.",
        "",
        "---",
        "",
    ]

    found = []
    for cat, _display in SECTION_ORDER:
        path = os.path.join(SYNTH_SECTIONS_DIR, f"{cat}.md")
        if os.path.isfile(path):
            body = open(path, encoding="utf-8").read().strip()
            parts.append(body)
            parts.append("\n\n---\n")
            found.append(cat)
        else:
            print(f"  [warn] missing synthesis section: {path}")

    with open(REVIEW_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(parts).rstrip() + "\n")
    print(f"Assembled {len(found)}/{len(SECTION_ORDER)} sections → {REVIEW_OUT}")
    return REVIEW_OUT
