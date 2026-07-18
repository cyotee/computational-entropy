# M10 — \(S_c\) vs Toy / Classical \(H_c\): Object Map and Honesty Boundaries

**M-id:** M10  
**Status:** **Dictionary / hygiene complete; identification theorem open**  
**P1 status:** **hybrid MC non-identity done** — [m10-p1-object-comparison.md](m10-p1-object-comparison.md) · code [m10_p1_entropy_objects.py](../simulations/bridging/m10_p1_entropy_objects.py)  
**Scope:** Disambiguate every object called “\(H_c\)” or “\(S_c\)” in the repo; forbid silent identity; sketch a program path only  
**Parents:** [foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) · [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) · [m11-idem-to-load.md](m11-idem-to-load.md) · [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md)  
**Siblings:** [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) · [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) · [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)  
**Date:** 2026-07-14 (P1 pointer 2026-07-15)  
**Stance:** Preliminary research. Under-claim. No fake proof of \(H_c \equiv S_c\).

---

## 0. Why M10 exists

The symbol \(H_c\) (and sometimes loose “computational entropy”) is used for **several inequivalent functionals**. Agents and drafts that treat them as one number produce:

- false bridges (dual-toy residual → von Neumann gravity channel),
- wrong load bookkeeping (\(L_S \propto |\Delta H_c|\) with the wrong \(H_c\)),
- overclaimed continuum contact (M5/M6 layers mixed with Stage-1 channel entropy).

M10 freezes a **named object map**. It does **not** construct \(\Phi_g\) or prove quantum–classical identification.

---

## 1. Precise object map

Each row is a **distinct** functional unless an explicit map is written and labeled.

| Tag | Symbol (recommended) | Domain / inputs | Definition (operational) | Code / canonical |
|-----|----------------------|-----------------|--------------------------|------------------|
| **A. Classical map \(H_c\)** | \(H_c(f;p_X)\) | Map \(f\), input law \(p_X\) | Shannon (or differential) entropy of **output** \(Y=f(X)\): \(H(Y)\) or \(h(Y)\) | [foundations/…/definition.md](../foundations/computational-entropy/definition.md) |
| **B. Quantum / gravity \(S_c\)** | \(S_c(\Phi;\rho)\) | CPTP \(\Phi\), state \(\rho\) | Von Neumann entropy of **channel output**: \(S(\Phi(\rho))=-\operatorname{Tr}\Phi(\rho)\log\Phi(\rho)\) | same foundations file; [master-equation.md](../emergent-gravity/master-equation.md) uses \(S_c=S(\Phi_g(\rho))\) |
| **C. Dual-toy residual / channel \(H_c\)** | \(H_c^{\mathrm{toy}}(\hat\phi\mid\phi_\star)\) | Reconstructor state \(\hat\phi\), hidden field \(\phi_\star\) | \(H_R+\lambda_e H_{\mathrm{edge}}\) with \(H_R=\log(1+R/\sigma_{\mathrm{ref}}^2)\), \(R=\mathrm{MSE}(\hat\phi,\phi_\star)\), \(H_{\mathrm{edge}}=\) soft Shannon of edge mass \(p\propto|\nabla\hat\phi|\) | `_joint_toy_v2_core.py` (`H_c_channel`); ACD-EW §1.4 |
| **D. Predictive game \(H_c\)** | \(H_c^{\mathrm{game}}(k)\) | Predictor / strategy map at step \(k\), filtration \(\mathcal{F}_{k-1}\) | One-step predictive Shannon \(H(Y_k\mid\mathcal{F}_{k-1})\) (or \(H(Y_k)\)); if log-loss scoring, label \(H_c^{\mathrm{score}}\) | classical games notes; M11 §3–4, §8; **not** implemented as dual-toy \(H_c\) |
| **E. Discrete M11 / IDEM \(H_c\)** | \(H_c^{\mathrm{disc}}(f;p_X)\) | Finite map (gate, lambda step, declared output \(Y\)) | Exact \(H(Y)\) under declared \(p_X\) (AND-gate: \(H(Y)\approx 0.811\) bits) | [m11-idem-to-load.md](m11-idem-to-load.md); `m11_and_gate_ledger.py` |

