"""
Joint toy 2D — Euclidean ACD-EW lift (image / grid).

Same dual as 1D: observation channel residual + load clock vs PM/GfE warm-up.
CLI:  .venv/bin/python simulations/bridging/_joint_toy_2d.py
"""
from __future__ import annotations

import numpy as np
from pathlib import Path

# Grid
N = 48
ALPHA_G = 1.0
K_PM = 0.28          # larger K → less edge freeze / less staircasing instability
ALPHA_L = 2.0
C_E, C_S, C_B = 1.0, 1.0, 0.5
DT = 0.04            # CFL-safe for explicit anisotropic diffusion
N_STEPS = 120
SNAPSHOT_EVERY = 15
NOISE_SIGMA = 0.10
LAMBDA_E = 0.1
DIFF_SCALE = 0.35    # global diffusivity scale (stability)


def gradients(phi: np.ndarray):
    """Forward differences; returns gx, gy of shape (N, N-1) and (N-1, N) — use padded versions."""
    gx = np.diff(phi, axis=1)  # (N, N-1)
    gy = np.diff(phi, axis=0)  # (N-1, N)
    return gx, gy


def grad_energy_map(phi: np.ndarray) -> np.ndarray:
    """Per-site |∇φ|² via average of incident edge grads (N, N)."""
    gx, gy = gradients(phi)
    ex = np.zeros_like(phi)
    ey = np.zeros_like(phi)
    ex[:, :-1] += gx**2
    ex[:, 1:] += gx**2
    ey[:-1, :] += gy**2
    ey[1:, :] += gy**2
    # each interior site touched by up to 4 edges; corners 2
    counts = np.ones_like(phi) * 2.0
    counts[1:-1, 1:-1] = 4.0
    counts[0, 1:-1] = counts[-1, 1:-1] = 3.0
    counts[1:-1, 0] = counts[1:-1, -1] = 3.0
    return (ex + ey) / counts


def mean_G_minus_1(phi: np.ndarray, alpha_g: float = ALPHA_G) -> float:
    e = grad_energy_map(phi)
    return float(np.mean(alpha_g * e))


def gfe_action(phi: np.ndarray, alpha_g: float = ALPHA_G) -> float:
    """S_GfE = -sum log(1 + alpha |grad|²) on edges."""
    gx, gy = gradients(phi)
    return float(-np.sum(np.log(1.0 + alpha_g * gx**2)) - np.sum(np.log(1.0 + alpha_g * gy**2)))


def residual_mse(phi_hat: np.ndarray, phi_star: np.ndarray) -> float:
    return float(np.mean((phi_hat - phi_star) ** 2))


def H_residual(phi_hat, phi_star, sigma_ref=None):
    if sigma_ref is None:
        sigma_ref = max(NOISE_SIGMA, 1e-3) ** 2
    R = residual_mse(phi_hat, phi_star)
    return float(np.log(1.0 + R / sigma_ref))


def H_edge_location(phi: np.ndarray, eps: float = 1e-12) -> float:
    e = np.sqrt(grad_energy_map(phi) + eps)
    p = e / e.sum()
    return float(-np.sum(p * np.log2(p + eps)))


def H_c_channel(phi_hat, phi_star, lambda_e=LAMBDA_E):
    return H_residual(phi_hat, phi_star) + lambda_e * H_edge_location(phi_hat)


def load_terms(phi_hat, phi_star, H_prev=None, dt=DT):
    e = grad_energy_map(phi_hat)
    L_E = C_E * float(np.mean(e))
    H = H_c_channel(phi_hat, phi_star)
    L_S = 0.0 if H_prev is None else C_S * abs(H - H_prev) / max(dt, 1e-12)
    gmax = float(np.sqrt(np.max(e)))
    L_B = C_B * gmax / (1.0 + gmax)
    return {
        "L_E": L_E,
        "L_S": L_S,
        "L_B": L_B,
        "L": L_E + L_S + L_B,
        "L_clock": L_E + L_S,
        "H_c": H,
        "residual": residual_mse(phi_hat, phi_star),
        "max_grad": gmax,
        "mean_G_minus_1": mean_G_minus_1(phi_hat),
    }


