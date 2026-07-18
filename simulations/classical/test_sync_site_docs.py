"""Tests for scripts/sync_site_docs.py — real entry path used by CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SYNC = REPO / "scripts" / "sync_site_docs.py"
DOCS = REPO / "docs"

EXPECTED_PAGES = [
    "foundations/computational-entropy.md",
    "emergent-gravity/master-equation.md",
    "emergent-gravity/newtonian-recovery.md",
    "synthesis/claims.md",
    "synthesis/conclusions.md",
    "synthesis/open-avenues.md",
    "papers/final-report.md",
    "papers/publishable.md",
    "glossary.md",
    "progress.md",
]


def test_sync_script_exits_zero_and_writes_allowlist():
    """Run the real sync CLI; require exit 0 and allowlisted outputs."""
    assert SYNC.is_file(), f"missing {SYNC}"
    proc = subprocess.run(
        [sys.executable, str(SYNC)],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, (
        f"sync failed ({proc.returncode})\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}"
    )
    for rel in EXPECTED_PAGES:
        path = DOCS / rel
        assert path.is_file(), f"expected synced page missing: {path}"
        assert path.stat().st_size > 0, f"empty synced page: {path}"


def test_denylisted_paths_not_under_docs_from_sync():
    """After sync, denylisted research dumps must not appear as site pages."""
    subprocess.run([sys.executable, str(SYNC)], cwd=REPO, check=True)
    forbidden_names = {
        "CLAUDE.md",
        "PRD.md",
    }
    for path in DOCS.rglob("*"):
        if path.is_file():
            assert path.name not in forbidden_names, f"denylisted name present: {path}"
            assert "external" not in path.parts or path.suffix != ".pdf", path
            # No wholesale drafts/archive trees under docs
            assert "drafts" not in path.parts
            assert "archive" not in path.parts


if __name__ == "__main__":
    test_sync_script_exits_zero_and_writes_allowlist()
    test_denylisted_paths_not_under_docs_from_sync()
    print("OK: sync_site_docs tests passed")
