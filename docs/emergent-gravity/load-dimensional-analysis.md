# Load constants — dimensional analysis and a consistency no-go

**Status:** Canonical analysis (2026-07-31) · Preliminary research · executes [../papers/PRD_load_constants_rebuild.md](../papers/PRD_load_constants_rebuild.md)
**Governs:** the constants \(\alpha,\beta,\gamma,\delta,\epsilon_0\) of [master-equation.md](master-equation.md)
**Depends on:** Stage-1 decoupling witness ([../papers/REGIME_PROGRAM_dSc_decoupling.md](../papers/REGIME_PROGRAM_dSc_decoupling.md)) · Newton Path J/M ([recoveries/newtonian/README.md](recoveries/newtonian/README.md))

This note rebuilds the load constants on a dimensionally-consistent footing (PRD Q1–Q5). The result is a **precise no-go** (PRD D-7): the load cannot both be the gravitational clock *and* contain an independent entropy-production term. This puts the reformulation verdict on firm structural ground and dissolves the Stage-2 "unfixed \(\alpha\gamma\)" worry.

---

## Q1 — Dimensional audit

Load and clock:


$$
L=\beta\frac{E}{V\epsilon_0}+\gamma\Big|\frac{dS_c}{d\tau}\Big|+\delta\frac{S_{\rm boundary}}{S_{\rm BH}},\qquad
d\tau=\frac{dt}{1+\alpha L}.
$$


\(L\) is dimensionless (type safety); \(d\tau,dt\) are times, so \(\alpha L\) is dimensionless \(\Rightarrow\alpha\) dimensionless.

| Quantity | Units | Consequence |
|----------|-------|-------------|
| \(E=\operatorname{Tr}(\rho H)\) | J | — |
| \(V\) | m³ | — |
| \(\epsilon_0\) (Planck energy density) | J·m⁻³ | \(E/(V\epsilon_0)=\rho_E/\rho_{\rm Pl}\) **dimensionless** ⇒ \(\beta\) dimensionless |
| \(S_c=-\operatorname{Tr}\rho\log_2\rho\) | dimensionless (bits) | — |
| \(dS_c/d\tau\) | s⁻¹ | \(\gamma\,\lvert dS_c/d\tau\rvert\) dimensionless ⇒ **\(\gamma\) has units of TIME** |
| \(S_{\rm boundary}/S_{\rm BH}\) | dimensionless | \(\delta\) dimensionless |

**Observable combinations.** Only \(\alpha L\) enters the physics, so the physically meaningful constants are


$$
\underbrace{\alpha\beta}_{\text{dimensionless}},\qquad \underbrace{\alpha\gamma}_{\text{time}},\qquad \underbrace{\alpha\delta}_{\text{dimensionless}}.
$$


Individual \(\alpha,\beta,\gamma,\delta\) are **not** separately observable.

**The stated calibration is invalid.** \(\alpha\beta\) is dimensionless, but \(4\pi G/c^4\) has units \(\mathrm{s^2\,kg^{-1}\,m^{-1}}\). So \(\alpha\beta=4\pi G/c^4\) **cannot hold** — confirming the Stage-2 finding.

---

## Q2 — The dimensionally-correct calibration

Physical proper time is set by the metric: for a static weak field \(g_{00}=-(1+2\Phi/c^2)\),


$$
d\tau=\sqrt{-g_{00}}\,dt=\Big(1+\frac{\Phi}{c^2}\Big)dt.
$$


Equating with \(d\tau=dt/(1+\alpha L)\) gives the **only** dimensionally valid calibration:


$$
\boxed{\;\alpha L = -\frac{\Phi}{c^2}=\frac{GM}{rc^2}\;}\qquad(\Phi<0,\ \alpha L>0).
$$


This is dimensionless on both sides (✓) and fixes the **sum** \(\alpha L\), not the individual coefficients. It replaces the garbled \(\alpha\beta=4\pi G/c^4\), which conflated a local-density coefficient with Newton's (dimensionful) constant.

---

## Q3 — Locality/consistency: the no-go

Two facts collide.

1. **The calibration is nonlocal and \(T_{\mu\nu}\)-sourced.** \(\Phi\) solves \(\nabla^2\Phi=4\pi G\rho\) (Path J/M: Clausius→Einstein→Poisson), an integral over the mass distribution. So \(\alpha L=-\Phi/c^2\) is fixed by \(T_{\mu\nu}\) and is **nonlocal**. When \(T_{\mu\nu}\) is held fixed, \(\Phi\) is fixed, hence \(\alpha L\) is fixed.

2. **The load's entropy term varies at fixed \(T_{\mu\nu}\).** Stage 1 (`regime_decoupling_witness.py`) showed pure dephasing makes \(\lvert dS_c/d\tau\rvert>0\) at **constant energy and no heat flux** — i.e. at fixed \(T_{\mu\nu}\). So the term \(\alpha\gamma\lvert dS_c/d\tau\rvert\) **changes** while \(T_{\mu\nu}\) is fixed.

