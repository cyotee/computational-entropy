# Paper outline — Computational Entropy and Emergent Gravity

**Status:** Outline for [DRAFT.md](DRAFT.md) (first complete program draft assembled 2026-07-15) · no new theorems beyond repo-settled claims  

**Authority:** [synthesis/CURRENT_CLAIMS.md](../../synthesis/CURRENT_CLAIMS.md) · [PROGRESS_REPORT.md](../../PROGRESS_REPORT.md) §2, §7  
**Audience:** Researchers in entropic/thermodynamic gravity, information theory of channels, and continuum Gravity-from-Entropy (GfE); secondarily classical-computation / IDEM readers  
**Stance:** Preliminary research. Prefer under-claiming. Constructions and evidence are real; **nothing has GR-level certainty**.  
**Type safety (must appear early):** load \(L\) is a **dimensionless scalar**; structure-induced \(G\) is a **metric** (or edgewise cousin). **\(L \neq G\)**.

### Non-claims banner (paste into intro + conclusion)

Do **not** assert: master equation \(\Leftrightarrow\) continuum GfE; \(L \equiv G\) or \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\); residual dual for all \(t\in(0,t_\star]\); pure T1′ with no soft hypotheses; Newton from pointwise \(\Phi\propto\rho\); next-order \(\gamma_L,\delta_L = D_{\mu\nu},\Lambda_G\); lattice denoising as empirical gravity; external GfE papers as GR-peer foundations; IDEM/decay fully constructs continuum \(L\) or \(G\).

---

## Working title options

1. **Computational Entropy and Emergent Gravity: Channels, Load, and a Euclidean Dual (Program Report)** — *recommended working title*
2. From Output Entropy to Load Clocks: Computational Entropy, Path J/M Newton, and Action–Channel Duality (Euclidean Warm-Up)
3. Computational Entropy, Gravitational Load, and Gravity-from-Entropy: Settled Claims and Explicit Non-Equivalences
4. (Series-style, if split later) Capstone: Computational Entropy and Emergent Gravity — From Discrete Maps to Spacetime Phenology *(aspirational; do not overclaim continuum construction)*

---

## Thesis (one paragraph)

Computational entropy is the entropy of a map or channel’s **output** distribution (classical \(H_c\), quantum/gravity \(S_c\)). Gravity is modeled as a CPTP channel \(\Phi_g\) whose instantaneous demand is a dimensionless **load** \(L\) that reparameterizes proper time via \(d\tau=dt/(1+\alpha L)\); Newtonian Poisson is recovered only via **Path J/M** (Clausius → Einstein → weak-field GR, then on-shell load-clock calibration \(\alpha\beta=4\pi G/c^4\)), not a withdrawn pointwise Laplacian identity. A **constructive Euclidean dual (ACD-EW)** links Bianconi’s GfE **warm-up** (induced \(G[\phi]\), Perona–Malik flow) to an observation channel with split load and load clock; residual dual of PM vs heat is **time-windowed (T1′ / \(U_\star\))**, with joint toys as **pattern witnesses**, not continuum gravity. Weak-field contact with continuum GfE is a **WEAK PASS** on shared Poisson and a **FAIL** of framework identity (M6/M6b). Classical IDEM/decay machinery is connected by a **design dictionary** plus **constructive discrete ledgers** (Phase 1 AND-gate; Phase 2 multi-step Boolean, tiny SKI ensemble, minimal R/B shoe) for \(H_c\) and three-slot \(L^{\mathrm{disc}}\) — not a continuum derivation.

---

## What this paper is / is not

| **Is** | **Is not** |
|--------|------------|
| Honest program synthesis of **settled** claims C1–C14 | A complete derivation of Einstein from bits alone |
| Canonical definitions + labeled rigor (constructive / hybrid / calibration / external theorem+assumption / design) | Symbolic identity of master equation and Bianconi action |
| Path J/M Newton with explicit calibration honesty | Free derivation of \(G\) from load without GR input |
| ACD-EW Euclidean dual + T1′/\(U_\star\) claims A–D | Residual dual = continuum gravitational equivalence |
| M6 WEAK PASS / FAIL + M6b structural FAIL | Numerical solution of Bianconi field equations |
| M11 design + Phase 1–2 discrete accounting | Continuum \(L\) or metric \(G\) from IDEM |
| Explicit non-claims appendix | “GR-level certainty” or peer-status for GfE literature |

