# Newtonian / Weak-Field Recovery (Path J/M)

**Status:** Canonical recovery note (rewritten 2026-07-14)  
**Correction (2026-07-31 per C17):** Path M restated. The former calibration \(\alpha\beta=4\pi G/c^4\) is dimensionally invalid and withdrawn; the surviving statement is \(\alpha L=-\Phi/c^2\) (`emergent-gravity/load-dimensional-analysis.md` Q1–Q3).  
**Canonical dynamics:** [master-equation.md](../../master-equation.md)  
**Audit of the old sketch:** [synthesis/m8-newton-recovery-audit.md](../../../synthesis/m8-newton-recovery-audit.md)  
**Narrative twin:** [quantum/Newton.md](../../../quantum/Newton.md)  
**Cross-framework plug-test:** [synthesis/m6-weak-field-plugtest.md](../../../synthesis/m6-weak-field-plugtest.md)

---

## 0. Honesty preamble

Newtonian gravity is recovered as a **calibrated low-load regime** of the master-equation framework, **not** by taking the Laplacian of a pointwise \(\Phi\propto\rho\) identification.

| Claim | Status |
|-------|--------|
| Master equation + load definitions | Canonical |
| Clausius on \(\mathcal{L}_g\) \(\Rightarrow\) Einstein (Jacobson 1995) | **External theorem + modeling assumption** |
| Einstein weak field \(\Rightarrow\) Poisson \(\nabla^2\Phi=4\pi G\rho\) | Standard GR |
| On-shell identification \(\alpha L=-\Phi/c^2\) so load clock agrees with Newtonian \(\Phi\) **on shell** (fixes the sum \(\alpha L\) only; former \(\alpha\beta=4\pi G/c^4\) withdrawn as dimensionally invalid, C17) | **Calibration** (Path M) |
| \(\Phi\propto\rho\) pointwise \(\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\Rightarrow\) Poisson | **Invalid** — removed |

---

## 1. Setup

Master equation and load (from canonical file):

\[
\frac{d\rho}{dt}
=
\frac{1}{1+\alpha L(\rho,g)}\,
\mathcal{L}_g\bigl[\rho;\, g_{\mu\nu}(\rho)\bigr],
\qquad
d\tau
=
\frac{dt}{1+\alpha L(\rho,g)},
\]

\[
L(\rho,g)
=
\beta\frac{E[\rho]}{V\epsilon_0}
+
\gamma\left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}}
+
\delta\frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)}.
\]

**Low-load, weak-field, slow-motion assumptions**

| # | Assumption |
|---|------------|
| L1 | \(\alpha L\ll 1\) |
| L2 | Curvature small; \(v\ll c\) |
| L3 | Entropy-production and holographic terms **subdominant**: \(\gamma,\delta\) contributions \(\ll\) energy-density term (modeling assumption; not quantified) |
| L4 | \(\mathcal{L}_g\) obeys \(\delta Q=T\,dS_c\) on every local Rindler horizon (Jacobson consistency) |

Under L1–L3:

\[
L
\approx
\beta\frac{E[\rho]}{V\epsilon_0}
\approx
\beta\frac{\rho_m c^2}{\epsilon_0},
\]

where \(\rho_m\) is classical mass density (\(T_{00}\approx\rho_m c^2\)).

---

## 2. Path J — Clausius → Einstein → Poisson (preferred)

This is the **derivation path for the Poisson equation**.

### Step J1 — Thermodynamic consistency of the generator

By L4, the channel generator \(\mathcal{L}_g\) is constrained so that heat flux and computational-entropy change on local horizons satisfy

\[
\delta Q = T\, dS_c.
\]

### Step J2 — Jacobson’s theorem

Jacobson (1995): the Clausius relation on local Rindler horizons, with entropy proportional to horizon area and Unruh temperature, implies the **Einstein field equations** as an equation of state of the underlying thermodynamics (up to a cosmological constant fixed by the vacuum).

In this framework: we **import** that theorem as the continuum content of L4. We do **not** re-prove Jacobson here.

### Step J3 — Weak-field GR → Poisson

Linearize Einstein about Minkowski with a static, non-relativistic perfect fluid. Standard textbook result:

\[
\nabla^2\Phi = 4\pi G\,\rho_m,
\qquad
g_{00} \approx -\bigl(1+2\Phi/c^2\bigr),
\quad
\sqrt{-g_{00}}\approx 1+\Phi/c^2.
\]

**Conclusion of Path J:** Newtonian Poisson is available as the weak-field limit of the Einstein thermodynamics already built into \(\mathcal{L}_g\). No Laplacian of \(\rho_m\) is required.

---

## 3. Path M — Load-clock calibration (matching, not derivation)

