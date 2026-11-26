# Glossary

**Purpose**: Shared notation and term correspondences between classical computational models and emergent gravity concepts.

## Lead-document terms (three-tier restructure, 2026-11-26)

Terms used by README, THEORY, CORE and the Tier 2 note. They are consistent with `synthesis/CURRENT_CLAIMS.md` (export \(H(X\mid Y)\), single-shot slot \(L_S\), non-claims §3).

- **Boltzmann–Shannon unification**: the programme's driving *intent*, a single notion of entropy that reads both as Shannon uncertainty and as Boltzmann's \(k_B\ln W\) count of compatible microstates. It is a research motivation, **not** a result. The only in-repo contact is the formal split \(\log_2 N = H(Y)+\sum_y p_Y(y)\log_2|f^{-1}(y)|\) for uniform inputs and deterministic maps (CORE §2.3) and the external Landauer theorem.
- **Channel-level entropy**: entropy defined on a channel's action on its input distribution, rather than on a static distribution. Concretely it is the pair \(\big(H_c(f;p_X),\,H(X\mid Y)\big)\) for a channel \(p(y\mid x)\) acting on \(X\sim p_X\), linked by \(H(X)-H(Y)=H(X\mid Y)-H(Y\mid X)\) (Paper A Thm 1). Both entries are standard Shannon functionals of the joint law (CORE §5).
- **Export \(H(X\mid Y)\)**: the input distinguishability discarded by the channel. It equals the visible entropy drop \(H(X)-H(Y)\) only for deterministic maps; for stochastic channels the drop is export minus noise \(H(Y\mid X)\). The ledger name is the single-shot slot \(L_S\). The Landauer-coincident bit count holds for deterministic maps (Paper A Thm 2).
- **Stage-wise export ledger**: the convention that charges each pipeline stage \(H(\text{declared inputs}\mid\text{stage output})\) and sums the charges. Its path-dependence (Paper A Thm 3, 1-bit AND witness) is a property of the convention, **not** a heat difference.
- **Informational equivalence**: \(f\) and \(g\) are informationally equivalent on \(p_X\) iff they induce the same output law \(p_Y\) (for channels, the same output state). Equal law implies equal \(H_c\), but **not conversely**: \(\min(U_1,U_2)\) has the same differential entropy and the same variance \(1/18\) as \(\max(U_1,U_2)\), but a different density, mean and tail. See CORE P1 and pitfall 1 in `AGENTS.md`.
- **Tier 1 / Tier 2 / Tier 3 (labels)**: **Tier 1** (primary result) is computational entropy as a proposed mathematical object (CORE.md; Papers A and C). **Tier 2** (secondary result, no gravity) is instruction persistence on a finite substrate (`TIER2_INSTRUCTION_PERSISTENCE.md`). Tiers 1–2 are backed by in-repo derivations or computations, with open problems labelled. **Tier 3 = Conjecture** marks material published as open conjecture resting on the core result, not as a supported claim: the gravitational programme (Paper B, load \(L\), \(\alpha L=-\Phi/c^2\) with \(\alpha\beta=4\pi G/c^4\) withdrawn per C17, R4a, Path J/M) and the quantum-channel / von Neumann layer (AI-proposed scaffolding, not derived).

## Core Terms

