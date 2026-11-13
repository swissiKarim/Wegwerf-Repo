# scenario-id: S1/SC-8
"""CLI: Fehlendes --brutto → Exit-Code 2, ok:false"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py"],
    capture_output=True, text=True
)
# stdout may have JSON; if not, construct error response
try:
    data = json.loads(result.stdout.strip())
except Exception:
    data = {"ok": False, "error": "no output"}
print(json.dumps({"exit_code": result.returncode, "stdout": data}))
