#!/usr/bin/env python3
"""Copy allowlisted canonical research Markdown into docs/ for MkDocs.

Fail loudly if any allowlisted source is missing. Never copies denylisted trees
(drafts/, archive/, external PDFs, agent bootstrap). Run before `mkdocs build`.

Also normalizes TeX delimiters for pymdownx.arithmatex + MathJax:
- same-line $$...$$ → blank-line block form (required for display math)
- spaced inline $  expr  $ is left alone (requires smart_dollar: false in mkdocs.yml)

Splits papers/06-synthesis/PAPER.md into chapter pages so the full manuscript
(including computational load §6) is navigable in the left sidebar.
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
    ("papers/06-synthesis/PAPER.md", "papers/paper-full.md"),
    ("GLOSSARY.md", "glossary.md"),
    ("PROGRESS_REPORT.md", "progress.md"),
]

PAPER_SRC = "papers/06-synthesis/PAPER.md"
PAPER_CHAPTERS_DIR = "papers/chapters"

# Paths that must never appear under docs/ from this sync (checked after copy).
DENY_MARKERS = (
    "drafts/",
    "archive/",
    "CLAUDE.md",
    "papers/external/",
    "external-docs/",
)

# $$...$$ display math (Arithmatex needs blank-line blocks, not same-line $$)
_SAME_LINE_DISPLAY = re.compile(
    r"(?<!\$)\$\$(?!\$)(.+?)(?<!\$)\$\$(?!\$)",
    re.DOTALL,
)
# Top-level ATX headings: "# Title" but not "##"
_H1 = re.compile(r"^# ([^#].*)$", re.MULTILINE)

# Map heading prefix → (filename, short nav title)
# Order follows the manuscript; unmatched H1s get a slugified name.
_CHAPTER_MAP: list[tuple[str, str, str]] = [
    ("1. Introduction", "01-introduction.md", "1. Introduction"),
    ("2. Related work", "02-related-work.md", "2. Related work"),
    ("3. Results", "03-results.md", "3. Results"),
    ("4. Foundations", "04-foundations.md", "4. Foundations"),
    ("5. Classical microstructure", "05-classical-microstructure.md", "5. Classical microstructure"),
    ("6. Gravitational channel", "06-channel-load-master-equation.md", "6. Channel, load & master equation"),
    ("7. Newton recovery", "07-newton-recovery.md", "7. Newton recovery (Path J/M)"),
    ("8. Euclidean dual", "08-euclidean-dual.md", "8. Euclidean dual (ACD-EW)"),
    ("9. Continuum GfE contact", "09-continuum-gfe.md", "9. Continuum GfE contact"),
    ("9.5 Continuum GfE applications", "09b-gfe-applications.md", "9.5 GfE applications"),
    ("10. Synthesis", "10-synthesis.md", "10. Synthesis & open program"),
    ("11. Final conclusions", "11-conclusions.md", "11. Final conclusions"),
    ("Appendix A", "appendix-a.md", "Appendix A. Witnesses"),
    ("Appendix B", "appendix-b.md", "Appendix B. Claims checklist"),
    ("Appendix C", "appendix-c.md", "Appendix C. Open avenues"),
    ("References", "references.md", "References"),
]


def normalize_math(text: str) -> str:
    """Make research markdown play well with Arithmatex + MathJax.

    Only rewrites display math into blank-line blocks. Inline forms like
    ``$  p(Y|X)  $`` are left as-is and rely on ``smart_dollar: false`` in
    mkdocs.yml. Do **not** rewrite padding between adjacent ``$...$`` spans —
    that previously ate inter-expression spaces (e.g. ``$\\Phi_g$ and``).
    """

    def display_repl(match: re.Match[str]) -> str:
        body = match.group(1).strip("\n").strip()
        return f"\n\n$$\n{body}\n$$\n\n"

    text = _SAME_LINE_DISPLAY.sub(display_repl, text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def _slugify(title: str) -> str:
    s = title.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:60] or "section"


def _chapter_meta(title: str) -> tuple[str, str]:
    for prefix, filename, nav_title in _CHAPTER_MAP:
        if title.startswith(prefix) or title == prefix:
            return filename, nav_title
    return f"{_slugify(title)}.md", title[:80]


def split_paper_chapters(paper_text: str) -> list[tuple[str, str, str]]:
    """Split PAPER.md on H1 into (filename, nav_title, body) chapters.

    Returns chapters including a front-matter page (abstract, contents, banner)
    before the first numbered section.
    """
    matches = list(_H1.finditer(paper_text))
    if not matches:
        return [("00-front-matter.md", "Front matter", paper_text)]

    chapters: list[tuple[str, str, str]] = []

    # Everything before first H1 after the title block: use content from start
    # First H1 is the document title — fold title + preamble until section 1.
    first = matches[0]
    # Find first "real" section after title (starts with digit or Appendix/References)
    section_starts: list[re.Match[str]] = []
    for m in matches[1:]:
        section_starts.append(m)
    if not section_starts:
        body = paper_text
        chapters.append(("00-front-matter.md", "Title & abstract", body))
        return chapters

    front_end = section_starts[0].start()
    front_body = paper_text[:front_end].rstrip() + "\n"
    chapters.append(("00-front-matter.md", "Title & abstract", front_body))

    for i, m in enumerate(section_starts):
        title = m.group(1).strip()
        start = m.start()
        end = section_starts[i + 1].start() if i + 1 < len(section_starts) else len(paper_text)
        body = paper_text[start:end].rstrip() + "\n"
        filename, nav_title = _chapter_meta(title)
        chapters.append((filename, nav_title, body))

    return chapters


def write_paper_chapters(paper_text: str) -> list[tuple[str, str]]:
    """Write chapter files under docs/papers/chapters/. Returns (nav_title, rel_path)."""
    out_dir = DOCS / PAPER_CHAPTERS_DIR
    if out_dir.exists():
        for old in out_dir.glob("*.md"):
            old.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)

    nav_entries: list[tuple[str, str]] = []
    for filename, nav_title, body in split_paper_chapters(paper_text):
        path = out_dir / filename
        path.write_text(normalize_math(body), encoding="utf-8")
        rel = f"{PAPER_CHAPTERS_DIR}/{filename}"
        nav_entries.append((nav_title, rel))
    return nav_entries


def write_generated_nav(nav_entries: list[tuple[str, str]]) -> None:
    """Write docs/_paper_nav.yml fragment for human inspection (mkdocs uses static nav)."""
    lines = ["# Auto-generated by sync_site_docs.py — mirror of paper chapter nav\n"]
    for title, rel in nav_entries:
        lines.append(f"- {title}: {rel}\n")
    (DOCS / "_paper_nav.yml").write_text("".join(lines), encoding="utf-8")


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

    paper_path = REPO_ROOT / PAPER_SRC
    if not paper_path.is_file():
        missing.append(PAPER_SRC)
    else:
        paper_text = paper_path.read_text(encoding="utf-8")
        nav_entries = write_paper_chapters(paper_text)
        write_generated_nav(nav_entries)
        copied.append(
            f"{PAPER_SRC} -> docs/{PAPER_CHAPTERS_DIR}/ ({len(nav_entries)} chapters)"
        )

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

    print(f"Synced {len(copied)} allowlisted target(s):")
    for line in copied:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