### Classical / Lambda Side
- **Computational Entropy (H_c)**: Entropy of the induced output distribution of a function/map. Depends only on the statistical pattern of outputs, not internal mechanics.
- **IDEM Function**: Expanded identity function that pairs output with metadata (arity, result dim, decay vector, d_f).
- **Decay Vector**: Component of IDEM metadata indicating which inputs are (ir)recoverable from the output.
- **d_f** (legacy, Bayesian): function unidentifiability \(d_f = 1-P_{\max}\in[0,1]\) of a posterior over candidate functions. Under a uniform prior conditioned on the output law it equals \(1-2^{-d_f^{\#}}\); see \(d_f^{\#}\) below.
- **\(d_f^{\#}\)** (log-cardinality, Tier 2): \(d_f^{\#} := \log_2\lvert[f]\rvert\), where \([f]\) is the class of maps with the same output law as \(f\). For uniform input on \(N\) points, \(\lvert[f]\rvert = N!/\prod_y W_y!\). It is read as the substrate's obligation to preserve reconstructability, not as observer ignorance (that reading is a hypothesis). Exact composition: \(d_f^{\#} = d_{g\circ f}^{\#} + R(g\mid f)\). See `TIER2_INSTRUCTION_PERSISTENCE.md`.
- **Infinite Reduction Paths**: Used to model underivability and preserve entropy for hidden variables.

### Gravity / Master Equation Side
- **Φ_g (Gravitational Channel)**: CPTP map acting on local density operators ρ.
- **S_c**: Computational entropy of the channel output (von Neumann entropy of Φ_g(ρ)).
- **L(ρ, g)**: Computational load scalar with three terms (energy density, entropy production rate, holographic boundary).
- **Master Equation**: dρ/dt = [1 / (1 + α L)] ℒ_g[ρ ; g_μν(ρ)]
- **Proper Time Reparameterization**: dτ = dt / (1 + α L)

## Cross-Mappings (to be expanded in THEORY.md)
- Output distribution entropy → S_c
- Information loss via overwriting → decay vector flips + exported entropy to screen
- Term complexity / reduction cost → contributions to load L
- etc.

## Notation Conventions
- Use H_c for classical computational entropy (Tag A when unambiguous)
- Use S_c for the quantum / gravity channel case
- Prefer superscript tags on dual / game / discrete objects (see below)

---

## Entropy object tags (M10)

Distinct functionals — **do not** silently identify. Full map: [synthesis/m10-sc-vs-toy-hc.md](synthesis/m10-sc-vs-toy-hc.md).

| Tag | Symbol | Meaning |
|-----|--------|---------|
| **A** | \(H_c(f;p_X)\) | Classical **map** output Shannon / differential entropy |
| **B** | \(S_c(\Phi;\rho)\) | Von Neumann entropy of **channel** output \(\Phi(\rho)\) |
| **C** | \(H_c^{\mathrm{toy}}\) | Dual-toy residual + edge entropy (ACD-EW scorecards) |
| **D** | \(H_c^{\mathrm{game}}\) | Predictive game Shannon \(H(Y_k\mid\mathcal{F}_{k-1})\) |
| **E** | \(H_c^{\mathrm{disc}}\) | Finite map / IDEM / M11 ledger \(H(Y)\) |

**House style:** bare \(H_c\) only for Tag A when unambiguous; theory claims mixing layers must tag.  
**Non-identity:** \(H_c^{\mathrm{toy}}\not\equiv S_c\); \(H_c^{\mathrm{disc}}\not\equiv S_c\); \(H_c\not\equiv S_{\mathrm{GfE}}\).

---

## Load vs discrete load vs metric \(G\)

| Symbol | Type | Role |
|--------|------|------|
| \(L\) / \(L(\rho,g)\) | **Dimensionless scalar** | Continuum computational **load** (demand; clocks \(d\tau\)) |
| \(L^{\mathrm{disc}}\) | Scalar (ledger) | M11 three-slot discrete proxies \(L_E^{\mathrm{disc}},L_S^{\mathrm{disc}},L_B^{\mathrm{disc}}\) |
| \(G\) | **Metric** (or edgewise cousin) | Structure-/matter-induced metric (GfE / ACD-EW); **not** Newton’s \(G\) in load formulas unless context is clear |

**Type safety (locked):** \(L\neq G\); \(L^{\mathrm{disc}}\neq L(\rho,g)\); continuum limit of dual \(G_i\) is not a limit of \(L_{\mathrm{clock}}\).  
See [emergent-gravity/master-equation.md](emergent-gravity/master-equation.md) · [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md).

---

## Layers W / D / G / M

Claim-bearing results must name their layer. Gate: [synthesis/CLAIM_GATE.md](synthesis/CLAIM_GATE.md).

| Code | Layer | Scope |
|------|-------|--------|
| **W** | Warm-up | Euclidean GfE warm-up (\(G=1+\alpha|\nabla\phi|^2\), PM flow) |
| **D** | Dual | ACD-EW observation dual + T1′ / joint toys (pattern only) |
| **G** | Full GfE | Continuum Bianconi relative-entropy gravity (action, \(\Lambda_G\), G-field) |
| **M** | Master eq | \(\Phi_g\), \(S_c\), continuum \(L\), load clock |

Do **not** transfer W/D theorems to G or M without an explicit labeled map.  
M6 Poisson WEAK PASS is GR-layer contact, **not** W⇔G or M⇔G identity.

---

## Claim hygiene pointers

| Doc | Role |
|-----|------|
| [synthesis/CLAIM_GATE.md](synthesis/CLAIM_GATE.md) | Pre-merge / pre-draft pass–fail checklist |
| [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) | Frozen may-assert (C1–C14) + non-claims §3 |
| [synthesis/NONCLAIMS_FIXTURE.md](synthesis/NONCLAIMS_FIXTURE.md) | Canonical non-claim list + grep hints |
| [synthesis/m10-sc-vs-toy-hc.md](synthesis/m10-sc-vs-toy-hc.md) | Entropy object dictionary |
| [synthesis/m5-warmup-continuum-hygiene.md](synthesis/m5-warmup-continuum-hygiene.md) | Warm-up continuum transfer honesty |
| [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) | Discrete \(H_c\) / \(L^{\mathrm{disc}}\) (not continuum derivation) |
| `simulations/classical/check_claim_hygiene.py` | Lightweight existence + banner + optional soft grep |

---
*Living document. Update as canonical definitions are established in foundations/.*