These are contradictory: (1) says \(\alpha L\) is fixed when \(T_{\mu\nu}\) is fixed; (2) says a summand of \(\alpha L\) changes when \(T_{\mu\nu}\) is fixed. Therefore:

> **No-go.** The load \(L\) cannot simultaneously (a) clock the gravitational proper time (\(\alpha L=-\Phi/c^2\)) and (b) contain an entropy-production term with an independent effect. Consistency **forces the entropy-production term to make no independent contribution to proper time**.

Equivalently: proper time at a point is single-valued and set by the metric. If \(d\tau=dt/(1+\alpha L)\) is to *be* that proper time, then \(L\) is a **diagnostic** constrained to equal \(-\Phi/c^2\) on-shell — it does not *generate* a second, dephasing-dependent clock. The local energy term \(\rho_E/\rho_{\rm Pl}\) likewise cannot *generate* the nonlocal \(\Phi\) (this is the already-**withdrawn** pointwise \(\Phi\propto\rho\) identity, N5); Newton is recovered only via Path J/M, and the load co-moves with that metric.

---

## Q4 — \(\gamma\) (moot under the no-go, but stated)

Dimensionally \(\gamma\) is a time. The framework's own regularization uses the Margolus–Levitin window \(\tau_{\rm ML}=\pi\hbar/2E\), so the natural choice is \(\gamma\sim\hbar/E\) (system-dependent, not universal). But **\(\alpha\) is not independently fixed**: the calibration constrains only the nonlocal sum \(\alpha L=-\Phi/c^2\), never the local split among the three terms. Hence \(\alpha\gamma\) is not determined by the theory — and, by Q3, this does not matter: under the only consistent reading the entropy term carries no independent clock effect, so \(\alpha\gamma\) is not a physical observable at all.

---

## Q5 — Observability (feeds the regime program)

Under the consistent (diagnostic) reading, changing the dephasing rate at fixed \(T_{\mu\nu}\) leaves the metric — hence the physical proper time — **unchanged**. So there is **no independent dephasing clock effect** to measure. The Stage-1 "departure in principle" was contingent on treating \(L\) as an independent generator with free constants; the dimensional/locality analysis shows \(L\) **cannot** be that generator while recovering gravity. 

This **sharpens** the Stage-2 verdict from "reformulation in practice (magnitude unknown)" to:

> **Reformulation structurally.** The entropy-production term does not produce a gravity-consistent independent clock effect. \(\alpha\gamma\) is not an open physical parameter; it was an artifact of an inconsistent (generator) reading.

*(Exotic escape, noted and closed: if one posits a second "computational proper time" distinct from the metric's, it is not gravity, would imply two clock rates at a point — not observed — and needs independent justification. Not pursued.)*

---

## Result & rigor

| Statement | Rigor |
|-----------|-------|
| \(\gamma\) has units of time; observables are \(\alpha\beta,\alpha\gamma,\alpha\delta\) (Q1) | **proved** (dimensional) |
| \(\alpha\beta=4\pi G/c^4\) is dimensionally invalid; correct form \(\alpha L=-\Phi/c^2\) (Q2) | **proved** |
| Load cannot be both the gravitational clock and an independent entropy clock (Q3) | **no-go** (uses Stage-1 fixed-\(T_{\mu\nu}\) fact) |
| \(\alpha\gamma\) undetermined and non-observable under the consistent reading (Q4–Q5) | **structural** |
| Verdict: reformulation **structurally** (not merely in practice) | conclusion |

**What this fixes.** The Stage-2 blocker ("theory doesn't fix \(\alpha\gamma\)") is resolved: \(\alpha\gamma\) is not a physical observable because the load is a diagnostic co-moving with the Path-J/M metric, not an independent clock. The regime program's experimental track is therefore closed on structural grounds, not left pending a calibration.

**What this does not do.** It does not repair the master equation into a *generator* of gravity — that route is a no-go for a local load term (nonlocal \(\Phi\)). Making the load generate gravity would require **promoting** load terms into the field equations (the R4a theme), i.e. a different theory; not undertaken here.

**Non-claims (stand):** no departure from GR is asserted; \(S_c\) production is real but gravitationally inert under the consistent reading; \(\sigma(x)\) (Paper C) remains a classical density; \(L\neq G\); N5 (no pointwise Newton) upheld.

---

*Update [master-equation.md](master-equation.md) constants section, [../papers/REGIME_PROGRAM_dSc_decoupling.md](../papers/REGIME_PROGRAM_dSc_decoupling.md), [../papers/FALSIFIABILITY_L_vs_GR.md](../papers/FALSIFIABILITY_L_vs_GR.md), and the ledgers to point here.*
