# Downloads

**Preliminary research.** PDFs below are generated from the canonical research sources in the repository. Prefer under-claiming; see [Non-claims](non-claims.md).

## Papers (PDF)

| Paper | Scope | Download | Read online |
|-------|-------|----------|-------------|
| **Paper A — Computational Entropy: Output-Distribution Entropy and Landauer-Exact Export** | Solid core: output-distribution entropy, export identity, Landauer-exactness, path-dependence. **No gravity claims.** | [PDF](pdf/computational-entropy-paper-A.pdf){:download} | [HTML](papers/paper-a.md) |
| **Paper C — The Decay Algebra: From Export Ledgers to a Continuum Entropy-Production Density** | Classical, no gravity: coupled export density, the decay-algebra transfer operator (proved 1D & general-\(w\)), 2D strip, and a constructive continuum density field \(\sigma(x)\). | [PDF](pdf/decay-algebra-paper-C.pdf){:download} | [HTML](papers/paper-c.md) |
| **Paper B — An Information-Theoretic Reformulation of Thermodynamic Gravity (Conjecture)** | Emergent gravity as a **reformulation/conjecture**: channel + load as a Jacobson-shaped postulate, Newton via Path J/M, falsifiability question. | [PDF](pdf/emergent-gravity-conjecture-paper-B.pdf){:download} | [HTML](papers/paper-b.md) |
| **Integrated paper — Computational Entropy and Emergent Gravity** | Full standalone manuscript (literature + our theory). | [PDF](pdf/computational-entropy-integrated-paper.pdf){:download} | [HTML](papers/paper-full.md) |

!!! note "How these PDFs are built"
    Paper PDFs are pre-built locally with `scripts/build_paper_pdfs.py` (pandoc + XeLaTeX) and committed, because the GitHub Pages CI has no LaTeX toolchain. The site's sync step copies them into `pdf/` at build time.

## Supporting reading

- **[Falsifiability analysis](papers/falsifiability.md)** — does the load \(L\) predict anything GR doesn't? (Verdict: **reformulation**, with the entropy-production term flagged as the sole candidate departure.)
- **[Results ledger](synthesis/results-ledger.md)** — consolidated *proved / rigor-label / open* status.
- **[Claims](synthesis/claims.md)** · **[Conclusions](synthesis/conclusions.md)** — frozen may-assert spine and non-claims.

## External reference literature

The Gravity-from-Entropy and related papers this program bridges to are **third-party works** (peers in a research program, not established foundations). Obtain them from their publishers / arXiv:

- Bianconi, *Gravity from entropy* (PRD 2025), arXiv:2408.14391
- Bianconi, *Beyond holography*, arXiv:2503.14048
- Thattarampilly & Zheng, *Inflation from entropy*, arXiv:2509.23987; *Spherically symmetric black hole*, arXiv:2602.13694
- Kumar, *Recovering semiclassical Einstein*, arXiv:2404.16912

Full research tree, ledgers, and build scripts: **[source repository](https://github.com/cyotee/computational-entropy)**.
