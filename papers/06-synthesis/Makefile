# Build the integrated paper PDF (simple pandoc path)
# Usage: make pdf

ENGINE ?= xelatex
MD     := _paper_build.md
PDF    := PAPER.pdf
TEX    := PAPER.tex

.PHONY: pdf tex html clean preprocess

preprocess:
	python3 build_pdf_preprocess.py

tex: preprocess
	pandoc $(MD) -o $(TEX) --standalone --toc --toc-depth=2 \
	  -f markdown+tex_math_dollars+pipe_tables \
	  -V documentclass=article \
	  -V geometry:margin=1in \
	  -V fontsize=11pt
	python3 fix_tex.py

pdf: tex
	latexmk -$(ENGINE) -interaction=nonstopmode -f $(TEX)
	@ls -la $(PDF)
	@echo "Built $(PDF)"

# One-shot: pandoc direct to PDF (when source is clean)
pdf-direct: preprocess
	pandoc $(MD) -o $(PDF) --pdf-engine=$(ENGINE) --toc --toc-depth=2 \
	  -f markdown+tex_math_dollars+pipe_tables \
	  -V geometry:margin=1in -V documentclass=article

html: preprocess
	pandoc $(MD) -o PAPER.html --standalone --toc --mathjax \
	  -f markdown+tex_math_dollars+pipe_tables

clean:
	latexmk -C $(TEX) 2>/dev/null || true
	rm -f *.aux *.log *.out *.toc *.fls *.fdb_latexmk *.xdv
