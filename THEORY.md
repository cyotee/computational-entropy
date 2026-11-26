# THEORY.md — Boltzmann–Shannon Unification: Tier 1 → Tier 2 → Tier 3

**Status**: Living architecture document (seeded 2026-06-22; Euclidean dual freeze 2026-07-15; two-paper split 2026-07-29; **three-tier restructure 2026-11-26**).

> **How this document is ordered (2026-11-26).** **Tier 1** (primary result, §1–§4) opens with the research motivator and then presents the proposed mathematical object, channel-level entropy (full statements and proofs in [CORE.md](CORE.md)). **Tier 2** (secondary result, no gravity) covers instruction persistence on a finite substrate ([TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md)). **[Tier 3: Conjecture](#tier-3-conjecture)** quarantines everything gravitational or quantum, as open conjecture resting on Tier 1 rather than supported claims. The author has no formal training in information theory or statistical mechanics, so each Tier 1–2 assertion carries a pointer to an in-repo derivation or computation.

**Claims sheet:** [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · **Tier 1:** [CORE.md](CORE.md) · **Tier 2:** [TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md) · **Progress:** [PROGRESS_REPORT.md](PROGRESS_REPORT.md) · **Plan:** [PLAN.md](PLAN.md)

---

## Tier 1: Computational entropy (primary result)

A proposed mathematical object for consideration, with no GR-level certainty and no gravitational connection. *Relation to prior work:* the repo reached \(H(X\mid Y)\) by its own route, years after Baez–Fritz–Leinster (2011) and Fullwood–Parzygnat (2021). This is independent convergence, not priority ([CORE §4.1](CORE.md#41-relation-to-prior-work-independent-convergence-added-2026-11-26)).

### 1. Motivation: a Boltzmann–Shannon unification

The driving intent is a **Boltzmann–Shannon unification**: one notion of entropy that reads, on the same object, both as Shannon's uncertainty about a signal and as Boltzmann's logarithmic count \(k_B\ln W\) of the microstates compatible with an observed macrostate. Shannon entropy is normally attached to a static distribution and does not measure what a computation does to random inputs ([foundations/computational-entropy/definition.md](foundations/computational-entropy/definition.md), Premise).

The proposed mathematical object is **entropy defined on a channel's action on its input distribution**, rather than on a static distribution. An output value plays the role of a macrostate, and its preimage plays the role of the compatible microstates ([CORE §2.3](CORE.md#23-the-boltzmann-form-reading-uniform-inputs-deterministic-maps)).

### 2. The core object: channel-level entropy

Full definitions, theorems and proofs: **[CORE.md](CORE.md)**. Summary:

| Item | Statement | Pointer |
|------|-----------|---------|
| Object | channel \(p(y\mid x)\) acting on \(X\sim p_X\); deterministic \(Y=f(X)\) is the special case | CORE §2.1 |
| Computational entropy | \(H_c(f;p_X) := H(Y)\) | CORE Def. 1 · [Paper A](papers/01-foundations/PAPER_A_computational_entropy.md) §1 |
| Informational equivalence | same output law \(p_Y\) (equal \(H_c\) is **not** sufficient: \(\min(U_1,U_2)\) vs \(\max(U_1,U_2)\)) | CORE P1 · [AGENTS.md](AGENTS.md) pitfall 1 |
| Export | \(H(X\mid Y)\) (single-shot slot \(L_S\)) | CORE Def. 2 · Paper A §3 |
| Export identity | \(H(X)-H(Y)=H(X\mid Y)-H(Y\mid X)\); \(=H(X\mid Y)\) if deterministic | Paper A Thm 1 · `simulations/classical/m11_and_gate_ledger.py` |
| Boltzmann-form split (uniform input, deterministic) | \(\log_2 N = H(Y) + \sum_y p_Y(y)\log_2\lvert f^{-1}(y)\rvert\) (formal only) | CORE §2.3 · [Paper C](papers/02-computational-models/PAPER_C_decay_algebra.md) §2 |
| Landauer coincidence | \(Q\ge kT\ln 2\cdot H(X\mid Y)\) for deterministic maps (external theorem) | Paper A Thm 2 · `m11_landauer_and_ledger.py` |
| Stage-wise ledger | path-dependent \(\sum L_S\) (1-bit gap); a **convention**, not heat | Paper A Thm 3 · `m11_composition_ledger.py` |
| Decay algebra | 1D density \(a=0.3007568\); general-\(w\) existence, Blackwell form, reset ⇒ exact finite algebra; 2D strip; continuum \(\sigma(x)\) (witnessed) | Paper C Thms 1–2, §5–§6 · `m11_decay_algebra*.py`, `m11_continuum_embedding.py` |

### 3. Genuinely new vs standard

See the two-column table in [CORE §4](CORE.md#4-genuinely-new-vs-standard). In short:
- **Candidate new (literature not yet checked):** the *framing* (channel–input pair, export); composition rules and path accounting *as a framework*, with the identities themselves standard and the 1-bit path gap a convention rather than heat; the decay algebra (Paper C: \(a=0.3007568\), and the general-\(w\) reset-gate ⇒ exact-finite criterion); and the Tier 2 resource-bound conjecture.
- **Standard (attributed):** conditional entropy \(H(X\mid Y)\) and its characterization as the information loss of a map (Baez–Fritz–Leinster 2011; Fullwood–Parzygnat 2021); Shannon entropy, the chain rule and data processing; Landauer-type bounds (Landauer; Bennett; Sagawa–Ueda; Sagawa); Blackwell's representation; the grouping property and type-class counting behind the Boltzmann-form split. \(H(X\mid Y)\) is **not** claimed as a new principle.

### 4. Open problems on the core

From [CORE §5](CORE.md#5-is-this-more-than-shannon-entropy) ("Is this more than Shannon entropy?"):
- **OP1 (separation):** a channel-level quantity that is not a functional of \(p_{XY}\) yet carries a proved operational meaning.
- **OP2 (Boltzmann–Shannon unification proper):** derive, for an explicit physical model, that the preimage count is a thermodynamic microstate count.
- **OP3 (decay algebra):** literature check, the converse of the reset criterion, and a general hydrodynamic theorem for \(\sigma(x)\).

---

## Tier 2: Instruction persistence on a finite substrate (secondary result)

Full text: **[TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md)** · script `simulations/classical/tier2_instruction_persistence.py`. No gravity, no quantum layer.

| Item | Statement | Status |
|------|-----------|--------|
| \(d_f^{\#}\) | \(d_f^{\#} := \log_2\lvert[f]\rvert\), where \([f]\) is the class of maps with the same output law (law-based equivalence, CORE P1). For uniform input, \(\lvert[f]\rvert = N!/\prod_y W_y!\) and \(d_f^{\#}/N\to H(Y)\). The legacy Bayesian \(d_f = 1-2^{-d_f^{\#}}\) under a uniform prior. | definition; standard counting |
| Composition | \(d_f^{\#} = d_{g\circ f}^{\#} + R(g\mid f)\) exactly; naive \(d_f^{\#}+d_g^{\#}\) additivity is false | **proved**; script part B |
| Problem T2 | joint minimum of output capacity + instruction persistence on a finite register with gates NOT/CNOT/Toffoli | **open** |
| Conjecture T2 | on a finite, non-free substrate, persistence scales with class log-cardinality \(d^{\#}\), not with one representative's \(K(f)\) | **open** |
| Toy | one stage, \(n=2\): \(d_f^{\#}\) does not order register need (XOR: 0 ancillas; AND: 1) | computed |

---

## Tier 3: Conjecture

> **Published as open conjecture resting on the core result, not as supported claims.** Everything in this section depends on Tier 1 (§2, the foundation) and possibly Tier 2, *plus* hypotheses that the repository has not proved. Rigor labels (semantic / structural / calibration / external theorem / constructive-toy) still apply item by item; see [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md). Nothing here should be cited as a result of the programme.

### C.1 Gravitational programme

- **Gravitational channel and load.** Gravity is modelled as a CPTP channel \(\Phi_g\), with a dimensionless **load** \(L(\rho,g)\) and the load clock \(d\tau = dt/(1+\alpha L)\). Canonical: [emergent-gravity/master-equation.md](emergent-gravity/master-equation.md). Paper B (conjecture): [papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md](papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md). Integrated paper (conjecture): [papers/06-synthesis/PAPER.md](papers/06-synthesis/PAPER.md).
- **Jacobson path (Path J/M).** Newton is recovered only via Clausius on local horizons → Einstein (Jacobson 1995, imported) → weak-field GR → Poisson, plus the on-shell load-clock identification \(\alpha L = -\Phi/c^2\). That identification fixes the sum \(\alpha L\) only. The former calibration \(\alpha\beta = 4\pi G/c^4\) is **withdrawn** because it is dimensionally invalid (C17). Pointwise \(\Phi\propto\rho\) Newton is withdrawn. See [emergent-gravity/recoveries/newtonian/README.md](emergent-gravity/recoveries/newtonian/README.md).
- **Load no-go (C17).** The entropy term varies at fixed \(T_{\mu\nu}\) while \(\alpha L = -\Phi/c^2\) is \(T_{\mu\nu}\)-fixed. So \(L\) is a diagnostic co-moving with the Path-J/M metric, not an independent clock, and the falsifiability verdict is **reformulation**. See [emergent-gravity/load-dimensional-analysis.md](emergent-gravity/load-dimensional-analysis.md) and [papers/FALSIFIABILITY_L_vs_GR.md](papers/FALSIFIABILITY_L_vs_GR.md).
- **R4a promotion.** Entropy production promoted into the field equations is Bianchi-consistent and reduces to ΛCDM. Its derived phantom sign is retracted (EoS-inconsistent), and reservoir dark energy is not framework-grounded (C18). See [emergent-gravity/r4a-promotion.md](emergent-gravity/r4a-promotion.md).
- **GfE contact and Euclidean dual.** M6 gives a WEAK PASS on shared Poisson and a FAIL on framework identity. ACD-EW is a constructive Euclidean warm-up dual at toy/pattern level only (C1–C13).
- **Classical → gravity bridge.** Paper C's \(\sigma(x)\) is a classical density. Identifying it with the load term \(\gamma\lvert dS_c/d\tau\rvert\) is a labelled semantic step, not a construction (non-claim 10).
- **Type safety (locked):** \(L\) is a dimensionless scalar, \(G\) is a metric, and \(L \neq G\).

### C.2 Quantum channel / von Neumann layer

- \(S_c(\Phi;\rho) := S(\Phi(\rho))\) is a definition carried over from the classical case ([foundations/computational-entropy/definition.md](foundations/computational-entropy/definition.md), Quantum Generalization).
- **Provenance (2026-11-26):** the von Neumann entropy connection was proposed by an AI agent during exploration and is scaffolding, not a derived result ([PROGRESS_REPORT.md](PROGRESS_REPORT.md)). No theorem in Papers A or C uses \(S_c\).
- Entropy-object tags (A–E) and the non-identities toy \(H_c\neq S_c\) and \(H_c^{\mathrm{disc}}\neq S_c\) stay in force: [GLOSSARY.md](GLOSSARY.md) and [synthesis/m10-sc-vs-toy-hc.md](synthesis/m10-sc-vs-toy-hc.md).

### Bridge architecture (pre-restructure material, kept for reference)

> **Positioning (2026-07-29, historical):** The program is now split into **Paper A** (solid core: computational entropy + Landauer-exact export — [papers/01-foundations/PAPER_A_computational_entropy.md](papers/01-foundations/PAPER_A_computational_entropy.md)) and **Paper B** (emergent-gravity **conjecture** — [papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md](papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md)). Falsifiability verdict = **reformulation** with the entropy-production term flagged as the sole candidate departure ([papers/FALSIFIABILITY_L_vs_GR.md](papers/FALSIFIABILITY_L_vs_GR.md)). Consolidated status: [synthesis/RESULTS_LEDGER.md](synthesis/RESULTS_LEDGER.md).

This is the living source of truth for the conceptual bridge between:
- The **lambda calculus / computational models** thread (IDEM functions, decay vectors, output distribution entropy, games as models, etc.)
- The **emergent gravity** thread (gravitational channel \(\Phi_g\), computational load \(L\), master equation, and recoveries)

#### Active research focus (historical snapshot, 2026-07-15; superseded by the 2026-11-26 core-first restructure)

| Layer | Status | Notes |
|-------|--------|--------|
| **Euclidean ACD-EW dual** (heat/PM residual, joint toys, T1′ / \(U_\star\)) | **Program-level settled** | Do not default-chase more dual scorecards; optional pure PCRH\(_b\) only for paper depth |
| **Primary next** | **M11 IDEM → load** | Connect decay / recoverability to \(L\) or \(H_c\); attacks central gap |
| **Also** | Continuum hygiene (M5/M10); claim freeze / paper outline | Not continuum ME ⇔ GfE |

**Claims sheet:** [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · **M11 design:** [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) · **Progress:** [PROGRESS_REPORT.md](PROGRESS_REPORT.md)

#### Purpose of the bridge architecture
- Define explicit mappings between concepts.
- Document the current level of rigor for each mapping (analogy / structural / constructive).
- Provide worked examples and correspondence tables.
- Guide the extraction of canonical content and the writing of future papers.
- Track open questions and progress toward a unified theory.

See [PLAN.md](PLAN.md) for the overall reorganization and paper plan.

---

### C.3 Current state diagnosis (bridge, pre-restructure §1)

The repository contains two substantial but only loosely connected research threads:

#### Lambda / classical computational entropy thread
- Rich formal machinery: IDEM functions (with arity, decay vectors \([d_1 \dots d_n], d_f\)), combinatorics from lambda expressions, infinite reduction paths for underivability, vectorial lambda calculus.
- Concrete examples: Blackjack and other games modeled as functions that reduce entropy / increase predictive accuracy.
- Early drafts explicitly attempted to ground entropy calculations in lambda calculus (system entropy ≈ log |AST size of normal form|, potential via unreduced paths).

#### Emergent gravity thread
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

### C.4 Vision for cohesion (pre-restructure §2)

A cohesive theory requires explicit connections at increasing levels:

| Level                  | Description                                      | Evidence Required                     |
|------------------------|--------------------------------------------------|---------------------------------------|
| Semantic / Analogical  | High-level concepts map (e.g. function → channel) | Clear prose + examples                |
| Structural             | Specific constructs correspond (decay vector → exported entropy) | Tables + derivations                  |
| Constructive / Derivational | Master equation or load terms can be motivated/discretized from the lambda model | Toy models + limiting arguments       |

**Desired outcome**: The lambda/IDEM work provides the *microscopic model of computation* that justifies and (eventually) discretizes the gravitational channel and load \(L\).

**Post dual-freeze note:** Stage-1 Euclidean dual (observation channel ↔ PM / induced \(G\)) is **constructive at toy level** and **settled at program level**. The remaining cohesion work is **structural/constructive IDEM → \(L\) / \(H_c\)** (M11), then continuum hygiene — not more residual dual scorecards. Type safety: \(L\) is a dimensionless scalar; \(G\) is a metric — **\(L \neq G\)**.

---

### C.5 Key correspondence tables (pre-restructure §3)

#### C.5.1 Core entropy concepts

| Classical / Lambda Side                  | Gravity Side                  | Current Rigor     | Notes / Next Work |
|------------------------------------------|-------------------------------|-------------------|-------------------|
| Computational entropy \(H_c\) = entropy of output distribution | \(S_c = S(\Phi_g(\rho))\)    | Semantic          | Direct generalization stated in canonical definition. |
| Different functions can produce identical output distributions (e.g. \(\sqrt{U}\) vs \(\max(U_1,U_2)\)) | Different microstate evolutions can produce the same output state (hence equal \(S_c\); equal \(S_c\) alone is not equivalence, see AGENTS.md pitfall 1) | Semantic / Structural | "Informationally equivalent" language already used. |
| Decay vector + irreversible overwriting  | Exported entropy to holographic screen / Hawking radiation | Structural (candidate) | Strong analogy; decay vector components flipping ≈ information loss term. |
| Infinite reduction paths for underivability | Information inaccessible to external observers | Analogical        | Promising for black-hole information problem. |
| AST size / reduction cost as complexity  | Energy-density term in \(L\)  | Candidate         | Needs toy model. |

#### C.5.2 Load \(L\) terms

| Term in \(L\)                            | Possible Lambda / Computational Origin                  | Status |
|------------------------------------------|---------------------------------------------------------|--------|
| \(\beta E[\rho] / (V \epsilon_0)\)      | Term size, number of active redexes, or "energy" of the lambda expression | To develop |
| \(\gamma \| dS_c / d\tau \|_{reg}\)     | Rate of output entropy reduction or number of decay-vector flips per reduction step | Strong candidate |
| \(\delta S_{boundary} / S_{BH}(A)\)     | Global distinguishability / total registerable normal forms (related to \(d_f\) across ensemble) | To develop |

#### C.5.3 External continuum bridge: Bianconi (2025)

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

### C.6 Toy models (pre-restructure §4)

#### C.6.1 Joint GfE ↔ load toy (settled pattern layer)

- 1D observation channel + classical PM + split load; scorecard **6/6 SUPPORT (PROMISING)**.
- 2D Catte PM lift and blackjack-belief IC also **6/6** (belief = pattern only).
- Residual dual is **time-windowed (T1′)** with unified pure window \(U_\star=[1.36,2.40]\) under soft PCRH\(_b\) — **program-level settled**.
- Paths: `simulations/bridging/gfe_load_joint_toy.ipynb`, `_joint_toy_v2_core.py`, `DESIGN_gfe_load_joint_toy.md`.
- **Not** continuum gravity confirmation; re-run for regression only.

#### C.6.2 Constructive work toward IDEM → load (historical; M11 has since advanced into Paper C)

- **M11 IDEM → load:** design and (later) implement decay / recoverability contributions to \(L\) or \(H_c\) — [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md).
- Prefer: high entropy flux / many open outcomes ⇒ **higher** \(L\) (not “identity stockpile left to compute”).
- Optional later: true game-channel \(H_c\) (M12); continuum warm-up limit (M5); toy residual \(H_c\) vs von Neumann \(S_c\) (M10).

---

### C.7 Open questions on the conjecture side (pre-restructure §6)

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

### C.8 Three linked conjectures ranked by testability

> **Conjecture: not derived, not tested.** This subsection records three proposals by the programme author, ranked in his order by how testable they are. None of them is derived in this repository, none has been tested, and none is a claim of the programme. They rest on Tier 1 plus hypotheses that are not yet defined, let alone proved (see *Status of the ingredients* and *Open definitional gap* below). Nothing in Tier 1 or Tier 2 uses them.

**Falsifiability, stated up front.** Only claim 1 could be falsified on its own. Claim 2 is a proposed theoretical derivation that could be checked against existing holographic calculations. Claim 3 cannot be confirmed or ruled out on its own; it is an interpretive scaffold for claims 1 and 2.

**Status of the ingredients.** The repository's own toy results do not currently support the mechanism these proposals lean on:

- **No saturation seen.** The procedural-share runs on the generalized amplitude-damping (GAD) toy ([docs/procedural-share.md](docs/procedural-share.md); commits 26b3589 and b12882d, binary and 16-symbol readouts) found **no** concave rise or saturation of the procedural share. The one slice that resembles that shape is not robust.
- **The motivating inequality is false in general.** \(I(X;Y) + H(F\mid Y) \le H(Y)\) fails in general. The bound that does hold is \(I(X;Y) + I(F;Y) \le H(Y)\).
- **"100 % procedural share" is undefined at a horizon.** Given the two points above, the phrase has no worked-out definition for a horizon and no in-repo derivation.
- **The joint encoding bound falls with temperature.** The joint encoding bound C_minus_K **falls** monotonically with \(T\) on the thermal toy ([docs/thermal-channel-cost.md](docs/thermal-channel-cost.md) §7).
- **"Alphabet" is defined only for a toy.** In the repository it means the output alphabet size of a classical readout of a toy channel (e.g. 2 or 16 symbols in the procedural-share runs). Nothing defines a physical alphabet for a black hole, the early universe or "our" universe.

**Open definitional gap (blocks claims 1–3).** The physical meaning of "a wider alphabet than ours", "a larger prior alphabet" and "a region where one alphabet size prevails" is **undefined**. Defining it is the first open problem. It would need to say what object has an alphabet, how its size is measured, and how it maps onto quantities in Hawking or holographic calculations.

**Claim 1: radiation signature (ranked most testable; load-bearing).** *Author's statement:* the final Hawking radiation spectrum contains a residual component that cannot be decoded, because the final evaporation burst may need a wider alphabet than ours.

- *Why it ranks first.* In principle it could be compared with quantum-gravity-corrected Hawking spectra, so it is the only one of the three that could be falsified on its own.
- *Why it is not falsifiable yet.* That needs a **quantitative** prediction: which spectral feature, at what magnitude, and how it differs from which QG-corrected spectrum. No such prediction exists. Producing one is the required next step, and it depends on closing the definitional gap above.
- *Regime caveat.* The final stage of evaporation is the Planck regime, where semiclassical calculations break down. Page (1993) describes Hawking's information-loss argument as assuming the semiclassical approximation holds only until the hole nears the Planck mass. So the comparison spectrum is itself not settled.
- *Observational caveat.* Hawking radiation from black holes has not been observed.

**Claim 2: capacity-saturation reading of the singularity (ranked middle).** *Author's statement:* at the horizon the procedural share reaches 100 % (capacity saturation). The Page curve is *proposed to follow as a corollary; derivation not done*: as inflow drops, capacity is released back to the semantic side.

- *What a derivation would have to do.* Reproduce the Page time (Page 1993) and the quantum-extremal-surface / island results that yield the Page curve in holographic and semiclassical gravity models (Penington 2019; Almheiri–Engelhardt–Marolf–Maxfield 2019).
- *What "middle testability" means.* Checkable against **existing calculations**, not against experiment.
- *Status in the repository.* The pre-restructure drafts [quantum/Blackhole_Evaporation.md](quantum/Blackhole_Evaporation.md) and [quantum/Blackholes.md](quantum/Blackholes.md) describe a Page-curve shape from the load terms qualitatively. They do not compute the Page time or a quantum extremal surface, so they are not the derivation required here.
- *Undefined ingredient.* As listed under *Status of the ingredients*, "100 % procedural share" itself is not yet defined at a horizon.

**Claim 3: direction of the alphabet cascade (ranked least testable; interpretive).** *Author's statement:* the Big Bang was a contraction from a larger prior alphabet, horizons are further contractions, and the universe is the region where one alphabet size prevails.

- *Status.* This is an interpretation, stated as such. It makes no independent prediction and cannot be confirmed or ruled out on its own. It serves as a scaffold that motivates claims 1 and 2.

**Dependencies.** Claims 1 and 2 rest on Tier 1 and on the physical alphabet notion, which is still undefined. Claim 2 also rests on a horizon definition of the procedural share that does not yet exist. Claim 3 is a scaffold only. None of the three is a resolution of the black-hole information problem or a prediction that has been checked.

**References (verified 2026-11-26).**
- D. N. Page, "Information in black hole radiation," *Phys. Rev. Lett.* **71**, 3743 (1993); arXiv:hep-th/9306083.
- G. Penington, "Entanglement wedge reconstruction and the information paradox," arXiv:1905.08255 (2019); *JHEP* **09** (2020) 002.
- A. Almheiri, N. Engelhardt, D. Marolf, H. Maxfield, "The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole," arXiv:1905.08762 (2019); *JHEP* **12** (2019) 063.

---

## Progress log

- **2026-06-22**: Duplication audit completed and added to PLAN.md.
- **2026-06-22**: Directory skeleton created.
- **2026-06-22**: First canonicals extracted:
  - `foundations/computational-entropy/definition.md`
  - `emergent-gravity/master-equation.md`
- Old copies marked with "Historical / superseded" headers (non-destructive).
- This THEORY.md seeded with audit findings and initial tables.
- **2026-07-14**: Bianconi (2025) *Gravity from entropy* added under `papers/external/`; bridge note in `synthesis/bridge-bianconi-relative-entropy.md`; §3.3 (now §C.5.3) correspondence table seeded; bibliography entry in main `.tex`.
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
- **2026-11-26**: Core-first restructure. Lead is now the **Boltzmann–Shannon unification** motivator, then the channel-level entropy core ([CORE.md](CORE.md); Papers A and C), then **Conjecture** (gravitational programme + quantum / von Neumann layer); reorganised the same day into Tier 1 → Tier 2 (instruction persistence) → Tier 3 (conjecture). Pre-restructure §§1–4 and §6 moved under Conjecture as §C.3–§C.7, with content unchanged apart from headings.
- **2026-11-26**: Added Tier 3 §C.8, which ranks three author conjectures by testability (radiation signature, capacity-saturation reading, alphabet cascade). It is labelled *conjecture: not derived, not tested*.

---

*This document should be updated whenever new mappings are articulated or canonical files are added. Tier 1 results go in [CORE.md](CORE.md), Tier 2 in [TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md); bridge, gravity and quantum material stays under **Tier 3: Conjecture**.*
