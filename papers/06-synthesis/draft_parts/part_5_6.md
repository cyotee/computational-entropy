# Parts 5–6 — Euclidean Dual (ACD-EW) and Continuum GfE Contact (M6)

**Draft status:** Program research prose (2026-07-15) · claim-gated  
**Authority:** [CURRENT_CLAIMS.md](../../../synthesis/CURRENT_CLAIMS.md) · [CLAIM_GATE.md](../../../synthesis/CLAIM_GATE.md) · [OUTLINE.md](../OUTLINE.md) Parts 5–6  
**Stance:** Preliminary research. Prefer under-claiming. Nothing here has GR-level certainty.  
**Claim IDs covered:** **C1–C8** (§5); **C11–C13** (§6).  
**Layer codes:** **W** = Euclidean GfE warm-up; **D** = ACD-EW observation dual; **G** = continuum Bianconi GfE; **M** = master equation / \(\Phi_g\), continuum \(L\).

---

## 5. Euclidean dual ACD-EW — T1′ / \(U_\star\), claims A–D, toys as witnesses

### 5.1 Scope: Layers W and D only

This part concerns a **constructive Euclidean dual**, not continuum gravitational equivalence. Two layers must be kept distinct.

**Layer W (warm-up).** On a flat Euclidean support, Bianconi’s Gravity-from-Entropy (GfE) program admits a scalar warm-up in which a structure-induced metric

\[
G[\phi] \;=\; 1 + \alpha_G\,(\nabla\phi)^2
\]

enters a relative-entropy / logarithmic action density \(\mathcal{L}=-\ln G\) (edgewise on a lattice). In continuum language (external literature; not re-derived here), the \(L^2\)-gradient flow of the associated energy is classical Perona–Malik (PM) anisotropic diffusion; isotropic heat is the special case of unit conductivity. Discrete toys implement explicit-Euler PM (and a Catte-style lift in 2D) on a lattice field \(\phi\). Layer W is about **action/energy and PM flow**, not about residual dual scorecards and not about Lorentzian GfE field equations.

**Layer D (dual).** Action–Channel Duality, Euclidean Warm-Up (**ACD-EW**) pairs that warm-up geometry with an **observation channel**: a hidden field \(\phi_\star\) is observed as \(y=\phi_\star+\eta\), reconstructed by heat, PM, or load-gated PM, scored by a residual/edge entropy proxy \(H_c^{\mathrm{toy}}\), and summarized by a split scalar load that can reparameterize the reconstruction clock. Layer D is about **channel residual, load clock, and residual dual windows**. It does **not** automatically transfer to continuum GfE (**G**) or to the gravitational master equation (**M**).

**Type safety.** Load \(L\) (and toy \(L_{\mathrm{clock}}\)) is a **dimensionless scalar** demand. Structure-induced \(G\) is a **metric** (or edgewise cousin). **\(L\neq G\)**. Results proved or scorecarded only on W or D must not be cited as G or M theorems. In particular: lattice denoising is **not** empirical gravity; residual dual is **not** master-equation \(\Leftrightarrow\) continuum GfE.

---

### 5.2 ACD-EW construction

**Support and state (1D primary toy).** Sites \(i=0,\ldots,N-1\) (default \(N=192\), spacing \(h=1\)); support metric \(g_i\equiv 1\); scalar field \(\phi\in\mathbb{R}^N\); edge gradients \((\nabla\phi)_i=\phi_{i+1}-\phi_i\).

**Stage 2 — shared geometric object.** The induced edgewise metric \(G_i[\phi]=1+\alpha_G(\nabla\phi)_i^2\) is simultaneously (i) the GfE warm-up second metric (Bianconi Stage 2–3 input) and (ii) the geometric imprint of local reconstructed structure in our workflow. Duality **hinges** on this shared Stage-2 object: both readings act on the same \(G[\hat\phi]\).

**Stage 3 — warm-up action and PM flow.** Edgewise warm-up density \(\mathcal{L}_i^{\mathrm{GfE}}=-\ln G_i[\phi]\); total action \(S_{\mathrm{GfE}}[\phi]=\sum_i\mathcal{L}_i^{\mathrm{GfE}}\). Dynamics on the GfE side are gradient flow implemented as Perona–Malik conductivity

