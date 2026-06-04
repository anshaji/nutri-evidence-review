"""Post-synthesis claim verification (audit fix #3).

Catches the failure modes the VAS audit surfaced in Stage 4:
  - external-knowledge leaks  (a figure with no corpus PMID)
  - misattribution            (a real number cited to the WRONG PMID — e.g.
                               the "823,000 deaths" breastfeeding figure pinned
                               onto vitamin A)

For every {numeric value, PMID} claim in a finished synthesis markdown it checks:
  (a) corpus membership — is that PMID actually in papers_database.json /
      cea_by_intervention.json?  (fully automated, stdlib)
  (b) support — does the cited paper's title/abstract contain the claimed
      number?  (heuristic string match; anything it can't confirm is flagged
      for the in-conversation semantic check, NOT silently passed.)

This is a lint: it reports, it does not edit.
"""

from __future__ import annotations

import json
import os
import re
import sys

from .config import OUTPUT_DIR, CEA_OUTPUT_PATH

# A PMID mention: "PMID: 26869575", "PMID 26869575", "(PMID 26869575)"
_PMID_RE = re.compile(r"PMID[:\s]*([0-9]{5,9})", re.IGNORECASE)

# Numbers that look like quantitative claims (effect sizes, %, money, counts).
_NUMBER_RE = re.compile(r"\$?\d[\d,]*\.?\d*\s*%?")

# Words that mark a line as making a quantitative *claim* worth sourcing.
_CLAIM_MARKERS = (
    "rr", "or ", "risk ratio", "odds ratio", "smd", "md ", "ci",
    "%", "daly", "death", "mortality", "reduction", "increase",
    "per child", "per year", "per dose", "cost", "$", "incremental",
)


def _default_corpus_paths() -> list[str]:
    paths = [os.path.join(OUTPUT_DIR, "papers_database.json")]
    cea = CEA_OUTPUT_PATH if os.path.isabs(CEA_OUTPUT_PATH) else os.path.join(OUTPUT_DIR, os.path.basename(CEA_OUTPUT_PATH))
    paths.append(cea)
    return paths


def load_corpus(paths: list[str] | None = None) -> dict:
    """Build {pmid -> paper} from the Phase 1 + Phase 2 corpus files."""
    paths = paths or _default_corpus_paths()
    papers: dict[str, dict] = {}

    def _add(p: dict):
        pmid = p.get("pmid")
        if pmid:
            papers[str(pmid)] = p

    for path in paths:
        if not os.path.isfile(path):
            print(f"  [verify] corpus file not found (skipping): {path}", file=sys.stderr)
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):  # papers_database.json
            for p in data:
                _add(p)
        elif isinstance(data, dict):  # cea_by_intervention.json
            for iv in data.get("interventions", []):
                for p in iv.get("cea_papers", []):
                    _add(p)
    print(f"  [verify] corpus loaded: {len(papers)} papers with PMIDs", file=sys.stderr)
    return papers


def _normalize_number(tok: str) -> str:
    return tok.replace(",", "").replace("$", "").replace("%", "").strip()


def _supported_by_text(numbers: list[str], paper: dict) -> bool:
    """Heuristic: does the paper's title/abstract contain any claimed number?"""
    hay = (paper.get("title", "") + " " + paper.get("abstract", "")).replace(",", "")
    for n in numbers:
        norm = _normalize_number(n)
        if len(norm.replace(".", "")) >= 2 and norm in hay:  # ignore trivial 1-digit
            return True
    return False


def _line_numbers(line: str) -> list[str]:
    return [t.strip() for t in _NUMBER_RE.findall(line) if _normalize_number(t)]


def verify_text(markdown: str, corpus: dict) -> dict:
    """Verify all PMID-backed claims and flag unsourced numeric claims."""
    pmid_claims = []
    unsourced = []

    for lineno, raw in enumerate(markdown.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        pmids = _PMID_RE.findall(line)
        # Exclude the PMID digits themselves from the claimed-numbers list
        numbers = [n for n in _line_numbers(line) if _normalize_number(n) not in pmids]
        lower = line.lower()
        is_claimish = any(m in lower for m in _CLAIM_MARKERS) and bool(numbers)

        if pmids:
            for pmid in pmids:
                paper = corpus.get(str(pmid))
                in_corpus = paper is not None
                supported = _supported_by_text(numbers, paper) if (in_corpus and numbers) else None
                if not in_corpus:
                    status = "NOT_IN_CORPUS"
                elif not numbers:
                    status = "OK_NO_NUMBER"  # citation w/o a numeric claim on this line
                elif supported:
                    status = "SUPPORTED"
                else:
                    status = "NEEDS_REVIEW"  # in corpus but number not found in abstract
                pmid_claims.append({
                    "line": lineno, "pmid": str(pmid), "numbers": numbers,
                    "status": status, "text": line[:200],
                    "cited_title": (paper or {}).get("title", "") if in_corpus else "",
                })
        elif is_claimish:
            unsourced.append({"line": lineno, "numbers": numbers, "text": line[:200]})

    return {"pmid_claims": pmid_claims, "unsourced_numeric": unsourced}


def format_report(report: dict) -> str:
    claims = report["pmid_claims"]
    unsourced = report["unsourced_numeric"]
    not_in = [c for c in claims if c["status"] == "NOT_IN_CORPUS"]
    review = [c for c in claims if c["status"] == "NEEDS_REVIEW"]
    supported = [c for c in claims if c["status"] == "SUPPORTED"]

    out = []
    out.append("=" * 70)
    out.append("SYNTHESIS CLAIM VERIFICATION REPORT")
    out.append("=" * 70)
    out.append(f"PMID-backed claims: {len(claims)}  "
               f"(supported: {len(supported)}, needs review: {len(review)}, "
               f"not in corpus: {len(not_in)})")
    out.append(f"Unsourced numeric claims: {len(unsourced)}")
    out.append("")

    if not_in:
        out.append("─ NOT IN CORPUS (likely misattribution / external-knowledge leak) ─")
        for c in not_in:
            out.append(f"  L{c['line']}  PMID {c['pmid']}  {c['numbers']}")
            out.append(f"         {c['text']}")
        out.append("")
    if review:
        out.append("─ NEEDS MANUAL REVIEW (PMID in corpus, but number not found in its abstract) ─")
        for c in review:
            out.append(f"  L{c['line']}  PMID {c['pmid']}  {c['numbers']}")
            out.append(f"         claim: {c['text']}")
            out.append(f"         cited: {c['cited_title'][:120]}")
        out.append("")
    if unsourced:
        out.append("─ UNSOURCED NUMERIC CLAIMS (no PMID on the line) ─")
        for c in unsourced:
            out.append(f"  L{c['line']}  {c['numbers']}")
            out.append(f"         {c['text']}")
        out.append("")

    verdict = "PASS" if not not_in and not unsourced else "REVIEW NEEDED"
    out.append(f"Verdict: {verdict}")
    out.append("=" * 70)
    return "\n".join(out)


def verify_file(markdown_path: str, corpus_paths: list[str] | None = None) -> dict:
    with open(markdown_path, encoding="utf-8") as f:
        markdown = f.read()
    corpus = load_corpus(corpus_paths)
    report = verify_text(markdown, corpus)
    print(format_report(report))
    return report
