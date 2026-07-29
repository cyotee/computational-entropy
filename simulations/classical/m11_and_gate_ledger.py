#!/usr/bin/env python3
"""
M11 Phase 1 — pure accounting ledger: irreversible AND-gate.

Ontology (matches synthesis/m11-idem-to-load.md):
  Microstate: fair bits (X1, X2) and map f = AND
  Channel step: one evaluation Y = X1 ∧ X2
  Output Y: declared public result of the gate
  H_c: Shannon entropy of Y only (foundations)

Load proxies (weights β'=γ'=δ'=1; no continuum constants):
  L_E  — active work (one gate op; optional: inputs touched)
  L_S  — export flux H(X|Y) as single-shot entropy-production proxy
  L_B  — mean lost-recoverability mass over inputs (soft decay)

Locked L reading: irreversible overwrite / high export ⇒ high L_S, not low.

Non-claims (do not assert from this script):
  - continuum L(ρ,g) equality, L ≡ G, Einstein/Newton from AND-gate
  - GfE / dual-toy residual H_c identity
  - gravity recovery of any kind

Run:
  .venv/bin/python simulations/classical/m11_and_gate_ledger.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

Bit = int
Pair = Tuple[Bit, Bit]


def shannon(probs: Iterable[float], base: float = 2.0) -> float:
    """Shannon entropy in the given base; zero-mass outcomes ignored."""
    h = 0.0
    log = math.log
    for p in probs:
        if p > 0.0:
            h -= p * log(p) / log(base)
    return h


def binary_entropy(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return shannon([p, 1.0 - p])


@dataclass(frozen=True)
class InputWorld:
    x1: Bit
    x2: Bit
    p: float  # prior mass

    @property
    def x(self) -> Pair:
        return (self.x1, self.x2)

    @property
    def y(self) -> Bit:
        return self.x1 & self.x2


def fair_bit_worlds() -> List[InputWorld]:
    """Uniform over {0,1}^2."""
    mass = 0.25
    return [
        InputWorld(0, 0, mass),
        InputWorld(0, 1, mass),
        InputWorld(1, 0, mass),
        InputWorld(1, 1, mass),
    ]


def output_distribution(worlds: Sequence[InputWorld]) -> Dict[Bit, float]:
    py: Dict[Bit, float] = {0: 0.0, 1: 0.0}
    for w in worlds:
        py[w.y] += w.p
    return py


def preimages(worlds: Sequence[InputWorld]) -> Dict[Bit, List[InputWorld]]:
    pre: Dict[Bit, List[InputWorld]] = {0: [], 1: []}
    for w in worlds:
        pre[w.y].append(w)
    return pre


def soft_decay(y: Bit, pre: Dict[Bit, List[InputWorld]]) -> Tuple[float, float]:
    """
    Soft recoverability per input coordinate for a fixed observed y.

    d_i = 1 - 1/|preimage(y)| when preimage size > 0, applied uniformly
    to both inputs when the coordinate is not fixed by the preimage;
    else 0 if the coordinate is constant across the preimage.

    For AND:
      y=1 → preimage {(1,1)} → both inputs fixed → d = (0, 0)
      y=0 → preimage {(0,0),(0,1),(1,0)} → x1 and x2 not fixed → soft loss
    """
    worlds = pre[y]
    n = len(worlds)
    if n == 0:
        return (1.0, 1.0)
    if n == 1:
        return (0.0, 0.0)

    def coord_loss(getter) -> float:
        vals = {getter(w) for w in worlds}
        if len(vals) == 1:
            return 0.0
        # soft: 1 - 1/|preimage| as unidentifiability of the joint input bit
        return 1.0 - 1.0 / n

    return (coord_loss(lambda w: w.x1), coord_loss(lambda w: w.x2))


def hard_decay(y: Bit, pre: Dict[Bit, List[InputWorld]]) -> Tuple[int, int]:
    """Hard {0,1} recoverability: 0 iff unique preimage forces the bit."""
    worlds = pre[y]
    if len(worlds) <= 1:
        return (0, 0)

    def fixed(getter) -> int:
        vals = {getter(w) for w in worlds}
        return 0 if len(vals) == 1 else 1

    return (fixed(lambda w: w.x1), fixed(lambda w: w.x2))


def conditional_entropy_x_given_y(
    worlds: Sequence[InputWorld], py: Dict[Bit, float], pre: Dict[Bit, List[InputWorld]]
) -> float:
    """H(X|Y) = sum_y p(y) H(X|Y=y)."""
    h = 0.0
    for y, p_y in py.items():
        if p_y <= 0.0:
            continue
        # renormalize preimage masses
        masses = [w.p / p_y for w in pre[y]]
        h += p_y * shannon(masses)
    return h


def mean_soft_decay_mass(
    worlds: Sequence[InputWorld], pre: Dict[Bit, List[InputWorld]]
) -> float:
    """Ensemble average of (d1+d2)/2 under p_X (via pushforward on y)."""
    total = 0.0
    for w in worlds:
        d1, d2 = soft_decay(w.y, pre)
        total += w.p * 0.5 * (d1 + d2)
    return total


@dataclass
class LedgerRow:
    k: int
    description: str
    H_c: float
    L_E: float
    L_S: float
    L_B: float
    L_disc: float
    export: float
    H_X: float
    notes: str


def run_and_gate_ledger() -> List[LedgerRow]:
    worlds = fair_bit_worlds()
    py = output_distribution(worlds)
    pre = preimages(worlds)

    H_X = shannon([w.p for w in worlds])  # = 2 bits
    H_Y = shannon(py.values())  # ≈ 0.811
    H_XgY = conditional_entropy_x_given_y(worlds, py, pre)
    # chain rule sanity: H(X) = H(Y) + H(X|Y)
    chain_err = abs(H_X - (H_Y + H_XgY))

    L_E = 1.0  # one gate evaluation (active work)
    L_S = H_XgY  # single-shot export flux proxy (locked: high export ⇒ high L)
    L_B = mean_soft_decay_mass(worlds, pre)
    L_disc = L_E + L_S + L_B  # β'=γ'=δ'=1

    # Identity map as "prior channel" baseline (optional comparison row)
    # Before AND: if channel were id on (X1,X2), H_c = 2, L_S flux not yet spent.
    rows = [
        LedgerRow(
            k=0,
            description="id prior on X=(X1,X2) [baseline]",
            H_c=H_X,
            L_E=0.0,
            L_S=0.0,
            L_B=0.0,
            L_disc=0.0,
            export=0.0,
            H_X=H_X,
            notes="no computation; idle identity — low L (not stockpile-as-load)",
        ),
        LedgerRow(
            k=1,
            description="Y = X1 AND X2 [one evaluation]",
            H_c=H_Y,
            L_E=L_E,
            L_S=L_S,
            L_B=L_B,
            L_disc=L_disc,
            export=H_XgY,
            H_X=H_X,
            notes=(
                f"chain |H(X)-H(Y)-H(X|Y)|={chain_err:.2e}; "
                f"P(Y=1)={py[1]:.3f}; soft L_B=mean lost recoverability"
            ),
        ),
    ]

    # Locked-reading unit check: high export ⇒ high L_S (not low)
    assert L_S > 1.0, "expected substantial export flux for AND"
    assert L_disc > L_E, "load should exceed pure gate cost when export is large"
    assert chain_err < 1e-12, "chain rule must hold exactly on finite model"

    return rows


def soft_decay_by_y(pre: Dict[Bit, List[InputWorld]]) -> Dict[Bit, Tuple[float, float]]:
    return {y: soft_decay(y, pre) for y in (0, 1)}


def hard_decay_by_y(pre: Dict[Bit, List[InputWorld]]) -> Dict[Bit, Tuple[int, int]]:
    return {y: hard_decay(y, pre) for y in (0, 1)}


def format_table(rows: Sequence[LedgerRow]) -> str:
    header = (
        f"{'k':>3}  {'H_c':>8}  {'L_E':>6}  {'L_S':>8}  {'L_B':>8}  "
        f"{'L_disc':>8}  {'export':>8}  description"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.k:3d}  {r.H_c:8.5f}  {r.L_E:6.3f}  {r.L_S:8.5f}  {r.L_B:8.5f}  "
            f"{r.L_disc:8.5f}  {r.export:8.5f}  {r.description}"
        )
    return "\n".join(lines)


def main() -> None:
    worlds = fair_bit_worlds()
    pre = preimages(worlds)
    rows = run_and_gate_ledger()

    print("=" * 72)
    print("M11 Phase 1 — AND-gate pure load ledger")
    print("Design: synthesis/m11-idem-to-load.md")
    print("=" * 72)
    print()
    print(format_table(rows))
    print()
    print("Per-output decay (soft / hard):")
    for y in (0, 1):
        print(f"  Y={y}: soft d={soft_decay_by_y(pre)[y]}, hard d={hard_decay_by_y(pre)[y]}")
    print()
    r1 = rows[1]
    print("Sanity (foundations AND-gate):")
    print(f"  H(X)     = {rows[0].H_c:.6f} bits  (expect 2)")
    print(f"  H_c=H(Y) = {r1.H_c:.6f} bits  (expect h2(1/4) ≈ 0.811278)")
    print(f"  export   = {r1.export:.6f} bits  (expect ≈ 1.188722)")
    print(f"  L_disc   = {r1.L_disc:.6f}  (= L_E + L_S + L_B)")
    print()
    print("Locked reading check: export high ⇒ L_S high during overwrite (PASS).")
    print()
    print("NON-CLAIMS: not continuum L, not L≡G, not gravity, not dual-toy H_c.")
    print("=" * 72)


if __name__ == "__main__":
    main()
