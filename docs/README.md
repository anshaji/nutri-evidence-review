# Documentation index

## Core pipeline

| Document | What it covers |
|---|---|
| [PROCESS_main_pipeline.md](PROCESS_main_pipeline.md) | The two-phase pipeline (v3) — retrieval, dedup, scoring, full text, Phase-2 cost-effectiveness, synthesis, verification. Includes the VAS validation audit that motivated the design. |
| [../claude.md](../claude.md) | Architecture, module map, scoring components, known gotchas. |

## CARE / ScaleWorks deep-dive

That workstream is **self-contained in [`../CARE_review/`](../CARE_review/)** —
deliverables, method docs, prompts, and its working dataset all live together.

| Document | What it covers |
|---|---|
| [../CARE_review/README.md](../CARE_review/README.md) | **Start here** — index for the whole CARE workstream. |
| [../CARE_review/docs/PICOS_specification.md](../CARE_review/docs/PICOS_specification.md) | PICOS per intervention, dual clinical + implementation outcome axis, scoping decisions. |
| [../CARE_review/docs/PROCESS_deepdive.md](../CARE_review/docs/PROCESS_deepdive.md) | The deep-dive method end to end. Read the main pipeline doc above first. |

## Where things live

| Location | Contents |
|---|---|
| `../code/` | Pipeline package, numbered by execution order |
| `../prompts/` | Core pipeline prompts (shortlist, synthesis, extraction) |
| `../CARE_review/` | The CARE workstream — everything, including its data |
| `../data/` | Core pipeline data + `fulltext/` (shared with the deep-dive) |
| `../output/` | Main-pipeline synthesis documents; superseded renders in `output/archive/` |

## A note on the numbering

Files in `code/` are prefixed by execution order (`01_config` → `31_validate`).
The prefix is positional, not a version: `19`–`26` are the full-corpus extension,
`27`–`30` are the deep-dive layer, and `31` is a post-hoc validator. Python cannot
import a module whose name starts with a digit, so `code/__init__.py` registers
clean aliases (`code.config`, `code.deepdive`, …) — import those, not the filenames.
