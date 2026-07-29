"""
M1g witness: unified pure residual dual window U_star with rho_b=0.42.

Run:  .venv/bin/python simulations/bridging/test_t1_unified_pure.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402


def main(n_mc: int = 400, seed: int = 17) -> Path:
    rng = np.random.default_rng(seed)
    K, sigma, dt, N = toy.K_PM, toy.NOISE_SIGMA, toy.DT, toy.N
    star = toy.phi_star_step()
    rho_b = 0.42
    h_floor = 0.25

    A = np.zeros((N, N))
    for i in range(N):
        e = np.zeros(N)
        e[i] = 1.0
        A[:, i] = toy.rhs_heat(e)
    evals = np.linalg.eigvalsh(A)

    def Rn(t: float, rho: float = 1.0) -> float:
        return float((sigma**2 / N) * np.sum(np.exp(2 * t * rho * evals)))

    def Rblur(n_steps: int) -> float:
        phi = star.astype(float).copy()
        for _ in range(n_steps):
            phi = toy.step_euler(phi, toy.rhs_heat, dt)
        return float(np.mean((phi - star) ** 2))

    def rint(t: float) -> float:
        return 2.0 * (K**2 * t / h_floor) ** 2 / N

    # U_star grid (includes I_star and late pure)
    steps_u = [17, 18, 19, 20, 25, 30]  # 1.36 .. 2.40
    steps_all = [15, 16] + steps_u  # also report 1.20, 1.28

    lines = [
        f"N_MC={n_mc} seed={seed} sigma={sigma} K={K} dt={dt} N={N} rho_b={rho_b}",
        "t R_PM_noise Rn_b PCRH_margin Rblur Delta_maj pure_margin "
        "mean_dR_full frac_pm_better in_U_star",
    ]

    pure_ok = True
    for n_steps in steps_all:
        t = n_steps * dt
        in_u = n_steps in steps_u
        rpm, dR = [], []
        for _ in range(n_mc):
            noise = sigma * rng.standard_normal(N)
            phi = noise.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
            rpm.append(float(np.mean(phi**2)))

            y = star + noise
            pp = y.copy()
            for __ in range(n_steps):
                pp = toy.step_euler(pp, lambda p: toy.rhs_pm(p, K), dt)
            ph = y.copy()
            for __ in range(n_steps):
                ph = toy.step_euler(ph, toy.rhs_heat, dt)
            dR.append(
                float(np.mean((ph - star) ** 2) - np.mean((pp - star) ** 2))
            )

        rm = float(np.mean(rpm))
        rnb = Rn(t, rho_b)
        rn = Rn(t, 1.0)
        rb = Rblur(n_steps)
        dmaj = rnb - rn + rint(t)
        pcrh_m = rnb - rm
        pure_m = rb - dmaj
        if in_u:
            if pcrh_m < 0 or pure_m < 0:
                pure_ok = False
            if float(np.mean(np.asarray(dR) > 0)) < 0.8:
                pure_ok = False
        lines.append(
            f"{t:.2f} {rm:.6f} {rnb:.6f} {pcrh_m:+.6f} {rb:.6f} {dmaj:.6f} "
            f"{pure_m:+.6f} {float(np.mean(dR)):+.6f} "
            f"{float(np.mean(np.asarray(dR) > 0)):.4f} {int(in_u)}"
        )

    assert pure_ok, "unified pure window U_star failed PCRH or maj or dual"
    # Explicit checks at anchors
    assert Rblur(17) >= Rn(1.36, rho_b) - Rn(1.36) + rint(1.36) - 1e-6
    assert Rblur(20) >= Rn(1.60, rho_b) - Rn(1.60) + rint(1.60) - 1e-6

    out = HERE / "t1_unified_pure_envelope.txt"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("WROTE", out)
    return out


if __name__ == "__main__":
    main()
