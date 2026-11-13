# scenario-id: S1/SC-2
"""CLI: stdout enthält genau ein JSON-Objekt (kein extra Output)"""
import json, subprocess, sys

result = subprocess.run(
    [sys.executable, "payout_cli.py", "--brutto", "1000"],
    capture_output=True, text=True
)
lines = [l for l in result.stdout.splitlines() if l.strip()]
data = json.loads(lines[0]) if lines else {}
print(json.dumps({"stdout_line_count": len(lines), "stdout": data}))
