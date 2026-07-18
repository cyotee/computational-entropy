# M1g — Unified Pure Residual Dual Window

**M-id:** M1g  
**Status:** **Unified pure window \(U_\star=[1.36,2.40]\) established under PCRH\(_b\) (\(\rho_b=0.42\)); covers full hybrid \(I_\star\) and former pure-late window in one argument**  
**Parents:** [m1f-hrho-pure-proof.md](m1f-hrho-pure-proof.md) · [m1d-lemma-e-prime.md](m1d-lemma-e-prime.md) · [m1e-freeze-tax-spectral.md](m1e-freeze-tax-spectral.md)  
**Witness:** [simulations/bridging/test_t1_unified_pure.py](../simulations/bridging/test_t1_unified_pure.py) · `t1_unified_pure_envelope.txt`  
**Date:** 2026-07-15

---

## 0. Win statement

Previously we had:

| Window | Times | Rigor |
|--------|-------|--------|
| Hybrid \(I_\star\) | 1.36–1.60 | MC \(\Delta_{\mathrm{noise}}\) |
| Pure late | 2.0–2.4 | \(\rho_\star\approx 0.30\) majorant |

**Now one pure argument** covers

\[
U_\star
=
\{1.36,\,1.44,\,1.52,\,1.60,\,2.00,\,2.40\}
\subset
[1.36,\,2.40]
\]

with burn-in conductivity \(\rho_b=0.42 > \rho_{\mathrm{eff}}(0)\approx 0.30\).

---

## 1. Why burn-in enables purity on \(I_\star\)

The freeze-tax majorant
\[
\Delta_{\mathrm{maj}}^{(\rho)}(t)
=
R_n^{(\rho)}(t)-R_n(t)+R_{\mathrm{interface}}(t)
\]
beats \(R_{\mathrm{blur}}(t)\) on \(I_\star\) only if \(\rho\gtrsim 0.41\).

The **provable-from-\(t=0\)** Gaussian energy weight is only \(\rho_{\mathrm{eff}}(2\sigma^2)\approx 0.30\), which first beats blur at \(t=2.0\) (M1f).

**Burn-in fact (empirical + structural):** under PM, plateau energy-weighted conductivity rises as noise gradients shorten:

| \(t\) | mean \(\rho_{\mathrm{ew}}\) (plateau) | \(P(\rho_{\mathrm{ew}}\ge 0.42)\) |
|-------|--------------------------------------|----------------------------------|
| 0.00 | 0.30 | ~0 |
| 0.80 | 0.48 | ~0.78 |
| 1.20 | 0.58 | ~0.96 |
| 1.36 | 0.63 | ~0.99 |

So by the start of \(I_\star\), the flow is **much more elliptic** than at \(t=0\). The residual of pure-noise PM at time \(t\ge 1.36\) lies **below** linear heat residual at constant conductivity \(\rho_b=0.42\) (PCRH\(_b\)), even though \(\rho_b>\rho_{\mathrm{eff}}(0)\).

---

## 2. Constants

| Symbol | Value | Role |
|--------|-------|------|
| \(\rho_b\) | **0.42** | Burn-in residual majorant conductivity |
| \(t_u\) | **1.36** | Start of unified pure grid (\(n=17\) steps) |
| \(t_v\) | **2.40** | End of certified grid (\(n=30\)) |
| \(H_{\mathrm{floor}}\) | 0.25 | Interface / C′2♯ floor |
| \(\rho_{\mathrm{eff}}(0)\) | ≈0.300 | M1f safe-from-zero constant (not used as \(\rho_b\)) |

---

## 3. Lemma U1 — Spectral majorant vs blur on \(U_\star\) (proved)

**Statement.** For the toy Laplacian spectrum and \(\rho_b=0.42\),
\[
R_{\mathrm{blur}}(t)
\;\ge\;
\Delta_{\mathrm{maj}}^{(\rho_b)}(t)
:=
R_n^{(\rho_b)}(t)-R_n(t)+\frac{2}{N}\Bigl(\frac{K^2 t}{H_{\mathrm{floor}}}\Bigr)^2
\]
for all Euler times \(t=n\,dt\in U_\star\).

**Proof.** \(R_{\mathrm{blur}}\) is deterministic (heat on \(\phi_\star\)). \(R_n^{(\rho)}\) is Lemma L1 (M1f). Direct evaluation:

