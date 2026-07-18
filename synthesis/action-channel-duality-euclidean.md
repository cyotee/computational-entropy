# Action–Channel Duality (Euclidean Warm-Up)

**Status:** Formal conjecture + experimental support (2026-07-14)  
**Scope:** Euclidean warm-up (1D + 2D + game-motivated ICs) — **not** full Lorentzian GfE or the gravitational master equation  
**Evidence:** Joint toys **6/6 SUPPORT** (1D, 2D, blackjack-belief IC) — [simulations/bridging/](../simulations/bridging/)  
**Parents:** [PRD.md](../PRD.md) · [THEORY.md](../THEORY.md) §3.3 · [bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md)  
**Siblings:** [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) · [weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md) · [t1-residual-domination.md](t1-residual-domination.md)

---

## 0. Claim in one paragraph

On a one-dimensional flat lattice, **Bianconi’s Gravity-from-Entropy (GfE) warm-up** — relative entropy between a support metric \(g\) and a structure-induced metric \(G[\phi]\), whose gradient flow is Perona–Malik (PM) anisotropic diffusion — is **operationally dual** to an **observation channel** that reconstructs a hidden field \(\phi_\star\) from noisy data \(y\), with computational entropy \(H_c\) measured by residual reconstruction error (plus edge-location uncertainty) and a **load** \(L\) that (i) tracks the intensity of \(G-g\) and (ii) reparameterizes the reconstruction clock. Duality here means: **the same geometric imprint \(G\) is the Stage-2 object both theories act on**, Stage-3 GfE/PM flow is a structure-preserving reconstructor that reduces Stage-1 channel residual relative to isotropic heat, and Stage-1 load is a scalar summary of induction intensity plus entropy-production rate. This is a **constructive special case**, not a derivation of continuum modified Einstein equations.

---

## 1. Definitions (this special case only)

### 1.1 Support and state

- Discrete manifold: sites \(i=0,\ldots,N-1\), spacing \(h=1\).
- Support metric on edges: \(g_i \equiv 1\) (flat Euclidean warm-up).
- Scalar field \(\phi \in \mathbb{R}^N\) (intensity / reconstructed structure).
- Edge gradient: \((\nabla\phi)_i = \phi_{i+1}-\phi_i\).

### 1.2 Stage 2 — Induced metric (shared object)

\[
G_i[\phi] \;=\; 1 + \alpha_G \,(\nabla\phi)_i^2 .
\]

- \(G-g = \alpha_G(\nabla\phi)^2\) is the **matter-/structure-induced deformation**.
- In Bianconi’s warm-up language, \(G\) is the metric induced by the scalar (image) on the support.
- In our workflow language, \(G\) is the geometric encoding of local computational structure in \(\phi\).

**Type note:** \(G\) is edgewise scalar (1D rank-1 analogue of a metric operator). Load \(L\) remains a separate scalar.

### 1.3 Stage 3 — GfE action and gradient flow

Warm-up Lagrangian density (edgewise):

\[
\mathcal{L}^{\mathrm{GfE}}_i \;=\; -\ln G_i[\phi]
\;=\; -\ln\bigl(1+\alpha_G(\nabla\phi)_i^2\bigr).
\]

Total action:

\[
S_{\mathrm{GfE}}[\phi] \;=\; \sum_i \mathcal{L}^{\mathrm{GfE}}_i .
\]

**Dynamics (GfE side):** gradient flow of the GfE warm-up, implemented as classical Perona–Malik conductivity

\[
\rho_i \;=\; \frac{1}{1+\bigl((\nabla\phi)_i/K\bigr)^2},
\qquad
\partial_t\phi \;=\; \mathrm{div}\bigl(\rho\,\nabla\phi\bigr),
\]

with \(K\) of order the observation noise scale (P0).  
Bianconi, *Beyond holography* (arXiv:2503.14048): PM is the gradient flow maximizing the Euclidean GfE warm-up action between support metric and image-induced metric.

