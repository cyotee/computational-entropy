# M1e — Pure E′c: Spectral Freeze-Tax Majorant

**M-id:** M1e (advances pure analytic half of E′c)  
**Status:** **Spectral majorant closed under plateau-conductivity hypothesis Hρ; pure implementation in M1f**  
**Parent:** [m1d-lemma-e-prime.md](m1d-lemma-e-prime.md)  
**Follow-on:** [m1f-hrho-pure-proof.md](m1f-hrho-pure-proof.md) — pure dual on \([2.0,2.4]\) with \(\rho_{\mathrm{eff}}\approx 0.30\)  
**Date:** 2026-07-14

---

## 1. Goal

Replace MC certification of \(\Delta_{\mathrm{noise}}(t)\le R_{\mathrm{blur}}(t)\) by an **explicit spectral majorant** built from the discrete Laplacian of the toy.

---

## 2. Heat noise spectrum (exact)

Let \(A\) be the matrix of the toy operator \(\mathrm{div}\circ\nabla\) (Neumann-type ends; eigenvalues \(\lambda_i\le 0\)). For \(\eta\sim\mathcal{N}(0,\sigma^2 I)\),

\[
R_{\mathrm{noise}}^{\mathrm{heat}}(t)
=
\frac{\sigma^2}{N}\sum_{i=1}^{N} e^{2t\lambda_i}
=
\frac{\sigma^2}{N}\operatorname{Tr}\bigl(e^{2t A}\bigr).
\]

**Verified:** matches Monte Carlo pure-noise heat residual to \(\sim 10^{-5}\) at \(t=1.2,1.6\).

Isotropic heat with constant conductivity \(\rho\in(0,1]\) is the same operator scaled:

\[
R_{\mathrm{noise}}^{(\rho)}(t)
=
\frac{\sigma^2}{N}\sum_{i} e^{2t\rho\lambda_i}
=
R_{\mathrm{noise}}^{\mathrm{heat}}(\rho\, t).
\]

Since \(\lambda_i\le 0\) and \(\rho<1\), \(R_{\mathrm{noise}}^{(\rho)}(t) > R_{\mathrm{noise}}^{\mathrm{heat}}(t)\) for \(t>0\): slower diffusion leaves more noise energy.

---

## 3. Hypothesis Hρ (plateau conductivity)

**Hρ.** On the residual-relevant plateau dynamics up to time \(T_{\mathrm{pers}}^\sharp\), the PM dissipation form satisfies, in expectation (or pathwise on a high-probability event),

\[
\mathbb{E}\sum_e \rho_e |(\nabla\hat\phi)_e|^2
\;\ge\;
\rho_{\mathrm{typ}}\,
\mathbb{E}\sum_e |(\nabla\hat\phi)_e|^2
\quad\text{after removing the single true jump edge},
\]

with the **typical-noise conductivity**

\[
\rho_{\mathrm{typ}}
:=
\frac{1}{1+\bigl(\sigma\sqrt{2}/K\bigr)^2}.
\]

For toy \(\sigma=0.12\), \(K=0.15\):

\[
\sigma\sqrt{2}\approx 0.1697,
\qquad
\rho_{\mathrm{typ}}
\approx
0.4386.
\]

**Interpretation:** edge gradients of pure noise have scale \(\sigma\sqrt{2}\); evaluating \(\rho\) at that scale gives a baseline conductivity. Super-threshold false edges make Hρ **optimistic** (they lower average \(\rho\)); the majorant below is therefore a **conditional** pure bound, not yet unconditional.

**Status of Hρ:** **modeling hypothesis / proved sketch target** — not fully proved. Partial support: most edges have \(|g|=O(\sigma)\); \(P(|g|>2K)\approx 0.077\) per false edge.

---

## 4. Lemma E′c-typ (spectral majorant under Hρ)

**Statement.** Assume Hρ in the form: plateau noise residual under PM is at most the residual of isotropic heat run at conductivity \(\rho_{\mathrm{typ}}\) (equivalently, heat for time \(\rho_{\mathrm{typ}} t\)). On the C′2♯ event, add the interface majorant of M1d. Then

\[
\Delta_{\mathrm{noise}}(t)
\;\le\;
\Delta_{\mathrm{maj}}^{\mathrm{typ}}(t)
:=
R_{\mathrm{noise}}^{\mathrm{heat}}(\rho_{\mathrm{typ}} t)
-
R_{\mathrm{noise}}^{\mathrm{heat}}(t)
+
\frac{2}{N}\left(\frac{K^2 t}{H_{\mathrm{floor}}}\right)^2.
\]

**Proof sketch.**  
1. Split \(\Delta_{\mathrm{noise}}=\Delta_{\mathrm{freeze}}+\Delta_{\mathrm{interface}}+\Delta_{\mathrm{cross}}\).  
2. \(\Delta_{\mathrm{interface}}\le 2\mu(t)^2/N\) with \(\mu\le K^2 t/H_{\mathrm{floor}}\) (M1d E′b).  
3. Under Hρ, \(\mathbb{E}R_{\mathrm{PM}}^{\mathrm{(plateau\,noise)}}\le R_{\mathrm{noise}}^{(\rho_{\mathrm{typ}})}(t)\), while heat’s pure-noise term is \(R_{\mathrm{noise}}^{\mathrm{heat}}(t)\), giving the difference of traces.  
4. Cross terms absorbed into the same interface scale for the toy regime (as in M1d). \(\square\)

