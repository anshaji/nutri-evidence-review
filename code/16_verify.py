"""Post-synthesis claim verification (audit fix #3).

Catches the failure modes the VAS audit surfaced in Stage 4:
  - external-knowledge leaks  (a figure with no corpus citation)
  - misattribution            (a real number cited to the WRONG paper — e.g.
                               the "823,000 deaths" breastfeeding figure pinned
                               onto vitamin A)

For every {numeric value, citation} claim in a finished synthesis markdown it
checks:
  (a) corpus membership — is that identifier (PMID, DOI, or paper key) actually
      in papers_database.json / evidence_db.json / cea_by_intervention.json?
  (b) support — does the cited paper's title/abstract/**full text**/extracted
      outcomes contain the claimed number?  (heuristic; anything it can't confirm
      is flagged for the in-conversation semantic check, NOT silently passed.)

v4 (full-corpus): citations may be PMID, DOI, or paper key (pmid_… / oa_W… /
doi_…), and numeric support is checked against the per-paper full text
(data/fulltext/{key}.json) and the extracted outcome values
(data/evidence_db.json), not just the abstract — because the full-corpus
synthesis grounds effect sizes in full text that no longer lives in the DB.

This is a lint: it reports, it does not edit.
"""

from __future__ import annotations

import json
import os
import re
import sys

from .config import OUTPUT_DIR, CEA_OUTPUT_PATH

FULLTEXT_DIR = os.path.join(OUTPUT_DIR, "fulltext")


def paper_key(p: dict) -> str:
    """Stable filesystem-safe key (PMID > OpenAlex id > DOI).

    Kept in sync with code/19_fulltext_all.py:paper_key; inlined here to avoid a
    package load-order dependency (verify is aliased before fulltext_all).
    """
    if p.get("pmid"):
        return f"pmid_{p['pmid']}"
    oa = p.get("openalex_id") or p.get("id") or ""
    m = re.search(r"(W\d+)", oa)
    if m:
        return f"oa_{m.group(1)}"
    doi = p.get("doi") or ""
    return "doi_" + re.sub(r"[^A-Za-z0-9]+", "_", doi).strip("_") or "unknown"

# Citations we recognise: PMID, paper key, or bare DOI.
_PMID_RE = re.compile(r"PMID[:\s]*([0-9]{5,9})", re.IGNORECASE)
_KEY_RE = re.compile(r"\b((?:pmid|oa|doi)_[A-Za-z0-9._]+)\b")
_DOI_RE = re.compile(r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)\b")

_NUMBER_RE = re.compile(r"\$?\d[\d,]*\.?\d*\s*%?")

_CLAIM_MARKERS = (
    "rr", "or ", "risk ratio", "odds ratio", "smd", "md ", "ci",
    "%", "daly", "death", "mortality", "reduction", "increase",
    "per child", "per year", "per dose", "cost", "$", "incremental",
)


def _norm_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    doi = doi.strip().lower()
    for pre in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.startswith(pre):
            doi = doi[len(pre):]
    return doi.rstrip("/.")


def _default_corpus_paths() -> list[str]:
    cea = CEA_OUTPUT_PATH if os.path.isabs(CEA_OUTPUT_PATH) else os.path.join(OUTPUT_DIR, os.path.basename(CEA_OUTPUT_PATH))
    return [
        os.path.join(OUTPUT_DIR, "papers_database.json"),
        os.path.join(OUTPUT_DIR, "evidence_db.json"),
        cea,
    ]


def load_corpus(paths: list[str] | None = None) -> dict:
    """Index the corpus by PMID, DOI, and paper key.

    Returns {"by_id": {identifier -> paper}, "outcome_nums": {key -> set(str)}}.
    """
    paths = paths or _default_corpus_paths()
    by_id: dict[str, dict] = {}
    outcome_nums: dict[str, set] = {}

    def _index(p: dict):
        key = paper_key(p)
        p.setdefault("_key", key)
        by_id[key] = p
        if p.get("pmid"):
            by_id[str(p["pmid"])] = p
        nd = _norm_doi(p.get("doi"))
        if nd:
            by_id[nd] = p

    for path in paths:
        if not os.path.isfile(path):
            print(f"  [verify] corpus file not found (skipping): {path}", file=sys.stderr)
            continue
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            # papers_database.json OR evidence_db.json (records)
            for p in data:
                if not isinstance(p, dict):
                    continue
                if "outcomes" in p and "intervention_category" in p:
                    # evidence_db record → harvest numeric values for support check
                    key = p.get("key") or paper_key(p)
                    nums = set()
                    for o in p.get("outcomes", []):
                        for fld in ("value", "ci_low", "ci_high"):
                            v = o.get(fld)
                            if isinstance(v, (int, float)):
                                nums.add(str(v).replace(".0", "") if str(v).endswith(".0") else str(v))
                    outcome_nums.setdefault(key, set()).update(nums)
                    by_id.setdefault(key, p)
                    if p.get("pmid"):
                        by_id.setdefault(str(p["pmid"]), p)
                    nd = _norm_doi(p.get("doi"))
                    if nd:
                        by_id.setdefault(nd, p)
                else:
                    _index(p)
        elif isinstance(data, dict):  # cea_by_intervention.json
            for iv in data.get("interventions", []):
                for p in iv.get("cea_papers", []):
                    _index(p)
    print(f"  [verify] corpus indexed: {len(by_id)} identifiers "
          f"({len(outcome_nums)} records with extracted outcomes)", file=sys.stderr)
    return {"by_id": by_id, "outcome_nums": outcome_nums}


