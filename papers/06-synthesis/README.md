# Integrated research paper

## Files for review / publish

| File | Role |
|------|------|
| **[PAPER.pdf](PAPER.pdf)** | **Built PDF** (~60 pages) — open this to review |
| **[PAPER.md](PAPER.md)** | Full integrated manuscript (markdown source) |
| **[PAPER.tex](PAPER.tex)** | LaTeX from pandoc (editable) |
| [refs.bib](refs.bib) | BibTeX for published literature |
| [Makefile](Makefile) | Rebuild: `make pdf` |

## Rebuild PDF (simple pandoc path)

Same idea as other successful pandoc PDFs in this project:

```bash
cd papers/06-synthesis
make pdf
# or one-shot:
python3 build_pdf_preprocess.py
pandoc _paper_build.md -o PAPER.tex --standalone --toc \
  -f markdown+tex_math_dollars+pipe_tables \
  -V geometry:margin=1in -V documentclass=article
python3 fix_tex.py
latexmk -xelatex -f PAPER.tex
```

**Note:** The paper is long and math-heavy. A few non-ASCII glyphs in diagrams may still warn in the log; the PDF should still build with `latexmk -f`. Prefer `PAPER.md` / HTML if a glyph looks odd:

```bash
pandoc _paper_build.md -o PAPER.html --standalone --toc --mathjax
open PAPER.html
```

## What this paper integrates

**Our theory:** $H_c$/$S_c$, $L$ + master equation, Path J/M Newton, discrete load + Landauer + path dependence, ACD-EW dual, M6 GfE contact, promotion no-go, appendices.

**External literature:** Shannon, Landauer, Jacobson, Verlinde, holography/complexity (RT, Susskind, Lloyd), Bianconi GfE + Beyond holography, Thattarampilly–Zheng inflation/BH, Kumar $S_{\mathrm{gen}}$, Perona–Malik.

Standalone: **no repo hyperlinks** — appendices + published citations.

## Other drafts (supporting)

| File | Role |
|------|------|
| `FINAL.md` | In-repo freeze with internal pointers (agents) |
| `PUBLISHABLE.md` | Earlier standalone freeze |
| `PUBLISHING.md` | Notes on math delimiters vs repo links |
