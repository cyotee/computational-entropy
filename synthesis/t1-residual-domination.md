# T1 Residual Domination — Lattice Proposition and Proof Plan

**Status:** Proposition target + lemma stack (**T1′ window refined 2026-07-14; not a finished theorem**)  
**Program:** Action–Channel Duality Euclidean Warm-Up (ACD-EW), theorem-program **T1** / **M1**  
**Parent sketch:** [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) §3.2, §10  
**M1 advance:** [m1](m1-lemma-c-prime.md) · [m1b](m1b-t1-prime-c2-bound.md) · [m1c](m1c-c2-sharp-delta-noise.md) · [m1d](m1d-lemma-e-prime.md) · MC: [t1_mc_envelope.txt](../simulations/bridging/t1_mc_envelope.txt) · [t1_delta_noise_envelope.txt](../simulations/bridging/t1_delta_noise_envelope.txt) · [t1_eprime_envelope.txt](../simulations/bridging/t1_eprime_envelope.txt)  
**Toy witness:** [simulations/bridging/_joint_toy_v2_core.py](../simulations/bridging/_joint_toy_v2_core.py)  
**Design:** [simulations/bridging/DESIGN_gfe_load_joint_toy.md](../simulations/bridging/DESIGN_gfe_load_joint_toy.md)  
**Scope of this note:** single jump / `noisy_step` only; residual domination of Perona–Malik (PM) vs isotropic heat  
**Not claimed:** full continuum GfE, Lorentzian master equation, multi-jump/texture theorems, or that T1 is proved

---

## 0. Epistemic labels used here

| Label | Meaning |
|-------|---------|
| **Proposition (target)** | Precise claim we aim to prove; **not** currently proved end-to-end |
| **Lemma (proved sketch)** | Core inequality is standard or elementary; bookkeeping / constants may remain incomplete |
| **Lemma (open)** | Statement is plausible and needed; proof is incomplete or heuristic |
| **Conjecture** | Useful strengthening beyond the minimal proposition |
| **Experimental witness** | Fixed-parameter numerical scorecard / trajectory; supports but does **not** prove the proposition |

**Citation posture:** T1 is an **attackable proof program** with experimental support on the joint toy. Do **not** cite residual domination as a theorem until Gaps G1–G5 in §7 are closed.

**Bianconi (warm-up dual only).**  
G. Bianconi, *Beyond holography*, arXiv:2503.14048 — used **only** for the statement that classical Perona–Malik anisotropic diffusion is the gradient flow maximizing the Euclidean GfE warm-up action between a support metric \(g\) and an image-/structure-induced metric \(G[\phi]\). This note does **not** derive continuum modified Einstein equations from T1.

---

## 1. Setting (lattice, matches joint toy)

### 1.1 Discrete manifold and fields

- Sites \(i\in\{0,\ldots,N-1\}\), spacing \(h=1\) (toy default \(N=192\)).
- Scalar field \(\phi\in\mathbb{R}^N\).
- Forward edge gradients:
  \[
  (\nabla\phi)_i \;=\; \phi_{i+1}-\phi_i,\qquad i=0,\ldots,N-2.
  \]
- Edge-to-site divergence of an edge flux \(F\in\mathbb{R}^{N-1}\) (Neumann-type ends as in the toy):
  \[
  (\mathrm{div}\,F)_0=F_0,\quad
  (\mathrm{div}\,F)_i=F_i-F_{i-1}\ (1\le i\le N-2),\quad
  (\mathrm{div}\,F)_{N-1}=-F_{N-2}.
  \]

### 1.2 Hidden structure (single jump)

\[
(\phi_\star)_i \;=\;
\begin{cases}
0 & i < i_\star,\\
1 & i \ge i_\star,
\end{cases}
\qquad
i_\star \;=\; \lfloor N/2\rfloor
\quad\text{(toy: ``phi_star_step'').}
\]

Only **one** true jump edge \(e_\star=\{i_\star-1,i_\star\}\) with deterministic gradient \(1\). All other true gradients vanish.

### 1.3 Observation channel (noise model)

\[
y \;=\; \phi_\star + \eta,\qquad
\eta_i \;\stackrel{\mathrm{i.i.d.}}{\sim}\; \mathcal{N}(0,\sigma^2).
\]

Toy default: \(\sigma=\mathtt{NOISE\_SIGMA}=0.12\).  
We work with **fixed** \(\sigma>0\) and \(N\) polynomial in \(1/\sigma\) (or at least \(N\le \exp(c/\sigma^2)\) for small \(c\)); pure continuum white noise is **not** the primary object of this note (see Gap G1).

### 1.4 Reconstructors

All channels start at \(\hat\phi(0)=y\) and advance by **explicit Euler** with fixed wall-clock step \(dt>0\):

\[
\hat\phi^{k+1}
\;=\;
\hat\phi^k + dt_{\mathrm{eff}}\,
\mathrm{div}\bigl(F(\nabla\hat\phi^k)\bigr).
\]

| Mode | Flux \(F\) | \(dt_{\mathrm{eff}}\) | Toy name |
|------|------------|----------------------|----------|
| Heat | \(F=\nabla\phi\) | \(dt\) | `mode="heat"` |
| PM | \(F=\rho\,\nabla\phi\), \(\rho_i=1/(1+((\nabla\phi)_i/K)^2)\) | \(dt\) | `mode="pm"` |
| Load-PM | same PM flux | \(dt/(1+\alpha_L L_{\mathrm{clock}})\) | `mode="load_pm"` |

