#!/usr/bin/env python3
"""Tier 2 toy model: slack H(Y) - I(X;Y) - I(F;Y) at readout ranks 2, 4, 8, 16
of the existing sixteen-symbol (two-use) surface runs.

    *** TOY MODEL. Two-qubit, two-use proof-of-concept. It is NOT evidence
    *** about hadronic or QCD physics and makes no physical claim.

No new simulation. Recomputes the deterministic joint-law quantities already
produced by procedural_share_surface.py (CE-9 Haar-50 pool, seed 2026) and
procedural_share_mlpool.py (CE-12 ML-200 pool, canonical draw 2026, eps=0.05).
Blind input; existing seeds, ranks, and g-grid. GAD temperatures T in {0, 1, inf}
are the CE-9 settings; dephasing is the CE-12 channel (also applied to the
CE-9 Haar pool through the existing CE-12 surface path). No new sampling
and no parameter change.

Run:

    python simulations/classical/analysis_slack_per_rank.py            # self-checks + report
    python simulations/classical/analysis_slack_per_rank.py --check    # self-checks only

SLACK. H(Y) - I(X;Y) - I(F;Y), the slack of the corrected bound
  I(X;Y) + I(F;Y) <= H(Y). With X independent of F, this equals
  H(Y|X,F) + I(X;F|Y).

THE RUNS. Rank r in {2, 4, 8, 16} is the number of outcomes of one joint
  projective measurement on the 16-dimensional two-use output (the
  sixteen-symbol readout of CE-7/CE-9/CE-12). Nested Z is primary;
  the random-basis control is also reported. Inputs are the CE-9 half
  encoding (blind).
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import procedural_share as ps
import procedural_share_mlpool as mlp
import procedural_share_surface as pss

RANKS = (2, 4, 8, 16)
GAMMAS = np.round(np.arange(0, 1.01, 0.1), 10)
SEED = 2026
HAAR_N = 50
HAAR_SHA_PREFIX = "114e410f9fcf4700"
ML_SHA_PREFIX = "d11fa3d1ec4594b7"

# Printed headlines locked so a later change of the surface hooks cannot
# silently drift the analysis note. Values are 3-decimal print strings.
FROZEN = dict(
    haar_sha=HAAR_SHA_PREFIX,
    ml_sha=ML_SHA_PREFIX,
    ml_n=200,
    # CE-9 published H(F|Y) at T=1, nested, g=0 and g=1 (docs/procedural-share-surface.md).
    haar_HFgY_g0="5.609 / 5.486 / 5.453 / 5.338",
    haar_HFgY_g1="5.644 / 5.644 / 5.644 / 5.644",
    # Slack min/med/max and endpoints, T=1 nested, rank 16 (primary headline).
    haar_T1_n_r16="3.360 / 3.741 / 3.818",
    haar_T1_n_r16_g0="3.647",
    haar_T1_n_r16_g1="3.360",
    ml_T1_n_r16="3.360 / 3.649 / 3.741",
    ml_T1_n_r16_g0="3.552",
    ml_T1_n_r16_g1="3.360",
    # H(F|Y) at g=0, ML nested (all T agree at g=0).
    ml_HFgY_g0="7.599 / 7.487 / 7.444 / 7.339",
    # T=0 nested rank-16 slack vanishes at g=1 (plain AD resets to |0>).
    haar_T0_n_r16_g1="0.000",
    ml_T0_n_r16_g1="0.000",
    # T=inf nested rank-16 slack at g=1 is 4 bits (maximally mixed output).
    haar_Tinf_n_r16_g1="4.000",
    ml_Tinf_n_r16_g1="4.000",
)


def _zero(x):
    x = np.asarray(x, float)
    return np.where(np.abs(x) < 5e-10, 0.0, x) + 0.0


def fz(v, nd: int = 3) -> str:
    return f"{float(_zero(v)):.{nd}f}"


def _mmm(t, nd: int = 3) -> str:
    return " / ".join(fz(v, nd) for v in t)


def slack_of(R: dict) -> np.ndarray:
    return _zero(R["Hy"] - R["IXY"] - R["IFY"])


def col_stats(M: np.ndarray, j: int) -> tuple[float, float, float, float, float]:
    col = _zero(M[:, j])
    return (float(col.min()), float(np.median(col)), float(col.max()),
            float(col[0]), float(col[-1]))


def md_table(M: np.ndarray, gammas, ranks, nd: int = 3) -> str:
    M = _zero(M)
    lines = ["| \\(g\\) | " + " | ".join(f"r={r}" for r in ranks) + " |",
             "|---|" + "---|" * len(ranks)]
    for i, g in enumerate(gammas):
        lines.append(
            f"| {g:.1f} | " + " | ".join(f"{M[i, j]:.{nd}f}" for j in range(len(ranks))) + " |"
        )
    return "\n".join(lines)


def pack(R: dict) -> dict:
    S = slack_of(R)
    d = dict(R=R, slack=S, n=int(S.size),
             corr=int((R["IXY"] + R["IFY"] <= R["Hy"] + 1e-10).sum()),
             orig=int((R["IXY"] + R["HFgY"] <= R["Hy"] + 1e-10).sum()),
             max_Hy=float(_zero(R["Hy"]).max()),
             max_IXY=float(_zero(R["IXY"]).max()),
             max_IFY=float(_zero(R["IFY"]).max()))
    d["stats"] = {r: dict(slack=col_stats(S, j), HFgY=col_stats(_zero(R["HFgY"]), j),
                          Hy=col_stats(_zero(R["Hy"]), j))
                  for j, r in enumerate(RANKS)}
    if "ident" in R:
        d["max_ident"] = float(np.abs(R["ident"]).max())
    if "IXF" in R:
        d["max_IXF"] = float(np.abs(R["IXF"]).max())
    return d


def compute() -> dict:
    """Recompute CE-9 and CE-12 surfaces with existing seeds and grids."""
    haar_pool = pss.draw_pool(HAAR_N, SEED)
    phash = pss.pool_hash(haar_pool)
    pss.self_checks(haar_pool)
    bases = pss.random_readouts(RANKS, SEED)
    inputs = pss.ENCODINGS["half"]

    def haar_gad(T, ro):
        p = 1.0 if T == 0 else ps.p_of_T(T)
        S, _ = pss.run_surface(haar_pool, phash, GAMMAS, list(RANKS), p, ro, bases, inputs)
        return pack(S)

    def via_mlp(pool, channel, p, ro):
        return pack(mlp.surface(pool, mlp.blind_inputs(len(pool)), None,
                                channel, p, GAMMAS, RANKS, ro, bases))

    haar = {}
    for Tlabel, T in (("T0", 0.0), ("T1", 1.0), ("Tinf", math.inf)):
        for ro in ("nested", "random"):
            haar[f"GAD_{Tlabel}_{ro}"] = haar_gad(T, ro)
    for ro in ("nested", "random"):
        haar[f"deph_{ro}"] = via_mlp(haar_pool, "dephasing", 0.0, ro)

    ml_pool, rec = mlp.load_pool()
    regen = mlp.ml_pool(rec["seed"], rec["n_samples"], rec["eps"],
                        rec["budget"], rec["tfrac"], rec["ref"])
    ml = {}
    for Tlabel, T in (("T0", 0.0), ("T1", 1.0), ("Tinf", math.inf)):
        p = 1.0 if T == 0 else ps.p_of_T(T)
        for ro in ("nested", "random"):
            ml[f"GAD_{Tlabel}_{ro}"] = via_mlp(ml_pool, "gad", p, ro)
    for ro in ("nested", "random"):
        ml[f"deph_{ro}"] = via_mlp(ml_pool, "dephasing", 0.0, ro)

    # Agreement of the two GAD code paths on the CE-9 pool.
    p = ps.p_of_T(1.0)
    Rmlp = mlp.surface(haar_pool, mlp.blind_inputs(len(haar_pool)), None,
                       "gad", p, GAMMAS, RANKS, "nested", bases)
    Rpss, _ = pss.run_surface(haar_pool, phash, GAMMAS, list(RANKS), p,
                              "nested", bases, inputs)
    diffs = {k: float(np.abs(Rmlp[k] - Rpss[k]).max()) for k in ("Hy", "IXY", "IFY", "HFgY")}

    return dict(haar=haar, ml=ml, haar_sha=phash, ml_sha=rec["pool_sha256"],
                ml_n=len(ml_pool), regen_ok=pss.pool_hash(regen) == rec["pool_sha256"],
                pss_mlp_diffs=diffs, gammas=GAMMAS, ranks=RANKS)


def self_checks() -> dict:
    data = compute()
    f = FROZEN
    assert data["haar_sha"].startswith(f["haar_sha"]), data["haar_sha"]
    assert data["ml_sha"].startswith(f["ml_sha"]), data["ml_sha"]
    assert data["ml_n"] == f["ml_n"] and data["regen_ok"]
    assert max(data["pss_mlp_diffs"].values()) < 1e-14

    # Every surface: corrected bound holds (theorem), original form holds nowhere.
    for bundle in (data["haar"], data["ml"]):
        for name, P in bundle.items():
            assert P["corr"] == P["n"] == 44 and P["orig"] == 0, name
            assert P["max_Hy"] <= 4.0 + 1e-12, name
            if "max_ident" in P:
                assert P["max_ident"] < 1e-12, name
            if "max_IXF" in P:
                assert P["max_IXF"] < 1e-12, name

    H = data["haar"]["GAD_T1_nested"]
    M = data["ml"]["GAD_T1_nested"]
    # Published CE-9 H(F|Y) table, T=1 nested.
    haar_g0 = _mmm(H["R"]["HFgY"][0])
    haar_g1 = _mmm(H["R"]["HFgY"][-1])
    assert haar_g0 == f["haar_HFgY_g0"], haar_g0
    assert haar_g1 == f["haar_HFgY_g1"], haar_g1
    assert _mmm(M["R"]["HFgY"][0]) == f["ml_HFgY_g0"]

    def r16(P):
        s = P["stats"][16]["slack"]
        return _mmm(s[:3]), fz(s[3]), fz(s[4])

    h_mmm, h_g0, h_g1 = r16(H)
    m_mmm, m_g0, m_g1 = r16(M)
    assert (h_mmm, h_g0, h_g1) == (f["haar_T1_n_r16"], f["haar_T1_n_r16_g0"], f["haar_T1_n_r16_g1"])
    assert (m_mmm, m_g0, m_g1) == (f["ml_T1_n_r16"], f["ml_T1_n_r16_g0"], f["ml_T1_n_r16_g1"])

    # T=0 nested: slack is 0 at g=1 (plain AD, Y deterministic) at every rank,
    # including 16; T=inf nested: slack is log2(r) at g=1 (Y maximally mixed).
    for pool, t0, tinf in (("haar", f["haar_T0_n_r16_g1"], f["haar_Tinf_n_r16_g1"]),
                           ("ml", f["ml_T0_n_r16_g1"], f["ml_Tinf_n_r16_g1"])):
        assert fz(data[pool]["GAD_T0_nested"]["stats"][16]["slack"][4]) == t0
        assert fz(data[pool]["GAD_Tinf_nested"]["stats"][16]["slack"][4]) == tinf
        for r in RANKS:
            assert data[pool]["GAD_T0_nested"]["stats"][r]["slack"][4] < 1e-12
            assert abs(data[pool]["GAD_Tinf_nested"]["stats"][r]["slack"][4] - math.log2(r)) < 1e-12

    # Dephasing with nested Z is flat and equals the g=0 GAD surface (Z-invisible).
    for pool in ("haar", "ml"):
        deph = data[pool]["deph_nested"]["slack"]
        gad0 = data[pool]["GAD_T1_nested"]["slack"][0]
        assert np.allclose(deph, deph[0:1], atol=1e-12)
        assert np.allclose(deph[0], gad0, atol=1e-12)

    # g=0 values do not depend on T (noise is off).
    for pool in ("haar", "ml"):
        a = data[pool]["GAD_T0_nested"]["slack"][0]
        b = data[pool]["GAD_T1_nested"]["slack"][0]
        c = data[pool]["GAD_Tinf_nested"]["slack"][0]
        assert np.allclose(a, b) and np.allclose(a, c)

    # Procedural share does not collapse at rank 16: stays near log2|pool|.
    assert H["stats"][16]["HFgY"][3] > 5.3  # g=0
    assert M["stats"][16]["HFgY"][3] > 7.3
    return data


def _stats_row(label: str, P: dict) -> str:
    cells = [label]
    for r in RANKS:
        s = P["stats"][r]["slack"]
        cells.append(f"{fz(s[0])} / {fz(s[1])} / {fz(s[2])}")
        cells.append(f"{fz(s[3])} / {fz(s[4])}")
    return "| " + " | ".join(cells) + " |"


def _hf_row(label: str, P: dict) -> str:
    g0 = " / ".join(fz(P["stats"][r]["HFgY"][3]) for r in RANKS)
    g1 = " / ".join(fz(P["stats"][r]["HFgY"][4]) for r in RANKS)
    return f"| {label} | {g0} | {g1} |"


def report(data: dict) -> None:
    print("TOY MODEL (Tier 2). Two-qubit, two-use readout; NOT evidence about")
    print("hadronic or QCD physics; no physical claim.\n")
    print(f"Haar-50 pool (CE-9, seed {SEED}): sha256 {data['haar_sha'][:16]}...")
    print(f"ML-200 pool (CE-12, draw {SEED}, eps=0.05): sha256 {data['ml_sha'][:16]}... "
          f"(n={data['ml_n']}, regen={'ok' if data['regen_ok'] else 'FAIL'})")
    print(f"pss vs mlp GAD path, Haar T=1 nested: max term difference "
          f"{max(data['pss_mlp_diffs'].values()):.1e}")
    print()

    print("## Per-rank slack summary (min / median / max over g; endpoints g=0 / g=1)")
    print()
    hdr = "| surface | " + " | ".join(f"r={r} min/med/max | r={r} g=0 / g=1" for r in RANKS) + " |"
    sep = "|---|" + "---|" * (2 * len(RANKS))
    print(hdr)
    print(sep)
    rows = [
        ("Haar-50, GAD T=0, nested", data["haar"]["GAD_T0_nested"]),
        ("Haar-50, GAD T=1, nested", data["haar"]["GAD_T1_nested"]),
        ("Haar-50, GAD T=inf, nested", data["haar"]["GAD_Tinf_nested"]),
        ("Haar-50, dephasing, nested", data["haar"]["deph_nested"]),
        ("Haar-50, GAD T=1, random", data["haar"]["GAD_T1_random"]),
        ("ML-200, GAD T=0, nested", data["ml"]["GAD_T0_nested"]),
        ("ML-200, GAD T=1, nested", data["ml"]["GAD_T1_nested"]),
        ("ML-200, GAD T=inf, nested", data["ml"]["GAD_Tinf_nested"]),
        ("ML-200, dephasing, nested", data["ml"]["deph_nested"]),
        ("ML-200, GAD T=1, random", data["ml"]["GAD_T1_random"]),
    ]
    for lab, P in rows:
        print(_stats_row(lab, P))
        assert P["corr"] == 44 and P["orig"] == 0
    print()

    print("## Slack vs g, primary surfaces (nested Z, bits)")
    print()
    for lab, P in (
        ("Haar-50, GAD T=1, nested", data["haar"]["GAD_T1_nested"]),
        ("ML-200, GAD T=1, nested", data["ml"]["GAD_T1_nested"]),
        ("Haar-50, GAD T=0, nested", data["haar"]["GAD_T0_nested"]),
        ("ML-200, GAD T=0, nested", data["ml"]["GAD_T0_nested"]),
        ("Haar-50, GAD T=inf, nested", data["haar"]["GAD_Tinf_nested"]),
        ("ML-200, GAD T=inf, nested", data["ml"]["GAD_Tinf_nested"]),
    ):
        print(f"**{lab}**")
        print()
        print(md_table(P["slack"], data["gammas"], data["ranks"]))
        print()

    print("## H(F|Y) at g=0 and g=1 (does the procedural share collapse?)")
    print()
    print("| surface | H(F|Y) at g=0, r=2/4/8/16 | H(F|Y) at g=1, r=2/4/8/16 |")
    print("|---|---|---|")
    for lab, P in (
        ("Haar-50, GAD T=1, nested (all T agree at g=0)", data["haar"]["GAD_T1_nested"]),
        ("ML-200, GAD T=1, nested (all T agree at g=0)", data["ml"]["GAD_T1_nested"]),
        ("Haar-50, dephasing, nested (flat in g)", data["haar"]["deph_nested"]),
        ("ML-200, dephasing, nested (flat in g)", data["ml"]["deph_nested"]),
    ):
        print(_hf_row(lab, P))
    print()
    print(f"log2 50 = {math.log2(50):.3f}; log2 200 = {math.log2(200):.3f}. "
          f"At g=1 under GAD, H(F|Y) equals the pool entropy at every rank.")
    print()

    print("## Bound counts")
    print()
    print("On every surface above (44 points = 11 values of g x 4 ranks): "
          "corrected bound I(X;Y)+I(F;Y)<=H(Y) holds 44/44; "
          "original form I(X;Y)+H(F|Y)<=H(Y) holds 0/44. "
          "H(Y) never exceeds 4 bits (log2 of the 16-symbol alphabet).")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="self-checks only")
    args = ap.parse_args()
    data = self_checks()
    print("self-checks passed")
    if not args.check:
        print()
        report(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
