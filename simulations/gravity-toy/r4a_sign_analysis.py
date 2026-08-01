#!/usr/bin/env python3
"""
R4a sign analysis — which end of the free-energy flow is rho_S?

Prompted by a sharp objection: the master-equation load is built on the OUTPUT
entropy S_c (von Neumann of the channel output), and |dS_c/dtau| is a MAGNITUDE
(sign-neutral). So the earlier "derived phantom" was over-confident — the sign
of the energy exchange is NOT fixed by the load term alone. Can the output-
generation ("information generated from the inputs") reading legitimately give
the data-favored quintessence sign?

The honest way to settle it: cosmic computation is a single FREE-ENERGY FLOW
driven by the 2nd law:
      reservoir (low-entropy initial state / free energy)  --->  dissipation
      (radiation, black-hole entropy, heat)
The reservoir DEPLETES; the dissipation ACCUMULATES; they are the two ends of
ONE flow. Which end we identify with the gravitating sector rho_S fixes the sign
of Q (rho_m' + 3H rho_m = -Q, rho_S' = +Q), hence phantom vs quintessence.

We enumerate the reasonable identifications, give each its cosmological direction
(grows/shrinks) from INDEPENDENT principles (2nd law / free-energy consumption),
the resulting sign, and its status under the framework's locked reading.

Key fact: EVERY identification that tracks entropy PRODUCTION (the 2nd-law arrow)
gives rho_S GROWING => phantom. Quintessence requires identifying rho_S with the
free-energy RESERVOIR being consumed — which is the framework's EXPLICITLY
REJECTED 'remaining stockpile/potential' anti-pattern.

Conclusion: phantom is robustly favored across entropy-tracking readings; the
quintessence escape requires the rejected reservoir reading. So the sign is a
STRONG LEAN to phantom (not an airtight theorem, not a free 50/50), and the
quintessence rescue is not available without a NEW, independently-motivated
principle (which must not be chosen to fit data).

NON-CLAIMS: maps a theory space from a program convention + 2nd law; not a claim
about nature; magnitude free; no dark-energy claim.

Run:
  .venv/bin/python simulations/gravity-toy/r4a_sign_analysis.py
"""

from __future__ import annotations

OM0, OS0 = 0.30, 0.70


def w0_of_signed_xi(xi):
    return -1.0 - xi * OM0 / (3.0 * OS0)


# (name, cosmological direction, why (independent principle), branch, framework status)
IDENTIFICATIONS = [
    ("loss-repository (erased-info heat)",
     "grows", "fed by entropy-production flux (2nd law: Sdot>0)",
     "phantom", "ENDORSED (flux of active loss)"),
    ("output-entropy flux (S_c increases)",
     "grows", "coarse-grained output entropy rises (2nd law)",
     "phantom", "consistent (entropy flux)"),
    ("generated-structure resource (records built)",
     "grows", "structure/records net-ACCUMULATE over cosmic time",
     "phantom", "consistent (active generation flux)"),
    ("free-energy reservoir (initial potential)",
     "shrinks", "free energy is net-CONSUMED (heat death direction)",
     "quintessence", "REJECTED (remaining stockpile/potential anti-pattern)"),
]


def main():
    print("=" * 82)
    print("R4a sign analysis — identifications of rho_S and their derived sign")
    print("Design: emergent-gravity/r4a-promotion.md §4c · PROGRESS_REPORT §2.1")
    print("=" * 82)

    print("\nSingle free-energy flow (2nd law):  reservoir --(consumed)--> dissipation.")
    print("Which END is the gravitating sector rho_S decides the sign.\n")

    xi_mag = 0.3
    hdr = f"  {'identification':>38}  {'dir':>6}  {'branch':>12}  status"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    phantom_count = quint_count = 0
    for name, direction, why, branch, status in IDENTIFICATIONS:
        xi = +xi_mag if branch == "phantom" else -xi_mag
        w0 = w0_of_signed_xi(xi)
        if branch == "phantom":
            phantom_count += 1
        else:
            quint_count += 1
        print(f"  {name:>38}  {direction:>6}  {branch:>12}  {status}")
        print(f"  {'':>38}  w0={w0:+.4f}   why: {why}")

    # every entropy-PRODUCTION-tracking reading -> phantom; only reservoir -> quint
    entropy_tracking = [i for i in IDENTIFICATIONS if i[1] == "grows"]
    assert all(i[3] == "phantom" for i in entropy_tracking), \
        "all entropy-production-tracking identifications must give phantom"
    quint = [i for i in IDENTIFICATIONS if i[3] == "quintessence"]
    assert all("REJECTED" in i[4] for i in quint), \
        "quintessence must require the framework's rejected reservoir reading"

    print("\n" + "=" * 82)
    print("RESULT")
    print("=" * 82)
    print(f"  {phantom_count} of {len(IDENTIFICATIONS)} identifications give PHANTOM; all of them are the ones")
    print("  that TRACK ENTROPY PRODUCTION (the 2nd-law arrow: loss flux, output-")
    print("  entropy rise, or structure accumulating). The single QUINTESSENCE case")
    print("  identifies rho_S with the free-energy RESERVOIR being consumed — which")
    print("  is the framework's EXPLICITLY REJECTED 'remaining stockpile' anti-pattern.")
    print()
    print("  Correction to the earlier claim: the sign is NOT an airtight theorem")
    print("  (|dS_c/dtau| is sign-neutral, and the load is output-based, as objected).")
    print("  But it is also NOT a free 50/50: phantom is ROBUSTLY FAVORED, because")
    print("  every reading that follows the entropy arrow lands there. Quintessence")
    print("  needs the one reading the framework rejects.")
    print()
    print("  ==> The quintessence (Szilard/generation) rescue is NOT available within")
    print("      the framework as it stands. It would require a NEW, independently-")
    print("      motivated principle that identifies rho_S with the reservoir end —")
    print("      and that principle must NOT be chosen to fit DESI. Absent it, the")
    print("      honest prediction remains PHANTOM (currently disfavored), and the")
    print("      escape is a genuine open theory problem, not a quick sign flip.")
    print()
    print("NON-CLAIMS: theory-space map from a convention + 2nd law; not nature;")
    print("magnitude free; no dark-energy claim. See emergent-gravity/r4a-promotion.md.")
    print("=" * 82)


if __name__ == "__main__":
    main()
