# Glossary

**Purpose**: Shared notation and term correspondences between classical computational models and emergent gravity concepts.

## Core Terms

### Classical / Lambda Side
- **Computational Entropy (H_c)**: Entropy of the induced output distribution of a function/map. Depends only on the statistical pattern of outputs, not internal mechanics.
- **IDEM Function**: Expanded identity function that pairs output with metadata (arity, result dim, decay vector, d_f).
- **Decay Vector**: Component of IDEM metadata indicating which inputs are (ir)recoverable from the output.
- **d_f**: Probability or measure of function unidentifiability.
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