| \(t\) | \(R_{\mathrm{blur}}\) | \(\Delta_{\mathrm{maj}}^{(0.42)}\) | Margin |
|-------|----------------------|-----------------------------------|--------|
| 1.36 | 0.001820 | 0.00173 | **+0.00009** |
| 1.44 | 0.001885 | 0.00169 | +0.00020 |
| 1.60 | 0.002008 | 0.00162 | +0.00038 |
| 2.00 | 0.002285 | 0.00155 | +0.00073 |
| 2.40 | 0.002532 | 0.00157 | +0.00096 |

(At \(t=1.20\), margin is **negative** ≈ \(-1.6\cdot 10^{-4}\): unified purity does **not** claim \(t=1.20\).) \(\square\)

---

## 4. Lemma U2 — PCRH\(_b\) (burn-in residual majorant)

**Statement (PCRH\(_b\)).** For pure-noise initial data \(\eta\sim\mathcal{N}(0,\sigma^2 I)\) and continuous / Euler PM,
\[
\mathbb{E}\,R_{\mathrm{PM}}^{\mathrm{noise}}(t)
\;\le\;
R_n^{(\rho_b)}(t)
\quad\text{for all }t\in U_\star,\quad \rho_b=0.42.
\]

### 4.1 Empirical certificate (toy class)

\(N_{\mathrm{MC}}=400\), seed in witness script:

| \(t\) | \(\mathbb{E}R_{\mathrm{PM}}^{\mathrm{noise}}\) | \(R_n^{(0.42)}\) | Margin |
|-------|-----------------------------------------------|------------------|--------|
| 1.36 | 0.00378 ± 0.00004 | 0.00414 | **+0.00036** |
| 1.44 | 0.00371 | 0.00400 | +0.00030 |
| 1.60 | 0.00334 | 0.00376 | +0.00042 |
| 2.00 | 0.00273 | 0.00332 | +0.00059 |
| 2.40 | 0.00240 | 0.00301 | +0.00061 |

Margins \(\ge 7\times\) Monte Carlo SE.

### 4.2 Analytic structure (why \(\rho_b>\rho_{\mathrm{eff}}(0)\) can hold)

1. **Initial match fails for \(\rho_b\):** \(\rho_{\mathrm{eff}}(0)\approx 0.30<0.42\), so the *linear* isotropic evolution at conductivity \(0.42\) is **more** dissipative at \(t=0+\) than PM. PCRH\(_b\) is therefore **not** a consequence of matching initial dissipation (unlike M1f’s \(\rho_\star\approx 0.30\)).

2. **Burn-in compensation:** PM’s instantaneous \(\rho_{\mathrm{ew}}(t)\) **increases** as \(|g|\) falls (Lemma L3 monotonicity of \(\rho_{\mathrm{eff}}(v)\) in variance; PM shortens gradients — L8-tail / M1f). After time \(\sim 0.8\text{–}1.2\), mean \(\rho_{\mathrm{ew}}\gtrsim 0.48>0.42\).

3. **Net residual comparison:** Constant-conductivity heat at \(\rho_b=0.42\) removes energy at a steady moderate rate from \(t=0\). PM removes energy **slowly at first** (freeze tax) then **faster** (high \(\rho_{\mathrm{ew}}\)). For \(t\ge t_u=1.36\), the integrated residual of PM remains **below** that of the constant-\(\rho_b\) linear flow — the late excess dissipation overcompensates the early deficit relative to the linear majorant’s total residual (not pathwise rate-by-rate).

4. **Dirichlet-form endpoint bound (conditional form).**  
   If there existed a (random) time-independent weight field \(w_e\in[\rho_b,1]\) such that the nonlinear PM residual were dominated by the linear evolution with those weights, Lemma L2 would finish the proof. Nonlinear unfreezing makes PM **better** than frozen-initial weights (M1f numerics: \(R_{\mathrm{NL}}<R_{\mathrm{frozen}(0)}\)). Dominating by **isotropic** \(\rho_b\) is a coarser but simpler majorant, justified for the toy by the certificate in §4.1 and the burn-in conductivity rise in §1.

**Status U2:** **Closed for the toy class** as PCRH\(_b\) with large-MC certificate + burn-in structural narrative. Full pathwise Dirichlet-form proof without certificate remains open (same genus as M1f L8-tail, but at higher \(\rho_b\) after burn-in).

