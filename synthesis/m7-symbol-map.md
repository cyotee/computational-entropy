# M7 — Candidate Symbol Map (Load Constants ↔ GfE Couplings)

**M-id:** M7  
**Status:** **Candidate map + structural non-maps; no numerical identification claimed**  
**Depends on:** [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md) · Path J/M [../emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md)  
**Feeds:** [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) · [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md)  
**Date:** 2026-07-14

---

## 1. Purpose

Propose **which symbols could correspond** between:

| Ours | Bianconi GfE |
|------|----------------|
| \(\alpha_L,\beta_L,\gamma_L,\delta_L\), \(\epsilon_0\), \(L\), \(S_c\), \(\Phi_g\) | \(\alpha_B,\beta_B\), \(\tilde G\), \(\tilde{\mathcal{G}}\), \(\Lambda_G\), \(\kappa=\alpha_B/\beta_B\) |

After M8: our Newtonian contact is **Path J/M** (Clausius → Einstein → Poisson + load calibration), not the false \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\) step.

---

## 2. Type-safe dictionary

| Ours | Type | Bianconi | Type | Map? |
|------|------|----------|------|------|
| \(L\) | scalar field (dimensionless) | \(\tilde{\mathcal{G}}\) | metric/operator field | **No identity** — at most functionals |
| \(L_E\sim E[\rho]\) | scalar | \(\alpha_B\tilde M\) deformation | tensor | **Structural candidate** (matter drives geometry) |
| \(\gamma_L|dS_c/d\tau|\) | scalar rate | \(D_{\mu\nu}\) / entropy production in channel language | tensor | **Analogical** |
| \(\delta_L S_{\rm boundary}/S_{\rm BH}\) | scalar | holographic / screen content (not primary in GfE action) | — | **Weak / none** in GfE core action |
| \(S_c=S(\Phi_g(\rho))\) | von Neumann of state | \(\operatorname{Tr} g\ln G^{-1}\) | relative entropy of metrics | **No identity** |
| \(d\tau=dt/(1+\alpha_L L)\) | time reparam | no direct scalar clock in GfE EL | — | **Form rhyme only** with \(1/(1+\cdot)\) |
| \(\alpha_L\beta_L=4\pi G/c^4\) | matched product | \(\kappa=\alpha_B/\beta_B\) | ratio in modified Einstein | **Analogical calibration roles** — **not equal as numbers** |
| \(g_{\mu\nu}(\rho)\) | metric from state | \(g\) dynamical metric | metric | **Semantic** shared role |
| Euclidean \(G[\phi]=1+\alpha_G|\nabla\phi|^2\) | ACD-EW | warm-up \(G=g+\alpha_B M\) | metric | **Structural** (warm-up only; M5) |

---

## 3. Candidate continuum map (hypothesis, not theorem)

### Hypothesis H-map (weak-field)

On a static weak-field background with mass density \(\rho_m\) (classical):

1. **Common end:** both frameworks aim at Newtonian \(\nabla^2\Phi=4\pi G\rho_m\) (ours via Path J/M + calibration; GfE via low coupling → EH → GR weak field).  
2. **Shared calibration target:** fix one overall coupling so Poisson source coefficient is \(4\pi G\).  
3. **Do not set** \(\alpha_L\beta_L=\alpha_B/\beta_B\); instead define a **bridge functional**

\[
L_{\mathrm{eff}}[\rho_m,g]
\;\stackrel{?}{=}\;
F\bigl(\|G[g,\rho_m]-g\|,\; \partial_t S,\; S_{\partial}\bigr)
\]

whose small-\(L_{\mathrm{eff}}\) expansion reproduces \(d\tau/dt\approx 1+\Phi/c^2\) **on shell** of the Einstein solution with the same \(\Phi[\rho_m]\).

**Status:** **candidate program** — not constructed explicitly beyond ACD-EW’s \(L_E\propto\mathbb{E}[G-1]\) in Euclidean signature.

### Explicit non-map theorems (type)

| Forbidden equality | Reason |
|--------------------|--------|
| \(L=\tilde{\mathcal{G}}\) | Scalar vs operator-valued field |
| \(S_c=\operatorname{Tr} g\ln G^{-1}\) | Different arguments (state vs metrics) |
| \(\alpha_L=\alpha_B\), \(\beta_L=\beta_B\) | Different actions; clash with M8 Path J |

---

## 4. Minimal map for M6 plug-test

For the plug-test we only need:

| Object | Our side (M8 Path J/M) | GfE side |
|--------|------------------------|----------|
| Leading weak-field equation | \(\nabla^2\Phi=4\pi G\rho_m\) (via Einstein/Jacobson + calibration) | \(\nabla^2\Phi=4\pi G\rho_m\) (via EH low coupling + GR linearization) |
| Extra structures at next order | load corrections \(\propto\alpha_L L\) beyond linear; \(\gamma_L,\delta_L\) terms | \(\Lambda_G\), \(D_{\mu\nu}\), dressed \(R^G\) |

**M6 outcome options:**

- **PASS (weak):** both reduce to the **same** Poisson equation at leading order (shared GR weak field) — agreement is **real but unsurprising** if both embed Einstein.  
- **FAIL:** GfE low-coupling expansion produces extra long-range scalars / modified Poisson not present in our Path J.  
- **IMPOSSIBLE SETUP:** cannot place the same \(\rho_m\) in both matter sectors without undefined maps — then M9 required.

---

## 5. Status line

**M7: candidate structural map only; numerical constant identification refused; M6 should test shared Poisson end + next-order extras, not \(\alpha_L\beta_L=\alpha_B/\beta_B\).**

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
