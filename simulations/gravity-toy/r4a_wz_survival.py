#!/usr/bin/env python3
"""
w(z) survival test — does the R4a candidate survive current dark-energy data?

Context: R4a (emergent-gravity/r4a-promotion.md) predicts a Landauer-coupled
interacting dark sector with a *determined shape* but a *free coupling* xi.
Before attempting the hard first-principles coupling, we test the shape against
data: map the model onto the standard CPL plane (w0, wa) and compare to
published constraints.

Our model (Landauer sign, xi>0):
  rho_m = Om0 a^{-(3+xi)},  rho_S = OS0 + xi Om0/(3+xi) (1 - a^{-(3+xi)})
  w_eff(a) = -1 - xi rho_m/(3 rho_S)  (PHANTOM, w<=-1, sign fixed by Landauer)
  CPL fit:  w0 = w_eff(1),  wa = -dw_eff/da|_{a=1}

Key structural fact: the Landauer sign forces  w0 <= -1  (phantom) and wa < 0.
The model can NEVER reach w0 > -1. So if data prefers w0 > -1, the natural
(Landauer) R4a is disfavored regardless of coupling.

DATA (representative, approximate — DESI DR1 2024 w0waCDM; NOT settled, ~2-3sigma,
sample-dependent). Central values quoted from the 2024 DESI BAO papers; treat as
illustrative, verify against primary sources before any strong claim:
  DESI+CMB+PantheonPlus : w0 ~ -0.83, wa ~ -0.75   (sigma_w0 ~ 0.06)
  DESI+CMB+DESY5        : w0 ~ -0.73, wa ~ -1.05    (sigma_w0 ~ 0.07)
  DESI+CMB+Union3       : w0 ~ -0.65, wa ~ -1.27    (sigma_w0 ~ 0.10)
All have w0 > -1 (the QUINTESSENCE side), opposite our phantom prediction.

NON-CLAIMS: the DESI dynamical-DE hint is unsettled; LambdaCDM remains viable;
our model is consistent with LambdaCDM in the xi->0 limit. This tests the SHAPE
of a candidate, not a validated theory. No claim to measure dark energy.

Run:
  .venv/bin/python simulations/gravity-toy/r4a_wz_survival.py
"""

from __future__ import annotations

OM0, OS0 = 0.30, 0.70


def rho_m(a, xi):
    return OM0 * a ** (-(3.0 + xi))


def rho_S(a, xi):
    if xi == 0.0:
        return OS0
    return OS0 + xi * OM0 / (3.0 + xi) * (1.0 - a ** (-(3.0 + xi)))


def w_eff(a, xi):
    rs = rho_S(a, xi)
    return float("nan") if rs <= 0 else -1.0 - xi * rho_m(a, xi) / (3.0 * rs)


def cpl(xi, h=1e-5):
    """(w0, wa) with wa = -dw/da at a=1 (finite difference)."""
    w0 = w_eff(1.0, xi)
    dwda = (w_eff(1.0 + h, xi) - w_eff(1.0 - h, xi)) / (2 * h)
    return w0, -dwda


# representative DESI DR1 2024 w0waCDM points (approx; see docstring caveat)
DESI = [
    ("DESI+CMB+PantheonPlus", -0.83, 0.06, -0.75, 0.29),
    ("DESI+CMB+DESY5",        -0.73, 0.07, -1.05, 0.31),
    ("DESI+CMB+Union3",       -0.65, 0.10, -1.27, 0.40),
]


def main():
    print("=" * 76)
    print("R4a w(z) survival — model (w0,wa) line vs current dark-energy data")
    print("Design: emergent-gravity/r4a-promotion.md")
    print("=" * 76)

    print("\nModel line in the CPL plane (Landauer sign, xi>=0):")
    print(f"  {'xi':>5} {'w0':>9} {'wa':>9}")
    for xi in (0.0, 0.05, 0.1, 0.2, 0.35, 0.5):
        w0, wa = cpl(xi)
        print(f"  {xi:5.2f} {w0:9.4f} {wa:9.4f}")
    print("  => the whole line has w0 <= -1 (phantom) and wa <= 0; starts at")
    print("     LambdaCDM (-1, 0) and moves into the w0<-1, wa<0 quadrant.")

    print("\nData (representative DESI DR1 2024 w0waCDM; unsettled ~2-3sigma):")
    print(f"  {'combination':>22} {'w0':>8} {'wa':>8}  {'w0 vs -1':>12}")
    for name, w0d, sw0, wad, swa in DESI:
        n_sigma = (w0d - (-1.0)) / sw0   # how far the data's w0 sits from -1
        side = "quintessence" if w0d > -1 else "phantom"
        print(f"  {name:>22} {w0d:8.3f} {wad:8.3f}  {n_sigma:+5.1f}s ({side})")

    # Can our model (w0<=-1) reach any DESI central region?
    reach = any(w0d <= -1.0 for _, w0d, _, _, _ in DESI)
    # how disfavored is the phantom boundary (best our model can do beyond LCDM)?
    worst = max((abs(w0d - (-1.0)) / sw0) for _, w0d, sw0, _, _ in DESI)

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    print(f"  Every DESI central value has w0 > -1 (quintessence side); our model")
    print(f"  is confined to w0 <= -1 (phantom). The model CANNOT reach the data's")
    print(f"  preferred direction — the data sits {worst:.1f}-{max((w0d+1)/sw0 for _,w0d,sw0,_,_ in DESI):.1f}+ sigma away on the")
    print(f"  OPPOSITE side of LambdaCDM from where our prediction points.")
    assert not reach, "sanity: no DESI central is on the phantom side"
    print()
    print("  ==> The natural (Landauer-sign) R4a prediction is DISFAVORED by the")
    print("      current data hint. The model survives only in its xi->0 limit,")
    print("      i.e. LambdaCDM — the 'no new physics' branch. Its distinctive")
    print("      phantom signature points the WRONG way.")
    print()
    print("  Nuance (honest): (i) the DESI dynamical-DE preference is ~2-3sigma,")
    print("  sample-dependent, and NOT settled — LambdaCDM is still viable, and our")
    print("  model is fine at xi->0. (ii) The OPPOSITE energy-flow sign (xi<0,")
    print("  dark->matter) would give quintessence (w0>-1) and could MATCH the DESI")
    print("  hint — but that reinterprets the Landauer direction. So the data, if it")
    print("  holds, tells us which way the computational energy exchange must go.")
    print()
    print("  Recommendation: do NOT invest in the first-principles coupling for the")
    print("  phantom branch now — it is the disfavored direction. Either wait for")
    print("  DESI DR2 / firmer data, or study the opposite-sign (quintessence) branch")
    print("  as the physically motivated alternative if data solidifies at w0>-1.")
    print()
    print("NON-CLAIMS: unsettled data; LambdaCDM viable; candidate shape test only;")
    print("no claim to measure or explain dark energy.")
    print("=" * 76)


if __name__ == "__main__":
    main()
