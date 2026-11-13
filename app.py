"""Minimal HTTP app (stdlib only). Payout brutto→netto."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from payout_cli import compute_net_payout


HOST = "127.0.0.1"
PORT = 8080


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:  # quieter lab logs
        return

    def _send(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path.split("?", 1)[0] == "/health":
            self._send(200, {"ok": True})
            return
        self._send(404, {"ok": False, "error": "not_found"})

    def do_POST(self) -> None:  # noqa: N802
        if self.path.split("?", 1)[0] != "/payout":
            self._send(404, {"ok": False, "error": "not_found"})
            return

        # Read body
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b""

        # Parse JSON
        try:
            data = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            self._send(400, {"ok": False, "error": "invalid JSON"})
            return

        # Validate brutto field
        if "brutto" not in data:
            self._send(400, {"ok": False, "error": "missing field: brutto"})
            return

        brutto = data["brutto"]
        if not isinstance(brutto, (int, float)) or isinstance(brutto, bool):
            self._send(400, {"ok": False, "error": "brutto must be a number"})
            return

        if brutto < 0:
            self._send(400, {"ok": False, "error": "brutto must be >= 0"})
            return

        net = compute_net_payout(float(brutto))
        self._send(200, {"ok": True, "brutto": brutto, "net_payout": net})


def serve(host: str = HOST, port: int = PORT) -> None:
    httpd = ThreadingHTTPServer((host, port), Handler)
    httpd.serve_forever()


if __name__ == "__main__":
    serve()
