# 7. Newton recovery --- Path J/M only

### 4.1 Honesty preamble

Newtonian gravity is recovered as a **calibrated low-load regime** of the master-equation framework (**C9**), **not** by taking the Laplacian of a pointwise identification $\Phi\propto\rho_m$.

| Claim piece | Status / rigor |
|-------------|----------------|
| Master equation + load definitions | Canonical (Part 3) |
| Clausius on $\mathcal{L}_g$ $\Rightarrow$ Einstein (Jacobson 1995) | **External theorem + modeling assumption** |
| Einstein weak field $\Rightarrow$ $\nabla^2\Phi=4\pi G\rho_m$ | Standard GR |
| Matching $\alpha\beta=4\pi G/c^4$ so load clock agrees with Newtonian $\Phi$ **on shell** | **Calibration** (Path M; **C10**) |
| Pointwise $\Phi\propto\rho_m\Rightarrow\nabla^2\Phi\propto\nabla^2\rho_m\Rightarrow$ Poisson | **Invalid / withdrawn** |

**What is not claimed.** We do not derive Newton independently of Jacobson/Einstein input. We do not claim free derivation of Newton's constant $G$ from load bookkeeping alone. We do not claim that $\gamma=\delta=0$ is proved---only that those contributions are modeled as subdominant in the leading weak-field regime.

Canonical recovery is Path J/M as stated in this section; the historical pointwise Laplacian route is withdrawn (Section 4.5).

### 4.2 Setup: low-load, weak-field, slow-motion assumptions

Under the master equation and load of Part 3, the Newtonian analysis uses:

| # | Assumption |
|---|------------|
| L1 | $\alpha L\ll 1$ |
| L2 | Curvature small; $v\ll c$ |
| L3 | Entropy-production and holographic terms **subdominant**: $\gamma,\delta$ contributions $\ll$ energy-density term (modeling assumption; not quantified) |
| L4 | $\mathcal{L}_g$ obeys $\delta Q=T\,dS_c$ on every local Rindler horizon (Jacobson consistency) |

Under L1--L3,


$$
L
\approx
\beta\frac{E[\rho]}{V\epsilon_0}
\approx
\beta\frac{\rho_m c^2}{\epsilon_0},
$$


where $\rho_m$ is classical mass density ($T_{00}\approx\rho_m c^2$).

### 4.3 Path J --- Clausius → Einstein → Poisson

Path J is the **derivation path for the Poisson equation**.

**Step J1 --- Thermodynamic consistency of the generator.**  
By L4, heat flux and computational-entropy change on local horizons satisfy $\delta Q=T\,dS_c$.

**Step J2 --- Jacobson's theorem (imported).**  
Jacobson (1995): the Clausius relation on local Rindler horizons, with entropy proportional to horizon area and Unruh temperature, implies the **Einstein field equations** as an equation of state of the underlying thermodynamics (up to a cosmological constant fixed by the vacuum). In this framework we **import** that theorem as the continuum content of L4. We do **not** re-prove Jacobson here. Rigor: **external theorem + modeling assumption**.

**Step J3 --- Weak-field GR → Poisson.**  
Linearize Einstein about Minkowski with a static, non-relativistic perfect fluid. Standard textbook result:


$$
\nabla^2\Phi = 4\pi G\,\rho_m,
\qquad
g_{00} \approx -\bigl(1+2\Phi/c^2\bigr),
\quad
\sqrt{-g_{00}}\approx 1+\Phi/c^2.
$$


**Conclusion of Path J.** Newtonian Poisson is available as the weak-field limit of the Einstein thermodynamics already built into $\mathcal{L}_g$ under L4. No Laplacian of $\rho_m$ is required. The nonlocal structure of $\Phi$ (inverse-square forces from compact sources) is inherited from GR, not invented by load algebra.

### 4.4 Path M --- Load-clock calibration (matching, not derivation)

Path J yields a metric with Newtonian potential $\Phi[\rho_m]$. Path M fixes how the **load reparameterization** tracks the same $\Phi$. Rigor: **calibration**, conditional on Path J (**C10**).

**Step M1 --- Proper-time expansion.** For $\alpha L\ll 1$,


