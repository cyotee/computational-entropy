# M5 — Continuum Warm-Up Hygiene (ACD-EW / PM / \(G=1+\alpha(\nabla\phi)^2\))

**M-id:** M5 (hygiene deepen)  
**Status:** **Honesty boundaries frozen; full \(h\to 0\) Γ-convergence still open**  
**Scope:** What “continuum warm-up limit” may mean for **Euclidean GfE warm-up only** — not Lorentzian modified Einstein, not master equation  
**Historical / technical parent:** [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) (citation bridge + smooth FD sketch; **do not rewrite** that history)  
**Smooth-only action lemma (M5b):** [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) — conditional \(O(h)\) Riemann-sum limit for \(C^3\) \(\phi\); **not** Γ-convergence / jumps  
**PM gradient-flow / discrete descent (M5c):** [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) — Layer W continuum lit link + discrete Euler energy sketch  
**Transfer dictionary:** [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md)  
**Formal dual:** [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md)  
**Gravity contact contrast:** [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) (Poisson WEAK PASS is a **different layer**)  
**Date:** 2026-07-14  
**Stance:** Preliminary research. Under-claim. **No** master equation \(\Leftrightarrow\) GfE. **No** Γ-convergence claimed proved.

---

## 0. Purpose of this note

[m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) records:

- literature identification of lattice toys with Bianconi Euclidean warm-up,
- a **target** T4 continuum statement,
- a **smooth** finite-difference consistency **sketch**.

This hygiene note **does not replace** that file. It freezes **what agents may write** when they say “continuum limit,” “warm-up,” or “PM = GfE,” and what they must not transfer upward.

---

## 1. What “continuum warm-up limit” means **here**

### 1.1 Objects in scope (only these)