**Contrast threshold:** \(K=\Theta(\sigma)\). Toy: \(K_{\mathrm{PM}}=0.15\), \(\sigma=0.12\), so \(K/\sigma\approx 1.25\in[1,3]\).

**CFL / stability (toy regime).**  
With \(h=1\), isotropic heat flux gives spectral radius of the discrete Laplacian of order \(4\). Explicit Euler is stable for heat when \(dt\le 1/2\) (1D) in the usual \(\ell^2\) sense; the toy uses \(dt=0.08\), well inside that window. PM has \(|\rho|\le 1\), so the same CFL bound is **sufficient** (not always necessary) for the regularized scheme. We treat the Euler PM map as a **stable semi-discrete scheme with \(K>0\)**, not as continuum forward–backward PM (see Lemma well-posedness note in §4).

### 1.5 Residual and edge error

Lattice residual (channel MSE; matches `residual_mse`):

\[
R(\hat\phi,\phi_\star)
\;=\;
\frac{1}{N}\sum_{i=0}^{N-1}\bigl(\hat\phi_i-\phi_{\star,i}\bigr)^2.
\]

Edge-error proxies (either is acceptable for the proposition; toy uses max-gradient retention):

\[
\begin{aligned}
\mathrm{EdgeHeight}(\hat\phi)
&\;=\;
\max_i\bigl|(\nabla\hat\phi)_i\bigr|,\\
\mathrm{EdgeBlur}(\hat\phi)
&\;=\;
\sum_{i\in\mathcal{N}(e_\star)}
\bigl(\hat\phi_i-\phi_{\star,i}\bigr)^2
\quad\text{(optional localization near \(e_\star\)).}
\end{aligned}
\]

Channel computational entropy in the toy (\(H_c=H_R+\lambda_e H_{\mathrm{edge}}\)) is **downstream** of \(R\); T1 is stated for \(R\) (and edge height), not for full \(H_c\).

### 1.6 Induced metric / GfE warm-up (context only)

\[
G_i[\phi]=1+\alpha_G(\nabla\phi)_i^2,\qquad
S_{\mathrm{GfE}}[\phi]=-\sum_i\ln G_i[\phi].
\]

PM with conductivity \(\rho=1/(1+(\nabla\phi/K)^2)\) is the structure-preserving reconstructor dual to this warm-up (Bianconi arXiv:2503.14048). **T1 does not re-prove that duality**; it only compares residual of PM vs heat as reconstructors of \(\phi_\star\).

---

## 2. Precise lattice proposition (target)

> **Proposition T1 (lattice, single jump; target).**  
> Fix constants \(c_K\in[1,3]\) and set \(K=c_K\sigma\). There exist \(t_\star>0\), \(N_0\in\mathbb{N}\), and \(c_{\mathrm{edge}}>1\), depending only on \((c_K,\sigma)\) through universal combinations of \(\sigma\) and \(K\), such that the following holds.
>
> For every \(N\ge N_0\) and every wall-clock time \(t\in(0,t_\star]\) that is an integer multiple of a CFL-stable Euler step \(dt\in(0,dt_{\max}]\) (e.g. \(dt_{\max}=1/8\)), let \(\hat\phi^{\mathrm{heat}}(t)\) and \(\hat\phi^{\mathrm{PM}}(t)\) be the heat and PM trajectories of §1.4 starting from \(y=\phi_\star+\eta\) with \(\eta\sim\mathcal{N}(0,\sigma^2 I_N)\). Then
>
> \[
> \mathbb{E}\bigl[R\bigl(\hat\phi^{\mathrm{PM}}(t),\phi_\star\bigr)\bigr]
> \;\le\;
> \mathbb{E}\bigl[R\bigl(\hat\phi^{\mathrm{heat}}(t),\phi_\star\bigr)\bigr],
> \]
>
> and
>
> \[
> \mathbb{E}\bigl[\mathrm{EdgeHeight}\bigl(\hat\phi^{\mathrm{PM}}(t)\bigr)\bigr]
> \;\ge\;
> c_{\mathrm{edge}}\,
> \mathbb{E}\bigl[\mathrm{EdgeHeight}\bigl(\hat\phi^{\mathrm{heat}}(t)\bigr)\bigr].
> \]

**What “proved” would mean.** Full proof of both displays under the stated assumptions, with explicit (or effectively computable) \(t_\star,N_0,c_{\mathrm{edge}}\).  
**Current status:** **not proved**. Lemmas A–E below form the intended reduction. Joint toy §6 is an **experimental witness** at one \((N,\sigma,K,dt,T_{\mathrm{run}})\).

**Conjecture T1+ (optional strengthening).**  
The same inequality holds pathwise with high probability (not only in expectation), and along a dense time grid up to \(t_\star\), with residual improvement margin \(\Omega(\sqrt{t})\) for small \(t\).

**Conjecture T1-load (link to T3).**  
If \(\tau(t)=\int_0^t (1+\alpha_L L_{\mathrm{clock}}(s))^{-1}\,ds\le t\), then for all wall-clock \(t\) with \(\tau(t)\in(0,t_\star]\),
\[
\mathbb{E}\bigl[R\bigl(\hat\phi^{\mathrm{load}}(t),\phi_\star\bigr)\bigr]
\;\le\;
\mathbb{E}\bigl[R\bigl(\hat\phi^{\mathrm{heat}}(t),\phi_\star\bigr)\bigr]
\]
still holds (load-PM may lag pure PM but need not lose to heat). Status: **conjecture**; see §5.

