#!/usr/bin/env python3
"""
R4a promotion — put the entropy-production content INTO the field equations.

Context: the load-dimensional no-go (emergent-gravity/load-dimensional-analysis.md)
showed the load cannot be an independent clock — a departure from GR requires
promoting load terms into the field equations (metric-level content). This
script runs that promotion in a cosmology, where it is tractable and testable.

Promotion (minimal, generally covariant):
  G_mu_nu = kappa ( T^matter_mu_nu + T^S_mu_nu ),
where T^S is a perfect-fluid "computational sector" of energy density rho_S
built from entropy production. Take the vacuum-like intrinsic EoS w_S = -1.

Bianchi fork (the decisive, rigorous test). ∇^mu G_mu_nu = 0 forces
∇^mu(T^matter + T^S) = 0. With w_S=-1, ∇^mu T^S_mu_nu = -∂_nu(rho_S c^2). So:
  (a) if matter is separately conserved  => rho_S = const  => just a
      cosmological constant Λ. NO new physics (reproduces ΛCDM's Λ).
  (b) if rho_S tracks entropy production (dynamical) => matter is NOT separately
      conserved: energy Q flows between matter and the computational sector.
Branch (b) is physically motivated by Landauer (Paper A): producing entropy
costs energy, drawn from matter => Q>0 (matter -> computational). This is a
standard interacting-dark-energy structure.

FRW model (flat, dust matter + w_S=-1 computational sector, coupling Q=xi*H*rho_m):
  rho_m' + 3 H rho_m = -Q,   rho_S' = +Q,   H^2 = (8πG/3) (rho_m + rho_S).
Analytic:
  rho_m(a) = rho_m0 a^{-(3+xi)}
  rho_S(a) = rho_S0 + xi rho_m0/(3+xi) (1 - a^{-(3+xi)})
  effective DE EoS:  w_eff(a) = -1 - xi rho_m(a)/(3 rho_S(a))   (phantom, <-1, for xi>0)

Checks: xi=0 recovers ΛCDM exactly (w_eff=-1). xi>0 gives a distinct H(z) and a
phantom w_eff; current data (|w0+1|<~0.05) already BOUNDS xi.

NON-CLAIMS: one minimal promotion (perfect fluid, w_S=-1, Q=xi H rho_m, sign
from Landauer) — a CANDIDATE hypothesis, not a unique or validated theory. The
coupling magnitude xi is free (the load-constant calibration is still unfixed);
only the SIGN/FORM is determined. No claim this explains dark energy.

Run:
  .venv/bin/python simulations/gravity-toy/r4a_frw_promotion.py
"""

from __future__ import annotations


OM0 = 0.30   # matter density parameter today
OS0 = 0.70   # computational-sector (dark-energy-like) density parameter today
W0_TOL = 0.05  # representative observational tolerance on w0 (|w0+1| < 0.05)


def rho_m(a: float, xi: float) -> float:
    return OM0 * a ** (-(3.0 + xi))


def rho_S(a: float, xi: float) -> float:
    if xi == 0.0:
        return OS0
    return OS0 + xi * OM0 / (3.0 + xi) * (1.0 - a ** (-(3.0 + xi)))


def E2(a: float, xi: float) -> float:
    """(H/H0)^2 = rho_m + rho_S in units of rho_crit,0."""
    return rho_m(a, xi) + rho_S(a, xi)


def w_eff(a: float, xi: float) -> float:
    """Effective equation of state of the computational (dark) sector."""
    rs = rho_S(a, xi)
    if rs <= 0:
        return float("nan")
    return -1.0 - xi * rho_m(a, xi) / (3.0 * rs)


def w0(xi: float) -> float:
    return -1.0 - xi * OM0 / (3.0 * OS0)


def min_valid_a(xi: float) -> float:
    """Smallest a with rho_S(a) >= 0 (consistency of the toy back in time)."""
    if xi == 0.0:
        return 0.0
    # rho_S(a)=0  =>  a^{-(3+xi)} = 1 + OS0 (3+xi)/(xi OM0)
    val = 1.0 + OS0 * (3.0 + xi) / (xi * OM0)
    return val ** (-1.0 / (3.0 + xi))