| Object | Discrete (joint toys / ACD-EW) | Continuum warm-up target |
|--------|-------------------------------|---------------------------|
| Domain | Lattice sites / edges, mesh \(h\) | Domain \(\Omega\subset\mathbb{R}^d\) or torus (Euclidean) |
| Field | \(\phi\in\mathbb{R}^N\) | \(\phi:\Omega\to\mathbb{R}\) (Sobolev / BV as needed) |
| Support metric | \(g\equiv 1\) (flat) | \(g=\mathrm{Id}\) (flat Euclidean) |
| Induced metric | \(G_i=1+\alpha_G(\nabla_h\phi)_i^2\) (1D); mean-squared forward grads (2D) | \(G=g+\alpha(\nabla\phi)\otimes(\nabla\phi)\) → 1D \(G=1+\alpha|\phi'|^2\) |
| Action | \(S_{\mathrm{GfE}}^h=-\sum_i\ln G_i\) (or \(h\sum\)) | \(\int -\ln(1+\alpha|\nabla\phi|^2)\,dx\) (warm-up density) |
| Dynamics | Explicit Euler PM (Catte-regularized in 2D) | Continuum Perona–Malik / Catte anisotropic diffusion |
| Observation dual | \(y=\phi_\star+\eta\); heat / PM / load-PM reconstructors | **Same story only if** observation model is stated in continuum; not automatic |

**Type safety (reaffirmed):** load \(L\) (scalar) \(\neq\) metric \(G\). Continuum limit of \(G_i\) is **not** a limit of \(L_{\mathrm{clock}}\).

### 1.2 Working definition (hygiene)

> **Continuum warm-up limit (project sense):**  
> A statement that discrete warm-up **geometry and PM dynamics** — \(G^h[\phi^h]\), \(S_{\mathrm{GfE}}^h\), Euler PM with \(dt=O(h^2)\) — converge, in a specified topology (strong \(C^1\), weak Sobolev, Γ-convergence, SPDE, …), to the **Euclidean scalar warm-up** analyzed by Bianconi (*Beyond holography* / GfE warm-up), **not** to Lorentzian GfE field equations and **not** to \(\partial_\tau\rho=\mathcal{L}_g\rho\).

Anything outside that sentence is a **different** limit problem and must be named differently (e.g. “Lorentzian GfE continuum,” “master-equation continuum,” “network-to-manifold limit”).

### 1.3 What is **not** included in “warm-up continuum”

| Excluded object | Why |
|-----------------|-----|
| Full Bianconi \(G=\tilde g+\alpha\tilde M-\beta\tilde{\mathcal{R}}\) | Curvature-in-\(G\), topological forms — M9 / full GfE, not warm-up |
| G-field, \(\Lambda_G\), modified Einstein | Continuum Stage-3 macro; not lattice dual layer |
| \(\Phi_g\), density operator \(\rho\), \(S_c=S(\Phi_g(\rho))\) | Quantum / gravity Stage-1 (see [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md)) |
| Continuum three-term \(L(\rho,g)\) | Only clock **form** mirrored in toys |
| Path J/M Newtonian Poisson | Gravity-facing GR layer ([m6](m6-weak-field-plugtest.md)); independent of PM mesh limit |
| Residual dual for all continuum \(\phi_\star\) | T1′ is discrete / toy-windowed; continuum PDE residual dual open |

---

## 2. Literature-backed vs open (repo honesty)

### 2.1 Literature-backed (may cite as **external**)

| Claim | Source | Our use | Rigor in **this** repo |
|-------|--------|---------|------------------------|
| Euclidean GfE warm-up: relative entropy / action between support metric and matter-/image-induced metric | Bianconi, *Gravity from entropy* (arXiv:2408.14391 / PRD 2025) warm-up discussion | Continuum **target** of T4 | **External** (not re-derived) |
| Perona–Malik anisotropic diffusion = gradient flow of that Euclidean warm-up | Bianconi, *Beyond holography* (arXiv:2503.14048) | Justifies PM as Stage-3 warm-up dynamics **and** dual reconstructor | **Structural / literature**; toys are **constructive discretizations** |
| Low-coupling GfE → EH (then Newton via GR) | Bianconi GfE + standard GR | M6 WEAK PASS context only | **External + GR**; **≠** warm-up mesh limit |

**Allowed citation sentence:**

> *Joint toys discretize Bianconi’s Euclidean GfE warm-up (\(G=1+\alpha|\nabla\phi|^2\), action \(-\sum\ln G\), PM flow), following the continuum identification in* Beyond holography*; they do not implement Lorentzian modified Einstein equations.*

### 2.2 Open in this repo (must not claim proved)

| Claim | Status in repo |
|-------|----------------|
| Full **Γ-convergence** of \(S_{\mathrm{GfE}}^h\to\int -\ln(1+\alpha|\nabla\phi|^2)\,dx\) on \(H^1\) / BV | **Open** (T4 target; [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) §3) |
| Continuum limit of **jump / BV** solutions of discrete Euler PM | **Open** (forward–backward continuum PM is delicate) |
| SPDE / continuum limit of **noisy** observation + reconstructor dual (T1′ in continuum) | **Open** |
| Rate of convergence \(O(h)\) for **action** on smooth \(\phi\in C^3\) | **Conditional lemma** [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md); PM flux still sketch-only in T4 §4 |
| Load-gated clock \(dt/(1+\alpha_L L)\) continuum limit as geometric proper time | **Not** a warm-up theorem; form analogy only |
| 2D Catte scheme → continuum Catte–PM as \(h\to 0\) with residual dual preserved | **Open** (toys: constructive 6/6 pattern only) |

### 2.3 Settled **inside** the repo (warm-up layer only)

| Settled | Pointer |
|---------|---------|
| Dictionary lattice \(\leftrightarrow\) continuum warm-up objects | m5 T4 §2; this note §1 |
| Smooth FD **consistency sketch** (gradient, Riemann sum, PM flux, CFL) | m5 T4 §4 |
| Smooth **action** \(O(h)\) conditional lemma (\(C^3\), mesh-weighted \(S_h\)) | [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) |
| PM = warm-up gradient flow (external) + discrete \(E_h\) descent sketch | [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) |
| ACD-EW constructive dual on fixed lattices (1D/2D) | ACD-EW; scorecards 6/6 |
| Residual dual **pattern** time-windowed (T1′ / \(U_\star\)) on discrete 1D toy | CURRENT_CLAIMS; **not** continuum SPDE theorem |

---

## 3. Transferable vs non-transferable (to Lorentzian GfE / master equation)

**Canonical long form:** [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) §§3–4.  
Below is the **M5-scoped** checklist: what a continuum warm-up result (if obtained) would and would not license.

### 3.1 Transferable **if** warm-up continuum (T4) is later proved

These transfer as **program templates**, still conditional language only:

| Item | Transfers as | Does **not** become |
|------|--------------|---------------------|
| Stage-1 → Stage-2 → Stage-3 workflow | Architectural scaffold | Field-equation identity |
| Induced \(G\) from structure gradients | Role of Stage-2 imprint | Full \(\tilde G\) with curvature-in-\(G\) |
| PM as structure-preserving channel reading | Research principle | \(\Phi_g\) CPTP dynamics |
| Split load \(L_E+L_S\) template | Multi-component demand idea | Continuum \(L(\rho,g)\) formula |
| Clock factor \(1/(1+\alpha L)\) | Formal analogy to \(d\tau\) | Derivation of proper time from relative entropy of metrics |
| Euclidean robustness 1D→2D | Mild support for image/PDE link in *Beyond holography* | Lorentzian well-posedness |

### 3.2 Non-transferable (even after T4)

From transfer dictionary §4, specialized to continuum warm-up:

| Must not transfer | Reason |
|-------------------|--------|
| Master equation \(\Leftrightarrow\) full continuum GfE | Different primary objects and dynamics |
| \(L\equiv G\), \(H_c\equiv S_{\mathrm{GfE}}\), \(H_c^{\mathrm{toy}}\equiv S_c\) | Type / functional mismatch ([m10](m10-sc-vs-toy-hc.md)) |
| Lattice residual dual ⇒ Newtonian gravity or BH physics | Wrong phenomenology layer (see M6: Poisson is GR weak-field, not PM) |
| Warm-up mesh limit ⇒ modified Einstein + \(\Lambda_G\) | Warm-up omits curvature-in-\(G\), G-field |
| Discrete load-gating ⇒ continuum Clausius/Jacobson Path J | Path J imports Einstein thermodynamically; independent of PM |
| External GfE inflation / spherical BH papers as outputs of toys | GfE applications, not ACD-EW results |

### 3.3 Layer separation (agents: do not mix)

```text
Layer W — Euclidean warm-up continuum (M5 / T4)
  G = 1+α|∇φ|², PM, lattice→PDE
        │  (no automatic lift)
        ▼
Layer D — ACD-EW dual (constructive lattices)
  H_c^toy, L_clock, T1′ residual windows
        │  (no automatic lift)
        ▼
Layer G — Continuum GfE Lorentzian / full action
  relative entropy of metrics, modified Einstein
        │  (no automatic lift)
        ▼
Layer M — Our master equation
  Φ_g, S_c, L(ρ,g), dτ, Path J/M Newton
```

**M6 contact** sits at **Layer G ∩ Layer M** (shared Poisson via Einstein/GR) — **not** at Layer W. Proving T4 does **not** improve M6 identity status.

---

## 4. Checklist: abstracts / talks vs forbidden language

### 4.1 Claims agents **may** write (if true to evidence)

Use near-verbatim; prefer soft verbs.

| # | Allowed claim | Label |
|---|---------------|-------|
| A1 | We implement a **discrete Euclidean warm-up** dual to Bianconi’s \(G=1+\alpha|\nabla\phi|^2\) / \(-\sum\ln G\) / PM flow | constructive + literature |
| A2 | On fixed 1D/2D lattices, joint toys score **6/6 SUPPORT** for the dual **pattern** (not gravity confirmation) | hybrid-experimental |
| A3 | *Beyond holography* identifies continuum PM with Euclidean GfE warm-up gradient flow | external literature |
| A4 | For **smooth** \(\phi\), standard FD arguments give **consistency** of discrete action density and PM flux as \(h\to 0\) (sketch); **action** \(O(h)\) formalized in M5b | analytic sketch / M5b lemma |
| A5 | Full lattice→continuum Γ-convergence / jump limits remain **open** | honest open |
| A6 | Residual dual is established as a **discrete** T1′ / \(U_\star\) story under stated soft hypotheses | analytic + soft PCRH\(_b\) |
| A7 | Load clock mirrors the **form** \(dt/(1+\alpha L)\) without deriving continuum \(L(\rho,g)\) | semantic / constructive toy |
| A8 | M6: both frameworks share Newtonian Poisson at leading order **via GR**, not via PM continuum limit | WEAK PASS / FAIL identity |

### 4.2 Claims agents **must not** write

| # | Forbidden | Replace with |
|---|-----------|--------------|
| F1 | “We prove the continuum limit of GfE” | citation bridge + open T4 / optional smooth consistency |
| F2 | “Γ-convergence of the dual action is established” | **open**; only Riemann-sum sketch for smooth \(\phi\) |
| F3 | “Master equation \(\Leftrightarrow\) Bianconi GfE” | explicit non-claim (CURRENT_CLAIMS §3) |
| F4 | “Lattice denoising confirms emergent gravity” | dual pattern / Euclidean warm-up only |
| F5 | “PM continuum limit yields Einstein/Newton” | Newton = Path J/M; M6 via GR — different layer |
| F6 | “\(L\) converges to the metric \(G\)” | \(L\neq G\) always |
| F7 | “Toy \(H_c\) is von Neumann \(S_c\)” | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) |
| F8 | “T1′ holds for continuum SPDEs / all images” | discrete windowed dual only |
| F9 | “2D scorecard proves continuum 2D GfE” | constructive pattern on a grid |
| F10 | “Warm-up continuum closes the gravity program” | Layer W only; Layers G/M open / analysis-only |

