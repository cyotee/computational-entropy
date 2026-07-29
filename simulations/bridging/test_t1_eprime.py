"""
Lemma E′ witness: exact heat blur, Δ_noise, residual domination on analytic T1′ window.

Run:  .venv/bin/python simulations/bridging/test_t1_eprime.py
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


def _heat(phi0: np.ndarray, n_steps: int, dt: float) -> np.ndarray:
    phi = phi0.astype(float).copy()
    for _ in range(n_steps):
        phi = toy.step_euler(phi, toy.rhs_heat, dt)
    return phi


def _pm(phi0: np.ndarray, n_steps: int, dt: float, K: float) -> np.ndarray:
    phi = phi0.astype(float).copy()
    for _ in range(n_steps):
        phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
    return phi


def _heat_neumann_halves(y: np.ndarray, n_steps: int, dt: float, i_star: int) -> np.ndarray:
    left = y[:i_star].astype(float).copy()
    right = y[i_star:].astype(float).copy()

    def step_seg(seg: np.ndarray) -> np.ndarray:
        if len(seg) < 2:
            return seg
        g = np.diff(seg)
        dphi = np.zeros(len(seg))
        dphi[0] = g[0]
        dphi[1:-1] = g[1:] - g[:-1]
        dphi[-1] = -g[-1]
        return seg + dt * dphi

    for _ in range(n_steps):
        left = step_seg(left)
        right = step_seg(right)
    return np.concatenate([left, right])


def main(n_mc: int = 300, seed: int = 11) -> Path:
    rng = np.random.default_rng(seed)
    K, sigma, dt, N = toy.K_PM, toy.NOISE_SIGMA, toy.DT, toy.N
    i_star = N // 2
    H_init, H_floor = 0.80, 0.25
    star = toy.phi_star_step()
    rate_worst = K + 2 * (K**2 / H_floor)
    T_sharp = (H_init - H_floor) / rate_worst

    # Grid covering analytic window neighbors
    steps_list = list(range(12, 23))  # t = 0.96 .. 1.76

    lines = [
        f"N_MC={n_mc} seed={seed} sigma={sigma} K={K} dt={dt} N={N} H_floor={H_floor}",
        f"T_pers_sharp={T_sharp:.4f}",
        (
            "n t Rblur Rnoise_h Rh Rp Rneu mean_dR frac_pm_better "
            "Delta_noise R_int_major margin_blur_minus_Delta "
            "margin_vs_neu_int E_R_PM_minus_Rneu"
        ),
    ]

    def r_int(t: float, c_sp: float = 2.0) -> float:
        mu = t * (K**2 / H_floor)
        return c_sp * mu**2 / N

    dR_by_t: dict[float, float] = {}
    margin_by_t: dict[float, float] = {}

    for n_steps in steps_list:
        t = n_steps * dt
        rblur = _res(_heat(star, n_steps, dt), star)
        rnh_l, rh_l, rp_l, rneu_l, dr_l, gap_l = [], [], [], [], [], []
        for _ in range(n_mc):
            noise = sigma * rng.standard_normal(N)
            y = star + noise
            rnh_l.append(_res(_heat(noise, n_steps, dt), np.zeros(N)))
            yh = _heat(y, n_steps, dt)
            yp = _pm(y, n_steps, dt, K)
            yn = _heat_neumann_halves(y, n_steps, dt, i_star)
            rh_l.append(_res(yh, star))
            rp_l.append(_res(yp, star))
            rneu_l.append(_res(yn, star))
            dr_l.append(rh_l[-1] - rp_l[-1])
            gap_l.append(rp_l[-1] - rneu_l[-1])

        rnh = float(np.mean(rnh_l))
        rh = float(np.mean(rh_l))
        rp = float(np.mean(rp_l))
        rneu = float(np.mean(rneu_l))
        dr = float(np.mean(dr_l))
        delta = rp - rnh
        ri = r_int(t)
        margin = rblur - delta
        margin_arch = rblur - (rneu - rnh) - ri
        gap = float(np.mean(gap_l))
        dR_by_t[t] = dr
        margin_by_t[t] = margin
        lines.append(
            f"{n_steps} {t:.2f} {rblur:.6f} {rnh:.6f} {rh:.6f} {rp:.6f} {rneu:.6f} "
            f"{dr:+.6f} {float(np.mean(np.asarray(dr_l) > 0)):.4f} {delta:.6f} {ri:.6f} "
            f"{margin:+.6f} {margin_arch:+.6f} {gap:+.6f}"
        )

    # Sanity: hybrid I_star domination
    for t_star in (1.36, 1.44, 1.52, 1.60):
        assert dR_by_t[t_star] > 0.0, f"expected PM better at t={t_star}"
        assert margin_by_t[t_star] > 0.0, f"expected blur >= Delta_noise at t={t_star}"
    # Ultra-short still heat-favored (T1′ windowing)
    assert dR_by_t[0.96] < 0.0
    # Comfortable margin at t=1.60
    assert margin_by_t[1.60] > 5e-4
    assert T_sharp + 1e-12 >= 1.60

    out = HERE / "t1_eprime_envelope.txt"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("WROTE", out)
    return out


if __name__ == "__main__":
    main()
