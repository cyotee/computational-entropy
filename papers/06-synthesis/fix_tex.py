#!/usr/bin/env python3
"""Post-pandoc fixes for robust xelatex (load-clock brackets, sec numbers)."""
from pathlib import Path
import re

p = Path("PAPER.tex")
t = p.read_text(encoding="utf-8")

t = t.replace(
    r"\setcounter{secnumdepth}{-\maxdimen} % remove section numbering",
    r"\setcounter{secnumdepth}{3}",
)
t = t.replace(
    r"load clock {[} d\tau=\frac{dt}{1+\alpha L}, {]}",
    r"load clock ($d\tau=dt/(1+\alpha L)$)",
)
t = t.replace(
    r"load clock {[} d\tau=\frac{dt}{1+\alpha L}",
    r"load clock ($d\tau=dt/(1+\alpha L)$)",
)
t = re.sub(r"\{\[\}([^]]*)\{\]\}", r"[\1]", t)
t = t.replace("′", "'")
t = t.replace("τ", r"\tau")
t = t.replace("dτ/dt", r"$d\tau/dt$")

# Remaining high-unicode math glyphs in text mode
for a, b in {
    "∑": r"$\sum$",
    "∫": r"$\int$",
    "⋅": r"$\cdot$",
    "≠": r"$\neq$",
    "→": r"$\to$",
    "⇒": r"$\Rightarrow$",
    "⇔": r"$\Leftrightarrow$",
}.items():
    t = t.replace(a, b)

p.write_text(t, encoding="utf-8")
print("Fixed PAPER.tex")
