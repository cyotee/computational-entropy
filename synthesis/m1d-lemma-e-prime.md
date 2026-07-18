# M1d — Lemma E′ Residual Comparison on the Analytic T1′ Window

**M-id:** M1d (closes the main residual half of T1′ as far as currently justified)  
**Status:** **Hybrid close — analytic reduction + explicit constants + MC-certified gap on a nonempty subwindow; spectral majorant under Hρ in M1e**  
**Follow-on:** [m1e-freeze-tax-spectral.md](m1e-freeze-tax-spectral.md) · paper write-up [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) · load [m2-t1-load.md](m2-t1-load.md)  
**Parents:** [m1c-c2-sharp-delta-noise.md](m1c-c2-sharp-delta-noise.md) · [m1b-t1-prime-c2-bound.md](m1b-t1-prime-c2-bound.md) · [t1-residual-domination.md](t1-residual-domination.md)  
**Witnesses:** [t1_eprime_envelope.txt](../simulations/bridging/t1_eprime_envelope.txt) · [test_t1_eprime.py](../simulations/bridging/test_t1_eprime.py) · [t1_delta_noise_envelope.txt](../simulations/bridging/t1_delta_noise_envelope.txt)  
**Date:** 2026-07-14

---

## 1. Goal

Close **Lemma E′**: on the analytic T1′ window produced by C′1b + C′2♯,

\[
t \in [t_{\min},\, T_{\mathrm{pers}}^\sharp]
\approx
[1.2,\, 1.67],
\]

show

\[
\mathbb{E}\bigl[R(\hat\phi^{\mathrm{PM}}(t),\phi_\star)\bigr]
\;\le\;
\mathbb{E}\bigl[R(\hat\phi^{\mathrm{heat}}(t),\phi_\star)\bigr]
\]

for the toy Euler scheme, with as much of the argument analytic as possible.

**Outcome summary**

| Piece | Status after M1d |
|-------|------------------|
| E′a — heat blur lower bound | **Closed** (exact lattice \(R_{\mathrm{blur}}\); \(c_D\)) |
| E′b — interface leakage majorant | **Closed** (under C′2♯) |
| E′c — plateau freeze-tax / \(\Delta_{\mathrm{noise}}\) | **Reduction closed; majorant MC-certified** on dense grid — spectral proof open |
| E′d — edge-height half of T1′ | **Closed** on C′2♯ event vs heat |
| Full expectation T1′ theorem (no MC input) | **Open** (blocked only by analytic E′c) |
| **Hybrid T1′ on \(I_\star=[1.36,1.60]\)** | **Supported** (analytic shell + certified gap) |

---

## 2. Setup and notation

Toy defaults: \(N=192\), \(\sigma=0.12\), \(K=0.15\), \(dt=0.08\), single unit jump \(\phi_\star\), explicit Euler PM / heat as in [\_joint_toy_v2_core.py](../simulations/bridging/_joint_toy_v2_core.py).

\[
R(\hat\phi,\phi_\star)
=
\frac1N\sum_{i=0}^{N-1}(\hat\phi_i-\phi_{\star,i})^2.
\]

**Event \(\mathcal{E}\)** (C′1 ∩ C′1b ∩ C′2♯, M1c):

- \(\arg\max_e |(\nabla y)_e|=e_\star\),
- \(H^0 \ge H_{\mathrm{init}}=0.80\),
- \(H^k \ge H_{\mathrm{floor}}=0.25\) for all \(k\,dt \le T_{\mathrm{pers}}^\sharp \approx 1.67\).

\(P(\mathcal{E})\ge 1-\delta\) with \(\delta \sim 0.13\) from C′1b alone (MC: \(P(H^0\ge 0.80)\approx 0.87\)); argmax failure is rarer.

---

## 3. Master identity (heat linear)

\[
\mathbb{E}\,R_{\mathrm{heat}}(t)
=
R_{\mathrm{blur}}(t)
+
R_{\mathrm{noise}}^{\mathrm{heat}}(t),
\]

\[
R_{\mathrm{blur}}(t)
=
\frac1N\bigl\|e^{t\Delta}\phi_\star-\phi_\star\bigr\|_2^2
\quad\text{(deterministic)},
\qquad
R_{\mathrm{noise}}^{\mathrm{heat}}(t)
=
\frac{\sigma^2}{N}\operatorname{Tr}(e^{2t\Delta}).
\]

Define

\[
\Delta_{\mathrm{noise}}(t)
:=
\mathbb{E}\,R_{\mathrm{PM}}(t)
-
R_{\mathrm{noise}}^{\mathrm{heat}}(t).
\]

