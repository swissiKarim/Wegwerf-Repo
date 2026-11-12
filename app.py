"""Minimal HTTP app (stdlib only). Stubs — Developer must implement payout."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


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
        # STUB: real story requires brutto→netto JSON body.
        length = int(self.headers.get("Content-Length") or 0)
        _ = self.rfile.read(length) if length else b""
        self._send(
            501,
            {
                "ok": False,
                "error": "not_implemented",
                "hint": "implement brutto to netto payout",
            },
        )


def serve(host: str = HOST, port: int = PORT) -> None:
    httpd = ThreadingHTTPServer((host, port), Handler)
    httpd.serve_forever()


if __name__ == "__main__":
    serve()
