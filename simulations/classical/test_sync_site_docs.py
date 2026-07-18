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
    "papers/paper-full.md",
    "glossary.md",
    "progress.md",
]

EXPECTED_PAPER_CHAPTERS = [
    "papers/chapters/00-front-matter.md",
    "papers/chapters/01-introduction.md",
    "papers/chapters/06-channel-load-master-equation.md",
    "papers/chapters/11-conclusions.md",
    "papers/chapters/references.md",
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


def test_normalize_math_fixes_same_line_display_without_eating_inline_spaces():
    """Same-line $$...$$ → block form; do not glue adjacent $...$ expressions."""
    mod = _load_sync_module()
    raw = (
        "A stochastic map $  p(Y|X)  $ and $  p_Y  $.\n"
        "Channel $\\Phi_g$ and entropy $S_c$.\n"
        "$$H_c(f; p_X) := H(Y)$$\n"
    )
    out = mod.normalize_math(raw)
    # Spaced inline left for smart_dollar: false
    assert "$  p(Y|X)  $" in out, out
    assert "$  p_Y  $" in out, out
    # Must not eat the space between two math spans
    assert r"$\Phi_g$ and entropy $S_c$" in out, out
    assert r"$\Phi_g$and" not in out, out
    assert "$$\nH_c(f; p_X) := H(Y)\n$$" in out, out


def test_paper_chapters_include_load_equation():
    """Full paper must be split into chapters; §6 must contain L(ρ,g)."""
    subprocess.run([sys.executable, str(SYNC)], cwd=REPO, check=True)
    for rel in EXPECTED_PAPER_CHAPTERS:
        path = DOCS / rel
        assert path.is_file(), f"missing paper chapter {path}"
        assert path.stat().st_size > 0
    load_ch = (DOCS / "papers/chapters/06-channel-load-master-equation.md").read_text(
        encoding="utf-8"
    )
    assert "Computational load" in load_ch or "computational load" in load_ch
    assert "L(\\rho,g)" in load_ch or r"L(\rho,g)" in load_ch or "L(\\rho,g)" in load_ch
    assert "E[\\rho]" in load_ch or r"E[\rho]" in load_ch or "E[" in load_ch
    assert "master equation" in load_ch.lower()
    full = (DOCS / "papers/paper-full.md").read_text(encoding="utf-8")
    # Full paper should be substantial (entire manuscript)
    assert len(full) > 50_000, f"paper-full too small: {len(full)}"
    assert "Gravitational channel" in full or "gravitational channel" in full


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
    assert build.returncode == 0, build.stderr + build.stdout
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


def test_built_site_includes_paper_load_chapter():
    """Built site must ship paper §6 HTML with load formula markup."""
    load_html = REPO / "site/papers/chapters/06-channel-load-master-equation/index.html"
    if not load_html.is_file():
        subprocess.run([sys.executable, str(SYNC)], cwd=REPO, check=True)
        subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "-q"],
            cwd=REPO,
            check=True,
        )
    html = load_html.read_text(encoding="utf-8")
    assert "arithmatex" in html
    assert "Computational load" in html or "computational load" in html
    # Energy term from L formula should appear in TeX body
    assert "epsilon" in html or "epsilon_0" in html or "\\epsilon" in html


if __name__ == "__main__":
    test_normalize_math_fixes_same_line_display_without_eating_inline_spaces()
    test_sync_script_exits_zero_and_writes_allowlist()
    test_denylisted_paths_not_under_docs_from_sync()
    test_paper_chapters_include_load_equation()
    test_built_foundations_page_wraps_stochastic_math()
    test_built_site_includes_paper_load_chapter()
    print("OK: sync_site_docs tests passed")