\[
\rho_i \;=\; \frac{1}{1+\bigl((\nabla\phi)_i/K\bigr)^2},\qquad
\partial_t\phi \;=\; \operatorname{div}(\rho\,\nabla\phi),
\]

with \(K\) of order the observation noise scale. External literature (Bianconi, *Beyond holography*) identifies continuum PM with the Euclidean GfE warm-up gradient flow; this repository treats that identification as **literature structure for Layer W**, not as a re-proof of the continuum variational identity.

**Stage 1 — observation channel.** Hidden structure \(\phi_\star\); observation \(y=\phi_\star+\eta\) with i.i.d. Gaussian noise \(\eta\sim\mathcal{N}(0,\sigma^2 I)\) (default \(\sigma=0.12\)); reconstructor \(\mathcal{C}_t:y\mapsto\hat\phi(t)\) given by heat, PM, or load-gated PM with \(\hat\phi(0)=y\). Residual energy \(R=\mathrm{mean}_i(\hat\phi_i-\phi_{\star,i})^2\); residual entropy proxy \(H_R=\log(1+R/\sigma_{\mathrm{ref}}^2)\); edge-location entropy \(H_{\mathrm{edge}}=-\sum_i p_i\log_2 p_i\) with \(p\propto|\nabla\hat\phi|\). The dual **channel score** is

\[
H_c^{\mathrm{toy}}(\hat\phi\mid\phi_\star) \;=\; H_R + \lambda_e H_{\mathrm{edge}}
\]

(tag **C** in the M10 object dictionary). Lower \(H_c^{\mathrm{toy}}\) means better reconstruction / more localized edge mass. This is a **supervised residual score**, not Shannon entropy of a generic map output and not von Neumann \(S_c\).

**Stage 1 — split load.** \(L_E=c_E\mathbb{E}[(\nabla\hat\phi)^2]\) tracks induction intensity (and \(\mathbb{E}[G-1]\)); \(L_S=c_S|\Delta H_c^{\mathrm{toy}}|/\Delta t\) tracks rate of channel-score change; \(L_B\) is a capacity-like edge saturation not used in the v2 clock; \(L_{\mathrm{clock}}=L_E+L_S\). Load-gated dynamics use the same PM vector field with \(dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}})\), a discrete analogue of \(d\tau=dt/(1+\alpha L)\).

**Duality statement (ACD-EW).** On this Euclidean special case: (A) \(G[\hat\phi]\) is shared Stage 2; (B) PM is a structure-preserving reconstructor that reduces residual relative to isotropic heat on jump-like \(\phi_\star\) with noise; (C) \(L_E\) associates with induction intensity and load-gating slows mid-run evolution without erasing PM’s residual/edge advantages; (D) dynamics admit dual language (maximize / flow \(S_{\mathrm{GfE}}\) \(\leftrightarrow\) run structure-preserving channel \(\mathcal{C}^{\mathrm{GfE}}\)). **Rigor for the existence of this dual construction: constructive** (definitions + implemented toys), with residual dual theorems hybrid/soft as in §5.3.

**What ACD-EW does not claim.** Equivalence of full Lorentzian GfE (curvature-in-\(G\), G-field, \(\Lambda_G\)) to the gravitational master equation; numeric identity \(H_c^{\mathrm{toy}}\equiv S_{\mathrm{GfE}}\) or \(H_c^{\mathrm{toy}}\equiv S_c\); identity \(L\equiv G\); continuum gravity confirmation from lattice denoising.

---

### 5.3 Claims A–D (T1′ residual dual)

Primary analytic setting (T1′ write-up): unit step \(\phi_\star=\mathbf{1}_{i\ge N/2}\), \(\sigma=0.12\), \(K=0.15\), explicit Euler \(dt=0.08\). Residual \(R=N^{-1}\|\hat\phi-\phi_\star\|_2^2\). The residual dual is **time-windowed (T1′)**, not residual domination for all \(t\in(0,t_\star]\) (**C4**).

#### Claim A — Unified pure residual window \(U_\star\) (**C5**)

On the unified pure window

\[
U_\star \;=\; [1.36,\,2.40]
\]

