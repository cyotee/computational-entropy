# M5b — Smooth Warm-Up Action Limit (Conditional Lemma)

**M-id:** M5b (smooth action slice of T4)  
**Status:** Lemma sketch (D15 polish) — cite from program DRAFT Layer W  
**Rigor:** Elementary FD consistency + Riemann-sum estimate under H1–H4; **not** Γ-convergence  
**Scope:** Euclidean GfE warm-up action only — lattice \(G_i=1+\alpha|\nabla_h\phi|^2\), mesh-weighted \(S_h\)  
**Parents:** [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) · [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) · [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md)  
**Dynamics sibling (M5c):** [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md)  
**Date:** 2026-07-15  
**Stance:** Preliminary research. Under-claim. No jumps, no residual dual continuum, no Lorentzian GfE, no master equation.

---

## 0. Purpose

M5 hygiene asks for a short pure proposition on the **action only**, with rate \(O(h)\), then stop. This note is that proposition in **conditional lemma** form: fixed smooth field, forward differences, mesh-weighted discrete action \(\to\) continuum integral.

It does **not** close full Proposition T4 (Γ-convergence, BV jumps, PM scheme, residual dual).

---

## 1. Objects

### 1.1 Discrete (1D periodic lattice)

Let \(N\in\mathbb{N}\), \(h=1/N\), sites \(x_i=ih\) on the torus \(\mathbb{T}^1=\mathbb{R}/\mathbb{Z}\) (period \(1\)).

For a lattice field \(\phi^h=(\phi_i)_{i=0}^{N-1}\),

\[
(D_h\phi)_i
\;:=\;
\frac{\phi_{i+1}-\phi_i}{h},
\qquad
G_i^h[\phi^h]
\;:=\;
1+\alpha\,(D_h\phi)_i^2,
\qquad
\alpha>0\text{ fixed}.
\]

**Mesh-weighted discrete action** (Riemann-sum normalization matching \(dx\)):

\[
S_h[\phi^h]
\;:=\;
h\sum_{i=0}^{N-1}
-\ln\bigl(1+\alpha\,(D_h\phi)_i^2\bigr).
\]

**Note:** Unweighted sum \(S_{\mathrm{GfE}}^h=-\sum_i\ln G_i\) used in some joint-toy writeups equals \(S_h/h\). Continuum contact as an **integral** requires the factor \(h\). This note always uses \(S_h\).

### 1.2 Continuum target

For \(\phi:\mathbb{T}^1\to\mathbb{R}\) smooth,