---

## 3. Assumptions (checklist)

| ID | Assumption | Toy match | Role in T1 |
|----|------------|-----------|------------|
| A1 | \(\phi_\star\) is a single unit jump at \(i_\star\) | `phi_star_step` | Isolates one interface |
| A2 | \(\eta_i\stackrel{\mathrm{iid}}{\sim}\mathcal{N}(0,\sigma^2)\) | `make_observation` | Concentration for edge location |
| A3 | \(K=c_K\sigma\), \(c_K\in[1,3]\) | \(K=0.15\), \(\sigma=0.12\) | True jump \(\gg K\); noise grads \(O(\sigma)\) |
| A4 | Explicit Euler, same \(dt\) for heat and PM; CFL-stable \(dt\) | `DT=0.08`, `step_euler` | Stable discrete dynamics |
| A5 | Short-time window \(t\le t_\star\) | Scorecard uses full run \(T=N_{\mathrm{steps}}\,dt=14.4\); analytic \(t_\star\) may be smaller | Avoid long-time staircasing / interface drift |
| A6 | \(N\) not exponentially large in \(1/\sigma^2\) | \(N=192\) | Union bound over edges |
| A7 | Neumann-type ends; no periodic identification of the jump | toy `divergence_from_edge_flux` | Boundary effects \(O(1/N)\) away from \(e_\star\) |

**Out of scope for this proposition:** multi-jump interference, smooth ramps (ramp is a **stability** check, not residual domination), continuum white-noise SPDE limits, adaptive \(dt\), Catte-smoothed 2D PM.

---

## 4. Heuristic picture (why heat loses)

1. **Heat** is isotropic low-pass filtering. The jump’s high-frequency content is damped by factors \(\sim e^{-t\xi^2}\) in the Fourier (or discrete spectral) picture. The deterministic step becomes an error-function transition of width \(\Theta(\sqrt{t})\), which contributes a **positive** bulk residual near \(e_\star\) of order \(\Theta(\sqrt{t}/N)\) in mean-square (lattice mean), independent of beneficial noise smoothing.

2. **PM** multiplies edge fluxes by \(\rho\le 1\). On the true jump, \(|\nabla y|_{e_\star}\approx 1+O(\sigma)\gg K\), so \(\rho_{e_\star}\approx (K/|\nabla|)^2\ll 1\): the interface is **almost insulating**. Each plateau then behaves like heat flow on a half-chain with nearly Neumann boundary condition at \(e_\star\).

3. On a constant plateau, residual is pure noise energy. Half-chain heat flow reduces that energy **without** paying the \(\Theta(\sqrt{t})\) jump-blur penalty. Hence short-time residual of PM can undercut heat while \(\mathrm{EdgeHeight}\) stays order \(1\).

This is standard anisotropic-diffusion intuition; Lemmas A–E make the residual comparison quantitative.

---

## 5. Lemma stack A–E

Each item: **statement**, **proof idea**, **status**. Status key: **proved sketch** / **open**.

---

### Lemma A — Noise reduction on a constant domain  
**Status: proved sketch** (classical Gaussian heat kernel / discrete spectral calculation; continuum scaling constants still to pin to lattice mean-square)

**Statement.**  
Let \(\Omega_+\!=\!\{i_\star,\ldots,N-1\}\) and \(\Omega_-\!=\!\{0,\ldots,i_\star-1\}\). Suppose \(u(t)\) solves discrete heat flow on \(\Omega_\pm\) with **Neumann** condition at the artificial boundary \(e_\star\) (no flux across \(e_\star\)) and the same Neumann ends as the toy, with initial data pure noise \(\eta|_{\Omega_\pm}\). Then for times \(t\) with \(1\ll t\ll N^2\) (diffusion has mixed locally but not fully mixed the half-chain),

\[
\mathbb{E}\!\left[\frac{1}{|\Omega_\pm|}\sum_{i\in\Omega_\pm} u_i(t)^2\right]
\;=\;
\sigma^2\cdot \Psi_\pm(t,N),
\]

where \(\Psi_\pm(t,N)\downarrow 0\) as \(t\) increases through the short-time window, and in the infinite-half-line continuum analogue one has the scaling

\[
\mathbb{E}\int_{\mathbb{R}_\pm} u_{\mathrm{noise}}(t,x)^2\,dx
\;=\;
\Theta\bigl(\sigma^2\, t^{-1/4}\bigr)
\quad\text{(1D white-noise / spectral heuristic; lattice needs a UV cutoff).}
\]

Any reconstructor that keeps flux across \(e_\star\) of size \(o(1)\) relative to heat inherits the same plateau noise-reduction rate up to a multiplicative \(1+o(1)\) factor.

**Proof idea.**  
- On a fixed finite graph with Neumann Laplacian \(\Delta_N\), \(u(t)=e^{t\Delta_N}\eta\), so \(\mathbb{E}\|u(t)\|_2^2=\sigma^2\,\mathrm{Tr}(e^{2t\Delta_N})\).  
- Short-time trace asymptotics of the heat kernel on a 1D chain give a decaying noise energy (high modes die as \(e^{-c t \xi^2}\)).  
- Continuum half-line calculation with Neumann reflection is standard; match lattice by Poisson summation / eigenvalue spacing \(O(1/N)\).  
- **Gap inside A:** convert continuum \(\Theta(\sigma^2 t^{-1/4})\) integrated residual into lattice **mean** residual \(\frac1N\sum_i\), with explicit constants for \(N=192\).

