# PRD — Documenting the Decay-Algebra Ladder (papers + Git Pages)

**Status:** Active PRD (written 2026-07-30) · Preliminary research
**Owner:** cyotee
**Purpose:** Update the research papers and the GitHub Pages site to document the new **decay-algebra / continuum-density** research (O1 ladder, `m11f`–`m11i`) in a cohesive form.
**Companions:** [DELIVERY_PLAN.md](DELIVERY_PLAN.md) · [DELIVERY_SCOPE.md](DELIVERY_SCOPE.md) · [FALSIFIABILITY_L_vs_GR.md](FALSIFIABILITY_L_vs_GR.md) · [../synthesis/RESULTS_LEDGER.md](../synthesis/RESULTS_LEDGER.md)
**Authority for claims:** [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md) (non-claims stand)

---

## 1. End goal (one paragraph)

Incorporate the completed O1 arc — from Paper A's Landauer-exact export ledger, through the **decay algebra** (a boundary-belief transfer operator that computes coupled export densities), to a **constructive continuum entropy-production density field** `σ(x)` — into the paper set and the Pages site, as a single coherent story: *the discrete side of the computational-entropy → continuum bridge is now built and largely proved, while the identification of `σ` with the gravitational load term remains an explicit, labeled semantic step.*

## 2. What is new (the research to document)

The session produced a proved/witnessed ladder (canonical sources in `synthesis/m11f–i` and `simulations/classical/m11_*`):

| ID | Result | Rigor | Source |
|----|--------|-------|--------|
| IDEM↔export | Hard decay vector upper-bounds `H(X\|Y)`, **exact for product/reset maps** ⇒ O(N) enumeration-free density | proved | `m11_idem_export_density.py` |
| m11f | **1D density theorem**: `a = 1 − h_Y` via run-length belief chain; `π*=(3−√5)/2`, `a=0.3007568` | **proved** | `m11f` · `m11_decay_algebra.py` |
| m11g | **General-`w` theorem**: existence via `(w−1)`-dependence; Blackwell transfer representation; **reset gates regenerate ⇒ renewal-reward**; dichotomy `exact ⇔ reset` | **proved** | `m11g` · `m11_decay_algebra_general.py` |
| m11h | **2D strip transfer**: density exists on ℤ²; width-`W` transfer on `2^W` row-cut; `2^W` wall | proved (existence) | `m11h` · `m11_decay_algebra_2d.py` |
| m11i | **Continuum embedding**: local equilibrium ⇒ `σ(x)=a(θ(x))` at O(1/N); `∫σ=0.29937` | witnessed | `m11i` · `m11_continuum_embedding.py` |

**Headline narrative:** the export ledger admits a constructive continuum entropy-production **density field**, computed by the decay algebra; IDEM's decay vector earns a *proved, load-bearing* role (its reset structure controls the algebra's exact finiteness).

## 3. Goals & non-goals

**Goals.**
- G1 — A new **Paper C** presenting the decay-algebra ladder as self-contained classical research (no gravity claims).
- G2 — Targeted updates to **Paper A** (forward reference), **Paper B** (sharpen the reformulation bridge to `σ`), and the **integrated PAPER.md** (§5 + synthesis/conclusions).
- G3 — **Git Pages** updated: new section + pages for Paper C and the `m11f–i` results, homepage/nav, downloadable PDF.
- G4 — Scope/claims artifacts updated (`DELIVERY_SCOPE`, `RESULTS_LEDGER`, `CURRENT_CLAIMS` if needed).

**Non-goals.**
- Not claiming `σ` **is** the gravitational load term `γ|dS_c/dτ|` (semantic bridge only).
- Not reopening the ACD-EW residual dual, GfE identity, or any frozen non-claim.
- Not a general hydrodynamic theorem (all gates/2D) — that stays open; document it as such.

## 4. Deliverables (paper-by-paper requirements)

### 4.1 NEW — Paper C: *The Decay Algebra: From Export Ledgers to a Continuum Entropy-Production Density*

Location: `papers/02-computational-models/PAPER_C_decay_algebra.md` (+ committed PDF).
Genre: technical, theorem-level, **classical, no gravity**. Depends on Paper A.

