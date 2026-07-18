# M6 — Weak-Field Plug-Test: Load/Master Equation vs GfE Low-Coupling

**M-id:** M6  
**Status:** **Completed as analysis — outcome: WEAK PASS on shared Poisson end; NO framework equivalence; extra structures unmatched**  
**Depends on:** [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md) · [m7-symbol-map.md](m7-symbol-map.md) · [weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md)  
**Next-order follow-on:** [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md) · [m6c-bianconi-linearization.md](m6c-bianconi-linearization.md)  
**Path J/M recovery:** [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md)  
**Date:** 2026-07-14

---

## 1. Test design

### Shared problem (static weak field)

- Background: Minkowski + static Newtonian potential \(\Phi\ll c^2\).  
- Matter: classical mass density \(\rho_m(\mathbf{x})\) (perfect fluid at rest; \(T_{00}\approx\rho_m c^2\)).  
- Ask for the **leading** equation determining \(\Phi\).

### Side A — Ours (after M8 Path J/M)

1. Assume \(\mathcal{L}_g\) satisfies Clausius on local horizons ⇒ Einstein equation (Jacobson), **or** take Einstein as the thermodynamic fixed point of the channel generator.  
2. Weak-field GR ⇒
   \[
   \nabla^2\Phi = 4\pi G\rho_m.
   \]
3. Load \(L\approx\beta_L\rho_m c^2/\epsilon_0\) calibrates proper-time factor to the same \(\Phi\) via matching \(\alpha_L\beta_L=4\pi G/c^4\) **on shell** (Path M), not via the false pointwise Laplacian identity.

### Side B — Bianconi GfE (documented low coupling)

1. Low coupling: entropic action → Einstein–Hilbert with **zero** cosmological constant (Bianconi arXiv:2408.14391 abstract/body; repo notes).  
2. Standard GR weak field on that EH theory ⇒
   \[
   \nabla^2\Phi = 4\pi G\rho_m
   \]
   (Newton via GR; **not** a separate load-clock derivation in GfE).  
3. Away from strict low coupling: modified equations with \(\Lambda_G(\tilde{\mathcal{G}})\), dressed \(R^G\), \(D_{\mu\nu}\).

---

## 2. Side-by-side leading order

| Item | Ours (Path J/M) | GfE low coupling |
|------|-----------------|------------------|
| Leading PDE for \(\Phi\) | \(\nabla^2\Phi=4\pi G\rho_m\) | \(\nabla^2\Phi=4\pi G\rho_m\) |
| Mechanism | Clausius/Einstein + load calibration | Relative-entropy action → EH → GR linearization |
| Extra fields at leading Newton | None if \(\gamma_L,\delta_L\) dropped | None if \(\tilde{\mathcal{G}}=\tilde I\), \(\Lambda_G=0\) |
| Status | Internal (gap N1 fixed by Path J) | External paper claim + standard GR |

**Leading-order comparison:** **equations agree**.

---

## 3. Next-order / structural extras

| Feature | Ours | GfE | Match? |
|---------|------|-----|--------|
| Scalar demand clock \(1/(1+\alpha L)\) | Yes — defines \(d\tau\) even in weak field as correction | No direct analogue | **No** |
| Emergent \(\Lambda\ge 0\) from auxiliary field | Cosmology recovery narrative | \(\Lambda_G(\tilde{\mathcal{G}})\) explicit | **Analogical only** |
| Matter as channel state \(\rho\) | Yes | Metrics + topological forms | **No** |
| Relative entropy of metrics | Not primary | Primary action | **No** |
| Euclidean PM dual (ACD-EW) | Constructive warm-up | Warm-up of same paper family | **Yes (warm-up only)** |

---

## 4. Plug-test outcome

### Result: **WEAK PASS at Poisson order; FAIL as theory identity**

| Criterion | Outcome |
|-----------|---------|
| Same leading Poisson equation | **PASS** |
| Same derivation mechanism | **FAIL** (shared GR weak field / Einstein, different upper structure) |
| Identifiable \((\alpha_L,\beta_L)=(\alpha_B,\beta_B)\) | **FAIL / refused** (M7) |
| Next-order corrections match | **FAIL (structural)** at object-class level ([m6b](m6b-next-order-weak-field.md)); coefficient/PPN **NOT ESTABLISHED** |
| Continuum GfE \(\Leftrightarrow\) master equation | **FAIL** (not supported) |

### Interpretation (honest)

Agreement on \(\nabla^2\Phi=4\pi G\rho_m\) is **real** and **expected** if both frameworks embed Einstein gravity at low demand. It is **supporting circumstantial evidence** that they sit in the same phenomenological class as GR, **not** evidence that our load dynamics equal Bianconi’s relative-entropy EL equations.

The interesting dual remains **ACD-EW Euclidean warm-up**, which does **not** lift automatically to this Poisson agreement (different mathematical layer).

---

## 5. What would flip the outcome

| Upgrade | Would enable |
|---------|----------------|
| Explicit expansion of Bianconi modified Einstein + G-field EOM to \(\mathcal{O}(\Phi)\) with extra Yukawa/scalar modes | Strong FAIL or refined PASS if modes decouple |
| Continuum \(L[G-g,\dot S_c]\) whose EL reproduce load-gated channel | Constructive dynamics dual |
| Solar-system bounds on both extras | Phenomenological discrimination |

---

## 6. Explicit non-claims

1. We did **not** solve Bianconi’s field equations numerically.  
2. We did **not** derive \(\alpha_L\beta_L\) from \(\alpha_B,\beta_B\).  
3. We did **not** prove master equation \(\Leftrightarrow\) GfE.  
4. Weak PASS does **not** upgrade either theory to GR-level certainty.  
5. M8 Path J still relies on Jacobson/Einstein input — Poisson is not free from GR.

---

## 7. Status line

**M6: WEAK PASS — both sides yield Newtonian Poisson at leading weak-field order via Einstein/GR; mechanisms and next-order structures diverge; no framework equivalence.**  
**M6b:** structural next-order mismatch frozen (GfE metric EOM extras vs load-clock \(\gamma_L,\delta_L\)) — see [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md).

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
