# M6c — Bianconi Linearization (W1): Coefficient-Level Next Order

**M-id:** M6c (executes weak-field note **W1** + upgrades M6b)  
**Status:** **Linearized schematic derived from PDF Eqs. (60),(64),(66)–(68); Poisson sector recovered; next-order operators identified; full numerical PPN not claimed**  
**Primary external:** G. Bianconi, *Gravity from entropy*, arXiv:2408.14391 (PDF pp. 7–9; Eqs. 45, 60, 64, 66–68)  
**Parents:** [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md) · [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) · [weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md)  
**Local PDF:** [papers/external/Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf](../papers/external/Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf)  
**Date:** 2026-07-14

---

## 1. Purpose

Carry out the **linearized weak-field expansion** of Bianconi’s modified Einstein + G-field system about Minkowski, far enough to:

1. Recover leading Poisson (confirm M6).  
2. Name the **next-order operators** that correct \(\nabla^2\Phi=4\pi G\rho_m\).  
3. Compare those operators **coefficient-structurally** to our load \(\gamma_L,\delta_L\) clock extras (M6b).

**Honesty:** Bianconi explicitly states that a detailed study of solutions is **beyond the scope** of the paper (PDF p. 9 after Eq. 68). This note is a **repo linearization sketch** citing paper equations — not an independent numerical GR code or published PPN analysis.

---

## 2. Exact continuum equations (from PDF)

### 2.1 G-field algebraic / EOM content

PDF Eq. **(60)** (after eliminating \(\tilde\Theta=\tilde{\mathcal{G}}^{-1}\)):

\[
\tilde{\mathcal{G}}^{-1}
=
\tilde I
+
\alpha_B\,\tilde M\,\tilde g^{-1}
-
\beta_B\,\tilde{\mathcal{R}}\,\tilde g^{-1}.
\]

(Repo subscripts \(B\) for Bianconi couplings.)

### 2.2 Emergent cosmological term

PDF Eq. **(64)**:

\[
\Lambda_G
=
\frac{1}{2\beta_B}
\operatorname{Tr}_F
\bigl(
\tilde{\mathcal{G}}
-
\tilde I
-
\ln\tilde{\mathcal{G}}
\bigr)
\;\ge\; 0.
\]

Near identity \(\tilde{\mathcal{G}}=\tilde I+\tilde\epsilon\), \(\|\tilde\epsilon\|\ll 1\):

\[
\Lambda_G
=
\frac{1}{4\beta_B}
\operatorname{Tr}_F(\tilde\epsilon^2)
+
O(\|\tilde\epsilon\|^3).
\]

**Leading piece is quadratic in the G-field perturbation** — vanishes at linear order in \(\tilde\epsilon\).

### 2.3 Modified Einstein equations

PDF Eq. **(66)**:

\[
R^G_{(\mu\nu)}
-
\frac12 g_{\mu\nu}
\bigl(R_G-2\Lambda_G\bigr)
+
D_{(\mu\nu)}
=
\kappa\, T_{(\mu\nu)},
\qquad
\kappa=\frac{\alpha_B}{\beta_B}.
\]

**Dressed Ricci** PDF Eq. **(67)** (structure):

\[
R^G_{\mu\nu}
=
\mathcal{G}^{(0)} R_{\mu\nu}
+
[\mathcal{G}^{(1)}]^\rho{}_\mu R_{\rho\nu}
+
\text{(2-form G-field contractions with Riemann)}
+\cdots
\]

**G-field second-derivative tensor** PDF Eq. **(68)** (structure):

\[
\begin{aligned}
D_{\mu\nu}
&=
\bigl(\nabla^\rho\nabla_\rho g_{\mu\nu}-\nabla_\mu\nabla_\nu\bigr)\mathcal{G}^{(0)}
-
\nabla_\rho\nabla_\nu[\mathcal{G}^{(1)}]^{(\rho}{}_\mu)
\\
&\quad
+
\tfrac12\nabla^\rho\nabla_\rho[\mathcal{G}^{(1)}]_{\mu\nu}
+
\tfrac12\nabla_\rho\nabla_\eta[\mathcal{G}^{(1)}]^{\rho\eta}g_{\mu\nu}
\\
&\quad
+
\text{(2-form G-field second derivatives)}
+\cdots
\end{aligned}
\]

**Key structural facts from the paper:**

