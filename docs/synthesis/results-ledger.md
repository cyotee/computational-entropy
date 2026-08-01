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
| R-O1b | **General-\(w\) decay-algebra theorem** (any gate, sliding window \(w\)): \(a=1-h_Y\) exists (\((w{-}1)\)-dependence), \(h_Y=\mathbb E_{\mu^\star}[H(Y\mid\pi)]\) via the \(2^{w-1}\)-state belief-transfer operator (Blackwell), and **reset gates regenerate** ⇒ exact renewal-reward. Dichotomy exact\(\Leftrightarrow\)reset. | **proved** (non-atomicity converse conjectural) | — (feeds B) | [m11g-decay-algebra-general-w-theorem.md](m11g-decay-algebra-general-w-theorem.md) · `m11_decay_algebra_general.py` |
| R-O1c | **2D strip transfer**: plaquette-AND density \(a_{2D}\) exists on \(\mathbb Z^2\) (finite-dependence); width-\(W\) density \(a_W=(W-h_{\text{row}})/(W-1)\) via the transfer operator on the \(2^W\) row-cut, matches enumeration to \(\sim10^{-3}\); \(a_W\) converges. | **proved** (existence + width-\(W\)); convergence-to-bulk numerical | — (feeds B) | [m11h-decay-algebra-2d.md](m11h-decay-algebra-2d.md) · `m11_decay_algebra_2d.py` |
| R-O1d | **Continuum embedding**: with a smooth bias field \(\theta(x)\), the coupled per-site export density → the pointwise decay-algebra density \(\sigma(x)=a(\theta(x))\) at **\(O(1/N)\)** (local equilibrium). Discrete ledger ⇒ **constructive continuum entropy-production density field** \(\sigma\), \(\int\sigma=0.29937\). \(\sigma\neq\) load term (semantic bridge only). | **witnessed** (1D family; general theorem open) | — (feeds B) | [m11i-continuum-embedding.md](m11i-continuum-embedding.md) · `m11_continuum_embedding.py` |

*(Legacy IDs: R-A* subsume P1–P4 + Paper A theorems; R-B3=P7; R-B4=P10/P11; R-B5=P8/P9.)*

## 2. Open (must not assert; needs new theory)

| ID | Missing theorem / construction | Bucket | Legacy |
|----|-------------------------------|--------|--------|
| O-1 | Continuum limit of **one** load slot (\(L_S\) density) — or obstruction. *Witnesses PASSED*: coupled-AND export extensive (`m11_lattice_export_density.py`); IDEM decay upper-bounds export, exact for product maps (`m11_idem_export_density.py`); **decay algebra** closes the 1D gap (`m11_decay_algebra.py`), **proved** as theorem R-O1a (`m11f`); **generalized** to range-\(r\)/multi-gate via a \(2^{w-1}\)-state transfer operator, exact for reset gates (`m11_decay_algebra_general.py`, 2026-07-30). Open: general-\(w\) theorem, 2D strip, continuum embedding. | B | O1, N9 |
| O-2 | Γ-convergence / BV of warm-up action; continuum residual dual | B | O2 |
| O-3 | Positive continuum/quantum \(S_c\) path (not \(H_c^{\rm toy}\equiv S_c\)) | B | O3 |
| O-4 | Lorentzian GfE lift **or** extended no-go | B | O4, N1 |
| O-5 | Central conjecture: departure regime **or** no-go. **Load-clock: NO-GO** (load is a diagnostic co-moving with the Path-J/M metric; \(\alpha L=-\Phi/c^2\) is \(T_{\mu\nu}\)-fixed while the entropy term varies at fixed \(T_{\mu\nu}\); [load-dim](../emergent-gravity/load-dimensional-analysis.md) · `regime_*`). **R4a promotion: CANDIDATE, but the DERIVED sign is disfavored.** Promotion is Bianchi-consistent and reduces to \(\Lambda\)CDM (\(\xi\to0\)); it departs as **phantom** interacting dark energy \(w_0=-1-0.143\xi\le-1\) ([r4a](../emergent-gravity/r4a-promotion.md) · `r4a_frw_promotion.py`). **Sign/EoS** (`r4a_sign_*`, `r4a_eos_test.py`): dissipation/phantom end is **thermal** \((w\ge0)\), **cannot be dark energy** ⇒ **phantom retracted** (EoS-inconsistent). Only a \(w\approx-1\) reservoir is a viable dark sector. **Path 1** (`r4a_reservoir_eos.py`, data-independent): the framework does **not force** \(w\approx-1\) — the load identifies the scalar's *kinetic* term with the active flux \(\lvert dS_c/d\tau\rvert\), so the emphasized high-flux regime is \(w\to+1\) (stiff, not DE); \(w\approx-1\) holds **only in the idle/low-flux regime** (the de-emphasized stockpile). Dynamics lean **freezing** \((w_a>0)\) — wrong side of the DESI hint; §4d thawing **retracted**. | clock closed; phantom retracted (EoS); reservoir-DE **not grounded** (idle-only + likely wrong-sign \(w_a\)); no clean data-consistent departure | Phase 2; regime; PRD; R4a; w(z); sign; EoS; Path 1 |
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