\[
S[\phi]
\;:=\;
\int_{\mathbb{T}^1}
-\ln\bigl(1+\alpha\,(\phi'(x))^2\bigr)\,dx.
\]

This is the 1D Euclidean scalar warm-up density of M5 T4 (\(G=1+\alpha|\phi'|^2\); \(\mathcal{L}=-\ln G\)). External literature identification is **not re-proved** here.

---

## 2. Hypotheses

| Id | Name | Statement |
|----|------|-----------|
| **H1** | Smooth field | \(\phi\in C^3(\mathbb{T}^1)\). Write \(M_k:=\|\phi^{(k)}\|_{L^\infty(\mathbb{T}^1)}\) for \(k=1,2,3\). |
| **H2** | Sampling | Lattice values are point samples: \(\phi_i=\phi(x_i)\), \(x_i=ih\). (Restriction of a fixed smooth \(\phi\) — **not** a sequence of rough lattice fields.) |
| **H3** | Coupling | \(\alpha\in(0,\alpha_{\max}]\) with \(\alpha_{\max}<\infty\) fixed independent of \(h\). |
| **H4** | Mesh | \(h=1/N\to 0\), \(N\ge 2\). |

**Not assumed:** weak compactness of \(\phi^h\), lower semicontinuity of \(S_h\), recovery sequences for non-smooth limits, stochastic observation noise, residual dual inequalities.

---

## 3. Lemma (M5b, conditional)

> **Lemma (M5b, conditional).**  
> *Rigor: elementary FD consistency + Riemann-sum estimate under H1–H4; labeled **lemma sketch**, not Γ-convergence.*
>
> Assume **H1–H4**. There exists a constant
> \[
> C \;=\; C(\alpha,M_1,M_2,M_3)
> \]
> independent of \(h\) (explicitly controllable; see §4) such that, for all \(h\le 1\),
> \[
> \Bigl|\,
> S_h[\phi|_{\mathrm{grid}}]
> \;-\;
> S[\phi]
> \,\Bigr|
> \;\le\;
> C\,h.
> \]
> Explicitly,
> \[
> \Bigl|\,
> h\sum_{i=0}^{N-1}
> -\ln\bigl(1+\alpha\,(D_h\phi)_i^2\bigr)
> \;-\;
> \int_{\mathbb{T}^1}
> -\ln\bigl(1+\alpha\,(\phi'(x))^2\bigr)\,dx
> \,\Bigr|
> \;\le\;
> C\,h.
> \]
> In particular,
> \[
> S_h[\phi|_{\mathrm{grid}}]
> \;\xrightarrow[h\to 0]{}\;
> S[\phi].
> \]
>
> The continuum integrand is the **Euclidean scalar warm-up density** of M5 T4 (Bianconi warm-up / *Beyond holography* language for \(G=1+\alpha|\nabla\phi|^2\)).

**Constant (for \(h\le 1\)):** with \(C_{\nabla}:=M_2/2+M_3/6\),

\[
C
\;=\;
\sqrt{\alpha}\Bigl(C_{\nabla}+M_2\Bigr)
\;=\;
\sqrt{\alpha}\Bigl(\tfrac{3}{2}M_2+\tfrac{1}{6}M_3\Bigr).
\]

---

## 4. Proof sketch

*Sketch only — not a full published proof. Steps are elementary analysis under H1–H4.*

### Step 1 — Taylor consistency of \(D_h\)

By Taylor expansion with remainder, for each \(i\),

\[
\phi(x_i+h)
\;=\;
\phi(x_i)+h\phi'(x_i)+\tfrac{h^2}{2}\phi''(x_i)+\tfrac{h^3}{6}\phi'''(\xi_i)
\]

for some \(\xi_i\in(x_i,x_i+h)\). Hence

\[
(D_h\phi)_i
\;=\;
\phi'(x_i)+\tfrac{h}{2}\phi''(x_i)+\tfrac{h^2}{6}\phi'''(\xi_i),
\]

and

\[
\bigl|(D_h\phi)_i-\phi'(x_i)\bigr|
\;\le\;
\tfrac{h}{2}M_2+\tfrac{h^2}{6}M_3
\;\le\;
h\,C_{\nabla}
\quad(h\le 1),
\qquad
C_{\nabla}
\;:=\;
\tfrac{M_2}{2}+\tfrac{M_3}{6}.
\]

Also \(\lvert(D_h\phi)_i\rvert\le M_1+C_{\nabla}\) for \(h\le 1\).

### Step 2 — Lipschitz density map

Define \(f:\mathbb{R}\to\mathbb{R}\) by \(f(z):=-\ln(1+\alpha z^2)\). Then \(f\in C^\infty(\mathbb{R})\), \(f\le 0\), and

\[
|f'(z)|
\;=\;
\Bigl|\frac{-2\alpha z}{1+\alpha z^2}\Bigr|
\;\le\;
\sqrt{\alpha}
\]

(using \(2|u|/(1+u^2)\le 1\) with \(u=\sqrt{\alpha}\,z\)). Thus \(f\) is **globally** Lipschitz with \(\operatorname{Lip}(f)\le\sqrt{\alpha}\), and

\[
\bigl|f((D_h\phi)_i)-f(\phi'(x_i))\bigr|
\;\le\;
\sqrt{\alpha}\;C_{\nabla}\,h.
\]

Uniformly in \(i\): \(\max_i\lvert f((D_h\phi)_i)-f(\phi'(x_i))\rvert\le C_f h\) with \(C_f:=\sqrt{\alpha}\,C_{\nabla}\).

### Step 3 — Riemann-sum error for the continuum density

Let \(g(x):=f(\phi'(x))\). Under H1, \(g\in C^1(\mathbb{T}^1)\) and \(\|g'\|_\infty\le\sqrt{\alpha}\,M_2\). The rectangular Riemann sum on period \(1\) satisfies

\[
\Bigl|\,
h\sum_{i=0}^{N-1} g(x_i)
-\int_{\mathbb{T}^1} g(x)\,dx
\,\Bigr|
\;\le\;
h\,\|g'\|_\infty
\;\le\;
h\,\sqrt{\alpha}\,M_2
\]

(on each cell \([x_i,x_i+h]\), \(\lvert g(x)-g(x_i)\rvert\le\|g'\|_\infty|x-x_i|\); integrate and sum).

### Step 4 — Triangle inequality

\[
\begin{aligned}
\bigl|S_h-S\bigr|
&\le
\Bigl|\,h\sum_i\bigl(f((D_h\phi)_i)-f(\phi'(x_i))\bigr)\,\Bigr|
+
\Bigl|\,h\sum_i f(\phi'(x_i))-\int f(\phi')\,dx\,\Bigr| \\
&\le
h\cdot N\cdot (C_f h)
\;+\;
h\sqrt{\alpha}\,M_2
\qquad
(hN=1) \\
&=
C_f\,h+\sqrt{\alpha}\,M_2\,h
\;=\;
C\,h,
\end{aligned}
\]

with \(C=\sqrt{\alpha}(C_{\nabla}+M_2)=\sqrt{\alpha}\bigl(\tfrac{3}{2}M_2+\tfrac{1}{6}M_3\bigr)\) for \(h\le 1\). This yields the \(O(h)\) bound and the limit \(h\to 0\).

### Remarks

1. **No claim that \(C\) is sharp.** Centered differences would typically improve gradient error to \(O(h^2)\); toys use forward edges, so we match \(D_h\).  
2. **Composition with \(\ln\)** never degenerates: \(1+\alpha z^2\ge 1\), so \(f\) is smooth on all of \(\mathbb{R}\).  
3. **What fails for jumps:** if \(\phi\) has a jump, \(D_h\phi\sim O(1/h)\) on one edge and \(f((D_h\phi))\sim O(|\ln h|)\); the discrete sum does **not** track the classical continuum integral. BV/jump limits are **out of scope**.

### Optional 2D remark (same rigor class)

On \(\mathbb{T}^2\), mesh-weighted \(h^2\sum f_h\) with isotropic density \(f_h=-\ln\bigl(1+\alpha\bigl((D_h^{(1)}\phi)^2+(D_h^{(2)}\phi)^2\bigr)\bigr)\) converges at rate \(O(h)\) under \(\phi\in C^3(\mathbb{T}^2)\) by the same Taylor + multivariable Riemann argument. Primary formal statement remains 1D. **PM flux consistency** is **not** part of Lemma M5b (see M5 T4 / M5c).

---

## 5. Corollary (paper sentence)

> Under hypotheses H1–H4 (fixed \(C^3\) periodic field, point sampling, fixed \(\alpha>0\), mesh \(h\to 0\)), the mesh-weighted discrete Euclidean warm-up action \(S_h[\phi|_{\mathrm{grid}}]=h\sum_i -\ln\bigl(1+\alpha(D_h\phi)_i^2\bigr)\) approximates the continuum integral \(S[\phi]=\int -\ln\bigl(1+\alpha|\phi'|^2\bigr)\,dx\) with error at most \(C(\alpha,\|\phi'\|_\infty,\|\phi''\|_\infty,\|\phi'''\|_\infty)\,h\); the argument is Taylor consistency of forward differences, global Lipschitz continuity of \(z\mapsto -\ln(1+\alpha z^2)\), and a standard Riemann-sum estimate. This is a **conditional smooth lemma** (Layer W action consistency), not Γ-convergence, not a BV/jump theorem, not residual dual continuum, and not Lorentzian GfE or master-equation contact.

**Continuous dependence (still not Γ):** If \(\phi^{(\varepsilon)}\to\phi\) in \(C^3\) and \(h\to 0\), then \(S_h[\phi^{(\varepsilon)}|_{\mathrm{grid}}]\to S[\phi]\). No claim about minimizing sequences or non-smooth \(\phi\).

---

## 6. Non-claims

> **Non-claims (M5b does *not* assert)**  
>
> 1. **Γ-convergence** of \(S_h\) to \(S\) (or any relaxed functional) on \(H^1\), \(BV\), or SBV — **open** (full T4).  
> 2. **BV / jump continuum limits**, perimeter / interfacial energy, or recovery of jump solutions of continuum PM.  
> 3. **Continuum residual dual** / T1′ as an SPDE inequality; discrete dual windows stay discrete.  
> 4. **Lorentzian GfE**, modified Einstein equations, G-field, \(\Lambda_G\).  
> 5. **Master equation** \(\partial_\tau\rho=\mathcal{L}_g\rho\), \(\Phi_g\), or \(S_c=S(\Phi_g(\rho))\).  
> 6. **\(L\equiv G\)**, continuum limit of load clock as proper time, or \(H_c^{\mathrm{toy}}\equiv S_{\mathrm{GfE}}\).  
> 7. **Newtonian gravity** / Path J/M / M6 identity upgrade from this lemma.  
> 8. **Full Proposition T4** (PM scheme \(+\) Γ-limit \(+\) Sobolev class) — only the **smooth action** slice.  
> 9. **Re-derivation** of Bianconi’s variational identification PM = warm-up gradient flow (external literature).  
> 10. **Empirical gravity** from lattice denoising or joint-toy 6/6 SUPPORT.

---

## 7. Agent abstract checklist

### May write (3)

| # | Allowed sentence | Label |
|---|------------------|-------|
| M1 | For smooth periodic \(\phi\), the mesh-weighted discrete warm-up action \(h\sum -\ln(1+\alpha(D_h\phi)^2)\) converges to \(\int-\ln(1+\alpha|\phi'|^2)\,dx\) at rate \(O(h)\) under H1–H4 (Lemma M5b, conditional). | lemma sketch |
| M2 | This is **consistency of the warm-up action density** for the Euclidean scalar warm-up target — not a proof of continuum gravity. | structural + hygiene |
| M3 | Full lattice→continuum Γ-convergence, jump limits, and residual-dual continuum statements remain **open**; M5b is smooth-only. | honest open |

### Must not write (5)

| # | Forbidden | Replace with |
|---|-----------|--------------|
| N1 | “We prove the continuum / Γ-limit of GfE” | M5b smooth action \(O(h)\) only; T4 Γ open |
| N2 | “Discrete dual implies continuum SPDE dual / gravity” | Layer W action consistency only |
| N3 | “\(L\) converges to metric \(G\)” | \(L\neq G\) always |
| N4 | “Master equation \(\Leftrightarrow\) Bianconi GfE via mesh limit” | explicit non-claim |
| N5 | “Jump / BV / Newton / Lorentzian covered by M5b” | smooth \(\phi\), Euclidean warm-up action only |

---

## 8. Relation and pointers

| File | Role |
|------|------|
| [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) | T4 **target** + literature bridge |
| [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) | Claim language; transfer checklist |
| **This note** | Smooth-only **action** lemma (H1–H4, \(O(h)\), proof sketch) |
| [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) | Dynamics sibling: PM / discrete energy |
| [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) | Transfer dictionary |
| [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) | ACD-EW |
| [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) | Claims freeze |
| [papers/external/README.md](../papers/external/README.md) | External GfE index |

**Does not upgrade:** M6 FAIL identity; Path J/M; ACD-EW residual dual continuum; M10 / M11 continuum contact.

---

*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)  
*Status:* Lemma sketch (D15 polish) — cite from program DRAFT Layer W
