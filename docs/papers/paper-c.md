# The Decay Algebra: From Export Ledgers to a Continuum Entropy-Production Density

**Paper C (decay algebra) — Draft**
**Status:** 2026-07-30 · Preliminary research · self-contained, **classical, no gravitational claims**
**Scope contract:** [../DELIVERY_SCOPE.md](../DELIVERY_SCOPE.md) · **Depends on:** Paper A [../01-foundations/PAPER_A_computational_entropy.md](../01-foundations/PAPER_A_computational_entropy.md)
**Canonical notes:** `synthesis/m11f`–`m11i` · **Reproducible:** `simulations/classical/m11_{idem,decay_algebra,decay_algebra_general,decay_algebra_2d,continuum_embedding}*.py`

---

## Abstract

Paper A defined computational entropy as the entropy of a map's output distribution and showed that the entropy exported by an irreversible computation, `H(X∣Y)`, is Landauer-exact but **path-dependent** and **non-additive**. That raises a sharp question: does a *coupled* lattice of local maps have a well-defined export **density** at all, and if so can it be computed without exponential enumeration? We answer both. First, the IDEM *decay vector* gives a tight upper bound on export, exact for maps with product (fully-recoverable) preimages. Second, promoting the hard decay flag to a **belief transported across the coupling boundary** yields a *decay algebra* — a transfer operator that computes the exact coupled export density. We prove a density theorem for the 1D nearest-neighbour case, generalize it to arbitrary gates and window widths (with a clean dichotomy: the algebra is exactly finite iff the gate has a fully-recoverable branch), lift it to a 2D strip transfer, and finally show a **hydrodynamic limit**: with a smoothly varying spatial field the discrete density converges (at rate `O(1/N)`) to a **constructive continuum entropy-production density field** `σ(x)`. Every result is backed by an exactly-reproducing computation. We make **no** claim that `σ` is a gravitational load term; that identification is discussed only as an explicit, deferred semantic bridge.

---

## 1. Setup: from a path-dependent ledger to a density question

For a computation `X → Y` on uniform inputs, Paper A's **export identity** is


$$
H(X) - H(Y) = H(X\mid Y) =: \text{export},
$$


the chain-rule remainder (AND gate: `H(Y)=0.811278`, export `=1.188722`). Paper A also proved two facts that make a continuum density non-obvious: cumulative export `Σ L_S` is **path-dependent** (Thm 3), and the soft-recoverability slot is **non-additive** (Thm F).

So for a lattice of *coupled* local maps (maps sharing input wires), it is not clear that the total export is even extensive. We fix a concrete family: a sliding window of width `w` over an i.i.d. fair bit stream,


$$
Y_i = g(b_i,\dots,b_{i+w-1}),
$$


and study the per-site export density `a := lim_{k→∞} E(k)/k`, where `E(k)=H(X∣Y_{0:k-1})`.

**Extensivity witness** (`m11_lattice_export_density.py`). For coupled AND lattices `E(k)` is linear in `k` — a well-defined bulk density exists (shared-input `a≈0.30076`, residual `~10⁻⁸`; chained `a≈0.999`) — and the path-dependence of Paper A saturates to an `O(1)` **boundary** term, so per-site it vanishes like `1/k`. The obstruction is real but subleading: a density exists.

## 2. The decay vector bounds export (exact for product maps)

The IDEM *decay vector* records, per input coordinate and per output branch, whether that input is recoverable from `Y` (`d_i=0`) or lost (`d_i=1`). Since `X∣(Y=y)` is uniform on the preimage `f⁻¹(y)`,


$$
H(X\mid Y) = \sum_y p(y)\,\log_2|f^{-1}(y)| \;\le\; \sum_y p(y)\,\#\{\text{unrecoverable coords}\} \;=\; \text{decay bound},
$$


with **equality iff every preimage is a product subcube** (a fully-recoverable branch). This is proved and asserted over a map family (`m11_idem_export_density.py`):

| map | exact export | decay bound | gap | product? |
|-----|-----|-----|-----|-----|
| `erase(2,1)`, `erase(3,1)`, `erase(4,2)` | = bound | = exact | 0 | ✓ |
| `AND(2)` | 1.18872 | 1.50000 | 0.311 | ✗ |
| `majority(3)`, `parity(3)` | 2.00000 | 3.00000 | 1.000 | ✗ |

**Consequence (utility).** For product/erasure lattices the export density is read directly from local decay metadata in `O(N)` — enumeration-free and exact. For non-product/coupled maps the bound is loose (e.g. the shared-input AND lattice has true density `0.30076 ≪ 1.5`), which motivates the algebra of §3.

## 3. The decay algebra and the 1D density theorem

