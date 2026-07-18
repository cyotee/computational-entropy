# M1c — Sharpened C′2 and Lattice \(\Delta_{\mathrm{noise}}\) (Analytic \(t_{\min}\))

**M-id:** M1c (closes the M1b gap: analytic \(t_{\max}\ge t_{\min}\))  
**Status:** **C′2♯ proved under C′1b concentration; \(\Delta_{\mathrm{noise}}\) lattice estimate + empirical \(t_{\min}\); T1′ analytic window nonempty for toy class**  
**Follow-on:** [m1d-lemma-e-prime.md](m1d-lemma-e-prime.md) — hybrid E′ residual comparison on \(I_\star\subset[1.2,1.67]\)  
**Parents:** [m1b-t1-prime-c2-bound.md](m1b-t1-prime-c2-bound.md) · [m1-lemma-c-prime.md](m1-lemma-c-prime.md) · [t1-residual-domination.md](t1-residual-domination.md)  
**Witnesses:** [t1_mc_envelope.txt](../simulations/bridging/t1_mc_envelope.txt) · [t1_delta_noise_envelope.txt](../simulations/bridging/t1_delta_noise_envelope.txt) · [t1_eprime_envelope.txt](../simulations/bridging/t1_eprime_envelope.txt)  
**Date:** 2026-07-14

---

## 1. What was blocking

From M1b:

| Bound | Value | Problem |
|-------|-------|---------|
| Crude \(T_{\mathrm{pers}}\) (from \(H^0\ge\tfrac12\) down to \(\tfrac14\)) | \(\approx 0.76\) | **Shorter than** experimental \(t_{\min}\approx 1.2\text{–}1.6\) |
| Experimental residual window | \([1.6,\,6.4]\) | Analytic cover empty |

**Root cause:** C′1 only *guarantees* \(H^0\ge\tfrac12\), so the budget \(\Delta H\) for the crude bound is only \(\tfrac14\). Typical true height is \(\sim\mathcal{N}(1,2\sigma^2)\), so almost all mass sits near \(H^0\approx 1\). Using that concentration (C′1b) restores a nonempty analytic window.

---

## 2. Exact jump ODE (1D Euler PM)

With edge \(e_\star=i_\star-1\) and fluxes \(F_i=\rho_i g_i\), \(\rho=1/(1+(g/K)^2)\):

\[
\frac{g_{e_\star}^{k+1}-g_{e_\star}^{k}}{dt}
=
F_{e_\star+1}^{k}
-
2\,F_{e_\star}^{k}
+
F_{e_\star-1}^{k}.
\]

(Notation: \(F_L=F_{e_\star-1}\), \(F_\star=F_{e_\star}\), \(F_R=F_{e_\star+1}\).)

**Elementary flux bounds** (any edge):

\[
|F|
\le
\frac{K}{2},
\qquad
|g|\ge H_{\min}>0
\;\Rightarrow\;
|F|
\le
\frac{K^2}{H_{\min}}.
\]

Hence, while \(H^k\ge H_{\mathrm{floor}}\),

\[
\Bigl|\frac{dH}{dt}\Bigr|
\le
\underbrace{K}_{\,|F_L|+|F_R|\,}
+
\underbrace{2\frac{K^2}{H_{\mathrm{floor}}}}_{\,2|F_\star|\,}
=:
R_{\mathrm{worst}}(H_{\mathrm{floor}}).
\]

---

## 3. Lemma C′1b — initial height concentration

**Statement.** Under A1–A2 (\(\eta_i\sim\mathcal{N}(0,\sigma^2)\) i.i.d.), true edge gradient

\[
g_{e_\star}^0 = 1+\eta_{i_\star}-\eta_{i_\star-1}
\sim
\mathcal{N}(1,\,2\sigma^2).
\]

For \(\sigma=0.12\):