### 1.4 Stage 1 — Observation channel

| Object | Definition |
|--------|------------|
| Hidden structure | \(\phi_\star \in \mathbb{R}^N\) |
| Observation | \(y = \phi_\star + \eta\), \(\eta\sim\mathcal{N}(0,\sigma^2 I)\) |
| Channel / reconstructor | Map \(\mathcal{C}_t: y \mapsto \hat\phi(t)\) given by heat, PM, or load-gated PM flow with \(\hat\phi(0)=y\) |
| Residual energy | \(R(\hat\phi,\phi_\star)=\mathrm{mean}_i(\hat\phi_i-\phi_{\star,i})^2\) |
| Residual entropy proxy | \(H_R=\log(1+R/\sigma_{\mathrm{ref}}^2)\) |
| Edge-location entropy | \(H_{\mathrm{edge}}=-\sum_i p_i\log_2 p_i\), \(p\propto|\nabla\hat\phi|\) |
| **Channel computational entropy** | \(H_c(\hat\phi\mid\phi_\star)=H_R+\lambda_e H_{\mathrm{edge}}\) |

Lower \(H_c\) means better reconstruction / more localized edge mass.  
This is a **specialization** of project \(H_c\): entropy of the channel’s output quality relative to the hidden input structure — not Shannon entropy of a generic function on random bits, but the same *output-pattern* idea applied to a reconstructor.

### 1.5 Stage 1 — Load (split)

\[
\begin{aligned}
L_E &= c_E\,\mathbb{E}\bigl[(\nabla\hat\phi)^2\bigr], \\
L_S &= c_S\,\bigl|\Delta H_c\bigr|/\Delta t, \\
L_B &= c_B\,\frac{\max|\nabla\hat\phi|}{1+\max|\nabla\hat\phi|}, \\
L_{\mathrm{clock}} &= L_E + L_S .
\end{aligned}
\]

**Load-gated dynamics:** same PM operator with

\[
dt_{\mathrm{eff}} \;=\; \frac{dt}{1+\alpha_L L_{\mathrm{clock}}} .
\]

Interpretation:

- \(L_E\): intensity of Stage-2 induction (tracks \(\mathbb{E}[G-1]\)).
- \(L_S\): rate of Stage-1 entropy change (production / reduction).
- \(L_B\): capacity-like edge saturation (not used in the clock in v2).
- \(1/(1+\alpha_L L_{\mathrm{clock}})\): discrete analogue of proper-time reparameterization \(d\tau=dt/(1+\alpha L)\).

---

## 2. The duality statement

### Conjecture ACD-EW (Action–Channel Duality, Euclidean Warm-Up)

Let \(\mathcal{M}\) be the 1D flat lattice above. For observation models of the form \(y=\phi_\star+\eta\) and reconstructors in the family \(\{\text{heat},\,\text{PM},\,\text{load-PM}\}\):

**(A) Shared geometric object.**  
The induced metric \(G[\hat\phi]\) is simultaneously:

1. the GfE warm-up second metric (Bianconi Stage 2–3 input), and  
2. the geometric imprint of the reconstructor’s local structure (our Stage 2).

**(B) Action flow as channel.**  
The PM flow (GfE gradient flow) is a **computational channel** \(\mathcal{C}^{\mathrm{GfE}}_t\) that, relative to isotropic heat \(\mathcal{C}^{\mathrm{heat}}_t\),

1. reduces residual \(R(\hat\phi(t),\phi_\star)\) more effectively on jump-like \(\phi_\star\) with noise, and  
2. retains edge sharpness (structure-preserving reconstruction).

**(C) Load as induction + clock.**  
Along these flows:

1. \(L_E(\hat\phi)\) is monotonically associated with induction intensity \(\mathbb{E}[G[\hat\phi]-1]\) (in practice: correlation \(\approx 1\) in the joint toy), and  
2. load-gating \(dt/(1+\alpha_L L_{\mathrm{clock}})\) slows mid-run state change without destroying the residual/edge advantages of PM.

**(D) Dual reading of dynamics.**

| GfE / action language | Channel / load language |
|----------------------|-------------------------|
| Maximize / flow \(S_{\mathrm{GfE}}\) (warm-up) | Run structure-preserving reconstructor \(\mathcal{C}^{\mathrm{GfE}}\) |
| Second metric \(G[\phi]\) | Geometric encoding of reconstructed structure |
| Edge-stopping conductivity \(\rho\) | Preferential computation along uncertain/high-gradient loci |
| (no native clock in warm-up PM) | Load \(L_{\mathrm{clock}}\) reparameterizes reconstructor time |

**What ACD-EW does *not* claim**

- Equivalence of the full Lorentzian GfE action (with curvature-in-\(G\), G-field, \(\Lambda_G\)) to the gravitational master equation.
- Identity \(H_c \equiv S_{\mathrm{GfE}}\) as real numbers (different units and functionals).
- Identity \(L \equiv G\) (scalar vs metric).
- That lambda/IDEM microstructure has been embedded in the toy.

---

## 3. What counts as a proof (success criteria)

### 3.1 Experimental / constructive proof in the toy (achieved at 6/6)

A **constructive verification** of ACD-EW on a fixed IC family and parameter set consists of all of:

| # | Criterion | Joint toy v2 status |
|---|-----------|---------------------|
| E1 | PM residual better than heat on primary noisy jump IC | **Pass** (`noisy_step` impro ≫ 0.05) |
| E2 | PM residual not worse than heat on secondary structured IC | **Pass** (`noisy_two_bumps` impro > 0) |
| E3 | PM retains edges vs heat on step ICs | **Pass** (~10× max-grad retention) |
| E4 | Weak-gradient IC does not staircase under PM | **Pass** (ramp max-grad ratio ≪ 2.5) |
| E5 | \(L_E\) tracks \(\mathbb{E}[G-1]\) on PM trajectories | **Pass** (corr = 1.0) |
| E6 | Load-gating slows mid-run evolution vs pure PM | **Pass** (all ICs) |
| E7 | Residual co-motion: PM residual monotone better than heat on primary IC | **Pass** |

**Status:** E1–E7 satisfied under deterministic seeds (2026-07-14).  
See `simulations/bridging/gfe_load_joint_toy_scorecard_v2.txt`.

This is a **proof of the dual on the implemented special case**, not a theorem for all \(\phi_\star\), all \(\sigma\), all \(K\).

### 3.2 Mathematical program (T1–T4)

A **theorem-level** ACD-EW requires T1–T4 below. **T1 is sketched in §10** (proof outline, not a finished proof). T2–T4 remain open.

**(T1) Residual domination.**  
Under suitable assumptions (piecewise constant \(\phi_\star\), i.i.d. noise, \(K\sim\sigma\), controlled time window), show

\[
\mathbb{E}\bigl[R(\hat\phi^{\mathrm{PM}}(t),\phi_\star)\bigr]
\;\le\;
\mathbb{E}\bigl[R(\hat\phi^{\mathrm{heat}}(t),\phi_\star)\bigr]
\]

with a quantitative edge-error bound. → **§10 sketch**

**(T2) Lyapunov relation.**  
Exhibit a Lyapunov functional linking residual decrease to GfE / edge energy.

**(T3) Load as reparameterization.**  
Load-gating = monotone reparameterization of PM time that preserves descent for channel loss.

**(T4) Continuum limit sketch.**  
As \(h\to 0\), identify \(G[\phi]\) and \(S_{\mathrm{GfE}}\) with Bianconi’s warm-up (*Beyond holography*).

**Citation posture until T1 is complete:** dual is **experimentally constructive + definitionally aligned + T1 outline available**, not a published theorem.

