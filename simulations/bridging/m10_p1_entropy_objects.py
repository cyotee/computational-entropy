#!/usr/bin/env python3
"""
M10 P1 — empirical non-identity of entropy objects on the 1D dual toy.

Compares, under the standard noisy-step observation model:
  - H_c^toy  = residual-channel score (dual): H_R + λ_e H_edge
  - H(Z)     = Shannon entropy of a *declared coarsened* reconstructor
               observable Z under the MC noise ensemble (unsupervised)
  - R        = residual MSE (not an entropy; contrast only)

Times are on / near the unified pure residual window U_star = [1.36, 2.40]
(DT = 0.08 ⇒ step counts 17, 20, 25 for t ∈ {1.36, 1.60, 2.00}).

Rigor: hybrid-experimental. Not S_c, not continuum, not gravity.

Run:
  .venv/bin/python simulations/bridging/m10_p1_entropy_objects.py
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _joint_toy_v2_core as toy  # noqa: E402

# --- experiment defaults (runtime-conscious) ---
N_MC = 80
SEED0 = 20260715
# U_star-adjacent times: t = n_steps * DT
TARGET_TIMES = (1.36, 1.60, 2.00)
MODES = ("heat", "pm")
N_EDGE_BINS = 8  # coarsening for multi-bin Z
# equality tolerance: objects live on different scales; still assert |a-b| > tol
ABS_EQ_TOL = 1e-3


def steps_for_time(t: float, dt: float = toy.DT) -> int:
    """Nearest integer step count for target lab time t."""
    return int(round(t / dt))


def shannon_empirical(labels: Sequence[int], n_states: int, base: float = 2.0) -> float:
    """Shannon entropy (bits if base=2) of empirical categorical distribution."""
    if len(labels) == 0:
        return 0.0
    counts = np.bincount(np.asarray(labels, dtype=int), minlength=n_states).astype(float)
    p = counts / counts.sum()
    nz = p[p > 0.0]
    return float(-np.sum(nz * np.log(nz) / np.log(base)))


def Z_binary_edge(phi_hat: np.ndarray, e_star: int | None = None) -> int:
    """
    Binary coarsened edge-location observable.

    Z = 1 iff argmax_i |∇φ̂|_i is on the true-edge side of the midpoint of the
    edge index set (or ≥ e_star if provided); else 0.

    This is a map from reconstructor field → {0,1}, independent of φ_star
    values except for the fixed geometric threshold e_star (structural label).
    """
    g = np.abs(toy.gradients(phi_hat))
    e = int(np.argmax(g))
    if e_star is None:
        e_star = toy.N // 2 - 1
    return 1 if e >= e_star else 0


def Z_edge_bin(phi_hat: np.ndarray, n_bins: int = N_EDGE_BINS) -> int:
    """
    Multi-bin coarsened edge location: argmax |∇φ̂| quantized into n_bins
    equal partitions of the N-1 edge slots. Range {0,...,n_bins-1}.
    """
    g = np.abs(toy.gradients(phi_hat))
    e = int(np.argmax(g))
    n_edges = len(g)
    # floor partition; last bin absorbs remainder
    bin_w = max(n_edges // n_bins, 1)
    z = min(e // bin_w, n_bins - 1)
    return int(z)


def evolve_to_targets(
    y: np.ndarray,
    mode: str,
    target_steps: Sequence[int],
    dt: float = toy.DT,
    K: float = toy.K_PM,
) -> Dict[int, np.ndarray]:
    """Euler-integrate reconstructor; return φ̂ at each requested step count."""
    phi = y.astype(float).copy()
    want = set(int(s) for s in target_steps)
    max_s = max(want)
    out: Dict[int, np.ndarray] = {}
    if 0 in want:
        out[0] = phi.copy()
    if mode == "heat":
        rhs = toy.rhs_heat
    elif mode == "pm":
        rhs = lambda p, _K=K: toy.rhs_pm(p, _K)
    else:
        raise ValueError(mode)
    for k in range(1, max_s + 1):
        phi = toy.step_euler(phi, rhs, dt)
        if k in want:
            out[k] = phi.copy()
    return out


def run_mc(
    n_mc: int = N_MC,
    seed0: int = SEED0,
    times: Sequence[float] = TARGET_TIMES,
) -> Tuple[List[dict], dict]:
    """
    Monte Carlo over observation noise seeds.

    For each (t, mode) return mean H_c^toy, mean R, and ensemble H(Z) for
    binary and multi-bin edge-location observables.
    """
    star = toy.phi_star_step()
    e_star = toy.N // 2 - 1
    sigma = toy.NOISE_SIGMA
    dt = toy.DT
    target_steps = [steps_for_time(t, dt) for t in times]
    # align reported times to actual grid
    actual_times = [s * dt for s in target_steps]

    # Accumulators: key = (step, mode)
    Hc_lists: Dict[Tuple[int, str], List[float]] = {}
    R_lists: Dict[Tuple[int, str], List[float]] = {}
    Zbin_lists: Dict[Tuple[int, str], List[int]] = {}
    Zmulti_lists: Dict[Tuple[int, str], List[int]] = {}
    for s in target_steps:
        for m in MODES:
            Hc_lists[(s, m)] = []
            R_lists[(s, m)] = []
            Zbin_lists[(s, m)] = []
            Zmulti_lists[(s, m)] = []

    rng = np.random.default_rng(seed0)
    for _ in range(n_mc):
        y = star + sigma * rng.standard_normal(toy.N)
        for mode in MODES:
            snaps = evolve_to_targets(y, mode, target_steps, dt=dt)
            for s in target_steps:
                phi = snaps[s]
                Hc_lists[(s, mode)].append(float(toy.H_c_channel(phi, star)))
                R_lists[(s, mode)].append(float(toy.residual_mse(phi, star)))
                Zbin_lists[(s, mode)].append(Z_binary_edge(phi, e_star=e_star))
                Zmulti_lists[(s, mode)].append(Z_edge_bin(phi, n_bins=N_EDGE_BINS))

    rows: List[dict] = []
    for t_rep, s in zip(actual_times, target_steps):
        for mode in MODES:
            Hc = np.asarray(Hc_lists[(s, mode)], dtype=float)
            R = np.asarray(R_lists[(s, mode)], dtype=float)
            z_bin = Zbin_lists[(s, mode)]
            z_multi = Zmulti_lists[(s, mode)]
            H_Z_bin = shannon_empirical(z_bin, n_states=2)
            H_Z_multi = shannon_empirical(z_multi, n_states=N_EDGE_BINS)
            rows.append(
                {
                    "t": t_rep,
                    "steps": s,
                    "mode": mode,
                    "H_c_toy_mean": float(Hc.mean()),
                    "H_c_toy_std": float(Hc.std(ddof=1)) if n_mc > 1 else 0.0,
                    "H_Z_binary": H_Z_bin,
                    "H_Z_edgebin": H_Z_multi,
                    "R_mean": float(R.mean()),
                    "R_std": float(R.std(ddof=1)) if n_mc > 1 else 0.0,
                    "frac_Zbin_1": float(np.mean(np.asarray(z_bin) == 1)),
                }
            )

    meta = {
        "n_mc": n_mc,
        "seed0": seed0,
        "N": toy.N,
        "sigma": sigma,
        "dt": dt,
        "K_PM": toy.K_PM,
        "lambda_e": toy.LAMBDA_E,
        "n_edge_bins": N_EDGE_BINS,
        "target_times_requested": list(times),
        "actual_times": actual_times,
        "target_steps": target_steps,
        "U_star": [1.36, 2.40],
        "formulas": {
            "H_c_toy": "H_R + λ_e H_edge; H_R=log(1+R/σ_ref²), R=MSE(φ̂,φ★); "
            "H_edge=soft Shannon of p∝|∇φ̂| (per realization; table reports MC mean)",
            "H_Z_binary": "H(Z) bits, Z=1{argmax|∇φ̂| ≥ e★}, e★=N//2-1; ensemble Shannon",
            "H_Z_edgebin": f"H(Z) bits, Z=bin(argmax|∇φ̂|) in {N_EDGE_BINS} equal edge bins; ensemble Shannon",
            "R": "mean_i (φ̂_i - φ★_i)² (not entropy)",
        },
    }
    return rows, meta


def print_table(rows: List[dict], meta: dict) -> None:
    print("M10 P1 — entropy object comparison (1D noisy_step dual)")
    print(
        f"N_MC={meta['n_mc']} seed0={meta['seed0']} N={meta['N']} "
        f"σ={meta['sigma']} dt={meta['dt']} K={meta['K_PM']} λ_e={meta['lambda_e']}"
    )
    print(f"U_star≈{meta['U_star']}; times on grid: {meta['actual_times']}")
    print()
    print(meta["formulas"]["H_c_toy"])
    print(meta["formulas"]["H_Z_binary"])
    print(meta["formulas"]["H_Z_edgebin"])
    print(meta["formulas"]["R"])
    print()
    hdr = (
        f"{'t':>6} {'dyn':>6} {'H_c_toy':>10} {'±':>6} "
        f"{'H(Z_bin)':>10} {'H(Z_8)':>8} {'R':>10} {'±':>6}  notes"
    )
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        notes = []
        # same-scale non-identity vs both coarsenings
        if abs(r["H_c_toy_mean"] - r["H_Z_binary"]) > ABS_EQ_TOL:
            notes.append("≠Zbin")
        if abs(r["H_c_toy_mean"] - r["H_Z_edgebin"]) > ABS_EQ_TOL:
            notes.append("≠Z8")
        # residual dual hint (PM better residual)
        if r["mode"] == "pm":
            heat = next(
                x for x in rows if x["t"] == r["t"] and x["mode"] == "heat"
            )
            if r["R_mean"] < heat["R_mean"]:
                notes.append("R_pm<R_h")
        note_s = ",".join(notes) if notes else "—"
        print(
            f"{r['t']:6.2f} {r['mode']:>6} {r['H_c_toy_mean']:10.4f} "
            f"{r['H_c_toy_std']:6.3f} {r['H_Z_binary']:10.4f} "
            f"{r['H_Z_edgebin']:8.4f} {r['R_mean']:10.5f} {r['R_std']:6.4f}  {note_s}"
        )


def assert_non_identity(rows: List[dict]) -> None:
    """
    Conclude H_c^toy and H(Z) are not numerically identical in general.

    Checks:
      1. For every row, |mean H_c^toy - H(Z)| > tol for both coarsenings.
      2. At least one (t, mode pair) where dual residual ordering holds
         (PM R < heat R) — sanity that we sit on the dual window.
    """
    diffs_bin = []
    diffs_multi = []
    for r in rows:
        d_bin = abs(r["H_c_toy_mean"] - r["H_Z_binary"])
        d_multi = abs(r["H_c_toy_mean"] - r["H_Z_edgebin"])
        diffs_bin.append(d_bin)
        diffs_multi.append(d_multi)
        assert d_bin > ABS_EQ_TOL, (
            f"unexpected near-identity H_c^toy ≈ H(Z_bin) at t={r['t']} mode={r['mode']}: "
            f"{r['H_c_toy_mean']} vs {r['H_Z_binary']}"
        )
        assert d_multi > ABS_EQ_TOL, (
            f"unexpected near-identity H_c^toy ≈ H(Z_8) at t={r['t']} mode={r['mode']}: "
            f"{r['H_c_toy_mean']} vs {r['H_Z_edgebin']}"
        )

    # Sanity: residual dual pattern on at least one U_star time
    residual_pm_better = False
    for t in sorted({r["t"] for r in rows}):
        heat = next(r for r in rows if r["t"] == t and r["mode"] == "heat")
        pm = next(r for r in rows if r["t"] == t and r["mode"] == "pm")
        if pm["R_mean"] < heat["R_mean"]:
            residual_pm_better = True
            break
    assert residual_pm_better, (
        "expected PM mean residual < heat on at least one U_star-adjacent time "
        "(check dual setup / seeds)"
    )

    print()
    print(
        f"ASSERT non-identity: min |H_c^toy - H(Z_bin)| = {min(diffs_bin):.4f} > {ABS_EQ_TOL}"
    )
    print(
        f"ASSERT non-identity: min |H_c^toy - H(Z_8)|   = {min(diffs_multi):.4f} > {ABS_EQ_TOL}"
    )
    print(
        "CONCLUSION: H_c^toy (supervised residual+edge score, MC-averaged) is not "
        "numerically identical to ensemble Shannon H(Z) of coarsened edge-location "
        "observables of φ̂. Objects differ in definition and in measured values."
    )
    print(
        "Non-claims: not S_c, not continuum GfE, not gravity; not a proof that "
        "H(Z) never co-moves with H_c^toy (ordering/correlation left open)."
    )


def format_results_text(rows: List[dict], meta: dict) -> str:
    """Plain-text dump for synthesis note / regression."""
    lines = [
        "M10 P1 entropy object comparison",
        f"N_MC={meta['n_mc']} seed0={meta['seed0']} N={meta['N']} "
        f"sigma={meta['sigma']} dt={meta['dt']} K={meta['K_PM']} lambda_e={meta['lambda_e']}",
        f"actual_times={meta['actual_times']} steps={meta['target_steps']}",
        f"n_edge_bins={meta['n_edge_bins']}",
        "",
        "t mode H_c_toy_mean H_c_toy_std H_Z_binary H_Z_edgebin R_mean R_std frac_Zbin_1",
    ]
    for r in rows:
        lines.append(
            f"{r['t']:.2f} {r['mode']} {r['H_c_toy_mean']:.6f} {r['H_c_toy_std']:.6f} "
            f"{r['H_Z_binary']:.6f} {r['H_Z_edgebin']:.6f} "
            f"{r['R_mean']:.6f} {r['R_std']:.6f} {r['frac_Zbin_1']:.4f}"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    rows, meta = run_mc(n_mc=N_MC, seed0=SEED0, times=TARGET_TIMES)
    print_table(rows, meta)
    assert_non_identity(rows)
    out = HERE / "m10_p1_results.txt"
    out.write_text(format_results_text(rows, meta))
    print()
    print("WROTE", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