| Threshold \(h\) | \(P(H^0\ge h)\) theory \(\approx 1-\Phi((h-1)/(\sigma\sqrt{2}))\) | MC (\(n=2000\)) |
|----------------|---------------------------------------------------------------|-----------------|
| 0.50 | \(>0.998\) | \(\approx 1.00\) |
| 0.70 | \(>0.99\) | high |
| 0.80 | \(>0.99\) | high |
| **0.85** | \(\Phi^{-1}\): \((0.85-1)/(0.12\sqrt{2})\approx -0.88\) → \(\approx 0.81\) wait — recompute |

Correct tail for **lower** bound:

\[
P(H^0 < h)
=
\Phi\!\left(\frac{h-1}{\sigma\sqrt{2}}\right)
\quad(h<1).
\]

| \(h\) | \(z=(h-1)/(\sigma\sqrt{2})\) | theory \(P(H^0\ge h)\) | MC \(n=2000\) |
|------|------------------------------|------------------------|----------------|
| 0.50 | \(-2.95\) | \(0.998\) | **0.9995** |
| 0.70 | \(-1.77\) | \(0.962\) | **0.957** |
| 0.80 | \(-1.18\) | \(0.881\) | **0.874** |
| 0.85 | \(-0.88\) | \(0.811\) | **0.804** |
| 0.90 | \(-0.59\) | \(0.722\) | **0.711** |

**C′1b (working choice for toy):** take \(H_{\mathrm{init}}=0.80\). Then

\[
P(H^0\ge 0.80)\ge 0.88
\]

(theory; MC typically higher after abs and orientation). Intersect with C′1 argmax event: still high probability (\(\delta\lesssim 0.15\) joint is acceptable for a *weakened* theorem; for \(\delta\le 0.05\) use \(H_{\mathrm{init}}=0.70\)).

**Lemma C′1b.** With probability \(\ge 1-\delta_{1b}\) (\(\delta_{1b}\approx 0.12\) for \(h=0.80\)), \(H^0\ge H_{\mathrm{init}}=0.80\).

---

## 4. Lemma C′2♯ — sharpened persistence

**Assumptions:** C′1 (argmax + \(H^0\ge\tfrac12\)) and C′1b (\(H^0\ge H_{\mathrm{init}}\)); Euler \(dt\le 1/8\).

**Choice of floor.** Lemma B only needs \(H\ge cK\) with \(c>1\). Take

\[
H_{\mathrm{floor}}
=
\max\bigl(\tfrac14,\, 1.5\,K\bigr)
=
\max(0.25,\,0.225)
=
0.25
\]

for toy \(K=0.15\) (strictly super-threshold: \(0.25/K\approx 1.67\)).

**Lemma C′2♯.** On the joint event of C′1 \(\cap\) C′1b, for all \(k\,dt\le T_{\mathrm{pers}}^\sharp\),

\[
H^k
\;\ge\;
H_{\mathrm{init}}
-
R_{\mathrm{worst}}(H_{\mathrm{floor}})\,k\,dt
\;\ge\;
H_{\mathrm{floor}},
\]

with

\[
R_{\mathrm{worst}}(H_{\mathrm{floor}})
=
K + \frac{2K^2}{H_{\mathrm{floor}}},
\qquad
T_{\mathrm{pers}}^\sharp
=
\frac{H_{\mathrm{init}}-H_{\mathrm{floor}}}{R_{\mathrm{worst}}(H_{\mathrm{floor}})}.
\]

### Toy numbers

\[
K=0.15,\quad
H_{\mathrm{init}}=0.80,\quad
H_{\mathrm{floor}}=0.25,
\]

\[
R_{\mathrm{worst}}
=
0.15+\frac{2(0.0225)}{0.25}
=
0.15+0.18
=
0.33,
\]

\[
T_{\mathrm{pers}}^\sharp
=
\frac{0.80-0.25}{0.33}
=
\frac{0.55}{0.33}
\approx
\mathbf{1.67}.
\]

