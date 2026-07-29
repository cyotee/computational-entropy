#!/usr/bin/env python3
"""
M11 Phase 2 / M12-adjacent — minimal residual multiset shoe load ledger.

Ontology (matches synthesis/m11-idem-to-load.md §7.B pattern, simplified):
  Microstate: residual multiset of binary card classes (R, B)
  Channel step: one draw from the remaining multiset (fixed explicit order)
  Output Y_k: next-card class under the residual multiset (combinatorial)
  H_c: exact Shannon of next-card class P(R)=n_R/N, P(B)=n_B/N
        (binary entropy); H_c=0 when one card remains of known class,
        or when empty

Load proxies (weights β'=γ'=δ'=1; no continuum constants):
  L_E  — count-update cost = 1 per draw (one multiset bucket touched),
         or 2 if both class counts are consulted (we use 1)
  L_S  — |ΔH_c| per draw (predictive entropy flux as info arrives)
  L_B  — H_seq(Ω_k)/H_seq(Ω_0) residual order-entropy ratio
         H_seq = log2(N!) - log2(n_R!) - log2(n_B!)  (uniform residual
         sequences consistent with the multiset)

Honesty / non-claims (do not assert from this script):
  - NOT blackjack EV / strategy ROI / bankroll
  - NOT continuum gravity, L ≡ G, Einstein/Newton recovery
  - NOT ACD-EW dual residual H_c (lattice φ belief dual is a different object)
  - NOT continuum L(ρ,g) equality

Run:
  .venv/bin/python simulations/classical/m11_minimal_shoe_ledger.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

# Explicit fixed shoe sequence (reproducible; not RNG-version dependent).
# 6R + 6B; mixed so H_c / L_S vary (not a sorted trivial run).
FIXED_SHOE: Tuple[str, ...] = (
    "R", "B", "R", "R", "B", "B", "R", "B", "R", "B", "R", "B",
)
N_RED = sum(1 for c in FIXED_SHOE if c == "R")
N_BLACK = sum(1 for c in FIXED_SHOE if c == "B")
assert N_RED == 6 and N_BLACK == 6


def shannon(probs: Iterable[float], base: float = 2.0) -> float:
    h = 0.0
    logb = math.log(base)
    for p in probs:
        if p > 0.0:
            h -= p * math.log(p) / logb
    return h


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return shannon([p, 1.0 - p])


def log2_factorial(n: int) -> float:
    """log2(n!) via sum of logs (exact enough for n <= 12)."""
    if n < 0:
        raise ValueError(n)
    s = 0.0
    for i in range(2, n + 1):
        s += math.log2(i)
    return s


def residual_order_entropy(n_r: int, n_b: int) -> float:
    """
    Entropy (bits) of the uniform distribution over residual sequences
    consistent with multiset counts (n_r, n_b).

    H_seq = log2( (n_r+n_b)! / (n_r! n_b!) )
    """
    n = n_r + n_b
    if n <= 0:
        return 0.0
    return log2_factorial(n) - log2_factorial(n_r) - log2_factorial(n_b)


def next_card_Hc(n_r: int, n_b: int) -> float:
    """H_c = Shannon of next-card class under residual multiset."""
    n = n_r + n_b
    if n <= 0:
        return 0.0
    if n == 1:
        return 0.0  # class is determined
    return binary_entropy(n_r / n)


@dataclass
class LedgerRow:
    k: int
    drawn: str  # card drawn *into* this residual state ("" at k=0)
    n_r: int
    n_b: int
    H_c: float
    L_E: float
    L_S: float
    L_B: float
    L_disc: float
    H_seq: float
    notes: str


def run_minimal_shoe_ledger(
    shoe: Sequence[str] = FIXED_SHOE,
) -> Tuple[List[LedgerRow], List[str]]:
    shoe_list = list(shoe)
    n_r0 = sum(1 for c in shoe_list if c == "R")
    n_b0 = sum(1 for c in shoe_list if c == "B")
    H_seq0 = residual_order_entropy(n_r0, n_b0)

    n_r, n_b = n_r0, n_b0
    rows: List[LedgerRow] = []

    # k=0: full shoe, before any draw
    H0 = next_card_Hc(n_r, n_b)
    rows.append(
        LedgerRow(
            k=0,
            drawn="",
            n_r=n_r,
            n_b=n_b,
            H_c=H0,
            L_E=0.0,
            L_S=0.0,
            L_B=1.0 if H_seq0 > 0 else 0.0,
            L_disc=0.0,
            H_seq=H_seq0,
            notes="full residual multiset; predictive H_c of next class",
        )
    )

    prev_H = H0
    for i, card in enumerate(shoe_list):
        # draw card, update residual
        if card == "R":
            n_r -= 1
        else:
            n_b -= 1
        assert n_r >= 0 and n_b >= 0

        H = next_card_Hc(n_r, n_b)
        H_seq = residual_order_entropy(n_r, n_b)
        L_E = 1.0  # one count-bucket update
        L_S = abs(H - prev_H)
        L_B = (H_seq / H_seq0) if H_seq0 > 0 else 0.0
        L_disc = L_E + L_S + L_B

        rows.append(
            LedgerRow(
                k=i + 1,
                drawn=card,
                n_r=n_r,
                n_b=n_b,
                H_c=H,
                L_E=L_E,
                L_S=L_S,
                L_B=L_B,
                L_disc=L_disc,
                H_seq=H_seq,
                notes=f"after draw {card}; remaining N={n_r + n_b}",
            )
        )
        prev_H = H

    # Sanity: empty shoe at end
    assert n_r == 0 and n_b == 0
    assert rows[-1].H_c == 0.0
    assert rows[-1].H_seq == 0.0

    # Locked reading: late shoe can have large |ΔH_c| when balance breaks
    active = [r for r in rows if r.k > 0]
    assert any(r.L_S > 0 for r in active), "expected some predictive flux"
    # L_S equals |ΔH_c| by construction
    for i in range(1, len(rows)):
        assert abs(rows[i].L_S - abs(rows[i].H_c - rows[i - 1].H_c)) < 1e-12

    # H_seq monotone nonincreasing (removing cards never increases order entropy)
    for i in range(1, len(rows)):
        assert rows[i].H_seq <= rows[i - 1].H_seq + 1e-12

    return rows, shoe_list


def format_table(rows: Sequence[LedgerRow]) -> str:
    header = (
        f"{'k':>3}  {'draw':>4}  {'nR':>3}  {'nB':>3}  {'H_c':>8}  "
        f"{'L_E':>5}  {'L_S':>8}  {'L_B':>8}  {'L_disc':>8}  {'H_seq':>8}"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        draw = r.drawn if r.drawn else "—"
        lines.append(
            f"{r.k:3d}  {draw:>4}  {r.n_r:3d}  {r.n_b:3d}  {r.H_c:8.5f}  "
            f"{r.L_E:5.2f}  {r.L_S:8.5f}  {r.L_B:8.5f}  {r.L_disc:8.5f}  "
            f"{r.H_seq:8.5f}"
        )
    return "\n".join(lines)


def main() -> None:
    rows, shoe = run_minimal_shoe_ledger()

    print("=" * 88)
    print("M11 Phase 2 / M12-adjacent — minimal residual multiset shoe ledger")
    print("Design: synthesis/m11-idem-to-load.md §7.B (simplified R/B)")
    print("=" * 88)
    print()
    print(f"Shoe: {N_RED}R + {N_BLACK}B; fixed sequence (no RNG)")
    print(f"Order: {''.join(shoe)}")
    print()
    print(format_table(rows))
    print()
    r0 = rows[0]
    # find max flux step
    active = [r for r in rows if r.k > 0]
    max_flux = max(active, key=lambda r: r.L_S)
    print("Sanity:")
    print(f"  H_c(0)     = {r0.H_c:.6f} bits  (expect 1.0 for balanced R/B)")
    print(f"  H_seq(0)   = {r0.H_seq:.6f} bits  (log2 C(12,6))")
    print(f"  H_c(final) = {rows[-1].H_c:.6f}")
    print(
        f"  max L_S at k={max_flux.k}: L_S={max_flux.L_S:.6f} "
        f"(draw {max_flux.drawn}, residual {max_flux.n_r}R/{max_flux.n_b}B)"
    )
    print(f"  mean L_disc (k>0) = {sum(r.L_disc for r in active) / len(active):.6f}")
    print()
    print("Locked reading: L_S := |ΔH_c| so fast predictive drop ⇒ high L_S (PASS).")
    print()
    print("HONESTY / NON-CLAIMS:")
    print("  not blackjack EV / strategy ROI; not gravity; not L≡G;")
    print("  not ACD-EW dual residual H_c (lattice belief dual ≠ this H_c);")
    print("  not continuum L(ρ,g).")
    print("=" * 88)


if __name__ == "__main__":
    main()
