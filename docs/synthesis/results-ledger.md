# Results Ledger — Proved / Rigor-Label / Open (consolidated)

**Status:** Consolidated ledger (written 2026-07-29) · Preliminary research
**Purpose:** One table replacing the parallel numbering schemes (M/D/P/O/W, tags A–E) for at-a-glance status. The older schemes remain valid in their source files; this is the single **entry point** for "what is established vs open."
**Authority:** [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) (frozen may-assert / non-claims) · **Papers:** [../papers/DELIVERY_SCOPE.md](../papers/DELIVERY_SCOPE.md)

---

## How to read

- **Rigor labels:** `proved` (theorem on a finite/standard model) · `analytic` · `hybrid` (analytic + Monte-Carlo/ensemble) · `calibration` (fixed by matching) · `structural` · `semantic` · `imported` (external theorem) · `open`.
- **Paper:** which deliverable carries it — **A** (solid core), **B** (conjecture), or **—** (internal only).
- This ledger does not restate proofs; it links the source of truth.

---

## 1. Established (may assert)

| ID | Result | Rigor | Paper | Source |
|----|--------|-------|-------|--------|
| R-A1 | \(H_c\)/\(S_c\) = entropy of channel **output** distribution | definition | A | [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) |
| R-A2 | Informational equivalence (same \(p_Y\) ⇒ same \(H_c\)); \(\sqrt U\) vs \(\max\) example | proved | A | Paper A §1.1 |
| R-A3 | **Export identity:** \(H(X)-H(Y)=H(X\mid Y)\) (chain-rule remainder) | proved | A | Paper A §3 · `m11_and_gate_ledger.py` |
| R-A4 | **Landauer-exactness:** \(L_S=H(X\mid Y)\) = erased-bit count in \(Q\ge kT\ln2\,H(X\mid Y)\) | proved | A | Paper A §4 · `m11_landauer_and_ledger.py` |
| R-A5 | **Path-dependence** of cumulative \(\sum L_S\) (1.189 vs 2.189; gap 1 bit) | proved | A | Paper A §5 · `m11_composition_ledger.py` |
| R-A6 | Invariant carrier = \(I(X;Y)\)/KL; differential entropy illustrative only | proved/semantic | A | Paper A §6 |
| R-B3 | Newton via **Path J/M** only; \(\alpha\beta=4\pi G/c^4\) on-shell | imported + calibration | B | [../emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) |
| R-B4 | M6: shared leading Poisson (**WEAK PASS**); **FAIL** framework identity; next-order structural FAIL | analytic/structural | B | [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) |
| R-B5 | ACD-EW Euclidean dual = **analogy/pattern only** (Perona–Malik prior art) | structural/hybrid | B | [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) |
| R-B6 | Falsifiability **verdict: reformulation**; entropy-production term = sole candidate departure | analysis | B | [../papers/FALSIFIABILITY_L_vs_GR.md](../papers/FALSIFIABILITY_L_vs_GR.md) |
| R-O1a | **1D decay-algebra density theorem**: for the nearest-neighbour AND lattice the export density \(a=\lim E(k)/k\) exists \(=1-h_Y=0.3007568\), computed by a local belief-transfer recursion; \(E(k)=ak+b+o(1)\) | **proved** | — (feeds B) | [m11f-decay-algebra-theorem.md](m11f-decay-algebra-theorem.md) · `m11_decay_algebra.py` |

*(Legacy IDs: R-A* subsume P1–P4 + Paper A theorems; R-B3=P7; R-B4=P10/P11; R-B5=P8/P9.)*

## 2. Open (must not assert; needs new theory)

| ID | Missing theorem / construction | Bucket | Legacy |
|----|-------------------------------|--------|--------|
| O-1 | Continuum limit of **one** load slot (\(L_S\) density) — or obstruction. *Witnesses PASSED*: coupled-AND export extensive w/ well-defined bulk density, path-dependence subleading (`m11_lattice_export_density.py`, 2026-07-29); IDEM decay vector upper-bounds export, **exact for product maps** ⇒ \(O(N)\) enumeration-free density (`m11_idem_export_density.py`); **decay algebra** (boundary-belief transfer) closes the coupled gap for 1D nearest-neighbour, matching enumeration to \(<10^{-8}\) via a local \(O(R)\) recursion (`m11_decay_algebra.py`, 2026-07-30). Open: general graphs / range-\(r\) coupling + entropy-rate limit theorem. | B | O1, N9 |
| O-2 | Γ-convergence / BV of warm-up action; continuum residual dual | B | O2 |
| O-3 | Positive continuum/quantum \(S_c\) path (not \(H_c^{\rm toy}\equiv S_c\)) | B | O3 |
| O-4 | Lorentzian GfE lift **or** extended no-go | B | O4, N1 |
| O-5 | Central conjecture: departure regime for entropy-production term **or** degeneracy no-go | B→C | Phase 2 verdict |
| O-6 | Free \(G\)-from-bits, or no-go under program axioms | B | — |

## 3. Frozen non-claims (never assert without new work)

Mirror of [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) §3: N1 master eq ⇎ GfE · N2 \(L\not\equiv G\) · N3 no all-\(t\) residual dominance · N4 no soft-free T1′ · N5 no pointwise-\(\rho\) Newton · N6 \(\gamma_L,\delta_L\neq D_{\mu\nu},\Lambda_G\) · N7 lattice ≠ gravity · N8 GfE not on par with GR · N9 no continuum \(L\)/\(G\) from IDEM.

## 4. Closed threads (do not reopen as crisis)

| Thread | Status | Note |
|--------|--------|------|
| Heat/PM residual dual (M1/M2/T1′/\(U_\star\)) | **Closed** | Settled enough; Perona–Malik is prior art; gravity payoff analogical. Archive pending user sign-off. |
| Dual scorecard farming | **Deprioritized** | More ICs do not close any O-item. |

---

## 5. Crosswalk to legacy schemes

| Legacy scheme | Where it still lives |
|---------------|----------------------|
| P1–P11 conclusions | [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md) |
| O1–O5 avenues | [OPEN_AVENUES.md](OPEN_AVENUES.md) |
| W1–W6 withdrawn | [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md) |
| M1–M12 / D1–D15 board | [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) · [PACK_INDEX.md](PACK_INDEX.md) |
| Entropy-object tags A–E | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) |

*This ledger is the preferred entry point. Update it when an R-item or O-item changes status; keep legacy files as detailed sources.*