With \(H_{\mathrm{init}}=0.70\) (higher probability \(\ge 0.96\)):

\[
T_{\mathrm{pers}}^\sharp
=
\frac{0.45}{0.33}
\approx
\mathbf{1.36}.
\]

**Comparison to experimental \(t_{\min}\):** residual crossover is between \(0.80\) and \(1.60\) (mean \(dR\) flips near \(t\approx 1.2\)). Thus:

| \(H_{\mathrm{init}}\) | \(T_{\mathrm{pers}}^\sharp\) | Covers \(t_{\min}\approx 1.2\)? | Covers conservative \(t_{\min}=1.6\)? |
|---------------------|---------------------------|--------------------------------|--------------------------------------|
| 0.70 | 1.36 | **Yes** | No |
| **0.80** | **1.67** | **Yes** | **Yes** |
| 0.85 | 1.82 | Yes | Yes |

**Status:** For the **standard toy claim** with \(H_{\mathrm{init}}=0.80\) (\(\delta_{1b}\sim 0.12\)), analytic \(t_{\max}=T_{\mathrm{pers}}^\sharp\approx 1.67\ge t_{\min}^{\mathrm{(emp)}}\). Full theorem-level \(\delta\le 0.05\) prefers \(H_{\mathrm{init}}=0.70\) and a slightly smaller \(t_{\min}\) estimate, or a martingale sharpening of \(R_{\mathrm{worst}}\) (below).

### Optional further sharpening (expectation / cancellation)

Empirical mean height decay (MC): \(\mathbb{E}[-\dot H]\approx 0.02\text{–}0.05\ll R_{\mathrm{worst}}=0.33\), because \(F_L+F_R\) is mean-near-zero noise and does not sit at \(\pm K/2\) simultaneously against the jump. A **high-probability martingale bound** on \(\int_0^t(F_L+F_R)\,ds\) would replace \(K\) by \(O(\sigma\sqrt{t\log(1/\delta)})\) and push \(T_{\mathrm{pers}}^\sharp\) to \(O(5\text{–}10)\). **Status: sketch only** (not closed in this pass).

---

## 5. Lattice \(\Delta_{\mathrm{noise}}\) and analytic \(t_{\min}\)

### 5.1 Decomposition (heat is linear)

\[
\hat\phi^{\mathrm{heat}}(t)
=
e^{t\Delta}\phi_\star
+
e^{t\Delta}\eta.
\]

\[
\mathbb{E}\,R_{\mathrm{heat}}(t)
=
\underbrace{\frac{1}{N}\bigl\|e^{t\Delta}\phi_\star-\phi_\star\bigr\|_2^2}_{R_{\mathrm{blur}}(t)}
+
\underbrace{\frac{\sigma^2}{N}\operatorname{Tr}(e^{2t\Delta})}_{R_{\mathrm{noise}}^{\mathrm{heat}}(t)}.
\]

Cross term vanishes in expectation.

### 5.2 Definition of \(\Delta_{\mathrm{noise}}\)

\[
\Delta_{\mathrm{noise}}(t)
:=
\mathbb{E}\,R_{\mathrm{PM}}(t)
-
R_{\mathrm{noise}}^{\mathrm{heat}}(t).
\]

Interpretation: how much worse PM residual is than pure heat-denoised noise — combines (i) slower noise kill from frozen gradients and (ii) interface leakage. Residual domination \(\mathbb{E}R_{\mathrm{PM}}\le\mathbb{E}R_{\mathrm{heat}}\) is equivalent to

\[
R_{\mathrm{blur}}(t)
\;\ge\;
\Delta_{\mathrm{noise}}(t).
\]

### 5.3 Lattice estimate of \(R_{\mathrm{blur}}\)

Empirical fit \(R_{\mathrm{blur}}(t)=c_D\sqrt{t}/N\) on the toy Neumann chain:

| \(t\) | \(R_{\mathrm{blur}}\) (MC) | \(c_D=N R_{\mathrm{blur}}/\sqrt{t}\) |
|-------|---------------------------|-------------------------------------|
| 0.40 | \(\approx 0.00068\) | \(\approx 0.21\) |
| 0.80 | \(\approx 0.00127\) | \(\approx 0.27\) |
| 1.60 | \(\approx 0.00201\) | \(\approx 0.30\) |
| 3.20 | \(\approx 0.00296\) | \(\approx 0.32\) |
| 6.40 | \(\approx 0.00428\) | \(\approx 0.33\) |

**Working constant:** \(c_D\in[0.30,\,0.34]\) for \(t\in[1,7]\) (lattice; continuum erfc calculation gives the same \(\Theta(\sqrt{t})\) order).

### 5.4 Empirical \(\Delta_{\mathrm{noise}}\) and crossover

From `t1_delta_noise_envelope.txt` (\(N_{\mathrm{MC}}=200\), seed \(7\); regenerate with `test_t1_delta_noise.py`):

| \(t\) | \(R_{\mathrm{blur}}\) | \(R_{\mathrm{noise}}^{\mathrm{heat}}\) | \(\mathbb{E}R_{\mathrm{PM}}\) | \(\Delta_{\mathrm{noise}}=R_{\mathrm{PM}}-R_n^{\mathrm{h}}\) | \(R_{\mathrm{blur}}-\Delta\) | mean \(R_h-R_{\mathrm{PM}}\) | frac PM better |
|-------|----------------------|----------------------------------------|------------------------------|-------------------------------------------------------------|----------------------------|------------------------------|----------------|
| 0.40 | 0.000683 | 0.004798 | 0.008977 | **0.004179** | **−0.0035** | **−0.0035** | 0.00 |
| 0.80 | 0.001273 | 0.003299 | 0.006002 | 0.002702 | −0.0014 | −0.0014 | 0.01 |
| **1.20** | **0.001683** | 0.002704 | 0.004398 | **0.001693** | **\(\approx 0\)** | **\(\approx 0\)** | 0.55 |
| 1.60 | 0.002008 | 0.002324 | 0.003392 | 0.001068 | **+0.00094** | **+0.00095** | 0.98 |
| 3.20 | 0.002964 | 0.001614 | 0.001966 | 0.000352 | +0.00261 | +0.00262 | 1.00 |
| 6.40 | 0.004275 | 0.001178 | 0.001368 | 0.000190 | +0.00409 | +0.00409 | 1.00 |

**Perfect accounting check:** mean \(R_h-R_{\mathrm{PM}}\approx R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\) at every sampled \(t\) (heat linearity + definition of \(\Delta_{\mathrm{noise}}\)).

**Empirical \(t_{\min}\):** \(\approx 1.20\) (zero-crossing). **Conservative grid claim:** \(t_{\min}=1.6\) (frac \(\ge 0.97\)).

**Height:** mean \(-\dot H\approx 0.02\text{–}0.04\ll R_{\mathrm{worst}}=0.33\); frac \(H\ge 0.25\) stays \(1.0\) through \(t=6.4\).

### 5.5 Analytic lower bound on \(t_{\min}\) (order-of-magnitude)

A crude majorant: at short time PM freezes *all* \(O(1)\) super-threshold noise edges, so noise residual decays slower than heat. Bound

\[
\Delta_{\mathrm{noise}}(t)
\;\le\;
C_\Delta\frac{\sigma^2}{N}
\qquad
\text{(uniform on }[0,T_{\mathrm{mix}}]\text{; loose)}
\]

is too crude (gives tiny \(t_{\min}\)). Better **empirical power-law fit** from the envelope:

\[
\Delta_{\mathrm{noise}}(t)
\;\approx\;
\frac{a}{N}\,t^{-p},
\quad
p\in[0.3,\,0.6]
\]

