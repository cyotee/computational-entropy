#!/usr/bin/env python3
"""
M5c — discrete warm-up / PM energy descent witness (Layer W only).

On one joint-toy IC (noisy_step), show that the explicit Euler PM step
non-increases the classical PM edge energy

    E_h[φ] = sum_e  (K²/2) log(1 + (g_e/K)²)

while the matched warm-up action

    S_matched = -sum_e log(1 + (g_e/K)²)   (= - (2/K²) E_h)

non-decreases. Heat is reported for contrast (Dirichlet flow ≠ Ψ-flow).

Reuses `_joint_toy_v2_core.py` PM/heat RHS. Not residual dual, not continuum
Γ-limit, not gravity, not L≡G.

Run:
  .venv/bin/python simulations/bridging/m5c_pm_energy_descent.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402

# Slightly safer explicit step than scorecard default for monotone energy witness
DT_WITNESS = 0.02
N_STEPS = 120
K = toy.K_PM
# Allow tiny float noise / O(dt²) Euler remainder on open chain
TOL_NONINCREASE = 1e-9


def pm_edge_energy(phi: np.ndarray, K: float = K) -> float:
    """E_h = sum Ψ(|g|) with Ψ(s) = (K²/2) ln(1+(s/K)²)."""
    g = toy.gradients(phi)
    return float(0.5 * (K**2) * np.sum(np.log1p((g / K) ** 2)))


def matched_warmup_action(phi: np.ndarray, K: float = K) -> float:
    """S_matched = -sum ln(1+(g/K)²); E_h = -(K²/2) S_matched."""
    g = toy.gradients(phi)
    return float(-np.sum(np.log1p((g / K) ** 2)))


def dirichlet_energy(phi: np.ndarray) -> float:
    g = toy.gradients(phi)
    return float(0.5 * np.sum(g**2))


def run_energy_hist(phi0: np.ndarray, mode: str, n_steps: int = N_STEPS, dt: float = DT_WITNESS):
    phi = phi0.astype(float).copy()
    E_pm = [pm_edge_energy(phi)]
    S_m = [matched_warmup_action(phi)]
    E_dir = [dirichlet_energy(phi)]
    S_gfe_default = [toy.gfe_action(phi)]  # α_G default bookkeeping only

    for _ in range(n_steps):
        if mode == "pm":
            phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
        elif mode == "heat":
            phi = toy.step_euler(phi, toy.rhs_heat, dt)
        else:
            raise ValueError(mode)
        E_pm.append(pm_edge_energy(phi))
        S_m.append(matched_warmup_action(phi))
        E_dir.append(dirichlet_energy(phi))
        S_gfe_default.append(toy.gfe_action(phi))

    return {
        "E_pm": np.asarray(E_pm),
        "S_matched": np.asarray(S_m),
        "E_dir": np.asarray(E_dir),
        "S_gfe_default": np.asarray(S_gfe_default),
        "phi_final": phi,
    }


def max_increment(arr: np.ndarray) -> float:
    """max_n (arr[n+1]-arr[n]) — largest step (positive ⇒ increase)."""
    d = np.diff(arr)
    return float(np.max(d)) if len(d) else 0.0


def min_increment(arr: np.ndarray) -> float:
    """min_n (arr[n+1]-arr[n]) — most negative step."""
    d = np.diff(arr)
    return float(np.min(d)) if len(d) else 0.0


def main() -> int:
    ics = toy.build_ics()
    y = ics["noisy_step"]["y"]
    star = ics["noisy_step"]["star"]

    print("M5c PM energy-descent witness (Layer W)")
    print(f"  IC: noisy_step  N={toy.N}  h={toy.h}  K={K}  dt={DT_WITNESS}  steps={N_STEPS}")
    print(f"  residual_mse(y, star) = {toy.residual_mse(y, star):.6f}")
    print()

    pm = run_energy_hist(y, "pm")
    heat = run_energy_hist(y, "heat")

    # Identity check: E = -(K²/2) S_matched
    id_err = np.max(np.abs(pm["E_pm"] + 0.5 * (K**2) * pm["S_matched"]))
    print(f"  identity |E_pm + (K²/2) S_matched|_∞ (PM traj) = {id_err:.3e}")

    pm_E_up = max_increment(pm["E_pm"])
    pm_S_down = min_increment(pm["S_matched"])  # most negative ΔS
    heat_E_up = max_increment(heat["E_pm"])

    print()
    print("  PM trajectory:")
    print(f"    E_pm:       {pm['E_pm'][0]:.6f} → {pm['E_pm'][-1]:.6f}  (max Δ⁺ = {pm_E_up:.3e})")
    print(f"    S_matched:  {pm['S_matched'][0]:.6f} → {pm['S_matched'][-1]:.6f}  (min Δ = {pm_S_down:.3e})")
    print(f"    E_Dir:      {pm['E_dir'][0]:.6f} → {pm['E_dir'][-1]:.6f}")
    print(f"    S_gfe(α_G): {pm['S_gfe_default'][0]:.6f} → {pm['S_gfe_default'][-1]:.6f}  (default α_G≠1/K²; bookkeeping)")
    print()
    print("  Heat trajectory (contrast):")
    print(f"    E_pm:       {heat['E_pm'][0]:.6f} → {heat['E_pm'][-1]:.6f}  (max Δ⁺ = {heat_E_up:.3e})")
    print(f"    E_Dir:      {heat['E_dir'][0]:.6f} → {heat['E_dir'][-1]:.6f}")
    print()

    ok = True
    # PM: E non-increasing (allow tiny positive float noise)
    if pm_E_up > TOL_NONINCREASE:
        # Also accept if overall net decrease and only O(1e-12)-scale blips
        net = pm["E_pm"][-1] - pm["E_pm"][0]
        if pm_E_up > 1e-8 or net > 0:
            print(f"FAIL: PM E_pm increased (max Δ⁺={pm_E_up:.3e}, net={net:.3e})")
            ok = False
        else:
            print(f"PASS (soft): PM E_pm max Δ⁺={pm_E_up:.3e} ≤ 1e-8 with net decrease")
    else:
        print(f"PASS: PM E_pm non-increasing (max Δ⁺={pm_E_up:.3e} ≤ {TOL_NONINCREASE})")

    # PM: S_matched non-decreasing
    if pm_S_down < -TOL_NONINCREASE:
        net_S = pm["S_matched"][-1] - pm["S_matched"][0]
        if pm_S_down < -1e-8 or net_S < 0:
            print(f"FAIL: PM S_matched decreased (min Δ={pm_S_down:.3e}, net={net_S:.3e})")
            ok = False
        else:
            print(f"PASS (soft): PM S_matched min Δ={pm_S_down:.3e} ≥ -1e-8 with net increase")
    else:
        print(f"PASS: PM S_matched non-decreasing (min Δ={pm_S_down:.3e})")

    if id_err > 1e-9:
        print(f"FAIL: E ↔ S identity broken (err={id_err:.3e})")
        ok = False
    else:
        print(f"PASS: E_pm = -(K²/2) S_matched identity")

    # Informative: heat also often reduces E_pm (smoothing), but is not the Ψ-gradient flow claim
    print()
    print("  Note: heat may also reduce E_pm by isotropic smoothing; M5c claim is PM = discrete")
    print("  gradient descent of E_h (matched), not that heat fails to decrease E_h.")
    print("  Layer D residual dual is not tested here.")
    print()

    if ok:
        print("VERDICT: PASS — discrete PM energy descent witness (Layer W, one IC)")
        return 0
    print("VERDICT: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
