# 8. Euclidean dual ACD-EW --- T1′ / $U_\star$, claims A--D, toys as witnesses

### 5.1 Scope: Layers W and D only

This part concerns a **constructive Euclidean dual**, not continuum gravitational equivalence. Two layers must be kept distinct.

**Layer W (warm-up).** On a flat Euclidean support, Bianconi's Gravity-from-Entropy (GfE) program admits a scalar warm-up in which a structure-induced metric


$$
G[\phi] \;=\; 1 + \alpha_G\,(\nabla\phi)^2
$$


enters a relative-entropy / logarithmic action density $\mathcal{L}=-\ln G$ (edgewise on a lattice). In continuum language (external literature; not re-derived here), the $L^2$-gradient flow of the associated energy is classical Perona--Malik (PM) anisotropic diffusion; isotropic heat is the special case of unit conductivity. Discrete toys implement explicit-Euler PM (and a Catte-style lift in 2D) on a lattice field $\phi$. Layer W is about **action/energy and PM flow**, not about residual dual scorecards and not about Lorentzian GfE field equations.

**Layer D (dual).** Action--Channel Duality, Euclidean Warm-Up (**ACD-EW**) pairs that warm-up geometry with an **observation channel**: a hidden field $\phi_\star$ is observed as $y=\phi_\star+\eta$, reconstructed by heat, PM, or load-gated PM, scored by a residual/edge entropy proxy $H_c^{\mathrm{toy}}$, and summarized by a split scalar load that can reparameterize the reconstruction clock. Layer D is about **channel residual, load clock, and residual dual windows**. It does **not** automatically transfer to continuum GfE (**G**) or to the gravitational master equation (**M**).

**Type safety.** Load $L$ (and toy $L_{\mathrm{clock}}$) is a **dimensionless scalar** demand. Structure-induced $G$ is a **metric** (or edgewise cousin). **$L\neq G$**. Results proved or scorecarded only on W or D must not be cited as G or M theorems. In particular: lattice denoising is **not** empirical gravity; residual dual is **not** master-equation $\Leftrightarrow$ continuum GfE.

---

### 5.2 ACD-EW construction

**Support and state (1D primary toy).** Sites $i=0,\ldots,N-1$ (default $N=192$, spacing $h=1$); support metric $g_i\equiv 1$; scalar field $\phi\in\mathbb{R}^N$; edge gradients $(\nabla\phi)_i=\phi_{i+1}-\phi_i$.

**Stage 2 --- shared geometric object.** The induced edgewise metric $G_i[\phi]=1+\alpha_G(\nabla\phi)_i^2$ is simultaneously (i) the GfE warm-up second metric (Bianconi Stage 2--3 input) and (ii) the geometric imprint of local reconstructed structure in our workflow. Duality **hinges** on this shared Stage-2 object: both readings act on the same $G[\hat\phi]$.

**Stage 3 --- warm-up action and PM flow.** Edgewise warm-up density $\mathcal{L}_i^{\mathrm{GfE}}=-\ln G_i[\phi]$; total action $S_{\mathrm{GfE}}[\phi]=\sum_i\mathcal{L}_i^{\mathrm{GfE}}$. Dynamics on the GfE side are gradient flow implemented as Perona--Malik conductivity


$$
\rho_i \;=\; \frac{1}{1+\bigl((\nabla\phi)_i/K\bigr)^2},\qquad
\partial_t\phi \;=\; \operatorname{div}(\rho\,\nabla\phi),
$$


with $K$ of order the observation noise scale. External literature (Bianconi, *Beyond holography*) identifies continuum PM with the Euclidean GfE warm-up gradient flow; this program treats that identification as **literature structure for Layer W**, not as a re-proof of the continuum variational identity.

**Stage 1 --- observation channel.** Hidden structure $\phi_\star$; observation $y=\phi_\star+\eta$ with i.i.d. Gaussian noise $\eta\sim\mathcal{N}(0,\sigma^2 I)$ (default $\sigma=0.12$); reconstructor $\mathcal{C}_t:y\mapsto\hat\phi(t)$ given by heat, PM, or load-gated PM with $\hat\phi(0)=y$. Residual energy $R=\mathrm{mean}_i(\hat\phi_i-\phi_{\star,i})^2$; residual entropy proxy $H_R=\log(1+R/\sigma_{\mathrm{ref}}^2)$; edge-location entropy $H_{\mathrm{edge}}=-\sum_i p_i\log_2 p_i$ with $p\propto|\nabla\hat\phi|$. The dual **channel score** is