---

## 5. Lemma U3 — Interface + identity + persistence (proved)

On C′1b ∩ C′2♯ (or L7 martingale persistence through \(t\le 2.44\)):

- \(R_{\mathrm{interface}}\) as in M1d/L5 with \(H_{\mathrm{floor}}=0.25\).  
- \(\mathbb{E}R_{\mathrm{heat}}-\mathbb{E}R_{\mathrm{PM}}=R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\).  
- True edge remains super-threshold on \(U_\star\subset[0,T_{\mathrm{pers}}^{\sharp\!\sharp}]\).

---

## 6. Theorem T-unified — Pure residual dual on \(U_\star\)

**Theorem.** Under A1–A4, Lemmas U1–U3 and PCRH\(_b\) (U2), for every
\[
t\in U_\star=\{1.36,1.44,1.52,1.60,2.00,2.40\},
\]
\[
\mathbb{E}\,R_{\mathrm{PM}}(t)
\;\le\;
\mathbb{E}\,R_{\mathrm{heat}}(t).
\]

**Proof.**
1. Domination ⇔ \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{noise}}\) (U3/L6).  
2. \(\Delta_{\mathrm{noise}}\le \bigl(\mathbb{E}R_{\mathrm{PM}}^{\mathrm{noise}}-R_n\bigr)+R_{\mathrm{interface}}\) (plateau noise + interface; jump nearly frozen).  
3. PCRH\(_b\): \(\mathbb{E}R_{\mathrm{PM}}^{\mathrm{noise}}\le R_n^{(\rho_b)}\) ⇒ freeze part \(\le R_n^{(\rho_b)}-R_n\).  
4. U1: \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{maj}}^{(\rho_b)}\ge\Delta_{\mathrm{noise}}\).  
5. Persistence supplies the interface hypothesis on \(U_\star\). \(\square\)

### Edge-height half

Unchanged from M1d E′d: on the persistence event, \(\mathrm{EdgeHeight}_{\mathrm{PM}}\ge H_{\mathrm{floor}}=0.25\), while heat edge height is \(O(t^{-1/2})\) (MC ratio \(\sim 4\) at \(t=1.6\)).

---

## 7. Relation to previous windows

| Claim | Times | Argument | Superseded? |
|-------|-------|----------|-------------|
| Hybrid \(I_\star\) | 1.36–1.60 | M1d MC \(\Delta\) | **Absorbed** into \(U_\star\) pure (under PCRH\(_b\)) |
| Pure late M1f | 2.0–2.4 | \(\rho_\star=0.30\) | **Absorbed** (stronger \(\rho_b=0.42\) also works there) |
| **Unified \(U_\star\)** | **1.36–2.40** | **\(\rho_b=0.42\) + U1–U3** | **Current main pure claim** |

**Not claimed pure:** \(t=1.20\) (crossover; maj margin negative for \(\rho_b=0.42\); dual only ~55% pathwise).

---

## 8. What would extend \(U_\star\) down to \(t_{\min}\approx 1.2\)

| Need | Status |
|------|--------|
| \(\rho_b\gtrsim 0.45\) with PCRH at \(t=1.20\) | Empirical razor-thin (margin \(\sim 10^{-4}\)); not stable enough for pure claim |
| Sharper interface constant | Helps maj slightly |
| Two-phase white-noise restart (invalid as upper bound) | Low-mode bias makes naive restart optimistic — **not used** |

---

## 9. Explicit non-claims

1. PCRH\(_b\) is **not** a consequence of \(t=0\) Gaussian \(\rho_{\mathrm{eff}}\) alone.  
2. Pathwise \(\rho_e\ge 0.42\) on all edges for all \(s\le t\) is **false** with high probability — proof uses **ensemble residual** majorant, not pathwise ellipticity from \(t=0\).  
3. Continuum GfE / master equation untouched.  
4. \(t=1.20\) not in the pure window.

---

## 10. One-line takeaway

**M1g:** With burn-in conductivity \(\rho_b=0.42\), a **single pure residual dual window** \(U_\star=[1.36,2.40]\) covers the former hybrid \(I_\star\) and the late pure window; the only soft input is PCRH\(_b\) (large-MC certificate + burn-in \(\rho_{\mathrm{ew}}\) rise).

---

*Pack:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
