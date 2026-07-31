# Falsifiability Analysis — Does the load \(L\) predict anything GR doesn't?

**Status:** Gating analysis (written 2026-07-29) · Preliminary research
**Purpose:** Determine whether the computational-load framework is a **reformulation** of GR or a **candidate new theory**, by asking whether the load clock produces a departure from general relativity that is, in principle, measurable.
**Gates:** Paper B framing (see [DELIVERY_SCOPE.md](DELIVERY_SCOPE.md) B1, B6).
**Verdict authority:** frozen non-claims [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md).

---

## 1. The object under test

The framework's dynamical content is the load-reparameterized clock and master equation ([../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)):

$$
d\tau = \frac{dt}{1+\alpha L(\rho,g)}, \qquad
\frac{d\rho}{dt} = \frac{1}{1+\alpha L}\,\mathcal{L}_g[\rho;g_{\mu\nu}(\rho)],
$$

$$
L(\rho,g) = \underbrace{\beta\,\frac{E[\rho]}{V\epsilon_0}}_{\text{(1) energy}}
+ \underbrace{\gamma\left|\frac{dS_c}{d\tau}\right|_{\rm reg}}_{\text{(2) entropy production}}
+ \underbrace{\delta\,\frac{S_{\rm boundary}(\rho)}{S_{\rm BH}(A)}}_{\text{(3) boundary}} .
$$

The generator \(\mathcal{L}_g\) is **required** to satisfy Clausius \(\delta Q = T\,dS_c\) on local horizons — i.e. Jacobson's condition, which yields the Einstein equations. So **on-shell the geometry is GR by construction.** Any new physics must therefore live in the *clock* term \(L\), not in the field equations.

The sharp question: **is \(L\) a function of the stress-energy \(T_{\mu\nu}\) alone?** If yes, the load clock is a rewrite of GR proper time and predicts nothing new. If some term in \(L\) depends on data *not* carried by \(T_{\mu\nu}\), that term is a candidate departure.

---

## 2. Term-by-term

| Term | Depends on | New vs GR? | Testability |
|------|-----------|------------|-------------|
| **(1) energy** \(\beta E/V\epsilon_0\) | local energy density (in \(T_{\mu\nu}\)) | **No.** Calibrated to reproduce Newtonian/GR gravitational redshift (\(\alpha\beta=4\pi G/c^4\)). | — (reproduces GR) |
| **(2) entropy production** \(\gamma\lvert dS_c/d\tau\rvert\) | *rate of irreversible information processing* — **not** a component of \(T_{\mu\nu}\) in GR | **Potentially yes.** GR proper time is metric-only; it has no dependence on how fast matter scrambles/decoheres at fixed energy. | In principle: two systems, equal stress-energy, different irreversible-computation rate → different tick rate. |
| **(3) boundary** \(\delta S_{\rm boundary}/S_{\rm BH}\) | holographic screen occupation | **Potentially yes,** but only bites as \(S_{\rm boundary}/S_{\rm BH}\to 1\) (near horizons). | Strong-field / quantum-gravity regime only; not currently accessible; degenerate with other QG proposals. |

---

## 3. The one candidate departure — and why it isn't sharp yet

**Term (2) is the only term that could give a low-energy, in-principle-measurable departure from GR.** In GR, two configurations with identical \(T_{\mu\nu}\) tick identically. Here, the one with higher regularized computational-entropy production rate would tick *slower* (higher \(L\), locked reading: active scrambling → higher \(L\)). That is a genuine, GR-distinguishing statement.

**Three deflating caveats keep it from being a sharp prediction today:**

1. **Degeneracy with effective stress-energy.** Irreversible entropy production is usually accompanied by heat flux, and heat flux *is* in \(T_{\mu\nu}\) — which already gravitates in GR, so term (2) *could* be reabsorbable into an effective source. **Update (2026-07-30):** a decoupled regime **has now been constructed** — pure dephasing produces \(S_c\) at fixed local energy with no heat flux (\(\kappa=\lvert dE/dt\rvert/\lvert dS_c/dt\rvert\approx0\)), so term (2) is **not** reabsorbable there ([REGIME_PROGRAM_dSc_decoupling.md](REGIME_PROGRAM_dSc_decoupling.md), Stage 1; `simulations/regime/regime_decoupling_witness.py`). The reabsorption horn is thus **excluded for dephasing**; the open question is now the *magnitude* (caveat 2), not the existence of a decoupled regime.
2. **Calibration suppresses it — now a structural no-go.** \(\gamma\) has units of time; the master equation's \(\alpha\beta=4\pi G/c^4\) is dimensionally inconsistent and the correct calibration is the on-shell identity \(\alpha L=-\Phi/c^2\) ([../emergent-gravity/load-dimensional-analysis.md](../emergent-gravity/load-dimensional-analysis.md)). That identity fixes \(\alpha L\) by \(T_{\mu\nu}\), yet the entropy-production term **varies at fixed \(T_{\mu\nu}\)** (Stage 1). The two are consistent only if the entropy term makes **no independent contribution to proper time** — i.e. the load is a **diagnostic co-moving with the Path-J/M metric**, not an independent clock. So \(\alpha\gamma\) is not an observable at all (the earlier clock bound \(\alpha\gamma\lesssim10^{-18}\)s stands as an empirical consistency check). **Verdict strengthened: reformulation *structurally*, not merely in practice.** Making the load *generate* gravity would require promoting load terms into the field equations (R4a) — a different theory.
3. **The term is regularized/averaged** over a Margolus–Levitin window explicitly to avoid circularity — which further suggests it is subtle, not a large leading effect.

