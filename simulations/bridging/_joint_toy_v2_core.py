
"""Joint toy v2 core — imported by notebook and CLI runner."""
from __future__ import annotations
import numpy as np
from pathlib import Path

# Defaults
N = 192
h = 1.0
ALPHA_G = 1.0
K_PM = 0.15
ALPHA_L = 3.0
C_E, C_S, C_B = 1.0, 1.0, 0.5
DT = 0.08
N_STEPS = 180
SNAPSHOT_EVERY = 15
NOISE_SIGMA = 0.12
LAMBDA_E = 0.15

def gradients(phi):
    return np.diff(phi) / h

def induced_G(phi, alpha_g=ALPHA_G):
    return 1.0 + alpha_g * gradients(phi) ** 2

def gfe_action(phi, alpha_g=ALPHA_G):
    G = induced_G(phi, alpha_g)
    return float(-np.sum(np.log(G)))

def gfe_density(phi, alpha_g=ALPHA_G):
    return -np.log(induced_G(phi, alpha_g))

def phi_star_step(n=N):
    phi = np.zeros(n)
    phi[n // 2 :] = 1.0
    return phi

def phi_star_two_bumps(n=N):
    i = np.arange(n)
    phi = np.exp(-0.5 * ((i - 0.30 * n) / (0.05 * n)) ** 2)
    phi += 0.7 * np.exp(-0.5 * ((i - 0.70 * n) / (0.07 * n)) ** 2)
    return phi

def phi_star_smooth_ramp(n=N):
    return 0.5 + 0.5 * np.tanh((np.arange(n) - n / 2) / (0.15 * n))

def make_observation(phi_star, sigma=NOISE_SIGMA, rng=None):
    rng = rng or np.random.default_rng(0)
    return phi_star + sigma * rng.standard_normal(len(phi_star))

def build_ics(noise_sigma=NOISE_SIGMA):
    specs = {
        "noisy_step": {"star": phi_star_step(), "sigma": noise_sigma, "desc": "Primary dual test: denoise + keep jump"},
        "noisy_two_bumps": {"star": phi_star_two_bumps(), "sigma": noise_sigma, "desc": "Localized structure recovery"},
        "noisy_ramp": {"star": phi_star_smooth_ramp(), "sigma": noise_sigma, "desc": "Weak-gradient: should not staircase"},
        "clean_step": {"star": phi_star_step(), "sigma": 0.0, "desc": "No noise: pure edge vs heat blur"},
    }
    # Fixed seeds (do not use hash() — PYTHONHASHSEED makes it nondeterministic)
    seeds = {
        "noisy_step": 101,
        "noisy_two_bumps": 102,
        "noisy_ramp": 103,
        "clean_step": 104,
    }
    ics = {}
    for name, spec in specs.items():
        star = spec["star"].copy()
        sig = spec["sigma"]
        if sig == 0.0:
            y = star.copy()
        else:
            y = make_observation(star, sigma=sig, rng=np.random.default_rng(seeds[name]))
        ics[name] = {"star": star, "y": y, "sigma": sig, "desc": spec["desc"]}
    return ics

def residual_mse(phi_hat, phi_star):
    return float(np.mean((phi_hat - phi_star) ** 2))

def H_residual(phi_hat, phi_star, sigma_ref=None):
    if sigma_ref is None:
        sigma_ref = max(NOISE_SIGMA, 1e-3) ** 2
    R = residual_mse(phi_hat, phi_star)
    return float(np.log(1.0 + R / sigma_ref))

def H_edge_location(phi_hat, eps=1e-12):
    s = np.abs(gradients(phi_hat)) + eps
    p = s / s.sum()
    return float(-np.sum(p * np.log2(p)))

def H_c_channel(phi_hat, phi_star, lambda_e=LAMBDA_E, sigma_ref=None):
    return H_residual(phi_hat, phi_star, sigma_ref=sigma_ref) + lambda_e * H_edge_location(phi_hat)

def load_terms(phi_hat, phi_star, H_prev=None, dt=DT, c_E=C_E, c_S=C_S, c_B=C_B):
    gphi = gradients(phi_hat)
    L_E = c_E * float(np.mean(gphi ** 2))
    H = H_c_channel(phi_hat, phi_star)
    if H_prev is None:
        L_S = 0.0
    else:
        L_S = c_S * abs(H - H_prev) / max(dt, 1e-12)
    gmax = float(np.max(np.abs(gphi)))
    L_B = c_B * gmax / (1.0 + gmax)
    return {
        "L_E": L_E, "L_S": L_S, "L_B": L_B,
        "L": L_E + L_S + L_B, "L_clock": L_E + L_S, "H_c": H,
        "H_R": H_residual(phi_hat, phi_star),
        "H_edge": H_edge_location(phi_hat),
        "residual": residual_mse(phi_hat, phi_star),
    }

def divergence_from_edge_flux(flux):
    n = len(flux) + 1
    dphi = np.zeros(n)
    dphi[0] = flux[0]
    dphi[1:-1] = flux[1:] - flux[:-1]
    dphi[-1] = -flux[-1]
    return dphi / h

def rhs_heat(phi):
    return divergence_from_edge_flux(gradients(phi))

def rhs_pm(phi, K=K_PM):
    gphi = gradients(phi)
    rho = 1.0 / (1.0 + (gphi / max(K, 1e-8)) ** 2)
    return divergence_from_edge_flux(rho * gphi)

def step_euler(phi, rhs, dt):
    return phi + dt * rhs(phi)

def run_dynamics(phi_init, phi_star, mode="pm", n_steps=N_STEPS, dt=DT,
                 alpha_L=ALPHA_L, snapshot_every=SNAPSHOT_EVERY, K=K_PM):
    phi = phi_init.astype(float).copy()
    terms = load_terms(phi, phi_star, H_prev=None, dt=dt)
    H_prev = terms["H_c"]
    hist = {k: [] for k in [
        "phi", "t", "S_gfe", "H_c", "H_R", "H_edge", "residual",
        "L", "L_E", "L_S", "L_B", "L_clock", "edge_energy", "max_grad",
        "mean_G_minus_1", "clock",
    ]}
    def snap(t, clock):
        gphi = gradients(phi)
        terms_now = load_terms(phi, phi_star, H_prev=H_prev, dt=dt)
        hist["phi"].append(phi.copy())
        hist["t"].append(t)
        hist["S_gfe"].append(gfe_action(phi))
        for k in ["H_c", "H_R", "H_edge", "residual", "L", "L_E", "L_S", "L_B", "L_clock"]:
            hist[k].append(terms_now[k] if k != "H_c" else terms_now["H_c"])
        # fix H_c from terms_now
        hist["H_c"][-1] = terms_now["H_c"]
        hist["edge_energy"].append(float(np.mean(gphi ** 2)))
        hist["max_grad"].append(float(np.max(np.abs(gphi))))
        hist["mean_G_minus_1"].append(float(np.mean(induced_G(phi) - 1)))
        hist["clock"].append(clock)
        return terms_now

    t = 0.0
    terms = snap(0.0, 1.0)
    H_prev = terms["H_c"]
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
        if k % snapshot_every == 0 or k == n_steps:
            # record with current H_prev already updated — pass H_prev for rate from last snap
            # recompute rate vs previous recorded H_c
            prev_H = hist["H_c"][-1]
            terms_rec = load_terms(phi, phi_star, H_prev=prev_H, dt=dt * snapshot_every)
            gphi = gradients(phi)
            hist["phi"].append(phi.copy())
            hist["t"].append(t)
            hist["S_gfe"].append(gfe_action(phi))
            for key in ["H_c", "H_R", "H_edge", "residual", "L", "L_E", "L_S", "L_B", "L_clock"]:
                hist[key].append(terms_rec[key])
            hist["edge_energy"].append(float(np.mean(gphi ** 2)))
            hist["max_grad"].append(float(np.max(np.abs(gphi))))
            hist["mean_G_minus_1"].append(float(np.mean(induced_G(phi) - 1)))
            hist["clock"].append(clock if mode == "load_pm" else 1.0)
    for key in hist:
        if key != "phi":
            hist[key] = np.asarray(hist[key], dtype=float)
    return hist

def run_all(ics=None, modes=None):
    if ics is None:
        ics = build_ics()
    if modes is None:
        modes = ["heat", "pm", "load_pm"]
    results = {}
    for ic_name, pack in ics.items():
        results[ic_name] = {}
        for mode in modes:
            results[ic_name][mode] = run_dynamics(pack["y"], pack["star"], mode=mode)
    return ics, results

def evaluate(ics, results):
    modes = ["heat", "pm", "load_pm"]
    improv = {}
    for ic_name, pack in ics.items():
        R0 = residual_mse(pack["y"], pack["star"])
        Rh = results[ic_name]["heat"]["residual"][-1]
        Rp = results[ic_name]["pm"]["residual"][-1]
        improv[ic_name] = (Rh - Rp) / max(R0, 1e-12)

    edge_score = {}
    for ic_name in ics:
        edge_score[ic_name] = {}
        for mode in modes:
            r = results[ic_name][mode]
            edge_score[ic_name][mode] = r["max_grad"][-1] / max(r["max_grad"][0], 1e-12)

    corrs_LE = {}
    for ic_name in ics:
        corrs_LE[ic_name] = {}
        for mode in modes:
            r = results[ic_name][mode]
            if len(r["L_E"]) > 2:
                corrs_LE[ic_name][mode] = float(np.corrcoef(r["mean_G_minus_1"], r["L_E"])[0, 1])
            else:
                corrs_LE[ic_name][mode] = float("nan")

    mono = {}
    for ic_name in ics:
        mono[ic_name] = {}
        for mode in modes:
            dR = np.diff(results[ic_name][mode]["residual"])
            mono[ic_name][mode] = float(np.mean(dR <= 1e-12))

    # scorecard
    # Primary dual IC must clear a solid margin; secondary noisy IC a weaker one
    # (smooth bumps are harder for 1D PM than a single step).
    c1_step = improv["noisy_step"] > 0.05
    c1_bumps = improv["noisy_two_bumps"] > 0.0  # strictly better residual than heat
    c1 = c1_step and c1_bumps
    c1_flags = [c1_step, c1_bumps]

    edge_ics = ["noisy_step", "clean_step"]
    c2_flags = [edge_score[ic]["pm"] > edge_score[ic]["heat"] * 1.15 for ic in edge_ics]
    c2 = all(c2_flags)

    ramp_ratio = edge_score["noisy_ramp"]["pm"]
    c3 = ramp_ratio < 2.5

    c4_corrs = [corrs_LE[ic]["pm"] for ic in ics]
    c4 = all(c > 0.85 for c in c4_corrs)

    slow_flags = []
    for ic in ics:
        r_pm = results[ic]["pm"]
        r_l = results[ic]["load_pm"]
        mid = len(r_pm["phi"]) // 2
        d_pm = np.linalg.norm(r_pm["phi"][mid] - ics[ic]["y"])
        d_l = np.linalg.norm(r_l["phi"][mid] - ics[ic]["y"])
        slow_flags.append(bool(d_l <= d_pm * 1.02))
    c5 = sum(slow_flags) >= 3

    c6 = (mono["noisy_step"]["pm"] >= mono["noisy_step"]["heat"] - 0.05 and
          results["noisy_step"]["pm"]["residual"][-1] < results["noisy_step"]["heat"]["residual"][-1])

    support = sum([c1, c2, c3, c4, c5, c6])
    if support >= 5:
        verdict = "PROMISING — formalize Action–Channel Duality for Euclidean warm-up; optional 2D next."
    elif support >= 3:
        verdict = "MIXED — dual holds partially (geometry/clock vs full channel dual); document honestly."
    else:
        verdict = "WEAK — keep GfE as continuum peer; redesign Stage-1 dual."

    card = {
        "c1": c1, "c2": c2, "c3": c3, "c4": c4, "c5": c5, "c6": c6,
        "support": support, "verdict": verdict,
        "improv": improv, "edge_score": edge_score,
        "corrs_LE": corrs_LE, "mono": mono, "slow_flags": slow_flags,
        "ramp_ratio": ramp_ratio, "c1_flags": c1_flags, "c2_flags": c2_flags,
        "c4_corrs": c4_corrs,
    }
    return card

def print_scorecard(card):
    lines = [
        "=" * 64,
        "GO / NO-GO SCORECARD v2 (P0–P2)",
        "=" * 64,
        f"[1] PM residual better than heat (step impro>0.05, bumps impro>0): "
        f"{'SUPPORT' if card['c1'] else 'WEAK/FAIL'} "
        f"improv={ {ic: round(card['improv'][ic],3) for ic in ['noisy_step','noisy_two_bumps']} }",
        f"[2] PM edge retention > heat*1.15 on step ICs: "
        f"{'SUPPORT' if card['c2'] else 'WEAK/FAIL'} "
        f"pm/heat={[round(card['edge_score'][ic]['pm']/max(card['edge_score'][ic]['heat'],1e-9),2) for ic in ['noisy_step','clean_step']]}",
        f"[3] P0 ramp stability (pm max_grad ratio < 2.5): "
        f"{'SUPPORT' if card['c3'] else 'WEAK/FAIL'} ratio={card['ramp_ratio']:.3f}",
        f"[4] corr(L_E, E[G-1]) > 0.85 on all PM runs: "
        f"{'SUPPORT' if card['c4'] else 'WEAK/FAIL'} {[round(c,3) for c in card['c4_corrs']]}",
        f"[5] Load-gating slows mid-run change vs PM: "
        f"{'SUPPORT' if card['c5'] else 'WEAK/FAIL'} {card['slow_flags']}",
        f"[6] Channel residual PM better final + monotone on noisy_step: "
        f"{'SUPPORT' if card['c6'] else 'WEAK/FAIL'} "
        f"mono pm/heat={card['mono']['noisy_step']['pm']:.2f}/{card['mono']['noisy_step']['heat']:.2f}",
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
    for ic_name, pack in ics.items():
        for mode in ["heat", "pm", "load_pm"]:
            r = results[ic_name][mode]
            print(f"{ic_name:16s} {mode:8s} resid {r['residual'][0]:.4f}->{r['residual'][-1]:.4f} "
                  f"H_c {r['H_c'][0]:.3f}->{r['H_c'][-1]:.3f} maxg {r['max_grad'][0]:.3f}->{r['max_grad'][-1]:.3f}")
    card = evaluate(ics, results)
    print_scorecard(card)