---

## 5. Comparison to blur (toy numbers)

Exact \(R_{\mathrm{blur}}(t)\) from heat on \(\phi_\star\); \(\Delta_{\mathrm{maj}}^{\mathrm{typ}}\) from spectrum of \(A\):

| \(t\) | \(R_{\mathrm{blur}}\) | \(\Delta_{\mathrm{maj}}^{\mathrm{typ}}\) | \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{maj}}\)? |
|-------|----------------------|------------------------------------------|-----------------------------------------------|
| 1.20 | 0.00168 | 0.00173 | **No** (thin miss) |
| **1.36** | **0.00182** | **0.00163** | **Yes** |
| 1.44 | 0.00188 | 0.00159 | Yes |
| **1.60** | **0.00201** | **0.00153** | **Yes** |
| 2.00 | 0.00229 | 0.00148 | Yes |
| 3.20 | 0.00296 | 0.00173 | Yes |
| 6.40 | 0.00427 | 0.00405 | Yes |
| 8.00 | 0.00480 | 0.00593 | No (majorant loosens) |

**Corollary under Hρ.** For all Euler grid times

\[
t\in I_\star=\{1.36,1.44,1.52,1.60\}
\]

(and up through at least \(t=6.4\)),

\[
R_{\mathrm{blur}}(t)
\;\ge\;
\Delta_{\mathrm{maj}}^{\mathrm{typ}}(t)
\;\ge\;
\Delta_{\mathrm{noise}}(t)
\quad\Rightarrow\quad
\mathbb{E}R_{\mathrm{PM}}(t)\le\mathbb{E}R_{\mathrm{heat}}(t).
\]

Thus **hybrid T1′ residual domination on \(I_\star\) becomes pure conditional on Hρ**.

---

## 6. Stronger / weaker majorants

| Majorant | Conductivity | Passes \(I_\star\)? | Notes |
|----------|--------------|---------------------|-------|
| **typ** (\(\rho_{\mathrm{typ}}\)) | 0.439 | **Yes** from \(t=1.36\) | Main pure candidate under Hρ |
| 2σ edge (\(\rho_{2\sigma}\approx 0.163\)) | lower | **No** on \(I_\star\) | Too pessimistic |
| Mixture \(p\cdot\sigma^2+(1-p)R^{(\rho)}\) | partial freeze | **No** | Too crude (charges full \(\sigma^2\) on frozen fraction) |
| Empirical \(\Delta_{\mathrm{noise}}\) | — | Yes from \(t=1.20\) | M1d hybrid (MC) |

The **typ** majorant is slightly conservative vs empirical \(\Delta\) at \(t=1.36\) (0.00163 vs emp \(\sim 0.00136\)) but still below blur.

---

## 7. What remains for unconditional pure E′c

| Gap | Approach |
|-----|----------|
| Prove Hρ (or a weaker \(\rho_\star<\rho_{\mathrm{typ}}\) still passing \(I_\star\)) | Truncate super-threshold edges; comparison principle for Euler PM; Dirichlet-form inequalities |
| Control lifetime of false frozen edges | Lemma B + noise decay under \(\rho\approx 1\) on \(|g|<K\) |
| Remove \(\Delta_{\mathrm{cross}}\) handwave | Collar estimate of width \(O(1)\) about \(e_\star\) |

**Status:** M1e **does not** claim unconditional pure T1′. It **does** supply the missing closed-form gap function once Hρ is granted.

---

## 8. Algorithm to recompute majorant

```python
# Build A = div∘grad matrix of the toy; evals = eigvalsh(A)
# R_noise(t, rho) = (sigma**2/N) * sum(exp(2*t*rho*evals))
# R_blur(t) = residual of heat(phi_star, t)
# maj = R_noise(t, rho_typ) - R_noise(t, 1) + 2*(K**2*t/H_floor)**2/N
```

---

## 9. Lemma board update

| Item | After M1d | **After M1e** |
|------|-----------|----------------|
| E′c MC-certified | Yes on \(I_\star\) | unchanged |
| E′c spectral majorant | open | **Closed under Hρ** (\(\rho_{\mathrm{typ}}\)) |
| Hρ | — | **Hypothesis** (main pure gap) |
| Unconditional pure T1′ | open | **Still open** |

---

## 10. One-line takeaway

**M1e:** With the discrete heat spectrum, the freeze tax is majorized by the noise residual of conductivity-\(\rho_{\mathrm{typ}}\) heat minus ordinary heat residual (plus interface); under hypothesis Hρ this pure majorant is **below blur on \(I_\star\)**, converting hybrid T1′ into a **conditional pure** residual dual.

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
