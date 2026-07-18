# 9. Continuum GfE contact --- M6 WEAK PASS / FAIL; M6b structural FAIL

### 6.1 Shared weak-field problem

Parts 3--4 recover Newtonian Poisson on **our** side (layer **M**) via **Path J/M** only (Clausius → Einstein → weak-field GR; load-clock on-shell calibration $\alpha\beta=4\pi G/c^4$). Continuum Bianconi GfE (layer **G**) is a **different** upper theory: relative entropy of metrics, low-coupling Einstein--Hilbert limit, and modified equations with $\Lambda_G$, $D_{\mu\nu}$, dressed $R^G$ away from strict low coupling. M6 asks only whether the two frameworks agree on a **shared weak-field problem**, not whether they are the same theory. Layers **W** / **D** dual success does not transfer automatically to **G** or **M**.

**Shared problem (static weak field).** Background Minkowski plus static Newtonian potential $\Phi\ll c^2$; classical mass density $\rho_m(\mathbf{x})$ (perfect fluid at rest, $T_{00}\approx\rho_m c^2$). Ask for the **leading** equation determining $\Phi$.

**Side A --- ours (Path J/M).** Assume $\mathcal{L}_g$ satisfies Clausius on local horizons so that the Einstein equation holds (Jacobson 1995 imported), or take Einstein as the thermodynamic fixed point of the channel generator. Weak-field GR yields $\nabla^2\Phi=4\pi G\rho_m$. Load $L\approx\beta_L\rho_m c^2/\epsilon_0$ calibrates the proper-time factor to the same $\Phi$ via on-shell matching $\alpha_L\beta_L=4\pi G/c^4$ (**Path M calibration**), not via the withdrawn pointwise Laplacian identity $\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho$.

**Side B --- Bianconi GfE (documented low coupling).** At low coupling the entropic action reduces to Einstein--Hilbert with zero cosmological constant (external paper claim). Standard GR weak-field linearization on that EH theory again yields $\nabla^2\Phi=4\pi G\rho_m$. Newton here is **via GR**, not via a load clock. Away from strict low coupling, modified equations involve $\Lambda_G(\tilde{\mathcal{G}})$, dressed $R^G$, and $D_{\mu\nu}$.

---

### 6.2 WEAK PASS at Poisson order (**C11**)

| Item | Ours (Path J/M) | GfE low coupling |
|------|-----------------|------------------|
| Leading PDE for $\Phi$ | $\nabla^2\Phi=4\pi G\rho_m$ | $\nabla^2\Phi=4\pi G\rho_m$ |
| Mechanism | Clausius/Einstein + load calibration | Relative-entropy action → EH → GR linearization |
| Extra fields at leading Newton | None if $\gamma_L,\delta_L$ dropped | None if $\tilde{\mathcal{G}}=\tilde I$, $\Lambda_G=0$ |

**Outcome:** **WEAK PASS** --- same leading Poisson equation. Equations agree at this order. The agreement is **real** and **expected** if both frameworks embed Einstein gravity at low demand. It is **supporting circumstantial evidence** that they sit in the same phenomenological class as GR --- **not** evidence that load dynamics equal Bianconi's relative-entropy Euler--Lagrange equations.

**Honesty limits.** WEAK PASS does **not** upgrade either theory to GR-level certainty. Path J still depends on Jacobson/Einstein input; Poisson is not free from GR. We did **not** solve Bianconi's field equations numerically.

---

### 6.3 FAIL of framework identity (**C12**)

| Criterion | Outcome |
|-----------|---------|
| Same leading Poisson $\nabla^2\Phi=4\pi G\rho_m$ | **WEAK PASS** |
| Same upper derivation mechanism | **FAIL** |
| Identifiable $(\alpha_L,\beta_L)=(\alpha_B,\beta_B)$ | **FAIL / refused** (M7) |
| Continuum GfE $\Leftrightarrow$ master equation | **FAIL** --- do not claim |

**Mechanisms differ.** Ours: Clausius constraint on a channel generator, Einstein as fixed point, load as scalar demand clock. GfE: relative entropy of metrics as primary action, low-coupling EH, then GR. Shared Poisson is shared **GR linearization**, not shared primary entropy object.

**Constant refusal.** Do **not** assert $\alpha_L\beta_L=\alpha_B/\beta_B$ (or $\alpha_L\beta_L\equiv\alpha_B/\beta_B$). The product $\alpha_L\beta_L$ is an **on-shell calibration** of our load clock to Newtonian redshift (Path M). The ratio $\alpha_B/\beta_B$ is a **coupling constant in Bianconi's field equations** (schematic $\kappa=\alpha_B/\beta_B$). Different roles; identification is refused without a new OPEN_MATH decision and an explicit continuum map. Also refuse $L\equiv G$ and $S_c\equiv\operatorname{Tr} g\ln G^{-1}$.

---

### 6.4 M6b: next-order structural FAIL (**C13**)

Leading Poisson does not discriminate mechanisms. Discrimination lives at **next order**.

**Our next-order candidates.** Full load


$$
L \;=\; \beta_L\frac{\rho_m c^2}{\epsilon_0} + \gamma_L\left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}} + \delta_L\frac{S_{\mathrm{boundary}}}{S_{\mathrm{BH}}},
$$