**Status detail.** Spectral identity is elementary (**closed** for finite graphs). Continuum scaling and transfer of constants to the toy residual normalization are **sketch**. Full matching of \(\Psi\) to joint-toy parameters is **open**.

---

### Lemma B — PM freezes super-threshold interfaces  
**Status: proved sketch** (elementary algebraic bound on \(\rho\); dynamical permanence of the threshold is Lemma C)

**Statement.**  
At any configuration \(v\in\mathbb{R}^N\), if the jump height on edge \(e_\star\) satisfies

\[
\bigl|(\nabla v)_{e_\star}\bigr| \;\ge\; c\,K
\quad\text{for a fixed }c>1,
\]

then the PM conductivity and flux on that edge obey

\[
\rho_{e_\star}
\;=\;
\frac{1}{1+\bigl((\nabla v)_{e_\star}/K\bigr)^2}
\;\le\;
\frac{1}{c^2},
\qquad
\bigl|F^{\mathrm{PM}}_{e_\star}\bigr|
\;=\;
\rho_{e_\star}\bigl|(\nabla v)_{e_\star}\bigr|
\;\le\;
\frac{K}{c}.
\]

In particular, relative to isotropic flux \(F^{\mathrm{heat}}_{e_\star}=(\nabla v)_{e_\star}\),

\[
\bigl|F^{\mathrm{PM}}_{e_\star}\bigr|
\;\le\;
\frac{1}{c^2}\,\bigl|F^{\mathrm{heat}}_{e_\star}\bigr|.
\]

Over a time interval of length \(t\) on which the threshold \(|\nabla v|_{e_\star}\ge cK\) is maintained, the **mass leaked** across \(e_\star\) is \(O(t K/c)\) in \(\ell^1\) (hence \(O(t^2 K^2/c^2)\) contribution to squared residual after spreading \(O(1)\) sites), vs \(O(t)\) leakage under heat when \(|\nabla|\sim 1\).

**Proof idea.**  
Immediate from \(\rho=1/(1+(g/K)^2)\le (K/g)^2\le 1/c^2\) when \(|g|\ge cK\). Integrate the edge ODE for the jump height:

\[
\frac{d}{dt}(\nabla v)_{e_\star}
\;=\;
(\mathrm{div}\,F)_{i_\star}-(\mathrm{div}\,F)_{i_\star-1},
\]

and bound the contribution of the single cross-edge flux term by \(2|F_{e_\star}|\le 2K/c\).

**Status detail.** Algebraic flux bound: **closed**. Converting “\(O(t/c^2)\) leakage” into a sharp residual additive term with universal constants: **sketch**. Requires Lemma C to keep \(c\) valid on \([0,t]\).

---

### Lemma C — Short-time edge persistence under PM (high probability)  
**Status: open** (Gaussian tails + union bound give *initial* localization; *dynamical* persistence under nonlinear PM is the main gap)

**Statement.**  
Assume A1–A3, A6. There exist constants \(c>1\), \(T=T(\sigma,K,N)>0\), and \(\delta\in(0,1)\) such that, with probability at least \(1-\delta\),

1. **Initial localization.** The maximizer of \(|\nabla y|\) is the true edge \(e_\star\), and
   \[
   \bigl|(\nabla y)_{e_\star}\bigr| \;\ge\; c\,K,
   \]
   while for all other edges \(e\neq e_\star\),
   \[
   \bigl|(\nabla y)_e\bigr| \;\le\; \tfrac{c}{2}\,K.
   \]
2. **Persistence.** Along the explicit-Euler PM trajectory, for all \(t\in[0,T]\),
   \[
   \bigl|(\nabla\hat\phi^{\mathrm{PM}}(t))_{e_\star}\bigr| \;\ge\; c\,K.
   \]

**Proof idea (two layers).**

*Layer C1 — initial localization (nearly closed).*  
\[
(\nabla y)_{e_\star}=1+\eta_{i_\star}-\eta_{i_\star-1}\sim\mathcal{N}(1,2\sigma^2),
\]
while for \(e\neq e_\star\), \((\nabla y)_e\sim\mathcal{N}(0,2\sigma^2)\) (adjacent edges are weakly dependent).  
Gaussian tail:

\[
\mathbb{P}\bigl(|(\nabla y)_e| > \lambda\bigr)
\;\le\;
2\exp\bigl(-\lambda^2/(4\sigma^2)\bigr).
\]

Union bound over \(N-1\) false edges: choose \(\lambda = \Theta(\sigma\sqrt{\log N})\).  
Require true jump lower tail:

\[
\mathbb{P}\bigl((\nabla y)_{e_\star} < 1 - \Theta(\sigma\sqrt{\log(1/\delta)})\bigr)
\;\le\;\delta/2.
\]

With \(K=c_K\sigma\) and \(1\gg \sigma\sqrt{\log N}\) (A6), one can pick \(c\in(1,1/(c_K\sigma))\) so that with high probability \(cK \le |(\nabla y)_{e_\star}|\) and false edges stay below \(cK/2\).  
For toy numbers: \(\sigma=0.12\), \(\sigma\sqrt{\log N}\approx 0.12\sqrt{5.26}\approx 0.28\), true jump \(1\), \(K=0.15\) — room exists but constants need care for *dependent* edges and for \(c\) large enough that \(1/c^2\) is small in Lemma B.

*Layer C2 — dynamical persistence (open).*  
Need to show that PM does not:

- collapse the true jump below \(cK\) before time \(T\), or  
- create a competing super-threshold false edge that steals residual budget.

Tools: (i) Lemma B flux bound while threshold holds; (ii) discrete maximum principle / comparison for the regularized Euler map; (iii) control of bulk noise gradients under anisotropic diffusion (they evolve almost by heat with \(\rho\approx 1\) on plateaus).  
**Forward–backward continuum PM is ill-posed** in general; the proof must stay inside the **regularized Euler scheme** (\(K>0\), small \(dt\)) used by the toy, which is a globally Lipschitz map \(\mathbb{R}^N\to\mathbb{R}^N\) for fixed \(dt,K\).

**Status detail.** C1: **proved sketch** (fill dependent-edge covariance and explicit \(c,\delta\)). C2: **open** (core analytic gap of T1).

---

### Lemma D — Heat must blur the jump  
**Status: proved sketch** (deterministic step vs heat kernel is classical; noise cross-term needs a short calculation)

**Statement.**  
Let \(\hat\phi^{\mathrm{heat}}(t)=e^{t\Delta}y = e^{t\Delta}\phi_\star + e^{t\Delta}\eta\). Write residual as

\[
N\,R(\hat\phi^{\mathrm{heat}}(t),\phi_\star)
\;=\;
\bigl\|e^{t\Delta}\phi_\star-\phi_\star\bigr\|_2^2
\;+\;
\bigl\|e^{t\Delta}\eta\bigr\|_2^2
\;+\;
2\bigl\langle e^{t\Delta}\phi_\star-\phi_\star,\, e^{t\Delta}\eta\bigr\rangle.
\]

Then:

1. **Deterministic blur (main term).** There exist \(c_D,C_D>0\) and \(t_0>0\) such that for all \(t\in(0,t_0]\),
   \[
   \bigl\|e^{t\Delta}\phi_\star-\phi_\star\bigr\|_2^2
   \;\ge\;
   c_D\,\sqrt{t}
   \qquad\text{(1D step vs heat; lattice: same order with \(h=1\))}
   \]
   and \(\le C_D\sqrt{t}\). Continuum model: \(e^{t\partial_{xx}}\mathbf{1}_{x\ge 0}\) has transition \(\mathrm{erfc}(x/\sqrt{4t})\); integrated squared error against the step is \(\Theta(\sqrt{t})\).

2. **Noise energy.** \(\mathbb{E}\|e^{t\Delta}\eta\|_2^2 = \sigma^2\,\mathrm{Tr}(e^{2t\Delta})\) is **decreasing** in \(t\) and equals \(N\sigma^2\) at \(t=0\).

3. **Cross term.** \(\mathbb{E}[\langle e^{t\Delta}\phi_\star-\phi_\star,\, e^{t\Delta}\eta\rangle]=0\).

Hence for the **expected residual**,

\[
\mathbb{E}\,R(\hat\phi^{\mathrm{heat}}(t),\phi_\star)
\;\ge\;
\frac{c_D}{N}\sqrt{t}
\;+\;
\frac{\sigma^2}{N}\,\mathrm{Tr}(e^{2t\Delta})
\;\ge\;
\frac{c_D}{N}\sqrt{t}.
\]

(The noise term is positive but is shared in spirit with PM plateaus; the **discriminating** lower bound is the \(\Omega(\sqrt{t}/N)\) blur.)

**Proof idea.**  
Fourier / explicit convolution with discrete heat kernel; compare to continuum error function on scale \(\sqrt{t}\) away from boundaries (jump is at mid-domain: distance \(\Theta(N)\)). For \(t\ll N^2\), boundary effects are negligible near \(e_\star\).

**Status detail.** Continuum deterministic lower bound: **closed** (standard). Lattice transfer + explicit \(c_D\) for Neumann chain: **sketch**. Cross-term vanishing in expectation: **closed**.

---

### Lemma E — PM residual upper bound and comparison  
**Status: open** (depends on C; comparison architecture clear)

**Statement.**  
On the high-probability event \(\mathcal{E}\) of Lemma C, for all \(t\in(0,T]\),

\[
R\bigl(\hat\phi^{\mathrm{PM}}(t),\phi_\star\bigr)
\;\le\;
R_{\mathrm{plateau}}(t)
\;+\;
R_{\mathrm{interface}}(t),
\]

where:

- \(R_{\mathrm{plateau}}\) is comparable to the residual of two independent Neumann half-chain heat flows of the noise (Lemma A), up to a multiplicative factor \(1+O(1/c^2)\) from residual conductivity on non-edge edges and \(O(t/c)\) interface leakage (Lemma B);  
- \(R_{\mathrm{interface}}=O\bigl((t K/c)^2 / N\bigr)\) (or better after localizing mass near \(e_\star\)).

Consequently, for \(c\) large enough and \(t\in(0,t_\star]\) with \(t_\star\le T\),

\[
\mathbb{E}\bigl[R(\hat\phi^{\mathrm{PM}}(t),\phi_\star)\bigr]
\;\le\;
\mathbb{E}\bigl[R(\hat\phi^{\mathrm{heat}}(t),\phi_\star)\bigr].
\]

Moreover, on \(\mathcal{E}\), \(\mathrm{EdgeHeight}(\hat\phi^{\mathrm{PM}}(t))\ge cK\), while heat satisfies \(\mathrm{EdgeHeight}(\hat\phi^{\mathrm{heat}}(t))=O(t^{-1/2})\) for the deterministic part (plus noise), yielding the edge-height inequality of Proposition T1 after taking expectations and adjusting \(c_{\mathrm{edge}}\).