---

## 4. Rigor level (project taxonomy)

| Mapping | Level | Evidence |
|---------|-------|----------|
| \(G[\phi]\) shared Stage-2 object | **Structural** | Definition + Bianconi warm-up |
| PM = GfE gradient flow | **Structural / literature** | Bianconi arXiv:2503.14048 |
| PM = residual-reducing channel vs heat | **Constructive (toy)** | Scorecard E1–E3, E7 |
| \(L_E\) = induction intensity of \(G\) | **Constructive (toy)** / near-definitional | \(L_E\propto\mathbb{E}[(\nabla\phi)^2]\), \(G-1=\alpha_G(\nabla\phi)^2\) |
| Load clock = discrete \(d\tau\) analogue | **Semantic + constructive (toy)** | E6; form matches master-equation factor |
| Full GfE gravity \(\Leftrightarrow\) \(\Phi_g,L\) master equation | **Open (not claimed)** | Requires continuum + curvature + quantum \(\rho\) |

---

## 5. Relation to the three-stage workflow

```text
STAGE 1  Observation y, channel Ĉ_t, H_c, L_E/L_S/L_clock
              │
              │  imprint of reconstructed structure
              ▼
STAGE 2  G[φ̂] = 1 + α_G (∇φ̂)²     ← SHARED OBJECT (duality hinge)
              │
              │  GfE warm-up action / gradient flow
              ▼
STAGE 3  S_GfE, PM dynamics  ↔  structure-preserving reconstructor
```

**Workflow slogan (now justified for this toy):**  
Stage 1 *operates* the reconstructor and measures demand; Stage 2 *encodes* its structure as \(G\); Stage 3 *is* the GfE warm-up law on that encoding. Duality = recognizing Stage-3 flow as a Stage-1 channel on the same Stage-2 object.

---

## 6. Implications for the broader program

### Supported next claims (careful wording)

1. There exists a **non-vacuous discrete model** in which computational load and computational (channel) entropy interface cleanly with Bianconi’s GfE warm-up geometry.
2. “Matter-induced metric” can be **defined from a reconstructor’s gradient structure**, not only from a classical field Lagrangian.
3. Load-dependent time reparameterization is compatible with GfE/PM without erasing structure-preserving benefits.

### Still required for gravity papers

1. Lift Stage 2 from \(G=1+\alpha|\nabla\phi|^2\) to topological \(G=\tilde g+\alpha\tilde M-\beta\tilde{\mathcal{R}}\).
2. Relate \(H_c\) residual to von Neumann \(S_c=S(\Phi_g(\rho))\).
3. Relate \(L_{\mathrm{clock}}\) to the three-term continuum load \(L(\rho,g)\).
4. Match weak-field Newton / cosmology recoveries to GfE modified Einstein (Thattarampilly–Zheng papers as continuum targets).

### Citation posture

- **Cite** Bianconi GfE + *Beyond holography* for continuum action and PM dual.  
- **Cite** joint toy + this note for constructive Euclidean dual.  
- **Do not** write “we derive Bianconi’s Einstein equations from computational load” based on this note alone.

---

## 7. Open problems (ordered)

1. **T1 residual domination theorem** (piecewise-constant \(\phi_\star\), short-time PM).  
2. Stability of scorecard under broader IC families (textures, multiple jumps, non-Gaussian noise).  
3. 2D image extension (true Perona–Malik plane).  
4. Embed IDEM/decay-vector metadata into \(\phi\) or into a multi-field \(G\).  
5. Continuum limit bridging ACD-EW to full GfE + master equation (long-range).

---

## 8. Reproduction

```bash
.venv/bin/python simulations/bridging/_joint_toy_v2_core.py
# Notebook: simulations/bridging/gfe_load_joint_toy.ipynb
# Kernel: Python (computational-entropy)
```

