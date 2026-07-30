# Delivery Scope — Three-Paper Contract

**Status:** Scope contract (written 2026-07-29; **Paper C added 2026-07-30**) · Preliminary research
**Governs:** Paper A (solid core), Paper C (decay algebra), Paper B (conjecture)
**Authority for claims:** [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md) · **Plan:** [DELIVERY_PLAN.md](DELIVERY_PLAN.md) · [PRD_decay_algebra_update.md](PRD_decay_algebra_update.md)

This file fixes, **before drafting**, what each paper **may assert** and **must not assert**. It is the boundary the drafts are checked against. If a draft needs to cross a boundary, amend this file first (with a changelog entry) — do not let scope drift silently.

---

## 0. Why three papers

The program has a **defensible classical core** and an **aspirational gravity conjecture**; keeping them separate stops the speculative half from contaminating the solid half. The core is now two papers: **Paper A** (definitions + Landauer-exact export) and **Paper C** (the decay algebra: from the export ledger to a continuum entropy-production density). **Paper B** carries the gravity reformulation as an explicit conjecture that *cites* A and C but does not claim their density is a load term.

| | **Paper A — solid core** | **Paper C — decay algebra** | **Paper B — conjecture** |
|---|---|---|---|
| Working title | *Computational Entropy: Output-Distribution Entropy and Landauer-Exact Export* | *The Decay Algebra: From Export Ledgers to a Continuum Entropy-Production Density* | *An Information-Theoretic Reformulation of Thermodynamic Gravity (Conjecture)* |
| Genre | Technical / theorem-level | Technical / theorem-level | Position / programme paper |
| Gravity content | **None** | **None** | Central, but explicitly conjectural |
| Depends on | Standard information theory | Paper A + ergodic theory (Blackwell, renewal-reward) | Papers A, C + imported GR/Jacobson |
| Publishable | Now | Now | As a research programme / preprint |

---

## 1. Paper A — may assert

- **A1** Computational entropy \(H_c(f;p_X) := H(Y)\) is the entropy of the induced **output** distribution of a map/channel (discrete Shannon; continuous differential; quantum von Neumann). Canonical: [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md).
- **A2** Informational equivalence: maps inducing the same output distribution have the same \(H_c\) (the \(\sqrt U\) vs \(\max(U_1,U_2)\) example).
- **A3** **Export identity:** for a computation \(X \to Y\), the local drop in system entropy is accounted for exactly by the export \(H(X\mid Y)\) (chain rule \(H(X)=H(Y)+H(X\mid Y)\)). Verified: `simulations/classical/m11_and_gate_ledger.py` (AND: \(H(Y)=0.811\), export \(=1.189\), chain error \(<10^{-12}\)).
- **A4** **Landauer-exactness:** single-shot \(L_S = H(X\mid Y)\) equals the erased-bit count in Landauer's \(Q \ge kT\ln 2 \cdot H(X\mid Y)\) (AND Protocol R). Verified: `m11_landauer_and_ledger.py`.
- **A5** **Path-dependence:** cumulative \(\sum L_S\) is path-dependent — same final \(H_c\), different total export via different circuits. Verified: `m11_composition_ledger.py`.
- **A6** **Invariant framing:** the coordinate-invariant carrier of "information imparted" is mutual information / relative entropy \(I(X;Y)\); differential entropy is used illustratively only (and its coordinate-dependence / possible negativity is stated explicitly).

## 1'. Paper A — must NOT assert

- No gravitational channel, load-as-time-dilation, master equation, or GfE content of any kind.
- No claim that toy \(H_c\) equals von Neumann \(S_c\) of any physical channel.
- No claim that the continuous differential entropy is itself a coordinate-invariant "information" measure (use \(I(X;Y)\) for that).
- No implication that the export ledger derives thermodynamics beyond the Landauer bound it instantiates.

---

## 1.5 Paper C — may assert

- **C1** Coupled export is **extensive** — a per-site density exists despite Paper A path-dependence/non-additivity (the latter saturate to an `O(1)` boundary). Verified: `m11_lattice_export_density.py`.
- **C2** **Decay bound:** the IDEM hard decay vector upper-bounds `H(X∣Y)`, **exact iff product-preimage** ⇒ `O(N)` enumeration-free density for erasure lattices. Verified: `m11_idem_export_density.py`.
- **C3** **1D density theorem** (proved): `a=1−h_Y=0.3007568`, `π★=(3−√5)/2`, via the run-length belief chain. `m11f` · `m11_decay_algebra.py`.
- **C4** **General-`w` theorem** (proved): existence via `(w−1)`-dependence; Blackwell representation on the `2^{w-1}` boundary simplex; **reset gates regenerate ⇒ renewal-reward**; dichotomy `exact ⇔ reset`. `m11g` · `m11_decay_algebra_general.py`.
- **C5** **2D strip transfer:** 2D density exists (finite-dependence); width-`W` transfer on the `2^W` row-cut; `2^W` wall. `m11h` · `m11_decay_algebra_2d.py`.
- **C6** **Continuum embedding** (witnessed): local equilibrium ⇒ `σ(x)=a(θ(x))=h_2(θ)−h_Y(θ)` at `O(1/N)`; `∫σ=0.29937`. `m11i` · `m11_continuum_embedding.py`.