$$
H_c^{\mathrm{toy}}(\hat\phi\mid\phi_\star) \;=\; H_R + \lambda_e H_{\mathrm{edge}}
$$


(tag **C** in the M10 object dictionary). Lower $H_c^{\mathrm{toy}}$ means better reconstruction / more localized edge mass. This is a **supervised residual score**, not Shannon entropy of a generic map output and not von Neumann $S_c$.

**Stage 1 --- split load.** $L_E=c_E\mathbb{E}[(\nabla\hat\phi)^2]$ tracks induction intensity (and $\mathbb{E}[G-1]$); $L_S=c_S|\Delta H_c^{\mathrm{toy}}|/\Delta t$ tracks rate of channel-score change; $L_B$ is a capacity-like edge saturation not used in the v2 clock; $L_{\mathrm{clock}}=L_E+L_S$. Load-gated dynamics use the same PM vector field with $dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}})$, a discrete analogue of 

$$
d\tau=dt/(1+\alpha L)
$$

.

**Duality statement (ACD-EW).** On this Euclidean special case: (A) $G[\hat\phi]$ is shared Stage 2; (B) PM is a structure-preserving reconstructor that reduces residual relative to isotropic heat on jump-like $\phi_\star$ with noise; (C) $L_E$ associates with induction intensity and load-gating slows mid-run evolution without erasing PM's residual/edge advantages; (D) dynamics admit dual language (maximize / flow $S_{\mathrm{GfE}}$ $\leftrightarrow$ run structure-preserving channel $\mathcal{C}^{\mathrm{GfE}}$). **Rigor for the existence of this dual construction: constructive** (definitions + implemented toys), with residual dual theorems hybrid/soft as in §5.3.

**What ACD-EW does not claim.** Equivalence of full Lorentzian GfE (curvature-in-$G$, G-field, $\Lambda_G$) to the gravitational master equation; numeric identity $H_c^{\mathrm{toy}}\equiv S_{\mathrm{GfE}}$ or $H_c^{\mathrm{toy}}\equiv S_c$; identity $L\equiv G$; continuum gravity confirmation from lattice denoising.

---

### 5.3 Claims A--D (T1′ residual dual)

Primary analytic setting (T1′ write-up): unit step $\phi_\star=\mathbf{1}_{i\ge N/2}$, $\sigma=0.12$, $K=0.15$, explicit Euler $dt=0.08$. Residual $R=N^{-1}\|\hat\phi-\phi_\star\|_2^2$. The residual dual is **time-windowed (T1′)**, not residual domination for all $t\in(0,t_\star]$ (**C4**).

#### Claim A --- Unified pure residual window $U_\star$ (**C5**)

On the unified pure window


$$
U_\star \;=\; [1.36,\,2.40]
$$


(grid times in $U_\star$), under a spectral majorant with burn-in conductivity $\rho_b=0.42$, Dirichlet-form linear theory, interface bound, and PCRH$_b$,


$$
\mathbb{E}\,R_{\mathrm{PM}}(t) \;\le\; \mathbb{E}\,R_{\mathrm{heat}}(t).
$$


PCRH$_b$ is an **ensemble residual majorant** (large-MC certificate): **soft**. The unified pure argument covers the former hybrid intermediate grid $I_\star$ and the former pure-late band $[2.0,2.4]$ in one window. The short-time crossover $t\approx 1.2$ remains **outside** $U_\star$.

**Rigor:** analytic majorant + identity machinery, with **soft** PCRH$_b$ input.

#### Claim B --- Edge persistence (**C6**)

With probability $\gtrsim 0.87$, initial true jump height $H^0\ge 0.80$. On that high-probability event, for all $t\le T_{\mathrm{pers}}^\sharp\approx 1.67$,


$$
H^t \;\ge\; H_{\mathrm{floor}}=0.25 \;>\; K
$$


(super-threshold freeze; Lemma C′2#).

**Rigor:** **analytic** (flux ODE bound + Gaussian concentration).

#### Claim C --- Short-$t$ heat win as noise race (**C7**)

For $t\lesssim 1.2$, heat can win residual because noise reduction dominates jump blur. This is **not** dual failure. The identity


$$
\mathbb{E}(R_{\mathrm{heat}}-R_{\mathrm{PM}}) \;=\; R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}
$$


