#!/usr/bin/env python3
"""Light preprocess of PAPER.md for pandoc PDF (same spirit as other repo PDFs)."""
from pathlib import Path
import re

src = Path("PAPER.md").read_text(encoding="utf-8")

# Characters that break LM Roman in text mode when outside $...$
for a, b in {
    "\U0001d70f": r"\tau",
    "𝜏": r"\tau",
    "⋅": r"\cdot",
    "│": "|",
    "▼": "v",
    "►": "->",
    "─": "-",
    "♯": "#",
    "\u201c": '"',
    "\u201d": '"',
    "\u2018": "'",
    "\u2019": "'",
    "—": "---",
    "–": "--",
    "\u00a0": " ",
    "′": "'",
    "∑": r"\sum",
    "∫": r"\int",
}.items():
    src = src.replace(a, b)

# Avoid pandoc turning [$...$] into broken {[} ... {]} with \frac
src = re.sub(r"\[\$([^$]+)\$\]", r"($\1$)", src)
# Prefer slash form for load clock in prose (more robust than nested frac)
src = re.sub(
    r"\$d\\tau\s*=\s*\\frac\{dt\}\{1\+\\alpha\s*L\}\$",
    r"$d\\tau=dt/(1+\\alpha L)$",
    src,
)

src = re.sub(r"\n## Contents\n.*?(?=\n# 1\. Introduction)", "\n", src, count=1, flags=re.S)
src = re.sub(r"^# Computational Entropy[^\n]*\n+", "", src, count=1)
src = re.sub(
    r"^\*\*(Authors|Affiliation|Version|Status|Abstract-level type safety)\.\*\*[^\n]*\n",
    "",
    src,
    flags=re.M,
)

yaml = """---
title: "Computational Entropy and Emergent Gravity: From Output Distributions to Load-Gated Geometry"
author: "not_cyotee"
date: "2026-07-16"
geometry: margin=1in
fontsize: 11pt
---

"""
Path("_paper_build.md").write_text(yaml + src, encoding="utf-8")
print("Wrote _paper_build.md")