---

## Suggested product form

### Primary recommendation

**One long research paper / program report** (target ~25–40 pages when drafted; suitable as a monograph chapter or arXiv long article), structured as the Part outline below.

**Rationale:** Settled material is already a single narrative spine (foundations → load/master eq → Path J/M → ACD-EW dual → M6 non-equivalence → M11 microstructure start). Splitting into six full papers now would force padding or overclaim on deferred recoveries (BH, cosmology) and incomplete M11 Phase 2.

### Optional series map (from PLAN.md §4)

Use as **extraction targets after** the primary draft freezes claims:

| # | PLAN series paper | Role vs this outline | Ready? |
|---|-------------------|----------------------|--------|
| 1 | Foundations — \(H_c\)/\(S_c\), equivalence, conservation | Extract **Part 1** | Yes (canonical defs exist) |
| 2 | IDEM and computational models | Expand **Part 2** + classical corpus | Partial (M11 Phase 1 only) |
| 3 | Classical maps → quantum channels | Thin bridge section inside Part 1/3 | Semantic only (M10 deferred) |
| 4 | \(\Phi_g\) and load from information principles | Extract **Part 3** | Yes (canonical + C14) |
| 5 | Master equation + recoveries | Extract **Parts 3–4**; detail only Path J/M | Newton yes; others deferred |
| 6 | Capstone synthesis | **This document’s product** | Outline stage |

**Alternative (PLAN):** single primary monograph with shorter focused notes extracted (dual-only math note; M6 plug-test note). Prefer dual math note only if PCRH\(_b\) is hardened beyond ensemble certificate.

---

## Part / section outline

### Part 0 — Abstract + keywords

- **Content bullets**
  - State computational entropy as output entropy; load-gated \(\Phi_g\); Path J/M Newton as calibration + imported Clausius/Einstein.
  - ACD-EW constructive Euclidean dual; T1′ residual window \(U_\star\); toys as witnesses.
  - M6: shared Poisson WEAK PASS; FAIL identity; M11 discrete ledger design/Phase 1.
  - End with explicit non-equivalence and preliminary stance.
- **Claim IDs:** C1, C9–C12 (banner-level); full list in body
- **Rigor:** mixed (summary only)
- **Sources:** [CURRENT_CLAIMS.md](../../synthesis/CURRENT_CLAIMS.md); paste-ready dual sentence in same file §6
- **Figures/tables:** none in abstract

**Keywords (draft):** computational entropy; CPTP channel; computational load; thermodynamic gravity; Jacobson Clausius; Gravity from Entropy; Perona–Malik; action–channel duality; IDEM

---

### Part 1 — Foundations — \(H_c\) / \(S_c\), informational equivalence, global conservation

- **Content bullets**
  - One-paragraph definition: \(H_c(f;p_X)=H(Y)\) for \(Y=f(X)\); continuous differential form; quantum \(S_c(\Phi;\rho)=S(\Phi(\rho))\).
  - Key property: informational equivalence of maps with identical output entropy (mechanics do not matter).
  - Worked classical example: \(\sqrt{U}\) vs \(\max(U_1,U_2)\) shared \(H_c\) (from foundations; optional density).
  - Global conservation + local transfer: AND-gate sketch \(H(Y)\approx 0.811\), export \(\approx 1.189\) via chain rule \(H(X)=H(Y)+H(X\mid Y)\).
  - Three-stage mental model: computational induction → geometric imprint → continuum GfE macro (**do not** collapse stages).
  - Notation table: \(H_c\), \(S_c\), \(\Phi_g\), \(L\), \(G\) (type safety).
- **Claim IDs:** C14 (semantic reading of demand; preview); foundations are definitional (pre-C)
- **Rigor:** **constructive** (Shannon/von Neumann defs); global conservation **constructive** for finite classical maps
- **Sources:** [foundations/computational-entropy/definition.md](../../foundations/computational-entropy/definition.md); [GLOSSARY.md](../../GLOSSARY.md); [THEORY.md](../../THEORY.md) stage diagram
- **Figures/tables:** notation/type-safety table; optional AND entropy ledger table (shared with Part 2)

---

### Part 2 — Classical models — IDEM, decay, games (M11 Phase 1–2)

