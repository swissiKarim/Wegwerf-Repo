# scenario-id: S1/SC-3
"""CLI: Brutto-Grenzwert 0 → net_payout 0.0, Exit-Code 0"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py", "--brutto", "0"],
    capture_output=True, text=True
)
data = json.loads(result.stdout.strip())
print(json.dumps({"exit_code": result.returncode, "stdout": data}))