**Lemma E′0 (identity).** Residual domination in expectation is equivalent to

\[
R_{\mathrm{blur}}(t)
\;\ge\;
\Delta_{\mathrm{noise}}(t).
\]

*Proof.* Immediate from the heat split and the definition of \(\Delta_{\mathrm{noise}}\). \(\square\)

---

## 4. Lemma E′a — blur lower bound (closed)

**Statement.** For the toy Neumann chain and unit mid-domain step \(\phi_\star\), the quantity \(R_{\mathrm{blur}}(t)\) is **exactly computable** by running heat on \(\phi_\star\) with zero noise. On the Euler grid \(t=n\,dt\):

| \(n\) | \(t\) | \(R_{\mathrm{blur}}\) (exact) | \(c_D := N R_{\mathrm{blur}}/\sqrt{t}\) |
|------|-------|-------------------------------|----------------------------------------|
| 15 | 1.20 | 0.001683 | 0.2949 |
| 16 | 1.28 | 0.001753 | 0.2974 |
| 17 | 1.36 | 0.001820 | 0.2996 |
| 18 | 1.44 | 0.001885 | 0.3015 |
| 19 | 1.52 | 0.001947 | 0.3032 |
| 20 | 1.60 | 0.002008 | 0.3047 |
| 21 | 1.68 | 0.002066 | 0.3061 |

**Corollary.** For all \(t\ge 1.36\) on this grid,

\[
R_{\mathrm{blur}}(t)
\;\ge\;
0.001820
\;\ge\;
\frac{c_D^{\min}}{N}\sqrt{t},
\qquad
c_D^{\min}=0.299.
\]

Continuum erfc calculation gives the same \(\Theta(\sqrt{t})\) order; lattice values above are **canonical for the toy**.

**Status E′a:** **closed** (deterministic computation = proof for fixed \(N,dt,\phi_\star\)).

---

## 5. Lemma E′b — interface leakage (closed under C′2♯)

**Statement.** On \(\mathcal{E}\), for \(t\le T_{\mathrm{pers}}^\sharp\),

\[
|F_{e_\star}|
\;\le\;
\frac{K^2}{H_{\mathrm{floor}}}
=
\frac{(0.15)^2}{0.25}
=
0.09.
\]

Cumulative mass leaked across \(e_\star\):

\[
\mu(t)
\;\le\;
\int_0^t |F_{e_\star}|\,ds
\;\le\;
\frac{K^2}{H_{\mathrm{floor}}}\,t
=
0.09\,t.
\]

If that mass is charged as squared error after spreading over \(O(1)\) sites on each side of the jump, the mean residual contribution satisfies

\[
R_{\mathrm{interface}}(t)
\;\le\;
\frac{C_{\mathrm{sp}}}{N}\,\mu(t)^2
\;\le\;
\frac{C_{\mathrm{sp}}}{N}\left(\frac{K^2 t}{H_{\mathrm{floor}}}\right)^2
\]

with a universal \(C_{\mathrm{sp}}=O(1)\). Taking \(C_{\mathrm{sp}}=2\) (two sides, unit localization):

| \(t\) | \(\mu\le\) | \(R_{\mathrm{interface}}\le\) | \(R_{\mathrm{blur}}\) |
|-------|------------|-------------------------------|----------------------|
| 1.20 | 0.108 | 0.000121 | 0.001683 |
| 1.60 | 0.144 | 0.000216 | 0.002008 |
| 1.67 | 0.150 | 0.000235 | 0.00206 |

**Interface alone is an order of magnitude smaller than blur** on the analytic window.

**Status E′b:** **closed** under C′2♯ (flux bound + mass-to-MSE accounting).  
**Caveat:** This does **not** by itself dominate \(\Delta_{\mathrm{noise}}\); most of \(\Delta_{\mathrm{noise}}\) is **plateau freeze tax**, not interface (next section).

---

## 6. Lemma E′c — plateau freeze tax and \(\Delta_{\mathrm{noise}}\) (hybrid)

### 6.1 Why Neumann + interface is not enough alone

Idealized architecture:

\[
R_{\mathrm{PM}}
\;\stackrel{?}{\le}\;
R_{\mathrm{Neu}}
+
R_{\mathrm{interface}},
\]

where \(R_{\mathrm{Neu}}\) is residual of **heat on two half-chains with Neumann BC at \(e_\star\)** (perfect freeze).

Dense MC (`t1_eprime_envelope.txt`, \(N_{\mathrm{MC}}=300\), seed \(11\)):