**Proof idea (comparison architecture).**

1. **Split residual** into plateau sites (distance \(\ge r(t)\) from \(e_\star\)) and interface collar (width \(r(t)=\Theta(\sqrt{t})\) or fixed \(O(1)\) sites).  
2. **Plateau:** couple PM to Neumann heat via flux difference \(\|(1-\rho)\nabla v\|\); on plateaus \(\rho\to 1\) after a short transient if gradients are \(O(\sigma)\). Bound \(\mathbb{E} R_{\mathrm{plateau}}\) by Lemma A.  
3. **Interface:** use Lemma B to cap mass exchange; true jump remains \(\ge cK\) on \(\mathcal{E}\).  
4. **Heat lower bound:** Lemma D supplies \(\Omega(\sqrt{t}/N)\) that PM does **not** pay.  
5. **Choose parameters:**  
   \[
   \underbrace{C\sigma^2\,\Psi(t)}_{\text{shared noise floor}}
   +
   \underbrace{O(t^2 K^2/(c^2 N))}_{\text{PM interface}}
   \;\le\;
   \underbrace{c_D\sqrt{t}/N}_{\text{heat blur}}
   +
   \underbrace{\sigma^2\,\mathrm{Tr}(e^{2t\Delta})/N}_{\text{heat noise}}.
   \]
   For small \(t>0\), \(\sqrt{t}\) dominates \(t^2\); for large \(c\), interface pollution is negligible. Pick \(t_\star\) small enough that the inequality is strict in expectation, then extend by continuity on the discrete time grid.

**Status detail.** Architecture: **proved sketch** (as a reduction). Quantitative closure: **open**, blocked primarily by Lemma C (persistence) and constant-matching to A/D.

---

### Auxiliary note — Well-posedness of toy PM  
**Status: proved sketch** (for the scheme actually used)

The map \(v\mapsto \mathrm{div}(\rho(v)\nabla v)\) with \(\rho=1/(1+(g/K)^2)\) and \(K>0\) is \(C^\infty\) and globally Lipschitz on \(\mathbb{R}^N\) (each \(\rho g = g/(1+(g/K)^2)\) is bounded and Lipschitz in \(g\)). Explicit Euler with fixed \(dt\) is therefore a globally defined iteration; no continuum forward–backward pathology enters the lattice proposition. Stability in \(\ell^2\) for small \(dt\) follows from the flux bound \(|\rho g|\le K/2\).

---

## 6. How load-gating interacts with T1

### 6.1 Time change

Load terms in the toy (`load_terms`):

\[
\begin{aligned}
L_E &= c_E\,\mathbb{E}\bigl[(\nabla\hat\phi)^2\bigr],\\
L_S &= c_S\,|\Delta H_c|/\Delta t,\\
L_{\mathrm{clock}} &= L_E+L_S \;\ge\; 0.
\end{aligned}
\]

Load-gated step:

\[
dt_{\mathrm{eff}}
\;=\;
\frac{dt}{1+\alpha_L L_{\mathrm{clock}}}.
\]

If \(L_{\mathrm{clock}}\) is evaluated along the trajectory (as in the toy), the load-PM path is a **monotone time change** of pure PM in the continuum idealization:

\[
\hat\phi^{\mathrm{load}}(t)
\;=\;
\hat\phi^{\mathrm{PM}}\bigl(\tau(t)\bigr),
\qquad
\tau(t)
\;=\;
\int_0^t \frac{ds}{1+\alpha_L L_{\mathrm{clock}}(s)}
\;\le\;
t.
\]

(Discrete Euler with state-dependent \(dt_{\mathrm{eff}}\) is a consistent discretization of that ODE time change when \(dt\to 0\).)

### 6.2 Consequences for residual domination

| Claim | Status |
|-------|--------|
| Load-PM residual at wall-clock \(t\) equals pure-PM residual at internal time \(\tau(t)\le t\) (continuum idealization) | **proved sketch** (definition of time change) |
| Pure PM residual is nonincreasing in \(t\) on the short-time event \(\mathcal{E}\) (denoising dominates) | **conjecture / experimental witness** (scorecard mono on `noisy_step` ≈ 1.0); needed for T2/T3 |
| Therefore load-PM residual \(\ge\) pure-PM residual at the same wall-clock \(t\) (load is “behind”) | **conditional** on residual monotone decrease for PM |
| Load-PM still beats heat at wall-clock \(t\) if \(\tau(t)\in(0,t_\star]\) and heat’s blur term grows fast enough that \(\mathbb{E}R_{\mathrm{PM}}(\tau)\le\mathbb{E}R_{\mathrm{heat}}(t)\) | **Conjecture T1-load** (§2) |

**Honest short-time reading.**  
Load-gating **does not break** the PM mechanism (same vector field, slower clock). It can make residual **slightly worse** than pure PM at fixed wall-clock \(t\) (less denoising completed) while **preserving** edge freeze. Domination vs heat is a **race**: heat pays \(\Omega(\sqrt{t})\) blur in wall-clock time; load-PM pays almost none but progresses only \(\tau(t)\). For small \(\alpha_L L_{\mathrm{clock}}\) or moderate \(t\), the race still favors load-PM experimentally on `noisy_step`.

### 6.3 Link to program T3

