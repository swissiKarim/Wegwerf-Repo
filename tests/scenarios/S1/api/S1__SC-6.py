# scenario-id: S1/SC-6
"""HTTP: GET /health → 200"""
import json, os, urllib.request

base = os.environ.get("ASB_API_BASE") or os.environ.get("ASB_SVC_WEB_URL", "http://127.0.0.1:8080")
base = base.rstrip("/")

req = urllib.request.Request(f"{base}/health", method="GET")
with urllib.request.urlopen(req) as resp:
    status = resp.status
    body = json.loads(resp.read())

print(json.dumps({"status": status, "body": body}))
