#!/usr/bin/env bash
# Render the CMAM policy report. CMAM_REPORT.md is the single source of truth.
set -euo pipefail
cd "$(dirname "$0")"
pandoc CMAM_REPORT.md \
  --from=markdown+pipe_tables+yaml_metadata_block \
  --reference-doc=../code/assets/reference.docx --toc --toc-depth=2 --standalone \
  -o CMAM_REPORT.docx && echo "rendered CMAM_REPORT.docx"