### 1.1 Relationship diagram (rigor only)

```text
Canonical definition (foundations)
        │
        ├─ classical specialization ──► A. H_c(f;p_X)  ── constructive in finite models
        │                                      │
        │                                      ├─ M11 gates / IDEM ──► E. H_c^disc  (constructive)
        │                                      └─ game predictor   ──► D. H_c^game  (structural once Y, F fixed)
        │
        └─ quantum specialization ──► B. S_c(Φ;ρ)     ── semantic template for Φ_g
                                              │
                                              └── identification with A/C/D/E: **OPEN (M10 program)**

Dual toys (ACD-EW)
        └── C. H_c^toy  = residual quality proxy
              │
              ├── **semantic** cousin of “output pattern uncertainty”
              ├── **not** Shannon of a bit map’s p_Y
              └── **not** von Neumann S_c
```

### 1.2 What the joint toy **actually** computes

From `_joint_toy_v2_core.py` (names approximate):

| Quantity | Formula in code | Role in dual |
|----------|-----------------|--------------|
| Residual energy \(R\) | \(\mathrm{mean}_i(\hat\phi_i-\phi_{\star,i})^2\) | Denoising loss vs **oracle** \(\phi_\star\) |
| \(H_R\) | \(\log(1+R/\sigma_{\mathrm{ref}}^2)\) | Log residual proxy (not Shannon of a PMF) |
| \(H_{\mathrm{edge}}\) | \(-\sum_i p_i\log_2 p_i\), \(p\propto|\nabla\hat\phi|\) | Soft location entropy of edge mass |
| \(H_c^{\mathrm{toy}}\) | \(H_R+\lambda_e H_{\mathrm{edge}}\) | Scalar “channel quality” for dual scorecard + \(L_S\) |
| \(L_S\) | \(c_S\,|\Delta H_c^{\mathrm{toy}}|/\Delta t\) | Entropy-**rate** load term in the toy |

**Important:** \(H_c^{\mathrm{toy}}\) depends on **ground-truth** \(\phi_\star\). Canonical \(H_c(f;p_X)=H(Y)\) depends only on the **output law**, not on an external truth field. So \(H_c^{\mathrm{toy}}\) is a **supervised residual score**, not the unsupervised output-entropy functional of foundations §Definition.

**Blackjack belief dual:** same \(H_c^{\mathrm{toy}}\) on a game-**labeled** field \(\phi\); **not** next-card predictive entropy ([DESIGN_blackjack_belief_dual.md](../simulations/bridging/DESIGN_blackjack_belief_dual.md) §3).

---

## 2. Same-name collisions (when agents misuse “\(H_c\)”)

| Misuse | What was meant | Correct tag | Damage if left |
|--------|----------------|-------------|----------------|
| “\(H_c\) drops under PM” as Shannon of a map | Dual residual score improves | **C** \(H_c^{\mathrm{toy}}\) | Claims map-output entropy without a declared \(Y\sim p_Y\) |
| “AND-gate \(H_c\) supports dual residual theorem” | Discrete Shannon \(H(Y)\) | **E** vs **C** | Conflates M11 bookkeeping with ACD-EW |
| “Blackjack \(H_c\) is card entropy” in dual scorecard | Residual/edge on belief field | **C**, not **D** | Fake game-theory result |
| “Game \(H_c\)” without declaring \(Y\) and \(\mathcal{F}\) | Unspecified predictor | must fix **D** | Unfalsifiable claim |
| “\(S_c\) of the lattice field” | Toy residual or \(S_{\mathrm{GfE}}=-\sum\ln G\) | neither is **B** | Fake quantum gravity channel |
| “\(H_c \equiv S_{\mathrm{GfE}}\)” | Residual score vs warm-up action | **C** vs \(\sum-\ln G_i\) | Forbidden identity (ACD-EW non-claim) |
| “\(H_c \equiv S_c\)” | Classical output Shannon ≡ von Neumann of \(\Phi_g(\rho)\) | **A** vs **B** | Central non-claim of M10 / CURRENT_CLAIMS |
| Load \(L_S\) from dual \(H_c\) as continuum \(\|dS_c/d\tau\|\) | Toy rate of residual score | form match only | Overclaim master-equation load |
| Differential \(h(Y)\) of continuous map written as bits of dual \(H_R\) | Different units and semantics | **A** continuous vs **C** | Numeric nonsense |
| “Output entropy” of reconstructor \(\hat\phi\) as vector | Field configuration entropy without law | need a **measure on fields** | Not defined in toys |