Required sections:
1. **Setup** — export identity recap (from Paper A); the sliding-window lattice; the extensivity question (Paper A path-dependence/non-additivity as the live obstruction).
2. **IDEM decay bounds export** — `H(X\|Y) ≤ Σ_y p(y)·#unrecoverable-coords`, exact iff product-preimage; O(N) enumeration-free density for erasure lattices. (`m11_idem`)
3. **The decay algebra (1D) + theorem** — boundary-belief transfer; the m11f theorem (`a=1−h_Y`, run-length chain, `π*`, `a=0.3007568`), with proof sketch.
4. **General-`w` theorem** — `(w−1)`-dependence existence; Blackwell representation; **reset ⇒ regeneration ⇒ renewal-reward**; dichotomy `exact ⇔ reset` (ties finiteness to the decay-vector's fully-recoverable branch). (m11g)
5. **2D strip transfer** — existence on ℤ²; strip operator; the `2^W` wall as motivation for the limit. (m11h)
6. **Continuum embedding** — local equilibrium; `σ(x)=a(θ(x))`; O(1/N) convergence table; `∫σ`. (m11i)
7. **Scope & non-claims** — `σ` is classical; **not** the load term; general hydrodynamic theorem open.
8. **Appendix R** — reproduce all five scripts with expected numbers.

Must-not-assert (Paper C): `σ ≡ γ|dS_c/dτ|`; continuum `L`/`G`; gravity; that witnessed rungs (m11h/i) are proved theorems where they are not.

### 4.2 Paper A — minimal update

- Add a closing "**Continuation**" note: the export identity (Thm 1) is the seed of Paper C's decay-algebra ladder; link Paper C.
- No change to A's theorems or scope. A stays the foundations.

### 4.3 Paper B — sharpen the reformulation bridge

- Replace the stub **O1 seed** (§7) with: "the discrete side of O1 is now built — the export ledger yields a constructive continuum entropy-production density `σ(x)` (Paper C)."
- State the reformulation bridge concretely: the open **semantic** step is now *"is `σ(x)` the continuum entropy-production density appearing in the load term `γ|dS_c/dτ|`?"* — a sharper, better-posed question than before, still **not** asserted (ties to `FALSIFIABILITY_L_vs_GR.md` term (2)).
- Keep all non-claims; Paper B remains a conjecture.

### 4.4 Integrated PAPER.md — substantive update

- **§5 (Classical microstructure)**: add a subsection "Decay algebra and the continuum density" summarizing m11f–i (with the proved/witnessed labels) and pointing to Paper C.
- **§1.1 (integration gap)** and **§10 (Synthesis)**: update the "central gap" narrative — the gap is now **bridged on the discrete side** (IDEM decay → export density → continuum `σ`), with the gravity identification as the remaining labeled semantic step.
- **§3 (Results)** / **Appendix A**: add the decay-algebra results and witnesses (`m11f–i`).
- **Non-claims banner**: append `σ ≠ load term` explicitly.
- Rebuild `PAPER.pdf` via `scripts/build_paper_pdfs.py` pattern.

### 4.5 Scope / claims artifacts

- `DELIVERY_SCOPE.md`: add Paper C's may-assert (C-list) / must-not-assert.
- `RESULTS_LEDGER.md`: already has R-O1a–d; ensure Paper-C mapping.
- `CURRENT_CLAIMS.md`: add the proved decay-algebra theorems (m11f/g) to the may-assert table with rigor labels; add `σ ≠ load term` to non-claims if not implied.

## 5. Git Pages requirements

- **New nav section "Computational entropy → continuum"**: pages for Paper C, and the `m11f`, `m11g`, `m11h`, `m11i` notes (allowlist in `scripts/sync_site_docs.py`).
- **Downloads page**: add Paper C PDF (build + commit source PDF; sync copies to `docs/pdf/`).
- **Homepage**: add a short "Latest research: the decay algebra" block linking Paper C + the continuum-density result, with the honest `σ ≠ load term` caveat.
- **Witness reproducibility page** (optional): a short page listing the five `m11_*` scripts and their expected outputs.
- Rebuild locally (`scripts/build_site.sh`), verify links + PDFs land in `site/`, and confirm on a clean-checkout sync (CI parity).

## 6. Guardrails (non-claims that MUST survive)

Every deliverable preserves: `σ` is a **classical** entropy-production density (not `γ|dS_c/dτ|`, not continuum `L(ρ,g)`, not gravity); `L ≠ G`; master equation ⇎ continuum GfE; Newton via Path J/M only; ACD-EW as analogy; frozen non-claims N1–N9. Rigor labels required on every bridge statement (proved / witnessed / structural / semantic).

## 7. Definition of Done

- [ ] **D-1** Paper C written (§1–8 + Appendix R), classical, no gravity; PDF built & committed.
- [ ] **D-2** Paper A "Continuation" note added.
- [ ] **D-3** Paper B O1 section rewritten around `σ`; reformulation bridge stated as an open semantic question; non-claims intact.
- [ ] **D-4** Integrated PAPER.md §5/§1.1/§10/§3/Appendix A + non-claims banner updated; PDF rebuilt.
- [ ] **D-5** `DELIVERY_SCOPE`, `RESULTS_LEDGER`, `CURRENT_CLAIMS` updated; `check_claim_hygiene.py` green.
- [ ] **D-6** Git Pages: nav + Paper C page + `m11f–i` pages + Downloads + homepage; `build_site.sh` clean; PDFs in `site/`; clean-checkout sync verified.
- [ ] **D-7** All five `m11_*` scripts run green; numbers in papers match script output.
- [ ] **D-8** Commit per deliverable; push to GitHub/Pages (the completion step).

## 8. Sequencing

```
Phase 1: Paper C (4.1) + scope/claims (4.5)         → the new core
Phase 2: Paper A note (4.2) + Paper B rewrite (4.3) → integrate into spine
Phase 3: Integrated PAPER.md (4.4) + PDFs           → the big synthesis
Phase 4: Git Pages (5) + build/verify               → publish surface
Phase 5: push (D-8)                                  → completion
```

## 9. Risks

- **Over-claiming the bridge** — mitigated by the `σ ≠ load term` guardrail in every file and the hygiene gate.
- **Paper sprawl** — Paper C must be self-contained and *classical*; resist folding gravity in.
- **PDF/CI drift** — Paper C PDF must be pre-built & committed (CI has no LaTeX), same as A/B.
- **Number drift** — papers cite script outputs verbatim; D-7 enforces re-run.

## 10. Changelog

| Date | Entry |
|------|-------|
| 2026-07-30 | PRD created: new Paper C + A/B/integrated updates + Git Pages, to document the m11f–i decay-algebra ladder. |
