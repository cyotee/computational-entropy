#!/usr/bin/env python3
"""Lightweight claim-hygiene check (Track A failure-mode infra).

Does not invent physics. Verifies gate docs exist, prints frozen non-claims,
checks non-claims banner language in key files, optionally greps for
forbidden positive identity phrases (soft; human review).

Usage:
  .venv/bin/python simulations/classical/check_claim_hygiene.py
  .venv/bin/python simulations/classical/check_claim_hygiene.py --strict
  .venv/bin/python simulations/classical/check_claim_hygiene.py --grep
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    REPO / "synthesis" / "CLAIM_GATE.md",
    REPO / "synthesis" / "CURRENT_CLAIMS.md",
    REPO / "synthesis" / "NONCLAIMS_FIXTURE.md",
    REPO / "synthesis" / "m10-sc-vs-toy-hc.md",
    REPO / "synthesis" / "m5-warmup-continuum-hygiene.md",
    REPO / "GLOSSARY.md",
]

# Frozen non-claims — mirror CURRENT_CLAIMS §3 / NONCLAIMS_FIXTURE (print only).
FROZEN_NONCLAIMS = [
    "N1  Master equation ⇔ Bianconi continuum GfE.",
    "N2  L ≡ G; S_c ≡ Tr g ln G^{-1}; α_L β_L ≡ α_B/β_B.",
    "N3  T1 residual domination for all t ∈ (0, t_★] (use T1′ / U_★).",
    "N4  Pure T1′ with no soft hypotheses (PCRH_b still ensemble-certified).",
    "N5  Newton from pointwise Φ ∝ ρ Laplacian (withdrawn).",
    "N6  Next-order γ_L, δ_L equal GfE D_μν, Λ_G.",
    "N7  Lattice denoising = empirical gravity.",
    "N8  External GfE papers established on par with GR.",
    "N9  IDEM/decay fully constructs continuum L or G (open / deferred).",
]

# Banner markers: (path relative to repo, required substring).
BANNER_MARKERS = [
    ("synthesis/CURRENT_CLAIMS.md", "Explicit non-claims"),
    ("PROGRESS_REPORT.md", "Explicit non-claims"),
    ("papers/06-synthesis/OUTLINE.md", "Non-claims banner"),
    ("synthesis/CLAIM_GATE.md", "Pass/fail"),
    ("synthesis/NONCLAIMS_FIXTURE.md", "Frozen non-claims"),
    ("GLOSSARY.md", "Entropy object tags"),
]

# Soft forbidden patterns: flag lines that look like positive identities.
# Negation keywords nearby reduce false positives.
FORBIDDEN = [
    (
        "L_equiv_G",
        re.compile(r"\bL\s*≡\s*G\b|\bL\s*\\equiv\s*G\b|\bL\s*==\s*G\b"),
        "Possible L ≡ G identity",
    ),
    (
        "ME_iff_GfE",
        re.compile(
            r"master\s+equation.{"
            r"0,80}"
            r"(equivalent|⇔|\\Leftrightarrow|identical|equals?)\s+.{0,40}GfE",
            re.I | re.S,
        ),
        "Possible master equation ⇔ GfE",
    ),
    (
        "Sc_equiv_Tr",
        re.compile(
            r"S_c\s*(≡|\\equiv)\s*(Tr|\\operatorname\{Tr\})",
            re.I,
        ),
        "Possible S_c ≡ Tr identity",
    ),
    (
        "alpha_id",
        re.compile(
            r"(α_L|alpha_L|\\alpha_L).{0,20}(β_L|beta_L|\\beta_L).{0,30}"
            r"(≡|\\equiv|=).{0,20}(α_B|alpha_B|\\alpha_B)",
            re.I,
        ),
        "Possible α_L β_L = α_B identification",
    ),
    (
        "phi_propto_rho_newton",
        re.compile(
            r"(Φ|\\Phi|Phi)\s*(∝|\\propto|propto)\s*(ρ|\\rho|rho).{0,60}"
            r"(Newton|Poisson|Laplacian)",
            re.I | re.S,
        ),
        "Possible withdrawn Φ∝ρ Newton path",
    ),
    (
        "denoising_is_gravity",
        re.compile(
            r"lattice\s+denoising.{"
            r"0,40}"
            r"(is|=|equals?)\s+.{0,20}empirical\s+gravity",
            re.I | re.S,
        ),
        "Possible lattice denoising = empirical gravity",
    ),
]

NEGATION_HINT = re.compile(
    r"\b(not|never|do\s+not|don't|forbid|forbidden|refuse|refused|withdrawn|"
    r"non-claim|nonclaim|≠|\\neq|must\s+not|no\s+claim|without\s+new|"
    r"do\s+\*\*not\*\*|FAIL|fail if|must not assert)\b",
    re.I,
)

GREP_ALLOWLIST = [
    "synthesis/CURRENT_CLAIMS.md",
    "synthesis/CLAIM_GATE.md",
    "synthesis/NONCLAIMS_FIXTURE.md",
    "PROGRESS_REPORT.md",
    "papers/06-synthesis/OUTLINE.md",
    "GLOSSARY.md",
    "THEORY.md",
    "PRD.md",
    "Claude.md",
    "synthesis/m10-sc-vs-toy-hc.md",
    "synthesis/m5-warmup-continuum-hygiene.md",
    "synthesis/m11-idem-to-load.md",
    "synthesis/m6-weak-field-plugtest.md",
    "emergent-gravity/recoveries/newtonian/README.md",
]


def check_required_files() -> list[str]:
    missing = []
    for path in REQUIRED_FILES:
        if not path.is_file():
            missing.append(str(path.relative_to(REPO)))
    return missing


def check_banners() -> list[tuple[str, str]]:
    """Return list of (path, missing_marker) warnings."""
    warnings = []
    for rel, marker in BANNER_MARKERS:
        path = REPO / rel
        if not path.is_file():
            warnings.append((rel, f"(file missing) expected marker: {marker!r}"))
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if marker not in text:
            warnings.append((rel, f"missing banner marker: {marker!r}"))
    return warnings


def grep_forbidden() -> list[tuple[str, int, str, str]]:
    """Return (rel_path, line_no, rule_id, line_snippet) for soft hits."""
    hits: list[tuple[str, int, str, str]] = []
    for rel in GREP_ALLOWLIST:
        path = REPO / rel
        if not path.is_file():
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        # Also join for multi-line patterns with small windows
        for i, line in enumerate(lines, start=1):
            window = "\n".join(lines[max(0, i - 2) : min(len(lines), i + 1)])
            if NEGATION_HINT.search(window):
                # Still scan single-line positive identities carefully
                pass
            for rule_id, pattern, _msg in FORBIDDEN:
                if pattern.search(line) or (
                    "\n" in pattern.pattern and pattern.search(window)
                ):
                    # Skip if window clearly refuses the identity
                    if NEGATION_HINT.search(window):
                        continue
                    snippet = line.strip()
                    if len(snippet) > 120:
                        snippet = snippet[:117] + "..."
                    hits.append((rel, i, rule_id, snippet))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description="Claim hygiene checker (lightweight)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if required files or banner markers are missing",
    )
    parser.add_argument(
        "--grep",
        action="store_true",
        help="Also soft-grep allowlisted files for forbidden positive phrases",
    )
    args = parser.parse_args()

    print("=== Claim hygiene (Track A) ===")
    print(f"repo: {REPO}")
    print()

    missing = check_required_files()
    if missing:
        print("REQUIRED FILES: MISSING")
        for m in missing:
            print(f"  - {m}")
    else:
        print("REQUIRED FILES: OK")
        for p in REQUIRED_FILES:
            print(f"  + {p.relative_to(REPO)}")
    print()

    print("FROZEN NON-CLAIMS (CURRENT_CLAIMS §3 mirror):")
    for row in FROZEN_NONCLAIMS:
        print(f"  {row}")
    print("  Also: toy H_c ≠ von Neumann S_c; M11 accounting ≠ continuum derivation.")
    print()

    banner_warn = check_banners()
    if banner_warn:
        print("BANNER MARKERS: WARNINGS")
        for rel, msg in banner_warn:
            print(f"  ! {rel}: {msg}")
    else:
        print("BANNER MARKERS: OK")
        for rel, marker in BANNER_MARKERS:
            print(f"  + {rel} contains {marker!r}")
    print()

    grep_hits: list[tuple[str, int, str, str]] = []
    if args.grep:
        grep_hits = grep_forbidden()
        if grep_hits:
            print("SOFT GREP: possible positive forbidden phrases (human review)")
            for rel, lineno, rule_id, snippet in grep_hits:
                print(f"  ? {rel}:{lineno} [{rule_id}] {snippet}")
            print(
                "  (Negated/refused contexts are filtered; residual hits need eyes.)"
            )
        else:
            print("SOFT GREP: no positive forbidden phrases on allowlist")
        print()

    print("Pointers:")
    print("  synthesis/CLAIM_GATE.md")
    print("  synthesis/CURRENT_CLAIMS.md")
    print("  synthesis/NONCLAIMS_FIXTURE.md")
    print("  synthesis/m10-sc-vs-toy-hc.md")
    print("  synthesis/m5-warmup-continuum-hygiene.md")
    print()

    if args.strict and (missing or banner_warn):
        print("RESULT: FAIL (--strict)")
        return 1
    if missing:
        print("RESULT: FAIL (missing required files)")
        return 1
    print("RESULT: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
