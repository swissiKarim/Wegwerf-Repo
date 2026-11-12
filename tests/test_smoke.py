"""Smoke tests that stay green on stubs and after real payout implementation."""

from __future__ import annotations

import json


def test_imports():
    import app
    import payout_cli

    assert hasattr(app, "Handler")
    assert hasattr(app, "serve")
    assert hasattr(payout_cli, "compute_net_payout")
    assert hasattr(payout_cli, "main")


def test_health_handler_ok():
    from app import Handler

    class _W:
        def __init__(self):
            self.chunks = []

        def write(self, b: bytes) -> None:
            self.chunks.append(b)

    class Fake(Handler):
        def __init__(self):
            self.path = "/health"
            self.wfile = _W()
            self._headers = []

        def send_response(self, code):
            self.code = code

        def send_header(self, k, v):
            self._headers.append((k, v))

        def end_headers(self):
            pass

    h = Fake()
    h.do_GET()
    assert h.code == 200
    body = json.loads(b"".join(h.wfile.chunks).decode())
    assert body.get("ok") is True
