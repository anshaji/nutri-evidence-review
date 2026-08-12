"""Country-fit analysis over the deep-dive evidence database.

Answers CARE's "where" question from the corpus alone: which countries carry
enough country-specific evidence, across all three interventions, delivered
through government platforms, to be credible co-design candidates.

Deliberate methodological choices
---------------------------------
1. **Aggregate/regional tags are excluded from country counts.** A 42-country
   pooled Cochrane review is global evidence, not evidence *about* Ethiopia.
   Only clean single-country tags count toward a country's score. They are
   tallied separately as `aggregate_records` for transparency.

2. **Record volume is never the score.** Publication counts measure research
   attention, not scaling suitability — heavily-studied countries would win by
   default. Volume gates candidacy (a minimum evidence base per intervention);
   ranking is driven by implementation evidence and government-platform signal.

3. **Primary studies weigh more than reviews for country fit.** A program
   evaluation of an Ethiopian OTP tells you about Ethiopia; a global review
   tagged "Ethiopia" among 20 countries does not.

Run:  python3 CARE_review/code/country_analysis.py
Out:  CARE_review/data/country_analysis.json
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "CARE_review" / "data"
BLOCKS = ("cmam", "breastfeeding", "mms")

# --------------------------------------------------------------------------
# 1. Country-name normalisation
# --------------------------------------------------------------------------

# Name variants that must collapse to one country.
ALIASES = {
    "democratic republic of congo": "Democratic Republic of the Congo",
    "democratic republic of the congo": "Democratic Republic of the Congo",
    "dr congo": "Democratic Republic of the Congo",
    "drc": "Democratic Republic of the Congo",
    "cote d'ivoire": "Côte d'Ivoire",
    "côte d'ivoire": "Côte d'Ivoire",
    "ivory coast": "Côte d'Ivoire",
    "tanzania, united republic of": "Tanzania",
    "united republic of tanzania": "Tanzania",
    "viet nam": "Vietnam",
    "lao pdr": "Laos",
    "lao people's democratic republic": "Laos",
    "burma": "Myanmar",
    "the gambia": "Gambia",
    "bolivia (plurinational state of)": "Bolivia",
    "iran (islamic republic of)": "Iran",
    "syrian arab republic": "Syria",
    "republic of korea": "South Korea",
    "china, people's republic of": "China",
    "eswatini (swaziland)": "Eswatini",
    "swaziland": "Eswatini",
    "occupied palestinian territory": "Palestine",
    "timor leste": "Timor-Leste",
    "guinea bissau": "Guinea-Bissau",
    "papua new guinea ": "Papua New Guinea",
}

# Tokens that mark a tag as a region / aggregate / pooled description rather
# than a single country. Matched case-insensitively as substrings.
AGGREGATE_MARKERS = (
    "countries", "multi-country", "multiple", "region", "regional", "global",
    "sub-saharan", "subsaharan", "south asia", "southeast asia", "south-east asia",
    "east africa", "west africa", "central africa", "southern africa",
    "north africa", "latin america", "caribbean", "middle east", "asia-pacific",
    "lmic", "low- and middle", "low and middle", "high-income", "worldwide",
    "various", "pooled", "not specified", "not itemized", "not reported",
    "unclear", "n/a", "africa (", "asia (", "review of", "several",
)

# Bare region names that are exactly equal to the tag (not caught above).
BARE_REGIONS = {
    "africa", "asia", "europe", "americas", "oceania", "world", "international",
    "sub-saharan africa", "south asia", "global", "lmics", "lmic",
}


def normalise_country(raw: str) -> tuple[str | None, str]:
    """Return (canonical_country_or_None, kind).

    kind is one of: 'country', 'aggregate', 'empty'.
    """
    if not raw:
        return None, "empty"
    s = str(raw).strip().strip(".,;")
    if not s:
        return None, "empty"

    low = s.lower()

    # Long free-text descriptions are pooled/aggregate by construction.
    if len(s) > 30:
        return None, "aggregate"
    if low in BARE_REGIONS:
        return None, "aggregate"
    if any(m in low for m in AGGREGATE_MARKERS):
        return None, "aggregate"
    # Digits usually signal "42 countries", "118 LMICs", etc.
    if re.search(r"\d", s):
        return None, "aggregate"

    if low in ALIASES:
        return ALIASES[low], "country"

    # Title-case the tag but preserve internal capitals/apostrophes sensibly.
    canon = " ".join(w if w.isupper() else w.capitalize() for w in s.split())
    return canon, "country"


# --------------------------------------------------------------------------
# 2. Signals extracted from implementation findings
# --------------------------------------------------------------------------

# Evidence that delivery runs through an existing *government* platform at
# scale — the thing CARE's ask actually hinges on.
#
# NOTE: deliberately GENERIC. An earlier version also matched named national
# CHW cadres (ASHA, Anganwadi, Health Extension Worker, Lady Health Worker...).
# That biased the ranking toward whichever countries' cadres happened to be
# listed — India took the top rank on 9/12 cadre-name hits versus Malawi's
# 1/12. Since the list of names is an artifact of the author, not of the
# evidence, named cadres are excluded from scoring and used only as
# qualitative profile evidence (see NAMED_CADRES below).
PLATFORM_PATTERNS = re.compile(
    r"("
    r"\bnational(?:ly)?\s+(?:scale|programme|program|policy|coverage|rollout|roll-out|guideline|level)"
    r"|\bgovernment[- ](?:led|run|owned|delivered|managed|implemented|supported|operated)"
    r"|\bministry of health|\bmoh\b|\bpublic[- ]sector|\bstate[- ]run"
    r"|\bintegrated into (?:routine|national|government|existing)"
    r"|\broutine (?:health )?system|\bscale[- ]up|\bscaled up"
    r"|\bexisting (?:health )?(?:system|infrastructure|platform)"
    r"|\bhealth system strengthening"
    r")",
    re.I,
)

# Named national community-health cadres. NOT scored — used to describe a
# country's platform qualitatively in its profile, where naming the actual
# cadre is what makes the profile useful.
NAMED_CADRES = re.compile(
    r"("
    r"health extension worker|hew\b|women'?s development army"
    r"|accredited social health activist|asha\b|anganwadi|icds\b"
    r"|anemia mukt bharat|poshan|lady health worker|lhw\b"
    r"|health surveillance assistant|hsa\b|community health volunteer|chv\b"
    r"|health surveillance|female community health volunteer|fchv\b"
    r"|community health extension worker|chew\b"
    r")",
    re.I,
)

# Evidence of a measured shortfall — i.e. headroom for an intervention to matter.
GAP_PATTERNS = re.compile(
    r"\b("
    r"below (?:the )?(?:sphere|target|standard|minimum|who)"
    r"|did not (?:meet|reach)|fell short|shortfall|underperform"
    r"|low (?:coverage|adherence|uptake|compliance)"
    r"|stock[- ]?out|dropout|drop[- ]out|default(?:er|ing)?"
    r"|lost to follow[- ]up|ltfu\b"
    r"|gap\b|barrier|not achiev|inadequate|insufficient|suboptimal"
    r")\b",
    re.I,
)

IMPL_DIMENSIONS = ("coverage", "adherence", "scalability", "delivery_platform",
                   "barriers", "equity")

# Study designs that constitute country-specific implementation evidence
# (as opposed to a global review that happens to name the country).
PRIMARY_DESIGNS = {
    "Program evaluation", "RCT", "Cohort", "Cross-sectional",
    "Non-randomised trial", "Qualitative", "Case-control",
}

# A record tagged with many countries is evidence *mentioning* a country, not
# evidence *about* it. Left uncontrolled this badly distorts the ranking: the
# multi-country CHW review that describes Ethiopia's Health Extension Programme
# is tagged with 9 countries, so it was crediting Malawi, Kenya and Pakistan
# with Ethiopia's national-platform evidence. Implementation signals are
# therefore counted only from records at or below this tag count (70% of tagged
# records are single-country; 76% are <=3). Multi-country records still count
# toward a country's record breadth.
COUNTRY_SPECIFIC_MAX_TAGS = 3


def load_records() -> list[dict]:
    path = DATA / "evidence_db.json"
    if not path.exists():
        sys.exit(f"missing {path} — run the extraction pipeline first")
    return [r for r in json.loads(path.read_text()) if r.get("on_topic")]


def build() -> dict:
    records = load_records()

    countries: dict[str, dict] = defaultdict(lambda: {
        "records": 0,
        "country_specific_records": 0,
        "multi_country_records": 0,
        "by_block": Counter(),
        "primary_studies": 0,
        "program_evaluations": 0,
        "impl_findings": 0,
        "impl_by_dimension": Counter(),
        "platform_hits": 0,
        "gap_hits": 0,
        "platform_quotes": [],
        "gap_quotes": [],
        "cadre_quotes": [],
        "cadres_named": Counter(),
        "record_keys": [],
    })

    aggregate_records = 0
    untagged_records = 0

    for rec in records:
        raw_tags = rec.get("countries") or []
        if isinstance(raw_tags, str):
            raw_tags = [raw_tags]

        resolved, saw_aggregate = [], False
        for tag in raw_tags:
            canon, kind = normalise_country(tag)
            if kind == "country" and canon:
                resolved.append(canon)
            elif kind == "aggregate":
                saw_aggregate = True

        if not resolved:
            if saw_aggregate:
                aggregate_records += 1
            else:
                untagged_records += 1
            continue

        block = rec.get("deepdive_block")
        design = rec.get("study_design")
        findings = rec.get("implementation_findings") or []
        unique = list(dict.fromkeys(resolved))  # de-dupe within a record
        country_specific = len(unique) <= COUNTRY_SPECIFIC_MAX_TAGS

        for country in unique:
            c = countries[country]
            c["records"] += 1
            c["by_block"][block] += 1
            c["record_keys"].append(rec.get("key"))
            if design in PRIMARY_DESIGNS:
                c["primary_studies"] += 1
            if design == "Program evaluation":
                c["program_evaluations"] += 1

            if not country_specific:
                c["multi_country_records"] += 1
                continue  # counts toward breadth, not toward signals
            c["country_specific_records"] += 1

            for f in findings:
                dim = f.get("dimension")
                text = f"{f.get('finding', '')} {f.get('value', '')}"
                c["impl_findings"] += 1
                if dim in IMPL_DIMENSIONS:
                    c["impl_by_dimension"][dim] += 1
                if PLATFORM_PATTERNS.search(text):
                    c["platform_hits"] += 1
                    if len(c["platform_quotes"]) < 12:
                        c["platform_quotes"].append({
                            "key": rec.get("key"), "block": block,
                            "dimension": dim, "text": text.strip()[:400],
                        })
                if GAP_PATTERNS.search(text):
                    c["gap_hits"] += 1
                    if len(c["gap_quotes"]) < 12:
                        c["gap_quotes"].append({
                            "key": rec.get("key"), "block": block,
                            "dimension": dim, "text": text.strip()[:400],
                        })
                # Qualitative only — never scored.
                for m in NAMED_CADRES.finditer(text):
                    c["cadres_named"][m.group(0).lower()] += 1
                    if len(c["cadre_quotes"]) < 10:
                        c["cadre_quotes"].append({
                            "key": rec.get("key"), "block": block,
                            "dimension": dim, "text": text.strip()[:400],
                        })

    # ---------------------------------------------------------------- scoring
    # Candidacy gate: real evidence in every one of the three interventions,
    # and enough country-specific primary work to say anything operational.
    MIN_PER_BLOCK = 5
    MIN_PRIMARY = 10

    for name, c in countries.items():
        blocks_covered = sum(1 for b in BLOCKS if c["by_block"].get(b, 0) > 0)
        blocks_at_min = sum(1 for b in BLOCKS if c["by_block"].get(b, 0) >= MIN_PER_BLOCK)
        c["blocks_covered"] = blocks_covered
        c["blocks_at_min"] = blocks_at_min
        c["eligible"] = blocks_at_min == 3 and c["primary_studies"] >= MIN_PRIMARY
        c["balance"] = round(
            min(c["by_block"].get(b, 0) for b in BLOCKS)
            / max(1, max(c["by_block"].get(b, 0) for b in BLOCKS)), 3)
        c["by_block"] = dict(c["by_block"])
        c["impl_by_dimension"] = dict(c["impl_by_dimension"])
        c["cadres_named"] = dict(c["cadres_named"].most_common(8))
        c["record_keys"] = c["record_keys"][:60]

    eligible = {k: v for k, v in countries.items() if v["eligible"]}

    def scale(vals: dict[str, float]) -> dict[str, float]:
        hi = max(vals.values()) if vals else 1
        return {k: (v / hi if hi else 0) for k, v in vals.items()}

    # Four transparent components, each normalised to the strongest candidate.
    s_platform = scale({k: v["platform_hits"] for k, v in eligible.items()})
    s_impl = scale({k: v["impl_findings"] for k, v in eligible.items()})
    s_primary = scale({k: v["primary_studies"] for k, v in eligible.items()})
    s_gap = scale({k: v["gap_hits"] for k, v in eligible.items()})

    for name, c in eligible.items():
        components = {
            "government_platform": round(s_platform[name] * 35, 1),
            "implementation_depth": round(s_impl[name] * 25, 1),
            "country_specific_primary_evidence": round(s_primary[name] * 20, 1),
            "documented_performance_gap": round(s_gap[name] * 10, 1),
            "cross_intervention_balance": round(c["balance"] * 10, 1),
        }
        c["score_components"] = components
        c["score"] = round(sum(components.values()), 1)

    ranked = sorted(eligible.items(), key=lambda kv: -kv[1]["score"])

    return {
        "meta": {
            "on_topic_records": len(records),
            "records_with_country_tag": sum(1 for r in records
                                            if any(normalise_country(t)[1] == "country"
                                                   for t in (r.get("countries") or []))),
            "records_aggregate_only": aggregate_records,
            "records_untagged": untagged_records,
            "distinct_countries": len(countries),
            "eligible_countries": len(eligible),
            "gate": {
                "min_records_per_intervention": MIN_PER_BLOCK,
                "min_primary_studies": MIN_PRIMARY,
            },
            "score_weights": {
                "government_platform": 35,
                "implementation_depth": 25,
                "country_specific_primary_evidence": 20,
                "documented_performance_gap": 10,
                "cross_intervention_balance": 10,
            },
            "not_scored_here": [
                "fragility, conflict and security",
                "CARE / IA operational footprint and partnerships",
                "government appetite and current policy windows",
                "donor and financing landscape",
                "cost and cost-effectiveness (deferred to Phase 2)",
            ],
        },
        "ranked": [{"country": k, **v} for k, v in ranked],
        "all_countries": {k: v for k, v in sorted(
            countries.items(), key=lambda kv: -kv[1]["records"])},
    }


def main() -> None:
    result = build()
    out = DATA / "country_analysis.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False))

    m = result["meta"]
    print(f"on-topic records          {m['on_topic_records']}")
    print(f"  with a country tag      {m['records_with_country_tag']}")
    print(f"  aggregate/regional only {m['records_aggregate_only']}")
    print(f"  untagged                {m['records_untagged']}")
    print(f"distinct countries        {m['distinct_countries']}")
    print(f"eligible candidates       {m['eligible_countries']}"
          f"  (>={m['gate']['min_records_per_intervention']}/intervention,"
          f" >={m['gate']['min_primary_studies']} primary studies)")
    print()
    hdr = f"{'':2} {'country':<18} {'score':>6} {'cmam':>5} {'bf':>4} {'mms':>4} " \
          f"{'own':>5} {'multi':>6} {'prim':>5} {'impl':>5} {'plat':>5} {'gap':>4}"
    print(hdr)
    print("-" * len(hdr))
    for i, row in enumerate(result["ranked"], 1):
        b = row["by_block"]
        print(f"{i:>2} {row['country']:<18} {row['score']:>6} "
              f"{b.get('cmam', 0):>5} {b.get('breastfeeding', 0):>4} {b.get('mms', 0):>4} "
              f"{row['country_specific_records']:>5} {row['multi_country_records']:>6} "
              f"{row['primary_studies']:>5} {row['impl_findings']:>5} "
              f"{row['platform_hits']:>5} {row['gap_hits']:>4}")
    print("\n'own' = country-specific records (<=3 country tags); signals counted from these only."
          "\n'multi' = multi-country records: count toward breadth, excluded from signals.")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
