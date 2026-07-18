# M1 — Lemma C′ (Weakened Edge Persistence) and Short-Time Residual Window

**M-id:** M1 (advances T1)  
**Status:** **Weakened C′ closed as probabilistic + experimental envelope; C′2 analytic crude bound in M1b; Proposition T1′ refined (not fully proved)**  
**Parent:** [t1-residual-domination.md](t1-residual-domination.md)  
**Follow-on:** [m1b-t1-prime-c2-bound.md](m1b-t1-prime-c2-bound.md) (analytic C′2 + pinned T1′ window)  
**Witness data:** [simulations/bridging/t1_mc_envelope.txt](../simulations/bridging/t1_mc_envelope.txt)  
**Date:** 2026-07-14

---

## 1. Why weaken C

Original Lemma C demanded: true edge super-threshold at \(cK\) with \(c>1\) **and** all false edges below \(cK/2\).  

For toy parameters \(\sigma=0.12\), \(K=0.15\), \(N=192\):

| Statistic (MC \(n=2000\)) | Value |
|---------------------------|-------|
| \(\mathbb{E}|(\nabla y)_{e_\star}|\) | \(\approx 1.00\) (theory: mean \(1\), var \(2\sigma^2\)) |
| \(\mathbb{E}\max_{e\neq e_\star}|(\nabla y)_e|\) | \(\approx 0.50\) |
| \(P(\arg\max|\nabla y|=e_\star)\) | \(\approx 0.998\) |
| \(c=1.5\Rightarrow cK=0.225\) | true edge \(\gg cK\), but **max false often \(> cK/2\)** |

So the **strict false-edge gap** in original C fails: noise edges are often larger than \(cK/2\). PM may partially freeze some noise gradients (staircasing risk) while the **true** edge still dominates as unique maximizer.

---

## 2. Lemma C′ (weakened) — statement

**Assumptions:** A1–A4, A6 from t1 note; \(K=c_K\sigma\) with \(c_K\in[1,3]\); single unit jump.

**Lemma C′ (initial localization + height persistence).**  
**Status: C′1 proved sketch (with explicit constants for toy class); C′2 experimental + flux bound sketch; not a full dynamical theorem.**

### C′1 — Initial localization  
With probability at least \(1-\delta\),

1. \(\arg\max_e |(\nabla y)_e| = e_\star\),
2. \(|(\nabla y)_{e_\star}| \ge \tfrac12\).

**Proof idea (C′1).**  

- \((\nabla y)_{e_\star}=1+\eta_{i_\star}-\eta_{i_\star-1}\sim\mathcal{N}(1,2\sigma^2)\).  
  \[
  P\bigl(|(\nabla y)_{e_\star}|<\tfrac12\bigr)
  = P\bigl(\mathcal{N}(1,2\sigma^2)<\tfrac12\bigr)
  = \Phi\!\left(\frac{-1/2}{\sigma\sqrt{2}}\right)
  \]
  For \(\sigma=0.12\): \(-0.5/(0.12\sqrt{2})\approx -2.95\), so \(P<\tfrac12 \approx 0.0016\). Union over orientation already covered by abs.  
- False edge \(e\): \((\nabla y)_e\sim\mathcal{N}(0,2\sigma^2)\) (adjacent edges correlated; bound by \(N\) marginal tails).  
  \[
  P\bigl(|(\nabla y)_e| > 1-\varepsilon\bigr)\le 2\exp\bigl(-(1-\varepsilon)^2/(4\sigma^2)\bigr).
  \]
  For \(\varepsilon=0.2\), \(\sigma=0.12\): exponent \(-(0.8)^2/(4\cdot 0.0144)\approx -11.1\), tail \(\sim 3\cdot 10^{-5}\). Union bound \(\times N=192\) still \(\ll 10^{-2}\).  
- Hence \(P(\max_{\mathrm{false}} > |(\nabla y)_{e_\star}|)\) is tiny when true height concentrates near \(1\).  
- **MC witness** (canonical `t1_mc_envelope.txt`, \(N_{\mathrm{MC}}=200\), seed \(1\)):  
  \(P(\arg\max=e_\star)=0.995\), \(P(|\nabla y|_{e_\star}\ge 0.5)=1.000\).

**Status C′1:** **proved sketch** for Gaussian i.i.d. noise + single jump; constants explicit for \(\sigma\lesssim 0.15\), \(N\lesssim 10^3\). Dependent-edge joint law: fill with comparison inequality (max of correlated Gaussians dominated by independent case up to factor).

### C′2 — Height persistence under Euler PM  
On the event of C′1, for the explicit-Euler PM scheme of the toy with CFL-stable \(dt\), there exists

\[
T = T(\sigma,K,N,dt) \;=\; \min\left\{
T_{\mathrm{mix}},\;
\frac{\bigl(|(\nabla y)_{e_\star}| - \tfrac12\bigr)^2}{8\,(K/2 + 2\|\nabla\|_{\infty,\mathrm{init}} dt)^2}
\right\}
\]

(form schematic — see bound below) such that with high probability, for all integers \(k\) with \(k\,dt\le T\),

\[
\bigl|(\nabla\hat\phi^{k})_{e_\star}\bigr| \;\ge\; \tfrac12.
\]

**Proof idea (C′2) — flux ODE bound (sketch, not fully closed).**  
While \(|g_{e_\star}|\ge 1/2 > K\) (since \(K=0.15\)), Lemma B gives \(|F_{e_\star}|\le K/(1/2\cdot 1/K wait)\):  
actually \(|g|\ge 1/2\), \(\rho\le 1/(1+(1/(2K))^2)\). For \(K=0.15\), \(1/(2K)\approx 3.33\), \(\rho\le 1/(1+11.1)\approx 0.083\), \(|F|\le 0.083\cdot |g|\le O(0.1)\).  