Parameters (v2 defaults): \(N=192\), \(\alpha_G=1\), \(K=0.15\), \(\alpha_L=3\), \(\sigma=0.12\), \(dt=0.08\), \(180\) steps; IC seeds 101–104.

---

## 9. Document control

| Date | Change |
|------|--------|
| 2026-07-14 | Initial ACD-EW conjecture after joint toy v2 6/6 SUPPORT |
| 2026-07-14 | §10 T1 residual-domination sketch; paper cross-ref |
| 2026-07-14 | 2D joint toy 6/6 SUPPORT; Catte PM + flux fix |

*Update this file when T1–T4 progress or when 2D/game extensions change the dual’s scope.*

---

## 10. T1 sketch — residual domination (proof outline)

This section is a **research outline**: lemmas to prove, not a finished derivation. Goal: make T1 attackable in a follow-up note or appendix.

### 10.1 Setting

Work on the continuum interval \(x\in\mathbb{R}\) (or the circle \(\mathbb{T}\)) to avoid boundary bookkeeping; discrete lattice is the same story with \(O(h)\) consistency error.

- **Truth:** single jump of height \(1\) at the origin,
  \[
  \phi_\star(x) \;=\; \mathbf{1}_{x\ge 0}.
  \]
  (Finite unions of jumps are identical after localization.)
- **Observation:** \(y=\phi_\star+\eta\) with \(\eta\) white noise of intensity \(\sigma^2\) in the continuum scaling sense, or i.i.d. \(\mathcal{N}(0,\sigma^2)\) on the lattice.
- **Heat flow:** \(\partial_t u = \partial_{xx} u\), \(u(0)=y\).
- **PM flow:** \(\partial_t v = \partial_x\bigl(\rho(|\partial_x v|^2)\,\partial_x v\bigr)\) with
  \[
  \rho(s) \;=\; \frac{1}{1+s/K^2},
  \]
  \(v(0)=y\), and contrast threshold \(K=\Theta(\sigma)\).

Channel residual at time \(t\):

\[
R[w](t) \;=\; \int \bigl(w(t,x)-\phi_\star(x)\bigr)^2\,dx
\quad\text{(lattice: mean square).}
\]

**Target inequality (T1).** There exist \(T>0\) and \(C<\infty\) (depending on \(\sigma,K\) but not on a particular noise realization beyond high probability) such that for all \(t\in(0,T]\),

\[
\mathbb{E}\,R[v](t)
\;\le\;
\mathbb{E}\,R[u](t)
\qquad\text{and}\qquad
\mathbb{E}\,\mathrm{EdgeErr}[v](t)
\;\le\;
C\,\mathbb{E}\,\mathrm{EdgeErr}[u](t),
\]

where \(\mathrm{EdgeErr}\) measures blur of the jump (e.g. transition-layer \(L^1\) width, or \(1-\max|\partial_x w|\) after normalization).

### 10.2 Heuristic: why heat loses and PM wins

1. **Heat** is a low-pass filter. The jump’s Fourier content \(\sim 1/|\xi|\) is damped by \(e^{-t\xi^2}\). At scales \(|\xi|\gtrsim t^{-1/2}\), the edge is erased; residual near the jump is order the mass of the diffused step error \(\sim t^{1/4}\) (1D scaling) plus noise smoothed at the same scale.
2. **PM** reduces conductivity where \(|\partial_x v|\) is large. Across a true jump, \(|\partial_x v|\) stays \(\gg K\) for a long time, so \(\rho\approx 0\): the two sides **decouple** and each side denoises almost like a **separate heat flow on a half-line with Neumann (no-flux) condition at the jump**.
3. On each plateau, the signal is constant; half-line heat flow reduces Gaussian noise without paying a jump-blur penalty. Hence residual drops while edge height is approximately preserved.

This “edge as free boundary / insulating interface” picture is the standard Perona–Malik / anisotropic diffusion intuition; T1 makes it quantitative for residual MSE.

