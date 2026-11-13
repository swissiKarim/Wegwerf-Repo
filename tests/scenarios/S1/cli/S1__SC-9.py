# scenario-id: S1/SC-9
"""CLI: Ungültiger Wert (--brutto abc) → Exit-Code 2, ok:false"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py", "--brutto", "abc"],
    capture_output=True, text=True
)
try:
    data = json.loads(result.stdout.strip())
except Exception:
    data = {"ok": False, "error": "no output"}
print(json.dumps({"exit_code": result.returncode, "stdout": data}))
