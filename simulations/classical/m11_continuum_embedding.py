#!/usr/bin/env python3
"""
O1 step 8 (final rung) — continuum embedding of the export density.

The discrete rungs (m11f/g/h) computed a per-site export density for
*homogeneous* lattices. To reach a continuum density FIELD we let the local
statistics vary in space: bit b_j is Bernoulli(θ(x_j)) with x_j = j/N a smooth
bias profile on [0,1], and the 1D nearest-neighbour AND coupling y_i = b_i∧b_{i+1}.

Homogeneous decay-algebra density at bias θ (m11f generalized):
    a(θ) = h2(θ) − h_Y(θ),   h_Y(θ) = Σ_r ρ_θ(r) h2(θ·π_θ(r)),
computed exactly from the θ-dependent run-length belief chain.

Local-equilibrium (hydrodynamic) hypothesis:
    the coupled per-site density at position x → a(θ(x)) as N → ∞,
i.e. the continuum entropy-production density is the POINTWISE decay-algebra
density σ(x) = a(θ(x)), with corrections O(1/N) = O(h).

Test: propagate the exact belief DISTRIBUTION along the inhomogeneous chain,
read the local per-site density d_i, and measure the interior discrepancy
    Δ(N) = max_i | d_i − a(θ(x_i)) |
over N = 40,80,160,320. If Δ(N) ~ 1/N → local equilibrium holds ⇒ constructive
continuum density σ(x)=a(θ(x)); total continuum export ∫ σ dx. Otherwise the
limit is non-local ⇒ a precise obstruction.

NON-CLAIMS: σ is a classical entropy-production density for a 1D lattice; NOT
the gravitational load term γ|dS_c/dτ|, NOT continuum L(ρ,g), NOT gravity. This
is the discrete→continuum bridge for one classical family only.

Run:
  .venv/bin/python simulations/classical/m11_continuum_embedding.py
"""

from __future__ import annotations

import math
from typing import Callable, Dict, List, Tuple


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


# --- homogeneous decay-algebra density a(θ) (exact, θ-dependent run-length) ---


def h_Y_homog(theta: float, R: int = 1500) -> float:
    pis = [1.0]
    for _ in range(R):
        pr = pis[-1]
        denom = 1 - pr * theta
        pis.append((1 - pr) * theta / denom if denom > 0 else 0.0)
    p1 = [theta * pi for pi in pis]           # P(y=1 | run-length r) = θ·π_r
    w = [1.0]
    for r in range(1, R + 1):
        w.append(w[-1] * (1 - p1[r - 1]))
    S = sum(w)
    rho = [x / S for x in w]
    return sum(rho[r] * h2(p1[r]) for r in range(R + 1))


def a_homog(theta: float) -> float:
    return h2(theta) - h_Y_homog(theta)


# --- inhomogeneous chain: exact belief-DISTRIBUTION propagation ---


def local_densities(thetas: List[float], ndig: int = 9, prune: float = 1e-13) -> List[float]:
    """Per-site coupled density d_i along an inhomogeneous chain.

    Bit b_j ~ Bernoulli(thetas[j]); y_i = b_i ∧ b_{i+1}. d_i uses the fresh
    bit b_{i+1} (bias thetas[i+1]) as the local input rate.
    """
    N = len(thetas)
    # belief distribution over π_i = P(b_i = 1 | past outputs); start π_0 = θ_0
    D: Dict[float, float] = {round(thetas[0], ndig): 1.0}
    ds: List[float] = []
    for i in range(N - 1):
        th = thetas[i + 1]  # fresh bit bias at this step
        # predictive conditional entropy H(Y_i | Y_{<i}) = E_D[h2(π·θ)]
        H_i = 0.0
        for pi, pr in D.items():
            H_i += pr * h2(pi * th)
        ds.append(h2(th) - H_i)  # local input rate − output conditional entropy
        # propagate belief on b_{i+1}
        Dn: Dict[float, float] = {}
        for pi, pr in D.items():
            p_one = pi * th
            if p_one > 0:
                Dn[1.0] = Dn.get(1.0, 0.0) + pr * p_one
            p_zero = 1 - p_one
            if p_zero > 0:
                nb = (1 - pi) * th / (1 - p_one) if (1 - p_one) > 0 else 0.0
                k = round(nb, ndig)
                Dn[k] = Dn.get(k, 0.0) + pr * p_zero
        # prune negligible mass, renormalize
        tot = 0.0
        for k, v in list(Dn.items()):
            if v < prune:
                del Dn[k]
            else:
                tot += v
        D = {k: v / tot for k, v in Dn.items()}
    return ds


