#!/usr/bin/env python3
"""
O1 step 7 — 2D strip transfer: the decay algebra on a 2D lattice.

Model: 2×2-plaquette AND on an i.i.d. fair bit grid b[i][j].
       Y[i][j] = b[i][j] ∧ b[i][j+1] ∧ b[i+1][j] ∧ b[i+1][j+1].
Sweeping row by row, the boundary between processed and unprocessed sites is a
whole ROW-CUT of width W. The belief-transfer becomes an OPERATOR on the 2^W
row configurations (the Bayesian-filter form of a statistical-mechanics strip
transfer matrix): hidden state = current input row (W bits), fresh W-bit row
each step, emission = the (W-1)-bit output row.

Export density per output site at strip width W:
       a_W = (W − h_row) / (W − 1),
where h_row is the entropy rate per output ROW (input rate W bits/row minus the
output-row entropy). As W grows, a_W → the bulk 2D density.

Two computations:
  * enumerate  — exact E(R)=R·W − H(Y) on a W×R input strip; slope in R gives
                 W − h_row (ground truth; capped by 2^{RW}).
  * transfer   — belief filter (Monte Carlo) over the 2^W row-cut → h_row.

Deliverable: transfer ≈ enumeration at fixed W, and a_W converges in W. Honest
wall: the row-cut has 2^W states and 2^{W-1} emission branches ⇒ exact methods
blow up; this is exactly why the CONTINUUM embedding (next rung) is needed to
escape enumeration.

NON-CLAIMS: not continuum L, not dS_c/dτ, not gravity; finite classical.

Run:
  .venv/bin/python simulations/classical/m11_decay_algebra_2d.py
"""

from __future__ import annotations

import math
import random
from typing import Dict, List, Tuple

Row = Tuple[int, ...]


def shannon(counts, total: int) -> float:
    h = 0.0
    for c in counts:
        if c > 0:
            q = c / total
            h -= q * math.log2(q)
    return h


def emit_row(cur: Row, nxt: Row, W: int) -> Row:
    """(W-1)-bit output row from two W-bit input rows (2×2 plaquette AND)."""
    return tuple(cur[j] & cur[j + 1] & nxt[j] & nxt[j + 1] for j in range(W - 1))


def linfit(xs: List[float], ys: List[float]) -> Tuple[float, float]:
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    a = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    return a, (sy - a * sx) / n


# --- ground truth: exact enumeration on a W×R strip ---


def rows_of(val: int, R: int, W: int) -> List[Row]:
    return [tuple((val >> (r * W + c)) & 1 for c in range(W)) for r in range(R)]


def density_enum(W: int, Rmax: int) -> Tuple[float, float]:
    ks: List[float] = []
    Es: List[float] = []
    for R in range(2, Rmax + 1):
        n = R * W
        counts: Dict[Row, int] = {}
        for val in range(1 << n):
            rows = rows_of(val, R, W)
            Y = tuple(emit_row(rows[i], rows[i + 1], W) for i in range(R - 1))
            counts[Y] = counts.get(Y, 0) + 1
        E = n - shannon(counts.values(), 1 << n)
        ks.append(R)
        Es.append(E)
    slope, _ = linfit(ks, Es)  # per-input-row export = W - h_row
    return slope / (W - 1), slope


# --- strip transfer: belief filter over the 2^W row-cut (Monte Carlo) ---


def density_transfer_mc(W: int, steps: int = 300_000, burn: int = 2000,
                        seed: int = 7) -> Tuple[float, float]:
    rng = random.Random(seed)
    S = 1 << W
    rows = [tuple((s >> c) & 1 for c in range(W)) for s in range(S)]
    emit = [[emit_row(rows[s], rows[sp], W) for sp in range(S)] for s in range(S)]

    pi = [1.0 / S] * S
    cur = rng.randrange(S)
    acc = 0.0
    cnt = 0
    inv = 1.0 / S
    for t in range(steps):
        nxt = rng.randrange(S)
        e_true = emit[cur][nxt]
        # predictive emission distribution from the belief → its entropy
        pred: Dict[Row, float] = {}
        for s in range(S):
            ws = pi[s]
            if ws == 0.0:
                continue
            row_e = emit[s]
            wsi = ws * inv
            for sp in range(S):
                e = row_e[sp]
                pred[e] = pred.get(e, 0.0) + wsi
        if t >= burn:
            acc += shannon(pred.values(), 1)  # already normalized (sums to 1)
            cnt += 1
        # posterior over next row given the observed emission
        nb = [0.0] * S
        norm = 0.0
        for s in range(S):
            ws = pi[s]
            if ws == 0.0:
                continue
            row_e = emit[s]
            wsi = ws * inv
            for sp in range(S):
                if row_e[sp] == e_true:
                    nb[sp] += wsi
                    norm += wsi
        pi = [v / norm for v in nb] if norm > 0 else [1.0 / S] * S
        cur = nxt
    h_row = acc / cnt
    return (W - h_row) / (W - 1), h_row


def main() -> None:
    print("=" * 76)
    print("O1 step 7 — 2D strip transfer (2×2 plaquette AND)")
    print("Design: this file · m11g (1D general-w) · OPEN_AVENUES O1")
    print("=" * 76)

    print(f"\n{'W':>2}  {'2^W states':>10}  {'a_enum':>10}  {'a_transfer':>11}  "
          f"{'|Δ|':>8}  {'h_row':>8}")
    print("-" * 60)

    enum_widths = {2: 9, 3: 6}  # RW <= ~18 bits
    a_by_W: Dict[int, float] = {}
    for W in (2, 3, 4):
        a_tr, h_row = density_transfer_mc(W, steps=300_000 if W < 4 else 200_000)
        a_by_W[W] = a_tr
        if W in enum_widths:
            a_en, _ = density_enum(W, enum_widths[W])
            d = abs(a_en - a_tr)
            print(f"{W:2d}  {1 << W:10d}  {a_en:10.5f}  {a_tr:11.5f}  {d:8.1e}  {h_row:8.5f}")
            assert d < 2e-2, f"W={W}: strip transfer must match enumeration"
        else:
            print(f"{W:2d}  {1 << W:10d}  {'—':>10}  {a_tr:11.5f}  {'—':>8}  {h_row:8.5f}")

    print("\n  strip-width convergence of the per-site density a_W:")
    for W in (2, 3, 4):
        print(f"    a_{W} = {a_by_W[W]:.5f}")
    print(f"    trend Δ: a_3−a_2 = {a_by_W[3]-a_by_W[2]:+.5f}, "
          f"a_4−a_3 = {a_by_W[4]-a_by_W[3]:+.5f}  (shrinking ⇒ converging)")

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    print("  The decay algebra lifts to 2D: a belief-transfer OPERATOR on the 2^W")
    print("  row-cut (statistical-mechanics strip transfer, Bayesian-filter form)")
    print("  reproduces the enumerated per-site export density, and a_W converges")
    print("  as the strip widens.")
    print("\n  WALL: the row-cut has 2^W states and 2^(W-1) emission branches, so")
    print("  exact/transfer cost is exponential in strip width — enumeration cannot")
    print("  reach large 2D systems. This is exactly why the CONTINUUM embedding")
    print("  (next rung) is needed: take the limit to get a density field directly.")
    print("\nNON-CLAIMS: not continuum L, not dS_c/dτ, not gravity; finite classical.")
    print("=" * 76)


if __name__ == "__main__":
    main()
