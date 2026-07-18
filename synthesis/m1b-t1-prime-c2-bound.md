# M1b — Analytic C′2 Bound and Solidified T1′ Window

**M-id:** M1b (solidifies M1 / T1′)  
**Status:** **Analytic C′2 height bound closed under explicit Euler + C′1 event; T1′ limits pinned for toy class; residual comparison E′ still open as full proof**  
**Follow-on:** [m1c-c2-sharp-delta-noise.md](m1c-c2-sharp-delta-noise.md) — **C′2♯** makes analytic \(t_{\max}\ge t_{\min}\); \(\Delta_{\mathrm{noise}}\) lattice estimate  
**Parents:** [m1-lemma-c-prime.md](m1-lemma-c-prime.md) · [t1-residual-domination.md](t1-residual-domination.md)  
**Witness:** [simulations/bridging/t1_mc_envelope.txt](../simulations/bridging/t1_mc_envelope.txt) · [t1_delta_noise_envelope.txt](../simulations/bridging/t1_delta_noise_envelope.txt)  
**Date:** 2026-07-14

---

## 1. Goal

Close the remaining analytic gaps that keep **Proposition T1′** from being a usable theorem-level statement for the **toy Euler PM scheme**:

| Piece | Prior (M1) | After M1b |
|-------|------------|-----------|
| C′1 initial localization | Proved sketch + MC | Unchanged (still proved sketch) |
| C′2 height persistence | Experimental + schematic \(T\) | **Analytic bound** under C′1 + flux Lipschitz |
| \(t_{\min},t_{\max}\) for T1′ | MC-only | **Pinned ranges** for toy class + scaling form |
| E′ residual comparison | Architecture + MC | Architecture + **explicit comparison inequality under C′2**; expectation closure still needs noise estimates |

**Not claimed:** full T1 on \((0,t_\star]\); continuum SPDE; multi-jump.

---

## 2. Notation (Euler PM toy)

- Lattice size \(N\), \(h=1\), true jump edge \(e_\star\).  
- Gradients \(g_i=(\nabla\phi)_i\), PM conductivity \(\rho_i=1/(1+(g_i/K)^2)\), flux \(F_i=\rho_i g_i\).  
- Explicit Euler: \(\phi^{k+1}=\phi^k+dt\cdot\mathrm{div}\,F(\nabla\phi^k)\).  
- Jump height \(H^k := |g_{e_\star}^k|\).  
- Toy defaults: \(\sigma=0.12\), \(K=0.15\), \(dt=0.08\), \(N=192\).

**Elementary flux bound (Lemma B form).** For any edge,

\[
\bigl|F\bigr|
=
\frac{|g|}{1+(g/K)^2}
\le
\frac{K}{2},
\]

with equality only at \(|g|=K\). For \(|g|\ge H_{\min}>K\),

\[
|F|
\le
\frac{K^2}{H_{\min}}
\qquad
\bigl(\text{since }|F|=|g|/(1+(g/K)^2)\le K^2/|g|\bigr).
\]

---

## 3. Lemma C′2 (analytic) — height persistence

### Statement

**Assumptions:** A1–A4, A6 from the T1 note; explicit Euler with \(0<dt\le dt_{\max}\le 1/8\); event \(\mathcal{E}_0\) of C′1:

\[
H^0 \ge H_{\star} := \tfrac12,
\qquad
\arg\max_e |g_e^0| = e_\star.
\]

(For toy \(K=0.15\), \(H_{\star}=1/2>K\), so the true edge is super-threshold.)

**Lemma C′2 (closed form).**  
On \(\mathcal{E}_0\), for all integers \(k\ge 0\) with \(k\,dt\le T_{\mathrm{pers}}\),

\[
H^k \;\ge\; H_{\star} - 2\,C_F\,k\,dt
\;\ge\;
\tfrac12\,H_{\star}
=
\tfrac14,
\]

where

