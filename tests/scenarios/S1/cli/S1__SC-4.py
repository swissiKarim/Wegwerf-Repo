# scenario-id: S1/SC-4
"""CLI: Nachkommabrutto (100.5) → net_payout korrekt gerundet (85.43)"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py", "--brutto", "100.5"],
    capture_output=True, text=True
)
data = json.loads(result.stdout.strip())
print(json.dumps({"exit_code": result.returncode, "stdout": data}))