(grid times in \(U_\star\)), under a spectral majorant with burn-in conductivity \(\rho_b=0.42\), Dirichlet-form linear theory, interface bound, and PCRH\(_b\),

\[
\mathbb{E}\,R_{\mathrm{PM}}(t) \;\le\; \mathbb{E}\,R_{\mathrm{heat}}(t).
\]

PCRH\(_b\) is an **ensemble residual majorant** (large-MC certificate): **soft**. The unified pure argument covers the former hybrid intermediate grid \(I_\star\) and the former pure-late band \([2.0,2.4]\) in one window. The short-time crossover \(t\approx 1.2\) remains **outside** \(U_\star\).

**Rigor:** analytic majorant + identity machinery, with **soft** PCRH\(_b\) input.

#### Claim B — Edge persistence (**C6**)

With probability \(\gtrsim 0.87\), initial true jump height \(H^0\ge 0.80\). On that high-probability event, for all \(t\le T_{\mathrm{pers}}^\sharp\approx 1.67\),

\[
H^t \;\ge\; H_{\mathrm{floor}}=0.25 \;>\; K
\]

(super-threshold freeze; Lemma C′2♯).

**Rigor:** **analytic** (flux ODE bound + Gaussian concentration).

#### Claim C — Short-\(t\) heat win as noise race (**C7**)

For \(t\lesssim 1.2\), heat can win residual because noise reduction dominates jump blur. This is **not** dual failure. The identity

\[
\mathbb{E}(R_{\mathrm{heat}}-R_{\mathrm{PM}}) \;=\; R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}
\]

holds to numerical precision; crossover when \(R_{\mathrm{blur}}=\Delta_{\mathrm{noise}}\) near \(t\sim 1.2\). Mechanism in brief: heat must blur the unit jump on scale \(\sqrt{t}\) (deterministic residual \(\Theta(\sqrt{t}/N)\)); PM freezes the true edge and plateaus but freezes some noise gradients too (noise-race tax \(\Delta_{\mathrm{noise}}\)); residual dual holds when blur exceeds that tax.

**Rigor:** **analytic identity** + **hybrid-experimental** accounting.

#### Claim D — Load-PM as mild time change (**C8**)

Load-PM is a monotone time change of pure PM: internal time \(\tau(t)=\int_0^t(1+\alpha_L L_{\mathrm{clock}})^{-1}\,ds\le t\). Empirically \(\tau/t\sim 0.95\)–\(0.98\) on the dual window. Residual dual of load-PM versus heat is supported experimentally on the same window (high Monte Carlo pathwise fractions on \(I_\star\) / \(U_\star\)).

**Rigor:** time-change definition **constructive**; residual dual vs heat **hybrid-experimental**.

#### Soft spot: PCRH\(_b\)

PCRH\(_b\) (with \(\rho_b=0.42\)) is **ensemble-certified** for the toy class. A full pathwise Dirichlet-form proof without certificate remains **open**. Do not assert pure T1′ with **no** soft hypotheses. Further pure-proof polishing is optional paper depth, not a main program crisis: the residual dual program is **settled enough** at T1′ / \(U_\star\).

**Paste-ready citation sentence.** *In a 1D lattice observation model with a single noisy jump, PM residual domination over isotropic heat holds on an intermediate window \(U_\star=[1.36,2.40]\) (T1′; PCRH\(_b\), \(\rho_b=0.42\)), with analytic edge persistence and noise-versus-blur accounting; load reparameterization preserves the dual experimentally as a slower clock. This supports constructive Euclidean ACD-EW, not continuum gravitational equivalence.*

---

### 5.4 Joint toys as pattern witnesses (6/6 SUPPORT)

Beyond the residual-window analysis, joint toys implement the full ACD-EW special case (observation + split load + scorecard criteria E1–E7). Under fixed seeds and IC families:

| Toy | Role | Outcome |
|-----|------|---------|
| 1D joint toy | Noisy step / two-bumps / ramp; heat vs PM vs load-PM | **6/6 SUPPORT** |
| 2D joint toy | Catte-style PM lift on planar lattice | **6/6 SUPPORT** |
| Blackjack-belief dual | Game-motivated field \(\phi\) (belief geometry) | **6/6 SUPPORT**, **pattern only** |

