# M5c — Warm-Up Action Gradient Flow ↔ PM / Discrete Consistency

**M-id:** M5c (gradient-flow / discrete-descent slice of Layer W)  
**Status:** **Literature continuum link (external) + discrete gradient-structure sketch + optional numerical witness** — not a continuum PM well-posedness theorem  
**Scope:** **Layer W only** — Euclidean GfE warm-up action / energy and (Catte–)Perona–Malik form  
**Parents:** [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) · [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) · [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) · [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) · [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md)  
**Code:** `simulations/bridging/_joint_toy_v2_core.py` · optional witness `simulations/bridging/m5c_pm_energy_descent.py`  
**Date:** 2026-07-15  
**Stance:** Preliminary research. Under-claim. Layer W ≠ Layer D. No Lorentzian GfE, no master equation, no \(L\equiv G\), no Newton.

---

## 0. Purpose

M5 hygiene freezes what “warm-up continuum” may mean.  
M5b gives a **conditional smooth lemma** for the **action** as a Riemann sum:  
\[
S_h[\phi]\to\int -\ln\bigl(1+\alpha|\phi'|^2\bigr)\,dx
\]
at rate \(O(h)\) for \(C^3\) fields.

This note (M5c) addresses the **dynamics** side of Layer W:

1. **Continuum (external literature):** gradient flow of the Euclidean warm-up action/energy is (classical) Perona–Malik anisotropic diffusion.  
2. **Discrete (repo constructive):** the joint-toy explicit Euler PM step is consistent with **discrete gradient descent** of a discrete edge energy whose conductivity matches the toy flux — under stated hypotheses (not a full scheme-convergence theorem).  
3. **Layer D separation:** residual dual \(H_c^{\mathrm{toy}}\) is **not** continuum relative entropy of metrics.

M5c does **not** close full T4 (Γ-limit + BV + residual dual continuum).

---

## 1. Layer separation (mandatory)

```text
Layer W — Euclidean warm-up (THIS NOTE)
  action/energy  S or E[φ], G = 1+α|∇φ|², PM / Catte flow
  continuum: external lit; discrete: joint-toy Euler
        │  (no automatic lift)
        ▼
Layer D — ACD-EW dual (toys + residual windows)
  H_c^toy = H_R + λ_e H_edge, L_clock, T1′ / U_★
  ≠ relative entropy of metrics; ≠ S_c
        │
        ▼
Layer G / M — Lorentzian GfE / master equation
  out of scope for M5c
```

| Layer | Objects | May relate in M5c? |
|-------|---------|-------------------|
| **W** | \(G\), \(S_{\mathrm{GfE}}\) / \(\Psi\)-energy, PM flux, Euler step | **Yes** — main content |
| **D** | \(H_c^{\mathrm{toy}}\), residual dual, load clock | **Mention only to separate** — not identified with \(S_{\mathrm{GfE}}\) |
| **G/M** | full GfE EL, \(\Phi_g\), Newton Path J/M | **No** |

---

## 2. Continuum relationship (Layer W) — external literature

### 2.1 Objects (1D scalar warm-up; flat support \(g=\mathrm{Id}\))

\[
G[\phi]
\;=\;
1+\alpha\,(\phi')^2,
\qquad
\mathcal{L}(\phi')
\;=\;
-\ln\bigl(1+\alpha\,(\phi')^2\bigr),
\qquad
S[\phi]
\;=\;
\int_{\Omega}
-\ln\bigl(1+\alpha\,|\nabla\phi|^2\bigr)\,dx .
\]

(Up to dimension / trace notation, this is the Euclidean scalar warm-up density used in M5 T4 §2 and M5b §1.2.)

### 2.2 Energy vs action sign convention

Classical anisotropic-diffusion energy for conductivity
\[
\rho(s)
\;=\;
\frac{1}{1+(s/K)^2}
\]
is (up to additive constants)

\[
E[\phi]
\;=\;
\int \Psi\bigl(|\nabla\phi|\bigr)\,dx,
\qquad
\Psi(s)
\;=\;
\frac{K^2}{2}\,\ln\Bigl(1+\bigl(\tfrac{s}{K}\bigr)^2\Bigr),
\]

so that \(\Psi'(s)/s=\rho(s)\) for \(s\neq 0\). Then the \(L^2\)-gradient flow of \(E\) is

\[
\partial_t\phi
\;=\;
\operatorname{div}\bigl(\rho(|\nabla\phi|)\,\nabla\phi\bigr)
\;=\;
\operatorname{div}\Bigl(
\frac{\nabla\phi}{1+(|\nabla\phi|/K)^2}
\Bigr),
\]

i.e. **classical Perona–Malik** (isotropic heat is the special case \(\rho\equiv 1\), Dirichlet energy).

**Matched coupling.** If \(\alpha=1/K^2\), then

\[
E[\phi]
\;=\;
-\frac{K^2}{2}\,S[\phi]
\quad\text{(1D density identity up to the same measure \(dx\))}.
\]

Thus:

- **gradient descent of \(E\)** \(\Leftrightarrow\) **gradient ascent of the warm-up action \(S\)** (when \(\alpha=1/K^2\));  
- both are implemented by the same PM PDE.

### 2.3 Literature claim (external — not re-derived here)

| Claim | Source (repo index) | Rigor in **this** repo |
|-------|---------------------|-------------------------|
| Euclidean GfE warm-up action between support metric and structure-/image-induced metric | Bianconi, *Gravity from entropy* (arXiv:2408.14391 / PRD 2025), warm-up discussion; notes in `papers/external/` | **External** |
| Perona–Malik anisotropic diffusion = gradient flow of that Euclidean warm-up | Bianconi, *Beyond holography* (arXiv:2503.14048); `papers/external/README.md`, ACD-EW §1.3 | **Structural / literature** — we **do not** re-derive Bianconi’s variational calculation |

**Allowed citation sentence (paste-ready):**

> *In continuum Euclidean warm-up language (Bianconi, Beyond holography, arXiv:2503.14048 — external), Perona–Malik anisotropic diffusion is the gradient flow of the GfE warm-up action between a flat support metric and a structure-induced metric \(G=1+\alpha|\nabla\phi|^2\). This repository treats that identification as literature structure for Layer W; joint toys are constructive discretizations, not a re-proof of the continuum variational identity.*

**2D / Catte.** Continuum ill-posedness of forward–backward PM motivates **Catte regularization** (convolve \(\nabla\phi\) before evaluating \(\rho\)). The 2D joint toy uses a Catte-style scheme (`_joint_toy_2d.py`); continuum Catte–PM as \(h\to 0\) remains **open** (M5 hygiene §2.2).

---

## 3. Discrete relationship (Layer W) — joint-toy Euler

### 3.1 Objects as implemented

From [`_joint_toy_v2_core.py`](../simulations/bridging/_joint_toy_v2_core.py) (1D, spacing \(h\), open chain of \(N\) sites / \(N-1\) edges):

\[
(g_\phi)_i
\;=\;
\frac{\phi_{i+1}-\phi_i}{h},
\qquad
G_i
\;=\;
1+\alpha_G\,(g_\phi)_i^2,
\qquad
S_{\mathrm{GfE}}[\phi]
\;=\;
-\sum_i\ln G_i
\quad\texttt{(gfe\_action)}.
\]

PM right-hand side (`rhs_pm`):

\[
\rho_i
\;=\;
\frac{1}{1+\bigl((g_\phi)_i/K\bigr)^2},
\qquad
\partial_t\phi
\;\approx\;
\operatorname{div}_h\bigl(\rho\,g_\phi\bigr),
\qquad
\phi \leftarrow \phi + \Delta t\cdot\operatorname{div}_h(\rho\,g_\phi)
\quad\text{(explicit Euler)}.
\]

Heat control: \(\rho\equiv 1\).

**Parameter honesty (toy defaults):**  
`ALPHA_G = 1.0`, `K_PM = 0.15` \(\Rightarrow\) \(\alpha_G \neq 1/K^2\).  
Bookkeeping metric \(G\) (and \(S_{\mathrm{GfE}}\)) and PM conductivity \(K\) are **structurally aligned** (same functional form) but **not coefficient-matched** under default scorecard parameters (P0: \(K\sim\) noise scale). Exact discrete descent of \(S_{\mathrm{GfE}}\) requires the **matched** choice \(\alpha=1/K^2\) (or conductivity \(\rho=1/(1+\alpha_G g^2)\)).

### 3.2 Discrete energy whose gradient flow is discrete PM

Define the **edge energy** matching the conductivity used in the flux:

\[
E_h[\phi]
\;:=\;
\sum_{i=0}^{N-2}
\Psi\bigl((g_\phi)_i\bigr),
\qquad
\Psi(s)
\;=\;
\frac{K^2}{2}\,\ln\Bigl(1+\bigl(\tfrac{s}{K}\bigr)^2\Bigr).
\]

**Hypothesis H1 (smooth edge potential).**  
\(\Psi\in C^2(\mathbb{R})\), even, \(\Psi(0)=0\), \(\Psi'(s)/s=\rho(s)=1/(1+(s/K)^2)\) for \(s\neq 0\), and \(\rho(0)=1\).

**Hypothesis H2 (discrete gradient structure).**  
The discrete divergence in the joint toy is the negative adjoint of the forward difference (with the open-chain boundary convention in `divergence_from_edge_flux`): for edge fluxes \(F\) and site fields \(u\),

\[
\sum_{\text{sites}} u\cdot\operatorname{div}_h(F)
\;=\;
-\sum_{\text{edges}} F\cdot g_u
\]

(up to the consistent \(h\)-scaling already built into `gradients` / `divergence_from_edge_flux`).

**Hypothesis H3 (small explicit step).**  
\(\Delta t>0\) is small enough that the explicit Euler map stays in a regime where a standard one-step energy estimate applies (e.g. \(\Delta t\le C_{\mathrm{CFL}}h^2\) with \(C_{\mathrm{CFL}}\) controlled by \(\sup\rho\le 1\) and mesh constants) — **not** proved here for all toy defaults; used as a working stability hypothesis.

### 3.3 Formal discrete statement (sketch / conditional)

> **Sketch M5c (discrete PM Euler as energy descent).**  
> *Rigor: elementary discrete calculus of variations under H1–H3; labeled **sketch**, not a published scheme theorem.*  
>
> Let \(\phi^{n+1}=\phi^n+\Delta t\,\operatorname{div}_h\bigl(\rho(g_{\phi^n})\,g_{\phi^n}\bigr)\) be one joint-toy explicit Euler PM step.  
> Along the **continuous-time** semi-discrete flow \(\partial_t\phi=\operatorname{div}_h(\rho(g_\phi)\,g_\phi)\),
> \[
> \frac{d}{dt}E_h[\phi(t)]
> \;=\;
> -\bigl\|\,
> \operatorname{div}_h\bigl(\rho(g_\phi)\,g_\phi\bigr)
> \,\bigr\|_{h}^{2}
> \;\le\; 0
> \]
> (exact non-increase of \(E_h\)).  
> For **explicit Euler**, under H3 one has the standard first-order statement
> \[
> E_h[\phi^{n+1}]
> \;\le\;
> E_h[\phi^n]
> + O\bigl((\Delta t)^2\bigr)
> \]
> with non-increase of \(E_h\) for sufficiently small \(\Delta t\) on fixed meshes (numerical witness: §5).  
> When \(\alpha=1/K^2\), \(E_h=-(K^2/2)\,S_{\mathrm{GfE}}\) (same edges), so descent of \(E_h\) is ascent of the discrete warm-up action \(S_{\mathrm{GfE}}\).

**One-line structural content:** discrete PM is the structure-preserving diffusion whose edge conductivity is the derivative of a convex-in-\(s^2\) log energy — the same log form as the warm-up density \(-\ln(1+\alpha s^2)\).

### 3.4 Link to M5b (action continuum limit)

| Piece | Result | Note |
|-------|--------|------|
| Discrete \(\to\) continuum **action** density | M5b: \(S_h\to S\) at \(O(h)\) for \(C^3\) \(\phi\) | Mesh-weighted \(h\sum-\ln G\) |
| Continuum **flow** of that action | External: PM (Beyond holography) | Not re-proved here |
| Discrete **flow** consistency | This note: Euler PM \(\leftrightarrow\) descent of \(E_h\) | Matched \(\alpha\leftrightarrow K\) for \(S_{\mathrm{GfE}}\) identity |
| Full scheme \(\to\) continuum PM as \(h\to 0\) | M5 T4 §4 sketch; **open** as theorem | Including jumps/BV open |

M5b concerns **values of the action functional** under mesh refinement for fixed smooth \(\phi\).  
M5c concerns **time dynamics** that decrease the matching energy / increase the matching action. Together they support (but do not prove) the T4 program sentence: *lattice toys discretize Bianconi’s Euclidean warm-up geometry and PM flow*.

### 3.5 Heat comparison (control, not a dual claim)

Heat Euler is gradient descent of the **Dirichlet** edge energy \(E^{\mathrm{Dir}}_h=\frac12\sum_i (g_\phi)_i^2\), not of \(E_h=\sum\Psi\). Therefore:

- heat need **not** monotone-decrease \(E_h\) at the same rate or with the same edge-stopping structure;  
- comparing residual dual \(H_c^{\mathrm{toy}}\) of heat vs PM is a **Layer D** experiment (ACD-EW scorecards), not a continuum relative-entropy identity.

---

## 4. Layer D — residual dual is not continuum relative entropy

| Object | Definition | Equal to continuum \(\operatorname{Tr} g\ln G^{-1}\) / warm-up \(S\)? |
|--------|------------|----------------------------------------------------------------------|
| \(S_{\mathrm{GfE}}\) / \(E_h\) | Edge log-\(G\) action / \(\Psi\)-energy | **Layer W** — warm-up geometry |
| \(H_c^{\mathrm{toy}}=H_R+\lambda_e H_{\mathrm{edge}}\) | Residual log-energy + edge-location Shannon | **Layer D** — channel quality score |
| \(S_c=S(\Phi_g(\rho))\) | von Neumann of gravitational channel output | **Not in toys** |

**Mandatory non-identity:**

\[
H_c^{\mathrm{toy}}
\;\not\equiv\;
S_{\mathrm{GfE}},
\qquad
H_c^{\mathrm{toy}}
\;\not\equiv\;
\int -\ln\bigl(1+\alpha|\nabla\phi|^2\bigr)\,dx,
\qquad
H_c^{\mathrm{toy}}
\;\not\equiv\;
S_c.
\]

ACD-EW asserts an **operational dual pattern** (shared Stage-2 \(G\), residual/edge advantages of PM vs heat on fixed ICs), not functional identity of Layer D scores with Layer W action. See [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md), [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md).

---

## 5. Optional numerical witness

**Script:** [`simulations/bridging/m5c_pm_energy_descent.py`](../simulations/bridging/m5c_pm_energy_descent.py)

**What it does (one IC, reuse joint-toy core):**

1. Build `noisy_step` observation (\(y=\phi_\star+\eta\)).  
2. Run pure **PM** and **heat** Euler with core `rhs_pm` / `rhs_heat`.  
3. Track discrete PM energy \(E_h=\sum\Psi(|g|)\) with \(\Psi(s)=(K^2/2)\ln(1+(s/K)^2)\) and \(K=K_{\mathrm{PM}}\).  
4. Track matched warm-up action \(S_{\mathrm{matched}}=-\sum\ln(1+(g/K)^2)\) (so \(E_h=-(K^2/2)S_{\mathrm{matched}}\)).  
5. Assert: under PM, \(E_h\) is **non-increasing** within a small numerical tolerance (and \(S_{\mathrm{matched}}\) non-decreasing); report heat’s \(E_h\) trajectory for contrast only.

**Interpretation:** constructive **energy-descent witness** on one lattice IC — not a proof for all \(\phi\), not continuum, not Layer D residual dual, not gravity.

---

## 6. Explicit non-claims

1. **Not** Lorentzian / full continuum GfE (curvature-in-\(G\), G-field, \(\Lambda_G\), modified Einstein).  
2. **Not** master equation \(\partial_\tau\rho=\mathcal{L}_g\rho\), \(\Phi_g\), or \(S_c=S(\Phi_g(\rho))\).  
3. **Not** \(L\equiv G\); load clock is Layer D / Stage-1 form only.  
4. **Not** master equation \(\Leftrightarrow\) GfE.  
5. **Not** Newtonian recovery / Path J/M / M6 identity upgrade from PM energy descent.  
6. **Not** \(H_c^{\mathrm{toy}}\equiv\) continuum relative entropy of metrics.  
7. **Not** Γ-convergence, BV/jump continuum PM, or full T4 scheme theorem.  
8. **Not** re-derivation of Bianconi’s continuum variational proof (*Beyond holography* remains **external**).  
9. **Not** claim that default toy \((\alpha_G,K)\) are coefficient-matched without the \(\alpha=1/K^2\) (or equivalent) identification.  
10. **Not** empirical gravity; lattice denoising ≠ gravity experiment.

---

## 7. Agent abstract checklist

### 7.1 May write

| # | Allowed | Label |
|---|---------|-------|
| C1 | Continuum PM is the gradient flow of Euclidean GfE warm-up action/energy (*Beyond holography*; external) | literature / structural |
| C2 | Joint-toy explicit Euler PM is discrete gradient descent of edge energy \(E_h=\sum\Psi\) with \(\Psi'(s)/s=\rho_{\mathrm{PM}}\) under H1–H3 (sketch + optional witness) | constructive / sketch |
| C3 | When \(\alpha=1/K^2\), descent of \(E_h\) is ascent of discrete \(S_{\mathrm{GfE}}\) | elementary identity |
| C4 | M5b action consistency + M5c flow structure jointly support “toys discretize warm-up geometry+PM” without closing T4 | Layer W program |
| C5 | \(H_c^{\mathrm{toy}}\) remains a dual channel score, not \(S\) or \(S_c\) | Layer D hygiene |

### 7.2 Must not write

| # | Forbidden | Replace with |
|---|-----------|--------------|
| X1 | “We prove continuum PM = GfE from first principles” | cite Beyond holography as external |
| X2 | “Residual dual proves action gradient flow” | Layer D ≠ Layer W |
| X3 | “Energy descent ⇒ Newton / Einstein / master equation” | Path J/M and ME are other layers |
| X4 | “\(L\) is the metric / action” | \(L\neq G\); \(L\neq S\) |
| X5 | “Γ-limit / all-\(t\) dual / Lorentzian closed by M5c” | open; Layer W only |

---

## 8. Paper-ready one-paragraph conclusion

> *For the Euclidean warm-up only (Layer W), continuum Perona–Malik anisotropic diffusion is identified in the external literature (Bianconi, Beyond holography) with the gradient flow of the GfE warm-up action between a flat support metric and a structure-induced metric \(G=1+\alpha|\nabla\phi|^2\). On the joint-toy lattice, the explicit Euler PM step is the natural discrete gradient descent of the edge energy whose conductivity matches the implemented flux; when the warm-up coupling matches that conductivity, this is equivalent to ascent of the discrete action \(-\sum\ln G\). Smooth mesh consistency of the action values is the separate conditional lemma M5b. None of this identifies the dual residual score \(H_c^{\mathrm{toy}}\) with continuum relative entropy of metrics, nor does it yield Lorentzian GfE, the gravitational master equation, \(L\equiv G\), or Newtonian gravity.*

---

## 9. Status line and pointers

**Status (M5 / M5b / M5c combined):**  
**Citation bridge complete; hygiene frozen; smooth action \(O(h)\) lemma (M5b); PM ↔ warm-up gradient flow recorded as external continuum + discrete energy-descent sketch/witness (M5c); full T4 Γ / BV / scheme theorem and residual dual continuum still open.**

| Resource | Path |
|----------|------|
| M5 hygiene | [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) |
| M5b smooth action | [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) |
| M5 T4 parent | [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) |
| ACD-EW dual | [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) |
| Transfer dictionary | [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) |
| Joint-toy core | [`simulations/bridging/_joint_toy_v2_core.py`](../simulations/bridging/_joint_toy_v2_core.py) |
| DESIGN | [`simulations/bridging/DESIGN_gfe_load_joint_toy.md`](../simulations/bridging/DESIGN_gfe_load_joint_toy.md) |
| External index | [papers/external/README.md](../papers/external/README.md) |
| Claims freeze | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) |

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