\[
C_F
:=
\frac{K}{2}
+
\frac{K^2}{H_{\star}/2}
=
\frac{K}{2}
+
\frac{2K^2}{H_{\star}},
\]

and

\[
T_{\mathrm{pers}}
:=
\frac{H_{\star}/2}{2\,C_F}
=
\frac{H_{\star}}{4\,C_F}.
\]

In particular \(H^k\ge H_{\star}/2\) on \([0,T_{\mathrm{pers}}]\), so the true edge remains super-threshold (\(>K\) for toy parameters) throughout the window.

### Proof

**Step 1 — one-step jump change.**  
The discrete jump evolves only through the divergence of fluxes at the two sites adjacent to \(e_\star\):

\[
g_{e_\star}^{k+1}-g_{e_\star}^{k}
=
dt\Bigl[
(\mathrm{div}\,F^k)_{i_\star}
-
(\mathrm{div}\,F^k)_{i_\star-1}
\Bigr].
\]

Each \(\mathrm{div}\,F\) is a difference of at most two adjacent fluxes (Neumann ends at most one). Expanding the two site contributions, every term is \(\pm F_e\) for an edge \(e\) incident to \(\{i_\star-1,i_\star\}\). There are at most **four** flux terms (true edge twice with opposite signs in the two divs, plus one left-plateau edge and one right-plateau edge). A crude bound is therefore

\[
\bigl|g_{e_\star}^{k+1}-g_{e_\star}^{k}\bigr|
\le
4\,dt\cdot\max_e |F_e^k|
\le
4\,dt\cdot\frac{K}{2}
=
2\,K\,dt.
\]

**Sharper while \(H^k\ge H_{\star}/2\):** the true-edge flux satisfies \(|F_{e_\star}|\le K^2/H^k\le 2K^2/H_{\star}\), while adjacent plateau fluxes still obey \(|F|\le K/2\). Collecting coefficients of the true-edge contribution (weight \(\le 2\)) and adjacent contributions (weight \(\le 2\)):

\[
\bigl|\Delta g_{e_\star}\bigr|
\le
dt\Bigl(
2\cdot\frac{2K^2}{H_{\star}}
+
2\cdot\frac{K}{2}
\Bigr)
=
2\,dt\Bigl(
\frac{2K^2}{H_{\star}}
+
\frac{K}{2}
\Bigr)
=
2\,C_F\,dt.
\]

(The factor \(2\) in front of \(C_F\) in the lemma statement absorbs this accounting; any \(O(1)\) overestimate only shortens \(T_{\mathrm{pers}}\).)

**Step 2 — induction.**  
Assume \(H^j\ge H_{\star}/2\) for all \(j\le k\). Then

\[
H^{k+1}
\ge
H^k - 2\,C_F\,dt
\ge
H^0 - 2\,C_F\,(k+1)\,dt.
\]

Require \(H^0-2\,C_F\,(k+1)\,dt\ge H_{\star}/2\). Since \(H^0\ge H_{\star}\), it suffices that

\[
(k+1)\,dt
\le
\frac{H_{\star}/2}{2\,C_F}
=
T_{\mathrm{pers}}.
\]

Thus for all \(k\,dt\le T_{\mathrm{pers}}\), \(H^k\ge H_{\star}/2\).

**Step 3 — super-threshold.**  
For toy \(H_{\star}/2=1/4>K=0.15\), the true edge remains strictly super-threshold on the whole interval, so Lemma B flux freeze applies with \(c=H^k/K\ge (1/4)/0.15\approx 1.67\).

### Toy numbers

\[
K=0.15,\quad H_{\star}=0.5,
\quad
C_F
=
\frac{0.15}{2}+\frac{2(0.15)^2}{0.5}
=
0.075+0.09
=
0.165,
\]

\[
T_{\mathrm{pers}}
=
\frac{0.5}{4\cdot 0.165}
\approx
0.758.
\]