**Interpretation (C2–C3).** Six-of-six SUPPORT means the Euclidean dual **pattern** is robust under these IC classes: PM residual better than heat on primary edged ICs; edge retention; no staircase on weak-gradient ramps; \(L_E\) tracks \(\mathbb{E}[G-1]\); load-gating slows mid-run evolution. That PM outperforms heat on edged structure is **expected** dual success, not a theory bug. Blackjack-belief is **not** blackjack EV, strategy ROI, or predictive card-channel \(H_c^{\mathrm{game}}\).

**Non-claims for toys.** Lattice denoising is not empirical gravity. Scorecard success does not lift residual dual to continuum SPDE residual domination, multi-jump theorem-level domination, or 2D theorem-level residual dual. Toys witness **Layer D pattern**, not Layer G/M equivalence.

**Rigor:** **hybrid-experimental** (**C2**); structural expectation of PM > heat on edges (**C3**).

---

### 5.5 M5c / M5b: warm-up continuum vs dual residual

Layer W continuum hygiene and Layer D residual dual must not be conflated.

**M5b (smooth action limit).** Under \(C^3\) hypotheses, the mesh-weighted discrete warm-up action \(S_h[\phi]=h\sum_i -\ln(1+\alpha(D_h\phi)_i^2)\) is an \(O(h)\) Riemann-sum consistent approximation to the continuum integral \(\int -\ln(1+\alpha|\phi'|^2)\,dx\). This is a **conditional smooth lemma**, not Γ-convergence, not BV/jump continuum residual dual, and not Lorentzian GfE.

**M5c (PM energy descent, Layer W).** Continuum literature identifies PM with the gradient flow of the Euclidean warm-up energy/action (matched coupling \(\alpha=1/K^2\) equates energy descent with action ascent up to a positive factor). On the discrete side, joint-toy explicit-Euler PM is consistent with **discrete gradient descent** of an edge energy whose conductivity matches the toy flux (under stated hypotheses; not a full scheme-convergence theorem). Optional numerical witnesses check energy descent along PM trajectories.

**Relationship to residual dual.** M5c lives on **Layer W**: action/energy and PM flux. Residual dual \(H_c^{\mathrm{toy}}\) and T1′ / \(U_\star\) live on **Layer D**. Discrete energy descent of the warm-up does **not** identify residual dual with continuum relative entropy of metrics, nor with von Neumann \(S_c\). Continuum PM well-posedness / Catte regularization as \(h\to 0\) and full T4 (Γ-limit + BV + residual dual continuum) remain **open**. The dual residual program and the warm-up continuum program are **siblings under ACD-EW**, not the same theorem.

---

### 5.6 M10 P1: non-identity of entropy objects

ACD-EW uses \(H_c^{\mathrm{toy}}\) (tag **C**). Foundations computational entropy \(H_c(f;p_X)=H(Y)\) is map-output Shannon (tag **A**). Gravity uses \(S_c(\Phi;\rho)=S(\Phi(\rho))\) (tag **B**). These must not be silently identified.

**M10 P1** (hybrid-experimental) measures both \(H_c^{\mathrm{toy}}\) and ensemble Shannon \(H(Z)\) of coarsened reconstructor observables \(Z(\hat\phi)\) (binary edge-location cut; 8-bin argmax of \(|\nabla\hat\phi|\)) on the standard 1D dual at times in / near \(U_\star\). On that grid, MC means of \(H_c^{\mathrm{toy}}\) sit near **\(\sim 1.1\)–\(1.3\)**, while ensemble \(H(Z_{\mathrm{bin}})\) and \(H(Z_8)\) are **\(\approx 0\)** (or at most \(\mathcal{O}(0.1)\) on one heat row): residual dual quality and unsupervised coarsened Shannon of declared edge location are **not the same measured object**.

Structural reasons (definitional, no MC needed): \(H_c^{\mathrm{toy}}\) is a **per-sample supervised score** using oracle \(\phi_\star\) via residual \(R\); \(H(Z)\) is **across-sample Shannon** of a declared coarse alphabet without residual supervision. Aggregation, edge role (soft within-field entropy vs hard argmax location), and units differ. Residual dual (\(R_{\mathrm{PM}}<R_{\mathrm{heat}}\)) can hold while \(H(Z)\approx 0\).

**Non-claims.** Not \(S_c\); not continuum GfE; not \(H_c^{\mathrm{toy}}\equiv H(Y)\) for the full field \(\hat\phi\in\mathbb{R}^N\); not a proof that no other \(Z\) ever co-moves. House style: tag \(H_c^{\mathrm{toy}}\) on dual residual; reserve bare \(H_c\) for unambiguous Tag A; never write \(H_c^{\mathrm{toy}}=S_c\).

---

### 5.7 Claim inventory for Part 5

| ID | One-line | Rigor |
|----|----------|-------|
| **C1** | ACD-EW constructive Euclidean dual (warm-up \(G[\phi]\), PM, observation channel, split load, load clock) | constructive (+ toys hybrid) |
| **C2** | Joint toys 6/6 SUPPORT: dual **pattern** robust | hybrid-experimental |
| **C3** | PM > heat on edged structure is expected dual success | structural |
| **C4** | Residual dual is time-windowed T1′, not all \(t\in(0,t_\star]\) | analytic + hybrid |
| **C5** | \(U_\star=[1.36,2.40]\), \(\rho_b=0.42\), PCRH\(_b\) soft | analytic + soft |
| **C6** | Edge persistence \(H_{\mathrm{floor}}=0.25>K\) through \(T_{\mathrm{pers}}^\sharp\approx 1.67\) | analytic |
| **C7** | Short-\(t\) noise race; identity \(R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\); crossover \(\sim 1.2\) | analytic identity + hybrid |
| **C8** | Load-PM mild time change; residual dual vs heat on window | hybrid-experimental |

---

## 6. Continuum GfE contact — M6 WEAK PASS / FAIL; M6b structural FAIL

### 6.1 Shared weak-field problem

Parts 3–4 recover Newtonian Poisson on **our** side via **Path J/M** only (Clausius → Einstein → weak-field GR; load-clock on-shell calibration \(\alpha\beta=4\pi G/c^4\)). Continuum Bianconi GfE is a **different** upper theory: relative entropy of metrics, low-coupling Einstein–Hilbert limit, and modified equations with \(\Lambda_G\), \(D_{\mu\nu}\), dressed \(R^G\) away from strict low coupling. M6 asks only whether the two frameworks agree on a **shared weak-field problem**, not whether they are the same theory.

**Shared problem (static weak field).** Background Minkowski plus static Newtonian potential \(\Phi\ll c^2\); classical mass density \(\rho_m(\mathbf{x})\) (perfect fluid at rest, \(T_{00}\approx\rho_m c^2\)). Ask for the **leading** equation determining \(\Phi\).

**Side A — ours (Path J/M).** Assume \(\mathcal{L}_g\) satisfies Clausius on local horizons so that the Einstein equation holds (Jacobson 1995 imported), or take Einstein as the thermodynamic fixed point of the channel generator. Weak-field GR yields \(\nabla^2\Phi=4\pi G\rho_m\). Load \(L\approx\beta_L\rho_m c^2/\epsilon_0\) calibrates the proper-time factor to the same \(\Phi\) via on-shell matching \(\alpha_L\beta_L=4\pi G/c^4\) (**Path M calibration**), not via the withdrawn pointwise Laplacian identity \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\).

**Side B — Bianconi GfE (documented low coupling).** At low coupling the entropic action reduces to Einstein–Hilbert with zero cosmological constant (external paper claim). Standard GR weak-field linearization on that EH theory again yields \(\nabla^2\Phi=4\pi G\rho_m\). Newton here is **via GR**, not via a load clock. Away from strict low coupling, modified equations involve \(\Lambda_G(\tilde{\mathcal{G}})\), dressed \(R^G\), and \(D_{\mu\nu}\).

---

### 6.2 WEAK PASS at Poisson order (**C11**)

| Item | Ours (Path J/M) | GfE low coupling |
|------|-----------------|------------------|
| Leading PDE for \(\Phi\) | \(\nabla^2\Phi=4\pi G\rho_m\) | \(\nabla^2\Phi=4\pi G\rho_m\) |
| Mechanism | Clausius/Einstein + load calibration | Relative-entropy action → EH → GR linearization |
| Extra fields at leading Newton | None if \(\gamma_L,\delta_L\) dropped | None if \(\tilde{\mathcal{G}}=\tilde I\), \(\Lambda_G=0\) |

**Outcome:** **WEAK PASS** — same leading Poisson equation. Equations agree at this order. The agreement is **real** and **expected** if both frameworks embed Einstein gravity at low demand. It is **supporting circumstantial evidence** that they sit in the same phenomenological class as GR — **not** evidence that load dynamics equal Bianconi’s relative-entropy Euler–Lagrange equations.

**Honesty limits.** WEAK PASS does **not** upgrade either theory to GR-level certainty. Path J still depends on Jacobson/Einstein input; Poisson is not free from GR. We did **not** solve Bianconi’s field equations numerically.

---

### 6.3 FAIL of framework identity (**C12**)

| Criterion | Outcome |
|-----------|---------|
| Same leading Poisson \(\nabla^2\Phi=4\pi G\rho_m\) | **WEAK PASS** |
| Same upper derivation mechanism | **FAIL** |
| Identifiable \((\alpha_L,\beta_L)=(\alpha_B,\beta_B)\) | **FAIL / refused** (M7) |
| Continuum GfE \(\Leftrightarrow\) master equation | **FAIL** — do not claim |

**Mechanisms differ.** Ours: Clausius constraint on a channel generator, Einstein as fixed point, load as scalar demand clock. GfE: relative entropy of metrics as primary action, low-coupling EH, then GR. Shared Poisson is shared **GR linearization**, not shared primary entropy object.

**Constant refusal.** Do **not** assert \(\alpha_L\beta_L=\alpha_B/\beta_B\) (or \(\alpha_L\beta_L\equiv\alpha_B/\beta_B\)). The product \(\alpha_L\beta_L\) is an **on-shell calibration** of our load clock to Newtonian redshift (Path M). The ratio \(\alpha_B/\beta_B\) is a **coupling constant in Bianconi’s field equations** (schematic \(\kappa=\alpha_B/\beta_B\)). Different roles; identification is refused without a new OPEN_MATH decision and an explicit continuum map. Also refuse \(L\equiv G\) and \(S_c\equiv\operatorname{Tr} g\ln G^{-1}\).

---

### 6.4 M6b: next-order structural FAIL (**C13**)

Leading Poisson does not discriminate mechanisms. Discrimination lives at **next order**.

**Our next-order candidates.** Full load

\[
L \;=\; \beta_L\frac{\rho_m c^2}{\epsilon_0} + \gamma_L\left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}} + \delta_L\frac{S_{\mathrm{boundary}}}{S_{\mathrm{BH}}},
\]

