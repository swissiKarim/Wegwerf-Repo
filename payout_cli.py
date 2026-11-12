#!/usr/bin/env python3
"""CLI payout stub (stdlib). Prints one JSON object on stdout when implemented."""

from __future__ import annotations

import argparse
import json
import sys


def compute_net_payout(brutto: float) -> float:
    """STUB — Developer must implement brutto→netto (e.g. fixed tax/fee rules)."""
    raise NotImplementedError("payout not implemented: compute net from brutto")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Payout CLI (lab stub)")
    parser.add_argument("--brutto", type=float, required=True)
    args = parser.parse_args(argv)
    try:
        net = compute_net_payout(args.brutto)
    except NotImplementedError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), flush=True)
        return 2
    print(json.dumps({"ok": True, "brutto": args.brutto, "net_payout": net}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