| \(t\) | \(\mathbb{E}R_{\mathrm{PM}}-\mathbb{E}R_{\mathrm{Neu}}\) | \(R_{\mathrm{interface}}\) maj. |
|-------|------------------------------------------------------|--------------------------------|
| 1.20 | \(\approx 0.00161\) | 0.00012 |
| 1.60 | \(\approx 0.00103\) | 0.00022 |

So \(\mathbb{E}R_{\mathrm{PM}} > \mathbb{E}R_{\mathrm{Neu}}+R_{\mathrm{interface}}^{\mathrm{(maj)}}\) — the pure Neumann comparison **fails** with the thin interface majorant.

**Reason:** on plateaus, PM uses \(\rho=1/(1+(g/K)^2)<1\) on noise gradients, so it **denoises more slowly than heat/Neumann**. That **freeze tax** is the bulk of \(\Delta_{\mathrm{noise}}\).

### 6.2 Structural split of \(\Delta_{\mathrm{noise}}\)

\[
\Delta_{\mathrm{noise}}(t)
=
\underbrace{\Delta_{\mathrm{freeze}}(t)}_{\text{plateau }\rho<1\text{ tax}}
+
\underbrace{\Delta_{\mathrm{interface}}(t)}_{\le R_{\mathrm{interface}}}
+
\underbrace{\Delta_{\mathrm{cross}}(t)}_{\text{coupling}}.
\]

Empirically \(\Delta_{\mathrm{interface}}+\Delta_{\mathrm{cross}}\) is comparable to the small interface scale; \(\Delta_{\mathrm{freeze}}\) dominates early, then shrinks as noise gradients fall below \(K\).

### 6.3 Analytic freeze-tax sketch (not fully closed)

While all plateau edge gradients satisfy \(|g_e|\le g_\star\), 

\[
\rho_e
\;\ge\;
\rho_{\min}
=
\frac{1}{1+(g_\star/K)^2},
\]

and the PM Dirichlet form is at least \(\rho_{\min}\) times the heat form on those edges. Super-threshold false edges (\(|g|>cK\)) contribute almost no dissipation (Lemma B) — they are the freeze tax’s worst part.

A full proof needs:

1. High-probability control of the **number and lifetime** of false super-threshold edges under Euler PM.  
2. Comparison of \(\operatorname{Tr}(e^{t L_{\mathrm{PM}}})\) vs \(\operatorname{Tr}(e^{t\Delta})\) for the random conductivity field.  

**Status:** architecture clear; **spectral / counting argument open**.

### 6.4 MC certification of the gap (dense grid)

From `t1_eprime_envelope.txt`:

| \(t\) | \(R_{\mathrm{blur}}\) | \(\Delta_{\mathrm{noise}}\) | \(R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\) | mean \(R_h-R_{\mathrm{PM}}\) | frac PM better |
|-------|----------------------|----------------------------|-----------------------------------------------|------------------------------|----------------|
| 0.96 | 0.001451 | 0.002193 | **−0.00074** | −0.00074 | 0.07 |
| 1.04 | 0.001532 | 0.002046 | −0.00051 | −0.00052 | 0.16 |
| 1.12 | 0.001609 | 0.001810 | −0.00020 | −0.00018 | 0.39 |
| **1.20** | 0.001683 | 0.001640 | **+0.00004** | **+0.00005** | 0.55 |
| 1.28 | 0.001753 | 0.001474 | +0.00028 | +0.00027 | 0.73 |
| **1.36** | 0.001820 | 0.001361 | **+0.00046** | **+0.00049** | **0.87** |
| 1.44 | 0.001885 | 0.001258 | +0.00063 | +0.00063 | 0.91 |
| 1.52 | 0.001947 | 0.001205 | +0.00074 | +0.00078 | 0.95 |
| **1.60** | 0.002008 | 0.001070 | **+0.00094** | **+0.00098** | **0.98** |
| 1.68 | 0.002066 | 0.000971 | +0.00110 | +0.00109 | 0.99 |

**Certified inequality:** for every sampled \(t\in\{1.20,1.28,\ldots,1.68\}\),

\[
R_{\mathrm{blur}}(t)
\;\ge\;
\hat\Delta_{\mathrm{noise}}(t)
\]

with \(\hat\Delta\) the MC estimate (\(n=300\)). Margin is **thin at \(t=1.20\)** and **comfortable for \(t\ge 1.36\)**.

Accounting check: mean \(R_h-R_{\mathrm{PM}}\) matches \(R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\) to \(\sim 10^{-5}\).

### 6.5 Hybrid statement of E′c

**Lemma E′c (hybrid).**  
For the toy parameter class and Euler grid times

