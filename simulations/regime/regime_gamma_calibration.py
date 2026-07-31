#!/usr/bin/env python3
"""
Stage 2 — calibrate gamma and compute the dephasing clock magnitude.

Program: papers/REGIME_PROGRAM_dSc_decoupling.md (Stage 2).
Stage 1 showed pure dephasing produces S_c at fixed local energy (a departure
in principle). Whether it is OBSERVABLE depends on the magnitude of the load's
entropy-production term  gamma*|dS_c/dtau|. This script attempts to pin gamma.

--- Dimensional analysis (what IS derivable) ---
L is a dimensionless scalar and, in dtau=dt/(1+alpha*L), alpha is dimensionless.
The term gamma*|dS_c/dtau| must be dimensionless; S_c is dimensionless (bits),
so |dS_c/dtau| has units 1/time  =>  gamma has units of TIME.

--- The structural gap (what is NOT derivable) ---
The master equation states alpha*beta = 4*pi*G/c^4 as the calibration. But the
energy term beta*E/(V*eps0) is dimensionless (E over a Planck-density * volume),
so beta is dimensionless; with alpha dimensionless, alpha*beta is dimensionless
while 4*pi*G/c^4 is dimensionful. The stated relation is therefore NOT
dimensionally consistent, and no independent condition fixes gamma's value.
=> gamma is under-determined by the theory as written. We proceed by treating
gamma as a fundamental time and bounding the ONLY observable combination.

--- The observable ---
The fractional dephasing clock shift (small-load) is
    delta ~ alpha * gamma * |dS_c/dtau| ~ eta / T2 ,   eta := alpha*gamma  [time],
since |dS_c/dtau| ~ (order 1 bit)/T2 during dephasing. Only the product
eta = alpha*gamma is observable.

We (a) tabulate delta for candidate fundamental gamma with alpha=1, (b) derive
the empirical bound on eta from precision-clock null results, and (c) state the
verdict.

NON-CLAIMS: no gravity asserted; gamma is not uniquely derivable from the
theory; alpha=1 rows are a charitable upper-end reading, not a prediction.

Run:
  .venv/bin/python simulations/regime/regime_gamma_calibration.py
"""

from __future__ import annotations

import math

# physical constants (SI)
HBAR = 1.054_571_817e-34     # J s
C = 2.997_924_58e8           # m/s
G = 6.674_30e-11             # m^3 kg^-1 s^-2
KB = 1.380_649e-23           # J/K
M_E = 9.109_383_7e-31        # kg  (electron)
T_PLANCK = math.sqrt(HBAR * G / C**5)   # ~5.39e-44 s

# a representative optical clock transition (Sr, 429 THz)
NU_OPT = 4.29e14             # Hz
OMEGA_OPT = 2 * math.pi * NU_OPT
E_OPT = HBAR * OMEGA_OPT     # J

CLOCK_SENS = 1e-18           # state-of-the-art fractional frequency sensitivity


def ml_time(E: float) -> float:
    """Margolus-Levitin time: minimum time to an orthogonal state at energy E."""
    return math.pi * HBAR / (2 * E)


def candidate_gammas():
    """(name, gamma[s], rationale)."""
    return [
        ("Planck time", T_PLANCK, "sqrt(hbar G / c^5)"),
        ("Compton (electron)", HBAR / (M_E * C**2), "hbar/(m_e c^2)"),
        ("Margolus-Levitin (optical)", ml_time(E_OPT), "pi hbar/(2 E_opt)"),
    ]


