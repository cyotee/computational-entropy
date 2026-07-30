# M11i — Continuum embedding of the export density (local equilibrium)

**M-id:** M11i · **Status:** **Hydrodynamic limit witnessed** — 1D biased-AND family
**Date:** 2026-07-30 · **Stance:** Preliminary research; the discrete→continuum bridge is **constructive**, its identification with the gravitational load term is **not** claimed.
**Caps the ladder:** [m11f](m11f-decay-algebra-theorem.md) · [m11g](m11g-decay-algebra-general-w-theorem.md) · [m11h](m11h-decay-algebra-2d.md)
**Witness:** `simulations/classical/m11_continuum_embedding.py`

The discrete rungs computed a per-site export density for *homogeneous* lattices. This rung produces a continuum density **field** by letting the local statistics vary in space and taking a scaling limit — closing the discrete side of O1.

---

## 1. Setup

Bit \(b_j\sim\mathrm{Bernoulli}(\theta(x_j))\), \(x_j=j/N\), for a smooth bias field \(\theta:[0,1]\to(0,1)\); coupling \(Y_i=b_i\wedge b_{i+1}\). The homogeneous decay-algebra density at constant bias \(\theta\) is (m11f generalized to bias)


$$
a(\theta)=h_2(\theta)-h_Y(\theta),\qquad h_Y(\theta)=\sum_r\rho_\theta(r)\,h_2\!\big(\theta\,\pi_\theta(r)\big),
$$


with the \(\theta\)-dependent run-length belief chain \(\pi_\theta(0)=1,\ \pi_\theta(r{+}1)=\frac{(1-\pi_\theta(r))\theta}{1-\pi_\theta(r)\theta}\).

---

## 2. Local-equilibrium (hydrodynamic) result

**Hypothesis.** As \(N\to\infty\), the coupled per-site density \(d_i\) at position \(x_i\) converges to the *pointwise* homogeneous density:


$$
d_i \;\longrightarrow\; \sigma(x):=a(\theta(x)),\qquad \text{with corrections } O(1/N).
$$


**Mechanism.** The belief filter mixes geometrically (mixing length \(O(1)\) sites), so the belief law at site \(i\) equals the homogeneous stationary law at bias \(\theta(x_i)\) up to the bias variation over one mixing length, \(O(\theta'\!\cdot h)=O(1/N)\).

**Witness** (`m11_continuum_embedding.py`, \(\theta(x)=0.35+0.30x\), interior discrepancy \(\Delta(N)=\max_i|d_i-a(\theta(x_i))|\)):

| \(N\) | \(\Delta(N)\) | \(\Delta\!\cdot\!N\) |
|------|---------------|----------------------|
| 40 | \(2.54\times10^{-3}\) | 0.102 |
| 80 | \(1.72\times10^{-3}\) | 0.138 |
| 160 | \(1.00\times10^{-3}\) | 0.161 |
| 320 | \(5.34\times10^{-4}\) | 0.171 |
| 640 | \(2.75\times10^{-4}\) | 0.176 |

Halving ratios \(\Delta(N)/\Delta(2N)=1.48,1.71,1.88,1.95\to 2\), and \(\Delta\!\cdot\!N\) approaches a constant — i.e. \(\Delta(N)=O(1/N)\). Local equilibrium holds.

---

## 3. The continuum density field

The discrete export ledger therefore admits a **constructive continuum entropy-production density**


$$
\boxed{\;\sigma(x)=a(\theta(x))=h_2(\theta(x))-h_Y(\theta(x))\;}
$$


— a *local functional of the field, computed by the decay algebra* — with total continuum export \(\int_0^1\sigma(x)\,dx=0.29937\) for the sample field. Sample profile: \(\sigma=0.446,0.379,0.301,0.220,0.146\) at \(x=0,\tfrac14,\tfrac12,\tfrac34,1\).

This is exactly the O1 target on the **discrete side**: a scaling limit sending the discrete export density to a continuum density, with a stated rate.

---

## 4. What this does and does NOT establish

**Does (constructive):** the discrete export ledger (Paper A) → the decay algebra (m11f/g/h) → a **continuum entropy-production density field** \(\sigma(x)\), via a hydrodynamic/local-equilibrium limit at rate \(O(1/N)\). The full ladder discrete→continuum is built for this family.

**Does NOT (explicit non-claim):** \(\sigma(x)\) is a **classical** entropy-production density for a 1D lattice. It is **not** identified with the gravitational load term \(\gamma\lvert dS_c/d\tau\rvert\), **not** continuum \(L(\rho,g)\), **not** gravity. The map \(\sigma \leftrightarrow\) load term remains the program's **semantic** reformulation bridge (labeled, not constructed). What has changed: the discrete side now terminates in a genuine continuum density rather than a lattice number.

---

## 5. Scope, rigor, non-claims

| Statement | Rigor |
|-----------|-------|
| \(a(\theta)=h_2(\theta)-h_Y(\theta)\) homogeneous density (exact) | **proved** (m11f at bias \(\theta\)) |
| \(d_i\to a(\theta(x_i))\), \(O(1/N)\) local-equilibrium limit | **witnessed** (this family; general theorem open) |
| continuum density \(\sigma(x)=a(\theta(x))\), total \(\int\sigma\) | **constructive** (given the limit) |
| \(\sigma \equiv \gamma\lvert dS_c/d\tau\rvert\) / continuum \(L\) / gravity | **NOT claimed** (semantic bridge only) |

**Open:** a general hydrodynamic **theorem** (all gates, 2D); relating \(\sigma\) to the load term is the reformulation program's remaining semantic step (see [../papers/FALSIFIABILITY_L_vs_GR.md](../papers/FALSIFIABILITY_L_vs_GR.md)).

---

*O1 discrete-side ladder complete: export ledger → decay algebra → continuum density field \(\sigma(x)\). Update [OPEN_AVENUES.md](OPEN_AVENUES.md) / [RESULTS_LEDGER.md](RESULTS_LEDGER.md).*