**Conservative analytic persistence window:** \(T_{\mathrm{pers}}\approx 0.76\) (wall-clock).  

**MC observation:** height \(\ge 0.5\) persists with fraction \(1.0\) out to \(t=6.4\) — much longer than the crude bound. The analytic \(T_{\mathrm{pers}}\) is a **lower bound on guaranteed persistence**, not the observed lifetime. For residual domination we may use a **hybrid**:

\[
t_{\max}
=
\min\bigl(T_{\mathrm{pers}}^{\mathrm{(analytic)}},\; T_{\mathrm{MC}}\bigr)
\quad\text{or better}\quad
t_{\max}^{\mathrm{(MC)}}\gg T_{\mathrm{pers}}
\text{ with experimental label}.
\]

### Status

| Claim | Status |
|-------|--------|
| \(H^k\) cannot fall faster than \(O(K\,dt)\) per step | **Proved** (flux bound) |
| Explicit \(T_{\mathrm{pers}}\) with \(H^k\ge H_{\star}/2\) on \([0,T_{\mathrm{pers}}]\) under C′1 | **Proved** (crude constants) |
| Optimal constants / matching MC lifetime \(t\sim 6+\) | **Open** (needs comparison principle, not just worst-case flux) |
| False-edge creation control | **Not in C′2**; residual E′ uses C′1 argmax only at \(t=0\) + bulk \(\rho\approx 1\) heuristic |

---

## 4. Refined Proposition T1′ (solidified)

### Statement

> **Proposition T1′ (lattice, single jump; solidified target).**  
> Under A1–A4, A6, \(K=c_K\sigma\) with \(c_K\in[1,3]\), and the C′1 event \(\mathcal{E}_0\) of probability \(\ge 1-\delta\) (M1), there exist
>
> \[
> 0 < t_{\min} < t_{\max},
> \]
>
> depending on \((\sigma,K,N,dt)\), such that for all wall-clock times \(t=k\,dt\in[t_{\min},t_{\max}]\),
>
> \[
> \mathbb{E}\bigl[R(\hat\phi^{\mathrm{PM}}(t),\phi_\star)\bigr]
> \;\le\;
> \mathbb{E}\bigl[R(\hat\phi^{\mathrm{heat}}(t),\phi_\star)\bigr],
> \]
>
> and
>
> \[
> \mathbb{E}\bigl[\mathrm{EdgeHeight}(\hat\phi^{\mathrm{PM}}(t))\bigr]
> \;\ge\;
> c_{\mathrm{edge}}\,
> \mathbb{E}\bigl[\mathrm{EdgeHeight}(\hat\phi^{\mathrm{heat}}(t))\bigr]
> \]
>
> for some \(c_{\mathrm{edge}}>1\).

### Pinned limits for the toy class

Using canonical MC envelope (\(N_{\mathrm{MC}}=200\), seed \(1\)) and analytic C′2:

| Limit | Analytic | Experimental (MC) | Recommendation for claims |
|-------|----------|-------------------|---------------------------|
| \(t_{\min}\) | Noise vs blur crossover: equate heat blur \(\sim c_D\sqrt{t}/N\) with shared noise floor difference — scaling \(t_{\min}=\Theta(\sigma^4)\) continuum heuristic; lattice toy: **order \(1\)** | Mean \(R_h-R_{\mathrm{PM}}\) flips **between \(0.80\) and \(1.60\)**; frac PM better: \(0.015\) at \(0.80\), \(0.990\) at \(1.60\) | **\(t_{\min}\in[1.0,\,1.6]\)** for toy; cite **\(t_{\min}\approx 1.2\)** as mid-bracket or use \(t_{\min}=1.6\) for conservative “all checked times pass” |
| \(t_{\max}\) | \(T_{\mathrm{pers}}\approx 0.76\) (crude; **too short** for residual window that starts at \(t_{\min}\sim 1\)) | Persist \(H\ge 0.5\) and residual dual hold through **\(t=6.4\)** (last MC point); joint toy runs to \(T=14.4\) | **For experimental T1′:** \(t_{\max}\ge 6.4\). **For analytic-only T1′:** need sharpened C′2 before \(t_{\max}\ge t_{\min}\) |
| \(c_{\mathrm{edge}}\) | \(\ge H_{\star}/2=1/4\) vs heat \(O(t^{-1/2})\) deterministic | Final-time scorecard ratio \(\gg 1.15\) | Use \(c_{\mathrm{edge}}=1.15\) as **scorecard-aligned** lower target |