## 1.5'. Paper C — must NOT assert

- No claim that `σ(x)` is the gravitational load term `γ|dS_c/dτ|`, continuum `L(ρ,g)`, or any metric `G`.
- No gravitational or spacetime content of any kind.
- No claim that the **witnessed** rungs (2D convergence-to-bulk, continuum embedding) are proved theorems where they are numerical; no claim of a general hydrodynamic theorem (all gates/2D) — that is open.
- No claim that the non-reset ⇒ non-atomic converse is proved (it is conjectural).

## 2. Paper B — may assert

- **B1** A **reformulation stance**: gravity's thermodynamic/entropic character can be *re-expressed* in the computational-entropy / load vocabulary. This is a reframing, **contingent** on a falsifiable departure being found (see Phase 2 verdict).
- **B2** The gravitational channel \(\Phi_g\) and load \(L\) as **defined objects** (canonical: [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)), with the master equation presented as a **Jacobson-shaped postulate**, not a derivation.
- **B3** **Newton via Path J/M only:** Clausius → Einstein (Jacobson 1995, *imported*) → weak-field GR → Poisson; \(\alpha\beta = 4\pi G/c^4\) as an **on-shell calibration**. Honestly flagged as *not* a free derivation of Newton or \(G\).
- **B4** **M6 result:** both frameworks reach the same leading Poisson equation via Einstein/GR (**WEAK PASS**), which is **not** framework equivalence (**FAIL identity**); next-order structures diverge (structural FAIL).
- **B5** The ACD-EW heat-vs-PM construction as an **analogy / Euclidean warm-up pattern only** — explicitly noting Perona–Malik edge-preserving diffusion is prior art and the gravity payoff is analogical.
- **B6** A stated **falsifiability question** and its Phase-2 verdict as the paper's central open problem.
- **B7** (Optional) The **O1 seed**: a single-slot (\(L_S\)) continuum-limit sketch, presented as a *first step / open direction*, not a completed construction.

## 2'. Paper B — must NOT assert (frozen non-claims N1–N9)

- Master equation \(\Leftrightarrow\) Bianconi continuum GfE (N1).
- \(L \equiv G\); \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\); \(\alpha_L\beta_L \equiv \alpha_B/\beta_B\) (N2).
- Newton from pointwise \(\Phi\propto\rho\) Laplacian — withdrawn (N5).
- Next-order \(\gamma_L,\delta_L\) equal GfE \(D_{\mu\nu},\Lambda_G\) (N6).
- Completed recovery of Schwarzschild / black holes / cosmology / inflation / Lloyd bounds (aspirational only).
- Lattice denoising = empirical gravity (N7).
- External GfE papers established on par with GR (N8).
- IDEM/decay fully constructs continuum \(L\) or \(G\) (N9, open).
- A free first-principles value of Newton's \(G\) from bits/load alone.

---

## 3. Shared rules

- Every bridge mapping carries a **semantic / structural / constructive** label.
- Type safety: load \(L\) is a dimensionless scalar; structure-induced \(G\) is a metric. \(L \neq G\).
- Prefer under-claiming. When in doubt, downgrade the rigor label.
- Reproducible code artifacts are cited by path and must run green before a claim relying on them ships.
- Run [../synthesis/CLAIM_GATE.md](../synthesis/CLAIM_GATE.md) checks before asserting any item closed.

---

## 4. Cross-reference map

| Claim family | Source of truth |
|--------------|-----------------|
| \(H_c\)/\(S_c\) definition (A1–A2) | [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) |
| Export / Landauer / path-dep (A3–A5) | `simulations/classical/m11_*_ledger.py` · [../synthesis/m11-idem-to-load.md](../synthesis/m11-idem-to-load.md) |
| \(\Phi_g\), \(L\), master eq (B2) | [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) |
| Newton Path J/M (B3) | [../emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) |
| M6 WEAK PASS / FAIL (B4) | [../synthesis/m6-weak-field-plugtest.md](../synthesis/m6-weak-field-plugtest.md) |
| ACD-EW analogy (B5) | [../synthesis/action-channel-duality-euclidean.md](../synthesis/action-channel-duality-euclidean.md) |
| Frozen non-claims | [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md) §3 |

---

## 5. Changelog

| Date | Entry |
|------|-------|
| 2026-07-29 | Initial scope contract: Paper A (A1–A6) and Paper B (B1–B7) boundaries fixed. |

*Amend this file (with a changelog entry) before any draft crosses a scope boundary.*
