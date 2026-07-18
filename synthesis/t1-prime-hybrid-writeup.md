# T1′ Hybrid Dual — Paper-Ready Write-Up

**Status:** Paste-ready intermediate research result (2026-07-14)  
**Scope:** Euclidean ACD-EW residual dual only — not continuum GfE equivalence  
**Canonical math:** [m1d](m1d-lemma-e-prime.md) · [m1c](m1c-c2-sharp-delta-noise.md) · [m1e](m1e-freeze-tax-spectral.md) · [m1f](m1f-hrho-pure-proof.md) · [m2](m2-t1-load.md)  
**Witnesses:** `t1_eprime_envelope.txt`, `t1_delta_noise_envelope.txt`, `t1_load_m2_envelope.txt`, `t1_pure_hrho_envelope.txt`

---

## Abstract (≤120 words)

On a one-dimensional lattice with a single unit jump observed in i.i.d. Gaussian noise, explicit-Euler Perona–Malik (PM) anisotropic diffusion beats isotropic heat in expected residual MSE on an intermediate time window, while retaining the jump edge. Ultra-short times favor heat (noise race); intermediate times favor PM (edge freeze vs jump blur). We prove height persistence under a high-probability initial-height event, reduce residual comparison to an exact identity \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{noise}}\), and establish a **hybrid** residual dual on a nonempty grid \(I_\star\subset[1.2,1.67]\). Load-gated PM inherits the dual as a slower clock. This is a constructive Euclidean dual (ACD-EW), not a continuum gravity theorem.

---

## 1. Setting (one paragraph)

Sites \(i=0,\ldots,N-1\) (\(N=192\)), hidden step \(\phi_\star=\mathbf{1}_{i\ge N/2}\), observation \(y=\phi_\star+\eta\) with \(\eta_i\sim\mathcal{N}(0,\sigma^2)\), \(\sigma=0.12\). Reconstructors start at \(y\) and use explicit Euler with step \(dt=0.08\): heat flux \(F=\nabla\phi\); PM flux \(F=\rho\nabla\phi\) with \(\rho=1/(1+(\nabla\phi/K)^2)\), \(K=0.15\); load-PM uses the same PM vector field with \(dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}})\). Residual \(R=N^{-1}\|\hat\phi-\phi_\star\|_2^2\).

---

## 2. Main claims (labeled)

### Claim A — Time-windowed residual dual (unified pure)

**Unified pure window** \(U_\star=[1.36,2.40]\) ([m1g](m1g-unified-pure-window.md)):
\[
\mathbb{E}\,R_{\mathrm{PM}}(t)\le\mathbb{E}\,R_{\mathrm{heat}}(t)
\]
under spectral majorant with burn-in conductivity \(\rho_b=0.42\), Dirichlet-form linear theory, interface bound, and PCRH\(_b\) (ensemble residual majorant; large-MC certificate).

Covers former hybrid \(I_\star\) and former pure-late \([2.0,2.4]\) in **one** pure argument.  
Crossover \(t\approx 1.2\) remains outside the pure window (dual only ~50–55% pathwise).

**Status:** **Unified pure claim on \(U_\star\)** (soft input: PCRH\(_b\)).

### Claim B — Edge persistence (analytic on high-probability event)

With probability \(\gtrsim 0.87\), initial true jump height \(H^0\ge 0.80\). On that event, for all \(t\le T_{\mathrm{pers}}^\sharp\approx 1.67\),

\[
H^t \ge H_{\mathrm{floor}}=0.25 > K
\]

(super-threshold freeze; Lemma C′2♯).

**Status:** **Analytic** (flux ODE bound + Gaussian concentration).

### Claim C — Short-time obstruction (experimental + identity)

For \(t\lesssim 1.2\), heat wins residual because noise reduction dominates jump blur. The identity

\[
\mathbb{E}(R_{\mathrm{heat}}-R_{\mathrm{PM}})
=
R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}
\]

holds to numerical precision; crossover when \(R_{\mathrm{blur}}=\Delta_{\mathrm{noise}}\) at \(t\approx 1.2\).

**Status:** **Explained** (not a dual failure).

### Claim D — Load clock (hybrid M2)

Load-PM is a monotone time change of pure PM: internal time \(\tau(t)=\int_0^t(1+\alpha_L L_{\mathrm{clock}})^{-1}ds\le t\). Empirically \(\tau/t\approx 0.95\text{–}0.98\) on the window. For \(t\in I_\star\),

\[
\mathbb{E}\,R_{\mathrm{load\text{-}PM}}(t)
\;\le\;
\mathbb{E}\,R_{\mathrm{heat}}(t)
\]

with high Monte Carlo support (frac \(\ge 0.73\) at \(t=1.36\), \(\ge 0.97\) at \(t=1.60\)).

**Status:** **Hybrid / experimental** ([m2](m2-t1-load.md)); time-change identity is definitional.

---

## 3. Mechanism (three sentences)

Heat must blur the unit jump on scale \(\sqrt{t}\), contributing deterministic residual \(R_{\mathrm{blur}}=\Theta(\sqrt{t}/N)\). PM nearly freezes the true edge (\(\rho\ll 1\) for \(|\nabla|\gg K\)) and denoises plateaus, but freezes some noise gradients too, creating a noise-race tax \(\Delta_{\mathrm{noise}}\). Residual dual holds when blur exceeds that tax.

---

## 4. What this is not

| Non-claim |
|-----------|
| Full pure-analytic T1′ for all continuous \(t\) with no hypotheses |
| T1 residual domination on every \((0,t_\star]\) |
| Continuum Lorentzian GfE \(\Leftrightarrow\) gravitational master equation |
| Lattice denoising as empirical gravity |
| Identity of toy \(H_c\) with von Neumann \(S_c\) |

---

## 5. Paste-ready “we have / have not” (update)

### We have (additions beyond prior transfer note)

- A **hybrid T1′ residual dual** on a nonempty intermediate time grid \(I_\star\), with analytic edge persistence through \(t\approx 1.67\) and an exact residual accounting identity.
- An **explanation** of the ultra-short heat win as a noise-vs-blur race (\(\Delta_{\mathrm{noise}}\) vs \(R_{\mathrm{blur}}\)).
- **Load-gated PM** experimental residual dual vs heat on the same window (clock dual / M2 hybrid).
- A **spectral freeze-tax majorant** (conductivity \(\rho_{\mathrm{typ}}\)) that closes \(R_{\mathrm{blur}}\ge\Delta\) on \(I_\star\) under an explicit plateau-conductivity hypothesis.

### We have not

- A fully unconditional spectral proof of freeze tax without conductivity hypothesis or MC.
- Continuum GfE / master-equation equivalence.
- Theorem-level multi-jump, 2D, or continuum SPDE residual domination.

---

## 6. Suggested paper citation sentence

> In a 1D lattice observation model with a single noisy jump, Perona–Malik residual domination over isotropic heat holds on an intermediate time window (hybrid T1′), with analytic edge persistence and a precise noise-versus-blur accounting; load reparameterization preserves the dual experimentally as a slower clock on the same flow. This supports a constructive Euclidean action–channel dual (ACD-EW), not continuum gravitational equivalence.

---

## 7. Reproduction

```bash
.venv/bin/python simulations/bridging/test_t1_eprime.py
.venv/bin/python simulations/bridging/test_t1_delta_noise.py
.venv/bin/python simulations/bridging/test_t1_load_m2.py
.venv/bin/python simulations/bridging/_joint_toy_v2_core.py
```

---

*Companion to [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md). Update when pure E′c is fully closed.*