**House style for new writing:** use superscript tags \(H_c^{\mathrm{toy}}\), \(H_c^{\mathrm{disc}}\), \(H_c^{\mathrm{game}}\), \(S_c\) on first use in a section; plain \(H_c\) only for **A** (foundations classical) when unambiguous.

---

## 3. When identification is allowed vs forbidden

### 3.1 Allowed (with label)

| Identification | Condition | Rigor |
|----------------|-----------|-------|
| **A = E** | Same map \(f\), same \(p_X\), exact finite \(H(Y)\) | **constructive** (e.g. AND ledger) |
| **A ≈ sample estimate** | MC histogram of \(Y\) under \(p_X\); report bias | **constructive** (approximate) |
| **D as instance of A** | Declared output \(Y_k\) and law (conditional on \(\mathcal{F}_{k-1}\)) | **structural** once declarations fixed |
| **B reduces to A** | Classical commutative limit: \(\Phi\) dephases / measures to a classical channel with output PMF \(p_Y\), then \(S(\rho_Y)=H(Y)\) | **structural** (standard QI; not a new theorem here) |
| **C as “channel quality”** in ACD-EW only | Explicitly residual/edge dual object; dual scorecards | **constructive** specialization; **not** foundations \(H(Y)\) |
| **Role analogy \(L_S\)** | \(|\Delta H_c^{\bullet}|\) uses **one** fixed bullet (toy **or** disc **or** game) | **semantic / structural** bookkeeping; not continuum identity |
| **Notation \(H_c\) for A** | Document states classical discrete/continuous foundations case | canonical |

### 3.2 Forbidden (without new work)

| Forbidden claim | Why |
|-----------------|-----|
| \(H_c^{\mathrm{toy}} \equiv H_c(f;p_X)\) | Supervised residual functional ≠ unsupervised \(H(Y)\) |
| \(H_c^{\mathrm{toy}} \equiv S_c(\Phi_g;\rho)\) | No \(\Phi_g\), no density operator in toys |
| \(H_c^{\mathrm{disc}} \equiv S_c\) | Classical bits ≠ von Neumann of gravitational channel |
| \(H_c^{\mathrm{game}} \equiv H_c^{\mathrm{toy}}\) | Predictive card/action entropy ≠ residual belief-field score |
| \(H_c^{\mathrm{toy}} \equiv S_{\mathrm{GfE}}=-\sum\ln G\) | ACD-EW explicitly rejects numeric identity |
| \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\) | CURRENT_CLAIMS non-claim #2; different primary objects |
| Continuum load \(L(\rho,g)\) uses dual \(H_c^{\mathrm{toy}}\) without a map | Missing \(\rho\), missing continuum limit of residual score |
| Any equality that drops the **tag** and asserts one number across stages | Stage collapse |

### 3.3 Grey zone (program only — may discuss, not assert as settled)

| Grey claim | Status |
|------------|--------|
| Residual dual quality tracks “information gained by structure-preserving channel” | **semantic** story of ACD-EW; OK if not written as \(H_c^{\mathrm{toy}}=H(Y)\) |
| Export \(H(X\mid Y)\) in M11 parallels environment entropy in CPTP picture | **semantic** global-conservation analogy (foundations §Global Conservation) |
| In a **future** embedding, field residual might be a classical sufficient statistic for a measurement channel | **program**; requires explicit \(\Phi\), POVM, state |