- **Content bullets**
  - Central gap: classical IDEM thread vs gravity thread (THEORY / PROGRESS).
  - IDEM ontology: arity, decay vector \(\mathbf{d}\), \(d_f\), AST metrics — **semantic/structural** roles only.
  - Operational \(H_c\): entropy of **declared** output, not residual dual-toy \(H_c\), not internal AST size alone.
  - Discrete three-slot load \(L^{\mathrm{disc}}=L_E^{\mathrm{disc}}+L_S^{\mathrm{disc}}+L_B^{\mathrm{disc}}\) aligned to continuum **roles** of energy / entropy-rate / boundary — **not** numerical continuum equality.
  - Locked \(L\) reading: high flux / scrambling / open results ⇒ **higher** \(L\) (C14); reject “idle identity stockpile” primary story.
  - **Phase 1 constructive:** AND-gate pure ledger — \(H_c\approx 0.811\), export \(\approx 1.189\), chain rule exact; candidate \(L_E,L_S,L_B\).
  - **Phase 2 constructive:** multi-step Boolean (AND high export, OR lower); tiny SKI ensemble (\(H_c\) drops under redex steps); minimal R/B shoe (predictive \(H_c\), not EV).
  - Honesty: not continuum \(L\) or \(G\); blackjack **belief dual** is ACD-EW pattern only, not strategy EV (defer M12).
- **Claim IDs:** C14; non-claim 9 (IDEM ↛ continuum \(L,G\))
- **Rigor:** **design** (dictionary) + **constructive** (Phase 1–2 ledgers); continuum role match **structural** only
- **Sources:** [synthesis/m11-idem-to-load.md](../../synthesis/m11-idem-to-load.md); `simulations/classical/m11_*.py`; classical notes under `computational-models/` / root IDEM drafts (cite, don’t invent)
- **Figures/tables:** AND + multi-step + SKI + shoe ledger tables; discrete↔continuum role map (M11 §5); optional decay-vector branch table

---

### Part 3 — Channels and load — \(\Phi_g\), \(L\), master equation

- **Content bullets**
  - \(\Phi_g\): CPTP gravitational channel on \(\rho\); \(S_c=S(\Phi_g(\rho))\).
  - Load one-liner: \(L=\beta E[\rho]/(V\epsilon_0)+\gamma|dS_c/d\tau|_{\mathrm{reg}}+\delta S_{\mathrm{boundary}}/S_{\mathrm{BH}}\) — **link** to [master-equation.md](../../emergent-gravity/master-equation.md); do **not** re-copy long justification blocks.
  - Load clock: \(d\tau=dt/(1+\alpha L)\); master equation \(d\rho/dt=(1+\alpha L)^{-1}\mathcal{L}_g[\rho;g_{\mu\nu}(\rho)]\).
  - Clausius constraint on \(\mathcal{L}_g\) (setup for Path J; not a re-proof of Jacobson).
  - Semantic reading of three terms (C14); \(\alpha\beta=4\pi G/c^4\) flagged as **calibration** (C10), detail in Part 4.
  - Type safety: \(L\) scalar ≠ metric \(g\) or GfE \(G\).
- **Claim IDs:** C10 (preview), C14
- **Rigor:** framework definitions **canonical/program**; Clausius→Einstein is **external theorem + assumption** (stated, proven in Part 4 Path J)
- **Sources:** [emergent-gravity/master-equation.md](../../emergent-gravity/master-equation.md); [CURRENT_CLAIMS.md](../../synthesis/CURRENT_CLAIMS.md) §2 C14
- **Figures/tables:** three-term load diagram; clock reparameterization schematic

---

### Part 4 — Recoveries — Path J/M Newton; others outlined / deferred

- **Content bullets**
  - Honesty preamble: low-load regime + calibration, not free Newton from \(\Phi\propto\rho\).
  - **Path J:** L4 Clausius on local horizons → import Jacobson (1995) ⇒ Einstein → standard weak-field Poisson \(\nabla^2\Phi=4\pi G\rho_m\).
  - **Path M:** on-shell match of load clock to Newtonian redshift for calibrated solution family; worked uniform-ball example from newtonian README; \(\alpha\beta=4\pi G/c^4\).
  - Explicit **withdrawn** path: pointwise \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\).
  - What is **not** claimed: Newton independent of Jacobson/Einstein; free derivation of \(G\).
  - **Other recoveries** (BH, cosmology, Lloyd capacity, time dilation): one-paragraph **status only** — outlined / historical drafts in `quantum/` and `emergent-gravity/recoveries/`; **deferred detail** pending same honesty pass as Path J/M. Do not present as settled at Path J/M rigor.
