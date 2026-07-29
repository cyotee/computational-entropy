"""
M2 witness: load-PM vs heat vs pure PM on T1′ window.

Run:  .venv/bin/python simulations/bridging/test_t1_load_m2.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402


def _res(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.mean((a - b) ** 2))


def _heat(y: np.ndarray, n: int, dt: float) -> np.ndarray:
    phi = y.astype(float).copy()
    for _ in range(n):
        phi = toy.step_euler(phi, toy.rhs_heat, dt)
    return phi


def _pm(y: np.ndarray, n: int, dt: float, K: float) -> np.ndarray:
    phi = y.astype(float).copy()
    for _ in range(n):
        phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
    return phi


def _load_pm_with_tau(
    y: np.ndarray, star: np.ndarray, n: int, dt: float, K: float, alpha_L: float
) -> tuple[np.ndarray, float]:
    phi = y.astype(float).copy()
    H_prev = None
    tau = 0.0
    for _ in range(n):
        terms = toy.load_terms(phi, star, H_prev=H_prev, dt=dt)
        clock = 1.0 / (1.0 + alpha_L * terms["L_clock"])
        phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt * clock)
        tau += dt * clock
        H_prev = toy.load_terms(phi, star, H_prev=terms["H_c"], dt=dt)["H_c"]
    return phi, tau


def main(n_mc: int = 200, seed: int = 21) -> Path:
    rng = np.random.default_rng(seed)
    K, sigma, dt, N = toy.K_PM, toy.NOISE_SIGMA, toy.DT, toy.N
    alpha_L = toy.ALPHA_L
    star = toy.phi_star_step()
    steps_list = [15, 17, 18, 20, 25, 40, 80, 180]

    lines = [
        f"N_MC={n_mc} seed={seed} sigma={sigma} K={K} dt={dt} N={N} ALPHA_L={alpha_L}",
        (
            "n t mean_Rh mean_Rp mean_Rl mean_Rh_minus_Rp mean_Rh_minus_Rl "
            "mean_Rp_minus_Rl frac_load_beats_heat frac_pm_beats_heat mean_tau_over_t"
        ),
    ]

    d_hl_by_t: dict[float, float] = {}
    for n in steps_list:
        t = n * dt
        Rh, Rp, Rl, d_hp, d_hl, d_pl, taus = [], [], [], [], [], [], []
        for _ in range(n_mc):
            y = star + sigma * rng.standard_normal(N)
            rh = _res(_heat(y, n, dt), star)
            rp = _res(_pm(y, n, dt, K), star)
            phi_l, tau = _load_pm_with_tau(y, star, n, dt, K, alpha_L)
            rl = _res(phi_l, star)
            Rh.append(rh)
            Rp.append(rp)
            Rl.append(rl)
            d_hp.append(rh - rp)
            d_hl.append(rh - rl)
            d_pl.append(rp - rl)
            taus.append(tau / t)
        d_hl_by_t[t] = float(np.mean(d_hl))
        lines.append(
            f"{n} {t:.2f} {float(np.mean(Rh)):.6f} {float(np.mean(Rp)):.6f} "
            f"{float(np.mean(Rl)):.6f} {float(np.mean(d_hp)):+.6f} "
            f"{float(np.mean(d_hl)):+.6f} {float(np.mean(d_pl)):+.6f} "
            f"{float(np.mean(np.asarray(d_hl) > 0)):.4f} "
            f"{float(np.mean(np.asarray(d_hp) > 0)):.4f} {float(np.mean(taus)):.4f}"
        )

    # Hybrid I_star: load beats heat
    for t_star in (1.36, 1.44, 1.52, 1.60):
        # 1.52 may not be in steps_list — check neighbors
        pass
    assert d_hl_by_t[1.36] > 0.0, "load should beat heat at t=1.36"
    assert d_hl_by_t[1.60] > 0.0, "load should beat heat at t=1.60"
    assert d_hl_by_t[1.20] < 0.05  # may be negative (load lag)

    out = HERE / "t1_load_m2_envelope.txt"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("WROTE", out)
    return out


if __name__ == "__main__":
    main()