### 4.3 Paste-ready abstract fragment (safe)

> *We study a Euclidean warm-up dual (ACD-EW) in which a structure-induced metric \(G=1+\alpha|\nabla\phi|^2\) and Perona–Malik flow—matching Bianconi’s GfE warm-up at the continuum literature level—interface with an observation channel and a scalar load clock on lattices. Continuum contact is a citation bridge plus smooth finite-difference consistency; Γ-convergence and Lorentzian/master-equation equivalence are not claimed.*

---

## 5. Relation to M5 T4 parent file

| File | Role |
|------|------|
| [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) | Goal, continuum dictionary table, **Proposition T4 target**, smooth consistency sketch, settled vs not |
| [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) | Smooth-only **action** \(O(h)\) conditional lemma (hypotheses + proof sketch); not Γ / BV |
| [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) | Layer W: PM ↔ warm-up gradient flow (external) + discrete Euler energy descent |
| **This note** | Hygiene: definition of “warm-up continuum,” lit vs open, transfer checklist, abstract language |

**Status line (combined):**  
**M5: citation bridge complete; hygiene boundaries frozen (this note); smooth action \(O(h)\) lemma (M5b); PM/energy flow sketch (M5c); full Γ-limit / BV / SPDE dual open.**

---

## 6. Explicit non-claims (M5 hygiene)

