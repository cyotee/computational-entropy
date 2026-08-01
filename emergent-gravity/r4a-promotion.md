# R4a promotion — entropy production in the field equations

**Status:** Candidate-hypothesis result (2026-07-31) · Preliminary research
**Follows:** the load no-go [load-dimensional-analysis.md](load-dimensional-analysis.md) (departure needs field-equation promotion)
**Witness:** `simulations/gravity-toy/r4a_frw_promotion.py`
**External kin:** Bianconi \(\Lambda_G\) / G-field ([../papers/external/](../papers/external/)); Thattarampilly–Zheng inflation-from-entropy

The no-go closed the load-as-clock route. The only remaining path to a genuine departure from GR is **R4a**: promote the entropy-production content into the **field equations** (metric-level content), not the clock. This note runs that promotion in a cosmology and finds it yields a **consistent, GR-reducing, testable candidate hypothesis** — not invalidation, and not (yet) a validated theory.

---

## 1. The promotion

Minimal, generally-covariant ansatz: add a perfect-fluid **computational sector** as a source,
$$
G_{\mu\nu}=\kappa\big(T^{\rm matter}_{\mu\nu}+T^{S}_{\mu\nu}\big),\qquad \kappa=\tfrac{8\pi G}{c^4},
$$
with \(T^S\) built from the entropy-production density (Paper C's \(\sigma\), carried to an energy density by the Landauer scale). Take the vacuum-like intrinsic equation of state \(w_S=-1\) (the least-structure choice; it is the term that plays Bianconi's \(\Lambda_G\) role).

## 2. The Bianchi fork (the rigorous core)

\(\nabla^\mu G_{\mu\nu}=0\) is a geometric identity, so **total** conservation \(\nabla^\mu(T^{\rm matter}+T^S)_{\mu\nu}=0\) is automatic. The physics is in the split:

- **(a) Matter separately conserved** \(\Rightarrow \nabla^\mu T^S_{\mu\nu}=0\Rightarrow \partial_\nu\rho_S=0\Rightarrow \rho_S=\)const. The computational sector is just a **cosmological constant \(\Lambda\)** — **no new physics** (reproduces \(\Lambda\)CDM's \(\Lambda\), does not predict its value).
- **(b) \(\rho_S\) dynamical (tracks entropy production)** \(\Rightarrow \nabla^\mu T^{\rm matter}_{\mu\nu}=-\nabla^\mu T^S_{\mu\nu}\neq0\): **energy \(Q\) is exchanged** between matter and the computational sector.

**Branch (b) sign is *derived*, not merely "Landauer-motivated" (see §4c):** the framework's locked reading (load = entropy **flux**, not stockpile) plus the second law force \(Q\ge0\) (matter → computational sector), so \(\rho_S\) grows. This is a standard *interacting dark energy* structure whose coupling is the Landauer power of cosmological entropy production — the classical core supplies it. (An earlier version of this note said "sign fixed by Landauer"; the sharper statement is §4c.)

## 3. FRW model and results

Flat FRW, dust matter + \(w_S=-1\) sector, coupling \(Q=\xi H\rho_m\):
$$
\dot\rho_m+3H\rho_m=-Q,\qquad \dot\rho_S=+Q,\qquad H^2=\tfrac{8\pi G}{3}(\rho_m+\rho_S).
$$
Closed form: \(\rho_m=\rho_{m0}\,a^{-(3+\xi)}\), \(\rho_S=\rho_{S0}+\tfrac{\xi\rho_{m0}}{3+\xi}\big(1-a^{-(3+\xi)}\big)\), and an effective dark-energy equation of state
$$
\boxed{\,w_{\rm eff}(a)=-1-\frac{\xi\,\rho_m(a)}{3\,\rho_S(a)}<-1\ \text{(phantom, for }\xi>0)\,}.
$$

| Result | Value |
|--------|-------|
| **GR limit** | \(\xi\to0\): \(\rho_m\propto a^{-3}\), \(\rho_S=\)const, \(w_{\rm eff}=-1\) — **exactly \(\Lambda\)CDM** |
| **Departure (\(\xi=0.3\))** | \(w_0=-1.043\), \(w_{\rm eff}(z{=}1)=-1.64\), \(H(z)\) distinct from \(\Lambda\)CDM |
| **Determined sign** | phantom \(w_{\rm eff}<-1\), fixed by the Landauer direction (matter → computation) |
| **Observational bound** | \(w_0=-1-0.143\,\xi\); \(\lvert w_0+1\rvert<0.05\Rightarrow \xi<0.35\) |
| **Consistency limit** | \(\rho_S\ge0\) only back to \(z\approx1.7\) at \(\xi=0.3\) (the simple ansatz breaks down earlier) |

## 4. Verdict

**The prospect is promoted, not invalidated.** R4a produces a **candidate hypothesis with mathematical evidence**: a consistent (Bianchi-satisfying), GR-reducing, interacting-dark-energy model in which computational entropy production sources a phantom dark sector, with a **determined sign** and a **free coupling already bounded by data** (\(\xi<0.35\)).

It is **not** a validated theory:

- **Magnitude free.** \(\xi\) (the coupling) is unfixed — the same load-constant calibration gap ([load-dimensional-analysis.md](load-dimensional-analysis.md)) reappears. Whether \(\xi\) is naturally \(O(0.1)\) or Planck-tiny is undetermined; only the sign/form is fixed.
- **One promotion among several.** Perfect-fluid, \(w_S=-1\), \(Q=\xi H\rho_m\), and the energy-flow sign are modeling choices. Other promotions exist; this is the minimal one.
- **Toy consistency limit.** \(\rho_S>0\) fails in the past for the crude ansatz; a realistic entropy-production source is needed for early times.

## 4b. w(z) survival test — the shape is disfavored by current data

Before attempting the hard first-principles coupling, we tested the *shape* of the prediction against data (`simulations/gravity-toy/r4a_wz_survival.py`), mapping the model to the standard CPL plane \((w_0,w_a)\).

**Key structural fact.** The Landauer sign forces the model onto the line
$$
w_0=-1-0.143\,\xi\le -1,\qquad w_a<0,
$$
starting at \(\Lambda\)CDM \((-1,0)\) and moving into the **phantom** quadrant. The model **can never reach \(w_0>-1\)**.

**The data points the other way.** Representative DESI DR1 (2024) \(w_0w_a\)CDM fits — *approximate, unsettled (~2–3\(\sigma\)), sample-dependent* — all sit at \(w_0>-1\) (the **quintessence** side), \(\sim2.8\)–\(3.9\sigma\) from \(\Lambda\)CDM on the **opposite** side from our prediction (DESI+CMB+PantheonPlus \(\approx(-0.83,-0.75)\); +DESY5 \(\approx(-0.73,-1.05)\); +Union3 \(\approx(-0.65,-1.27)\)).

**Verdict.** The natural (Landauer-sign) R4a prediction is **disfavored** by the current data hint; the model survives only in its \(\xi\to0\) (\(\Lambda\)CDM) limit — the *no-new-physics* branch. Honest nuances: (i) the DESI dynamical-DE preference is **not settled**, and \(\Lambda\)CDM (our \(\xi\to0\)) remains fully viable; (ii) the **opposite** energy-flow sign (\(\xi<0\), dark→matter) would give quintessence (\(w_0>-1\)) and *could match* DESI — so the data, if it holds, tells us which way the computational energy exchange must go.

**Consequence for strategy (this validated doing the cheap test first):** do **not** invest in the first-principles coupling for the phantom branch now — it is the disfavored direction. Wait for firmer data (DESI DR2), or study the opposite-sign (quintessence) branch as the physically motivated alternative if \(w_0>-1\) solidifies.

## 4c. Sign derivation — the framework predicts the *disfavored* sign

The w(z) test disfavored the phantom branch and noted the opposite (quintessence) sign fits better. Can we **derive** which sign the framework predicts, *independently of the data*? If so, we must take it — we cannot flip the sign to fit. Witness: `simulations/gravity-toy/r4a_sign_derivation.py`.

**The two signs are two thermodynamic readings of information change:**

- **Flux / Landauer (loss):** the source is the entropy-production *flux* (irreversible loss). \(Q=+\lvert\text{flux}\rvert\Rightarrow\rho_S\) grows \(\Rightarrow\) **phantom** \((w_0\le-1)\).
- **Stockpile / Szilard (gain):** the source is the *recording of identity* (information acquired), drawing down a reservoir. \(Q<0\Rightarrow\rho_S\) shrinks \(\Rightarrow\) **quintessence** \((w_0>-1)\).

**The framework's locked reading selects the flux side.** From PROGRESS_REPORT §2.1 / `m11-idem-to-load.md`: *"Load \(L\) = demand from … entropy **flux**, **not** remaining identity stockpile; active loss/scrambling \(\Rightarrow\) **higher** \(L\)"*, and "Load = remaining … potential identity" is the **explicitly rejected** anti-pattern. The \(\rho_S\) source is therefore the entropy-production **flux**, which is non-negative (second law). Hence
$$
Q=+\lvert\text{flux}\rvert\ge0\ \Rightarrow\ \rho_S\ \text{grows}\ \Rightarrow\ \boxed{\text{PHANTOM}}.
$$
Cross-check: the second law (net entropy production \(>0\)) *is* the dissipative/Landauer direction — independently consistent with phantom.

**Refinement (2026-07-31, `r4a_sign_analysis.py`).** An objection sharpened this: the load is built on the *output* entropy \(S_c\), and \(\lvert dS_c/d\tau\rvert\) is a **magnitude** (sign-neutral), so "derived phantom" was over-stated. Working the energy bookkeeping honestly: cosmic computation is a single **free-energy flow**, reservoir \(\to\) dissipation (2nd law). Which *end* is \(\rho_S\) fixes the sign. Enumerating the reasonable identifications:

| \(\rho_S\) identification | cosmic direction (independent principle) | branch | framework status |
|---------------------------|------------------------------------------|--------|------------------|
| loss-repository (erased-info heat) | grows (fed by entropy flux) | phantom | endorsed |
| output-entropy flux (\(S_c\) rises) | grows (2nd law) | phantom | consistent |
| generated-structure resource (records) | grows (structure accumulates) | phantom | consistent |
| free-energy **reservoir** (initial potential) | shrinks (free energy consumed) | **quintessence** | **rejected** (stockpile anti-pattern) |

**Consequence (honest, corrected).** The sign is **not** an airtight theorem — but it is **not** a free 50/50 either. **Every** identification that follows the entropy arrow (loss flux, output-entropy rise, structure accumulating) lands on **phantom**; the *only* quintessence route identifies \(\rho_S\) with the free-energy **reservoir** being drawn down — the framework's **explicitly rejected** "remaining stockpile/potential" anti-pattern. So **phantom is robustly favored**, and the Szilard/quintessence rescue is **not available within the framework** without a *new, independently-motivated* principle (that must not be chosen to fit the data). Absent such a principle, the honest prediction remains phantom (currently disfavored), and the escape is a **genuine open theory problem**, not a sign flip. (The locked reading is a program *convention* labeled "semantic"; the lean is as firm as that convention plus the second law.)

## 4d. Vacuum-character (equation-of-state) test — the reservoir reading is *forced*, and it is quintessence

§4c favored phantom *among readings that track the entropy arrow*. But a dark-energy sector must have \(w=p/(\rho c^2)\approx-1\). So ask, **data-independently**, what equation of state each end of the free-energy flow actually has (`simulations/gravity-toy/r4a_eos_test.py`):

| \(\rho_S\) end | physical nature | equation of state | dark energy? |
|----------------|-----------------|-------------------|--------------|
| **dissipation** (Landauer heat) | thermalized heat | \(w\in[0,\tfrac13]\ge0\) | **no** (dilutes, decelerates) |
| **reservoir** (latent free energy as a scalar potential) | slow-roll potential | \(w\to-1\) | **yes** (accelerates) |

**This is decisive, and it cuts the other way from §4c.** The dissipation end — the one the entropy-arrow readings pick, and the one that gave **phantom** — is *thermal* (\(w\ge0\)) and **cannot be dark energy at all**. The original phantom branch quietly assumed \(w_S=-1\) for this heat, which is **equation-of-state inconsistent**. The *only* end that can be a \(w\approx-1\) dark sector is the **reservoir** — and consuming it (the field rolls) gives **thawing quintessence** \((w_0>-1,\ w_a<0)\).

So requiring the sector to actually *be* dark energy (\(w\approx-1\)) — a physical demand, not a data fit — **forces the reservoir reading**, which gives quintessence. Structurally a rolling reservoir lands in the \((w_0>-1,\ w_a<0)\) thawing quadrant (Caldwell–Linder \(w_a\approx-1.5(1+w_0)\)) — the *same direction* current DESI hints point, but that is a **consistency remark, not the test** (the argument never used the data).

**Honest caveats (a step, not a theory):**
- It **revises** the framework's locked "flux, not stockpile" reading — *legitimate because motivated by EoS consistency, not by DESI*. The "phantom dark energy" of §3–4b was a category error (thermal energy mislabeled \(w=-1\)).
- The reservoir has \(w\approx-1\) **only if** the computational free energy is stored as a scalar potential — a modeling choice still to be justified from the framework independently.
- The **magnitude** (potential scale / coupling) is still **free**: this does **not** explain the observed dark-energy value.

**Net (⚠ partly superseded by §4e).** The dissipation/phantom reading is retracted as EoS-inconsistent — that stands. But the further claim that the reservoir gives *thawing* quintessence *consistent with the DESI direction* was **over-optimistic**: §4e (Path 1) shows the framework's own dynamics ground \(w\approx-1\) only in the *idle* regime and lean toward **freezing** (\(w_a>0\)), the wrong direction. Read §4e for the corrected status.

## 4e. Path 1 — does the framework *force* the reservoir to be \(w\approx-1\)? (Largely no)

The §4d win rested on "the reservoir is a \(w\approx-1\) scalar potential." Path 1 tests whether the framework actually delivers that, data-independently (`simulations/gravity-toy/r4a_reservoir_eos.py`). The scalar equation of state is fixed by the kinetic/potential ratio \(r=K/V\):
$$
w(r)=\frac{r-1}{r+1};\qquad r\to0:\ w\to-1\ (\text{idle}),\quad r=\tfrac12:\ w=-\tfrac13\ (\text{DE threshold}),\quad r\to\infty:\ w\to+1\ (\text{stiff}).
$$
**The framework's own load identifies the kinetic term.** The "realization rate" is exactly the load's active flux \(\lvert dS_c/d\tau\rvert\), and the locked reading *emphasizes high flux / active scrambling* \(\Rightarrow\) **large \(r\)** \(\Rightarrow\) \(w\to+1\) — **stiff, not dark energy**. The reservoir is \(w\approx-1\) **only in the low-flux / idle regime** (\(r\to0\)) — i.e. the framework's *de-emphasized* "stockpile" once again.

Worse, the **dynamics** (\(w_a\) sign) depend on the flux history: activity **declining** (the natural late-time reading — structure formation winds down as dark energy suppresses it) gives **freezing** (\(w\!\to\!-1\) late, \(w_a>0\)) — the **wrong** side of the DESI thawing hint. §4d's *thawing* assumed *rising* activity without justification, and is **retracted**.

**Path 1 verdict (honest, leaning negative):** the framework does **not** force a \(w\approx-1\) dark sector through its own dynamics. Positive: the reservoir *can* be \(w\approx-1\), but **only when idle** — putting dark energy back in the low-flux "stockpile" the load reading de-emphasizes. Negatives: the active/high-flux regime the framework emphasizes is \(w\to+1\) (not dark energy), and the natural dynamics lean **freezing** (\(w_a>0\)), on the wrong side of the data. So reservoir-as-dark-energy remains a **posit**, now with a known tension (idle-only) and a likely wrong-sign \(w_a\) — **not grounded**. The clean "thawing quintessence consistent with DESI" is withdrawn.

## 5. What this changes

- The gravity program is no longer a dead-ended reformulation: R4a opens a **concrete, falsifiable extension** (phantom interacting dark energy from computational entropy production), tied to the classical core via the Landauer coupling and kin to Bianconi \(\Lambda_G\) / entropy-inflation literature.
- The **decisive open question** is now sharply single: **fix the coupling \(\xi\)** (equivalently, the load-constant calibration). If \(\xi\) is bounded away from 0 by the theory, the hypothesis is live and testable against \(w(z)\) data; if forced to 0 / Planck-tiny, it collapses to \(\Lambda\)CDM (branch a) and the reformulation verdict stands.

## 6. Rigor & non-claims

| Statement | Rigor |
|-----------|-------|
| Bianchi fork: promotion ⇒ constant-\(\Lambda\) **or** matter↔computation exchange | **proved** (identity) |
| GR limit \(\xi\to0\Rightarrow\Lambda\)CDM | **proved** (closed form) |
| Phantom departure \(w_{\rm eff}<-1\), \(w_0=-1-0.143\xi\); bound \(\xi<0.35\) | **derived** (minimal model) + data |
| Coupling \(=\) Landauer power of entropy production | **structural** (modeling identification) |
| Magnitude of \(\xi\) / cosmological relevance | **open** (calibration unfixed) |

**Non-claims:** this is a **candidate** hypothesis, not a validated theory; it does **not** claim to explain dark energy or to fix its magnitude; it is **one** minimal promotion; \(\sigma\) remains a classical density (Paper C); \(L\neq G\); no pointwise Newton (N5). A departure exists **as a model**, its cosmological reality is undetermined pending the coupling.

---

*Update [../papers/FALSIFIABILITY_L_vs_GR.md](../papers/FALSIFIABILITY_L_vs_GR.md), [../synthesis/OPEN_AVENUES.md](../synthesis/OPEN_AVENUES.md), [../synthesis/RESULTS_LEDGER.md](../synthesis/RESULTS_LEDGER.md), [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md) to point here.*
