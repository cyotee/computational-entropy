**Recovery of Newtonian Gravity (Weak-Field / Low-Load Limit)**  
**Path J/M rewrite (2026-07-14)** — replaces the invalid \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\) chain.

Canonical recovery note: [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md)  
Master equation: [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)  
Audit: [synthesis/m8-newton-recovery-audit.md](../synthesis/m8-newton-recovery-audit.md)

---

### Stance

Newtonian gravity emerges as the **low-load, weak-field, non-relativistic regime** of the master equation **together with** the thermodynamic (Clausius) constraint on the channel generator. The Poisson equation \(\nabla^2\Phi=4\pi G\rho\) is **not** obtained by taking the Laplacian of a pointwise identification \(\Phi\propto\rho\). It comes from the Einstein equation of state (Jacobson) linearized about Minkowski; the load factor then **calibrates** proper-time bookkeeping to the same \(\Phi\).

---

### Master equation and load

$$
\frac{d\rho}{dt}
=
\frac{1}{1+\alpha L(\rho,g)}\,
\mathcal{L}_g\bigl[\rho;\, g_{\mu\nu}(\rho)\bigr],
\qquad
d\tau
=
\frac{dt}{1+\alpha L(\rho,g)}.
$$

$$
L(\rho,g)
=
\beta\frac{E[\rho]}{V\epsilon_0}
+
\gamma\left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}}
+
\delta\frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)}.
$$

**Low-load assumptions:** \(\alpha L\ll 1\); slow motion; curvature small; entropy-production and holographic terms **subdominant** relative to the energy-density term. Then

$$
L
\approx
\beta\frac{E[\rho]}{V\epsilon_0}
\approx
\beta\frac{\rho_m c^2}{\epsilon_0},
$$

with \(\rho_m\) the classical mass density.

---

### Path J — Poisson from Clausius / Einstein (derivation of \(\nabla^2\Phi\))

1. **Clausius constraint.** \(\mathcal{L}_g\) is required to satisfy \(\delta Q=T\,dS_c\) on every local Rindler horizon (Jacobson 1995 consistency condition in the canonical master-equation file).

2. **Jacobson’s theorem.** That thermodynamic condition implies the **Einstein field equations** as an equation of state (external theorem; imported, not re-proved here).

3. **Weak-field GR.** Linearizing Einstein about Minkowski for a static, non-relativistic perfect fluid yields the Newtonian Poisson equation and metric bookkeeping:
   $$
   \nabla^2\Phi = 4\pi G\,\rho_m,
   \qquad
   \sqrt{-g_{00}}\approx 1+\frac{\Phi}{c^2}.
   $$

No step of the form \(\nabla^2(\text{const}\cdot\rho_m)\) is used.

---

### Path M — Load clock calibration (matching, not derivation of Poisson)

With Path J already supplying a Newtonian \(\Phi[\rho_m]\), expand the load reparameterization:

$$
d\tau
\approx
dt\Bigl(1-\alpha\beta\frac{\rho_m c^2}{\epsilon_0}\Bigr)
\quad(\alpha L\ll 1).
$$

Static observers also have \(d\tau/dt=\sqrt{-g_{00}}\approx 1+\Phi/c^2\).

**On-shell matching:** require the load clock to track the Newtonian redshift **for the same \(\rho_m\) solutions** of Poisson (e.g. constant-density ball interior, where \(\Phi\) is quadratic and proportional to \(\rho_m R^2\)). This fixes the product used throughout the project,

$$
\alpha\beta = \frac{4\pi G}{c^4},
$$

as a **calibration** between load bookkeeping \((\alpha,\beta,\epsilon_0)\) and Newtonian \(G\), **conditional on** Path J. It does **not** mean \(\Phi=-\alpha\beta c^4\rho_m/\epsilon_0\) holds as a local algebraic law at every point.

---

### What is withdrawn

The previous draft wrote

$$
\frac{\Phi}{c^2}\approx -\alpha\beta\frac{\rho_m c^2}{\epsilon_0}
\quad\Rightarrow\quad
\nabla^2\Phi = -\alpha\beta c^4\nabla^2\rho_m
\quad\text{“matched to”}\quad
\nabla^2\Phi=4\pi G\rho_m.
$$

That intermediate Laplacian step is **algebraically invalid** unless \(\nabla^2\rho_m\propto-\rho_m\). Pointwise \(\Phi\propto\rho_m\) is also **physically wrong** as Newtonian gravity (which is nonlocal). See [m8 audit](../synthesis/m8-newton-recovery-audit.md) gap N1.

---

### Physical interpretation

In the low-load regime:

- Computational demand is dominated by local energy density.  
- Higher \(\rho_m\) raises \(L\), which slows proper time via \(1/(1+\alpha L)\).  
- That slowing is calibrated (Path M) to the same \(\Phi\) that Einstein thermodynamics produces (Path J).  
- The Newtonian force \(\mathbf{F}=-m\nabla\Phi\) is the effective description for slow massive probes; no separate force law is postulated **beyond** the Einstein/Poisson content of Path J.

---

### Consistency with related approaches

- **Jacobson (1995):** Einstein as equation of state from Clausius — **this is Path J**, not an optional analogy.  
- **Verlinde (2010):** entropic-force narrative remains heuristic; our energy-density term in \(L\) is a computational analogue of information demand, not a second derivation of Poisson.  
- **Bianconi GfE:** low coupling \(\to\) EH \(\to\) same Poisson via GR; shared Newtonian end is a **WEAK PASS** only — not framework equivalence ([m6](../synthesis/m6-weak-field-plugtest.md)).

---

### Summary chain (allowed)

1. Dominant load \(L\approx\beta\rho_m c^2/\epsilon_0\).  
2. Clausius on \(\mathcal{L}_g\) \(\Rightarrow\) Einstein (Jacobson).  
3. Weak field \(\Rightarrow\) \(\nabla^2\Phi=4\pi G\rho_m\).  
4. Match load clock to \(1+\Phi/c^2\) on shell \(\Rightarrow\) \(\alpha\beta=4\pi G/c^4\).

Newtonian gravity is a **calibrated low-load regime** of the same computational framework that targets other gravitational phenomena — with Poisson inherited from Einstein thermodynamics, not from an invalid Laplacian of \(\rho_m\).