- **Claim IDs:** C9, C10
- **Rigor:** Path J = **external theorem + modeling assumption** + standard GR; Path M = **calibration**
- **Sources:** [emergent-gravity/recoveries/newtonian/README.md](../../emergent-gravity/recoveries/newtonian/README.md); [synthesis/m8-newton-recovery-audit.md](../../synthesis/m8-newton-recovery-audit.md); [quantum/Newton.md](../../quantum/Newton.md) (narrative twin, historical caution)
- **Figures/tables:** Path J/M flowchart; calibration table (\(\alpha\beta\)); withdrawn-path callout box

---

### Part 5 — Euclidean dual ACD-EW — T1′ / \(U_\star\) claims A–D; toys as witnesses

- **Content bullets**
  - Scope: Euclidean **warm-up** only — not Lorentzian GfE, not master-equation equivalence.
  - ACD-EW claim (C1): induced \(G[\phi]=1+\alpha_G(\nabla\phi)^2\); GfE warm-up action / PM flow dual to observation channel + split load + load clock.
  - Setting: 1D lattice jump + Gaussian noise; heat vs PM vs load-PM (from t1-prime writeup).
  - **Claim A:** residual dual on unified pure window \(U_\star=[1.36,2.40]\), \(\rho_b=0.42\), PCRH\(_b\) **soft**.
  - **Claim B:** edge persistence analytic on high-prob. event (\(H_{\mathrm{floor}}=0.25>K\), \(T_{\mathrm{pers}}^\sharp\approx 1.67\)).
  - **Claim C:** short-\(t\) heat win = noise race; identity \(R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\); crossover \(\sim 1.2\).
  - **Claim D:** load-PM as mild time change (\(\tau/t\sim 0.95\)–\(0.98\)); residual dual vs heat on window (hybrid).
  - Joint toys **6/6 SUPPORT** (1D, 2D, blackjack-belief): **pattern** robust (C2–C3); PM > heat on edges is **expected**.
  - Soft spot: PCRH\(_b\) ensemble-certified; full pathwise Dirichlet-form proof open.
  - Paste-ready citation sentence (CURRENT_CLAIMS §6 / t1-prime §6).
- **Claim IDs:** C1–C8
- **Rigor:** ACD-EW **constructive** (+ hybrid-experimental toys); A **analytic + soft**; B **analytic**; C **identity + hybrid**; D **hybrid-experimental**
- **Sources:** [synthesis/action-channel-duality-euclidean.md](../../synthesis/action-channel-duality-euclidean.md); [synthesis/t1-prime-hybrid-writeup.md](../../synthesis/t1-prime-hybrid-writeup.md); [synthesis/m1g-unified-pure-window.md](../../synthesis/m1g-unified-pure-window.md); [synthesis/m2-t1-load.md](../../synthesis/m2-t1-load.md); [synthesis/acd-ew-continuum-transfer.md](../../synthesis/acd-ew-continuum-transfer.md)
- **Figures/tables:** scorecards `gfe_load_joint_toy_scorecard_v2.txt`, `gfe_load_joint_toy_2d_scorecard.txt`, `blackjack_belief_dual_scorecard.txt`; envelopes `t1_unified_pure_envelope.txt`, `t1_delta_noise_envelope.txt`, `t1_load_m2_envelope.txt`; summary PNGs if available; claims A–D rigor table

---

### Part 6 — Continuum GfE contact — M6 WEAK PASS / FAIL; M6b structural FAIL; non-equivalence

- **Content bullets**
  - Shared weak-field problem: Minkowski + \(\Phi\ll c^2\), mass density \(\rho_m\).
  - Side A: Path J/M → \(\nabla^2\Phi=4\pi G\rho_m\) + load calibration.
  - Side B: Bianconi low coupling → EH → same Poisson via GR.
  - **WEAK PASS:** same leading Poisson (C11).
  - **FAIL identity:** different upper mechanisms; refuse \((\alpha_L,\beta_L)=(\alpha_B,\beta_B)\) (C12, M7).
  - **M6b structural FAIL:** GfE extras in metric EOM (\(D_{\mu\nu},\Lambda_G\)); ours \(\gamma_L,\delta_L\) in load **clock** unless promoted (C13).
  - Interpretation: co-class with GR at low demand, **not** evidence load dynamics = relative-entropy EL equations.
  - Interesting dual remains ACD-EW warm-up (different mathematical layer).
  - Non-claims: no numerical Bianconi EOM solution; no master \(\Leftrightarrow\) GfE.