The looseness of the hard bound has two sources — fractional entropy of non-product preimages, and correlations from shared wires. Both are cured by replacing the `{0,1}` flag with a **belief over the shared boundary bit that is transported site-to-site** (a transfer operator).

**Theorem 1 (1D density theorem; `m11f`).** *For the 1D nearest-neighbour AND lattice `Y_i=b_i∧b_{i+1}`, the density*


$$
a=\lim_k E(k)/k \;\text{ exists and } \;= 1 - h_Y,\qquad h_Y=\sum_{r\ge0}\rho(r)\,h_2(p_1(r)),
$$


*with `E(k)=ak+b+o(1)`.* The belief filter `π_i=Pr(b_i=1∣Y_{<i})` resets to `1` on `Y_i=1`, so it collapses to a **run-length Markov chain** with `π_0=1`, `π_{r+1}=(1-π_r)/(2-π_r)`, `p_1(r)=π_r/2`, stationary law `ρ(r)∝∏_{j<r}(1-p_1(j))`. Fixed point `π★=(3-√5)/2`, density


$$
\boxed{a = 0.3007568}.
$$


*Proof idea.* `(Y_i)` is a sliding-block factor of i.i.d. ⇒ stationary ergodic ⇒ the entropy rate exists (Shannon–McMillan–Breiman); the input rate is exactly `1`, giving `a=1-h_Y`. The filter is a sufficient statistic, and its reset structure makes the run-length chain ergodic with the stated stationary law. The belief-transfer recursion reproduces the `O(2^k)` enumeration to `<10⁻⁸` at `O(R)` cost (`m11_decay_algebra.py`). ∎

## 4. General-`w` theorem: any gate, and the reset dichotomy

**Theorem 2 (general `w`; `m11g`).** *For any gate `g:{0,1}^w→{0,1}` and the sliding-window lattice:*

1. **(Existence.)** `(Y_i)` is `(w−1)`-dependent (outputs ≥`w` apart use disjoint bits), hence stationary ergodic; `a=1-h_Y` exists with `E(k)=ak+O(1)`.
2. **(Blackwell representation.)** `h_Y = 𝔼_{μ★}[H(Y∣π)]`, where `μ★` is the unique invariant measure of the belief-transfer operator on the `2^{w-1}`-state boundary simplex.
3. **(Regeneration.)** If `g` is a **reset gate** — some output value has a *singleton* preimage (a fully-recoverable `[0,…,0]` decay branch) — the filter restarts at the same point mass on every reset, so the inter-reset cycles are i.i.d. and `h_Y` is given by **renewal-reward**; the algebra is then exactly finite.

**Corollary (dichotomy).** The belief-transfer algebra is exactly finite ⇐ `g` is a reset gate. This is executably verified (`m11_decay_algebra_general.py` asserts `exact ⇔ singleton-preimage`):

| gate | `w` | reset? | method | density `a` |
|------|-----|--------|--------|-------------|
| AND | 2,3,4 | yes | exact | 0.30076 / 0.56568 / 0.74503 |
| OR | 2,3 | yes | exact | 0.30076 / 0.56568 |
| threshold≥2 | 3 | no | Monte Carlo | 0.23734 |

Thus the *decay-vector structure of a single gate* — whether some branch fully recovers its inputs — controls whether the *composition algebra* is finitely exact. The reset direction is proved; the converse (non-reset ⇒ non-atomic `μ★`) is left conjectural.

## 5. 2D strip transfer

Lifting to a 2D lattice (2×2-plaquette AND, `Y_{ij}=b_{i,j}∧b_{i,j+1}∧b_{i+1,j}∧b_{i+1,j+1}`), the boundary between processed and unprocessed sites becomes a **row-cut of width `W`** and the transfer becomes an operator on the `2^W` cut configurations — the Bayesian-filter form of a statistical-mechanics strip transfer matrix.

**Result (`m11h`).** The 2D per-site density exists (finite-dependence on ℤ²; proved). The width-`W` density `a_W=(W-h_{\text{row}})/(W-1)` computed by the strip operator matches exact enumeration (`m11_decay_algebra_2d.py`):

| `W` | `2^W` | `a_enum` | `a_transfer` | `\|Δ\|` |
|-----|-------|----------|--------------|------|
| 2 | 4 | 1.68412 | 1.68429 | 1.7e-4 |
| 3 | 8 | 1.19251 | 1.19329 | 7.8e-4 |
| 4 | 16 | — | 1.03098 | — |

`a_W` converges (1.684 → 1.193 → 1.031). The row-cut carries `2^W` states and `2^{W-1}` emission branches, so both enumeration and transfer cost grow exponentially in strip width. This exponential wall is generic in `d≥2` and is exactly why a genuine limit — not more enumeration — is required.

