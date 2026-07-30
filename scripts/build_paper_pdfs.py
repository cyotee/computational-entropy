#!/usr/bin/env python3
"""Build committed PDF assets for the standalone papers (Paper A, Paper B, ...).

CI (GitHub Pages) has no LaTeX toolchain, so paper PDFs are pre-built locally
and committed; `sync_site_docs.py` then copies them into `docs/pdf/` for the
MkDocs site to serve. Run this whenever a source paper markdown changes:

    .venv/bin/python scripts/build_paper_pdfs.py

Requires: pandoc + a LaTeX engine (xelatex by default).
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ENGINE = "xelatex"

# (source markdown relative to repo root, output pdf relative to repo root)
PAPERS: list[tuple[str, str]] = [
    (
        "papers/01-foundations/PAPER_A_computational_entropy.md",
        "papers/01-foundations/PAPER_A_computational_entropy.pdf",
    ),
    (
        "papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md",
        "papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.pdf",
    ),
]


def normalize_math_delims(text: str) -> str:
    r"""Convert \(..\) and \[..\] LaTeX delimiters to $..$ / $$..$$ for pandoc."""
    text = text.replace(r"\(", "$").replace(r"\)", "$")
    text = text.replace(r"\[", "$$").replace(r"\]", "$$")
    return text


def build(md_rel: str, pdf_rel: str) -> None:
    """Two-step build: pandoc -> standalone .tex, then xelatex twice (for TOC).

    pandoc's built-in ``--pdf-engine`` route was observed to hang; driving the
    engine directly with nonstopmode + halt-on-error is reliable.
    """
    src = REPO_ROOT / md_rel
    out = REPO_ROOT / pdf_rel
    if not src.is_file():
        raise SystemExit(f"ERROR: source markdown missing: {md_rel}")

    work = src.parent
    stem = "_build_" + src.stem
    tmp_md = work / (stem + ".md")
    tmp_tex = work / (stem + ".tex")
    tmp_pdf = work / (stem + ".pdf")

    tmp_md.write_text(normalize_math_delims(src.read_text(encoding="utf-8")), encoding="utf-8")

    try:
        subprocess.run(
            [
                "pandoc", str(tmp_md), "-o", str(tmp_tex),
                "--standalone", "--toc", "--toc-depth=2",
                "-f", "markdown+tex_math_dollars+pipe_tables+backtick_code_blocks",
                "-V", "geometry:margin=1in",
                "-V", "documentclass=article",
                "-V", "fontsize=11pt",
                "-V", "colorlinks=true",
                "-V", "linkcolor=blue",
            ],
            cwd=str(work), check=True,
        )
        for _ in range(2):  # two passes so the table of contents resolves
            subprocess.run(
                ["xelatex", "-interaction=nonstopmode", "-halt-on-error", tmp_tex.name],
                cwd=str(work), check=True,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
        shutil.move(str(tmp_pdf), str(out))
    finally:
        for ext in (".md", ".tex", ".aux", ".log", ".out", ".toc", ".pdf"):
            (work / (stem + ext)).unlink(missing_ok=True)

    print(f"  built {pdf_rel} ({out.stat().st_size/1024:.0f} KB)")


def main() -> int:
    if not shutil.which("pandoc"):
        raise SystemExit("ERROR: pandoc not found on PATH")
    if not shutil.which(ENGINE):
        raise SystemExit(f"ERROR: {ENGINE} not found on PATH")
    print(f"Building {len(PAPERS)} paper PDF(s) with pandoc + {ENGINE}:")
    for md_rel, pdf_rel in PAPERS:
        build(md_rel, pdf_rel)
    return 0


if __name__ == "__main__":
    sys.exit(main())
