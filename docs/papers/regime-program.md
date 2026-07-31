# Regime Program — Testing whether entropy production decouples from stress-energy

**Status:** Research program note (written 2026-07-30) · Preliminary research
**Purpose:** Elaborate the *constructive route* of [FALSIFIABILITY_L_vs_GR.md](FALSIFIABILITY_L_vs_GR.md) §5.1: what it would take to **find or rule out** a regime in which the computational-entropy-production rate \(dS_c/d\tau\) is **not** a function of the stress-energy \(T_{\mu\nu}\) — the one place the load framework could depart from GR rather than merely reformulate it.
**Stance:** The default verdict is **reformulation** ([FALSIFIABILITY](FALSIFIABILITY_L_vs_GR.md)); this note does **not** claim a departure. It specifies the experiments that could establish or exclude one. Either outcome is pre-accepted.
**Feeds:** OPEN_AVENUES experiment bucket (C) · Paper B §6 (the semantic bridge).

---

## 0. Why this note exists

Since the load framework reproduces GR on-shell (the Jacobson generator), any genuine departure must live in the **clock** term \(d\tau=dt/(1+\alpha L)\), specifically the entropy-production term \(\gamma\lvert dS_c/d\tau\rvert\). That term departs from GR **iff** \(dS_c/d\tau\) carries information not already in \(T_{\mu\nu}\). Whether such a regime exists is the program's sharpest open physical question. This note defines "regime," lists the regimes worth testing, and orders the experiments.

## 1. Prerequisite (do this first): operationally define \(dS_c/d\tau\)

Every regime is ill-posed until \(S_c\) is pinned down. Two facts force the setup:

- **Closed unitary ⇒ zero production.** Von Neumann entropy of a closed system is constant, so \(dS_c/d\tau=0\) for isolated systems. The term is identically zero unless the system is **open** (a channel with an environment).
- **Open ⇒ built-in degeneracy risk.** Coupling to an environment generically exchanges energy, and energy is in \(T_{\mu\nu}\). So the naive expectation is degeneracy.

**Refined target.** Not "decouple entropy from stress-energy" in general, but:
> *Is there an **open-system** process producing \(S_c\) at a rate we can dial while its energy exchange (hence \(T_{\mu\nu}\)) stays fixed?*