- **Claim IDs:** C11, C12, C13
- **Rigor:** **WEAK PASS** / **FAIL identity** / **structural FAIL** (analysis, not new derivation)
- **Sources:** [synthesis/m6-weak-field-plugtest.md](../../synthesis/m6-weak-field-plugtest.md); [synthesis/m6b-next-order-weak-field.md](../../synthesis/m6b-next-order-weak-field.md); [synthesis/m6c-bianconi-linearization.md](../../synthesis/m6c-bianconi-linearization.md); [synthesis/bridge-bianconi-relative-entropy.md](../../synthesis/bridge-bianconi-relative-entropy.md); `papers/external/` Bianconi PDFs + NOTES
- **Figures/tables:** M6 plug-test criteria table; side-by-side mechanism table; next-order mismatch table

---

### Part 7 — Synthesis / open program — M11 microstructure, M5/M10, M9 deferred

- **Content bullets**
  - Program map: Stage 1–3; what is frozen vs open (PROGRESS §6–§7, OPEN_MATH D1–D9).
  - Dual residual program: **settled enough** — stop as main crisis; optional PCRH\(_b\) harden for math note.
  - **M11 Phase 2** (default science track): multi-step map / tiny lambda / minimal shoe using M11 slots.
  - **M10:** toy residual \(H_c\) vs von Neumann \(S_c\) — hygiene without overclaim.
  - **M5:** warm-up continuum / Γ-limit — citation bridge; open.
  - **M9:** Lorentzian GfE lift — deferred, high cost.
  - **M12:** true game channel \(H_c\) (not belief dual).
  - Deprioritize: more dual scorecards; equating \(\alpha_L\beta_L\) with Bianconi coeffs; continuum \(L/G\) from AND Phase 1.
- **Claim IDs:** all C1–C14 as inventory of what is frozen
- **Rigor:** program planning (**design** / deferred labels)
- **Sources:** [PROGRESS_REPORT.md](../../PROGRESS_REPORT.md) §7; [synthesis/OPEN_MATH_DECISION_LOG.md](../../synthesis/OPEN_MATH_DECISION_LOG.md); [synthesis/PACK_INDEX.md](../../synthesis/PACK_INDEX.md); [PRD.md](../../PRD.md)
- **Figures/tables:** open-board snapshot table (M1–M12); recommended-next flowchart

---

### Part 8 — Conclusion + non-claims appendix

- **Content bullets**
  - Restate thesis under-claimed: definitions + Path J/M + ACD-EW dual + M6 honesty + M11 start.
  - What the program **may** assert (C1–C14 one-line each).
  - Full non-claims list (PROGRESS §2.3 + dual write-up extras).
  - Reproduction appendix: commands for AND ledger, joint toys, \(U_\star\), M2 (from PROGRESS §8).
  - Pointers to canonical files (single source of truth policy).
- **Claim IDs:** C1–C14 summary; non-claims 1–9
- **Rigor:** meta
- **Sources:** CURRENT_CLAIMS entire; PROGRESS §2.3, §8
- **Figures/tables:** claim checklist table; non-claims checklist

---

## Claim → section map

| Claim | Short statement | Primary section | Rigor label |
|-------|-----------------|-----------------|-------------|
| C1 | ACD-EW constructive Euclidean dual | Part 5 | constructive (+ toys hybrid) |
| C2 | Joint toys 6/6 SUPPORT pattern | Part 5 | hybrid-experimental |
| C3 | PM > heat on edges expected | Part 5 | structural |
| C4 | Residual dual time-windowed T1′ | Part 5 (Claim A setup) | analytic + hybrid |
| C5 | \(U_\star=[1.36,2.40]\), \(\rho_b=0.42\), PCRH\(_b\) | Part 5 Claim A | analytic + soft |
| C6 | Edge persistence \(H_{\mathrm{floor}}=0.25\) | Part 5 Claim B | analytic |
| C7 | Short-\(t\) noise race / blur identity | Part 5 Claim C | analytic identity + hybrid |
| C8 | Load-PM mild time change dual | Part 5 Claim D | hybrid-experimental |
| C9 | Newton = Path J/M only | Part 4 | external thm+assumption / calibration |
| C10 | \(\alpha\beta=4\pi G/c^4\) on-shell calibration | Parts 3–4 | calibration |
| C11 | M6 WEAK PASS shared Poisson | Part 6 | WEAK PASS |
| C12 | M6 FAIL framework identity | Part 6 | FAIL identity |
| C13 | M6b next-order structural FAIL | Part 6 | structural |
| C14 | \(L\) = demand from scale/rate of outcomes | Parts 1–3, 2 | semantic |

