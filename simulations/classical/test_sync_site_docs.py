"""Tests for scripts/sync_site_docs.py — real entry path used by CI."""

from __future__ import annotations

import importlib.util
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


def _load_sync_module():
    spec = importlib.util.spec_from_file_location("sync_site_docs", SYNC)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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


def test_normalize_math_fixes_spaced_inline_and_same_line_display():
    """Spaced $  expr  $ and same-line $$...$$ must become Arithmatex-friendly."""
    mod = _load_sync_module()
    raw = (
        "A stochastic map $  p(Y|X)  $ and $  p_Y  $.\n"
        "$$H_c(f; p_X) := H(Y)$$\n"
    )
    out = mod.normalize_math(raw)
    assert "$p(Y|X)$" in out, out
    assert "$p_Y$" in out, out
    assert "$$H_c" not in out.replace("$$\nH_c", "")  # not same-line
    assert "$$\nH_c(f; p_X) := H(Y)\n$$" in out, out


def test_built_foundations_page_wraps_stochastic_math():
    """After sync+mkdocs, p(Y|X) must be inside arithmatex, not raw $...$."""
    subprocess.run([sys.executable, str(SYNC)], cwd=REPO, check=True)
    build = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "-q"],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    assert build.returncode == 0, build.stderr
    html = (REPO / "site/foundations/computational-entropy/index.html").read_text(
        encoding="utf-8"
    )
    assert "stochastic map" in html
    # Must not leave the classic broken raw form
    assert "$  p(Y|X)  $" not in html
    assert "$p(Y|X)$" not in html or "arithmatex" in html
    assert 'class="arithmatex"' in html
    assert "p(Y|X)" in html
    # Prefer wrapped form
    assert "\\(p(Y|X)\\)" in html or "\\( p(Y|X) \\)" in html or (
        'class="arithmatex"' in html and "p(Y|X)" in html
    )


if __name__ == "__main__":
    test_normalize_math_fixes_spaced_inline_and_same_line_display()
    test_sync_script_exits_zero_and_writes_allowlist()
    test_denylisted_paths_not_under_docs_from_sync()
    test_built_foundations_page_wraps_stochastic_math()
    print("OK: sync_site_docs tests passed")
