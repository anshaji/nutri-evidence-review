# Optional CEA registry data (Phase 2)

Phase 2 (`run_cea.py`) always searches PubMed + OpenAlex for cost-effectiveness
evidence per shortlisted intervention. As an **optional** enrichment it will also
match each intervention against a local cost-effectiveness registry CSV, if you
provide one here. If no file is present, Phase 2 runs fine on the search backbone
alone — it just reports zero registry matches.

## Why this is a manual download

A research spike confirmed that neither major global-health CEA source exposes a
programmatic API reachable from this stdlib-only pipeline:

- **Tufts / CEVR Global Health CEA Registry** — the download page
  (`cear.tuftsmedicalcenter.org/registry/download`) is a client-side JavaScript
  app; `urllib` only receives an empty "Loading…" shell. Advanced/bulk export is
  behind subscriber access. The legacy `ghcearegistry.org` download host refuses
  connections.
- **DCP3 (Disease Control Priorities, 3rd ed.)** — cost-effectiveness data lives
  in **Annex 7A**, distributed as a PDF/HTML supplement off `dcp-3.org`. Not
  machine-readable.

So the registry is a one-time human download, not a live fetch.

## How to add a registry file

### GHCEA / CEA Registry → `data/ghcea_registry.csv`
1. Visit <https://cear.tuftsmedicalcenter.org/registry/download>.
2. Export the global-health / cost-per-DALY subset to CSV.
3. Save it as `data/ghcea_registry.csv`.

### DCP3 Annex 7A (optional) → `data/dcp3_annex7a.csv`
1. Open the DCP3 economic-evaluation annex (Annex 7A) from <https://dcp-3.org>.
2. Extract the cost-effectiveness table into a CSV.
3. Save it as `data/dcp3_annex7a.csv`.

## Expected columns

The loader (`code/13_ghcea_registry.py`) is tolerant of column-name variation
via an alias map. It recognizes (case-insensitive):

| Canonical field | Accepted column headers |
|-----------------|-------------------------|
| `intervention`  | Intervention, Intervention Name, Title, Description |
| `country`       | Country, Countries |
| `cost_per_daly` | Cost per DALY, Cost/DALY, ICER |
| `year`          | Year, Publication Year |
| `reference`     | Reference, Citation, Author |

Unknown columns are preserved under `_raw` and still searched during matching.

## Note

These CSVs are gitignored (`data/*.csv`) — they are not redistributed with the
repo. This README and the `data/` directory are tracked so the path exists.
