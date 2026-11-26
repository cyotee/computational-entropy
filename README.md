# Computational Entropy

**Preliminary research.** The supporting constructions and numerical ledgers are real. **Nothing here has GR-level certainty**, and the author has no formal training in information theory or statistical mechanics. Every assertion in the lead material is therefore backed by a derivation or computation in this repository, with a pointer. Anything not backed that way is labelled **Conjecture**.

The work is organised in **three tiers**, each resting on the one before:

1. **Tier 1 (primary result): computational entropy**, motivated by a **Boltzmann–Shannon unification**. It is a proposed mathematical object for consideration, with its definition, theorems and supporting computations. No GR-level certainty, no gravitational connection.
2. **Tier 2 (secondary result, no gravity): instruction persistence on a finite substrate.** The log-cardinality \(d_f^{\#}\) of an observational equivalence class, an exact composition rule, and an open joint-minimum problem.
3. **Tier 3 (conjecture only):** how Tiers 1–2 *might* connect to gravity and to a quantum / von Neumann layer.

## Tier 1: Computational entropy (primary result)

### Motivation: a Boltzmann–Shannon unification

The driving intent is a **Boltzmann–Shannon unification**: one notion of entropy that reads, on the same object, both as Shannon's uncertainty and as Boltzmann's logarithmic count \(k_B\ln W\) of the microstates compatible with what is observed. Shannon entropy is usually attached to a *static* distribution. It does not measure what a computation *does* to random inputs.

### The channel-level definition → [CORE.md](CORE.md)

The mathematical object proposed to serve that intent is **entropy defined on a channel's action on its input distribution**, rather than on a static distribution. For a channel \(p(y\mid x)\) acting on \(X\sim p_X\):

- **computational entropy** \(H_c(f;p_X) := H(Y)\), the entropy of the induced output law
- **export** \(H(X\mid Y)\), the input distinguishability the channel discards
- **export identity (any channel)** \(H(X)-H(Y) = H(X\mid Y) - H(Y\mid X)\), which reduces to \(H(X)-H_c = H(X\mid Y)\) for deterministic maps

Two maps that induce the same output distribution are informationally equivalent (and so have the same output entropy); equal output entropy alone does not imply equivalence. For example, \(\sqrt U\) and \(\max(U_1,U_2)\) share the density \(2y\), while \(\min(U_1,U_2)\) has the same differential entropy but a different law, \(2(1-y)\) ([canonical definition](foundations/computational-entropy/definition.md), Key Property; Paper A Prop. 1).

With uniform inputs and a deterministic map, \(H(X\mid Y)=\sum_y p_Y(y)\log_2|f^{-1}(y)|\). This is a mean log-count of compatible inputs, which is Boltzmann's form. It is a *formal* correspondence, not a physical derivation ([CORE §2.3](CORE.md#23-the-boltzmann-form-reading-uniform-inputs-deterministic-maps)).

| Result | Status | Where |
|--------|--------|-------|
| Framing: channel–input pair, export \(H(X\mid Y)\) | **candidate framing**; \(H(X\mid Y)\) itself is standard (not a new principle) | CORE §4 |
| Export identity (chain rule, two-sided) | **standard**, proved inline | [Paper A](papers/01-foundations/PAPER_A_computational_entropy.md) Thm 1 · `m11_and_gate_ledger.py` |
| Landauer coincidence \(Q\ge kT\ln2\cdot H(X\mid Y)\) (deterministic) | **standard** (external theorem) | Paper A Thm 2 · `m11_landauer_and_ledger.py` |
| Composition rules and path accounting (stage-wise ledger) | **candidate framework**; identities standard; 1-bit gap is a convention, not heat | Paper A Thm 3 · `m11_composition_ledger.py` |
| 1D export density \(a=0.3007568\); general-\(w\) reset ⇒ exact finite algebra (converse open) | **candidate new**, proved (literature not yet checked) | [Paper C](papers/02-computational-models/PAPER_C_decay_algebra.md) Thms 1–2 · `m11_decay_algebra*.py` |
| Continuum density field \(\sigma(x)\) | witnessed (theorem open) | Paper C §6 · `m11_continuum_embedding.py` |

**Is this more than Shannon entropy?** Not yet established. As stated, every core quantity is a Shannon functional of the joint law \(p_X(x)\,p(y\mid x)\). Entropy as the information loss of a map has already been characterized as conditional entropy (Baez–Fritz–Leinster 2011; Fullwood–Parzygnat 2021). [CORE §5](CORE.md#5-is-this-more-than-shannon-entropy) states what would have to be proved for a genuine separation.

**Relation to prior work.** The repo reached \(H(X\mid Y)\) by its own route, years after Baez–Fritz–Leinster (2011) and Fullwood–Parzygnat (2021). This is independent convergence, not priority ([CORE §4.1](CORE.md#41-relation-to-prior-work-independent-convergence-added-2026-11-26)).

**Core papers:** [Paper A — computational entropy and export](papers/01-foundations/PAPER_A_computational_entropy.md) · [Paper C — the decay algebra](papers/02-computational-models/PAPER_C_decay_algebra.md). Both are classical and make no gravity claims.

## Tier 2: Instruction persistence on a finite substrate (secondary result)

→ **[TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md)** · script `simulations/classical/tier2_instruction_persistence.py`

The question is what a finite, non-free substrate must keep so that the next computation stays possible. The function-unidentifiability measure is reframed from a Bayesian posterior into a count: \(d_f^{\#} := \log_2|[f]|\), where \([f]\) is the class of maps with the same output law (for uniform inputs, \(|[f]| = N!/\prod_y W_y!\)).
- **Proved:** an exact composition rule \(d_f^{\#} = d_{g\circ f}^{\#} + R(g\mid f)\). Naive additivity \(d_{g\circ f}^{\#} = d_f^{\#} + d_g^{\#}\) is false.
- **Open (Problem T2 / Conjecture T2):** the joint minimum of output capacity plus instruction persistence on a finite register with a universal (Toffoli) gate set.
- **Toy result:** \(d_f^{\#}\) alone does not order register need; XOR needs no ancilla, AND needs one.

## Tier 3: Conjecture

> **Published as open conjecture resting on the core result, not as supported claims.** Nothing in this section is asserted by the programme. Each item depends on Tier 1 (the foundation) plus additional, unproved hypotheses. No Tier 3 content is used by Tiers 1 or 2.

**Gravitational programme.** Gravity is modelled as a channel \(\Phi_g\) with a dimensionless **load** \(L\) and a load-gated clock \(d\tau = dt/(1+\alpha L)\). See [Paper B (conjecture)](papers/04-gravitational-channel/PAPER_B_emergent_gravity_conjecture.md) and the [integrated paper](papers/06-synthesis/PAPER.md), which is also conjecture (on the site: [§6. Channel, load & master equation](https://cyotee.github.io/computational-entropy/papers/chapters/06-channel-load-master-equation/)).
- Newton is recovered only via **Path J/M**: Jacobson's Clausius → Einstein theorem (imported) → weak-field GR, plus the on-shell identification \(\alpha L = -\Phi/c^2\). The former calibration \(\alpha\beta = 4\pi G/c^4\) is **withdrawn**: it is dimensionally invalid (C17, [load-dimensional-analysis](emergent-gravity/load-dimensional-analysis.md)).
- **Load no-go (C17):** \(L\) is a diagnostic that co-moves with the Path-J/M metric, not an independent clock. The falsifiability verdict is **reformulation** ([analysis](papers/FALSIFIABILITY_L_vs_GR.md)).
- **R4a:** promoting entropy production into the field equations gives a candidate whose derived phantom sign is retracted. Reservoir dark energy is not grounded ([r4a-promotion](emergent-gravity/r4a-promotion.md)).
- The Euclidean dual (ACD-EW) and GfE contact (M6 WEAK PASS / identity FAIL) are pattern-level only ([CURRENT_CLAIMS](synthesis/CURRENT_CLAIMS.md)).

**Quantum channel / von Neumann layer.** \(S_c(\Phi;\rho) := S(\Phi(\rho))\) is a *definition* carried over from the classical case. An AI agent proposed it during exploration. It is scaffolding, not a derived result, and no core theorem uses it ([PROGRESS_REPORT](PROGRESS_REPORT.md), note 2026-11-26).

**Ranked black-hole / cosmology conjectures.** Three author proposals are recorded in [THEORY.md §C.8](THEORY.md#c8-three-linked-conjectures-ranked-by-testability), labelled *conjecture: not derived, not tested*. In order of testability they are: a residual undecodable component in final Hawking radiation; a capacity-saturation reading of the singularity, with the Page curve proposed as a corollary; and an "alphabet cascade" reading of the Big Bang and horizons. Only the first could be falsified on its own, and only after a quantitative prediction exists. "Alphabet" has no physical definition yet.

**Type safety:** load \(L\) is a dimensionless **scalar**; structure metric \(G\) is a **metric**. \(L \neq G\).

**Non-claims (summary).** Do not assert any of the following without new work: master equation \(\Leftrightarrow\) continuum GfE; \(L \equiv G\); the residual dual for all \(t\); pointwise Laplacian Newton (withdrawn); \(\alpha\beta = 4\pi G/c^4\) (withdrawn, C17); lattice denoising as empirical gravity; IDEM fully constructing continuum \(L\) or \(G\); \(\sigma(x)\) equal to the gravitational load term. The full list is on the site: [Non-claims](https://cyotee.github.io/computational-entropy/non-claims/).

## Live documentation site

**[https://cyotee.github.io/computational-entropy/](https://cyotee.github.io/computational-entropy/)**

The site hosts Tier 1 ([CORE.md](CORE.md), Papers A and C), Tier 2, and, labelled as Tier 3 conjecture, Paper B and the **full integrated paper** (`papers/06-synthesis/PAPER.md`) as navigable chapters. It is built with MkDocs from an allowlist, not a dump of drafts or agent notes.

## Quick map (repository)

| Role | Path |
|------|------|
| **Tier 1:** core definition, theorems, new vs standard | [`CORE.md`](CORE.md) |
| **Tier 2:** instruction persistence (research avenue) | [`TIER2_INSTRUCTION_PERSISTENCE.md`](TIER2_INSTRUCTION_PERSISTENCE.md) |
| Core papers | [`papers/01-foundations/PAPER_A_computational_entropy.md`](papers/01-foundations/PAPER_A_computational_entropy.md) · [`papers/02-computational-models/PAPER_C_decay_algebra.md`](papers/02-computational-models/PAPER_C_decay_algebra.md) |
| Canonical \(H_c\) | [`foundations/computational-entropy/definition.md`](foundations/computational-entropy/definition.md) |
| Bridge architecture (core → conjecture) | [`THEORY.md`](THEORY.md) |
| *Tier 3 (conjecture):* integrated paper | [`papers/06-synthesis/PAPER.md`](papers/06-synthesis/PAPER.md) |
| *Tier 3 (conjecture):* \(\Phi_g\), load, master equation | [`emergent-gravity/master-equation.md`](emergent-gravity/master-equation.md) |
| Frozen claims / non-claims | [`synthesis/CURRENT_CLAIMS.md`](synthesis/CURRENT_CLAIMS.md) |
| Program conclusions | [`synthesis/PROGRAM_CONCLUSIONS.md`](synthesis/PROGRAM_CONCLUSIONS.md) |
| Final freeze report | [`papers/06-synthesis/FINAL.md`](papers/06-synthesis/FINAL.md) |
| Session bootstrap | [`PROGRESS_REPORT.md`](PROGRESS_REPORT.md) |
| Site plan | [`GITHUB_PAGES_PLAN.md`](GITHUB_PAGES_PLAN.md) |

## Local site preview

```bash
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/python scripts/sync_site_docs.py
.venv/bin/python -m mkdocs serve
```

Or run `bash scripts/build_site.sh`, then open `site/index.html`.

## License

See [LICENSE.md](LICENSE.md).
