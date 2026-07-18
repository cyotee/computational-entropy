# M8 — Internal Newton / Poisson Recovery Audit

**M-id:** M8  
**Status:** **Audit complete — gap N1 documented; Path J/M rewrite landed in canonical recovery + Newton.md**  
**Sources audited:** [quantum/Newton.md](../quantum/Newton.md) · [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)  
**Canonical rewrite:** [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md)  
**Downstream:** feeds M7/M6 ([weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md)) · next-order [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md)  
**Date:** 2026-07-14

---

## 1. What the recovery claims

From Newton.md:

1. Low load: \(L\approx\beta\rho c^2/\epsilon_0\).  
2. \(d\tau\approx dt\,(1-\alpha\beta\rho c^2/\epsilon_0)\) for \(\alpha L\ll 1\).  
3. Identify with \(\sqrt{-g_{00}}\approx 1+\Phi/c^2\).  
4. Obtain \(\Phi/c^2\approx -\alpha\beta\rho c^2/\epsilon_0\).  
5. “Laplacian + matching” \(\Rightarrow\nabla^2\Phi=4\pi G\rho\) with \(\alpha\beta=4\pi G/c^4\).

---

## 2. Algebraic gap (blocking as written)

From step 4 as a **pointwise** identification

\[
\Phi(x) \;=\; -\,\alpha\beta\frac{c^4}{\epsilon_0}\,\rho(x),
\]

one gets

\[
\nabla^2\Phi \;=\; -\,\alpha\beta\frac{c^4}{\epsilon_0}\,\nabla^2\rho,
\]

which is **not** Poisson \(\nabla^2\Phi=4\pi G\rho\) unless \(\rho\) satisfies a contrived PDE \(\nabla^2\rho\propto -\rho\).

Newton.md writes:

\[
\nabla^2\Phi = -\alpha\beta c^4\nabla^2\rho
\quad\text{then matches to}\quad
\nabla^2\Phi=4\pi G\rho,
\]

which **does not follow** without replacing \(\nabla^2\rho\) by something \(\propto\rho\) (unstated).  

**Status of intermediate Laplacian step:** **gap / incorrect as written.**

---

## 3. What still holds

| Piece | Status |
|-------|--------|
| Master equation + load definitions | Canonical, consistent |
| Low-load dominance of energy-density term | Modeling assumption, clear |
| First-order expansion \(d\tau/dt\approx 1-\alpha L\) | Elementary |
| Heuristic: higher \(\rho\) ⇒ higher \(L\) ⇒ slower clocks ⇒ gravitational redshift / \(\Phi\) | Semantic / physical story |
| Calibration \(\alpha\beta=4\pi G/c^4\) as **matching to Newton** once a valid map \(\Phi[\rho]\) exists | Legitimate if chain is fixed |
| Consistency with Jacobson weak-field Poisson **if** \(\mathcal{L}_g\) already encodes Einstein thermodynamics | Separate route (see §4) |

---

## 4. Corrected interpretation paths (candidates)

Do **not** claim any is fully proved in-repo; mark preferred path for M6.

### Path J — Jacobson / Clausius route (preferred for consistency with master-equation text)

1. \(\mathcal{L}_g\) obeys \(\delta Q=T\,dS_c\) on local Rindler horizons (assumed in canonical master equation).  
2. Jacobson (1995): that condition \(\Rightarrow\) Einstein equation as equation of state.  
3. Weak-field, slow-motion limit of Einstein \(\Rightarrow\) Poisson \(\nabla^2\Phi=4\pi G\rho\).  
4. Load factor \(1/(1+\alpha L)\) supplies **additional** time-dilation bookkeeping; matching \(\alpha\beta\) fixes how energy density in \(L\) scales redshift to the same Newtonian \(\Phi\) **on shell** of the Einstein solution.

**Status:** **Structural** — uses external theorem (Jacobson) + GR weak field; does **not** need the false \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\) step.  
**Gap:** in-repo writeup never spells this chain fully; Newton.md short-circuits with bad algebra.

### Path L — Pure load-clock phenomenology (weaker)

