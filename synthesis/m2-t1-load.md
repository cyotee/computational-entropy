# M2 — T1-load: Load-Gated PM vs Heat

**M-id:** M2  
**Status:** **Hybrid established on \(I_\star\); time-change lemma closed as definition; pure theorem open**  
**Depends on:** [m1d-lemma-e-prime.md](m1d-lemma-e-prime.md) (hybrid T1′) · [t1-residual-domination.md](t1-residual-domination.md) §6  
**Witness:** [simulations/bridging/t1_load_m2_envelope.txt](../simulations/bridging/t1_load_m2_envelope.txt) · [test_t1_load_m2.py](../simulations/bridging/test_t1_load_m2.py)  
**Date:** 2026-07-14

---

## 1. Statement

> **Proposition T1-load (hybrid target).**  
> For wall-clock times \(t\in I_\star=\{1.36,1.44,1.52,1.60\}\) (toy Euler grid),
>
> \[
> \mathbb{E}\,R\bigl(\hat\phi^{\mathrm{load\text{-}PM}}(t),\phi_\star\bigr)
> \;\le\;
> \mathbb{E}\,R\bigl(\hat\phi^{\mathrm{heat}}(t),\phi_\star\bigr).
> \]

**Physical reading:** the master-equation-style clock \(dt/(1+\alpha_L L_{\mathrm{clock}})\) slows PM without destroying residual dual vs heat — load is a **reparameterization**, not a different reconstructor.

---

## 2. Lemma M2-τ — time change (closed)

### Continuum idealization

Along a trajectory with \(L_{\mathrm{clock}}(s)\ge 0\),

\[
\frac{d\hat\phi^{\mathrm{load}}}{dt}
=
\frac{1}{1+\alpha_L L_{\mathrm{clock}}(t)}
\,
V_{\mathrm{PM}}\bigl(\hat\phi^{\mathrm{load}}\bigr),
\]

where \(V_{\mathrm{PM}}\) is the PM vector field. Define

\[
\tau(t)
=
\int_0^t \frac{ds}{1+\alpha_L L_{\mathrm{clock}}(s)}
\;\le\;
t.
\]

Then \(\hat\phi^{\mathrm{load}}(t)=\hat\phi^{\mathrm{PM}}(\tau(t))\) when both start at \(y\) and \(L_{\mathrm{clock}}\) is evaluated along the load path (state-dependent clock).

### Discrete Euler (toy)

Each step uses \(dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}}(\phi^k))\). This is a consistent discretization of the ODE time change as \(dt\to 0\).

**Status:** **proved sketch** (definition of time change / Euler consistency).  
**Toy parameters:** \(\alpha_L=3.0\), \(L_{\mathrm{clock}}=L_E+L_S\).

### Empirical \(\tau/t\)

| \(t\) | mean \(\tau/t\) |
|-------|-----------------|
| 1.20 | 0.951 |
| 1.36 | 0.953 |
| 1.60 | 0.957 |
| 3.20 | 0.970 |
| 6.40 | 0.979 |
| 14.40 | 0.985 |

Load runs at \(\sim 95\text{–}98\%\) of wall-clock internal time on the dual window — a **mild** lag.

---

## 3. Bridge from hybrid T1′

### Ideal argument

1. Hybrid T1′: \(\mathbb{E}R_{\mathrm{PM}}(s)\le\mathbb{E}R_{\mathrm{heat}}(s)\) for \(s\in I_\star\).  
2. Time change: \(R_{\mathrm{load}}(t)=R_{\mathrm{PM}}(\tau(t))\) (continuum).  
3. Need \(\mathbb{E}R_{\mathrm{PM}}(\tau(t))\le\mathbb{E}R_{\mathrm{heat}}(t)\).

If \(\tau(t)\in I_\star\) and residual of PM is **nonincreasing** on \(I_\star\), then  
\(R_{\mathrm{PM}}(\tau)\ge R_{\mathrm{PM}}(t)\) but we need vs **heat at wall \(t\)**, not at \(\tau\).

Heat residual is **not** monotone (blur↑, noise↓). The safe comparison is direct:

\[
\mathbb{E}R_{\mathrm{load}}(t)
\;\stackrel{?}{\le}\;
\mathbb{E}R_{\mathrm{heat}}(t)
\]

measured at equal wall-clock \(t\) (what the proposition states).

### Why mild lag helps

