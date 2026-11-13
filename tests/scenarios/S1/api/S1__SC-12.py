# scenario-id: S1/SC-12
"""HTTP: POST /payout mit brutto als String → 400, ok:false"""
import json, os, urllib.request, urllib.error

base = os.environ.get("ASB_API_BASE") or os.environ.get("ASB_SVC_WEB_URL", "http://127.0.0.1:8080")
base = base.rstrip("/")

req = urllib.request.Request(
    f"{base}/payout",
    data=json.dumps({"brutto": "1000"}).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
try:
    with urllib.request.urlopen(req) as resp:
        status = resp.status
        body = json.loads(resp.read())
except urllib.error.HTTPError as e:
    status = e.code
    body = json.loads(e.read())

print(json.dumps({"status": status, "body": body}))