### Critical honesty about analytic \(t_{\max}\)

The crude C′2 bound \(T_{\mathrm{pers}}\approx 0.76\) is **shorter than** experimental \(t_{\min}\approx 1.6\). Therefore:

- **Analytic C′2 alone does not yet cover the residual-domination window.**  
- What C′2 **does** establish: a rigorous short-time height floor under worst-case flux accounting; a template for sharpening.  
- What remains for a **full analytic T1′**: either (i) improve \(C_F\) using cancellation / comparison (true edge flux \(\ll K/2\) and adjacent fluxes partially cancel in the jump ODE), or (ii) prove residual domination on \([t_{\min},T_{\mathrm{pers}}]\) is empty and extend persistence first.

**Sharpening target (open).** If adjacent fluxes are \(O(\sigma)\) after a short transient and true-edge \(|F|\le K^2/H\le 2K^2\), a realistic rate is \(O(K^2+ \sigma)\) rather than \(O(K)\), giving

\[
T_{\mathrm{pers}}^{\mathrm{(target)}}
\sim
\frac{H_{\star}}{O(K^2+\sigma)}
\sim
\frac{0.5}{O(0.02+0.12)}
\sim O(1\text{–}5),
\]

which would **overlap** the MC residual window. Closing this is the main remaining analytic step for C′2.

---

## 5. Lemma E′ — comparison under C′2 (architecture with explicit inequality)

### On the event \(\mathcal{E}_0\cap\{H^s\ge H_{\star}/2:\, s\le t\}\)

Split residual into plateau and interface collar of width \(w=\Theta(1)\) sites about \(e_\star\):

\[
R_{\mathrm{PM}}
\le
R_{\mathrm{plateau}}^{\mathrm{(Neu)}}
+
R_{\mathrm{interface}}.
\]

**Interface budget (from C′2 + Lemma B).**  
Mass leaked across \(e_\star\) up to time \(t\) is at most

\[
\int_0^t |F_{e_\star}|\,ds
\le
t\cdot\frac{K^2}{H_{\star}/2}
=
\frac{2K^2\,t}{H_{\star}}.
\]

Squared residual contribution after spreading over \(O(1)\) sites:

\[
R_{\mathrm{interface}}
\le
\frac{C_{\mathrm{int}}}{N}\left(\frac{2K^2\,t}{H_{\star}}\right)^2.
\]

**Heat lower bound (Lemma D).**  

\[
\mathbb{E} R_{\mathrm{heat}}(t)
\ge
\frac{c_D}{N}\sqrt{t}.
\]

**Comparison inequality (pathwise on the event, then take expectations carefully):**

\[
R_{\mathrm{PM}}(t)
\le
R_{\mathrm{plateau}}^{\mathrm{(Neu)}}(t)
+
\frac{C_{\mathrm{int}}}{N}\left(\frac{2K^2\,t}{H_{\star}}\right)^2.
\]

For residual domination it suffices that

\[
\mathbb{E}\bigl[R_{\mathrm{plateau}}^{\mathrm{(Neu)}}(t)\bigr]
+
\frac{C_{\mathrm{int}}}{N}\left(\frac{2K^2\,t}{H_{\star}}\right)^2
\;\le\;
\frac{c_D}{N}\sqrt{t}
+
\mathbb{E}\bigl[R_{\mathrm{heat}}^{\mathrm{(noise)}}(t)\bigr].
\]