**Modeling decision required:** which channel and which coarse-graining define \(S_c\) (global output state? a subsystem's reduced state? our classical export density \(\sigma\) promoted to a quantum channel?). This choice determines every regime below and must be fixed before Stage 1.

## 2. What a "regime" is (definition)

A **regime** is a parameterized family of configurations with three handles:

1. **Knob** — a control that varies \(dS_c/d\tau\).
2. **Fixed \(T_{\mu\nu}\)** — held constant or precisely tracked as the knob turns.
3. **Clock observable** — a proper-time / rate measurement.

Decoupling holds in the regime iff moving handle 1 with handle 2 fixed moves handle 3. If handle 3 never responds at fixed \(T_{\mu\nu}\), the regime is a **reformulation witness**; if it responds, a **departure witness**. All definitional content is in *how handle 1 is realized at fixed handle 2*.

## 3. Do we need several regimes? Yes.

The degeneracy is **regime-dependent** — broken in some processes, not others — so no single regime can settle it. We need a positive candidate, a negative control, and a definitional anchor:

| Regime | Knob for \(dS_c/d\tau\) | \(T_{\mu\nu}\) decoupled? | Role |
|--------|--------------------------|---------------------------|------|
| **R1 — Pure dephasing** | dephasing rate \(1/T_2\) | **Yes** — dephasing (\(T_2\)) produces entropy with **no energy exchange**, unlike relaxation (\(T_1\)) | **Candidate departure** (best case) |
| **R2 — Landauer erasure** | erasure rate | **No** — erased-bit heat \(\ge kT\ln2\) is energy | **Negative control** (should show no departure) |
| **R3 — Unitary scrambling of a subsystem** | scrambling rate | global energy fixed; **subsystem** \(S_c\) changes | **Definitional anchor** (forces the coarse-graining choice) |

Rationale for needing all three: R1 is where a departure could live; R2 must behave degenerately (if it showed a departure, the model is wrong); R3 forces us to say which coarse-graining \(S_c\) uses, without which R1's dephasing entropy can't be trusted as the right object. **Pure dephasing (R1) is the canonical candidate** because it is the standard process that produces entropy at fixed energy.

## 4. The experiments, in honest order

### Stage 1 — Computational (our tools) — **DONE (2026-07-30): decoupling exhibited**

Built as an open-qubit Lindblad model: `simulations/regime/regime_decoupling_witness.py`.

- **R1 pure dephasing** (\(L=\sqrt{g}\,\sigma_z\)): energy \(E=\operatorname{Tr}(\rho H)\) is **exactly constant** (\(0.5\)) while \(S_c\) rises \(0\to1\) bit; \(dE/dt\equiv0\), so the coupling \(\kappa=\lvert dE/dt\rvert/\lvert dS_c/dt\rvert\approx10^{-14}\). The full load clock **dilates** where the energy-only clock does not.
- **R2 amplitude damping** (\(L=\sqrt{g}\,\sigma_-\)): \(E\) relaxes as \(S_c\) is produced; \(\kappa\approx0.42>0\) — the degenerate control behaves as expected (entropy rides with heat flux, which is in \(T_{\mu\nu}\)).
- **R3 two-qubit unitary**: global \(\langle H\rangle=0\) conserved while a **subsystem's** \(S_c\) rises \(0\to1\) bit — confirming that the coarse-graining choice *defines* whether production exists.

**Result.** The entropy-production term is **not generally reabsorbable into the energy term**: pure dephasing produces \(S_c\) at fixed local energy with **no heat flux**, so it lies outside the local stress-energy. The *"always reformulation via reabsorption"* horn is **ruled out for R1** — a departure exists **in principle**.

Rigor: **constructive model witness** (structural weights \(\alpha=\beta=\gamma=1\); no continuum/gravity claim).

### Stage 2 — Calibrate \(\gamma\) and the magnitude — **DONE (2026-07-31)**

Witness: `simulations/regime/regime_gamma_calibration.py`.

- **Dimensional analysis (derivable):** \(\gamma\) has units of **time** (since \(\lvert dS_c/d\tau\rvert\sim1/\text{time}\) and \(L\) is dimensionless). Candidate fundamental times: Planck \(t_{\rm Pl}=5.4\times10^{-44}\,\)s, electron Compton \(1.3\times10^{-21}\,\)s, Margolus–Levitin (optical) \(5.8\times10^{-16}\,\)s.
- **Structural gap (the real blocker):** the stated calibration \(\alpha\beta=4\pi G/c^4\) is **dimensionally inconsistent** with dimensionless \(\alpha,\beta,L\) (\(4\pi G/c^4\) is dimensionful, \(\sim10^{-43}\,\mathrm{s^2\,kg^{-1}\,m^{-1}}\)). So the master equation **does not fix** \(\gamma\) (nor \(\alpha\)).
- **Observable:** the fractional dephasing clock shift depends only on \(\eta\equiv\alpha\gamma\) (time): \(\delta\sim\eta/T_2\).
- **Empirical bound:** precision-clock null results (no dephasing-dependent shift at \(\sim10^{-18}\)) already require \(\alpha\gamma\lesssim10^{-18}\,\text{s}\) (for \(T_2\sim1\,\)s). This *already excludes* \(\gamma\sim\)ML-optical with \(\alpha\sim1\) (\(\delta\sim6\times10^{-16}\gg10^{-18}\)); \(\gamma\sim t_{\rm Pl}\) is unmeasurable (\(\delta\sim10^{-44}\)).

**Result.** For every *natural* parameter choice the effect is either **unmeasurable** (fundamental \(\gamma\)) or **already excluded** (order-unity \(\alpha\) with microscopic \(\gamma\)). No currently-observable prediction exists without an unmotivated, un-suppressed \(\alpha\gamma\). **Reformulation in practice** — the Stage-1 departure is real in principle but not observable. The genuine missing step is a **dimensionally-consistent completion of the load constants**, not a larger experiment.

### Stage 3 — Physical experiment — **not warranted (as things stand)**

Precision clocks under controlled dephasing would be the apparatus, and they *already* provide the bound in Stage 2. A dedicated experiment is not warranted until the theory supplies a \(\gamma\) (Stage-2 structural fix) predicting \(\alpha\gamma\) in the narrow, currently-unmotivated window \([\sim10^{-24},\sim10^{-18}]\,\)s that is both allowed and reachable.

## 5. Outcome so far

**Stage 1 confirmed the "in principle" horn.** The model witness (above) shows the decoupling is *real*: pure dephasing produces \(S_c\) at fixed local energy with no heat flux, so the entropy-production term is not reabsorbable into stress-energy for R1. This is genuine progress — it **rules out** the possibility that the framework is a reformulation *purely by reabsorption*, at least for the dephasing regime.

**Stage 2 resolved the magnitude question — as a no-go for observability.** The observable depends only on \(\eta=\alpha\gamma\); the master equation cannot fix it (the \(\alpha\beta=4\pi G/c^4\) calibration is dimensionally inconsistent). Bounding \(\eta\) by existing precision-clock null results (\(\alpha\gamma\lesssim10^{-18}\,\)s) and by natural fundamental-time values of \(\gamma\), the effect is **unobservable for every natural parameter choice** (and an order-unity \(\alpha\) with microscopic \(\gamma\) is *already excluded* by clocks).

**The dimensional rebuild then closed it structurally** ([../emergent-gravity/load-dimensional-analysis.md](../emergent-gravity/load-dimensional-analysis.md)). The correct calibration is the on-shell identity \(\alpha L=-\Phi/c^2\), fixed by \(T_{\mu\nu}\). But the entropy term varies at fixed \(T_{\mu\nu}\) (Stage 1) — so the load **cannot** be both the gravitational clock and an independent entropy clock. The entropy-production term therefore carries **no independent, gravity-consistent clock effect**; the load is a **diagnostic co-moving with the Path-J/M metric**. **Net: reformulation *structurally*** — \(\alpha\gamma\) is not even a physical observable. The regime program's experimental track is closed on structural grounds; a genuine departure would require a *different* theory (promoting load terms into the field equations, R4a).

## 6. Non-claims (stand)

- No claim that a departure exists; the default verdict is **reformulation**.
- \(\sigma(x)\) (Paper C) is a **classical** density; identifying it — or any \(dS_c/d\tau\) — with the load term is the labeled semantic step under test, **not** asserted (non-claim 10 / N9).
- No physical experiment is warranted until Stage 1–2 produce a *quantified* prediction; a bare clock comparison with no predicted magnitude tests nothing.

## 7. Links

| Resource | Role |
|----------|------|
| [FALSIFIABILITY_L_vs_GR.md](FALSIFIABILITY_L_vs_GR.md) | Verdict (reformulation); §5.1 constructive route this note elaborates |
| [04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md](04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md) §6 | The semantic bridge \(\sigma\leftrightarrow\) load term |
| [02-computational-models/PAPER_C_decay_algebra.md](02-computational-models/PAPER_C_decay_algebra.md) | Classical density \(\sigma(x)\) (Stage-1 starting point) |
| [../synthesis/OPEN_AVENUES.md](../synthesis/OPEN_AVENUES.md) §5 | Experiment bucket (C) |
| [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) | Load term \(\gamma\lvert dS_c/d\tau\rvert\) |
| `simulations/regime/regime_decoupling_witness.py` | Stage-1 open-qubit witness (R1/R2/R3) |
| `simulations/regime/regime_gamma_calibration.py` | Stage-2 \(\gamma\) calibration / clock-magnitude bound |

---

## Changelog

| Date | Entry |
|------|-------|
| 2026-07-30 | Initial program note: operational-\(S_c\) prerequisite; regime definition; regimes R1–R3 (dephasing / erasure / scrambling); staged experiments (computational → magnitude → precision clocks); reformulation default. |
| 2026-07-30 | **Stage 1 DONE:** open-qubit witness shows pure dephasing decouples (\(\kappa\approx0\), \(E\) fixed, \(S_c\) rises); R2 coupled control (\(\kappa\approx0.42\)); R3 coarse-graining anchor. Reabsorption horn ruled out for dephasing; magnitude (\(\gamma\) calibration) now the open blocker. |
| 2026-07-31 | **Stage 2 DONE:** \(\gamma\) has units of time but the master eq's \(\alpha\beta=4\pi G/c^4\) is dimensionally inconsistent ⇒ \(\alpha\gamma\) unfixed. Clock null-results bound \(\alpha\gamma\lesssim10^{-18}\,\)s; natural \(\gamma\) ⇒ unmeasurable, order-unity \(\alpha\) + microscopic \(\gamma\) ⇒ already excluded. **Reformulation in practice.** True blocker = dimensional completion of load constants. |
