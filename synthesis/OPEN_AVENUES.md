# Open Avenues — What Is Concluded vs What Needs New Theory or Experiment

**Status:** Living roadmap for **future research cycles** (written 2026-07-15; post D15 freeze)  
**Companion:** [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md) (P1–P11 · W1–W6 · O1–O5) · [FINAL.md](../papers/06-synthesis/FINAL.md) · [CLAIM_GATE.md](CLAIM_GATE.md)  
**Stance:** Preliminary research. Prefer under-claiming. This file does **not** reopen dual residual crisis or continuum identity claims.

---

## 0. Purpose

After the claim-freeze (FINAL program report v1.0), agents and collaborators need a clear map of:

1. What is **already concluded** under the freeze (do not re-prove as “crisis”).  
2. What **“needs new theory”** means (and does **not** mean).  
3. What would require **experiment / observation**.  
4. For each open avenue: the **missing theorem or construction** that would close it.

Use this file when planning a **new cycle** beyond editorial LaTeX/figures.

---

## 1. Three buckets (read this first)

| Bucket | Meaning | Typical work |
|--------|---------|----------------|
| **A — Concluded (this freeze)** | Assertable under current definitions, ledgers, and **imported** external inputs (Shannon, Landauer, Jacobson, GR weak field, Bianconi warm-up lit), with rigor labels and non-claims | Paper polish only; cite P1–P11 |
| **B — Needs new theory** | Not false—but **not yet constructed or proved**. Missing definitions, continuum limits, equivalence maps, Lorentzian lifts, pure analytic dual theorems | New math / modeling cycle; may still be “no experiment” |
| **C — Needs experiment** | A claim about **nature** (lab, GPS, cosmology, black-hole phenomenology as empirical test) after a sharp prediction exists | Observation / data; usually after B produces a prediction |

**“New theory” does *not* mean:** abandon computational entropy, or invent a rival slogan.

**“New theory” *does* mean:** additional **mathematical/structural work**—theorems, continuum constructions, matching maps, promotion rules—that this repo has **not** completed. More dual ICs or AND-gate scorecards do **not** close bucket B.

Often the pipeline is: **B (sharp prediction) → C (test)**. Many open items are still stuck in **B**.

---

## 2. Already concluded (bucket A) — do not reopen as main crisis

From [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md):

| ID | One-line |
|----|----------|
| **P1** | Computational entropy = **output** entropy \(H_c\) / \(S_c\) |
| **P2** | Local drop accounted by **export** \(H(X\mid Y)\) (chain rule) |
| **P3** | Single-shot \(L_S=H(X\mid Y)\) is Landauer erased-bit count (AND Protocol R) |
| **P4** | Cumulative \(\sum L_S\) is **path-dependent** |
| **P5–P6** | Three load **roles**; continuum \(L\) **motivated**, not identified with \(L^{\mathrm{disc}}\) |
| **P7** | Newton only **Path J/M**; \(\alpha\beta\) **calibration** |
| **P8** | Euclidean ACD-EW dual; T1′ / \(U_\star\); PCRH\(_b\) **soft** |
| **P9** | Layer W: PM energy descent + external warm-up flow cite |
| **P10** | M6 WEAK PASS Poisson / FAIL framework identity |
| **P11** | R4a: next-order identity needs **promotion** (structural no-go without it) |

**Withdrawn / refused (W1–W6):** pointwise \(\Phi\propto\rho\) Newton; all-\(t\) residual dual; \(L\equiv G\); ME ⇔ GfE; continuum \(L\)/\(G\) from IDEM ledgers; lattice = empirical gravity.

**Not open as crisis:** heat/PM residual dual scorecard farming.

---

## 3. Open avenues — missing theorems / constructions (bucket B)

Each row: **what we have**, **what we must not claim yet**, **missing theorem (statement only)**, **suggested first step**, **experiment later?**

### O1 — Continuum / hydrodynamic limit of discrete load and IDEM

