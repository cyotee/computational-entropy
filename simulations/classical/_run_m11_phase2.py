#!/usr/bin/env python3
"""Convenience: run all M11 Phase 2 ledgers back-to-back (stdlib only)."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "m11_multistep_boolean_ledger.py",
    "m11_tiny_lambda_ledger.py",
    "m11_minimal_shoe_ledger.py",
)


def main() -> int:
    for name in SCRIPTS:
        path = ROOT / name
        print(f"\n>>> running {name}\n")
        try:
            runpy.run_path(str(path), run_name="__main__")
        except SystemExit as e:
            code = e.code if isinstance(e.code, int) else 1
            if code:
                print(f"FAIL {name} exit={code}", file=sys.stderr)
                return code
        except Exception as e:
            print(f"FAIL {name}: {e}", file=sys.stderr)
            raise
    print("\nAll M11 Phase 2 ledgers exited cleanly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
