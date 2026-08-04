#!/usr/bin/env python3
"""Parse per-intervention ratings from the synthesis section files.

The synthesis agents write each section with a two-line header:
    ## <display name>  (<population>)
    **Evidence: A  |  Cost-effectiveness: Moderate  |  Scalability: ...  |  Tier 1**

This reads every data/synthesis_sections/*.md and reconstructs
data/synthesis_ratings.json for the assembler — robust to any workflow return
that failed mid-response (the .md file on disk is the source of truth).

Usage: python3 code/26_extract_ratings.py
"""

import json
import os
import re

SECTIONS = "./data/synthesis_sections"
OUT = "./data/synthesis_ratings.json"

_TITLE = re.compile(r"^##\s+(.*?)\s*(?:\(([^)]*)\)\s*)?$")
_RATE = re.compile(
    r"Evidence:\s*([ABC])\b.*?Cost-?effectiveness:\s*(Very High|High|Moderate|Unknown)\b"
    r".*?Scalability:\s*(.*?)\s*(?:\||\*\*).*?Tier\s*(\d)",
    re.IGNORECASE | re.DOTALL)


def main():
    ratings = []
    for fn in sorted(os.listdir(SECTIONS)):
        if not fn.endswith(".md"):
            continue
        cat = fn[:-3]
        text = open(os.path.join(SECTIONS, fn), encoding="utf-8").read()
        # title = first '## ' heading
        display, population = cat, ""
        for line in text.splitlines():
            if line.startswith("## "):
                m = _TITLE.match(line.strip())
                if m:
                    display = m.group(1).strip()
                    population = (m.group(2) or "").strip()
                break
        m = _RATE.search(text)
        if not m:
            print(f"  [warn] no rating header parsed in {fn}")
            ev, ce, scal, tier = "C", "Unknown", "", 3
        else:
            ev, ce, scal, tier = m.group(1).upper(), m.group(2), m.group(3).strip(), int(m.group(4))
        ratings.append({
            "category": cat,
            "display_name": display,
            "population": population,
            "evidence_grade": ev,
            "cost_effectiveness": ce,
            "scalability": scal,
            "tier": tier,
            "section_path": os.path.join(SECTIONS, fn),
        })
    json.dump(ratings, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(f"Parsed {len(ratings)} section ratings → {OUT}")
    from collections import Counter
    print("  tiers:", dict(sorted(Counter(r['tier'] for r in ratings).items())))
    print("  evidence:", dict(sorted(Counter(r['evidence_grade'] for r in ratings).items())))
    print("  cost-eff:", dict(Counter(r['cost_effectiveness'] for r in ratings)))


if __name__ == "__main__":
    main()
