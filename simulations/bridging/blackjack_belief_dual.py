#!/usr/bin/env python3
"""
Blackjack / game belief-field extension of the Euclidean Action–Channel Duality joint toy.

Maps a 1D "belief / true-count strength" field φ over deck-penetration (or info bins)
to the same observation-channel + heat / Perona–Malik (PM) / load-gated PM dual as
`_joint_toy_v2_core.py`.

This is a preliminary experiment: same dual pattern on a game-motivated IC.
Not a proof of gravity, not a card-counting edge claim, not a full blackjack engine.

Run:
  .venv/bin/python simulations/bridging/blackjack_belief_dual.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

# Reuse joint-toy v2 math (residual H_c, load split, heat/PM, scorecard plumbing)
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from _joint_toy_v2_core import (  # noqa: E402
    ALPHA_L,
    DT,
    K_PM,
    N_STEPS,
    SNAPSHOT_EVERY,
    residual_mse,
    run_dynamics,
)

# ---------------------------------------------------------------------------
# Domain parameters (belief field on a 1D lattice)
# ---------------------------------------------------------------------------
# x-axis interpretation (comments only — lattice is still Euclidean 1D):
#   bin i ≈ deck penetration or successive info bins as the shoe is depleted.
#   Low i: early shoe (counts less informative). High i: deep penetration.
N_BINS = 192
NOISE_SIGMA = 0.12
SEED_BASE = 201  # fixed seeds for determinism (distinct from joint-toy 101–104)

# Modes under comparison
MODES = ("heat", "pm", "load_pm")


# ---------------------------------------------------------------------------
# True structure φ_★: count / edge strength profiles
# ---------------------------------------------------------------------------
def phi_star_high_count_step(n: int = N_BINS) -> np.ndarray:
    """
    Idealized true edge strength: flat low early, jumps to high-count region.

    Motivated by: true count / advantage becoming strongly positive only after
    a threshold of low cards have been removed (deep penetration + rich shoe).
    """
    phi = np.zeros(n)
    phi[n // 2 :] = 1.0
    return phi


def phi_star_edge_ramp(n: int = N_BINS) -> np.ndarray:
    """
    Smooth ramp of edge strength with penetration (weaker gradients).

    Motivated by: gradual accumulation of count information; no hard switch.
    Used as a ramp-stability control (PM should not staircase).
    """
    x = np.arange(n)
    return 0.5 + 0.5 * np.tanh((x - n / 2) / (0.15 * n))


def phi_star_two_hot_regions(n: int = N_BINS) -> np.ndarray:
    """
    Two localized high-edge pockets (e.g. two favorable windows in a shoe).

    Motivated by: non-monotonic count path — edge appears, dilutes, reappears.
    """
    i = np.arange(n)
    phi = np.exp(-0.5 * ((i - 0.30 * n) / (0.05 * n)) ** 2)
    phi += 0.7 * np.exp(-0.5 * ((i - 0.70 * n) / (0.07 * n)) ** 2)
    return phi


def phi_star_clean_high_count(n: int = N_BINS) -> np.ndarray:
    """Same step as high_count, used with zero observation noise (edge vs heat blur)."""
    return phi_star_high_count_step(n)


def make_observation(phi_star: np.ndarray, sigma: float, rng: np.random.Generator) -> np.ndarray:
    """Noisy observation of true edge/count strength (imperfect count or belief)."""
    return phi_star + sigma * rng.standard_normal(len(phi_star))


def build_ics(noise_sigma: float = NOISE_SIGMA) -> dict:
    """
    Game-motivated initial conditions.

    y  = noisy belief / observed count-strength field (channel input).
    star = true edge / true-count strength φ_★ (hidden structure).

    Seeds fixed (do not use hash()) for determinism.
    """
    specs = {
        "noisy_high_count": {
            "star": phi_star_high_count_step(),
            "sigma": noise_sigma,
            "desc": "Primary: denoise belief; keep high-count jump (edge retention)",
        },
        "noisy_two_windows": {
            "star": phi_star_two_hot_regions(),
            "sigma": noise_sigma,
            "desc": "Two favorable windows; localized structure recovery",
        },
        "noisy_edge_ramp": {
            "star": phi_star_edge_ramp(),
            "sigma": noise_sigma,
            "desc": "Gradual edge ramp; PM should not staircase",
        },
        "clean_high_count": {
            "star": phi_star_clean_high_count(),
            "sigma": 0.0,
            "desc": "No noise: pure structure-preserving vs heat blur of the jump",
        },
    }
    seeds = {
        "noisy_high_count": SEED_BASE + 0,
        "noisy_two_windows": SEED_BASE + 1,
        "noisy_edge_ramp": SEED_BASE + 2,
        "clean_high_count": SEED_BASE + 3,
    }
    ics = {}
    for name, spec in specs.items():
        star = spec["star"].copy()
        sig = spec["sigma"]
        if sig == 0.0:
            y = star.copy()
        else:
            y = make_observation(star, sigma=sig, rng=np.random.default_rng(seeds[name]))
        ics[name] = {
            "star": star,
            "y": y,
            "sigma": sig,
            "desc": spec["desc"],
        }
    return ics


def run_all(ics: dict | None = None, modes=None):
    if ics is None:
        ics = build_ics()
    if modes is None:
        modes = list(MODES)
    results = {}
    for ic_name, pack in ics.items():
        results[ic_name] = {}
        for mode in modes:
            results[ic_name][mode] = run_dynamics(
                pack["y"],
                pack["star"],
                mode=mode,
                n_steps=N_STEPS,
                dt=DT,
                alpha_L=ALPHA_L,
                snapshot_every=SNAPSHOT_EVERY,
                K=K_PM,
            )
    return ics, results


# ---------------------------------------------------------------------------
# Scorecard — residual impro, edge retention, load slows (honest MIXED OK)
# ---------------------------------------------------------------------------
def evaluate(ics: dict, results: dict) -> dict:
    modes = list(MODES)
    primary = "noisy_high_count"
    secondary = "noisy_two_windows"
    ramp = "noisy_edge_ramp"
    edge_ics = ["noisy_high_count", "clean_high_count"]

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
                corrs_LE[ic_name][mode] = float(
                    np.corrcoef(r["mean_G_minus_1"], r["L_E"])[0, 1]
                )
            else:
                corrs_LE[ic_name][mode] = float("nan")

    mono = {}
    for ic_name in ics:
        mono[ic_name] = {}
        for mode in modes:
            dR = np.diff(results[ic_name][mode]["residual"])
            mono[ic_name][mode] = float(np.mean(dR <= 1e-12))

    # [1] residual dual: PM better residual than heat on primary + secondary
    c1_primary = improv[primary] > 0.05
    c1_secondary = improv[secondary] > 0.0
    c1 = c1_primary and c1_secondary
    c1_flags = [c1_primary, c1_secondary]

    # [2] edge retention: PM keeps high-count jump better than heat
    c2_flags = [
        edge_score[ic]["pm"] > edge_score[ic]["heat"] * 1.15 for ic in edge_ics
    ]
    c2 = all(c2_flags)

    # [3] ramp stability: no PM staircasing on gradual edge
    ramp_ratio = edge_score[ramp]["pm"]
    c3 = ramp_ratio < 2.5

    # [4] L_E tracks induction intensity E[G-1]
    c4_corrs = [corrs_LE[ic]["pm"] for ic in ics]
    c4 = all(c > 0.85 for c in c4_corrs)

    # [5] load clock slows mid-run change vs pure PM
    slow_flags = []
    for ic in ics:
        r_pm = results[ic]["pm"]
        r_l = results[ic]["load_pm"]
        mid = len(r_pm["phi"]) // 2
        d_pm = np.linalg.norm(r_pm["phi"][mid] - ics[ic]["y"])
        d_l = np.linalg.norm(r_l["phi"][mid] - ics[ic]["y"])
        slow_flags.append(bool(d_l <= d_pm * 1.02))
    c5 = sum(slow_flags) >= 3

    # [6] residual co-motion on primary IC
    c6 = (
        mono[primary]["pm"] >= mono[primary]["heat"] - 0.05
        and results[primary]["pm"]["residual"][-1]
        < results[primary]["heat"]["residual"][-1]
    )

    support = sum([c1, c2, c3, c4, c5, c6])
    if support >= 5:
        verdict = (
            "PROMISING — same Euclidean dual pattern holds on game-motivated belief ICs; "
            "still ACD-EW toy only (not a blackjack edge or gravity proof)."
        )
    elif support >= 3:
        verdict = (
            "MIXED — dual holds partially on belief-field ICs; document honestly. "
            "Not a proof of card-counting edge or continuum GfE."
        )
    else:
        verdict = (
            "WEAK — game IC does not reproduce residual/edge dual cleanly; "
            "keep as exploratory only."
        )

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
        "edge_score": edge_score,
        "corrs_LE": corrs_LE,
        "mono": mono,
        "slow_flags": slow_flags,
        "ramp_ratio": ramp_ratio,
        "c1_flags": c1_flags,
        "c2_flags": c2_flags,
        "c4_corrs": c4_corrs,
        "primary": primary,
        "secondary": secondary,
        "edge_ics": edge_ics,
        "ramp": ramp,
    }


def print_scorecard(card: dict) -> str:
    primary = card["primary"]
    secondary = card["secondary"]
    edge_ics = card["edge_ics"]
    lines = [
        "=" * 64,
        "BLACKJACK BELIEF-FIELD DUAL — GO / NO-GO SCORECARD",
        "(ACD-EW pattern on game-motivated 1D belief / count-strength φ)",
        "=" * 64,
        (
            f"[1] PM residual better than heat "
            f"(high_count impro>0.05, two_windows impro>0): "
            f"{'SUPPORT' if card['c1'] else 'WEAK/FAIL'} "
            f"improv={{{primary!r}: {round(float(card['improv'][primary]), 3)}, "
            f"{secondary!r}: {round(float(card['improv'][secondary]), 3)}}}"
        ),
        (
            f"[2] PM edge retention > heat*1.15 on high-count ICs: "
            f"{'SUPPORT' if card['c2'] else 'WEAK/FAIL'} "
            f"pm/heat={[round(float(card['edge_score'][ic]['pm'] / max(card['edge_score'][ic]['heat'], 1e-9)), 2) for ic in edge_ics]}"
        ),
        (
            f"[3] Edge-ramp stability (pm max_grad ratio < 2.5): "
            f"{'SUPPORT' if card['c3'] else 'WEAK/FAIL'} "
            f"ratio={float(card['ramp_ratio']):.3f}"
        ),
        (
            f"[4] corr(L_E, E[G-1]) > 0.85 on all PM runs: "
            f"{'SUPPORT' if card['c4'] else 'WEAK/FAIL'} "
            f"{[round(float(c), 3) for c in card['c4_corrs']]}"
        ),
        (
            f"[5] Load-gating slows mid-run change vs PM: "
            f"{'SUPPORT' if card['c5'] else 'WEAK/FAIL'} "
            f"{card['slow_flags']}"
        ),
        (
            f"[6] Channel residual PM better final + monotone on {primary}: "
            f"{'SUPPORT' if card['c6'] else 'WEAK/FAIL'} "
            f"mono pm/heat={card['mono'][primary]['pm']:.2f}/"
            f"{card['mono'][primary]['heat']:.2f}"
        ),
        "-" * 64,
        f"TOTAL: {card['support']}/6 criteria SUPPORT",
        "VERDICT: " + card["verdict"],
        "=" * 64,
        "Honesty: Euclidean warm-up dual on a belief-shaped IC only.",
        "Not a full blackjack simulator; not a claim of player edge or gravity.",
        f"Seeds: {SEED_BASE}–{SEED_BASE + 3}; N={N_BINS}; noise_sigma={NOISE_SIGMA}.",
    ]
    text = "\n".join(lines)
    print(text)
    return text


def main() -> int:
    np.random.seed(42)
    ics, results = run_all()

    print("Blackjack belief-field dual — trajectory summary")
    print("(φ = count/edge strength vs penetration bins; y = noisy observation)\n")
    for ic_name, pack in ics.items():
        print(f"  IC {ic_name}: {pack['desc']}")
        for mode in MODES:
            r = results[ic_name][mode]
            print(
                f"    {mode:8s} resid {r['residual'][0]:.4f}->{r['residual'][-1]:.4f} "
                f"H_c {r['H_c'][0]:.3f}->{r['H_c'][-1]:.3f} "
                f"maxg {r['max_grad'][0]:.3f}->{r['max_grad'][-1]:.3f} "
                f"L_clock_end {r['L_clock'][-1]:.4f}"
            )
        print()

    card = evaluate(ics, results)
    text = print_scorecard(card)

    out = _HERE / "blackjack_belief_dual_scorecard.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
        f.write("\n")
        f.write("Date: 2026-07-14 (deterministic seeds 201–204)\n")
        f.write("Run: .venv/bin/python simulations/bridging/blackjack_belief_dual.py\n")
        f.write("Link: ACD-EW same dual pattern on game-motivated IC; see DESIGN_blackjack_belief_dual.md\n")
    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
