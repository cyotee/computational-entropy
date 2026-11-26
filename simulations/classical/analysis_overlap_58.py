#!/usr/bin/env python3
"""Tier 2 toy model: read out the overlap term I(X;F|Y) at the 58 CE-6
identity-failure points (original form I(X;Y)+H(F|Y) <= H(Y)).

    *** TOY MODEL. One-qubit, one-use proof-of-concept. It is NOT evidence
    *** about hadronic or QCD physics and makes no physical claim.

No new simulation. Calls procedural_share_mlpool.ce6_overlap, which recomputes
the deterministic CE-6 one-bit run (variant (a), eps=0.05, alphabet 2) from
the same seeds and pool constructors already in the repo. pool_source="A"
is the original 58/72 set; pool_source="ml" is the Stage 2 pool A-ml (38/81),
printed as a one-line comparison. No new sampling and no parameter change.

Run:

    python simulations/classical/analysis_overlap_58.py            # self-checks + report
    python simulations/classical/analysis_overlap_58.py --check    # self-checks only

THE 58. docs/procedural-share.md section 4, row "(a) eps-class | A | uniform |
  0.05 | 72 | 14 | 58", reproduced in docs/procedural-share-mlpool.md section 5.
  Deficit D = H(F|Y) - H(Y|X). "Covers" means I(X;F|Y) >= D.

GRID. (g, p) only. USES = 1, two-outcome readout. There is no rank dimension.
  Spearman correlations are therefore reported against g and p, not rank.

IDENTITY (theorem; checked). I(X;Y)+I(F;Y) = I(X,F;Y)+I(X;F)-I(X;F|Y).
  The CE-6 inputs do not depend on the candidate, so X is independent of F
  and I(X;F) = 0 (checked).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import procedural_share as ps
import procedural_share_mlpool as mlp


# Printed headlines for pool A, uniform input, locked so a later change of
# the CE-6 hook cannot silently drift the analysis note.
FROZEN_A_UNIFORM = dict(
    n_defined=72,
    n_fail=58,
    covers=0,
    overlap_print="0.0000 / 0.0048 / 0.0285",
    D_print="0.047 / 1.455 / 3.076",
    residual_print="0.047 / 1.452 / 3.048",
    spearman_g_print="-0.892",
    spearman_p_print="0.005",
)


def _fails(rows: list[dict]) -> list[dict]:
    return [r for r in rows if r["deficit"] > 1e-12]


def summarize(rows: list[dict]) -> dict:
    fails = _fails(rows)
    a = np.array([r["IXFgY"] for r in fails])
    d = np.array([r["deficit"] for r in fails])
    g = np.array([r["g"] for r in fails])
    p = np.array([r["p"] for r in fails])
    res = d - a
    return dict(
        n_defined=len(rows),
        n_fail=len(fails),
        covers=int((a >= d - 1e-12).sum()),
        overlap=(float(a.min()), float(np.median(a)), float(a.max())),
        D=(float(d.min()), float(np.median(d)), float(d.max())),
        residual=(float(res.min()), float(np.median(res)), float(res.max())),
        spearman_g=ps.spearman(a, g),
        spearman_p=ps.spearman(a, p),
        spearman_D=ps.spearman(a, d),
        n_zero_overlap=int((np.abs(a) <= 1e-12).sum()),
        n_zero_slack=int(sum(r["slack"] <= 1e-12 for r in fails)),
        max_abs_IXF=max(abs(r["IXF"]) for r in rows),
        max_abs_ident=max(abs(r["ident"]) for r in rows),
    )


def _mmm(t, nd: int) -> str:
    return " / ".join(mlp.fz(v, nd) for v in t)


def self_checks() -> None:
    resA = mlp.ce6_overlap(pool_source="A")
    resM = mlp.ce6_overlap(pool_source="ml")
    su = summarize(resA["uniform"])
    sc = summarize(resA["capacity"])
    sm = summarize(resM["uniform"])
    # Pool A, both inputs: 72 defined, 58 failures, covers 0, X indep F, identity.
    for label, s in (("uniform", su), ("capacity", sc)):
        assert s["n_defined"] == 72 and s["n_fail"] == 58 and s["covers"] == 0, label
        assert s["max_abs_IXF"] < 1e-14 and s["max_abs_ident"] < 1e-14, label
    # Frozen printed headlines (the analysis note).
    f = FROZEN_A_UNIFORM
    assert _mmm(su["overlap"], 4) == f["overlap_print"]
    assert _mmm(su["D"], 3) == f["D_print"]
    assert _mmm(su["residual"], 3) == f["residual_print"]
    assert f"{su['spearman_g']:.3f}" == f["spearman_g_print"]
    assert f"{su['spearman_p']:.3f}" == f["spearman_p_print"]
    assert su["overlap"][0] > -1e-14  # numerical floor; printed as 0.0000
    # Capacity overlap statistics match uniform to the printed precision,
    # as already stated in procedural-share-mlpool.md section 5.
    assert mlp.fz(sc["overlap"][1]) == mlp.fz(su["overlap"][1])
    assert mlp.fz(sc["overlap"][2]) == mlp.fz(su["overlap"][2])
    assert mlp.fz(sc["D"][1], 3) == mlp.fz(su["D"][1], 3)
    # Pool A-ml comparison: 81 defined, 38 failures, covers 0, X indep F.
    assert sm["n_defined"] == 81 and sm["n_fail"] == 38 and sm["covers"] == 0
    assert sm["max_abs_IXF"] < 1e-14 and sm["max_abs_ident"] < 1e-14
    assert abs(sm["overlap"][1]) <= 1e-15  # median overlap is 0
    # No rank key on the CE-6 rows (single-use grid).
    assert all(set(r) <= {"g", "p", "k", "deficit", "IXFgY", "IXF", "slack", "ident"}
               for r in resA["uniform"])


def report() -> None:
    resA = mlp.ce6_overlap(pool_source="A")
    resM = mlp.ce6_overlap(pool_source="ml")
    print("Overlap I(X;F|Y) at the CE-6 original-form failure points")
    print("Toy model. NOT evidence about hadronic or QCD physics.")
    print("Source: procedural_share_mlpool.ce6_overlap; no new sampling.\n")
    print("The CE-6 one-bit grid is (g, p) only (USES=1, two-outcome readout).")
    print("There is no rank dimension; no rank correlation is reported.\n")
    print("| pool | input | defined | original fails | I(X;F|Y) min / median / max | "
          "D min / median / max | D - I(X;F|Y) min / median / max | covers | "
          "Spearman vs g | Spearman vs p | max |I(X;F)| | max |identity| |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for pool, res in (("A", resA), ("A-ml", resM)):
        for inp, rows in res.items():
            s = summarize(rows)
            print(
                f"| {pool} | {inp} | {s['n_defined']} | {s['n_fail']} | "
                f"{_mmm(s['overlap'], 4)} | {_mmm(s['D'], 3)} | {_mmm(s['residual'], 3)} | "
                f"{s['covers']}/{s['n_fail']} | {s['spearman_g']:.3f} | {s['spearman_p']:.3f} | "
                f"{s['max_abs_IXF']:.1e} | {s['max_abs_ident']:.1e} |"
            )
    su = summarize(resA["uniform"])
    sm = summarize(resM["uniform"])
    print()
    print(f"Pool A, uniform (the 58): {su['n_zero_overlap']} failures have "
          f"I(X;F|Y) consistent with 0 (numerical floor 1e-15), of which "
          f"{su['n_zero_slack']} have zero corrected-bound slack. "
          f"Spearman(I(X;F|Y), D) = {su['spearman_D']:.3f}.")
    print()
    print(f"Pool A-ml, uniform (the 38), one-line comparison: "
          f"I(X;F|Y) {_mmm(sm['overlap'], 4)} bits; covers {sm['covers']}/{sm['n_fail']}; "
          f"median D - overlap = {mlp.fz(sm['residual'][1], 3)} bits "
          f"(median overlap is 0: {sm['n_zero_overlap']}/{sm['n_fail']} failures "
          f"have overlap consistent with 0); "
          f"Spearman vs g / p = {sm['spearman_g']:.3f} / {sm['spearman_p']:.3f}.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="self-checks only")
    args = ap.parse_args()
    self_checks()
    print("self-checks passed")
    if not args.check:
        print()
        report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
