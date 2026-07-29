#!/usr/bin/env python3
"""
M11 Phase 2 — multi-step Boolean channel load ledger.

Ontology (matches synthesis/m11-idem-to-load.md):
  Microstate: fair bits (X1, X2, X3); composed maps
  Channel steps:
    k=0  id prior on X = (X1,X2,X3)
    k=1  A = X1 ∧ X2          (high export / AND-like)
    k=2  B = A ∨ X3           (lower irreversibility than AND)
  Output Y_k: declared public result of that step (joint bits for id;
              A at k=1; B at k=2). Intermediate register keeps (A, X3)
              for the second gate.
  H_c: exact Shannon of the declared output under the pushforward of
       the uniform input measure (finite support).

Load proxies (weights β'=γ'=δ'=1; no continuum constants):
  L_E  — active gate ops this step
  L_S  — export flux H(preimage vars | Y) for that evaluation
         (also report |ΔH_c| of declared outputs as a multi-step diagnostic)
  L_B  — mean soft lost-recoverability mass on the gate inputs

Optional discrete load clock (diagnostic only, not continuum τ):
  k_eff cumulative sum_j 1/(1 + α' L_disc,j) with α' = 0.1 conventional.

Locked L reading: high |ΔH_c| or high H(X|Y) ⇒ high L_S (asserted).

Non-claims (do not assert from this script):
  - continuum L(ρ,g) equality, L ≡ G, Einstein/Newton from Boolean gates
  - GfE / dual-toy residual H_c identity
  - gravity recovery of any kind; discrete k_eff is not continuum proper time

Run:
  .venv/bin/python simulations/classical/m11_multistep_boolean_ledger.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

# Conventional load-clock weight — diagnostic only (not continuum α).
ALPHA_PRIME = 0.1


def shannon(probs: Iterable[float], base: float = 2.0) -> float:
    """Shannon entropy in the given base; zero-mass outcomes ignored."""
    h = 0.0
    logb = math.log(base)
    for p in probs:
        if p > 0.0:
            h -= p * math.log(p) / logb
    return h


# ---------------------------------------------------------------------------
# Finite ensemble: uniform on {0,1}^3
# ---------------------------------------------------------------------------

World = Tuple[int, int, int]  # (x1, x2, x3)


def fair_worlds() -> List[Tuple[World, float]]:
    mass = 1.0 / 8.0
    out: List[Tuple[World, float]] = []
    for x1 in (0, 1):
        for x2 in (0, 1):
            for x3 in (0, 1):
                out.append(((x1, x2, x3), mass))
    return out


def pushforward(
    worlds: Sequence[Tuple[World, float]], f: Callable[[World], object]
) -> Dict[object, float]:
    dist: Dict[object, float] = {}
    for w, p in worlds:
        y = f(w)
        dist[y] = dist.get(y, 0.0) + p
    return dist


def conditional_entropy_input_given_y(
    worlds: Sequence[Tuple[World, float]],
    f: Callable[[World], object],
    input_proj: Callable[[World], object],
) -> float:
    """
    H(U|Y) where U = input_proj(world), Y = f(world).

    Exact: sum_y p(y) H(U | Y=y) over finite support.
    """
    # joint masses on (y, u)
    joint: Dict[Tuple[object, object], float] = {}
    py: Dict[object, float] = {}
    for w, p in worlds:
        y = f(w)
        u = input_proj(w)
        joint[(y, u)] = joint.get((y, u), 0.0) + p
        py[y] = py.get(y, 0.0) + p

    h = 0.0
    for y, p_y in py.items():
        if p_y <= 0.0:
            continue
        # masses of u | y
        masses: List[float] = []
        for (yy, _u), mass in joint.items():
            if yy == y:
                masses.append(mass / p_y)
        h += p_y * shannon(masses)
    return h


def soft_decay_mass_for_map(
    worlds: Sequence[Tuple[World, float]],
    f: Callable[[World], object],
    input_coords: Sequence[Callable[[World], int]],
) -> float:
    """
    Mean soft lost-recoverability over declared gate inputs.

    Preimage size is measured in the *projected gate-input* space (unique
    tuples of input_coords), not full-world multiplicity — free spectator
    bits must not inflate |preimage| (matches Phase-1 AND soft decay).

    For each y, each input coordinate: d = 0 if fixed on preimage, else
    1 - 1/|preimage_proj(y)|. Ensemble-average mean over coordinates under p_X.
    """
    pre: Dict[object, List[Tuple[World, float]]] = {}
    for w, p in worlds:
        y = f(w)
        pre.setdefault(y, []).append((w, p))

    total = 0.0
    n_coords = len(input_coords)
    for w, p in worlds:
        y = f(w)
        group = pre[y]
        proj_set = {
            tuple(getter(ww) for getter in input_coords) for ww, _ in group
        }
        n = len(proj_set)
        if n <= 1:
            d_mean = 0.0
        else:
            soft = 1.0 - 1.0 / n
            losses = []
            for getter in input_coords:
                vals = {getter(ww) for ww, _ in group}
                losses.append(0.0 if len(vals) == 1 else soft)
            d_mean = sum(losses) / n_coords
        total += p * d_mean
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
    dH_c: float  # |H_c(k) - H_c(k-1)| diagnostic; 0 at baseline
    k_eff_cum: float  # cumulative load-clock diagnostic
    notes: str


def run_multistep_boolean_ledger() -> List[LedgerRow]:
    worlds = fair_worlds()

    # --- k=0: id prior on full input ---
    f_id = lambda w: w  # noqa: E731 — clarity over style for local maps
    H_X = shannon(pushforward(worlds, f_id).values())  # 3 bits

    rows: List[LedgerRow] = [
        LedgerRow(
            k=0,
            description="id prior on X=(X1,X2,X3) [baseline]",
            H_c=H_X,
            L_E=0.0,
            L_S=0.0,
            L_B=0.0,
            L_disc=0.0,
            export=0.0,
            dH_c=0.0,
            k_eff_cum=0.0,
            notes="idle identity — low L (not stockpile-as-load)",
        )
    ]
    k_eff = 0.0

    # --- k=1: A = X1 AND X2 (high export) ---
    f_and = lambda w: w[0] & w[1]  # noqa: E731
    py_a = pushforward(worlds, f_and)
    H_A = shannon(py_a.values())
    export_and = conditional_entropy_input_given_y(
        worlds, f_and, lambda w: (w[0], w[1])
    )
    # Chain rule on the two AND inputs: H(X1,X2)=2 = H(A)+H(X1,X2|A)
    H_x12 = 2.0
    chain_and = abs(H_x12 - (H_A + export_and))
    L_E1 = 1.0
    L_S1 = export_and  # high for AND
    L_B1 = soft_decay_mass_for_map(
        worlds, f_and, [lambda w: w[0], lambda w: w[1]]
    )
    L_disc1 = L_E1 + L_S1 + L_B1
    dH1 = abs(H_A - H_X)  # multi-step diagnostic (declared outputs differ in type)
    k_eff += 1.0 / (1.0 + ALPHA_PRIME * L_disc1)
    rows.append(
        LedgerRow(
            k=1,
            description="A = X1 AND X2 [high export]",
            H_c=H_A,
            L_E=L_E1,
            L_S=L_S1,
            L_B=L_B1,
            L_disc=L_disc1,
            export=export_and,
            dH_c=dH1,
            k_eff_cum=k_eff,
            notes=(
                f"chain |H(X12)-H(A)-H(X12|A)|={chain_and:.2e}; "
                f"P(A=1)={py_a.get(1, 0.0):.3f}"
            ),
        )
    )

    # --- k=2: B = A OR X3 (lower export than AND on two fair bits) ---
    f_or = lambda w: (w[0] & w[1]) | w[2]  # noqa: E731
    # Gate inputs for this step: (A, X3) where A = X1∧X2
    f_or_inputs = lambda w: ((w[0] & w[1]), w[2])  # noqa: E731
    py_b = pushforward(worlds, f_or)
    H_B = shannon(py_b.values())
    export_or = conditional_entropy_input_given_y(worlds, f_or, f_or_inputs)
    # H(A,X3) under pushforward
    H_ax3 = shannon(pushforward(worlds, f_or_inputs).values())
    chain_or = abs(H_ax3 - (H_B + export_or))
    L_E2 = 1.0
    L_S2 = export_or
    L_B2 = soft_decay_mass_for_map(
        worlds,
        f_or,
        # recoverability of (A, X3) coordinates via preimages of B under full world
        # Use soft decay on the two logical gate inputs by projecting worlds
        [lambda w: (w[0] & w[1]), lambda w: w[2]],
    )
    L_disc2 = L_E2 + L_S2 + L_B2
    dH2 = abs(H_B - H_A)
    k_eff += 1.0 / (1.0 + ALPHA_PRIME * L_disc2)
    rows.append(
        LedgerRow(
            k=2,
            description="B = A OR X3 [lower export]",
            H_c=H_B,
            L_E=L_E2,
            L_S=L_S2,
            L_B=L_B2,
            L_disc=L_disc2,
            export=export_or,
            dH_c=dH2,
            k_eff_cum=k_eff,
            notes=(
                f"chain |H(A,X3)-H(B)-H(A,X3|B)|={chain_or:.2e}; "
                f"P(B=1)={py_b.get(1, 0.0):.3f}; H(A,X3)={H_ax3:.5f}"
            ),
        )
    )

    # Locked-reading unit checks
    assert L_S1 > 1.0, "AND step: expected substantial export flux ⇒ high L_S"
    assert L_S2 < L_S1, "OR-after-AND should have lower export than AND on fair bits"
    assert L_S2 > 0.5, "OR step still irreversible: export should be material"
    # high export ⇒ high L_S (not inverse)
    assert rows[1].L_S >= rows[1].export - 1e-15
    assert rows[2].L_S >= rows[2].export - 1e-15
    assert chain_and < 1e-12 and chain_or < 1e-12, "chain rule on finite supports"
    # Projected soft decay on AND inputs matches Phase-1 L_B = 0.5
    assert abs(L_B1 - 0.5) < 1e-12, f"AND L_B expected 0.5, got {L_B1}"

    # Explicit locked reading: high |ΔH_c| or high H(X|Y) ⇒ high L_S
    # Compare the two active steps: larger export must pair with larger L_S
    assert (export_and > export_or) == (L_S1 > L_S2)

    return rows


def format_table(rows: Sequence[LedgerRow]) -> str:
    header = (
        f"{'k':>3}  {'H_c':>8}  {'L_E':>6}  {'L_S':>8}  {'L_B':>8}  "
        f"{'L_disc':>8}  {'export':>8}  {'|dHc|':>8}  {'k_eff':>8}  description"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.k:3d}  {r.H_c:8.5f}  {r.L_E:6.3f}  {r.L_S:8.5f}  {r.L_B:8.5f}  "
            f"{r.L_disc:8.5f}  {r.export:8.5f}  {r.dH_c:8.5f}  {r.k_eff_cum:8.5f}  "
            f"{r.description}"
        )
    return "\n".join(lines)


def main() -> None:
    rows = run_multistep_boolean_ledger()

    print("=" * 88)
    print("M11 Phase 2 — multi-step Boolean load ledger")
    print("Design: synthesis/m11-idem-to-load.md §10 Phase 2")
    print("=" * 88)
    print()
    print(format_table(rows))
    print()
    print(f"Load clock α' = {ALPHA_PRIME} (diagnostic only; not continuum τ).")
    print(f"  final k_eff cumulative = {rows[-1].k_eff_cum:.6f}")
    print("  (compare naive step count = 2 active evaluations)")
    print()
    r1, r2 = rows[1], rows[2]
    print("Sanity:")
    print(f"  H(X)     = {rows[0].H_c:.6f} bits  (expect 3)")
    print(f"  H(A)     = {r1.H_c:.6f} bits  (expect h2(1/4) ≈ 0.811278)")
    print(f"  export₁  = {r1.export:.6f} bits  (AND, expect ≈ 1.188722)")
    print(f"  H(B)     = {r2.H_c:.6f} bits  (expect h2(5/8) ≈ 0.954434)")
    print(f"  export₂  = {r2.export:.6f} bits  (OR step, lower than AND)")
    print(f"  L_S,₁ > L_S,₂ : {r1.L_S:.5f} > {r2.L_S:.5f}  (PASS locked reading)")
    print()
    print("Locked reading check: high export / high H(X|Y) ⇒ high L_S (PASS).")
    print()
    print("NON-CLAIMS: not continuum L, not L≡G, not gravity, not dual-toy H_c;")
    print("            k_eff is a discrete diagnostic only (not continuum τ).")
    print("=" * 88)


if __name__ == "__main__":
    main()