| Fact | Implication |
|------|-------------|
| Equations second order in \(g\) and \(\tilde{\mathcal{G}}\) | No Ostrogradsky higher-derivative ghosts *at the level of derivative count* |
| Low coupling \(\alpha_B',\beta_B'\ll 1\) → EH + matter, \(\Lambda=0\) (PDF Eq. 45, p. 7) | Leading Newton via standard GR linearization |
| \(\Lambda_G=O(\|\epsilon\|^2)\) | **No linear CC** in the G-field fluctuation |
| \(D_{\mu\nu}\) involves \(\nabla\nabla\mathcal{G}\) | **Can** source corrections to \(\Phi\) at linear order in \(\epsilon\) if \(\epsilon\sim O(h)\) |

---

## 3. Linearization ansatz

### 3.1 Background

\[
g_{\mu\nu}
=
\eta_{\mu\nu}
+
h_{\mu\nu},
\qquad
|h|\ll 1,
\quad
\partial_t\approx 0
\quad\text{(static)},
\quad
|v|\ll c.
\]

Newtonian gauge (standard):

\[
h_{00}
=
-2\Phi/c^2,
\qquad
h_{ij}
=
-2\Psi\delta_{ij}/c^2
\quad\text{(or }=-2\Phi\delta_{ij}/c^2\text{ if }\Psi=\Phi\text{)},
\]

with matter \(T_{00}\approx\rho_m c^2\), other \(T_{\mu\nu}\) negligible.

### 3.2 G-field expansion

\[
\tilde{\mathcal{G}}
=
\tilde I
+
\tilde\epsilon,
\qquad
\|\tilde\epsilon\|\ll 1.
\]

From Eq. (60), to first order in couplings and curvature/matter:

\[
\tilde\epsilon
\;\approx\;
-
\alpha_B\,\tilde M\,\tilde g^{-1}
+
\beta_B\,\tilde{\mathcal{R}}\,\tilde g^{-1}
+
O(2),
\]

so on a weak-field background with slow matter,

\[
\tilde\epsilon
=
O\bigl(\alpha_B M\bigr)
+
O\bigl(\beta_B \partial^2 h\bigr).
\]

**Scaling:** if \(\alpha_B\sim\alpha'\ell_P^4\), \(\beta_B\sim\beta'\ell_P^2\) (paper’s dimensional assignments), then \(\epsilon\) is **Planck-suppressed** for laboratory densities/curvatures — consistent with “low coupling → pure EH.”

---

## 4. Leading order → Poisson (M6 reaffirmed)

Set \(\tilde\epsilon=0\) (or \(\alpha_B,\beta_B\to 0\)):

\[
R^G_{\mu\nu}\to R_{\mu\nu},
\quad
\Lambda_G\to 0,
\quad
D_{\mu\nu}\to 0.
\]

Eq. (66) → Einstein equation with \(\kappa=\alpha_B/\beta_B\) absorbed into the usual \(8\pi G/c^4\) normalization of \(T_{\mu\nu}\). Static weak field:

\[
\nabla^2\Phi
=
4\pi G\,\rho_m.
\]

**M6 WEAK PASS reaffirmed** with **PDF anchors:** low-coupling reduction Eq. (45)/(p. 7) + standard GR linearization.

---

## 5. Next order — operator decomposition for \(\Phi\)

Retain \(O(\epsilon)\) and \(O(h\epsilon)\) carefully.

### 5.1 Cosmological piece

\[
\Lambda_G
=
\frac{1}{4\beta_B}\operatorname{Tr}(\epsilon^2)+O(\epsilon^3)
=
O(\epsilon^2).
\]

In the linearized equation for \(h_{\mu\nu}\), a **constant** \(\Lambda\) sources

\[
\nabla^2\Phi
\supset
-\,\Lambda c^2
\quad\text{(de Sitter / continuous medium bookkeeping)}.
\]

But \(\Lambda_G=O(\epsilon^2)\) is **second order** in the G-field fluctuation. For \(\epsilon=O(h)\) this is \(O(h^2)\) — **beyond linear weak field**.  

**Conclusion G1a (refined):** \(\Lambda_G\) does **not** correct the **linear** Poisson equation; it enters as a **quadratic / cosmological** effect. Matches M6b “IR / cosmology, not solar-system linear force law” when \(\epsilon\) is small.