def _box_smooth(phi: np.ndarray, r: int = 1) -> np.ndarray:
    """Cheap separable box filter (Neumann via edge pad) for Catte regularization."""
    p = np.pad(phi, r, mode="edge")
    # cumulative sum for O(1) box
    c = np.cumsum(np.cumsum(p, axis=0), axis=1)
    c = np.pad(c, ((1, 0), (1, 0)), mode="constant")
    n = 2 * r + 1
    out = (
        c[n:, n:]
        - c[:-n, n:]
        - c[n:, :-n]
        + c[:-n, :-n]
    ) / (n * n)
    return out


def rhs_heat(phi: np.ndarray) -> np.ndarray:
    """5-point Laplacian with Neumann (copy edges)."""
    p = np.pad(phi, 1, mode="edge")
    return DIFF_SCALE * (p[1:-1, 2:] + p[1:-1, :-2] + p[2:, 1:-1] + p[:-2, 1:-1] - 4.0 * phi)


def rhs_pm(phi: np.ndarray, K: float = K_PM) -> np.ndarray:
    """
    Catte-regularized Perona–Malik: conductivity from smoothed field,
    flux from unsmoothed gradients — suppresses noise amplification.
    """
    smooth = _box_smooth(phi, r=1)
    gsx = np.diff(smooth, axis=1)
    gsy = np.diff(smooth, axis=0)
    rho_x = 1.0 / (1.0 + (gsx / max(K, 1e-8)) ** 2)
    rho_y = 1.0 / (1.0 + (gsy / max(K, 1e-8)) ** 2)
    gx = np.diff(phi, axis=1)
    gy = np.diff(phi, axis=0)
    flux_x = rho_x * gx  # gx = φ[j+1]-φ[j]; diffusion needs div(-ρ∇) or flipped assemble
    flux_y = rho_y * gy
    out = np.zeros_like(phi)
    # ∂t φ_j = ρ_{j-1}(φ_{j-1}-φ_j) + ρ_j(φ_{j+1}-φ_j) = flux_{j-1} wait:
    # with gx[j]=φ[j+1]-φ[j]:  out[j] = ρ_j gx[j] - ρ_{j-1} gx[j-1]
    out[:, :-1] += flux_x
    out[:, 1:] -= flux_x
    out[:-1, :] += flux_y
    out[1:, :] -= flux_y
    return DIFF_SCALE * out


def step_euler(phi, rhs, dt):
    return phi + dt * rhs(phi)


def run_dynamics(phi_init, phi_star, mode="pm", n_steps=N_STEPS, dt=DT, alpha_L=ALPHA_L, K=K_PM):
    phi = phi_init.astype(float).copy()
    terms = load_terms(phi, phi_star, H_prev=None, dt=dt)
    H_prev = terms["H_c"]
    hist = {
        "t": [0.0],
        "residual": [terms["residual"]],
        "H_c": [terms["H_c"]],
        "L_E": [terms["L_E"]],
        "L_clock": [terms["L_clock"]],
        "max_grad": [terms["max_grad"]],
        "mean_G_minus_1": [terms["mean_G_minus_1"]],
        "S_gfe": [gfe_action(phi)],
        "clock": [1.0],
        "phi": [phi.copy()],
    }
    t = 0.0
    for k in range(1, n_steps + 1):
        if mode == "heat":
            phi = step_euler(phi, rhs_heat, dt)
            clock = 1.0
        elif mode == "pm":
            phi = step_euler(phi, lambda p: rhs_pm(p, K), dt)
            clock = 1.0
        elif mode == "load_pm":
            terms_now = load_terms(phi, phi_star, H_prev=H_prev, dt=dt)
            clock = 1.0 / (1.0 + alpha_L * terms_now["L_clock"])
            phi = step_euler(phi, lambda p: rhs_pm(p, K), dt * clock)
        else:
            raise ValueError(mode)
        terms = load_terms(phi, phi_star, H_prev=H_prev, dt=dt)
        H_prev = terms["H_c"]
        t += dt
        if k % SNAPSHOT_EVERY == 0 or k == n_steps:
            hist["t"].append(t)
            hist["residual"].append(terms["residual"])
            hist["H_c"].append(terms["H_c"])
            hist["L_E"].append(terms["L_E"])
            hist["L_clock"].append(terms["L_clock"])
            hist["max_grad"].append(terms["max_grad"])
            hist["mean_G_minus_1"].append(terms["mean_G_minus_1"])
            hist["S_gfe"].append(gfe_action(phi))
            hist["clock"].append(clock if mode == "load_pm" else 1.0)
            hist["phi"].append(phi.copy())
    for key in hist:
        if key != "phi":
            hist[key] = np.asarray(hist[key], dtype=float)
    return hist