**Noise race (explains \(t_{\min}\)).**  
At very small \(t\), heat reduces bulk noise faster (PM freezes some noise gradients). The difference

\[
\Delta_{\mathrm{noise}}(t)
:=
\mathbb{E} R_{\mathrm{plateau}}^{\mathrm{(Neu)}}(t)
-
\mathbb{E} R_{\mathrm{heat}}^{\mathrm{(noise)}}(t)
\]

is **positive** for small \(t\) (heat wins the noise race). Residual domination requires the heat **blur** term \(\frac{c_D}{N}\sqrt{t}\) to overcome \(\Delta_{\mathrm{noise}}+\text{interface}\):

\[
\frac{c_D}{N}\sqrt{t}
\;\ge\;
\Delta_{\mathrm{noise}}(t)
+
\frac{C_{\mathrm{int}}}{N}\left(\frac{2K^2\,t}{H_{\star}}\right)^2.
\]

Define

\[
t_{\min}
:=
\inf\Bigl\{t>0:\text{the display holds}\Bigr\},
\qquad
t_{\max}
:=
\sup\bigl\{t\le T_{\mathrm{height}}:\text{C′2-style height event holds}\bigr\}.
\]

**Status E′:** inequality architecture **explicit**; \(\Delta_{\mathrm{noise}}(t)\) and \(c_D\) lattice constants **not fully evaluated** — MC supplies the empirical \(t_{\min}\).

---

## 6. MC envelope (canonical, unchanged)

From `t1_mc_envelope.txt` (\(N_{\mathrm{MC}}=200\), seed \(1\)):

| \(t\) | mean \(R_h-R_{\mathrm{PM}}\) | frac PM better | persist \(H\ge 0.5\) |
|-------|------------------------------|----------------|---------------------|
| 0.40 | −0.003442 | 0.000 | 1.000 |
| 0.80 | −0.001374 | 0.015 | 1.000 |
| 1.60 | +0.000975 | 0.990 | 1.000 |
| 3.20 | +0.002625 | 1.000 | 1.000 |
| 6.40 | +0.004070 | 1.000 | 1.000 |

**Experimental T1′ window (toy):** \([t_{\min},t_{\max}]=[1.6,\,6.4]\) on the sampled grid (and likely larger \(t_{\max}\) toward the joint-toy horizon \(T=14.4\)).

---

## 7. Lemma board update (M1b)

| Item | After M1 | **After M1b** |
|------|----------|----------------|
| C′2 analytic | sketch | **Proved crude \(T_{\mathrm{pers}}\approx 0.76\)**; sharpening open |
| T1′ limits | MC only | **Pinned:** experimental \([1.6,6.4]\); analytic \(t_{\max}\) still short of \(t_{\min}\) until C′2 sharpened |
| E′ | architecture | **Explicit comparison inequality**; \(\Delta_{\mathrm{noise}}\) open |
| Full T1′ theorem | open | **Still open** (blocked by sharpened persistence + \(\Delta_{\mathrm{noise}}\)) |
| Experimental T1′ | strong | **Unchanged strong** |

---

## 8. Explicit non-claims

1. T1′ is **not** a complete theorem.  
2. Crude \(T_{\mathrm{pers}}\) is **not** the observed lifetime.  
3. We do **not** claim residual domination for all \(t\in(0,t_\star]\).  
4. Continuum GfE / Lorentzian master equation untouched.

---

## 9. One-line takeaway

**M1b:** C′2 now has an **explicit Euler flux bound** and \(T_{\mathrm{pers}}\); T1′ residual window is **experimentally** \([1.6,6.4]\) on the toy grid; full analytic T1′ still needs a **sharpened** persistence constant so that \(t_{\max}^{\mathrm{(analytic)}}\ge t_{\min}\), plus a lattice estimate of the short-time noise race \(\Delta_{\mathrm{noise}}\).

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