Program T3 in ACD-EW: load-gating is a monotone reparameterization that preserves descent of a channel Lyapunov.  
T1 is about **PM vs heat** at equal wall-clock time. T3 is about **load-PM vs pure PM** as reparameterizations of the **same** flow. Closing T1 does not automatically close T3; closing T3 does not replace Lemma C. The bridge is: once residual (or \(H_c\)) is monotone along pure PM on \(\mathcal{E}\), any time change inherits descent in internal time.

---

## 7. What the joint toy scorecard does and does not prove

Implementation: `_joint_toy_v2_core.py` · defaults \(N=192\), \(\sigma=0.12\), \(K=0.15\), \(dt=0.08\), \(N_{\mathrm{steps}}=180\), seeds 101–104 for ICs.  
Reported v2 scorecard: **6/6 SUPPORT** ([gfe_load_joint_toy_scorecard_v2.txt](../simulations/bridging/gfe_load_joint_toy_scorecard_v2.txt)).

### 7.1 Criteria map to T1

| Scorecard | Statement (approx) | Relation to T1 |
|-----------|--------------------|----------------|
| **[1]** | PM residual improvement vs heat: `noisy_step` impro \(>0.05\); bumps \(>0\) | **Witness** of residual domination at **final** time on one seed path (step) + secondary IC |
| **[2]** | PM edge retention \(>1.15\times\) heat on step ICs | **Witness** of edge-height half of Proposition T1 |
| **[3]** | Ramp: PM max-grad ratio \(<2.5\) | **Not T1** — stability / anti-staircasing (P0); supports that \(K\sim\sigma\) is well-tuned |
| **[4]** | \(\mathrm{corr}(L_E,\mathbb{E}[G-1])>0.85\) | **Not T1** — Stage-2 load induction bookkeeping |
| **[5]** | Load-gating slows mid-run \(\ell^2\) change vs PM | **Witness** of time change (§6); not residual domination |
| **[6]** | On `noisy_step`: final \(R_{\mathrm{PM}}<R_{\mathrm{heat}}\) and mono fraction of PM \(\ge\) heat’s \(-\,0.05\) | **Witness** of residual path quality; closest single check to T1 |

Primary dual IC for T1: **`noisy_step`**.  
`clean_step` witnesses edge freeze **without** noise (Lemma B regime with \(c\) large).  
`noisy_two_bumps` / `noisy_ramp` are **outside** Proposition T1’s single-jump statement.

### 7.2 What the scorecard **does** establish

1. **Existence of a parameter regime** where residual and edge metrics favor PM over heat on a unit jump + i.i.d. Gaussian noise (constructive support for A1–A4).  
2. **Reproducibility** under fixed seeds (deterministic CLI).  
3. **Compatibility** of load-gating with residual dual on the same IC (experimental support for Conjecture T1-load, not a proof).  
4. **No immediate contradiction** with the Lemma A–E architecture (edge retention ≫ heat; residual impro ~0.37 on step).

### 7.3 What the scorecard **does not** establish

1. **Expectation** \(\mathbb{E}[R_{\mathrm{PM}}]\le\mathbb{E}[R_{\mathrm{heat}}]\) — one (or few) noise draws, not Monte Carlo over \(\eta\).  
2. **Uniformity in \(t\in(0,t_\star]\)** — checks emphasize final time / snapshot grid, not a proved short-time envelope.  
3. **All \(N,\sigma\)** — single lattice size and noise level.  
4. **Lemmas C–E** — no analytic edge-persistence or residual split.  
5. **Continuum limit** or Bianconi field equations.  
6. **Theorem-level ACD-EW** — still “experimentally constructive + T1 outline,” not a published residual-domination theorem.

**Label:** joint toy outcomes are **experimental witnesses**, not proofs.

---

## 8. Roadmap to close gaps (ordered checklist)

Complete in order; later items depend on earlier ones.

| # | Task | Closes | Output |
|---|------|--------|--------|
| **G0** | Freeze notation: residual as lattice mean-square; edge height as \(\max|\nabla|\); Euler PM as the only dynamics | Scope | This note (done as target) |
| **G1** | Write precise lattice noise + heat-kernel lemmas for the Neumann chain (no continuum white-noise SPDE) | Lemma A constants; Lemma D lattice | Appendix: \(\mathrm{Tr}(e^{2t\Delta})\), \(\|e^{t\Delta}\phi_\star-\phi_\star\|_2^2\ge c_D\sqrt{t}\) |
| **G2** | Finish **Lemma C1** with dependent-edge covariances; explicit \((c,\delta,N_0)\) for \(K=c_K\sigma\) | Initial localization | Probabilistic lemma with numbers covering \(\sigma=0.12\), \(N=192\) |
| **G3** | Prove **Lemma C2** for explicit Euler PM: jump height stays \(\ge cK\) on \([0,T]\); control false-edge creation | Main analytic gap | Persistence theorem for the scheme |
| **G4** | Execute **Lemma E** comparison with explicit \(t_\star,c_{\mathrm{edge}}\) | Proposition T1 residual + edge | Full proof of target proposition |
| **G5** | Monte Carlo validation: estimate \(\mathbb{E}[R_{\mathrm{PM}}-R_{\mathrm{heat}}]\) over \(\ge 10^2\) seeds for \(t\) on a grid in \((0,t_\star]\) | Experimental envelope of T1 | Notebook / CLI table (still not a proof) |
| **G6** | Optional: pathwise high-probability form (Conjecture T1+) | Stronger claim | Extra concentration |
| **G7** | Load: prove residual monotone decrease for pure PM on \(\mathcal{E}\), then Conjecture T1-load | Link T1↔T3 | Short corollary |
| **G8** | Multi-jump localization if jumps are separated by \(\gg\sqrt{t}\) | Beyond single jump | Separate note; not required for T1 |
| **G9** | Match constants to full toy window \(T=14.4\) or document that analytic \(t_\star\ll T\) while experiments run longer | Theory–toy reconciliation | Remark in proposition statement |

