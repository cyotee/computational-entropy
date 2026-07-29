#!/usr/bin/env python3
"""
M11e — Landauer / thermodynamic contact ledger for fair-bit AND.

Ontology (matches synthesis/m11e-landauer-export.md):
  Microstate: fair bits X=(X1,X2); map f = AND
  Protocol R: compute Y = X1 ∧ X2, keep only Y, reset input
  Export / erased bits: n_erased := H(X|Y)  (Shannon bits)
  Landauer (external): Q >= kT ln 2 * n_erased
  In units of kT ln 2: bound = H(X|Y) = L_S (single-shot)

Optional Protocol V: reversible dilation with garbage G;
  H(Y,G)=H(X) while G retained; garbage entropy accounts for export.

Non-claims (do not assert from this script):
  - Newton G, ħ, holographic area, L ≡ G
  - master equation ⇔ continuum GfE
  - continuum L identity; gravity-fitted T or k
  - dual-toy residual H_c as Landauer bits

Run:
  .venv/bin/python simulations/classical/m11_landauer_and_ledger.py
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
    p: float

    @property
    def x(self) -> Pair:
        return (self.x1, self.x2)

    @property
    def y(self) -> Bit:
        return self.x1 & self.x2


def fair_bit_worlds() -> List[InputWorld]:
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


def conditional_entropy_x_given_y(
    worlds: Sequence[InputWorld], py: Dict[Bit, float], pre: Dict[Bit, List[InputWorld]]
) -> float:
    """H(X|Y) = sum_y p(y) H(X|Y=y)."""
    h = 0.0
    for y, p_y in py.items():
        if p_y <= 0.0:
            continue
        masses = [w.p / p_y for w in pre[y]]
        h += p_y * shannon(masses)
    return h


def branch_h_x_given_y(
    py: Dict[Bit, float], pre: Dict[Bit, List[InputWorld]]
) -> Dict[Bit, float]:
    """Per-output H(X|Y=y)."""
    out: Dict[Bit, float] = {}
    for y, p_y in py.items():
        if p_y <= 0.0:
            out[y] = 0.0
            continue
        masses = [w.p / p_y for w in pre[y]]
        out[y] = shannon(masses)
    return out


@dataclass
class LandauerRow:
    protocol: str
    H_X: float
    H_Y: float
    H_XgY: float
    erased_bits: float
    landauer_bound_ktln2: float
    L_S: float
    H_joint: float
    garbage_entropy: float
    notes: str


def run_irreversible_protocol(worlds: Sequence[InputWorld]) -> LandauerRow:
    """Protocol R: keep Y only; export = H(X|Y) erased bits."""
    py = output_distribution(worlds)
    pre = preimages(worlds)

    H_X = shannon([w.p for w in worlds])
    H_Y = shannon(py.values())
    H_XgY = conditional_entropy_x_given_y(worlds, py, pre)
    chain_err = abs(H_X - (H_Y + H_XgY))

    erased = H_XgY
    # Landauer in units of kT ln 2: bound equals erased bits (Shannon base 2)
    bound = erased
    L_S = H_XgY  # single-shot export flux proxy (m11)

    assert chain_err < 1e-12, "chain rule H(X)=H(Y)+H(X|Y) must hold"
    assert abs(bound - erased) < 1e-15, "bound in kT ln 2 units must equal erased bits"
    assert abs(L_S - H_XgY) < 1e-15, "L_S must equal export H(X|Y)"
    assert abs(erased - H_XgY) < 1e-15, "erased bits := H(X|Y)"

    return LandauerRow(
        protocol="R irreversible (reset after AND)",
        H_X=H_X,
        H_Y=H_Y,
        H_XgY=H_XgY,
        erased_bits=erased,
        landauer_bound_ktln2=bound,
        L_S=L_S,
        H_joint=H_Y,  # only Y retained
        garbage_entropy=0.0,
        notes=f"chain |H(X)-H(Y)-H(X|Y)|={chain_err:.2e}; Q >= kT ln2 * {erased:.6f}",
    )


def run_reversible_dilation(worlds: Sequence[InputWorld]) -> LandauerRow:
    """
    Protocol V: reversible dilation R: X → (Y, G) with G = X (full copy).

    Joint (Y,G)=(Y,X) is redundant (Y=f(X)); H(Y,G)=H(X).
    Garbage entropy H(G|Y)=H(X|Y) accounts for export until G is erased.
    No Landauer cost while garbage is retained (bound deferred = 0 now).
    """
    py = output_distribution(worlds)
    pre = preimages(worlds)

    H_X = shannon([w.p for w in worlds])
    H_Y = shannon(py.values())
    H_XgY = conditional_entropy_x_given_y(worlds, py, pre)

    # Joint over (Y, X1, X2): deterministic function of X, so H(Y,G)=H(X)
    # Explicit joint mass on (y, x1, x2)
    joint_probs: List[float] = []
    for w in worlds:
        joint_probs.append(w.p)  # each (y,x) has mass p(x); y determined
    H_joint = shannon(joint_probs)
    # H(G|Y) with G=X: same as H(X|Y)
    garbage_entropy = H_XgY

    # While garbage retained: no erasure yet
    erased_now = 0.0
    bound_now = 0.0
    # Deferred cost if G later reset given Y
    deferred = garbage_entropy

    assert abs(H_joint - H_X) < 1e-12, "dilation must preserve H(Y,G)=H(X)"
    assert abs(garbage_entropy - H_XgY) < 1e-12, "garbage entropy must equal export"
    assert abs(deferred - H_XgY) < 1e-12

    return LandauerRow(
        protocol="V reversible dilation (keep G=X)",
        H_X=H_X,
        H_Y=H_Y,
        H_XgY=H_XgY,
        erased_bits=erased_now,
        landauer_bound_ktln2=bound_now,
        L_S=0.0,  # no flux paid yet; export parked in G
        H_joint=H_joint,
        garbage_entropy=garbage_entropy,
        notes=(
            f"H(Y,G)={H_joint:.6f}; H(G|Y)={garbage_entropy:.6f} "
            f"(= export; deferred Landauer if erase G)"
        ),
    )


def run_erase_garbage_after_dilation(worlds: Sequence[InputWorld]) -> LandauerRow:
    """After Protocol V: erase garbage G given Y — pay Landauer on H(G|Y)."""
    py = output_distribution(worlds)
    pre = preimages(worlds)

    H_X = shannon([w.p for w in worlds])
    H_Y = shannon(py.values())
    H_XgY = conditional_entropy_x_given_y(worlds, py, pre)

    erased = H_XgY  # H(G|Y) with G=X
    bound = erased
    L_S = erased  # export flux realized at erasure step

    assert abs(bound - H_XgY) < 1e-15
    assert abs(L_S - H_XgY) < 1e-15

    return LandauerRow(
        protocol="V→ erase garbage G|Y",
        H_X=H_X,
        H_Y=H_Y,
        H_XgY=H_XgY,
        erased_bits=erased,
        landauer_bound_ktln2=bound,
        L_S=L_S,
        H_joint=H_Y,
        garbage_entropy=0.0,
        notes="same export cost as Protocol R; irreversibility deferred then paid",
    )


def format_table(rows: Sequence[LandauerRow]) -> str:
    header = (
        f"{'protocol':<36}  {'H(X)':>7}  {'H(Y)':>8}  {'H(X|Y)':>8}  "
        f"{'erased':>8}  {'Qmin/(kTln2)':>12}  {'L_S':>8}  {'H(G|Y)':>8}"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.protocol:<36}  {r.H_X:7.5f}  {r.H_Y:8.5f}  {r.H_XgY:8.5f}  "
            f"{r.erased_bits:8.5f}  {r.landauer_bound_ktln2:12.5f}  "
            f"{r.L_S:8.5f}  {r.garbage_entropy:8.5f}"
        )
    return "\n".join(lines)


def main() -> None:
    worlds = fair_bit_worlds()
    py = output_distribution(worlds)
    pre = preimages(worlds)
    branch = branch_h_x_given_y(py, pre)

    row_r = run_irreversible_protocol(worlds)
    row_v = run_reversible_dilation(worlds)
    row_e = run_erase_garbage_after_dilation(worlds)

    # Cross-protocol: deferred erase equals irreversible export
    assert abs(row_e.erased_bits - row_r.erased_bits) < 1e-12
    assert abs(row_v.garbage_entropy - row_r.H_XgY) < 1e-12
    # export equals H(X|Y); bound matches export in bit units
    assert abs(row_r.erased_bits - row_r.H_XgY) < 1e-15
    assert abs(row_r.landauer_bound_ktln2 - row_r.H_XgY) < 1e-15

    # Expected analytics for fair-bit AND
    h_y_expected = binary_entropy(0.25)
    export_expected = 0.75 * math.log(3.0) / math.log(2.0)  # (3/4) log2 3
    assert abs(row_r.H_Y - h_y_expected) < 1e-12
    assert abs(row_r.H_XgY - export_expected) < 1e-12
    assert abs(row_r.H_X - 2.0) < 1e-12

    print("=" * 96)
    print("M11e — Landauer contact ledger: fair-bit AND")
    print("Design: synthesis/m11e-landauer-export.md")
    print("=" * 96)
    print()
    print(format_table([row_r, row_v, row_e]))
    print()
    print("Branch-wise H(X|Y=y):")
    for y in (0, 1):
        n_pre = len(pre[y])
        print(
            f"  Y={y}: P={py[y]:.3f}, |preimage|={n_pre}, "
            f"H(X|Y=y)={branch[y]:.6f} bits"
        )
    print()
    print("Main inequality (Landauer, external):")
    print("  Q >= k_B T ln(2) * H(X|Y)")
    print("  In units of kT ln 2:  Q_min / (kT ln 2) = H(X|Y) = erased bits = L_S")
    print()
    print("Sanity (fair-bit AND):")
    print(f"  H(X)              = {row_r.H_X:.6f} bits  (expect 2)")
    print(f"  H(Y)=H_c          = {row_r.H_Y:.6f} bits  (expect h2(1/4) ≈ 0.811278)")
    print(f"  export H(X|Y)     = {row_r.H_XgY:.6f} bits  (expect (3/4)log2(3) ≈ 1.188722)")
    print(f"  erased bits       = {row_r.erased_bits:.6f}  (= export)")
    print(f"  Q_min/(kT ln 2)   = {row_r.landauer_bound_ktln2:.6f}  (= export)")
    print(f"  L_S (single-shot) = {row_r.L_S:.6f}  (= export)")
    print(f"  garbage H(G|Y)    = {row_v.garbage_entropy:.6f}  (Protocol V; = export)")
    print()
    print("Asserts PASS: export = H(X|Y); bound matches export in bit units;")
    print("  reversible garbage entropy accounts for same export until erased.")
    print()
    print(
        "NON-CLAIMS: not Newton G, not ħ, not holographic area, not L≡G, "
        "not ME⇔GfE, not continuum L, not gravity-fitted T."
    )
    print("=" * 96)


if __name__ == "__main__":
    main()
