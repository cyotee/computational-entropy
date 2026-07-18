# M5 — Warm-Up Continuum Limit / T4 Citation Bridge

**M-id:** M5  
**Status:** **Citation bridge complete (literature-backed); full \(h\to 0\) lattice theorem open**  
**Hygiene (abstract language, transfer, lit-vs-open):** [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) — prefer that note for claim boundaries; this file keeps T4 target + FD sketch.  
**Smooth-only action lemma (M5b):** [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) — \(O(h)\) Riemann-sum consistency for \(C^3\) \(\phi\); **not** Γ-convergence.  
**PM gradient flow / discrete descent (M5c):** [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) — Layer W continuum lit + discrete \(E_h\) Euler sketch.  
**Scope:** Euclidean GfE warm-up only — **not** Lorentzian modified Einstein  
**Parents:** [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) · Bianconi arXiv:2503.14048 · arXiv:2408.14391 warm-up  
**Date:** 2026-07-14

---

## 1. Goal

Connect the **joint-toy discrete** objects

\[
G_i = 1+\alpha_G(\nabla_h\phi)_i^2,
\quad
S_{\mathrm{GfE}}^h[\phi]=-\sum_i\ln G_i,
\quad
\text{PM / Euler}
\]

to Bianconi’s **continuum Euclidean warm-up** (GfE action between support metric \(g\) and matter-induced metric \(G\), with PM as gradient flow — *Beyond holography*).

---

## 2. Continuum warm-up (external, as used)

| Object | Continuum (Bianconi warm-up) | Discrete toy |
|--------|------------------------------|--------------|
| Support metric | \(g=\mathrm{Id}\) on \(\mathbb{R}^d\) or domain \(\Omega\) | Edge weights \(1\) |
| Scalar | \(\phi:\Omega\to\mathbb{R}\) | \(\phi\in\mathbb{R}^N\) |
| Induced metric | \(G = g + \alpha (\nabla\phi)\otimes(\nabla\phi)\) (1D: \(G=1+\alpha(\phi')^2\)) | \(G_i=1+\alpha_G(\phi_{i+1}-\phi_i)^2\) |
| Action density | \(\mathcal{L}=-\operatorname{Tr}\ln(G g^{-1})=-\ln(1+\alpha|\nabla\phi|^2)\) (warm-up) | \(-\ln G_i\) summed |
| Gradient flow | Perona–Malik anisotropic diffusion | Explicit Euler PM |
| Literature | arXiv:2503.14048; warm-up in arXiv:2408.14391 | `_joint_toy_v2_core.py`, `_joint_toy_2d.py` |

**Status of literature link:** **Structural / accepted as external claim** — we do not re-derive Bianconi’s variational calculation here; we use it as the continuum target of T4.

---

## 3. Formal T4 statement (target)

> **Proposition T4 (lattice → continuum warm-up; target).**  
> Let \(\phi^h\) be grid interpolants of lattice fields on mesh \(h\), with \(\alpha_G\) fixed and \(\phi\) in a Sobolev class \(H^2\) (or BV for jump limits separately). Then as \(h\to 0\),
>
> \[
> h\sum_i -\ln\bigl(1+\alpha_G|D_h\phi_i|^2\bigr)
> \;\to\;
> \int -\ln\bigl(1+\alpha_G|\nabla\phi|^2\bigr)\,dx
> \]
>
> in the sense of Γ-convergence or continuous convergence on smooth \(\phi\), and the Euler PM scheme with \(dt=O(h^2)\) is a consistent discretization of continuum PM.

**Status:** **Open as full theorem** in this repo; **standard finite-difference consistency** for smooth \(\phi\) is a **proved sketch** below. Smooth **action** slice upgraded to conditional \(O(h)\) lemma in [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) (still **not** Γ-convergence / BV).

---

## 4. Consistency sketch (smooth \(\phi\))

Assume \(\phi\in C^3(\mathbb{R})\) with rapid decay / periodic.

1. **Gradient consistency:** \(D_h\phi(x)=h^{-1}(\phi(x+h)-\phi(x))=\phi'(x)+O(h)\).  
2. **Action density:** \(\ln(1+\alpha_G|D_h\phi|^2)=\ln(1+\alpha_G|\phi'|^2)+O(h)\) uniformly on compact sets where \(\phi'\) bounded.  
3. **Riemann sum:** \(h\sum_i f(D_h\phi(ih))\to\int f(\phi')\,dx\).  
4. **PM flux:** \(\rho_h=1/(1+(D_h\phi/K)^2)\to 1/(1+(\phi'/K)^2)\); discrete div is consistent with \(\partial_x(\rho\phi')\) at \(O(h)\).  
5. **CFL:** \(dt\le C h^2\) for parabolic stability → continuum heat/PM scaling.

**Jumps / BV:** continuum PM is delicate (forward–backward); lattice Euler with \(K>0\) remains well-posed. Continuum limit of **jump solutions** needs BV/Γ-convergence tools — **open** (not required for smooth warm-up bridge).

---

## 5. What M5 settles vs not

| Settled | Not settled |
|---------|-------------|
| Dictionary lattice \(\leftrightarrow\) continuum warm-up | Full Γ-convergence proof |
| Literature identification PM = GfE warm-up flow | Lorentzian GfE / modified Einstein |
| 1D and 2D toys are **consistent discretizations** of that warm-up (smooth regime) | That toys prove continuum gravity |
| Citation path for papers: dual toys implement discrete Bianconi warm-up | Equivalence to master equation |

---

## 6. Relationship to ACD-EW and M1

- ACD-EW uses the **discrete** warm-up; M5 says that warm-up is the standard continuum object Bianconi analyzes in Euclidean signature.  
- M1 residual domination is a **discrete** statement; continuum analogue would be a separate PDE inequality.  
- **Non-claim:** continuum limit of ACD-EW does **not** automatically yield Bianconi’s full gravitational EL equations.

---

## 7. Status line for board

**M5: citation bridge complete; smooth action \(O(h)\) lemma in [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md); T4 full Γ / BV / PM scheme still open. Claim hygiene:** [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md).

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
