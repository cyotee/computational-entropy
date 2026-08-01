#!/usr/bin/env python3
"""
Path 1 — does the framework FORCE the reservoir to be a w~-1 scalar potential?

The EoS test (r4a_eos_test.py) showed: IF the reservoir is a w~-1 scalar
potential, quintessence follows. Path 1 tests whether the framework actually
delivers a w~-1 potential — data-independently, prepared for it to FAIL.

Scalar-field equation of state (homogeneous field phi with potential V):
  rho = (1/2) phidot^2 + V,   p = (1/2) phidot^2 - V
  w = (K - V)/(K + V),  with  K = (1/2) phidot^2  (kinetic).
Let  r = K/V  (kinetic/potential ratio). Then
  w(r) = (r - 1)/(r + 1).
  r -> 0   : w -> -1  (idle / slow-roll, dark energy)
  r = 1/2  : w = -1/3 (dark-energy threshold; DE needs r < 1/2)
  r -> inf : w -> +1  (max activity, stiff, NOT dark energy)

Framework identification (the crux). The 'kinetic' term is the RATE of
realization/computation. The framework's load carries exactly this: the active
term |dS_c/dtau| (entropy-production flux). The locked reading emphasizes HIGH
flux / active scrambling => LARGE phidot => LARGE r => w -> +1 (stiff, NOT dark
energy). The reservoir is w~-1 ONLY in the LOW-flux / IDLE regime (r -> 0) — i.e.
exactly the 'idle stockpile' the load reading de-emphasizes.

So the framework does NOT force w~-1 through its active dynamics; w~-1 appears
only for the idle reservoir. And the DYNAMICS (thawing vs freezing, the sign of
wa) depend on the flux HISTORY r(a):
  activity DECLINING over time  (r falls)  => w falls toward -1 late => FREEZING
                                              (w>-1 early, ->-1 late) => wa > 0
  activity RISING over time     (r grows)  => w rises from -1        => THAWING
                                              => wa < 0
A natural late-time reading (structure formation winds down, dark energy
suppresses new structure => activity declines) gives FREEZING (wa>0) — the
OPPOSITE of the DESI thawing hint, and it RETRACTS the §4d 'thawing' assertion,
which assumed rising activity without justification.

Verdict: Path 1 does NOT cleanly ground w~-1. The w~-1 regime is the idle/low-
flux reservoir (tension with the load's high-flux emphasis — the dark sector is
the de-emphasized stockpile again), and the native dynamics lean FREEZING
(wa>0), on the WRONG side of the data. The clean thawing-quintessence match of
§4d was over-optimistic.

NON-CLAIMS: data-independent scalar-field analysis; flux history not precisely
derived; no dark-energy claim; magnitude free.

Run:
  .venv/bin/python simulations/gravity-toy/r4a_reservoir_eos.py
"""

from __future__ import annotations


def w_of_ratio(r: float) -> float:
    """w = (K-V)/(K+V) with r = K/V (kinetic/potential ratio)."""
    return (r - 1.0) / (r + 1.0)


def main():
    print("=" * 80)
    print("Path 1 — reservoir equation of state from the framework (data-independent)")
    print("Design: emergent-gravity/r4a-promotion.md §4d")
    print("=" * 80)

    print("\nScalar EoS  w(r)=(r-1)/(r+1),  r = kinetic/potential = realization rate^2 / V:")
    print(f"  {'r=K/V':>8}  {'w':>7}  {'regime':<28}  dark energy?")
    for r, label in [(0.0, "idle / slow-roll"), (0.1, "low activity"),
                     (0.5, "DE threshold"), (1.0, "kinetic=potential"),
                     (5.0, "active / high-flux")]:
        w = w_of_ratio(r)
        de = "yes" if w < -1.0 / 3.0 else "no"
        print(f"  {r:8.2f}  {w:+7.3f}  {label:<28}  {de}")

    # dark energy (w<-1/3) requires r<1/2
    assert w_of_ratio(0.49) < -1 / 3 <= w_of_ratio(0.51) + 1e-9, "DE threshold at r=1/2"

    print("\nFramework identification: kinetic term = realization RATE = the load's")
    print("active flux |dS_c/dtau|. The locked reading emphasizes HIGH flux/active")
    print("scrambling => LARGE r => w -> +1 (stiff, NOT dark energy). The reservoir")
    print("is w~-1 ONLY in the LOW-flux / IDLE regime (r->0) — the de-emphasized")
    print("'stockpile'.")

    print("\nDynamics (thawing vs freezing) from the flux history r(a):")
    print(f"  {'flux history':>22}  {'w trend':>16}  {'wa sign':>8}  vs DESI hint (thawing, wa<0)")
    for hist, trend, wa in [("activity DECLINING", "w -> -1 late (freeze)", "+  "),
                            ("activity RISING", "w rises from -1 (thaw)", "-  ")]:
        match = "MATCHES" if wa.strip() == "-" else "WRONG SIDE"
        print(f"  {hist:>22}  {trend:>16}  {wa:>8}  {match}")

    print("\n  Natural late-time reading: structure formation winds down (dark energy")
    print("  suppresses new structure) => activity DECLINES => FREEZING (wa>0) =>")
    print("  WRONG side of the DESI thawing hint. §4d's 'thawing' assumed RISING")
    print("  activity without justification — retracted.")

    print("\n" + "=" * 80)
    print("VERDICT — Path 1 does NOT cleanly ground w~-1 (partial, leaning negative)")
    print("=" * 80)
    print("  + Partial: the reservoir CAN be w~-1, but only in the IDLE / low-flux")
    print("    regime (r->0). So dark energy = the idle reservoir — which is again")
    print("    the framework's DE-EMPHASIZED 'stockpile', in tension with the load's")
    print("    high-flux reading.")
    print("  - The active/high-flux regime the framework emphasizes is kinetic-")
    print("    dominated (w->+1), i.e. NOT dark energy.")
    print("  - The wa sign is NOT cleanly derivable (needs the flux history); the")
    print("    natural declining-activity reading gives FREEZING (wa>0), the WRONG")
    print("    side of the DESI hint. The §4d thawing claim is RETRACTED.")
    print()
    print("  ==> The framework does not force a w~-1 dark sector through its own")
    print("      (active) dynamics; w~-1 requires the idle reservoir, and the")
    print("      dynamical signature leans the wrong way. The clean 'thawing")
    print("      quintessence consistent with DESI' of §4d was over-optimistic.")
    print("      Reservoir-as-dark-energy remains a POSIT, now with a known tension")
    print("      (idle-regime only) and a likely wrong-sign wa. Not grounded.")
    print()
    print("NON-CLAIMS: data-independent; flux history not derived; magnitude free;")
    print("no dark-energy claim. See emergent-gravity/r4a-promotion.md §4d-4e.")
    print("=" * 80)


if __name__ == "__main__":
    main()