with clock expansion $d\tau/dt=1/(1+\alpha_L L)=1-\alpha_L L+\alpha_L^2 L^2-\cdots$. In a static weak field, $\gamma_L L_S$ vanishes in strict equilibrium and $\delta_L L_\partial$ is a screen term; nonlinear $\alpha_L^2 L_E^2$ is PPN-like bookkeeping only if carefully mapped. Crucially: under Path J the **metric** is primarily Einstein-sourced. Default reading of $\gamma_L,\delta_L$ is **additive scalar corrections to the clock**, not automatic modifications of $\nabla^2\Phi=4\pi G\rho_m$, unless a dynamical rule promotes $L_S,L_\partial$ into effective stress.

**GfE next-order candidates.** Schematic modified sector: $R^G_{(\mu\nu)}-\frac12 g_{\mu\nu}(R_G-2\Lambda_G)+D_{(\mu\nu)}=\kappa T_{(\mu\nu)}$ with $\Lambda_G\ge 0$ from the G-field functional and $D_{\mu\nu}$ from G-field derivatives. Linearized deformations of Poisson may involve Yukawa/scalar modes, effective $G_N$ renormalization, or emergent cosmological terms --- **structurally inside the metric field equations**.

**Primary structural conclusion.** Next-order extras **do not match as the same object class**:

| Ours (next order) | GfE (next order) | Label |
|-------------------|------------------|-------|
| $\gamma_L\|dS_c/d\tau\|$ in load **clock** | $D_{\mu\nu}$ in metric EOM | type mismatch unless a map is built |
| $\delta_L S_{\partial}/S_{\mathrm{BH}}$ screen ratio | not primary as holographic screen term in GfE action | does not map cleanly |
| load reparam only (no new Poisson source by default) | $\Lambda_G$, $D_{\mu\nu}$ **do** enter metric EOM | **structural divergence** |
| no intrinsic $\Lambda$ from load at low order | $\Lambda_G\ge 0$ from G-field alone | **structural divergence** |

**Outcome:** **structural FAIL** of next-order match (**C13**). Coefficient-level PPN / Yukawa comparison is **not established** (needs explicit Bianconi linearization). Do **not** assert $\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G$.

---

### 6.5 Interpretation: co-class via GR, not shared primary entropy

M6's honest reading is **co-class membership** with general relativity at low demand, not framework identity:

1. Both sides can recover $\nabla^2\Phi=4\pi G\rho_m$ because both (under stated assumptions) sit on the Einstein/GR weak-field track at leading order.
2. Upper mechanisms differ: channel + load clock versus relative entropy of metrics.
3. Next-order structures live in different slots: **clock factors** versus **metric EOM extras**.
4. Therefore Poisson agreement is **not** evidence that continuum load dynamics equal Bianconi EL equations, and **not** evidence that master equation $\Leftrightarrow$ continuum GfE.

**Where the interesting dual remains.** The constructive dual that is **settled enough** in this program is **ACD-EW on Layers W and D** (Part 5): shared Stage-2 $G[\phi]$, PM as reconstructor, residual dual T1′ / $U_\star$, load as mild time change. That dual is a **different mathematical layer** from M6's Lorentzian weak-field plug-test. Euclidean residual dual does **not** lift automatically to Poisson agreement; Poisson agreement does **not** lift residual dual to continuum gravity. Stage-1 / Stage-2 / Stage-3 of the program mental model must not be collapsed into symbolic identity of master equation and GfE action.

**Non-claims (M6 block).** No numerical solution of Bianconi field equations; no derivation of $\alpha_L\beta_L$ from $\alpha_B,\beta_B$; no master equation $\Leftrightarrow$ GfE; no next-order $\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G$; WEAK PASS does not confer GR-level certainty; Path J still imports Jacobson/Einstein.

---

### 6.6 Claim inventory for Part 6

| ID | One-line | Rigor |
|----|----------|-------|
| **C11** | M6: both frameworks → $\nabla^2\Phi=4\pi G\rho_m$ via Einstein/GR at leading weak field | **WEAK PASS** |
| **C12** | M6: not framework equivalence; mechanisms diverge; refuse $(\alpha_L,\beta_L)=(\alpha_B,\beta_B)$ | **FAIL identity** |
| **C13** | M6b: GfE extras in metric EOM; $\gamma_L,\delta_L$ in load clock unless promoted | **structural FAIL** |

---

## Sources (Parts 5--6)

| Role | Path |
|------|------|
| Claims freeze C1--C8, C11--C13 | Section 3 and Appendix B |
| Claim gate / layers W D G M | Section 3 and Appendix B |
| ACD-EW formal dual | Appendix A |
| T1′ claims A--D | Appendix A |
| $U_\star$, $\rho_b$, PCRH$_b$ | Appendix A |
| Load M2 / Claim D | Appendix A |
| M5b smooth action | Appendix A.5 |
| M5c PM / Layer W | Appendix A.4 |
| M10 P1 non-identity | Appendix A.6 |
| M6 plug-test | Appendix A |
| M6b next-order | Appendix A |
| Joint toys / envelopes | Appendix A.8 |
| R4a promotion no-go | Appendix A.7 |
| Program conclusions spine | Section 3 and Appendix B |

---
