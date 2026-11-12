#!/bin/bash
set -euo pipefail
# Image agentsphere/sandbox-polyglot has pytest but NOT ruff (checked 2026-11-12).
echo 'lint_skipped: ruff not installed in sandbox-polyglot; no alternate linter pinned'
exit 0