with clock expansion \(d\tau/dt=1/(1+\alpha_L L)=1-\alpha_L L+\alpha_L^2 L^2-\cdots\). In a static weak field, \(\gamma_L L_S\) vanishes in strict equilibrium and \(\delta_L L_\partial\) is a screen term; nonlinear \(\alpha_L^2 L_E^2\) is PPN-like bookkeeping only if carefully mapped. Crucially: under Path J the **metric** is primarily Einstein-sourced. Default reading of \(\gamma_L,\delta_L\) is **additive scalar corrections to the clock**, not automatic modifications of \(\nabla^2\Phi=4\pi G\rho_m\), unless a dynamical rule promotes \(L_S,L_\partial\) into effective stress.

**GfE next-order candidates.** Schematic modified sector: \(R^G_{(\mu\nu)}-\frac12 g_{\mu\nu}(R_G-2\Lambda_G)+D_{(\mu\nu)}=\kappa T_{(\mu\nu)}\) with \(\Lambda_G\ge 0\) from the G-field functional and \(D_{\mu\nu}\) from G-field derivatives. Linearized deformations of Poisson may involve Yukawa/scalar modes, effective \(G_N\) renormalization, or emergent cosmological terms — **structurally inside the metric field equations**.

**Primary structural conclusion.** Next-order extras **do not match as the same object class**:

| Ours (next order) | GfE (next order) | Label |
|-------------------|------------------|-------|
| \(\gamma_L\|dS_c/d\tau\|\) in load **clock** | \(D_{\mu\nu}\) in metric EOM | type mismatch unless a map is built |
| \(\delta_L S_{\partial}/S_{\mathrm{BH}}\) screen ratio | not primary as holographic screen term in GfE action | does not map cleanly |
| load reparam only (no new Poisson source by default) | \(\Lambda_G\), \(D_{\mu\nu}\) **do** enter metric EOM | **structural divergence** |
| no intrinsic \(\Lambda\) from load at low order | \(\Lambda_G\ge 0\) from G-field alone | **structural divergence** |

**Outcome:** **structural FAIL** of next-order match (**C13**). Coefficient-level PPN / Yukawa comparison is **not established** (needs explicit Bianconi linearization). Do **not** assert \(\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G\).

---

### 6.5 Interpretation: co-class via GR, not shared primary entropy

M6’s honest reading is **co-class membership** with general relativity at low demand, not framework identity:

1. Both sides can recover \(\nabla^2\Phi=4\pi G\rho_m\) because both (under stated assumptions) sit on the Einstein/GR weak-field track at leading order.
2. Upper mechanisms differ: channel + load clock versus relative entropy of metrics.
3. Next-order structures live in different slots: **clock factors** versus **metric EOM extras**.
4. Therefore Poisson agreement is **not** evidence that continuum load dynamics equal Bianconi EL equations, and **not** evidence that master equation \(\Leftrightarrow\) continuum GfE.