def _normalize_number(tok: str) -> str:
    return tok.replace(",", "").replace("$", "").replace("%", "").strip()


_FT_CACHE: dict[str, str] = {}


def _fulltext_of(paper: dict) -> str:
    key = paper.get("_key") or paper.get("key") or paper_key(paper)
    if key in _FT_CACHE:
        return _FT_CACHE[key]
    text = ""
    fp = os.path.join(FULLTEXT_DIR, key + ".json")
    if os.path.isfile(fp):
        try:
            text = (json.load(open(fp)).get("full_text") or "")
        except Exception:
            text = ""
    _FT_CACHE[key] = text
    return text


def _supported(numbers: list[str], paper: dict, outcome_nums: dict) -> bool:
    """Does the claimed number appear in title/abstract/full text/outcomes?"""
    hay = (paper.get("title", "") + " " + paper.get("abstract", "")).replace(",", "")
    key = paper.get("_key") or paper.get("key") or paper_key(paper)
    onums = outcome_nums.get(key, set())
    for n in numbers:
        norm = _normalize_number(n)
        if len(norm.replace(".", "")) < 2:
            continue
        if norm in hay or norm in onums:
            return True
    # lazy: only pull full text if abstract/outcomes didn't confirm
    ft = _fulltext_of(paper).replace(",", "")
    if ft:
        for n in numbers:
            norm = _normalize_number(n)
            if len(norm.replace(".", "")) >= 2 and norm in ft:
                return True
    return False


def _line_numbers(line: str) -> list[str]:
    return [t.strip() for t in _NUMBER_RE.findall(line) if _normalize_number(t)]


def _citations(line: str) -> list[tuple[str, str]]:
    """Return [(kind, identifier)] citations found on a line."""
    cites = []
    for m in _PMID_RE.findall(line):
        cites.append(("PMID", str(m)))
    for m in _KEY_RE.findall(line):
        cites.append(("key", m))
    for m in _DOI_RE.findall(line):
        cites.append(("doi", _norm_doi(m)))
    return cites


def verify_text(markdown: str, corpus: dict) -> dict:
    by_id = corpus["by_id"]
    outcome_nums = corpus["outcome_nums"]
    pmid_claims = []
    unsourced = []

    for lineno, raw in enumerate(markdown.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        cites = _citations(line)
        cite_ids = {c[1] for c in cites}
        numbers = [n for n in _line_numbers(line) if _normalize_number(n) not in cite_ids]
        lower = line.lower()
        is_claimish = any(m in lower for m in _CLAIM_MARKERS) and bool(numbers)

        if cites:
            seen = set()
            for kind, ident in cites:
                if ident in seen:
                    continue
                seen.add(ident)
                lookup = ident if kind != "doi" else _norm_doi(ident)
                paper = by_id.get(str(lookup))
                in_corpus = paper is not None
                supported = _supported(numbers, paper, outcome_nums) if (in_corpus and numbers) else None
                if not in_corpus:
                    status = "NOT_IN_CORPUS"
                elif not numbers:
                    status = "OK_NO_NUMBER"
                elif supported:
                    status = "SUPPORTED"
                else:
                    status = "NEEDS_REVIEW"
                pmid_claims.append({
                    "line": lineno, "pmid": f"{kind}:{ident}", "numbers": numbers,
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
    out.append(f"Cited claims: {len(claims)}  "
               f"(supported: {len(supported)}, needs review: {len(review)}, "
               f"not in corpus: {len(not_in)})")
    out.append(f"Unsourced numeric claims: {len(unsourced)}")
    out.append("")

    if not_in:
        out.append("─ NOT IN CORPUS (likely misattribution / external-knowledge leak) ─")
        for c in not_in:
            out.append(f"  L{c['line']}  {c['pmid']}  {c['numbers']}")
            out.append(f"         {c['text']}")
        out.append("")
    if review:
        out.append("─ NEEDS MANUAL REVIEW (in corpus, but number not found in text) ─")
        for c in review:
            out.append(f"  L{c['line']}  {c['pmid']}  {c['numbers']}")
            out.append(f"         claim: {c['text']}")
            out.append(f"         cited: {c['cited_title'][:120]}")
        out.append("")
    if unsourced:
        out.append("─ UNSOURCED NUMERIC CLAIMS (no citation on the line) ─")
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