$$
d\tau
=
\frac{dt}{1+\alpha L}
\approx
dt\bigl(1-\alpha L\bigr)
\approx
dt\Bigl(1-\alpha\beta\frac{\rho_m c^2}{\epsilon_0}\Bigr).
$$


**Step M2 --- Static weak-field clock.** For a static observer,


$$
\frac{d\tau}{dt}
=
\sqrt{-g_{00}}
\approx
1+\frac{\Phi}{c^2}.
$$


**Step M3 --- On-shell matching (not pointwise $\Phi\propto\rho_m$).**  
Do **not** identify $\Phi/c^2=-\alpha\beta\rho_m c^2/\epsilon_0$ as a **local algebraic law**. That identification would give $\Phi\propto\rho_m$ pointwise, which is not Newtonian gravity.

Instead: for solutions of Poisson with the same $\rho_m$, require the **leading linear response** of the load clock to agree with the Newtonian redshift **on shell**.

*Worked example (uniform ball).* For constant density $\rho_m$ in a ball of radius $R$, the interior potential is


$$
\Phi_{\mathrm{in}}(r)
=
-2\pi G\rho_m\Bigl(R^2-\frac{r^2}{3}\Bigr)
\quad(r\le R).
$$


At the center, $\Phi_{\mathrm{in}}(0)/c^2=-2\pi G\rho_m R^2/c^2$. The load expansion at the center gives $d\tau/dt-1\approx-\alpha\beta\rho_m c^2/\epsilon_0$. Matching order of magnitude for a characteristic scale $R\sim R_\star$ (or equating coefficients after fixing a reference geometry where $\Phi$ is proportional to $\rho_m R^2$) calibrates $\alpha\beta$ relative to $\epsilon_0$. The **standard product used in this program**


$$
\alpha\beta = \frac{4\pi G}{c^4}
$$


is the convention that absorbs $\epsilon_0$ and geometric scale into the definitions of $\beta$ and $\epsilon_0$ so that $\alpha\cdot\beta\cdot c^2/\epsilon_0$ reproduces $\lvert\Phi\rvert/c^2$ **for the calibrated family of solutions**, not for arbitrary pointwise $\rho_m$.

**Honest reading of $\alpha\beta=4\pi G/c^4$:** it is a **matching condition** between load bookkeeping and Newtonian $\Phi$, **conditional on Path J already supplying Poisson**. It is **not** a free derivation of $G$ from first principles independent of Newton/GR (**C10**).

**Step M4 --- What the load clock then means.** With Path J + M: geometry / $\Phi$ is fixed by Einstein thermodynamics (Jacobson) + weak field; $L\approx\beta\rho_m c^2/\epsilon_0$ raises demand where energy density is high; 

$$
d\tau=dt/(1+\alpha L)
$$

 **tracks** the same slowing of clocks that GR encodes in $g_{00}$, once $\alpha\beta$ is calibrated; Newtonian force $\mathbf{F}=-m\nabla\Phi$ remains the effective description for slow massive probes---no extra force postulate beyond Path J's Einstein/Poisson content.

### 4.5 Withdrawn path (do not revive)

The following chain is **not** a valid recovery of Newtonian gravity (historical drafts; documented in M8; **withdrawn**):

1. Postulate $d\tau/dt=1/(1+\alpha L)$ with $L=\beta\rho_m c^2/\epsilon_0$.  
2. Set $d\tau/dt=1+\Phi/c^2$.  
3. Conclude $\Phi=-\alpha\beta c^4\rho_m/\epsilon_0$ **pointwise**.  
4. Take $\nabla^2$ and "match" to $4\pi G\rho_m$.

**Why it fails.** Newtonian $\Phi$ is **nonlocal** ($\Phi=-G\int\rho_m/|x-x'|\,dV'$). Pointwise $\Phi\propto\rho_m$ does not produce inverse-square forces from compact sources. Algebraically,


$$
\nabla^2\Phi
=
-\,\alpha\beta\frac{c^4}{\epsilon_0}\,\nabla^2\rho_m
$$


is **not** Poisson unless $\nabla^2\rho_m\propto-\rho_m$.

> **Disallowed one-liner:** "Taking the Laplacian of $\Phi\propto\rho$ yields $\nabla^2\Phi=4\pi G\rho$."