1. Master equation \(\not\Leftrightarrow\) continuum GfE (warm-up or Lorentzian).  
2. Γ-convergence of lattice warm-up action **not proved** in this repository.  
3. Dual toys \(\neq\) empirical gravity; \(\neq\) Lorentzian GfE.  
4. \(L \neq G\); continuum limit of \(G\) is not a continuum theory of load.  
5. M5 / T4 does not upgrade M6 FAIL identity or Path J assumptions.  
6. Literature PM = GfE warm-up flow is **external**; we do not re-derive Bianconi’s variational calculation here.  
7. Smooth consistency \(\neq\) BV/jump continuum theorem.  
8. Completing M5 hygiene does not complete M9 or M10 identification.

---

## 7. Recommended next analytic step

**Done (M5b):** smooth-only action proposition written as conditional lemma — [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md):

> For \(\phi\in C^3(\mathbb{T}^1)\), mesh \(h=1/N\), \(\alpha\) fixed,
> \[
> \Bigl|\,h\sum_{i}-\ln\bigl(1+\alpha|D_h\phi_i|^2\bigr)
> -\int -\ln\bigl(1+\alpha|\phi'|^2\bigr)\,dx\,\Bigr|
> \le C(\phi,\alpha)\,h,
> \]
> with \(C\) controlled by \(\|\phi''\|_\infty,\|\phi'''\|_\infty\). **Not** Γ-convergence, jumps, or residual dual continuum.

**Still open (do not default-chase):** full T4 Γ-limit; BV/jump continuum; continuum residual dual SPDE; PM scheme theorem beyond T4 sketch.

---

## 8. Pointers

| Resource | Path |
|----------|------|
| M5 T4 technical parent | [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) |
| M5b smooth action lemma | [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) |
| M5c PM gradient flow / discrete descent | [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) |
| Transfer / non-transfer | [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) |
| ACD-EW | [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) |
| \(H_c\) / \(S_c\) hygiene | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) |
| M6 gravity layer | [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) |
| Claims freeze | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) |
| External PDFs | [papers/external/README.md](../papers/external/README.md) |

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