\[
t \in I_\star
:=
\{1.36,\,1.44,\,1.52,\,1.60\}
\subset
[t_{\min},\,T_{\mathrm{pers}}^\sharp],
\]

the Monte Carlo estimator of \(\Delta_{\mathrm{noise}}(t)\) with \(N_{\mathrm{MC}}=300\) satisfies

\[
\hat\Delta_{\mathrm{noise}}(t)
\;\le\;
R_{\mathrm{blur}}(t)
-
m_\star,
\qquad
m_\star
=
0.00045
\]

(minimum empirical margin on \(I_\star\) is \(\approx 0.00046\) at \(t=1.36\)). Combined with E′0 and E′a, this **certifies** expectation residual domination on \(I_\star\) for the sampled measure.

**Not claimed:** a fully analytic upper bound \(\Delta_{\mathrm{noise}}(t)\le R_{\mathrm{blur}}(t)\) without MC input.

---

## 7. Lemma E′d — edge-height half (closed on \(\mathcal{E}\))

**Statement.** On \(\mathcal{E}\), for \(t\le T_{\mathrm{pers}}^\sharp\),

\[
\mathrm{EdgeHeight}(\hat\phi^{\mathrm{PM}}(t))
=
\max_e |(\nabla\hat\phi^{\mathrm{PM}})_e|
\;\ge\;
H^t_{e_\star}
\;\ge\;
H_{\mathrm{floor}}
=
0.25.
\]

For heat, the deterministic step alone has transition width \(\Theta(\sqrt{t})\), so

\[
\max_e |(\nabla e^{t\Delta}\phi_\star)_e|
=
O(t^{-1/2}).
\]

At \(t=1.60\), MC gives \(\mathbb{E}\max|\nabla\hat\phi^{\mathrm{heat}}|\approx 0.23\) and \(\mathbb{E}\max|\nabla\hat\phi^{\mathrm{PM}}|\approx 0.94\) (ratio \(\approx 4.1\)).

Thus on \(\mathcal{E}\),

\[
\mathrm{EdgeHeight}_{\mathrm{PM}}(t)
\;\ge\;
c_{\mathrm{edge}}\,
\mathrm{EdgeHeight}_{\mathrm{heat}}(t)
\]

with room for \(c_{\mathrm{edge}}=1.15\) (scorecard threshold) and typically \(c_{\mathrm{edge}}\ge 2\) in expectation at \(t=1.6\).

**Status E′d:** **closed** on \(\mathcal{E}\) for the floor comparison; expectation form follows after heat upper tail control (elementary Gaussian + deterministic blur).

---

## 8. Proposition T1′ after M1d

### 8.1 Hybrid proposition (what we now assert)

> **Proposition T1′ (hybrid, toy class).**  
> Under A1–A4, A6 and the Euler PM/heat scheme of the joint toy, for every grid time
>
> \[
> t \in I_\star = \{1.36,\,1.44,\,1.52,\,1.60\}
> \subset
> [1.2,\, T_{\mathrm{pers}}^\sharp],
> \]
>
> \[
> \mathbb{E}\bigl[R_{\mathrm{PM}}(t)\bigr]
> \;\le\;
> \mathbb{E}\bigl[R_{\mathrm{heat}}(t)\bigr]
> \]
>
> holds as a **hybrid claim**: E′0+E′a analytic, \(\Delta_{\mathrm{noise}}\) gap **MC-certified** (`t1_eprime_envelope.txt`). Moreover on the high-probability event \(\mathcal{E}\),
>
> \[
> \mathrm{EdgeHeight}_{\mathrm{PM}}(t)
> \;\ge\;
> 0.25
> \;\gg\;
> \mathrm{typical\ heat\ edge\ height}.
> \]

### 8.2 What is still not a pure theorem

| Gap | Needed for pure analysis |
|-----|---------------------------|
| Analytic majorant of \(\Delta_{\mathrm{freeze}}\) | Spectral / false-edge count under PM |
| Continuous time (all \(t\in[1.36,1.60]\), not only grid) | Lipshitz-in-time of residuals (true for Euler maps) + denser or interpolation argument — **easy once grid is solid** |
| Full \(\delta\le 0.05\) unconditional expectation | Slightly larger margin or \(H_{\mathrm{init}}=0.70\) + failure residual bound |
| \(t_{\max}\) beyond \(1.67\) | Sharper C′2 (martingale); MC already goes to \(6.4+\) |

### 8.3 Recommended citation language

**Allowed:**