> **Allowed one-liner:** In the low-load regime the energy-density term dominates $L$. With $\mathcal{L}_g$ constrained by the Clausius relation, the Einstein equation (Jacobson) and its weak-field Poisson limit are available; matching the load-induced proper-time factor to the Newtonian potential fixes $\alpha\beta=4\pi G/c^4$. Newtonian gravity is thus a **calibrated low-load regime** of the framework.

### 4.6 Recovery chain (allowed language)

```text
Clausius on L_g  --(Jacobson)--->  Einstein equation
                                      |
                                      v
                              weak field / slow motion
                                      |
                                      v
                              ∇²Φ = 4πG ρ_m     (Path J)
                                      |
                                      v
                    match load clock dτ/dt ≈ 1+Φ/c²
                    on shell  ⇒  αβ = 4πG/c⁴     (Path M)
```

**Role of coefficients at leading Newton.** $\epsilon_0$ is reference energy density making $L$ dimensionless (absorbed into $\beta$ bookkeeping under Path M). The product $\alpha\beta$ (with $\epsilon_0$) is fixed by Path M. Weights $\gamma$ and $\delta$ are **dropped** at leading Newton under L3; they re-enter next-order / nonequilibrium / near-horizon regimes and must not be silently equated with GfE extras $D_{\mu\nu},\Lambda_G$ (that identification is a **structural FAIL** at next order---Part 6 / M6b; not claimed here).

### 4.7 Other recoveries --- status only (deferred)

Black-hole horizons, cosmological expansion (including inflation narratives), Lloyd-type ultimate computational capacity, and unified accounts of gravitational and kinematic time dilation appear in historical and outline form under Appendix A and legacy Appendix A drafts. Those regimes are **not** presented here as settled at Path J/M rigor. High-load / horizon physics elevates the boundary term $\delta$; cosmology elevates boundary growth and expansion bookkeeping; capacity bounds touch Lloyd-type limits. Each requires the same honesty pass as Newton: explicit assumptions, external theorems labeled as such, calibration distinguished from free derivation, and no revival of withdrawn algebraic shortcuts. Until that pass is complete, the program's **settled** gravitational recovery claim remains **Path J/M Newtonian Poisson only** (**C9**, **C10**). Cross-framework weak-field contact with continuum GfE (shared Poisson via GR, **not** framework identity) is deferred to Part 6 (M6 WEAK PASS / FAIL).

---

## Claim inventory for Parts 3--4

| ID | Statement used | Where | Rigor |
|----|----------------|-------|-------|
| **C9** | Newton recovery = Path J/M only (Clausius → Einstein → Poisson; load-clock on-shell match) | §4 | Path J: external thm + assumption; Path M: calibration |
| **C10** | $\alpha\beta=4\pi G/c^4$ is on-shell calibration, not free derivation of $G$ | §3.3 preview; §4.4 | **calibration** |
| **C14** | Prefer $L$ as demand from scale/rate of channel outcomes (energy + entropy flux + boundary); active scrambling → higher $L$ | §3.2 | **semantic** (program convention) |

**Structural (not claim-ID frozen as C-number):** three-term continuum $L$ **roles** align with discrete $L_E,L_S,L_B$ (M11c)---**not** continuum equality.

**Explicit non-claims touched:** ME $\Leftrightarrow$ GfE; $L\equiv G$; free derivation of $G$; Newton from pointwise $\Phi\propto\rho$ Laplacian (**withdrawn**); IDEM/decay fully constructs continuum $L$ or $G$; other recoveries settled at Path J/M rigor.

---

## Sources (Parts 3--4)

| Role | Path |
|------|------|
| Outline Parts 3--4 | Appendix A |
| Canonical $\Phi_g$, $L$, master eq | Eq.\ (\ref{eq:load}) family below |
| Canonical Path J/M | Appendix A |
| M8 audit (withdrawn path) | Appendix A |
| Claims freeze C9--C10, C14 | Section 3 and Appendix B |
| Three-role structural motivation | Appendix A |
| Claim gate | Section 3 and Appendix B |

---

*External theorem (Path J): Jacobson (1995); see Bibliography.*

---