---

## 4. Semantic / structural / constructive labels (summary table)

| Object | Semantic | Structural | Constructive |
|--------|----------|------------|--------------|
| **A** \(H_c(f;p_X)\) | “entropy of computation as output pattern” | Shannon of \(p_Y\) from map | Exact on small discrete maps |
| **B** \(S_c(\Phi;\rho)\) | QI analogue for channels | von Neumann of \(\Phi(\rho)\) | Only if \(\Phi,\rho\) fully specified (not in dual toys) |
| **C** \(H_c^{\mathrm{toy}}\) | reconstructor quality / dual Stage-1 score | formula \(H_R+\lambda_e H_{\mathrm{edge}}\) | Implemented + scorecarded |
| **D** \(H_c^{\mathrm{game}}\) | predictive uncertainty under agent info | conditional Shannon given \(\mathcal{F}\) | Exact on small shoes; else estimate |
| **E** \(H_c^{\mathrm{disc}}\) | IDEM/gate output entropy | same as A on declared \(Y\) | AND Phase 1 ledger |
| **A ↔ B** | shared “output entropy of a map” slogan | classical limit of von Neumann | **not** constructive for \(\Phi_g\) yet |
| **C ↔ B** | both “channel performance” metaphors | **no shared formula** | **none** |
| **C ↔ A** | both called computational entropy in prose | residual score vs \(H(Y)\) | **none** as identity |

---

## 5. Path toward relating residual dual \(H_c^{\mathrm{toy}}\) to von Neumann \(S_c\) (program only)

This section is a **research ladder**, not a proof. Each rung must stay labeled.

| Step | Program content | Required object | Stops short of |
|------|-----------------|-----------------|----------------|
| **P0** | Keep tags; never write \(H_c^{\mathrm{toy}}=S_c\) | This note | — |
| **P1** | Classical unsupervised lift: treat reconstructor as map \(\mathcal{C}_t:y\mapsto\hat\phi\); define \(H_c^{\mathrm{map}}(t)=H(\mathrm{law\ of\ }\hat\phi)\) or entropy of a **coarsened** observable \(Z(\hat\phi)\) (e.g. edge location bin) under noise measure | Probability law on fields or observables | Equality with residual \(H_R\) |
| **P2** | Relate \(H_R\) to a **Bregman / log-loss** score against \(\phi_\star\); compare to cross-entropy \(H(p_\star,\hat p)\) if \(\phi_\star\) is encoded as a distribution | Scoring-rule dictionary | Shannon \(H(Y)\) identity |
| **P3** | Quantum dilations: encode classical observation model as a measurement channel \(\mathcal{E}:\rho\mapsto\sum_y |y\rangle\langle y|\operatorname{Tr}(M_y\rho)\); set \(S_c=S(\mathcal{E}(\rho))\) | Explicit \(\rho,\{M_y\}\) | Gravity \(\Phi_g\) |
| **P4** | Only then ask for inequalities of the form \(H_c^{\mathrm{toy}}\ge f(S_c)\) or data-processing bounds under the **same** channel | Shared channel | Continuum GfE or master equation |

**Non-path (do not take):** “PM residual is lower, therefore \(S_c\) of spacetime is lower.” Residual improvement is a Euclidean dual fact (T1′ / toys), not a von Neumann calculation.

**Cross-link:** Continuum warm-up hygiene ([m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md)) forbids lifting dual residual theorems to Lorentzian GfE; M10 forbids lifting dual residual scores to \(S_c\). Together they block **two** common overclaims.

---

## 6. Explicit non-claims (M10)

