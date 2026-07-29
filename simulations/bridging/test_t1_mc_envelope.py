"""
Drive the real joint-toy reconstructor (not a mock) and write residual-domination
envelope evidence for M1 / Proposition T1′.

Run:  .venv/bin/python simulations/bridging/test_t1_mc_envelope.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402


def main(n_mc: int = 200, seed: int = 1) -> Path:
    """Canonical witness: N_MC=200, times through t=6.40 (matches m1-lemma-c-prime.md)."""
    rng = np.random.default_rng(seed)
    star = toy.phi_star_step()
    e_star = toy.N // 2 - 1
    K, sigma, dt = toy.K_PM, toy.NOISE_SIGMA, toy.DT
    # Must stay aligned with synthesis/m1-lemma-c-prime.md residual table
    steps_list = [5, 10, 20, 40, 80]
    res = {n: [] for n in steps_list}
    persist = {n: [] for n in steps_list}
    argmax_ok = thr_ok = 0

    for _ in range(n_mc):
        y = star + sigma * rng.standard_normal(toy.N)
        g0 = np.abs(toy.gradients(y))
        if int(np.argmax(g0)) == e_star:
            argmax_ok += 1
        if g0[e_star] >= 0.5:
            thr_ok += 1
        for n_steps in steps_list:
            r_pm = toy.run_dynamics(
                y, star, mode="pm", n_steps=n_steps, snapshot_every=max(1, n_steps // 4)
            )
            r_h = toy.run_dynamics(
                y, star, mode="heat", n_steps=n_steps, snapshot_every=max(1, n_steps // 4)
            )
            res[n_steps].append(float(r_h["residual"][-1] - r_pm["residual"][-1]))
            phi = y.copy()
            ok = True
            for _k in range(n_steps):
                phi = toy.step_euler(phi, lambda p: toy.rhs_pm(p, K), dt)
                if abs(toy.gradients(phi)[e_star]) < 0.5:
                    ok = False
                    break
            persist[n_steps].append(ok)

    lines = [
        f"N_MC={n_mc} sigma={sigma} K={K} dt={dt} N={toy.N}",
        f"C1_prime_argmax_true_frac={argmax_ok / n_mc:.4f}",
        f"C1_prime_true_height_ge_0.5_frac={thr_ok / n_mc:.4f}",
    ]
    for n in steps_list:
        d = np.asarray(res[n], dtype=float)
        p = np.asarray(persist[n], dtype=float)
        lines.append(
            f"steps={n} t={n * dt:.2f} mean_Rheat_minus_Rpm={d.mean():.6f} "
            f"frac_pm_better={np.mean(d > 0):.4f} persist_ge_0.5={p.mean():.4f}"
        )
    # Sanity: intermediate window PM beats heat; ultra-short may not
    assert argmax_ok / n_mc > 0.9
    assert thr_ok / n_mc > 0.9
    assert float(np.mean(res[40])) > 0.0, "expected PM residual better than heat by t=3.2"
    assert float(np.mean(res[80])) > 0.0, "expected PM residual better than heat by t=6.4"
    assert float(np.mean(persist[40])) > 0.9
    assert float(np.mean(persist[80])) > 0.9

    out = HERE / "t1_mc_envelope.txt"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print("WROTE", out)
    return out


if __name__ == "__main__":
    main()
