# scenario-id: S1/SC-10
"""CLI: Negativer Wert (--brutto -1) → Exit-Code 2, ok:false"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py", "--brutto", "-1"],
    capture_output=True, text=True
)
try:
    data = json.loads(result.stdout.strip())
except Exception:
    data = {"ok": False, "error": "no output"}
print(json.dumps({"exit_code": result.returncode, "stdout": data}))