**Where the interesting dual remains.** The constructive dual that is **settled enough** in this program is **ACD-EW on Layers W and D** (Part 5): shared Stage-2 \(G[\phi]\), PM as reconstructor, residual dual T1′ / \(U_\star\), load as mild time change. That dual is a **different mathematical layer** from M6’s Lorentzian weak-field plug-test. Euclidean residual dual does **not** lift automatically to Poisson agreement; Poisson agreement does **not** lift residual dual to continuum gravity. Stage-1 / Stage-2 / Stage-3 of the program mental model must not be collapsed into symbolic identity of master equation and GfE action.

**Non-claims (M6 block).** No numerical solution of Bianconi field equations; no derivation of \(\alpha_L\beta_L\) from \(\alpha_B,\beta_B\); no master equation \(\Leftrightarrow\) GfE; no next-order \(\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G\); WEAK PASS does not confer GR-level certainty; Path J still imports Jacobson/Einstein.

---

### 6.6 Claim inventory for Part 6

| ID | One-line | Rigor |
|----|----------|-------|
| **C11** | M6: both frameworks → \(\nabla^2\Phi=4\pi G\rho_m\) via Einstein/GR at leading weak field | **WEAK PASS** |
| **C12** | M6: not framework equivalence; mechanisms diverge; refuse \((\alpha_L,\beta_L)=(\alpha_B,\beta_B)\) | **FAIL identity** |
| **C13** | M6b: GfE extras in metric EOM; \(\gamma_L,\delta_L\) in load clock unless promoted | **structural FAIL** |

---

## Sources (Parts 5–6)

| Role | Path |
|------|------|
| Claims freeze C1–C8, C11–C13 | `synthesis/CURRENT_CLAIMS.md` |
| Claim gate / layers W D G M | `synthesis/CLAIM_GATE.md` |
| ACD-EW formal dual | `synthesis/action-channel-duality-euclidean.md` |
| T1′ claims A–D | `synthesis/t1-prime-hybrid-writeup.md` |
| \(U_\star\), \(\rho_b\), PCRH\(_b\) | `synthesis/m1g-unified-pure-window.md` |
| Load M2 / Claim D | `synthesis/m2-t1-load.md` |
| M5b smooth action | `synthesis/m5b-smooth-action-limit.md` |
| M5c PM / Layer W | `synthesis/m5c-warmup-pm-gradient-flow.md` |
| M10 P1 non-identity | `synthesis/m10-p1-object-comparison.md` · `simulations/bridging/m10_p1_results.txt` |
| M6 plug-test | `synthesis/m6-weak-field-plugtest.md` |
| M6b next-order | `synthesis/m6b-next-order-weak-field.md` |
| Joint toys / envelopes | `simulations/bridging/` |

---

*Draft prose only — no new theorems. Update when \(U_\star\), PCRH\(_b\), or M6 status changes.*