### 5.2 Dressed Ricci \(R^G-R\)

Schematically,

\[
R^G_{\mu\nu}-R_{\mu\nu}
=
\epsilon\cdot R
+
(\delta_\epsilon\text{-contractions of Riemann})
=
O(\epsilon\cdot\partial^2 h).
\]

At linear order in \(h\) with \(\epsilon\) **independent** of \(h\), this can look like a **position-dependent \(G_N\)** or anisotropic stress. If \(\epsilon\) is **slaved** to \(h\) via Eq. (60) (\(\epsilon\sim\beta_B\partial^2 h\)), contributions are \(O(\beta_B(\partial^2)^2 h)\) — **higher-derivative / short-range** after moving to one side:

\[
\bigl(1+O(\beta_B\nabla^2)\bigr)\nabla^2\Phi
=
4\pi G\rho_m+\cdots
\]

**Yukawa / form-factor** schematic (not a derived mass pole without the G-field kinetic term isolated):

\[
\nabla^2\Phi
-
\ell_{\mathrm{eff}}^2\nabla^4\Phi
\;\sim\;
4\pi G\rho_m,
\qquad
\ell_{\mathrm{eff}}^2
\sim
O(\beta_B)
\sim
O(\ell_P^2)
\]

if the only scale is Planckian — **unobservable** at solar-system resolution. A **light** G-field mode would require a different mass gap not fixed in the paper’s weak-field discussion.

### 5.3 \(D_{\mu\nu}\) as effective source

At linear order in \(\epsilon\), static, Cartesian,

\[
D_{00}
\;\sim\;
c_1\nabla^2\epsilon^{(0)}
+
c_2\partial_i\partial_j\epsilon^{(1)ij}
+
\cdots
\]

(coefficients \(c_i\) are \(O(1)\) combinatorial factors from Eq. 68). The \(00\)-component of (66) then yields the schematic master formula:

\[
\boxed{
\nabla^2\Phi
=
4\pi G\rho_m
+
\mathcal{S}_D[\epsilon]
+
\mathcal{S}_{R^G}[\epsilon,h]
+
O(\Lambda_G,\,h^2)
}
\]

with

\[
\mathcal{S}_D[\epsilon]
\;\sim\;
c^2\,D_{00}[\epsilon]
\;\sim\;
c^2\nabla^2\epsilon_{\mathrm{eff}}.
\]

**If** \(\epsilon_{\mathrm{eff}}\) is quasi-local in \(\rho_m\) (\(\epsilon\sim \alpha_B\rho_m/\mu^4+\cdots\)), then \(\mathcal{S}_D\) **renormalizes the Poisson source** (effective \(G_N\)).  
**If** \(\epsilon_{\mathrm{eff}}\) is an independent light field, \(\mathcal{S}_D\) acts as a **fifth-force / scalar-tensor** correction.

Bianconi does **not** fix which regime is realized for dark-matter phenomenology (paper: future work).

### 5.4 Low-coupling linearized limit (paper’s own Eq. 45)

PDF Eq. **(45)** (linearized entropic Lagrangian before G-field dressing narrative):

\[
\mathcal{L}
\;\xrightarrow{\alpha',\beta'\ll 1}\;
3\beta_B R
-
\alpha_B\langle\Phi|\tilde D\tilde g^{-1}\tilde D|\Phi\rangle
-
\alpha_B(m^2+\xi R)|\Phi|_{\mathrm{top}}^2.
\]

This is **Einstein–Hilbert + topological matter**, \(\Lambda=0\). Linearizing about Minkowski **is ordinary GR + matter** — no extra \(D_{\mu\nu}\) because those appear in the **G-field reformulation** of the same theory when \(\tilde{\mathcal{G}}\) is retained as an independent dressing.

**Consistency check:** G-field form and low-coupling EH form must agree when \(\tilde{\mathcal{G}}\) is integrated out at low coupling; residual \(D_{\mu\nu}\) and \(\Lambda_G\) must then be higher order in \(\alpha_B,\beta_B\).

---

## 6. Coefficient-level comparison to load \(\gamma_L,\delta_L\)