For \(t=1.60\), \(\tau\approx 1.53\in[1.36,1.67]\). Pure PM at \(\tau\) already beats heat at \(\tau\); heat at larger wall time \(t>\tau\) has **more blur** (helps the inequality) but **less noise residual** (hurts slightly). Empirically the blur side wins on \(I_\star\).

---

## 4. Monte Carlo envelope (canonical)

`t1_load_m2_envelope.txt` — \(N_{\mathrm{MC}}=200\), seed \(21\), \(\alpha_L=3\):

| \(t\) | \(\mathbb{E}R_h-\mathbb{E}R_{\mathrm{PM}}\) | \(\mathbb{E}R_h-\mathbb{E}R_{\mathrm{load}}\) | \(\mathbb{E}R_{\mathrm{PM}}-\mathbb{E}R_{\mathrm{load}}\) | frac load≺heat | frac PM≺heat |
|-------|-----------------------------------------------|--------------------------------------------------|-----------------------------------------------------|----------------|--------------|
| 1.20 | +0.00007 | **−0.00012** | −0.00019 | **0.44** | 0.56 |
| **1.36** | +0.00042 | **+0.00025** | −0.00017 | **0.74** | 0.82 |
| 1.44 | +0.00061 | +0.00045 | −0.00016 | 0.89 | 0.95 |
| **1.60** | +0.00096 | **+0.00083** | −0.00013 | **0.97** | 0.98 |
| 2.00 | +0.00153 | +0.00144 | −0.00009 | 1.00 | 1.00 |
| 6.40 | +0.00409 | +0.00408 | −0.00001 | 1.00 | 1.00 |
| 14.40 | +0.00619 | +0.00619 | \(\approx 0\) | 1.00 | 1.00 |

**Reading:**

1. **Load beats heat** on \(I_\star\) (and beyond) with strong fraction from \(t=1.36\).  
2. **Load is slightly worse than pure PM** residual (expected: less internal time). Gap shrinks as \(\tau/t\to 1\) and both denoise.  
3. At \(t=1.20\), load still **loses** to heat on average — T1-load window starts **slightly later** than pure PM’s crossover (lag effect).

---

## 5. Hybrid proposition status

| Piece | Status |
|-------|--------|
| M2-τ time change | **Closed** (definitional / Euler consistent) |
| T1-load residual on \(I_\star\) | **Hybrid experimental** (MC envelope) |
| T1-load from pure T1′ + monotone residual | **Open** (needs PM residual monotone on window + heat comparison at unequal times) |
| Edge height under load | **Inherited** from PM on \(\mathcal{E}\) (same field, slower clock; height persists at least as long in wall time) |

**Citation language:**

> Load-gated PM preserves residual dual vs heat on the hybrid T1′ window in the joint toy, acting as a \(\sim 5\%\) slower clock on the same PM flow (\(\tau/t\approx 0.95\)).

**Not allowed:** “T1-load is a theorem” without hybrid/MC label.

---

## 6. Link to master equation

The toy clock

\[
dt_{\mathrm{eff}}
=
\frac{dt}{1+\alpha_L L_{\mathrm{clock}}},
\qquad
L_{\mathrm{clock}}=L_E+L_S,
\]

is the discrete form-match of

\[
d\tau=\frac{dt}{1+\alpha L(\rho,g)}
\]

in the canonical master equation. M2 says: **that reparameterization does not erase the Euclidean residual dual** in the tested regime. It does **not** derive continuum \(L(\rho,g)\) from \(L_E,L_S\).

---

## 7. M3/M4 status (unchanged deferral, updated dependency)

| ID | Status after M2 |
|----|-----------------|
| **M3** Lyapunov | Still open; residual alone is not a global Lyapunov (short-\(t\) heat race) |
| **M4** load reparam theorem | Structural half = M2-τ; descent preservation needs M3 |

---

## 8. Explicit non-claims

1. T1-load is not pure-analytic.  
2. Load does not improve residual vs pure PM (it slightly worsens it).  
3. Continuum master equation not derived.  
4. Final-time joint-toy scorecard alone is not the M2 envelope (windowed times needed).

---

## 9. One-line takeaway

**M2:** Load-PM is a mild time change of PM (\(\tau/t\approx 0.95\)); on hybrid window \(I_\star\) it still beats heat in residual with high MC support, slightly lagging pure PM — the clock dual is **real and cheap** once T1′ holds.

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) · prior deferral: [m2-m4-followups.md](m2-m4-followups.md)