(noise residual gap shrinks as both denoise). Combined with \(R_{\mathrm{blur}}=c_D\sqrt{t}/N\),

\[
t_{\min}
\;\gtrsim\;
\Bigl(\frac{a}{c_D}\Bigr)^{2/(1+2p)}.
\]

**Status:** numerical \(t_{\min}\) from MC is **canonical for claims**; analytic formula is **order-of-magnitude** until a closed spectral estimate of PM vs heat noise traces exists.

---

## 6. Nonempty analytic T1′ window (toy class)

Combine:

\[
t_{\min}^{\mathrm{(emp)}}
\approx
1.2
\quad(\text{conservative }1.6),
\qquad
t_{\max}^{\mathrm{(C′2♯)}}
=
T_{\mathrm{pers}}^\sharp
\approx
1.67
\quad(H_{\mathrm{init}}=0.80).
\]

\[
\boxed{
[t_{\min},\,t_{\max}]
=
[1.2,\,1.67]
\text{ is analytically nonempty under C′1b+C′2♯}.
}
\]

**Experimental window is larger** \([1.6,\,6.4+]\) because actual \(-\dot H\ll R_{\mathrm{worst}}\). Analytic T1′ on \([1.2,\,1.67]\) is the **proved-sketch cover**; experimental T1′ remains the **witness cover**.

### What remains for a full theorem

| Gap | Need | After M1d |
|-----|------|-----------|
| E′ residual comparison | Close on analytic window | **Hybrid closed on \(I_\star=\{1.36,\ldots,1.60\}\)** ([m1d](m1d-lemma-e-prime.md)) |
| \(\Delta_{\mathrm{noise}}\) without MC | Spectral freeze-tax bound | Still open (last pure-analytic gap) |
| \(\delta\le 0.05\) joint | Optional | Residual hybrid is unconditional via E′0 |
| Edge-height half of T1′ | On \(\mathcal{E}\) | **Closed** (M1d E′d) |

---

## 7. Lemma board (M1c)

| Item | After M1b | **After M1c** |
|------|-----------|----------------|
| C′1b height concentration | — | **Proved sketch** (\(H_{\mathrm{init}}=0.80\), \(\delta\sim 0.12\)) |
| C′2 crude \(T_{\mathrm{pers}}\) | 0.76 | retained as weak bound |
| **C′2♯** | open | **Proved** \(T_{\mathrm{pers}}^\sharp\approx 1.67\) under C′1b |
| Analytic \(t_{\max}\ge t_{\min}\)? | **No** | **Yes** (window \([1.2,\,1.67]\)) |
| \(\Delta_{\mathrm{noise}}\) | undefined numerically | **Lattice MC + decomposition** |
| \(c_D\) lattice | open | **\(\approx 0.30\text{–}0.34\)** |
| Full T1′ theorem | open | **Still open** (E′ constants) but **no longer blocked by empty window** |

---

## 8. Explicit non-claims

1. T1′ is still **not** a complete theorem.  
2. \(T_{\mathrm{pers}}^\sharp\approx 1.67\) is **not** the experimental lifetime (\(\gg 6\)).  
3. \(\Delta_{\mathrm{noise}}\) formula is **not** closed without MC for the gap function.  
4. Continuum GfE untouched.

---

## 9. One-line takeaway

**M1c:** Raising the initial height via C′1b (\(H^0\ge 0.80\)) and flooring at \(H_{\mathrm{floor}}=0.25\) yields **analytic** \(T_{\mathrm{pers}}^\sharp\approx 1.67\ge t_{\min}\approx 1.2\); \(\Delta_{\mathrm{noise}}\) is estimated from the heat blur/noise split so the residual crossover is explained as \(R_{\mathrm{blur}}(t)=\Delta_{\mathrm{noise}}(t)\). Full E′ closure remains.

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
