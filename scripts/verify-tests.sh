#!/bin/bash
set -euo pipefail
mkdir -p .agentsphere/reports
python3 -m pytest --junitxml=.agentsphere/reports/junit.xml