Path J yields a metric with Newtonian potential \(\Phi[\rho_m]\). Path M fixes how the **load reparameterization** tracks the same \(\Phi\).

### Step M1 — Proper-time expansion

\[
d\tau
=
\frac{dt}{1+\alpha L}
\approx
dt\bigl(1-\alpha L\bigr)
\approx
dt\Bigl(1-\alpha\beta\frac{\rho_m c^2}{\epsilon_0}\Bigr)
\quad(\alpha L\ll 1).
\]

### Step M2 — Static weak-field clock

For a static observer,

\[
\frac{d\tau}{dt}
=
\sqrt{-g_{00}}
\approx
1+\frac{\Phi}{c^2}.
\]

### Step M3 — On-shell matching (not pointwise \(\Phi\propto\rho_m\))

**Do not** identify \(\Phi/c^2 = -\alpha\beta\rho_m c^2/\epsilon_0\) as a **local algebraic law** (that would give \(\Phi\propto\rho_m\) pointwise, which is not Newtonian gravity).

Instead: for solutions of Poisson with the same \(\rho_m\), require the **leading linear response** of the load clock to agree with the Newtonian redshift **on shell**.

#### Worked example: uniform ball (constant \(\rho_m\), radius \(R\))

Interior potential (Newtonian):

\[
\Phi_{\mathrm{in}}(r)
=
-2\pi G\rho_m\Bigl(R^2-\frac{r^2}{3}\Bigr)
\quad(r\le R).
\]

At the center:

\[
\frac{\Phi_{\mathrm{in}}(0)}{c^2}
=
-\frac{2\pi G\rho_m R^2}{c^2}.
\]

Load expansion at the center (constant \(\rho_m\)):

\[
\frac{d\tau}{dt}-1
\approx
-\alpha\beta\frac{\rho_m c^2}{\epsilon_0}.
\]

Matching the **order of magnitude** for a characteristic scale \(R\sim R_\star\) (or equating coefficients after fixing a reference geometry where \(\Phi\) is proportional to \(\rho_m R^2\)) yields a calibration of the form

\[
\alpha\beta
\;\sim\;
\frac{2\pi G\,R_\star^2\,\epsilon_0}{c^4}
\]

for a **single-scale** match only: it depends on \(R_\star\), because the calibration is nonlocal (below). In general, equating the load expansion \(d\tau/dt-1\approx-\alpha L\) with Step M2 gives the **only** dimensionally valid calibration,

\[
\alpha L = -\frac{\Phi}{c^2}=\frac{GM}{rc^2}\qquad(\Phi<0,\ \alpha L>0),
\]

which is dimensionless on both sides and fixes the **sum** \(\alpha L\) on shell, not the individual coefficients. At the center of the ball it reads \(\alpha L(0)=2\pi G\rho_m R^2/c^2\), which depends on \(R\): the calibration is nonlocal and \(T_{\mu\nu}\)-sourced, so it is not reproduced pointwise by the local energy term \(\alpha\beta\rho_m c^2/\epsilon_0\) (`emergent-gravity/load-dimensional-analysis.md` Q3).

> *Corrected 2026-07-31 per C17:* earlier versions of this step stated a “repo-standard product” \(\alpha\beta=4\pi G/c^4\), obtained by absorbing \(\epsilon_0\) and geometric scale into \(\beta\). That relation is **dimensionally invalid**: \(\alpha\beta\) is dimensionless, but \(4\pi G/c^4\) has units \(\mathrm{s^2\,kg^{-1}\,m^{-1}}\) (Q1). It is withdrawn and replaced by \(\alpha L=-\Phi/c^2\) (Q2). Under that identification \(L\) is a **diagnostic** constrained to equal \(-\Phi/c^2\) on shell: it co-moves with the Path-J/M metric and is not a source of the geometry (Q3; C17).

**Honest reading of \(\alpha L=-\Phi/c^2\):** it is a **matching condition** between load bookkeeping and Newtonian \(\Phi\), **conditional on Path J already supplying Poisson**. It is **not** a free derivation of \(G\) from first principles independent of Newton/GR.

### Step M4 — What the load clock then means

With Path J + M:

- Geometry / \(\Phi\) is fixed by Einstein thermodynamics (Jacobson) + weak field.  
- Load \(L\approx\beta\rho_m c^2/\epsilon_0\) raises computational demand where energy density is high.  
- \(d\tau=dt/(1+\alpha L)\) **tracks** the same slowing of clocks that GR encodes in \(g_{00}\), once the on-shell identification \(\alpha L=-\Phi/c^2\) is imposed (a diagnostic co-moving with the metric, not a source of it; C17).  
- Newtonian force \(\mathbf{F}=-m\nabla\Phi\) remains the effective description for slow massive probes; no extra force postulate is needed **beyond** the Einstein/Poisson content of Path J.

---