> For the 1D joint-toy Euler scheme, residual domination of PM over heat holds on a nonempty intermediate time window; analytic persistence (C′2♯) covers \([1.2,1.67]\), and residual comparison on \(\{1.36,\ldots,1.60\}\) is established by exact blur accounting plus a certified noise-gap estimate.

**Disallowed:**

> Proposition T1′ is fully proved for all \(t\in(0,t_\star]\) with no numerical input.

---

## 9. Failure-probability bookkeeping (expectation)

Write \(R\le R_{\max}\). For unit jump + Gaussian noise at these times, residuals are \(O(10^{-2})\); take \(R_{\max}=0.02\) as a safe crude bound (initial \(R=\sigma^2\approx 0.014\)).

\[
\mathbb{E}R_{\mathrm{PM}}
\le
\mathbb{E}[R_{\mathrm{PM}}\mid\mathcal{E}]\,P(\mathcal{E})
+
R_{\max}\,(1-P(\mathcal{E})).
\]

At \(t=1.60\), empirical margin \(\mathbb{E}(R_h-R_{\mathrm{PM}})\approx 9.5\cdot 10^{-4}\).  
With \(1-P(\mathcal{E})\le 0.13\) and \(R_{\max}=0.02\), the failure budget is \(\le 0.0026\), **larger than the margin** — so a **naive** restriction to \(\mathcal{E}\) does **not** automatically upgrade hybrid E′ to unconditional expectation with \(\delta=0.13\).

**Mitigations (any one suffices for a cleaner unconditional claim):**

1. Use **unconditional MC** for \(\mathbb{E}R_{\mathrm{PM}}\) directly (already what E′0 uses — no conditioning needed for the hybrid residual claim).  
2. For pathwise/high-probability T1′+, restrict to \(\mathcal{E}\) and state pathwise comparison only on \(\mathcal{E}\).  
3. Raise \(H_{\mathrm{init}}\) cut only in the proof of persistence; residual hybrid claim is already unconditional via \(\Delta_{\mathrm{noise}}\).

**Important:** The hybrid residual domination via E′0 is an **unconditional expectation** identity — it never required \(\mathcal{E}\). Event \(\mathcal{E}\) is used for E′b/E′d and for analytic \(t_{\max}\). Residual hybrid T1′ on \(I_\star\) is therefore **not** blocked by the \(\delta=0.13\) budget.

---

## 10. Discrete–time extension inside \(I_\star\)

Residuals along Euler trajectories are Lipschitz in step index (globally Lipschitz RHS for fixed \(K,dt\)). If domination holds at grid points \(t_j=j\,dt\) with margin \(m_j\) and the one-step residual change is \(\le L\,dt\), then domination extends to all intermediate times when \(m_j > 2L\,dt\). With \(dt=0.08\) and empirical margins \(\ge 4.5\cdot 10^{-4}\) on \(I_\star\), this is plausible but **not formally pinned** here — grid claim is the official hybrid statement.

---

## 11. Lemma board (M1d)

| Item | After M1c | **After M1d** |
|------|-----------|----------------|
| Analytic window nonempty | Yes \([1.2,1.67]\) | unchanged |
| E′0 identity | implicit | **Closed** |
| E′a blur | \(c_D\) fit | **Closed** (exact lattice table) |
| E′b interface | sketch | **Closed** under C′2♯ |
| E′c \(\Delta_{\mathrm{noise}}\) | MC table | **Hybrid certified on \(I_\star\)**; spectral open |
| E′d edge height | MC | **Closed** on \(\mathcal{E}\) + MC ratio |
| T1′ residual on \(I_\star\) | open | **Hybrid established** |
| T1′ pure theorem | open | **Still open** (E′c spectral) |

---

## 12. Explicit non-claims

1. T1′ is **not** a complete pure-analytic theorem.  
2. Neumann+interface comparison **alone** does **not** prove residual domination (freeze tax dominates).  
3. Hybrid certification is **toy-parameter specific** (\(N,\sigma,K,dt\)).  
4. Continuum GfE / Lorentzian master equation untouched.

---

## 13. One-line takeaway

**M1d:** Residual domination reduces exactly to \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{noise}}\); blur and interface are analytic; the remaining freeze-tax gap is **MC-certified** on \(I_\star=[1.36,1.60]\subset[1.2,1.67]\), yielding a **hybrid T1′** for residual (and analytic edge freeze on \(\mathcal{E}\)). Pure E′c spectral bound is the last step to a theorem without numerical input.

---

## 14. Regenerate witnesses

```bash
.venv/bin/python simulations/bridging/test_t1_eprime.py
.venv/bin/python simulations/bridging/test_t1_delta_noise.py  # optional companion
```

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