| | |
|--|--|
| **Have** | Finite \(L^{\mathrm{disc}}\); composition laws; m11c **role** motivation; coupled-region ledgers |
| **Have (2026-07-29 witness)** | **Fast-fail PASSED** (`simulations/classical/m11_lattice_export_density.py`): for coupled AND lattices the block export \(E(k)=H(X\mid Y)\) is **extensive** — linear in \(k\) with a well-defined bulk density (shared-input \(a\approx 0.301\) bits/site, residual \(\sim\!10^{-8}\); chained \(a\approx 0.999\), residual \(\sim\!10^{-4}\)). Publication-gauge / path-dependence surplus **saturates** to an \(O(1)\) boundary term (\(\approx 1.31\) bits), so per-site \(\to 0\) like \(1/k\). Discrete witness only — **not** a continuum-limit theorem. |
| **Have (2026-07-30 IDEM)** | **Decay↔export bound witnessed** (`simulations/classical/m11_idem_export_density.py`): for uniform inputs the IDEM hard decay vector gives \(H(X\mid Y)\le\sum_y p(y)\,\#\{\text{unrecoverable coords}\}\), **exact iff preimages are product subcubes**. ⇒ for product/erasure lattices the export density is read from local decay metadata in \(O(N)\), enumeration-free & exact; AND/majority/parity have a known strict gap. IDEM utility demonstrated; **not** a continuum claim. |
| **Have (2026-07-30 decay algebra)** | **Coupled gap CLOSED (1D)** (`simulations/classical/m11_decay_algebra.py`): promoting the hard decay flag to a **transported boundary belief** (a transfer operator) gives the coupled export density \(a=1-h_Y\) (input rate − output-HMM entropy rate) from a **local \(O(R)\) recursion**, matching the \(O(2^k)\) enumeration (0.30076) to \(<10^{-8}\). |
| **Have (2026-07-30 THEOREM)** | **PROVED** ([m11f-decay-algebra-theorem.md](m11f-decay-algebra-theorem.md)): for the 1D nearest-neighbour AND lattice the density \(a=\lim E(k)/k\) **exists** and **equals** \(1-h_Y\), \(h_Y=\sum_r\rho(r)h_2(p_1(r))\), with \(E(k)=ak+b+o(1)\); \(\pi_\star=(3-\sqrt5)/2\), \(a=0.3007568\). Ergodic theory + belief-filter run-length reduction. Constructive/algorithmic — still **not** a continuum theorem. |
| **Have (2026-07-30 GENERALIZED)** | **Range-\(r\) generalization witnessed** (`simulations/classical/m11_decay_algebra_general.py`): the belief transfer becomes an **operator on the \(2^{w-1}\) window states** (\(w=r+1\)); reproduces the enumerated density for AND/OR (\(w\le4\), exact, \(\sim10^{-6}\)) and threshold (\(w=3\), MC, \(\sim10^{-4}\)), recovering \(a=0.3007568\) at \(w=2\). |
| **Have (2026-07-30 general-\(w\) THEOREM)** | **PROVED** ([m11g-decay-algebra-general-w-theorem.md](m11g-decay-algebra-general-w-theorem.md)): for **any** gate/width, (T1) \(a=1-h_Y\) exists with \(E(k)=ak+O(1)\) via \((w{-}1)\)-dependence; (T2) \(h_Y=\mathbb E_{\mu^\star}[H(Y\mid\pi)]\) — Blackwell representation on the \(2^{w-1}\) belief simplex; (T3) **reset gates** (singleton-preimage output = fully-recoverable branch) make the filter **regenerate** ⇒ exact finite algebra by **renewal-reward**. Dichotomy `exact ⇔ reset` executably asserted. Non-reset ⇒ non-atomic \(\mu^\star\) is **conjectural**. Still **not** continuum. |
| **Must not claim** | \(L^{\mathrm{disc}}=L(\rho,g)\); IDEM constructs continuum metric \(G\); that the witnesses above are the limit theorem |
| **Have (2026-07-30 2D)** | **2D strip transfer** ([m11h-decay-algebra-2d.md](m11h-decay-algebra-2d.md), `m11_decay_algebra_2d.py`): plaquette AND on \(\mathbb Z^2\); density \(a_{2D}\) **exists** (finite-dependence, proved); width-\(W\) density \(a_W=(W-h_{\text{row}})/(W-1)\) computed by the transfer operator on the \(2^W\) row-cut (Blackwell via m11g), matches enumeration \(W=2,3\) to \(\sim10^{-3}\); \(a_W\) converges (1.684→1.193→1.031). Exposes the \(2^W\) **wall** ⇒ motivates continuum. |
| **Have (2026-07-30 CONTINUUM)** | **Continuum embedding witnessed** ([m11i-continuum-embedding.md](m11i-continuum-embedding.md), `m11_continuum_embedding.py`): with a smooth bias field \(\theta(x)\), the coupled per-site density converges **\(O(1/N)\)** (halving ratios \(1.48\!\to\!1.71\!\to\!1.88\!\to\!1.95\)) to the pointwise decay-algebra density \(\sigma(x)=a(\theta(x))=h_2(\theta)-h_Y(\theta)\) — **local equilibrium**. The discrete export ledger thus yields a **constructive continuum entropy-production density field**, \(\int\sigma\,dx=0.29937\). **Non-claim:** \(\sigma\neq\) load term \(\gamma\lvert dS_c/d\tau\rvert\) (semantic bridge only). |
| **Missing theorem (target)** | Decay algebra ladder: **proved** \(w=2\) (m11f), **general \(w\)/any gate** (m11g), **2D existence + strip** (m11h); **continuum density field \(\sigma(x)\) witnessed** at \(O(1/N)\) (m11i). **Discrete side of O1 complete.** Remaining: a general hydrodynamic **theorem** (all gates/2D), and the **semantic** step \(\sigma\leftrightarrow\) load term (reformulation; see FALSIFIABILITY). |
| **Suggested first step** | ~~lattice extensive~~/~~IDEM bound~~/~~1D algebra (m11f)~~/~~range-\(r\)+general-\(w\) theorem (m11g)~~/~~2D strip (m11h)~~/~~continuum embedding (m11i)~~ **all done — O1 discrete ladder built**. Next: (a) general hydrodynamic theorem; (b) the reformulation's semantic \(\sigma\leftrightarrow\gamma\lvert dS_c/d\tau\rvert\) step (labeled, not forced). |
| **Experiment?** | Only after a sharp continuum prediction exists. Pure limit theorem is **theory-only**. |

### O2 — Full warm-up continuum (Γ-limit, BV jumps, residual dual continuum)

| | |
|--|--|
| **Have** | M5b smooth \(O(h)\) action lemma sketch; M5c discrete PM energy descent; transfer dictionary |
| **Must not claim** | Γ-convergence; jump continuum dual; residual dual as continuum SPDE |
| **Missing theorem (target)** | *Γ-convergence* of mesh-weighted warm-up action to continuum integral on a stated space (e.g. \(W^{1,p}\) or SBV), **and/or** continuum residual dual theorem under a declared continuum channel—not residual MSE alone. |
| **Suggested first step** | Finish M5b constants; then Γ-limit on **smooth → \(H^1\)** only; defer BV until that is solid. |
| **Experiment?** | No—analysis. |

### O3 — Positive continuum \(S_c\) path (beyond non-identity of entropy objects)

| | |
|--|--|
| **Have** | M10 dictionary tags A–E; M10 P1 **non-identity** \(H_c^{\mathrm{toy}}\neq H(Z)\); canonical \(S_c=S(\Phi(\rho))\) |
| **Must not claim** | \(H_c^{\mathrm{toy}}\equiv S_c\); dual residual = von Neumann dynamics |
| **Missing theorem (target)** | *A constructive continuum (or quantum) channel* \(\Phi_t\) *on a state space \(\rho\) such that* \(S_c(\Phi_t;\rho)\) *is related by inequality or limit to a declared classical object*—without equating residual dual scores by fiat. |
| **Suggested first step** | Classical continuum channel first (e.g. diffusion semigroup on densities): \(S_c\) or differential entropy along the flow vs residual quality functionals. |
| **Experiment?** | Optional later if a lab-accessible channel is defined. |

### O4 — Lorentzian / full GfE lift and true continuum dual (M9)

| | |
|--|--|
| **Have** | Euclidean warm-up dual (ACD-EW); M6 weak-field co-class via GR; R4a promotion no-go |
| **Must not claim** | Lorentzian GfE = master equation; dual toys = spacetime gravity |
| **Missing theorem (target)** | *A Lorentzian (or pseudo-Riemannian) extension* of the warm-up dual **or** a theorem that **no** such extension preserves stated axioms without promotion—either is progress. Full ME ⇔ GfE remains a separate, stronger claim (likely false without new structure). |
| **Suggested first step** | Dictionary-only Lorentzian lift **or** precise no-go extending R4a; do not start scorecards. |
| **Experiment?** | Cosmology/BH tests only after a prediction; currently **theory-first**. |

### O5 — Optional pure dual / true game channel / other recoveries

| Sub-item | Missing piece | Bucket |
|----------|---------------|--------|
| Pure pathwise PCRH\(_b\) (no MC soft spot) | Analytic theorem replacing ensemble certificate on \(U_\star\) | **B** (analysis of existing dual) |
| M12 true game \(H_c^{\mathrm{game}}\) (not belief dual) | Exact multiset / strategy channel + load ledger at scale | **B** (classical construction); EV claims need care |
| BH / cosmology / Lloyd recoveries at Path J/M honesty | Rewrite each recovery like Newton Path J/M (external inputs + calibration) | **B** then optional **C** |

**Suggested first step for O5:** pure PCRH\(_b\) only if writing a dual math SI; otherwise treat dual as closed.

---

## 4. Free derivation of \(G\) / “gravity from bits alone”

| | |
|--|--|
| **Have** | Path J/M with \(\alpha\beta=4\pi G/c^4\) as **on-shell calibration** after importing Einstein/Jacobson |
| **Must not claim** | Free first-principles value of Newton’s \(G\) from AND-gates or load alone |
| **Missing theory** | A foundational derivation of \(G\) (or of Einstein equations) **without** importing GR/Jacobson—or an explicit **no-go** under program axioms |
| **Bucket** | **B** (foundations); not closed by current freeze |
| **Experiment?** | Measuring \(G\) does not substitute for the derivation claim |

---

## 5. Experiment bucket (C) — only after predictions

Examples of claims that are **not** settled by pure math, and are **not** the same as O1–O4:

| Experimental / observational claim | Prerequisite theory |
|------------------------------------|----------------------|
| Load-gated clocks appear in precision timing / GPS | Continuum \(L\) + weak-field prediction (O1 + Path M sharpened) |
| **Entropy-production clock effect at fixed energy** (dephasing regime) | Regime program: [../papers/REGIME_PROGRAM_dSc_decoupling.md](../papers/REGIME_PROGRAM_dSc_decoupling.md) — R1 dephasing / R2 erasure / R3 scrambling; Stage-1 model witness → \(\gamma\)-magnitude → precision clocks |
| Dual residual pattern appears in a physical imaging/thermal system | Map Layer D to a real apparatus (not automatic) |
| Cosmological \(\Lambda_G\) or GfE BH corrections match data | Full continuum GfE + parameter map (O4 + external lit) |

**Do not** claim lattice denoising validates gravity (W6 / N7).

---

## 6. What does *not* need new theory (editorial / packaging)

| Task | Bucket |
|------|--------|
| LaTeX, figures, bibliography formatting of FINAL.md | Editorial |
| Human voice polish | Editorial |
| Re-running ledgers / claim hygiene | Regression |
| Another dual IC scorecard | **Deprioritized** — does not close O1–O4 |

---

## 7. Suggested priority for a *new* research cycle

If starting a cycle **after** reading FINAL + PROGRAM_CONCLUSIONS:

| Priority | Avenue | Why |
|----------|--------|-----|
| **1** | **O1** one-slot continuum density (export/\(L_S\)) | Highest strategic value; closes Stage-1 → continuum honesty |
| **2** | **O2** smooth/H¹ Γ or fully rigorous M5b constants | Strengthens Layer W without Lorentzian cost |
| **3** | **O3** classical continuum channel vs residual functionals | Blocks object confusion permanently with positive structure |
| **4** | **O5** pure PCRH\(_b\) | Dual SI polish only |
| **5** | **O4** Lorentzian dictionary or extended no-go | High cost; after O1–O2 |
| **—** | Dual scorecard farm | Avoid |

Always run [CLAIM_GATE.md](CLAIM_GATE.md) before claiming any O-item closed.

---

## 8. One-screen summary

```text
CONCLUDED (freeze): P1–P11, W1–W6 — see PROGRAM_CONCLUSIONS.md / FINAL.md

“NEW THEORY” = missing math/construction, NOT “wrong program”
  O1 continuum L limit / IDEM→fields
  O2 Γ / BV / residual continuum
  O3 positive S_c path (not H_c^toy ≡ S_c)
  O4 Lorentzian GfE / true continuum dual
  O5 pure PCRH_b; true game H_c; honest BH/cosmo recoveries
  + free G-from-bits (foundational)

EXPERIMENT = nature tests after sharp predictions (usually after O1/O4)

DO NOT: dual IC churn; L≡G; ME⇔GfE; lattice=gravity
```

---

## 9. Maintenance

- When an O-item closes, update: this file, [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md), [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md), [PROGRESS_REPORT.md](../PROGRESS_REPORT.md), and FINAL/DRAFT non-claims if needed.  
- Append a short **Changelog** entry below rather than silent rewrites.

### Changelog

| Date | Entry |
|------|--------|
| 2026-07-15 | Initial OPEN_AVENUES: buckets A/B/C; O1–O5 missing theorems; priority for next cycle |
| 2026-07-29 | O1 fast-fail witness PASSED (`m11_lattice_export_density.py`): coupled-AND export extensive with well-defined bulk density; path-dependence saturates to O(1) boundary (per-site → 0). Reframed as reformulation. Next: IDEM map family + entropy-rate limit theorem. |
| 2026-07-30 | IDEM decay↔export bound witnessed (`m11_idem_export_density.py`): hard decay vector upper-bounds H(X\|Y), exact for product/erasure maps ⇒ O(N) enumeration-free density. IDEM utility shown. Next: decay algebra under coupling + limit theorem. |
| 2026-07-30 | Decay algebra (`m11_decay_algebra.py`): boundary-belief transfer closes the coupled gap for 1D nearest-neighbour (density 0.30076 from O(R) local recursion, matches enumeration <1e-8). Next: general graphs / range-r; entropy-rate limit theorem. |
| 2026-07-30 | **1D density THEOREM proved** ([m11f-decay-algebra-theorem.md](m11f-decay-algebra-theorem.md)): a=lim E(k)/k exists = 1−h_Y via ergodicity + run-length filter reduction; π*=(3−√5)/2, a=0.3007568. Numeric witness verifies constants. Open: general graphs; continuum embedding. |
| 2026-07-30 | **Range-r generalization** (`m11_decay_algebra_general.py`): belief transfer operator on 2^{w-1} window states matches enumeration for AND/OR (w≤4, exact) & threshold (w=3, MC); recovers a=0.3007568 at w=2. Finding: exact-finite algebra ⇔ reset gate ([0,..,0] decay branch). Open: general-w theorem, 2D, continuum. |
| 2026-07-30 | **General-w THEOREM proved** ([m11g](m11g-decay-algebra-general-w-theorem.md)): any gate/width — a=1−h_Y exists ((w−1)-dependence); Blackwell transfer representation; reset gates regenerate ⇒ exact renewal-reward. Dichotomy exact⇔reset asserted in code. Non-reset non-atomicity conjectural. Open: 2D, continuum. |
| 2026-07-30 | **2D strip transfer** ([m11h](m11h-decay-algebra-2d.md), `m11_decay_algebra_2d.py`): 2D density exists (finite-dependence, proved); width-W strip operator on 2^W row-cut matches enumeration (W=2,3, ~1e-3), a_W converges 1.684→1.193→1.031. 2^W wall motivates continuum. Open: continuum embedding (final rung). |
| 2026-07-30 | **Continuum embedding** ([m11i](m11i-continuum-embedding.md), `m11_continuum_embedding.py`): smooth bias field ⇒ coupled density → σ(x)=a(θ(x)) at O(1/N) (ratios 1.48→1.95), local equilibrium. Discrete ledger yields a constructive continuum entropy-production density field, ∫σ=0.29937. O1 discrete ladder complete. Non-claim: σ≠ load term (semantic bridge). |

---

*Living document for post-freeze research avenues. Prefer under-claiming.*