## 4. Forbidden path (Path L — pure load phenomenology)

The following is **not** a valid recovery of Newtonian gravity:

1. Postulate \(d\tau/dt=1/(1+\alpha L)\) with \(L=\beta\rho_m c^2/\epsilon_0\).  
2. Set \(d\tau/dt=1+\Phi/c^2\).  
3. Conclude \(\Phi=-\alpha\beta c^4\rho_m/\epsilon_0\) **pointwise**.  
4. Take \(\nabla^2\) and “match” to \(4\pi G\rho_m\).

**Why it fails:** Newtonian \(\Phi\) is **nonlocal** (\(\Phi=-G\int\rho_m/|x-x'|\,dV'\)). Pointwise \(\Phi\propto\rho_m\) does not produce inverse-square forces from compact sources. Algebraically,

\[
\nabla^2\Phi
=
-\,\alpha\beta\frac{c^4}{\epsilon_0}\,\nabla^2\rho_m
\]

is **not** Poisson unless \(\nabla^2\rho_m\propto-\rho_m\).

---

## 5. Role of \(\epsilon_0\), \(\gamma\), \(\delta\)

| Symbol | Role in Newton recovery |
|--------|-------------------------|
| \(\epsilon_0\) | Reference (Planck) energy density making \(L\) dimensionless, so \(\beta\) is dimensionless (load-dimensional-analysis Q1) |
| \(\alpha,\beta\) | Not fixed separately: Path M fixes only the on-shell sum \(\alpha L=-\Phi/c^2\), not \(\alpha\beta\) or the split among the three terms (C17; load-dimensional-analysis Q2, Q4) |
| \(\gamma\) | Entropy-production weight — **dropped** at leading Newton (L3); re-enters next-order / nonequilibrium corrections |
| \(\delta\) | Holographic boundary weight — **dropped** at leading Newton (L3); relevant near horizons / cosmology |

Next-order comparison of \(\gamma,\delta\) to GfE extras: [synthesis/m6b-next-order-weak-field.md](../../../synthesis/m6b-next-order-weak-field.md).

---

## 6. Recovery chain (allowed language)

```text
Clausius on L_g  ──(Jacobson)──►  Einstein equation
                                      │
                                      ▼
                              weak field / slow motion
                                      │
                                      ▼
                              ∇²Φ = 4πG ρ_m     (Path J)
                                      │
                                      ▼
                    match load clock dτ/dt ≈ 1+Φ/c²
                    on shell  ⇒  αL = −Φ/c²      (Path M)
```

**Allowed one-liner:**

> In the low-load regime the energy-density term dominates \(L\). With \(\mathcal{L}_g\) constrained by the Clausius relation, the Einstein equation (Jacobson) and its weak-field Poisson limit are available; matching the load-induced proper-time factor to the Newtonian potential fixes \(\alpha L=-\Phi/c^2\) on shell (the sum \(\alpha L\), not \(\alpha\beta\) separately; C17). Newtonian gravity is thus a **calibrated low-load regime** of the framework.

**Disallowed one-liner:**

> Taking the Laplacian of \(\Phi\propto\rho\) yields \(\nabla^2\Phi=4\pi G\rho\).

---

## 7. Consistency with related recoveries

| Regime | Relation to this note |
|--------|------------------------|
| Moderate curvature | Path J already is Einstein-level; load reparam remains |
| Horizons / BH | Boundary term \(\delta\) and high \(L\) dominate; see black-holes recovery |
| Cosmology | Boundary growth / inflation notes; not pure Newton |
| GfE low coupling | Also ends at EH → Poisson via GR; shared end **≠** framework identity ([m6](../../../synthesis/m6-weak-field-plugtest.md)) |

---

## 8. Explicit non-claims

1. We do **not** derive Newton from load alone without Jacobson/Einstein input.  
2. We do **not** claim \(\alpha,\beta,\epsilon_0\) are predicted independently of \(G\).  
3. We do **not** claim \(\gamma=\delta=0\) is proved — only that they are subdominant under L3.  
4. We do **not** equate this recovery with Bianconi GfE (see M6/M7).  
5. The old Laplacian chain in prior Newton.md drafts is **withdrawn**.

---

## References

1. Jacobson, T. (1995). Thermodynamics of spacetime: The Einstein equation of state. *Phys. Rev. Lett.* **75**, 1260.  
2. [master-equation.md](../../master-equation.md) — canonical \(L\), \(d\tau\), \(\mathcal{L}_g\).  
3. [m8-newton-recovery-audit.md](../../../synthesis/m8-newton-recovery-audit.md) — algebraic gap documentation.  
4. Misner, Thorne, Wheeler — weak-field GR → Poisson (standard).

---

*Canonical Path J/M recovery. Update synthesis M8 when this file changes.*
