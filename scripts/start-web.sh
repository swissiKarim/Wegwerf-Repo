#!/bin/bash
set -euo pipefail
exec python3 -c 'from app import serve; serve()'