holds to numerical precision; crossover when $R_{\mathrm{blur}}=\Delta_{\mathrm{noise}}$ near $t\sim 1.2$. Mechanism in brief: heat must blur the unit jump on scale $\sqrt{t}$ (deterministic residual $\Theta(\sqrt{t}/N)$); PM freezes the true edge and plateaus but freezes some noise gradients too (noise-race tax $\Delta_{\mathrm{noise}}$); residual dual holds when blur exceeds that tax.

**Rigor:** **analytic identity** + **hybrid-experimental** accounting.

#### Claim D --- Load-PM as mild time change (**C8**)

Load-PM is a monotone time change of pure PM: internal time $\tau(t)=\int_0^t(1+\alpha_L L_{\mathrm{clock}})^{-1}\,ds\le t$. Empirically $\tau/t\sim 0.95$--$0.98$ on the dual window. Residual dual of load-PM versus heat is supported experimentally on the same window (high Monte Carlo pathwise fractions on $I_\star$ / $U_\star$).

**Rigor:** time-change definition **constructive**; residual dual vs heat **hybrid-experimental**.

#### Soft spot: PCRH$_b$

PCRH$_b$ (with $\rho_b=0.42$) is **ensemble-certified** for the toy class. A full pathwise Dirichlet-form proof without certificate remains **open**. Do not assert pure T1′ with **no** soft hypotheses. Further pure-proof polishing is optional paper depth, not a main program crisis: the residual dual program is **settled enough** at T1′ / $U_\star$.

**Paste-ready citation sentence.** *In a 1D lattice observation model with a single noisy jump, PM residual domination over isotropic heat holds on an intermediate window $U_\star=[1.36,2.40]$ (T1′; PCRH$_b$, $\rho_b=0.42$), with analytic edge persistence and noise-versus-blur accounting; load reparameterization preserves the dual experimentally as a slower clock. This supports constructive Euclidean ACD-EW, not continuum gravitational equivalence.*

---

### 5.4 Joint toys as pattern witnesses (6/6 SUPPORT)

Beyond the residual-window analysis, joint toys implement the full ACD-EW special case (observation + split load + scorecard criteria E1--E7). Under fixed seeds and IC families:

| Toy | Role | Outcome |
|-----|------|---------|
| 1D joint toy | Noisy step / two-bumps / ramp; heat vs PM vs load-PM | **6/6 SUPPORT** |
| 2D joint toy | Catte-style PM lift on planar lattice | **6/6 SUPPORT** |
| Blackjack-belief dual | Game-motivated field $\phi$ (belief geometry) | **6/6 SUPPORT**, **pattern only** |

**Interpretation (C2--C3).** Six-of-six SUPPORT means the Euclidean dual **pattern** is robust under these IC classes: PM residual better than heat on primary edged ICs; edge retention; no staircase on weak-gradient ramps; $L_E$ tracks $\mathbb{E}[G-1]$; load-gating slows mid-run evolution. That PM outperforms heat on edged structure is **expected** dual success, not a theory bug. Blackjack-belief is **not** blackjack EV, strategy ROI, or predictive card-channel $H_c^{\mathrm{game}}$.

**Non-claims for toys.** Lattice denoising is not empirical gravity. Scorecard success does not lift residual dual to continuum SPDE residual domination, multi-jump theorem-level domination, or 2D theorem-level residual dual. Toys witness **Layer D pattern**, not Layer G/M equivalence.

**Rigor:** **hybrid-experimental** (**C2**); structural expectation of PM > heat on edges (**C3**).

---

### 5.5 M5c / M5b: warm-up continuum vs dual residual

Layer W continuum hygiene and Layer D residual dual must not be conflated.

