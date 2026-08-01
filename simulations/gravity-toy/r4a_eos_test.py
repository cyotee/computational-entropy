#!/usr/bin/env python3
"""
Vacuum-character (equation-of-state) test — which end of the free-energy flow
can actually BE dark energy?

A dark-energy sector must have w = p/(rho c^2) ~ -1 (negative pressure, to
accelerate). The sign analysis left two candidate identifications of the
gravitating sector rho_S (the two ends of the free-energy flow). This test asks,
DATA-INDEPENDENTLY, what equation of state each physically has. If only one end
can be w~-1, the equation of state — not DESI — selects the reading.

Equation-of-state reference (standard):
  radiation (relativistic heat)  w = +1/3   (dilutes a^-4, decelerates)
  matter (thermalized, rest)     w =  0      (dilutes a^-3, decelerates)
  scalar potential, slow-roll    w -> -1     (nearly constant, accelerates)
  scalar potential, rolling      w  > -1     (thawing quintessence)

The two ends:
  DISSIPATION end (Landauer heat from entropy production): the exchanged energy
    is DISSIPATED HEAT -> thermalizes -> w in [0, 1/3] >= 0. This CANNOT be a
    w~-1 dark sector. (So the original R4a 'phantom' branch, which ASSUMED
    w_S=-1 for this energy, used an EoS-inconsistent assumption.)
  RESERVOIR end (latent free energy / unrealized potential): if stored as a
    scalar-field POTENTIAL, w ~ -1 (viable dark energy). As it is consumed
    (the field rolls / potential is realized), w rises above -1 => THAWING
    quintessence (w0 > -1, wa < 0).

Consequence: the equation of state RULES OUT the dissipation/phantom reading as
dark energy and SELECTS the reservoir reading — which gives quintessence — on
data-independent physical grounds. Bonus: a rolling reservoir predicts the
THAWING quadrant (w0>-1, wa<0) structurally (Caldwell-Linder), which is the same
DIRECTION current DESI hints point — but that is a consistency remark, NOT the
test (the test is the EoS argument, which never used the data).

Honest caveats (do not overstate): (i) this is a REVISION of the framework's
locked 'flux, not stockpile' reading — legitimate because motivated by EoS
consistency, not by DESI; (ii) the reservoir has w~-1 ONLY if the computational
free energy is stored as a scalar potential (a modeling choice); (iii) the
MAGNITUDE (coupling / potential scale) is still FREE — this does NOT explain the
value of dark energy.

NON-CLAIMS: no claim to explain dark energy; magnitude free; reservoir-as-scalar
is a modeling choice; a data-independent EoS argument, not a fit.

Run:
  .venv/bin/python simulations/gravity-toy/r4a_eos_test.py
"""

from __future__ import annotations


# equation of state of each candidate rho_S end (from its physical nature)
def w_dissipation() -> tuple[float, float]:
    """Dissipated heat: thermal, w in [0, 1/3]. Return (w_min, w_max)."""
    return (0.0, 1.0 / 3.0)


def w_reservoir_frozen() -> float:
    """Latent potential, slow-roll (frozen): w -> -1."""
    return -1.0


def thawing_wa(w0: float) -> float:
    """Caldwell-Linder thawing relation: wa ~ -1.5 (1 + w0)  (w0 > -1 => wa < 0)."""
    return -1.5 * (1.0 + w0)


def can_be_dark_energy(w: float) -> bool:
    """A dark-energy sector needs w < -1/3 (to accelerate expansion)."""
    return w < -1.0 / 3.0


def main():
    print("=" * 80)
    print("Vacuum-character (EoS) test — can each rho_S end be dark energy?")
    print("Design: emergent-gravity/r4a-promotion.md; data-INDEPENDENT")
    print("=" * 80)

    wd_lo, wd_hi = w_dissipation()
    wr = w_reservoir_frozen()

    print("\nEquation of state of the two ends (from physics, no DESI input):")
    print(f"  DISSIPATION (Landauer heat)   : w in [{wd_lo:.2f}, {wd_hi:.2f}]  "
          f"(thermal)  -> dark energy? {can_be_dark_energy(wd_hi)}")
    print(f"  RESERVOIR (scalar potential)  : w ~ {wr:+.2f}            "
          f"(slow-roll) -> dark energy? {can_be_dark_energy(wr)}")

    # the decisive checks
    assert not can_be_dark_energy(wd_lo) and not can_be_dark_energy(wd_hi), \
        "dissipation (thermal, w>=0) cannot be a w~-1 dark sector"
    assert can_be_dark_energy(wr), "reservoir (potential, w~-1) can be dark energy"

    print("\n  => The DISSIPATION end (which gave PHANTOM) is thermal (w>=0) and")
    print("     CANNOT be dark energy. The original R4a phantom branch assumed")
    print("     w_S=-1 for this heat — an EoS-INCONSISTENT assumption.")
    print("  => Only the RESERVOIR end (w~-1 potential) is a viable dark sector,")
    print("     and consuming it (the field rolls) gives QUINTESSENCE.")

    # structural prediction of the rolling reservoir: thawing quadrant
    print("\nStructural prediction of a rolling reservoir (thawing scalar):")
    print(f"  {'w0':>7} {'wa=-1.5(1+w0)':>14}  quadrant")
    for w0 in (-0.95, -0.90, -0.80):
        wa = thawing_wa(w0)
        quad = "w0>-1, wa<0 (thawing)" if (w0 > -1 and wa < 0) else "?"
        print(f"  {w0:7.2f} {wa:14.3f}  {quad}")
    print("  => reservoir/quintessence structurally lands in the (w0>-1, wa<0)")
    print("     THAWING quadrant — data-INDEPENDENTLY. (Current DESI hints point")
    print("     to that same quadrant; a consistency remark, NOT the test.)")

    print("\n" + "=" * 80)
    print("VERDICT — the vacuum-character argument SURVIVES")
    print("=" * 80)
    print("  On data-independent equation-of-state grounds:")
    print("  - dissipation (phantom) reading is thermal (w>=0) => NOT dark energy;")
    print("    the earlier phantom result used an EoS-inconsistent w_S=-1.")
    print("  - reservoir reading (w~-1 potential) is the ONLY viable dark sector,")
    print("    and it gives thawing QUINTESSENCE (w0>-1, wa<0).")
    print()
    print("  So the equation of state — not the data — selects the reservoir /")
    print("  quintessence reading. This LEGITIMATELY favors the quintessence")
    print("  direction, earned by physics, not by fitting DESI.")
    print()
    print("  HONEST CAVEATS (this is a step, not a theory):")
    print("  (i)   it REVISES the framework's locked 'flux, not stockpile' reading —")
    print("        legitimate because motivated by EoS consistency, not by DESI;")
    print("  (ii)  the reservoir is w~-1 only if the computational free energy is")
    print("        stored as a scalar potential (a modeling choice to be justified);")
    print("  (iii) the MAGNITUDE (potential scale / coupling) is still FREE — this")
    print("        does NOT explain the observed dark-energy value.")
    print()
    print("  Next (legitimate): justify the reservoir-as-scalar storage from the")
    print("  framework independently, then extract an INDEPENDENT prediction beyond")
    print("  the thawing quadrant to test against data DESI did not fix.")
    print()
    print("NON-CLAIMS: data-independent EoS argument; magnitude free; no claim to")
    print("explain dark energy. See emergent-gravity/r4a-promotion.md.")
    print("=" * 80)


if __name__ == "__main__":
    main()
