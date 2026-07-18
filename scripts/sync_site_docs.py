#!/usr/bin/env python3
"""Copy allowlisted canonical research Markdown into docs/ for MkDocs.

Fail loudly if any allowlisted source is missing. Never copies denylisted trees
(drafts/, archive/, external PDFs, agent bootstrap). Run before `mkdocs build`.

Also normalizes TeX delimiters for pymdownx.arithmatex + MathJax:
- same-line $$...$$ → blank-line block form (required for display math)
- $  expr  $ → $expr$ (smart_dollar-safe; also fine with smart_dollar: false)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"

# (source relative to repo root, destination relative to docs/)
ALLOWLIST: list[tuple[str, str]] = [
    (
        "foundations/computational-entropy/definition.md",
        "foundations/computational-entropy.md",
    ),
    (
        "emergent-gravity/master-equation.md",
        "emergent-gravity/master-equation.md",
    ),
    (
        "emergent-gravity/recoveries/newtonian/README.md",
        "emergent-gravity/newtonian-recovery.md",
    ),
    ("synthesis/CURRENT_CLAIMS.md", "synthesis/claims.md"),
    ("synthesis/PROGRAM_CONCLUSIONS.md", "synthesis/conclusions.md"),
    ("synthesis/OPEN_AVENUES.md", "synthesis/open-avenues.md"),
    ("papers/06-synthesis/FINAL.md", "papers/final-report.md"),
    ("papers/06-synthesis/PUBLISHABLE.md", "papers/publishable.md"),
    ("GLOSSARY.md", "glossary.md"),
    ("PROGRESS_REPORT.md", "progress.md"),
]

# Paths that must never appear under docs/ from this sync (checked after copy).
DENY_MARKERS = (
    "drafts/",
    "archive/",
    "CLAUDE.md",
    "papers/external/",
    "external-docs/",
)

# Same-line display math: $$ ... $$ (non-greedy, no nested newlines required)
_SAME_LINE_DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
# Inline $ ... $ with optional padding spaces (not $$)
_PADDED_INLINE = re.compile(r"(?<!\$)\$([ \t]+)([^\$]+?)([ \t]+)\$(?!\$)")


def normalize_math(text: str) -> str:
    """Make research markdown play well with Arithmatex + MathJax."""

    def display_repl(match: re.Match[str]) -> str:
        body = match.group(1).strip("\n")
        # Keep multi-line bodies indented content intact; strip only outer blank lines
        body = body.strip()
        return f"\n\n$$\n{body}\n$$\n\n"

    # Display first so we do not mangle $$ as two single-dollar wraps
    text = _SAME_LINE_DISPLAY.sub(display_repl, text)
    # Collapse padding around inline math: "$  p_Y  $" -> "$p_Y$"
    text = _PADDED_INLINE.sub(r"$\2$", text)
    # Tidy excess blank lines introduced around displays
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def main() -> int:
    missing: list[str] = []
    copied: list[str] = []

    for src_rel, dst_rel in ALLOWLIST:
        src = REPO_ROOT / src_rel
        dst = DOCS / dst_rel
        if not src.is_file():
            missing.append(src_rel)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        raw = src.read_text(encoding="utf-8")
        dst.write_text(normalize_math(raw), encoding="utf-8")
        copied.append(f"{src_rel} -> docs/{dst_rel}")

    if missing:
        print("ERROR: allowlisted source(s) missing:", file=sys.stderr)
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        return 1

    # Sanity: denylist markers should not be destinations of this allowlist.
    for _, dst_rel in ALLOWLIST:
        for marker in DENY_MARKERS:
            if marker.rstrip("/") in Path(dst_rel).parts or marker in dst_rel:
                print(
                    f"ERROR: allowlist destination hits denylist marker {marker!r}: {dst_rel}",
                    file=sys.stderr,
                )
                return 1

    print(f"Synced {len(copied)} allowlisted page(s):")
    for line in copied:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