def main():
    print("=" * 78)
    print("Stage 2 — gamma calibration & dephasing clock magnitude")
    print("Design: papers/REGIME_PROGRAM_dSc_decoupling.md")
    print("=" * 78)

    print("\nDimensional analysis: gamma has units of TIME (|dS_c/dtau| ~ 1/time).")
    print(f"  Planck time t_Pl = {T_PLANCK:.2e} s")
    print(f"  ML time (optical E={E_OPT:.2e} J) = {ml_time(E_OPT):.2e} s")
    print("\nStructural gap: alpha*beta = 4*pi*G/c^4 is dimensionally INCONSISTENT")
    print("  with dimensionless alpha,beta,L (4*pi*G/c^4 = "
          f"{4*math.pi*G/C**4:.2e} s^2 kg^-1 m^-1, dimensionful).")
    print("  => gamma is NOT uniquely fixed by the theory as written.")

    print("\nObservable: fractional dephasing clock shift  delta ~ eta / T2,  "
          "eta = alpha*gamma.")
    print(f"Precision-clock sensitivity assumed: delta_min = {CLOCK_SENS:.0e}")

    T2_vals = [1e-3, 1.0, 1e2]  # dephasing/coherence times (s): fast, atomic, best
    print("\n(a) delta = alpha*gamma/T2 with alpha=1 (charitable upper end):")
    header = f"  {'gamma model':>26} {'gamma [s]':>11} | " + " ".join(
        f"T2={t:g}s" for t in T2_vals)
    print(header)
    print("  " + "-" * (len(header) - 2))
    for name, g, _ in candidate_gammas():
        cells = []
        for t2 in T2_vals:
            d = g / t2
            flag = "obs" if d > CLOCK_SENS else "—"
            cells.append(f"{d:.1e}({flag})")
        print(f"  {name:>26} {g:>11.2e} | " + "  ".join(cells))

    print("\n  'obs' = above current clock sensitivity (would be seen / excluded);")
    print("  '—'   = below sensitivity (unmeasurable).")

    # (b) empirical bound on eta from null results (no anomalous shift seen)
    print("\n(b) Empirical bound from precision-clock null results (no dephasing-")
    print("    dependent shift observed at delta_min):  eta = alpha*gamma < delta_min * T2")
    for t2 in T2_vals:
        print(f"    T2={t2:g}s  =>  alpha*gamma < {CLOCK_SENS * t2:.1e} s")

    # verdict logic
    eta_bound = CLOCK_SENS * 1.0  # representative T2 ~ 1 s
    planck_eta = T_PLANCK          # alpha ~ 1, gamma ~ Planck
    ml_eta = ml_time(E_OPT)        # alpha ~ 1, gamma ~ ML

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  Empirical bound (T2~1s): alpha*gamma < {eta_bound:.0e} s.")
    print(f"  - gamma ~ Planck time ({planck_eta:.0e} s), alpha~1: "
          f"delta~{planck_eta:.0e} << {CLOCK_SENS:.0e}  => UNMEASURABLE (reformulation).")
    print(f"  - gamma ~ ML/optical ({ml_eta:.0e} s), alpha~1: "
          f"delta~{ml_eta:.0e} > {CLOCK_SENS:.0e}  => already EXCLUDED by clocks.")
    print("  - If alpha is gravitationally suppressed (as the Planck-scale eps0 and")
    print("    4piG/c^4 relation suggest), ALL cases are far below sensitivity.")
    print()
    print("  ==> For every NATURAL parameter choice the dephasing clock effect is")
    print("      either unmeasurable (fundamental gamma) or already excluded")
    print("      (order-unity alpha with microscopic gamma). The framework predicts")
    print("      NO currently-observable effect without an unmotivated, un-suppressed")
    print("      alpha*gamma. => REFORMULATION IN PRACTICE (Stage-1 departure real")
    print("      in principle, but not observable).")
    print()
    print("  The true blocker is structural: the master equation does not fix")
    print("  alpha*gamma (dimensional inconsistency of alpha*beta=4piG/c^4). A")
    print("  dimensionally-consistent completion of the load constants is the")
    print("  missing theory step, not a bigger experiment.")

    assert planck_eta / 1.0 < CLOCK_SENS, "Planck-gamma effect must be unmeasurable"
    assert ml_eta / 1.0 > CLOCK_SENS, "ML-gamma (alpha=1) effect must exceed sensitivity"
    print("\nNON-CLAIMS: gamma not uniquely derivable; alpha=1 is an upper-end")
    print("reading, not a prediction; no gravity asserted.")
    print("=" * 78)


if __name__ == "__main__":
    main()