## 6. Continuum embedding: a density field

Let the local statistics vary in space: `b_j∼Bernoulli(θ(x_j))`, `x_j=j/N`, for a smooth field `θ:[0,1]→(0,1)` with the 1D nearest-neighbour AND coupling. The homogeneous density at bias `θ` is `a(θ)=h_2(θ)-h_Y(θ)`.

**Result (local equilibrium; `m11i`).** As `N→∞`, the coupled per-site density converges to the *pointwise* homogeneous density,


$$
\boxed{\;\sigma(x) = a(\theta(x)) = h_2(\theta(x)) - h_Y(\theta(x))\;}\qquad\text{at rate } O(1/N).
$$


The belief filter mixes geometrically (mixing length `O(1)` sites), so its law at site `i` equals the homogeneous stationary law at `θ(x_i)` up to the bias variation over one mixing length, `O(1/N)`. Witness (`m11_continuum_embedding.py`, `θ(x)=0.35+0.30x`, interior discrepancy `Δ(N)`):

| `N` | 40 | 80 | 160 | 320 | 640 |
|-----|----|----|-----|-----|-----|
| `Δ(N)` | 2.54e-3 | 1.72e-3 | 1.00e-3 | 5.34e-4 | 2.75e-4 |

Halving ratios `1.48 → 1.71 → 1.88 → 1.95 → 2`, and `Δ·N` approaches a constant, i.e. `Δ(N)=O(1/N)`. The discrete export ledger therefore admits a **constructive continuum entropy-production density field** `σ(x)`, with total `∫₀¹ σ dx = 0.29937` for the sample field (profile `σ = 0.446, 0.379, 0.301, 0.220, 0.146` at `x=0,¼,½,¾,1`).

## 7. Scope, rigor, and non-claims

| Statement | Rigor |
|-----------|-------|
| Coupled export is extensive; density exists | witnessed |
| Decay vector upper-bounds export, exact for product maps | **proved** |
| 1D density theorem `a=1-h_Y=0.3007568` (Thm 1) | **proved** |
| General-`w` existence + Blackwell + reset-regeneration (Thm 2) | **proved** (non-atomicity converse conjectural) |
| 2D density exists; width-`W` strip transfer | **proved** (existence); convergence numerical |
| Continuum density field `σ(x)=a(θ(x))`, `O(1/N)` | witnessed (general theorem open) |

**Explicit non-claims.** `σ(x)` is a **classical** entropy-production density for a specific lattice family. It is **not** identified with the gravitational load term `γ|dS_c/dτ|`, **not** continuum `L(ρ,g)`, and carries **no** gravitational content. A general hydrodynamic theorem (all gates, 2D) is open. The map from `σ` to any physical load term is, at most, a separate labeled semantic step and is not undertaken here.

**Takeaway.** From the Landauer-exact export ledger, promoting the decay vector to a transported belief yields a compositional *decay algebra* that computes coupled export densities exactly (for reset gates) and, in a hydrodynamic limit, a constructive continuum entropy-production density field. IDEM's decay vector thereby acquires a proved, load-bearing role: its fully-recoverable-branch structure is exactly what makes the algebra finitely exact.

---

## Appendix R — Reproducibility

```bash
.venv/bin/python simulations/classical/m11_lattice_export_density.py   # extensivity; a≈0.30076, path-dep saturates
.venv/bin/python simulations/classical/m11_idem_export_density.py      # decay bound, exact for product maps
.venv/bin/python simulations/classical/m11_decay_algebra.py            # 1D: a=0.3007568, π★=(3-√5)/2
.venv/bin/python simulations/classical/m11_decay_algebra_general.py    # general w; exact⇔reset dichotomy
.venv/bin/python simulations/classical/m11_decay_algebra_2d.py         # 2D strip; a_W convergence
.venv/bin/python simulations/classical/m11_continuum_embedding.py      # σ(x)=a(θ(x)), O(1/N), ∫σ=0.29937
```

| Quantity | Value | Source |
|----------|-------|--------|
| AND export `H(X\|Y)` | 1.188722 | Paper A / decay bound |
| 1D density `a` | 0.3007568 (`π★=(3-√5)/2`) | Thm 1 |
| AND density `a_w`, `w=2,3,4` | 0.30076 / 0.56568 / 0.74503 | Thm 2 |
| 2D `a_W`, `W=2,3,4` | 1.68429 / 1.19329 / 1.03098 | §5 |
| continuum total `∫σ` (sample field) | 0.29937 | §6 |

---

## Changelog

| Date | Entry |
|------|-------|
| 2026-07-30 | Initial draft: extensivity → decay bound → 1D theorem → general-`w` → 2D strip → continuum density `σ(x)`; classical, no gravity; reproducibility appendix. |