Jump height evolves at rate bounded by \(O(|F_{e_\star}|+|F_{\mathrm{adj}}|)\). Over time \(T\), change \(\le C T\). Choose \(T \le (g_0 - 1/2)/(2C)\) so height cannot fall below \(1/2\).  

**Gap:** rigorous control of adjacent fluxes under Euler stepping and bulk noise (needs discrete comparison / Lipschitz of Euler map — well-posedness already sketched).  

**Experimental witness (C′2):** Canonical file `simulations/bridging/t1_mc_envelope.txt`  
(\(N_{\mathrm{MC}}=200\), seed \(1\), produced by `test_t1_mc_envelope.py`).  
Fraction with \(|(\nabla\hat\phi)_{e_\star}|\ge 0.5\) for all steps \(k\le n_{\mathrm{steps}}\):

| \(n_{\mathrm{steps}}\) | \(t=n\,dt\) | Persist frac |
|------------------------|-------------|--------------|
| 5 | 0.40 | **1.0000** |
| 10 | 0.80 | **1.0000** |
| 20 | 1.60 | **1.0000** |
| 40 | 3.20 | **1.0000** |
| 80 | 6.40 | **1.0000** |

**Status C′2:** **experimental closed in toy regime** + **analytic crude bound** \(T_{\mathrm{pers}}\approx 0.76\) (M1b); sharpened persistence for \(t\ge t_{\min}\) still open. See [m1b-t1-prime-c2-bound.md](m1b-t1-prime-c2-bound.md).

---

## 3. Refined residual window (critical MC finding)

Monte Carlo from canonical `t1_mc_envelope.txt` (\(N_{\mathrm{MC}}=200\), seed \(1\))  
of mean \(R_{\mathrm{heat}}-R_{\mathrm{PM}}\) along the real `_joint_toy_v2_core` scheme:

| \(t\) | mean \(R_h-R_{\mathrm{PM}}\) | frac PM better |
|-------|------------------------------|----------------|
| 0.40 | **−0.003442** | 0.0000 |
| 0.80 | **−0.001374** | 0.0150 |
| 1.60 | +0.000975 | 0.9900 |
| 3.20 | +0.002625 | 1.0000 |
| 6.40 | +0.004070 | 1.0000 |

Regenerate with: `.venv/bin/python simulations/bridging/test_t1_mc_envelope.py`

**Interpretation:** At very short times, isotropic heat reduces **noise** faster (PM freezes large noise gradients too). After a transient \(t_{\min}\sim 1\), heat’s **jump blur** dominates and PM residual wins.  

### Refined Proposition T1′ (target)

Same as T1 but residual domination only on a window

\[
t \in [t_{\min},\, t_{\max}],
\qquad
t_{\min} = \Theta(1)\ \text{(noise-dominated transient)},
\quad
t_{\max} = T\ \text{(from C′2)}.
\]

**Status:** **experimentally supported** for toy parameters on \([1.6,\,6.4]\) (MC grid); **not proved**. Full T1 as originally stated on \((0,t_\star]\) is **false** for this scheme/parameters (obstruction at short \(t\)). Analytic C′2 crude window does not yet cover \(t_{\min}\) — see M1b.

---

## 4. Lemma E′ — comparison architecture under C′

**Status: open as proof; architecture + MC envelope**

On the event of C′, for \(t\in[t_{\min},T]\):

\[
\mathbb{E} R_{\mathrm{PM}}(t)
\;\le\;
\underbrace{\mathbb{E} R_{\mathrm{plateau}}^{\mathrm{Neu}}(t)}_{\text{Lemma A style}}
+ O(T^2/N)
\;\le\;
\mathbb{E} R_{\mathrm{heat}}(t)
\]

because heat pays \(\Omega(\sqrt{t}/N)\) deterministic blur (Lemma D) while PM interface leakage stays \(O(\rho_{\star} t)\).  

**MC:** for \(t\ge 1.6\), mean improvement positive with frac \(\ge 0.98\).

---

## 5. Lemma board update (M1 outcome)

| Item | Prior | **After M1** |
|------|-------|----------------|
| Proposition T1 \((0,t_\star]\) | open | **Obstruction at short \(t\)** for toy scheme; replace by **T1′** window |
| Proposition T1′ \([t_{\min},t_{\max}]\) | — | **Open (target)**; **experimental support** strong |
| Lemma C original | open | **Superseded** by C′ (strict false-edge gap fails empirically) |
| Lemma C′1 | — | **Proved sketch** + MC |
| Lemma C′2 | — | **Experimental closed (toy)**; **analytic crude \(T_{\mathrm{pers}}\)** (M1b); sharpening open |
| Lemma E | open | **E′ architecture explicit** (M1b); MC envelope for \(t\ge t_{\min}\); \(\Delta_{\mathrm{noise}}\) open |
| Joint toy final-time residual | witness | Consistent with T1′ (run length \(\gg t_{\min}\)) |

---

## 6. Explicit non-claims

- T1 / T1′ is **not** a theorem.  
- C′2 is **not** fully proved analytically.  
- Short-time heat superiority is **not** a dual failure; it refines the dual’s **time window**.  
- Continuum GfE gravity is untouched.

---

## 7. One-line takeaway for decision log

**M1 result:** Strict Lemma C fails (noise edges too large for \(cK/2\) gap); weakened **C′** holds initially with high probability and persists experimentally; residual domination is **false at ultra-short \(t\)** (heat wins noise race) and **holds for intermediate \(t\)** (T1′ window) with strong MC support — dual is real but **time-windowed**, not instant.