### 10.3 Proposed lemma stack

**Lemma A (noise reduction on a constant domain).**  
Let \(\Omega_-\) and \(\Omega_+\) be the left/right half-lines. Conditional on an interface fixed at \(0\) with Neumann boundary conditions, the heat flow of pure noise has

\[
\mathbb{E}\int_{\Omega_\pm}\! u_{\mathrm{noise}}(t)^2
\;=\;
\Theta\bigl(\sigma^2\, t^{-1/4}\bigr)
\quad\text{(1D; lattice: \(\Theta(\sigma^2 (t/h^2)^{-1/4})\) up to cutoffs).}
\]

Any scheme that approximately enforces no flux across the jump inherits this rate on the plateaus.

**Lemma B (PM freezes super-threshold interfaces).**  
If at time \(t\) the discrete jump height satisfies \(|v_{i^\star+1}-v_{i^\star}|\ge c K\) for a fixed \(c>1\) on the true edge edge-set, then the PM flux across that edge is \(\le K^2/(c^2 K^2)=1/c^2\) times the isotropic flux. Hence interface leakage is \(O(1/c^2)\) relative to heat.  
*Proof idea:* \(\rho = 1/(1+(g/K)^2)\le (K/g)^2\le 1/c^2\).

**Lemma C (short-time edge persistence under PM, high probability).**  
With \(K=\Theta(\sigma)\) and \(y=\phi_\star+\eta\), the empirical jump at the true location dominates spurious noise gradients of height \(O(\sigma\sqrt{\log N})\) on the lattice, for \(N\) not exponentially large in \(1/\sigma^2\). Thus with high probability the maximizer of \(|\nabla y|\) sits at the true edge and remains super-threshold for a time \(T=\Theta(1)\) under PM.  
*Proof idea:* Gaussian tail bounds + union bound over \(N\) edges; true jump contribution \(1\) vs noise \(O(\sigma\sqrt{\log N})\).

**Lemma D (heat must blur the jump).**  
For heat flow of a noisy step, the deterministic part \(\mathrm{erfc}(x/\sqrt{4t})\) has transition width \(\sqrt{t}\), contributing residual \(\Theta(\sqrt{t})\) near the jump (integrated squared error of the smoothed step vs the step), independent of the beneficial noise smoothing.  
Thus \(\mathbb{E} R[u](t) \ge c\sqrt{t} - C\sigma^2 t^{-\alpha}\) for small \(t\), some \(\alpha>0\).

**Lemma E (PM residual upper bound).**  
On the event of Lemma C, split \(R[v]=R_{\mathrm{plateau}}+R_{\mathrm{interface}}\). Plateau term follows Lemma A (two half-lines). Interface leakage from Lemma B contributes \(O(t/c^2)\) edge mass error. Choose \(c\) large (via \(K\)) and \(t\in(0,T]\) so that

\[
\mathbb{E} R[v](t)
\;\le\;
C\sigma^2 t^{-\alpha} + O(t/c^2)
\;\le\;
\mathbb{E} R[u](t).
\]

### 10.4 Discrete translation (matches the joint toy)

On the lattice used in `_joint_toy_v2_core.py`:

| Continuum object | Toy object |
|------------------|------------|
| \(\phi_\star=\mathbf{1}_{x\ge 0}\) | `phi_star_step` |
| Heat | `mode="heat"` |
| PM | `mode="pm"`, \(K=K_{\mathrm{PM}}\) |
| \(R\) | `residual_mse` |
| Edge freeze | \(\rho=1/(1+(g/K)^2)\) small when \(|g|\gg K\) |

Scorecard E1/E6/E7 are **numerical witnesses** of Lemmas D–E in a fixed parameter regime; T1 is the analytic envelope.

### 10.5 Load-gating does not break T1 (link to T3)

