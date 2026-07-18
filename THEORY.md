# THEORY.md — Explicit Bridge Architecture and Cohesion Document

**Status**: Living bridge architecture (seeded 2026-06-22; **Euclidean dual freeze 2026-07-15+**).

This is the living source of truth for the conceptual bridge between:
- The **lambda calculus / computational models** thread (IDEM functions, decay vectors, output distribution entropy, games as models, etc.)
- The **emergent gravity** thread (gravitational channel \(\Phi_g\), computational load \(L\), master equation, and recoveries)

### Active research focus (2026-07-15+)

| Layer | Status | Notes |
|-------|--------|--------|
| **Euclidean ACD-EW dual** (heat/PM residual, joint toys, T1′ / \(U_\star\)) | **Program-level settled** | Do not default-chase more dual scorecards; optional pure PCRH\(_b\) only for paper depth |
| **Primary next** | **M11 IDEM → load** | Connect decay / recoverability to \(L\) or \(H_c\); attacks central gap |
| **Also** | Continuum hygiene (M5/M10); claim freeze / paper outline | Not continuum ME ⇔ GfE |

**Claims sheet:** [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · **M11 design:** [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) · **Progress:** [PROGRESS_REPORT.md](PROGRESS_REPORT.md)

## Purpose
- Define explicit mappings between concepts.
- Document the current level of rigor for each mapping (analogy / structural / constructive).
- Provide worked examples and correspondence tables.
- Guide the extraction of canonical content and the writing of future papers.
- Track open questions and progress toward a unified theory.

See [PLAN.md](PLAN.md) for the overall reorganization and paper plan.

---

## 1. Current State Diagnosis

The repository contains two substantial but only loosely connected research threads:

### Lambda / Classical Computational Entropy Thread
- Rich formal machinery: IDEM functions (with arity, decay vectors \([d_1 \dots d_n], d_f\)), combinatorics from lambda expressions, infinite reduction paths for underivability, vectorial lambda calculus.
- Concrete examples: Blackjack and other games modeled as functions that reduce entropy / increase predictive accuracy.
- Early drafts explicitly attempted to ground entropy calculations in lambda calculus (system entropy ≈ log |AST size of normal form|, potential via unreduced paths).

### Emergent Gravity Thread
- Core construction: gravitational quantum channel \(\Phi_g\) (CPTP map), output **computational entropy** \(S_c = S(\Phi_g(\rho))\), dimensionless **computational load** \(L\), and the master equation.
- Recoveries of Newtonian gravity, time dilation, Schwarzschild + horizons, Hawking/Page curve, FLRW + inflation, Lloyd capacity.
- Unification claims with Jacobson, Verlinde, Susskind, holography, Lloyd.

**The Gap** (confirmed by duplication audit 2026-06-22; still the **central** cohesion gap after dual freeze 2026-07-15):
- Gravity work uses the *high-level* definition of computational entropy and the "universe as computer" metaphor.
- It does **not** leverage the specific lambda/IDEM/decay-vector/AST machinery.
- Massive duplication of explanatory text (core definition appears verbatim in README, quantum/Computational_Entropy.md, and embedded in the .tex; master equation + load recapped in nearly every quantum/*.md and the .tex).
- Early unification intent has not been carried forward into the master equation.
- **Euclidean dual toys are saturated** (ACD-EW pattern robust) — they do **not** close IDEM↔gravity. Next primary attack: **M11** ([synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md)).

**Canonical sources now exist** (as of this update):
- [foundations/computational-entropy/definition.md](foundations/computational-entropy/definition.md)
- [emergent-gravity/master-equation.md](emergent-gravity/master-equation.md)

---

## 2. Vision for Cohesion

A cohesive theory requires explicit connections at increasing levels:

| Level                  | Description                                      | Evidence Required                     |
|------------------------|--------------------------------------------------|---------------------------------------|
| Semantic / Analogical  | High-level concepts map (e.g. function → channel) | Clear prose + examples                |
| Structural             | Specific constructs correspond (decay vector → exported entropy) | Tables + derivations                  |
| Constructive / Derivational | Master equation or load terms can be motivated/discretized from the lambda model | Toy models + limiting arguments       |

**Desired outcome**: The lambda/IDEM work provides the *microscopic model of computation* that justifies and (eventually) discretizes the gravitational channel and load \(L\).

**Post dual-freeze note:** Stage-1 Euclidean dual (observation channel ↔ PM / induced \(G\)) is **constructive at toy level** and **settled at program level**. The remaining cohesion work is **structural/constructive IDEM → \(L\) / \(H_c\)** (M11), then continuum hygiene — not more residual dual scorecards. Type safety: \(L\) is a dimensionless scalar; \(G\) is a metric — **\(L \neq G\)**.

---

## 3. Key Correspondence Tables (Initial)

### 3.1 Core Entropy Concepts

| Classical / Lambda Side                  | Gravity Side                  | Current Rigor     | Notes / Next Work |
|------------------------------------------|-------------------------------|-------------------|-------------------|
| Computational entropy \(H_c\) = entropy of output distribution | \(S_c = S(\Phi_g(\rho))\)    | Semantic          | Direct generalization stated in canonical definition. |
| Different functions can produce identical output distributions (e.g. \(\sqrt{U}\) vs \(\max(U_1,U_2)\)) | Different microstate evolutions can produce equivalent \(S_c\) | Semantic / Structural | "Informationally equivalent" language already used. |
| Decay vector + irreversible overwriting  | Exported entropy to holographic screen / Hawking radiation | Structural (candidate) | Strong analogy; decay vector components flipping ≈ information loss term. |
| Infinite reduction paths for underivability | Information inaccessible to external observers | Analogical        | Promising for black-hole information problem. |
| AST size / reduction cost as complexity  | Energy-density term in \(L\)  | Candidate         | Needs toy model. |

### 3.2 Load \(L\) Terms

| Term in \(L\)                            | Possible Lambda / Computational Origin                  | Status |
|------------------------------------------|---------------------------------------------------------|--------|
| \(\beta E[\rho] / (V \epsilon_0)\)      | Term size, number of active redexes, or "energy" of the lambda expression | To develop |
| \(\gamma \| dS_c / d\tau \|_{reg}\)     | Rate of output entropy reduction or number of decay-vector flips per reduction step | Strong candidate |
| \(\delta S_{boundary} / S_{BH}(A)\)     | Global distinguishability / total registerable normal forms (related to \(d_f\) across ensemble) | To develop |

### 3.3 External continuum bridge: Bianconi (2025)

A closely related continuum theory is Bianconi’s *Gravity from entropy* (Phys. Rev. D **111**, 066001 (2025); arXiv:2408.14391). Bianconi derives modified Einstein equations from an **entropic action**: the quantum relative entropy between the spacetime metric \(g\) (treated as a local quantum operator / effective density matrix) and a **matter-induced metric** \(G\). An auxiliary **G-field** rewrites the theory as a dressed Einstein–Hilbert action with an **emergent small positive cosmological constant** \(\Lambda_G\) depending only on the G-field; equations remain second order. Low coupling recovers Einstein gravity with zero \(\Lambda\).

This sits in the same research family as our emergent-gravity thread (Jacobson → Verlinde → holographic / complexity pictures → information-theoretic gravity), but uses a **different primary entropy object**: relative entropy of metrics-as-operators, rather than computational entropy \(S_c\) of a channel’s output state. Dynamics are variational (action → EL / modified Einstein), whereas ours is a master equation with load-dependent proper time. Full comparison, open mappings (G-field ↔ \(L\), \(\Lambda_G\) ↔ cosmology recovery, discrete network precursor ↔ lambda/IDEM), and rigor status are in [synthesis/bridge-bianconi-relative-entropy.md](synthesis/bridge-bianconi-relative-entropy.md). PDF and notes: [papers/external/](papers/external/).

| Bianconi concept | Our side | Current rigor | Next work |
|------------------|----------|---------------|-----------|
| Relative entropy \(\operatorname{Tr} g \ln G^{-1}\) | Continuum limit of mismatch between geometry and matter/channel output pattern | Semantic / structural candidate | Relate to \(S_c\) or a relative form of \(H_c\) |
| Metric as effective density matrix | Local \(\rho\) and \(S_c = S(\Phi_g(\rho))\) | Semantic | Operator-vs-state identification |
| Matter-induced metric \(G = g + \alpha M - \beta\mathcal{R}\) | Terms in \(L\) (energy, entropy production, boundary) | Structural candidate | Explicit term-by-term map |
| G-field and \(\Lambda_G \ge 0\) | Load dressing / cosmological recovery | Analogical | Compare \(\Lambda_G(\mathcal{G})\) to FLRW/inflation regime of master equation |
| Discrete network precursor | Lambda / IDEM / games models | Analogical | Shared discrete→continuum program |
| **Euclidean warm-up** \(G=1+\alpha_G(\nabla\phi)^2\), PM = GfE flow | Observation channel \(H_c\), \(L_E/L_S\), load clock | **Constructive (toy) — program-level settled** (ACD-EW 6/6; T1′ / \(U_\star\)) | Optional paper pure PCRH\(_b\); do not default-chase residual dual |

**Action–Channel Duality (Euclidean Warm-Up):** formal statement, proof criteria, and experimental support in [synthesis/action-channel-duality-euclidean.md](synthesis/action-channel-duality-euclidean.md). Joint toys: `simulations/bridging/` (reference layer). Frozen claims: [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md).

---

## 4. Toy Models

### 4.1 Joint GfE ↔ load toy (settled pattern layer)

- 1D observation channel + classical PM + split load; scorecard **6/6 SUPPORT (PROMISING)**.
- 2D Catte PM lift and blackjack-belief IC also **6/6** (belief = pattern only).
- Residual dual is **time-windowed (T1′)** with unified pure window \(U_\star=[1.36,2.40]\) under soft PCRH\(_b\) — **program-level settled**.
- Paths: `simulations/bridging/gfe_load_joint_toy.ipynb`, `_joint_toy_v2_core.py`, `DESIGN_gfe_load_joint_toy.md`.
- **Not** continuum gravity confirmation; re-run for regression only.

### 4.2 Next constructive work (primary)

- **M11 IDEM → load:** design and (later) implement decay / recoverability contributions to \(L\) or \(H_c\) — [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md).
- Prefer: high entropy flux / many open outcomes ⇒ **higher** \(L\) (not “identity stockpile left to compute”).
- Optional later: true game-channel \(H_c\) (M12); continuum warm-up limit (M5); toy residual \(H_c\) vs von Neumann \(S_c\) (M10).

---

## 5. Progress Log

- **2026-06-22**: Duplication audit completed and added to PLAN.md.
- **2026-06-22**: Directory skeleton created.
- **2026-06-22**: First canonicals extracted:
  - `foundations/computational-entropy/definition.md`
  - `emergent-gravity/master-equation.md`
- Old copies marked with "Historical / superseded" headers (non-destructive).
- This THEORY.md seeded with audit findings and initial tables.
- **2026-07-14**: Bianconi (2025) *Gravity from entropy* added under `papers/external/`; bridge note in `synthesis/bridge-bianconi-relative-entropy.md`; §3.3 correspondence table seeded; bibliography entry in main `.tex`.
- **2026-07-14**: Joint toy v2 (P0–P2) → 6/6 SUPPORT; formalized **ACD-EW** in `synthesis/action-channel-duality-euclidean.md`.
- **2026-07-14**: ACD-EW §10 T1 sketch; main `.tex` unification paragraph; **2D joint toy 6/6 SUPPORT**.
- **2026-07-14**: Parallel synthesis pack — continuum transfer dictionary, weak-field GfE vs load, T1 standalone proof plan, blackjack-belief dual toy (6/6 pattern only). All preliminary; no continuum equivalence claimed.
- **2026-07-14**: `synthesis/PACK_INDEX.md` + `synthesis/OPEN_MATH_DECISION_LOG.md` (M1–M12 board; default next math: M1 then M6 prep via M8/M7).
- **2026-07-14**: D1 M-series **executed** — M1 C′/T1′; M5 continuum bridge; M8 Newton gap N1; M7 map; M6 WEAK PASS Poisson / FAIL identity; M2–M4 deferred; M9–M12 deferred. See OPEN_MATH D2.
- **2026-07-15**: **Euclidean dual freeze** — residual dual program closed at research-program level (\(U_\star\), toys 6/6×3, ACD-EW). Primary track switches to **M11 IDEM→load** (+ continuum hygiene M5/M10, claim freeze / paper outline). Do not default-chase heat/PM residual. Claims: [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md); M11: [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md). Central gap remains **IDEM ↔ gravity**.
- **2026-07-15 (D9)**: M11 design note landed; Phase 1 constructive AND-gate ledger (`simulations/classical/m11_and_gate_ledger.py`) with exact \(H_c\), export \(H(X\mid Y)\), discrete \(L_E,L_S,L_B\). Continuum \(L\)/\(G\) from IDEM still **not** claimed.
- **2026-07-15 (D10–D11)**: Continuum hygiene M5/M10 dictionaries; M11 Phase 2 (multi-step Boolean, tiny SKI, minimal shoe); paper outline at [papers/06-synthesis/OUTLINE.md](papers/06-synthesis/OUTLINE.md). Default next = draft paper, not residual dual.
- **2026-07-15 (D12)**: Failure-mode [CLAIM_GATE](synthesis/CLAIM_GATE.md); [m11c continuum motivation](synthesis/m11c-continuum-motivation.md); coupled-regions ledger; M10 P1 non-identity \(H_c^{\mathrm{toy}}\neq H(Z)\); M5b smooth action \(O(h)\) sketch.
- **2026-07-15 (D13)**: Relationships — [m11d composition](synthesis/m11d-composition-laws.md) (path-dep \(\sum L_S\)); [m11e Landauer](synthesis/m11e-landauer-export.md); [m5c warm-up/PM](synthesis/m5c-warmup-pm-gradient-flow.md).
- **2026-07-15 (D14)**: First program paper draft; R4a [m6d-promotion-nogo.md](synthesis/m6d-promotion-nogo.md).
- **2026-07-15 (D15)**: Conclusion freeze — [FINAL.md](papers/06-synthesis/FINAL.md); [PROGRAM_CONCLUSIONS.md](synthesis/PROGRAM_CONCLUSIONS.md) P1–P11; M5b lemma polish.
- **2026-07-15**: [OPEN_AVENUES.md](synthesis/OPEN_AVENUES.md) — post-freeze map: concluded vs **new theory** (missing theorems) vs experiment; O1–O5 checklist.

---

## 6. Open Questions

**Still central (IDEM ↔ gravity — dual toys do not answer these):**
- What is the precise representation of local quantum microstates \(\rho\) using lambda terms (or is it only motivational)?
- How strictly should the three terms in \(L\) be *derived* vs. *motivated* from the computational model? (**M11**)
- Can Bianconi’s full (Lorentzian, curvature-coupled) relative entropy be recovered as a continuum limit of computational relative entropy between “realized geometry” and matter-channel output patterns?
- Is the G-field closer to a dressing of \(g_{\mu\nu}\), a coarse-grained load \(L\), or a new independent degree of freedom in our picture? (Keep **\(L \neq G\)**.)

**Program / paper:**
- Do we aim for one major synthesis paper or a short monograph?
- What level of simulation evidence is required beyond ACD-EW constructive verification? (Toys saturated for dual **pattern**; new evidence should target M11 / continuum hygiene.)

**Deprioritized (optional paper depth only — not default open crisis):**
- Pure residual-domination without MC soft spots (PCRH\(_b\)); residual dual is **program-level settled** as time-windowed T1′ / \(U_\star\).

See also the "Open Questions" section in PLAN.md and [PROGRESS_REPORT.md](PROGRESS_REPORT.md) §7.

---

*This document should be updated whenever new mappings are articulated or canonical files are added.*
