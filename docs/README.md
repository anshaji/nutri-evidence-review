# Documentation index

Read in this order depending on what you need.

## Understand the method

| Document | What it covers |
|---|---|
| [PROCESS_main_pipeline.md](PROCESS_main_pipeline.md) | The core two-phase pipeline (v3) — retrieval, dedup, scoring, full text, Phase-2 cost-effectiveness, synthesis, verification. Includes the VAS validation audit that motivated the design. |
| [PROCESS_deepdive.md](PROCESS_deepdive.md) | The CARE/ScaleWorks deep-dive layer — PICOS-targeted retrieval, the implementation pass, the extended extraction schema, and the stage-by-stage funnel. Read the main pipeline doc first. |
| [PICOS_specification.md](PICOS_specification.md) | The PICOS framework for the three deep-dive interventions (CMAM, breastfeeding, MMS), the dual clinical + implementation outcome axis, and the scoping decisions on record. |

## Find the deliverables

| Location | Contents |
|---|---|
| `../CARE_review/` | Partner-facing outputs — the deep-dive review and the workplan. |
| `../output/` | Synthesis documents from the main pipeline (current), with superseded renders under `output/archive/`. |

## Run it

Commands live in the root [README.md](../README.md) and in each process document's
"Running" / "Reproducing the run" section. Repo conventions and architecture notes
are in [claude.md](../claude.md); live task state is in [task.md](../task.md).

## A note on the numbering

Files in `code/` are prefixed by execution order (`01_config` → `31_validate`).
The prefix is positional, not a version: `19`–`26` are the full-corpus extension,
`27`–`30` are the deep-dive layer, and `31` is a post-hoc validator. Python cannot
import a module whose name starts with a digit, so `code/__init__.py` registers
clean aliases (`code.config`, `code.deepdive`, …) — import those, not the filenames.