def main() -> None:
    print("=" * 78)
    print("O1 step 8 — continuum embedding (local-equilibrium density field)")
    print("Design: this file · m11f/g/h decay algebra · OPEN_AVENUES O1")
    print("=" * 78)

    # sanity: homogeneous density at θ=1/2 recovers the proved constant
    a_half = a_homog(0.5)
    print(f"\n  sanity a(1/2) = {a_half:.6f}  (m11f constant 0.3007568)")
    assert abs(a_half - 0.3007568) < 1e-4

    # smooth bias field on [0,1]
    theta_field: Callable[[float], float] = lambda x: 0.35 + 0.30 * x  # 0.35 → 0.65

    print("\n  continuum density field σ(x) = a(θ(x)) (θ: 0.35→0.65):")
    for x in (0.0, 0.25, 0.5, 0.75, 1.0):
        th = theta_field(x)
        print(f"    x={x:.2f}  θ={th:.3f}  a(θ)={a_homog(th):.5f}")

    print("\n  hydrodynamic convergence  Δ(N)=max_i |d_i − a(θ(x_i))| (interior):")
    print(f"  {'N':>4}  {'Δ(N)':>10}  {'Δ·N':>8}")
    print("  " + "-" * 26)
    L0 = 15  # fixed burn-in (mixing length is O(1) sites)
    deltas: List[Tuple[int, float]] = []
    for N in (40, 80, 160, 320, 640):
        thetas = [theta_field(j / N) for j in range(N)]
        ds = local_densities(thetas)
        # compare d_i to a(θ) at the fresh-bit position (x=(i+1)/N)
        worst = 0.0
        for i in range(L0, len(ds) - 2):
            th = thetas[i + 1]
            worst = max(worst, abs(ds[i] - a_homog(th)))
        deltas.append((N, worst))
        print(f"  {N:4d}  {worst:10.2e}  {worst * N:8.3f}")

    # O(1/N): the halving ratio Δ(N)/Δ(2N) rises monotonically toward 2.
    ratios = [deltas[k][1] / deltas[k + 1][1] for k in range(len(deltas) - 1)]
    print(f"\n  halving ratios Δ(N)/Δ(2N): "
          + ", ".join(f"{r:.2f}" for r in ratios) + "  (→2 ⇒ approaching O(1/N))")
    assert deltas[-1][1] < deltas[0][1] / 4, "discrepancy must shrink clearly with N"
    assert all(b > a - 1e-9 for a, b in zip(ratios, ratios[1:])), \
        "halving ratios should rise monotonically toward the asymptotic rate"
    assert ratios[-1] > 1.8, "should be entering the O(1/N) regime by N=640"

    # total continuum export ∫ σ dx (Simpson on the field)
    M = 2000
    xs = [k / M for k in range(M + 1)]
    vals = [a_homog(theta_field(x)) for x in xs]
    integral = (vals[0] + vals[-1] + 4 * sum(vals[1:-1:2]) + 2 * sum(vals[2:-1:2])) / (3 * M)
    print(f"\n  total continuum export  ∫_0^1 σ(x) dx = {integral:.5f}  bits/(site·length)")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  LOCAL EQUILIBRIUM HOLDS: the discrete coupled export density converges")
    print("  (O(1/N)) to the pointwise decay-algebra density σ(x)=a(θ(x)). The")
    print("  discrete export ledger therefore admits a CONSTRUCTIVE continuum")
    print("  entropy-production density field, computed by the decay algebra, with")
    print("  total ∫ σ dx. This is the discrete→continuum bridge (rung 8).")
    print("\n  Rigor: hydrodynamic/local-equilibrium limit witnessed at O(1/N) for")
    print("  the 1D biased-AND family; a general theorem (all gates/2D) is open.")
    print("\nNON-CLAIMS: σ is a classical density; NOT γ|dS_c/dτ|, NOT continuum L,")
    print("NOT gravity. Bridge for one classical family only.")
    print("=" * 78)


if __name__ == "__main__":
    main()
