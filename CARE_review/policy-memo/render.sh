#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 make_memo_figures.py >/dev/null && echo "figure rebuilt"
pandoc SCALEWORKS_MEMO.md \
  --from=markdown+pipe_tables+yaml_metadata_block+implicit_figures \
  --reference-doc=../code/assets/reference.docx --standalone --resource-path=. \
  -o SCALEWORKS_MEMO.docx && echo "rendered SCALEWORKS_MEMO.docx"
