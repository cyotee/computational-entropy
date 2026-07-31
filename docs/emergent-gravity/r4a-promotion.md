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

**Branch (b) is physically motivated by Landauer (Paper A):** producing entropy costs energy, drawn from matter, so \(Q>0\) (matter → computational sector). This is a standard *interacting dark energy* structure — and the coupling is the Landauer power of cosmological entropy production. So the classical core (Landauer-exact export) supplies the promotion's coupling.

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