---

## Non-claims that must appear in the paper

Mirror [CURRENT_CLAIMS.md](../../synthesis/CURRENT_CLAIMS.md) §3 and [PROGRESS_REPORT.md](../../PROGRESS_REPORT.md) §2.3:

1. Master equation \(\Leftrightarrow\) Bianconi continuum GfE.  
2. \(L \equiv G\), \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\), \(\alpha_L\beta_L \equiv \alpha_B/\beta_B\).  
3. T1 residual domination for all \(t\in(0,t_\star]\) (false; use T1′ / \(U_\star\)).  
4. Pure T1′ with **no** soft hypotheses (PCRH\(_b\) still ensemble-certified).  
5. Newton from pointwise \(\Phi\propto\rho\) Laplacian (**withdrawn**).  
6. Next-order \(\gamma_L,\delta_L\) equal GfE \(D_{\mu\nu},\Lambda_G\).  
7. Lattice denoising = empirical gravity.  
8. External GfE papers established on par with GR.  
9. IDEM/decay fully constructs continuum \(L\) or \(G\).

**Also (dual write-up):** no theorem-level multi-jump / 2D / continuum SPDE residual domination; toy residual \(H_c\) ≠ von Neumann \(S_c\) identity (M10 open).

**Also (M6):** WEAK PASS does not upgrade either theory to GR-level certainty; Path J still depends on Jacobson/Einstein input.

---

## Bibliography stubs

| Stub | Role in paper | Local path / note |
|------|---------------|-------------------|
| Bianconi, *Gravity from entropy*, PRD 2025 / arXiv:2408.14391 | Continuum GfE target; low-coupling EH | `papers/external/Bianconi_Gravity_from_entropy_*` · NOTES |
| Bianconi, *Beyond holography*, arXiv:2503.14048 | PM = GfE warm-up gradient flow | `papers/external/Bianconi_Beyond_holography_*` |
| Thattarampilly–Zheng, inflation from entropy, arXiv:2509.23987 | GfE applications (context only) | `papers/external/Thattarampilly_*` |
| Thattarampilly–Zheng, spherical BH, arXiv:2602.13694 | GfE applications (context only) | same |
| Kumar, semiclassical Einstein via \(S_{\rm gen}\), arXiv:2404.16912 | Adjacent entropic Einstein recovery | `papers/external/Kumar_*` |
| Jacobson, *Thermodynamics of spacetime*, PRL 1995 | Path J external theorem | cite from master-equation / newtonian README |
| Verlinde, entropic force / emergent gravity (2010+) | Related program (comparison, not identity) | master-equation narrative peers |
| Lloyd, ultimate physical limits / cosmic computer | Capacity recovery narrative (deferred detail) | master-equation / capacity notes |
| Perona–Malik anisotropic diffusion (classic image processing) | ACD-EW reconstructor | via Bianconi Beyond holography + dual design |
| Shannon; Cover–Thomas (textbook) | Classical \(H_c\) foundations | standard |
| Nielsen–Chuang or equivalent | CPTP / von Neumann \(S_c\) | standard |

Do **not** invent citations beyond repo external set + standard classics named in canonical files.

---

## Figure/table inventory (existing repo artifacts only)