---

## 4. Verdict

> **VERDICT (2026-07-29): REFORMULATION, with one flagged candidate departure.**
>
> As currently constructed the load framework reproduces GR on-shell (Jacobson generator) and calibrates term (1) to GR redshift; it makes **no sharp, calibration-independent prediction that differs from GR** in any presently accessible regime. It is therefore an **information-theoretic reformulation** of thermodynamic gravity.
>
> The **entropy-production term (2)** was the single most promising place a genuine departure could live. **Update (2026-07-31):** this candidate is now **structurally closed**. The regime program traced it to a decoupling (Stage 1: entropy production at fixed \(T_{\mu\nu}\)), then a dimensional rebuild showed a **no-go** ([../emergent-gravity/load-dimensional-analysis.md](../emergent-gravity/load-dimensional-analysis.md)): a load that clocks the gravitational proper time (\(\alpha L=-\Phi/c^2\), fixed by \(T_{\mu\nu}\)) cannot also contain a term that varies at fixed \(T_{\mu\nu}\) — so the entropy term carries **no independent, gravity-consistent clock effect**. The load is a **diagnostic co-moving with the Path-J/M metric**, not an independent clock. **Verdict strengthened: reformulation *structurally*.** A genuine departure would require a *different* theory (promoting load terms into the field equations, R4a).

**Consequences for Paper B (per [DELIVERY_SCOPE.md](DELIVERY_SCOPE.md)):**

- Frame the paper as a **reformulation / research programme** (B1), *not* as a competitor theory.
- State the falsifiability question (B6) explicitly and record this verdict.
- Elevate **term (2)** to the paper's central open problem: the concrete missing result is *"exhibit a regime where \(dS_c/d\tau\) is not a function of \(T_{\mu\nu}\), compute the calibrated \(\gamma\)-residual, and derive a clock-rate prediction distinct from GR — or prove no such regime exists (degeneracy no-go)."*
- This is consistent with — and sharpens — non-claim N1 (master eq \(\not\Leftrightarrow\) GfE) and the Path J/M honesty (C9–C10).

---

## 5. What would flip the verdict to "new theory"

Either of:

1. **Constructive:** a physical or model regime with \(dS_c/d\tau \neq f(T_{\mu\nu})\), a computed non-negligible \(\gamma\)-residual, and a resulting clock/timing prediction that GR does not make (then bucket C: a real experiment — precision clocks near strongly irreversible processes, decoherence-heavy environments, etc.). **How to define such a regime and which experiments find or rule it out:** [REGIME_PROGRAM_dSc_decoupling.md](REGIME_PROGRAM_dSc_decoupling.md) (operational-\(S_c\) prerequisite; regimes R1 dephasing / R2 erasure / R3 scrambling; staged computational → magnitude → precision-clock experiments).
2. **Structural no-go against reformulation:** a proof that the Jacobson generator is *incompatible* with the three-term load unless the load is promoted into the field equations — which would force new metric-level content (this is the R4a "promotion" theme).

**Update (2026-07-31) — R4a done.** Route 1 (load-clock) is closed by the no-go. Route 2 (promotion into the field equations) was run ([../emergent-gravity/r4a-promotion.md](../emergent-gravity/r4a-promotion.md); `simulations/gravity-toy/r4a_frw_promotion.py`): it yields a **consistent, GR-reducing candidate hypothesis** — a Landauer-coupled interacting dark sector giving **phantom** dark energy \(w_0=-1-0.143\,\xi\), already bounded by data to \(\xi<0.35\). So a departure now exists **as a testable model**, with one free coupling \(\xi\); its cosmological reality is undetermined pending that coupling (the same calibration gap). **Status: reformulation as a *clock*; candidate modified-gravity hypothesis under *promotion*.** The single decisive open question is whether the theory fixes \(\xi\) away from 0.

---

## 6. Changelog

| Date | Entry |
|------|-------|
| 2026-07-29 | Initial analysis; verdict = reformulation + flagged entropy-production candidate departure (term 2). |