**M5b (smooth action limit --- conditional lemma).** Under hypotheses H1--H4 (fixed $C^3$ periodic field, point sampling, fixed $\alpha>0$, mesh $h\to 0$), the mesh-weighted discrete Euclidean warm-up action $S_h[\phi|_{\mathrm{grid}}]=h\sum_i -\ln\bigl(1+\alpha(D_h\phi)_i^2\bigr)$ approximates the continuum integral $S[\phi]=\int -\ln\bigl(1+\alpha|\phi'|^2\bigr)\,dx$ with error at most $C(\alpha,\|\phi'\|_\infty,\|\phi''\|_\infty,\|\phi'''\|_\infty)\,h$; the argument is Taylor consistency of forward differences, global Lipschitz continuity of $z\mapsto -\ln(1+\alpha z^2)$, and a standard Riemann-sum estimate (see Appendix A.5). This is a **conditional smooth lemma** (Layer **W** action consistency), **not** Γ-convergence, not a BV/jump theorem, not residual dual continuum, and not Lorentzian GfE or master-equation contact.

**M5c (PM energy descent, Layer W).** Continuum literature identifies PM with the gradient flow of the Euclidean warm-up energy/action (matched coupling $\alpha=1/K^2$ equates energy descent with action ascent up to a positive factor). On the discrete side, joint-toy explicit-Euler PM is consistent with **discrete gradient descent** of an edge energy whose conductivity matches the toy flux (under stated hypotheses; not a full scheme-convergence theorem). Optional numerical witnesses check energy descent along PM trajectories.

**Relationship to residual dual.** M5c lives on **Layer W**: action/energy and PM flux. Residual dual $H_c^{\mathrm{toy}}$ and T1′ / $U_\star$ live on **Layer D**. Discrete energy descent of the warm-up does **not** identify residual dual with continuum relative entropy of metrics, nor with von Neumann $S_c$. Continuum PM well-posedness / Catte regularization as $h\to 0$ and full T4 (Γ-limit + BV + residual dual continuum) remain **open**. The dual residual program and the warm-up continuum program are **siblings under ACD-EW**, not the same theorem.

---

### 5.6 M10 P1: non-identity of entropy objects

ACD-EW uses $H_c^{\mathrm{toy}}$ (tag **C**). Foundations computational entropy $H_c(f;p_X)=H(Y)$ is map-output Shannon (tag **A**). Gravity uses $S_c(\Phi;\rho)=S(\Phi(\rho))$ (tag **B**). These must not be silently identified.

**M10 P1** (hybrid-experimental) measures both $H_c^{\mathrm{toy}}$ and ensemble Shannon $H(Z)$ of coarsened reconstructor observables $Z(\hat\phi)$ (binary edge-location cut; 8-bin argmax of $|\nabla\hat\phi|$) on the standard 1D dual at times in / near $U_\star$. On that grid, MC means of $H_c^{\mathrm{toy}}$ sit near **$\sim 1.1$--$1.3$**, while ensemble $H(Z_{\mathrm{bin}})$ and $H(Z_8)$ are **$\approx 0$** (or at most $\mathcal{O}(0.1)$ on one heat row): residual dual quality and unsupervised coarsened Shannon of declared edge location are **not the same measured object**.

Structural reasons (definitional, no MC needed): $H_c^{\mathrm{toy}}$ is a **per-sample supervised score** using oracle $\phi_\star$ via residual $R$; $H(Z)$ is **across-sample Shannon** of a declared coarse alphabet without residual supervision. Aggregation, edge role (soft within-field entropy vs hard argmax location), and units differ. Residual dual ($R_{\mathrm{PM}}<R_{\mathrm{heat}}$) can hold while $H(Z)\approx 0$.

**Non-claims.** Not $S_c$; not continuum GfE; not $H_c^{\mathrm{toy}}\equiv H(Y)$ for the full field $\hat\phi\in\mathbb{R}^N$; not a proof that no other $Z$ ever co-moves. House style: tag $H_c^{\mathrm{toy}}$ on dual residual; reserve bare $H_c$ for unambiguous Tag A; never write $H_c^{\mathrm{toy}}=S_c$.

---

### 5.7 Claim inventory for Part 5

| ID | One-line | Rigor |
|----|----------|-------|
| **C1** | ACD-EW constructive Euclidean dual (warm-up $G[\phi]$, PM, observation channel, split load, load clock) | constructive (+ toys hybrid) |
| **C2** | Joint toys 6/6 SUPPORT: dual **pattern** robust | hybrid-experimental |
| **C3** | PM > heat on edged structure is expected dual success | structural |
| **C4** | Residual dual is time-windowed T1′, not all $t\in(0,t_\star]$ | analytic + hybrid |
| **C5** | $U_\star=[1.36,2.40]$, $\rho_b=0.42$, PCRH$_b$ soft | analytic + soft |
| **C6** | Edge persistence $H_{\mathrm{floor}}=0.25>K$ through $T_{\mathrm{pers}}^\sharp\approx 1.67$ | analytic |
| **C7** | Short-$t$ noise race; identity $R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}$; crossover $\sim 1.2$ | analytic identity + hybrid |
| **C8** | Load-PM mild time change; residual dual vs heat on window | hybrid-experimental |

---