1. Postulate \(d\tau/dt=1/(1+\alpha L)\) with \(L=\beta\rho c^2/\epsilon_0\).  
2. Define an effective potential by \(d\tau/dt=1+\Phi/c^2\) (static weak field).  
3. Then \(\Phi=-\alpha\beta c^4\rho/\epsilon_0\) **pointwise** — this is **not** Newtonian gravity (which is nonlocal: \(\Phi= -G\int\rho/|x-x'|\)).  
4. Pointwise \(\Phi\propto\rho\) is **unphysical** as gravity (no inverse-square force from a localized mass distribution in the usual sense).

**Status:** **Obstruction** as a derivation of Newtonian gravity. At best a local redshift model, not Poisson.

### Path M — Matching only (honest minimal claim)

1. Assume the continuum theory has already produced a metric with Newtonian limit \(\nabla^2\Phi=4\pi G\rho\) via Clausius/Einstein (Path J).  
2. Expand \(d\tau/dt\) and match coefficients so load energy term agrees with \(\Phi\) **for the same** \(\rho\) solutions (e.g. compare coefficients in constant-density ball interior where \(\Phi\) is quadratic and related to \(\rho\)).  
3. That fixes \(\alpha\beta=4\pi G/c^4\) **relative to \(\epsilon_0\) bookkeeping**.

**Status:** **Legitimate calibration**, not a derivation of Poisson from load alone.

---

## 5. Recommended claim language (post-audit)

**Allowed:**

> In the low-load regime the energy-density term dominates \(L\). With \(\mathcal{L}_g\) constrained by the Clausius relation, the Einstein equation (Jacobson) and its weak-field Poisson limit are available; matching the load-induced proper-time factor to the Newtonian potential fixes \(\alpha\beta=4\pi G/c^4\). Newtonian gravity is thus recovered as a **calibrated low-load regime** of the framework, not as an independent force law.

**Disallowed (until rewritten):**

> Taking the Laplacian of \(\Phi\propto\rho\) directly yields \(\nabla^2\Phi=4\pi G\rho\).

---

## 6. Gap list (actionable)

| ID | Gap | Severity | Action |
|----|-----|----------|--------|
| N1 | Laplacian step in Newton.md is algebraically wrong if \(\Phi\propto\rho\) pointwise | **High** | Rewrite recovery along Path J or M |
| N2 | Role of \(\epsilon_0\) in equating \(\Phi\) and \(\rho\) underspecified | Medium | Define dimensions / set \(\epsilon_0\) explicitly in matching |
| N3 | Entropy and boundary terms “negligible” not quantified | Low | State as modeling assumption |
| N4 | No interior/exterior matched example (constant ball) | Medium | Optional worked example for Path M |
| N5 | Canonical master-equation file asserts EFE “automatically” from Clausius without spelling weak-field | Medium | Cross-link Jacobson; avoid overclaim |

---

## 7. Status for M6/M7

| Input to weak-field plug-test | After M8 |
|-------------------------------|----------|
| Our side Poisson | Use **Path J/M**: Poisson from GR weak field + Clausius; load supplies calibrated redshift — **not** false Laplacian chain |
| Confidence | Medium: story viable; **writeup must be corrected** before claiming “exact recovery as written in Newton.md” |
| Blocking M6? | No — M6 can compare GfE low-coupling → EH → standard Newton **to** our Path J claim; both then share GR weak field as common end, which is a **valid but weaker** cross-check |

---

## 8. Follow-up (2026-07-14, N1 rewrite)

| Gap | Action taken |
|-----|----------------|
| N1 | **Closed as writeup:** Path J/M is now canonical in [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) and [quantum/Newton.md](../quantum/Newton.md) |
| N2 | \(\epsilon_0\) bookkeeping stated as absorbed into \(\beta\) under Path M (medium; still not a first-principles derivation of \(G\)) |
| N4 | Constant-density ball matching example added in newtonian recovery |
| N3, N5 | Unchanged modeling assumptions; master-equation still imports Jacobson |

**Status line:** **M8 audit complete + N1 rewrite landed.** Algebraic gap confirmed historically; **corrected Path J/M is now the in-repo recovery.** Calibration \(\alpha\beta=4\pi G/c^4\) retained only as matching under Path J/M.

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