| Artifact | Path | Use in draft |
|----------|------|--------------|
| 1D joint-toy scorecard | `simulations/bridging/gfe_load_joint_toy_scorecard_v2.txt` | Part 5 C2 |
| 1D summary figure | `simulations/bridging/gfe_load_joint_toy_summary.png` | Part 5 |
| 2D scorecard | `simulations/bridging/gfe_load_joint_toy_2d_scorecard.txt` | Part 5 |
| 2D summary figure | `simulations/bridging/gfe_load_joint_toy_2d_summary.png` | Part 5 |
| Blackjack belief scorecard | `simulations/bridging/blackjack_belief_dual_scorecard.txt` | Part 5 pattern-only |
| \(U_\star\) envelope | `simulations/bridging/t1_unified_pure_envelope.txt` | Part 5 Claim A |
| \(\Delta_{\mathrm{noise}}\) envelope | `simulations/bridging/t1_delta_noise_envelope.txt` | Part 5 Claim C |
| Load M2 envelope | `simulations/bridging/t1_load_m2_envelope.txt` | Part 5 Claim D |
| Other T1 envelopes | `t1_eprime_envelope.txt`, `t1_pure_hrho_envelope.txt`, `t1_mc_envelope.txt` | appendix / SI |
| AND-gate ledger (Phase 1) | `simulations/classical/m11_and_gate_ledger.py` | Part 2 table |
| Multi-step / SKI / shoe (Phase 2) | `simulations/classical/m11_*_ledger.py` · `_run_m11_phase2.py` | Part 2 tables |
| Entropy object map (M10) | `synthesis/m10-sc-vs-toy-hc.md` | Part 1 / 7 hygiene table |
| Warm-up continuum hygiene (M5) | `synthesis/m5-warmup-continuum-hygiene.md` | Part 5–6 checklist |
| Claims freeze table | `synthesis/CURRENT_CLAIMS.md` §2 | Part 8 checklist |
| M6 criteria table | `synthesis/m6-weak-field-plugtest.md` §4 | Part 6 |
| Path J/M tables | `emergent-gravity/recoveries/newtonian/README.md` | Part 4 |
| Dual claims A–D | `synthesis/t1-prime-hybrid-writeup.md` | Part 5 |

No new experimental figures required for a first complete draft beyond these (plus simple schematic diagrams drawn from existing tables).

---

## Writing order (dependency order for drafting)

1. **Part 1** — freeze definitions and notation (blocks later misuse of \(H_c\), \(L\), \(G\)).  
2. **Part 3** — load + master equation one-liners (link canonicals).  
3. **Part 4** — Path J/M (depends on Part 3 Clausius setup).  
4. **Part 5** — ACD-EW + A–D (self-contained Euclidean layer; after type safety is fixed).  
5. **Part 6** — M6/M6b (depends on Parts 4–5 for honest comparison).  
6. **Part 2** — M11 (after continuum \(L\) roles exist so discrete slots can align without equating).  
7. **Part 7** — open program (after all settled body sections).  
8. **Part 0 abstract + Part 8 conclusion / non-claims** — last, quote final claim IDs only.  
9. Optional: extract dual-only math note or PLAN series papers from frozen primary draft.

---

## Success criteria for a first complete draft

- [ ] Every **C1–C14** appears once with correct rigor label and pointer to a repo source.  
- [ ] Full **non-claims** list appears in intro banner **and** appendix; none contradicted in body prose.  
- [ ] **Type safety** \(L\neq G\) stated and never violated by loose language.  
- [ ] Newton section uses **only Path J/M**; withdrawn pointwise path is explicitly labeled withdrawn.  
- [ ] Dual section states **T1′ / \(U_\star\)**, soft PCRH\(_b\), and “**not continuum gravity**.”  
- [ ] M6 section states **WEAK PASS + FAIL identity + M6b structural FAIL**; no framework equivalence.  
- [ ] M11 section is **design + Phase 1–2 constructive accounting** only; no continuum derivation claim.  
- [ ] Core formulas for \(H_c/S_c\), \(L\), master equation are **linked** to canonical files, not re-invented at length.  
- [ ] Figures/tables are drawn **only** from inventory above (or trivial schematics of those tables).  
- [ ] No new theorems; no inflated certainty language (“proves GR”, “derives Bianconi action from \(L\)”).  
- [ ] Reproduction commands for dual + AND ledger work under project `.venv`.  
- [ ] Optional series map in front matter matches PLAN.md §4 without claiming all six papers are already written.

---

## Related paths

| Role | Path |
|------|------|
| This outline | `papers/06-synthesis/OUTLINE.md` |
| Claims freeze | `synthesis/CURRENT_CLAIMS.md` |
| Progress / next avenues | `PROGRESS_REPORT.md` |
| Series skeleton | `PLAN.md` §4 · `papers/README.md` |
| Main legacy TeX (do not bulk-edit from this outline) | `quantum/Computational_Entropy_and_Emergent_Gravity.tex` |

---

*Update this outline when CURRENT_CLAIMS, \(U_\star\), M6/M11 status, or recommended product form changes. Do not expand into proofs — link sources.*