def phi_star_disk(n=N, r=0.22):
    yy, xx = np.mgrid[0:n, 0:n]
    cy = cx = (n - 1) / 2.0
    rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / n
    return (rr <= r).astype(float)


def phi_star_vertical_edge(n=N):
    phi = np.zeros((n, n))
    phi[:, n // 2 :] = 1.0
    return phi


def phi_star_smooth_blob(n=N):
    yy, xx = np.mgrid[0:n, 0:n]
    cy = cx = (n - 1) / 2.0
    rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / n
    return 0.5 + 0.5 * np.tanh((0.25 - rr) / 0.08)


def build_ics(noise_sigma=NOISE_SIGMA):
    specs = {
        "noisy_edge": {"star": phi_star_vertical_edge(), "sigma": noise_sigma, "seed": 201},
        "noisy_disk": {"star": phi_star_disk(), "sigma": noise_sigma, "seed": 202},
        "noisy_smooth": {"star": phi_star_smooth_blob(), "sigma": noise_sigma, "seed": 203},
        "clean_edge": {"star": phi_star_vertical_edge(), "sigma": 0.0, "seed": 204},
    }
    ics = {}
    for name, spec in specs.items():
        star = spec["star"].copy()
        sig = spec["sigma"]
        if sig == 0.0:
            y = star.copy()
        else:
            rng = np.random.default_rng(spec["seed"])
            y = star + sig * rng.standard_normal(star.shape)
        ics[name] = {"star": star, "y": y, "sigma": sig}
    return ics


def run_all(ics=None):
    if ics is None:
        ics = build_ics()
    modes = ["heat", "pm", "load_pm"]
    results = {}
    for name, pack in ics.items():
        results[name] = {}
        for mode in modes:
            results[name][mode] = run_dynamics(pack["y"], pack["star"], mode=mode)
    return ics, results


def evaluate(ics, results):
    modes = ["heat", "pm", "load_pm"]
    improv = {}
    for name, pack in ics.items():
        R0 = residual_mse(pack["y"], pack["star"])
        Rh = results[name]["heat"]["residual"][-1]
        Rp = results[name]["pm"]["residual"][-1]
        improv[name] = (Rh - Rp) / max(R0, 1e-12)

    edge_ratio = {}
    for name in ics:
        edge_ratio[name] = {}
        for mode in modes:
            r = results[name][mode]
            edge_ratio[name][mode] = r["max_grad"][-1] / max(r["max_grad"][0], 1e-12)

    corrs = {}
    for name in ics:
        r = results[name]["pm"]
        if len(r["L_E"]) > 2:
            corrs[name] = float(np.corrcoef(r["mean_G_minus_1"], r["L_E"])[0, 1])
        else:
            corrs[name] = float("nan")

    # Scorecard (2D analogue of 1D)
    c1 = improv["noisy_edge"] > 0.05 and improv["noisy_disk"] > 0.0
    c2 = edge_ratio["noisy_edge"]["pm"] > edge_ratio["noisy_edge"]["heat"] * 1.15
    c2 = c2 and edge_ratio["clean_edge"]["pm"] > edge_ratio["clean_edge"]["heat"] * 1.15
    # smooth blob should not explode gradients
    c3 = edge_ratio["noisy_smooth"]["pm"] < 2.5
    c4 = all(c > 0.85 for c in corrs.values())
    slow = []
    for name in ics:
        r_pm = results[name]["pm"]
        r_l = results[name]["load_pm"]
        mid = len(r_pm["phi"]) // 2
        d_pm = np.linalg.norm(r_pm["phi"][mid] - ics[name]["y"])
        d_l = np.linalg.norm(r_l["phi"][mid] - ics[name]["y"])
        slow.append(bool(d_l <= d_pm * 1.05))
    c5 = sum(slow) >= 3
    c6 = results["noisy_edge"]["pm"]["residual"][-1] < results["noisy_edge"]["heat"]["residual"][-1]

    support = sum([c1, c2, c3, c4, c5, c6])
    if support >= 5:
        verdict = "PROMISING (2D) — Euclidean dual lifts off the line."
    elif support >= 3:
        verdict = "MIXED (2D) — partial lift; tune K/dt or IC."
    else:
        verdict = "WEAK (2D) — dual not yet robust on images."

    return {
        "c1": c1,
        "c2": c2,
        "c3": c3,
        "c4": c4,
        "c5": c5,
        "c6": c6,
        "support": support,
        "verdict": verdict,
        "improv": improv,
        "edge_ratio": edge_ratio,
        "corrs": corrs,
        "slow": slow,
    }


def print_scorecard(card):
    lines = [
        "=" * 64,
        "GO / NO-GO SCORECARD 2D (ACD-EW lift)",
        "=" * 64,
        f"[1] residual dual (edge impro>0.05, disk impro>0): "
        f"{'SUPPORT' if card['c1'] else 'WEAK/FAIL'} "
        f"improv edge/disk={card['improv']['noisy_edge']:.3f}/{card['improv']['noisy_disk']:.3f}",
        f"[2] edge retention PM > heat*1.15: "
        f"{'SUPPORT' if card['c2'] else 'WEAK/FAIL'}",
        f"[3] smooth stability (pm max_grad ratio < 2.5): "
        f"{'SUPPORT' if card['c3'] else 'WEAK/FAIL'} "
        f"ratio={card['edge_ratio']['noisy_smooth']['pm']:.3f}",
        f"[4] corr(L_E, E[G-1]) > 0.85: "
        f"{'SUPPORT' if card['c4'] else 'WEAK/FAIL'} { {k: round(v,3) for k,v in card['corrs'].items()} }",
        f"[5] load-gating slows: "
        f"{'SUPPORT' if card['c5'] else 'WEAK/FAIL'} {card['slow']}",
        f"[6] PM residual better than heat on noisy_edge: "
        f"{'SUPPORT' if card['c6'] else 'WEAK/FAIL'}",
        "-" * 64,
        f"TOTAL: {card['support']}/6 criteria SUPPORT",
        "VERDICT: " + card["verdict"],
        "=" * 64,
    ]
    text = "\n".join(lines)
    print(text)
    return text


if __name__ == "__main__":
    np.random.seed(42)
    ics, results = run_all()
    for name in ics:
        for mode in ["heat", "pm", "load_pm"]:
            r = results[name][mode]
            print(
                f"{name:14s} {mode:8s} resid {r['residual'][0]:.4f}->{r['residual'][-1]:.4f} "
                f"maxg {r['max_grad'][0]:.3f}->{r['max_grad'][-1]:.3f}"
            )
    card = evaluate(ics, results)
    text = print_scorecard(card)
    out = Path(__file__).resolve().parent / "gfe_load_joint_toy_2d_scorecard.txt"
    out.write_text(text + "\n")

    # Summary figure
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2, 3, figsize=(10, 6))
        for ax, name in zip(axes[0], ["noisy_edge", "noisy_disk", "noisy_smooth"]):
            ax.imshow(ics[name]["star"], cmap="gray", vmin=0, vmax=1)
            ax.set_title(f"{name} star")
            ax.axis("off")
        for ax, name in zip(axes[1], ["noisy_edge", "noisy_disk", "noisy_smooth"]):
            ax.imshow(results[name]["pm"]["phi"][-1], cmap="gray", vmin=0, vmax=1)
            ax.set_title(f"PM final ({name})")
            ax.axis("off")
        fig.suptitle(f"Joint toy 2D — {card['support']}/6 SUPPORT", y=1.02)
        plt.tight_layout()
        fig.savefig(Path(__file__).resolve().parent / "gfe_load_joint_toy_2d_summary.png", dpi=140, bbox_inches="tight")
        print("saved 2d summary figure")
    except Exception as e:
        print("figure skip:", e)
