"""
Lattice blur / noise split + Δ_noise envelope for M1c (T1′ analytic t_min).

Also records height-decay rates for C′2♯ cross-check.

Run:  .venv/bin/python simulations/bridging/test_t1_delta_noise.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402


def _res(a: np.ndarray, b: np.ndarray | None = None) -> float:
    if b is None:
        b = np.zeros_like(a)
    return float(np.mean((a - b) ** 2))


def main(n_mc: int = 200, seed: int = 7) -> Path:
    rng = np.random.default_rng(seed)
    K, sigma, dt, N = toy.K_PM, toy.NOISE_SIGMA, toy.DT, toy.N
    e_star = N // 2 - 1
    star = toy.phi_star_step()
    steps_list = [5, 10, 15, 20, 30, 40, 60, 80]

    H_init, H_floor = 0.80, 0.25
    rate_worst = K + 2 * (K**2 / H_floor)
    T_sharp = (H_init - H_floor) / rate_worst
    T_crude = 0.5 / (4 * (K / 2 + 2 * K**2 / 0.5))

    lines = [
        f"N_MC={n_mc} seed={seed} sigma={sigma} K={K} dt={dt} N={N}",
        f"analytic_C2_crude_T_pers={T_crude:.4f}",
        (
            f"analytic_C2sharp_Hinit={H_init} Hfloor={H_floor} "
            f"rate_worst={rate_worst:.4f} T_pers_sharp={T_sharp:.4f}"
        ),
    ]

    H0s = []
    for _ in range(2000):
        y = star + sigma * rng.standard_normal(N)
        H0s.append(abs(toy.gradients(y)[e_star]))
    H0s = np.asarray(H0s, dtype=float)
    for thr in (0.5, 0.7, 0.8, 0.85, 0.9):
        lines.append(f"P_H0_ge_{thr}={float(np.mean(H0s >= thr)):.4f}")

    lines.append(
        "t Rblur Rnoise_heat Rh Rp mean_dR frac_pm_better "
        "Delta_noise_proxy mean_dHdt mean_Hend "
        "frac_H_ge_0.5 frac_H_ge_0.25 c_D_est"
    )

    dR_by_t: dict[float, float] = {}
    for n_steps in steps_list:
        t = n_steps * dt
        Rblur_l, Rnh_l, Rh_l, Rp_l, dR_l = [], [], [], [], []
        dHdt_l, Hend_l, ok05_l, ok25_l = [], [], [], []
        for _ in range(n_mc):
            noise = sigma * rng.standard_normal(N)
            y = star + noise
            rh = toy.run_dynamics(
                y, star, mode="heat", n_steps=n_steps, snapshot_every=n_steps
            )
            rp = toy.run_dynamics(
                y, star, mode="pm", n_steps=n_steps, snapshot_every=n_steps
            )
            Rh_l.append(rh["residual"][-1])
            Rp_l.append(rp["residual"][-1])
            dR_l.append(Rh_l[-1] - Rp_l[-1])

            phi = star.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, toy.rhs_heat, dt)
            Rblur_l.append(_res(phi, star))

            phi = noise.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, toy.rhs_heat, dt)
            Rnh_l.append(_res(phi, np.zeros(N)))

            phi = y.copy()
            H0 = abs(toy.gradients(phi)[e_star])
            ok05 = ok25 = True
            for __ in range(n_steps):
                phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
                h = abs(toy.gradients(phi)[e_star])
                if h < 0.5:
                    ok05 = False
                if h < 0.25:
                    ok25 = False
            H1 = abs(toy.gradients(phi)[e_star])
            Hend_l.append(H1)
            dHdt_l.append((H0 - H1) / t)
            ok05_l.append(ok05)
            ok25_l.append(ok25)

        Rblur = float(np.mean(Rblur_l))
        Rnh = float(np.mean(Rnh_l))
        Rh = float(np.mean(Rh_l))
        Rp = float(np.mean(Rp_l))
        dR_m = float(np.mean(dR_l))
        dR_by_t[t] = dR_m
        Delta = Rp - Rnh
        cD = Rblur * N / np.sqrt(t)
        lines.append(
            f"{t:.2f} {Rblur:.6f} {Rnh:.6f} {Rh:.6f} {Rp:.6f} {dR_m:+.6f} "
            f"{float(np.mean(np.asarray(dR_l) > 0)):.4f} {Delta:.6f} "
            f"{float(np.mean(dHdt_l)):.4f} {float(np.mean(Hend_l)):.4f} "
            f"{float(np.mean(ok05_l)):.4f} {float(np.mean(ok25_l)):.4f} {cD:.4f}"
        )

    # Sanity aligned with T1′ story
    assert float(np.mean(H0s >= 0.5)) > 0.9
    assert dR_by_t[0.40] < 0.0, "ultra-short: heat should win residual"
    assert dR_by_t[1.60] > 0.0, "intermediate: PM should win residual"
    assert dR_by_t[6.40] > 0.0
    assert T_sharp + 1e-12 >= 1.2, "C′2♯ should cover empirical t_min~1.2"

    out = HERE / "t1_delta_noise_envelope.txt"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("WROTE", out)
    return out


if __name__ == "__main__":
    main()