1. \(H_c^{\mathrm{toy}} \not\equiv H_c(f;p_X)\) and \(H_c^{\mathrm{toy}} \not\equiv S_c(\Phi;\rho)\).  
2. \(H_c^{\mathrm{disc}}\) (AND / IDEM) does **not** construct continuum \(S_c\) or \(\Phi_g\).  
3. \(H_c^{\mathrm{game}}\) is **not** the blackjack belief dual score.  
4. No proof that residual domination (T1′) implies anything about von Neumann entropy of a gravitational channel.  
5. No identification \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\) (GfE relative entropy of metrics).  
6. No claim that master-equation load’s \(\|dS_c/d\tau\|\) term is numerically the toy’s \(L_S\).  
7. Classical limit “\(S\to H\)” is standard QI folklore for commuting states — **not** a derivation of emergent gravity from dual toys.  
8. M10 dictionary completion does **not** close M9 (Lorentzian lift) or master equation \(\Leftrightarrow\) GfE.

---

## 7. Open questions

| # | Question | Blocks |
|---|----------|--------|
| Q1 | Is there a natural observable \(Z(\hat\phi)\) such that \(H(Z)\) co-moves with \(H_c^{\mathrm{toy}}\) on dual windows? | Unsupervised classical lift (P1) |
| Q2 | Can residual \(R\) be written as a Bregman divergence for a full exponential family on lattice fields? | Scoring-rule bridge (P2) |
| Q3 | Minimal quantum model of \(y=\phi_\star+\eta\) with CPTP \(\mathcal{E}\) whose \(S(\mathcal{E}(\rho))\) has a proved relation to \(R\)? | First \(S_c\) contact (P3) |
| Q4 | Does M11 multi-step \(H_c^{\mathrm{disc}}\) chain admit a dilation consistent with foundations global conservation narrative? | Microstructure → channel |

---

## 8. Recommended next analytic step (**one only**)

**~~Do P1 for the dual toy~~ → done:** [m10-p1-object-comparison.md](m10-p1-object-comparison.md) (hybrid MC: \(H_c^{\mathrm{toy}}\) vs ensemble \(H(Z_{\mathrm{bin}})\), \(H(Z_8)\) on \(U_\star\) times; non-identity asserted; still \(\neq S_c\)).

**Optional next (only if pursued):** P2 scoring-rule / Bregman dictionary for residual \(R\), or a co-motion study of other coarsenings — **not** P3–P4 quantum gravity by default.

**Historical P1 brief (kept for archive):**  
Fix the 1D joint-toy observation measure (noise law on \(y\), fixed \(\phi_\star\) class). Choose **one** coarsened classical output \(Z=Z(\hat\phi)\) — recommended: **edge-location soft histogram** already used in \(H_{\mathrm{edge}}\), or a binary “jump bin” partition — and write a short lemma comparing ordering on \(U_\star\) to \(H_c^{\mathrm{toy}}\) **without** asserting equality. Avoid differential entropy of full \(\hat\phi\in\mathbb{R}^N\) without regularization.

---

## 9. Status line for board

**M10: object dictionary + collision table + allow/forbid rules frozen; residual \(H_c^{\mathrm{toy}}\) ↛ von Neumann \(S_c\); P1 coarsened \(H(Z)\) hybrid non-identity done ([m10-p1-object-comparison.md](m10-p1-object-comparison.md)); next optional = P2 scoring-rule dictionary, not quantum gravity by default.**

---

## 10. Pointers

| Resource | Path |
|----------|------|
| **P1 object comparison** | [m10-p1-object-comparison.md](m10-p1-object-comparison.md) · [m10_p1_entropy_objects.py](../simulations/bridging/m10_p1_entropy_objects.py) |
| Canonical \(H_c\) / \(S_c\) | [foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) |
| ACD-EW dual \(H_c\) | [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) §1.4 |
| Transfer non-identities | [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) §4 |
| M11 discrete \(H_c\) | [m11-idem-to-load.md](m11-idem-to-load.md) |
| Claims freeze | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) §3 |
| M5 continuum hygiene | [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) |
| Master equation \(S_c\) | [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) |

---
*Pack index:* [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)