If \(dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}})\) with \(L_{\mathrm{clock}}\ge 0\), the load-gated PM path is a **time-changed** PM path: \(\hat\phi^{\mathrm{load}}(t)=\hat\phi^{\mathrm{PM}}(\tau(t))\) with \(\tau(t)=\int_0^t ds/(1+\alpha_L L_{\mathrm{clock}}(s))\le t\).

- Residual domination at time \(\tau(t)\) for pure PM implies residual of load-PM at wall-clock \(t\) equals residual of pure PM at an **earlier** internal time.
- For short-time T1, load-PM may be *slightly worse* residual than pure PM at the same wall-clock \(t\) (less denoising done) but still better than heat if \(\tau(t)\) stays in the T1 window and heat blurs faster than the time change hurts.
- Joint toy E6 checks slowing; residual vs heat remains favorable on `noisy_step` experimentally.

Full T3 = prove descent of \(R\) (or \(H_c\)) along the time-changed vector field.

### 10.6 Gaps to close before calling T1 a theorem

1. Replace continuum white-noise heuristics with a precise lattice noise model and scaling limit.  
2. Prove Lemma C (edge persistence) with explicit \(T(\sigma,K,N)\).  
3. Control PM well-posedness (forward–backward diffusion issues): restrict to the **regularized** PM used in the toy (explicit Euler, small \(dt\), \(K>0\)), which is a stable semi-discrete scheme.  
4. Multi-jump and textured \(\phi_\star\): localization + non-interference if jumps are separated by \(\gg\sqrt{t}\).  
5. Match constants to the experimental window (\(dt=0.08\), \(180\) steps, \(\sigma=0.12\), \(K=0.15\)).

### 10.7 Minimal publishable T1 statement (target)

> **Proposition (T1, lattice, single jump).**  
> Fix \(K=c_K\sigma\) with universal \(c_K\in[1,3]\). There exist \(t_\star>0\) and \(N_0\) such that for all \(N\ge N_0\) and all \(t\in(0,t_\star]\), the explicit-Euler PM scheme of the joint toy with CFL-stable \(dt\) satisfies  
> \(\mathbb{E} R_{\mathrm{PM}}(t) \le \mathbb{E} R_{\mathrm{heat}}(t)\),  
> and \(\mathbb{E}\max|\nabla\hat\phi_{\mathrm{PM}}|(t) \ge c\,\mathbb{E}\max|\nabla\hat\phi_{\mathrm{heat}}|(t)\) for some \(c>1\).

This proposition is exactly what the joint toy samples; the sketch above is the proof strategy.

---

## 11. Two-dimensional extension (status)

**Path:** `simulations/bridging/_joint_toy_2d.py`  
**Run:** `.venv/bin/python simulations/bridging/_joint_toy_2d.py`  
**Latest scorecard:** **6/6 SUPPORT — PROMISING (2D)** (2026-07-14; Catte-regularized PM, corrected flux divergence).

| Object | 2D lift |
|--------|---------|
| \(\nabla\phi\) | Forward differences \(g_x, g_y\) |
| \(G-1\) | \(\alpha_G\) times mean squared edge grads |
| PM | Catte: \(\rho\) from box-smoothed field; flux from unsmoothed grads |
| \(H_c\) | residual MSE + soft edge-mass entropy |
| Load / clock | same split \(L_E+L_S\) as 1D |

**ICs:** noisy vertical edge, noisy disk, noisy smooth blob, clean edge.  
**Scope:** still Euclidean warm-up ACD-EW; still not Lorentzian GfE. The 2D pass strengthens the continuum / image-processing link of *Beyond holography* and T4.

---

## 12. Paper cross-reference

Main manuscript `quantum/Computational_Entropy_and_Emergent_Gravity.tex` (Unification section) cites Bianconi and records ACD-EW as a constructive Euclidean dual supported by the joint toy—not as a derivation of the continuum field equations.
