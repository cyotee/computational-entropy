"""
M1f witness: Gaussian rho_eff, pure majorant vs blur, rho_ew(t) under PM, residual dual at t>=2.

Run:  .venv/bin/python simulations/bridging/test_t1_pure_hrho.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402


def _build_A(n: int) -> np.ndarray:
    A = np.zeros((n, n))
    for i in range(n):
        e = np.zeros(n)
        e[i] = 1.0
        A[:, i] = toy.rhs_heat(e)
    return A


def main(n_mc: int = 150, seed: int = 9) -> Path:
    rng = np.random.default_rng(seed)
    K, sigma, dt, N = toy.K_PM, toy.NOISE_SIGMA, toy.DT, toy.N
    star = toy.phi_star_step()
    A = _build_A(N)
    evals = np.linalg.eigvalsh(A)

    def Rn(t: float, rho: float = 1.0) -> float:
        return float((sigma**2 / N) * np.sum(np.exp(2 * t * rho * evals)))

    def Rblur(n_steps: int) -> float:
        phi = star.astype(float).copy()
        for _ in range(n_steps):
            phi = toy.step_euler(phi, toy.rhs_heat, dt)
        return float(np.mean((phi - star) ** 2))

    def rint(t: float, h_floor: float = 0.25) -> float:
        return 2.0 * (K**2 * t / h_floor) ** 2 / N

    # Full-field rho_star at t=0
    n_samp = 400
    num = den = 0.0
    for _ in range(n_samp):
        eta = sigma * rng.standard_normal(N)
        g = toy.gradients(eta)
        f = g**2 / (1.0 + (g / K) ** 2)
        num += float(np.sum(f))
        den += float(np.sum(g**2))
    rho_star = num / den

    lines = [
        f"N_MC={n_mc} seed={seed} sigma={sigma} K={K} dt={dt} N={N}",
        f"rho_star_full_field={rho_star:.6f}",
        "t Rblur Rn Rn_rho Delta_maj pass_maj mean_R_PM_noise mean_R_heat_noise "
        "PCRH_ok mean_rho_ew mean_dR_full frac_pm_better",
    ]

    # rho_ew along pure-noise PM
    def rho_ew(phi: np.ndarray) -> float:
        g = toy.gradients(phi)
        w = g**2
        s = float(np.sum(w))
        if s < 1e-15:
            return 1.0
        rho = 1.0 / (1.0 + (g / K) ** 2)
        return float(np.sum(rho * w) / s)

    steps_list = [15, 17, 20, 25, 30, 35, 40]
    pcrh_ok_all = True
    pure_pass = False
    for n_steps in steps_list:
        t = n_steps * dt
        rb = Rblur(n_steps)
        rn = Rn(t, 1.0)
        rn_r = Rn(t, rho_star)
        dmaj = rn_r - rn + rint(t)
        pass_maj = rb >= dmaj

        r_pm_n, r_h_n, rews, dR = [], [], [], []
        for _ in range(n_mc):
            noise = sigma * rng.standard_normal(N)
            # pure noise PM / heat
            phi = noise.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
            r_pm_n.append(float(np.mean(phi**2)))
            rews.append(rho_ew(phi))
            phi = noise.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, toy.rhs_heat, dt)
            r_h_n.append(float(np.mean(phi**2)))
            # full jump problem
            y = star + noise
            phi = y.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
            rp = float(np.mean((phi - star) ** 2))
            phi = y.copy()
            for __ in range(n_steps):
                phi = toy.step_euler(phi, toy.rhs_heat, dt)
            rh = float(np.mean((phi - star) ** 2))
            dR.append(rh - rp)

        mean_pm = float(np.mean(r_pm_n))
        mean_h = float(np.mean(r_h_n))
        pcrh = mean_pm <= rn_r + 1e-4
        pcrh_ok_all = pcrh_ok_all and pcrh
        if pass_maj and t >= 2.0 - 1e-12:
            pure_pass = True
        lines.append(
            f"{t:.2f} {rb:.6f} {rn:.6f} {rn_r:.6f} {dmaj:.6f} {int(pass_maj)} "
            f"{mean_pm:.6f} {mean_h:.6f} {int(pcrh)} {float(np.mean(rews)):.4f} "
            f"{float(np.mean(dR)):+.6f} {float(np.mean(np.asarray(dR) > 0)):.4f}"
        )

    # Assertions
    assert 0.25 < rho_star < 0.35, f"unexpected rho_star={rho_star}"
    assert pcrh_ok_all, "PCRH failed: PM noise residual exceeded R_n(rho_star)"
    assert pure_pass, "expected pure majorant pass for some t>=2"
    # residual dual at t=2.0
    # find line with t=2.0
    assert Rblur(25) >= Rn(2.0, rho_star) - Rn(2.0) + rint(2.0) - 1e-6

    out = HERE / "t1_pure_hrho_envelope.txt"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("WROTE", out)
    return out


if __name__ == "__main__":
    main()
