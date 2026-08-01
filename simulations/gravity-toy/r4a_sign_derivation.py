#!/usr/bin/env python3
"""
R4a sign derivation — is the exchange phantom (Landauer) or quintessence (Szilard)?

The w(z) test disfavored the phantom (Landauer-sign) branch and the quintessence
(opposite-sign) branch matches data better. Question: can we DERIVE which sign
the framework actually predicts, WITHOUT looking at cosmological data? If the
sign is derivable, we must take whatever it gives; we cannot flip it to fit.

Two thermodynamically opposite readings give opposite signs of the exchange Q
(rho_m' + 3H rho_m = -Q,  rho_S' = +Q):
  FLUX / Landauer (loss):     Q = +|source|  => rho_S GROWS => w_eff<-1 PHANTOM
  STOCKPILE / Szilard (gain): Q = -|source|  => rho_S SHRINKS => w_eff>-1 QUINTESSENCE

The framework's LOCKED READING selects one (PROGRESS_REPORT §2.1 / m11-idem-to-load):
  "Load L = demand from ... entropy FLUX, NOT remaining identity stockpile;
   active identity loss / scrambling => HIGHER L."
  Anti-pattern EXPLICITLY REJECTED: "Load = remaining ... potential identity
   still to compute" ; "stockpile without flux is not high demand."

So the load (hence the rho_S source) is the entropy-production FLUX (the loss),
not the recorded/remaining stockpile. The flux is non-negative (2nd law: net
entropy production >= 0). Therefore:

  Q = +|flux| >= 0  =>  rho_S grows  =>  PHANTOM.

The Szilard/quintessence reading sources gravity from the RECORDING (stockpile
being drawn down) — which is exactly the rejected anti-pattern. So within the
framework as defined, the sign is DERIVED to phantom (the disfavored branch).
Getting quintessence would require overturning the locked reading (a different
theory, or fitting to data).

Cross-check: the second law (net entropy production > 0) is itself the
dissipative/Landauer direction — independently consistent with phantom.

NON-CLAIMS: this derives a SIGN from a program convention (labeled 'semantic')
plus the 2nd law; it is not a claim about nature. Magnitude still free. No
gravity/dark-energy claim.

Run:
  .venv/bin/python simulations/gravity-toy/r4a_sign_derivation.py
"""

from __future__ import annotations

OM0, OS0 = 0.30, 0.70


def w0_of_signed_xi(xi: float) -> float:
    """w0 = -1 - xi*Om/(3*OS); xi>0 phantom, xi<0 quintessence."""
    return -1.0 - xi * OM0 / (3.0 * OS0)


def main():
    print("=" * 76)
    print("R4a sign derivation — flux (Landauer) vs stockpile (Szilard)")
    print("Design: emergent-gravity/r4a-promotion.md · PROGRESS_REPORT §2.1")
    print("=" * 76)

    # the load's entropy term is a non-negative flux (rate of entropy production)
    flux_sign = +1        # |dS_c/dtau| >= 0 by the 2nd law (net entropy production)
    assert flux_sign > 0

    print("\nStep 1. The rho_S source = the load's entropy-production term")
    print("        = |dS_c/dtau|, a NON-NEGATIVE flux (2nd law).")
    print("\nStep 2. Locked reading (framework convention): the load is that FLUX")
    print("        (active loss/scrambling -> higher L), NOT the recorded/remaining")
    print("        stockpile (explicitly rejected anti-pattern).")
    print("\nStep 3. Sourcing rho_S from a non-negative flux => Q >= 0 => rho_S grows")
    print("        => the interacting-DE sign is xi > 0.")

    # the two readings, made concrete
    xi_flux = +0.3        # locked reading: flux sources rho_S (Q>0)
    xi_stock = -0.3       # rejected reading: stockpile drawdown drains rho_S (Q<0)
    w0_flux = w0_of_signed_xi(xi_flux)
    w0_stock = w0_of_signed_xi(xi_stock)

    print(f"\n  reading                     sign of Q   w0         branch")
    print(f"  --------------------------------------------------------------")
    print(f"  FLUX (Landauer, LOCKED)      Q>0 (xi>0)  {w0_flux:+.4f}   PHANTOM")
    print(f"  STOCKPILE (Szilard, REJECTED) Q<0 (xi<0)  {w0_stock:+.4f}   quintessence")

    # the derivation selects the flux reading
    derived_xi_sign = flux_sign     # locked reading ties rho_S source to +flux
    assert derived_xi_sign > 0, "locked reading forces xi>0"
    w0_derived = w0_of_signed_xi(abs(0.3) * derived_xi_sign)
    assert w0_derived < -1.0, "derived branch must be phantom (w0<-1)"

    print("\n" + "=" * 76)
    print("DERIVED RESULT")
    print("=" * 76)
    print("  The framework's OWN locked reading (load = entropy FLUX, not recorded")
    print("  stockpile) + the 2nd law (flux >= 0) force  Q >= 0  =>  rho_S grows  =>")
    print("  the PHANTOM branch (w0 <= -1).  This is the sign DERIVED from the")
    print("  framework, independent of any cosmological data.")
    print()
    print("  It is the SAME sign the w(z) test found DISFAVORED. So the framework")
    print("  genuinely predicts the disfavored sign — a clean, falsifiable outcome,")
    print("  not an ambiguity.")
    print()
    print("  The Szilard/quintessence sign (which the data prefers) requires sourcing")
    print("  gravity from the RECORDING/stockpile side — the framework's explicitly")
    print("  REJECTED anti-pattern. Adopting it would be either (i) a DIFFERENT theory")
    print("  (revise the locked reading for independent reasons), or (ii) FITTING to")
    print("  data (illegitimate). We cannot flip the sign to serve the data.")
    print()
    print("  => Honest verdict: the R4a promotion, on the framework's own terms,")
    print("     predicts PHANTOM dark energy, which current (unsettled) data mildly")
    print("     DISFAVORS. The quintessence rescue is not available within this theory.")
    print()
    print("NON-CLAIMS: sign derived from a program convention + 2nd law, not from")
    print("nature; magnitude still free; no dark-energy claim. See r4a-promotion.md.")
    print("=" * 76)


if __name__ == "__main__":
    main()
