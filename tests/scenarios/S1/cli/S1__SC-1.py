# scenario-id: S1/SC-1
"""CLI: --brutto 1000 → net_payout 850.0, Exit-Code 0"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py", "--brutto", "1000"],
    capture_output=True, text=True
)
data = json.loads(result.stdout.strip())
print(json.dumps({"exit_code": result.returncode, "stdout": data}))