def ztable(xi: float, zs):
    print(f"\n  xi = {xi}:   w0 = {w0(xi):+.4f},  rho_S>=0 back to z_max = "
          f"{1.0/min_valid_a(xi)-1.0:.1f}" if xi else f"\n  xi = {xi} (ΛCDM):  w0 = {w0(xi):+.4f}")
    print(f"  {'z':>5} {'E(z)=H/H0':>10} {'w_eff':>9} {'rho_S/rho_S0':>13}")
    for z in zs:
        a = 1.0 / (1.0 + z)
        e = E2(a, xi) ** 0.5
        print(f"  {z:5.2f} {e:10.4f} {w_eff(a, xi):9.4f} {rho_S(a, xi)/OS0:13.4f}")


def main():
    print("=" * 74)
    print("R4a promotion — entropy production sourcing the field equations (FRW)")
    print("Design: emergent-gravity/load-dimensional-analysis.md (no-go) -> R4a")
    print("=" * 74)

    print("\nBianchi fork (rigorous): promoting a w_S=-1 computational sector forces")
    print("  (a) matter conserved  => rho_S=const => plain Λ (no new physics), OR")
    print("  (b) energy exchange Q (matter<->computation) => dynamical (this model).")
    print("  Branch (b) sign is fixed by Landauer (Paper A): Q>0, matter->computation.")

    zs = [0.0, 0.5, 1.0, 2.0]
    ztable(0.0, zs)      # ΛCDM baseline
    ztable(0.3, zs)      # promoted, moderate coupling

    # GR limit: xi -> 0 recovers ΛCDM
    for a in (0.2, 0.5, 1.0):
        assert abs(E2(a, 0.0) - (OM0 * a**-3 + OS0)) < 1e-12, "xi=0 must be ΛCDM E^2"
        assert abs(w_eff(a, 0.0) + 1.0) < 1e-12, "xi=0 must give w_eff=-1"

    # departure: xi>0 gives phantom w_eff and a different expansion
    assert w_eff(1.0, 0.3) < -1.0, "xi>0 must give phantom effective DE (w<-1)"
    assert abs(E2(0.5, 0.3)**0.5 - E2(0.5, 0.0)**0.5) > 1e-3, "H(z) must differ from ΛCDM"

    # observational bound on the (free) coupling
    xi_bound = None
    xi = 0.0
    while xi < 5.0:
        if abs(w0(xi) + 1.0) > W0_TOL:
            xi_bound = xi
            break
        xi += 0.001
    print("\n" + "=" * 74)
    print("OBSERVATIONAL CONTACT")
    print("=" * 74)
    print(f"  Effective DE is PHANTOM: w0 = -1 - xi*Om/(3*OS) = -1 - {OM0/(3*OS0):.3f}*xi.")
    print(f"  Current bound |w0+1| < {W0_TOL}:  xi < {xi_bound:.2f}  (already constrains the coupling).")

    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    print("  The R4a promotion is CONSISTENT and non-trivial:")
    print("  - passes the Bianchi test via a Landauer-motivated matter<->computation")
    print("    energy exchange (branch b); constant-Λ (branch a) is the xi=0 limit;")
    print("  - reduces EXACTLY to ΛCDM / GR as xi -> 0 (GR limit holds);")
    print("  - departs for xi>0 with a DETERMINED signature: phantom dark energy")
    print("    (w_eff<-1), sign fixed by Landauer; magnitude xi free but already")
    print("    observationally BOUNDED (xi < ~0.35).")
    print()
    print("  ==> Promotion yields a CANDIDATE HYPOTHESIS with mathematical evidence:")
    print("      a testable, GR-reducing, interacting-dark-energy model whose free")
    print("      coupling is bounded by data. It is NOT invalidated, and NOT yet a")
    print("      validated theory (magnitude unfixed; one of several possible")
    print("      promotions). A departure from GR now has a concrete, falsifiable form.")
    print()
    print("NON-CLAIMS: minimal/one promotion; magnitude free; not a claim to explain")
    print("dark energy; sign from Landauer modeling. See emergent-gravity/r4a-promotion.md.")
    print("=" * 74)


if __name__ == "__main__":
    main()
