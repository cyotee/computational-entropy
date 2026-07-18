#!/usr/bin/env bash
# Shared local/CI entry: sync allowlist then mkdocs build.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
PYTHON="${PYTHON:-python3}"
if [[ -x "$ROOT/.venv/bin/python" ]]; then
  PYTHON="$ROOT/.venv/bin/python"
fi
"$PYTHON" scripts/sync_site_docs.py
"$PYTHON" -m mkdocs build "$@"
