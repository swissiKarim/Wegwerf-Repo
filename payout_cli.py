#!/usr/bin/env python3
"""CLI payout (stdlib). Prints one JSON object on stdout."""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, ROUND_HALF_UP


def compute_net_payout(brutto: float) -> float:
    """Return netto = brutto × 0.85, rounded to 2 decimal places (ROUND_HALF_UP)."""
    result = (Decimal(str(brutto)) * Decimal("0.85")).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
    return float(result)


class _SilentParser(argparse.ArgumentParser):
    """Override error() so we can emit our own JSON error on stdout."""

    def error(self, message: str) -> None:  # type: ignore[override]
        print(json.dumps({"ok": False, "error": message}), flush=True)
        sys.exit(2)


def main(argv: list[str] | None = None) -> int:
    parser = _SilentParser(description="Payout CLI")
    parser.add_argument("--brutto", type=float, default=None)
    args = parser.parse_args(argv)

    # Validate: --brutto must be present
    if args.brutto is None:
        print(json.dumps({"ok": False, "error": "missing --brutto"}), flush=True)
        return 2

    # Validate: must be non-negative
    if args.brutto < 0:
        print(json.dumps({"ok": False, "error": "brutto must be >= 0"}), flush=True)
        return 2

    net = compute_net_payout(args.brutto)
    print(json.dumps({"ok": True, "brutto": args.brutto, "net_payout": net}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