| Bianconi next-order object | Linear Poisson impact | Our load analogue | Match? |
|----------------------------|----------------------|-------------------|--------|
| \(\Lambda_G=O(\epsilon^2)\) | **None at linear order** | Cosmology / \(\delta_L\) screen narrative | Analogical IR only |
| \(D_{\mu\nu}\sim\nabla\nabla\epsilon\) | **Yes if \(\epsilon=O(h)\) or independent** | No direct tensor; \(\gamma_L|\dot S_c|\) is **scalar clock** | **Structural FAIL** (M6b stands) |
| \(R^G-R\sim\epsilon\cdot R\) | Effective \(G_N(x)\), anisotropic stress | Path J keeps Einstein \(G_N\) fixed; load calibrates clocks | **FAIL** as identity |
| Low-coupling Eq. (45) | Pure Poisson | Path J Poisson | **WEAK PASS** (shared) |
| \(\kappa=\alpha_B/\beta_B\) | Normalizes \(T_{\mu\nu}\) | \(\alpha_L\beta_L=4\pi G/c^4\) Path M product | **Analogical calibration roles only** (M7) |

### Refined M6/M6b outcome after linearization

| Criterion | Outcome |
|-----------|---------|
| Leading Poisson | **PASS** (PDF-anchored) |
| Linear-order \(\Lambda_G\) correction | **Absent** (\(O(\epsilon^2)\)) |
| Linear-order \(D_{\mu\nu}/R^G\) correction | **Present in structure**; **Planck-suppressed** if \(\epsilon\sim\beta_B\partial^2 h\); potentially light if \(\epsilon\) dynamical with tiny mass (not computed here) |
| Match to \(\gamma_L,\delta_L\) as same operators | **FAIL** |
| Numerical PPN \((\gamma,\beta)\) for GfE | **NOT COMPUTED** (needs full scalar-tensor reduction) |

---

## 7. What a coefficient-complete PPN would still need

| Step | Status |
|------|--------|
| Fix matter sector to perfect fluid \(T_{\mu\nu}\) (not only Dirac–Kähler) | Open modeling choice |
| Reduce \(\tilde{\mathcal{G}}\) multiplet to effective scalars/vectors | Open |
| Harmonic-gauge linear system for \((h_{\mu\nu},\epsilon)\) | Sketch only (§5) |
| Read off PPN potentials / light deflection | Not done |
| Solar-system bounds on \(\ell_{\mathrm{eff}}\) | Not done |

**Until those exist, do not quote a GfE PPN number from this repo.**

---

## 8. Implications for “equation adjustment”

| If we want frameworks closer | Adjustment direction |
|----------------------------|----------------------|
| Load side to look more GfE-like | Promote \(\gamma_L,\delta_L\) (or a new field) into **metric EOM** sources, not only \(d\tau\) |
| GfE side to look more load-like | Extract a **scalar clock** from \(\tilde{\mathcal{G}}\) or \(\Lambda_G\) for static observers — not primary in Bianconi |
| Keep both honest | Accept shared Einstein limit + **divergent next-order ontology** (M6b/M6c) |

**No forced numerical identification** of \((\alpha_L,\beta_L,\gamma_L,\delta_L)\) with \((\alpha_B,\beta_B,\epsilon)\).

---

## 9. Explicit non-claims

1. We did **not** solve Bianconi’s full nonlinear system.  
2. We did **not** compute solar-system observables.  
3. We did **not** prove stability of the G-field sector.  
4. Schematic \(O(\ell_P^2\nabla^4\Phi)\) is **illustrative scaling**, not a derived propagator pole.  
5. Dark-matter interpretation of \(\tilde{\mathcal{G}}\) remains the paper’s **open suggestion**, not a result of this note.

---

## 10. Status line

**M6c: PDF-anchored linearization freezes leading Poisson PASS; \(\Lambda_G\) is second order in \(\epsilon\); \(D_{\mu\nu}\) and dressed \(R^G\) are the true linear next-order structures and still do not match load-clock \(\gamma_L,\delta_L\). Coefficient-level PPN remains future work; structural M6b FAIL stands.**

---

### PDF equation index (for auditors)

| PDF eq. | Content used here |
|---------|-------------------|
| (45) | Low-coupling → EH + matter, \(\Lambda=0\) |
| (60) | G-field EOM / algebraic content |
| (64) | \(\Lambda_G(\tilde{\mathcal{G}})\) |
| (66) | Modified Einstein |
| (67) | Dressed Ricci \(R^G\) |
| (68) | \(D_{\mu\nu}\) second derivatives of G-field |

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