**Suggested first paper-quality milestone:** G1+G2+G3+G4 ⇒ **Proposition T1 proved** for the lattice Euler scheme.  
**Until then:** cite as **proof plan + experimental witness**.

---

## 9. Status summary (lemma board)

| Item | Role | Status |
|------|------|--------|
| **Proposition T1** on \((0,t_\star]\) | Residual domination for all short \(t>0\) | **Obstruction** (MC: heat wins residual for \(t\lesssim 1\)) — see [m1-lemma-c-prime.md](m1-lemma-c-prime.md) |
| **Proposition T1′** on \([t_{\min},t_{\max}]\) | Residual domination after noise transient | **Hybrid on \(I_\star=\{1.36,\ldots,1.60\}\)** ([m1d](m1d-lemma-e-prime.md)); pure theorem open (freeze-tax spectral); MC \([1.2,6.4+]\) |
| **Conjecture T1+** | Pathwise / dense-time strengthening | **Open** |
| **Conjecture T1-load / M2** | Load-PM vs heat at wall-clock \(t\) | **Hybrid on \(I_\star\)** ([m2-t1-load.md](m2-t1-load.md)); pure open |
| **Lemma A** | Plateau noise reduction (Neumann heat) | **Proved sketch** |
| **Lemma B** | Super-threshold flux freeze \(\rho\le 1/c^2\) | **Proved sketch** (algebra **closed**) |
| **Lemma C** (original) | False edges \(<cK/2\) + persistence | **Superseded** — false-edge gap fails empirically |
| **Lemma C′ / C′2♯** | Argmax + height persistence | **C′1/C′1b + C′2♯ \(T^\sharp\approx 1.67\)** ([m1](m1-lemma-c-prime.md)–[m1c](m1c-c2-sharp-delta-noise.md)) |
| **Lemma D** | Heat blur lower bound \(\Omega(\sqrt{t})\) | **Proved sketch** |
| **Lemma E / E′** | PM residual upper bound + comparison | **Unified pure \(U_\star=[1.36,2.40]\)** ([m1g](m1g-unified-pure-window.md)); hybrid history in m1d; \(\rho_{\mathrm{eff}}\) late window in m1f |
| **Well-posedness (Euler PM)** | Scheme is globally Lipschitz | **Proved sketch** |
| **Joint toy [1],[2],[6]** | Numerical residual/edge dual on `noisy_step` | **Experimental witness** (final \(t\gg t_{\min}\)) |
| **MC envelope** | \(n=200\) seeds, residual vs \(t\) | **Experimental witness** (`t1_mc_envelope.txt`) |

---

## 10. Discrete–continuum dictionary (toy)

| Continuum / analysis object | Joint toy object |
|----------------------------|------------------|
| \(\phi_\star=\mathbf{1}_{x\ge 0}\) | `phi_star_step` |
| \(y=\phi_\star+\eta\) | `make_observation(..., sigma=NOISE_SIGMA)` |
| Heat | `mode="heat"`, `rhs_heat` |
| PM, \(K=\Theta(\sigma)\) | `mode="pm"`, `K_PM=0.15` |
| Residual \(R\) | `residual_mse` |
| Edge height | `max_grad` in history |
| Load time change | `mode="load_pm"`, `dt * clock` |
| GfE warm-up action | `gfe_action` = \(-\sum\ln G\), \(G=1+\alpha_G(\nabla\phi)^2\) |

---

## 11. References (minimal)

1. **Parent duality note:** `synthesis/action-channel-duality-euclidean.md` §3.2 (T1–T4), §10 (original sketch expanded here).  
2. **Toy core / scorecard:** `simulations/bridging/_joint_toy_v2_core.py`, `DESIGN_gfe_load_joint_toy.md`.  
3. **Bianconi warm-up dual only:** G. Bianconi, *Beyond holography*, arXiv:2503.14048 — PM as gradient flow of Euclidean GfE warm-up between support metric and structure-induced metric. **Not** used here as a derivation of residual domination or of continuum gravity.

---

## 12. One-paragraph takeaway

**T1 residual domination** asserts that, for a single lattice jump observed in i.i.d. Gaussian noise with contrast \(K=\Theta(\sigma)\), short-time explicit-Euler Perona–Malik beats isotropic heat in expected residual MSE while retaining larger edge height — because PM nearly freezes the true interface and denoises plateaus like Neumann heat, whereas heat must blur the jump at scale \(\sqrt{t}\). The claim is reduced to Lemmas A–E; **B and the linear parts of A/D are elementary sketches**, while **C (persistence) and E (comparison)** remain **open**. The joint toy’s `noisy_step` scorecard is a strong **experimental witness**, not a proof. Load-gating is a slower clock on the same PM field and yields **Conjecture T1-load**, not a free corollary of T1. Until G1–G4 close, residual domination must be cited as a **proposition target + proof plan**.

---

*Note status: living proof plan. Update lemma board when G1–G4 land. Do not mark Proposition T1 closed without a complete writeup of C and E.*
