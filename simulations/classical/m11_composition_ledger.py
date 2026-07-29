#!/usr/bin/env python3
"""
M11d — composition laws ledger for H_c^disc and L^disc (finite classical).

Ontology (matches synthesis/m11-idem-to-load.md · m11d-composition-laws.md):
  Microstate: fair bits X = (X1, X2) i.i.d., H(X) = 2.

  --- Path dependence (circuit model: later stages may read residual wires) ---
  Path Direct (D):
    Z = X1 ∧ X2                         [1 active op]

  Path Circuit (C) — intermediate publish then AND (same final law):
    Y = X1                               [1 op: wire publish / projection]
    Z = Y ∧ X2                           [1 op: AND; X2 still on a wire]
    Final Z ~ Direct AND; cumulative stage L_S differs.

  --- Markov pure cascade (Z = g(Y) only; for export additivity lemma) ---
  Path Markov (M):
    Y = X1 ∧ X2
    Z = NOT(Y)                           [deterministic post-process of Y alone]
    Witness: H(X|Z) = H(X|Y) + H(Y|Z)

  --- DPI / L_B non-additivity ---
    W = NOT(AND) already on path M final
    Independent product of two ANDs on (X1,X2)×(X3,X4) for L_B sum vs mean

H_c: exact Shannon of declared outputs under uniform pushforward (Tag E).

Load proxies (β'=γ'=δ'=1; no continuum constants):
  L_E  — # active ops at a stage (or cumulative sum along a path)
  L_S  — export H(declared gate inputs | stage output); path cost = sum of stages
  L_B  — mean soft lost-recoverability mass on declared gate inputs

Demonstrates (exact finite Shannon + asserts):
  1. Export additivity along a deterministic pure cascade Z=g(Y), Y=f(X):
       H(X|Z) = H(X|Y) + H(Y|Z)
  2. Circuit path dependence of cumulative L_S:
       same final H(Z) (AND law) with different Σ L_S along D vs C
  3. L_E sums with sequential active ops
  4. DPI: H(g(Y)) ≤ H(Y) for deterministic g (NOT on AND output; equality)
  5. L_B non-additivity: sum of regional L_B ≠ global mean soft mass
     (and circuit Σ stage L_B ≠ L_B of direct joint map)

NON-CLAIMS (do not assert from this script):
  - continuum L(ρ,g) equality, L ≡ G, Einstein/Newton from Boolean composition
  - GfE / dual-toy residual H_c identity; master equation ⇔ continuum GfE
  - gravity recovery of any kind; composition laws of continuum load
  - L^disc continuum limit theorem

Run:
  .venv/bin/python simulations/classical/m11_composition_ledger.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

World2 = Tuple[int, int]  # (x1, x2)
World4 = Tuple[int, int, int, int]  # (x1, x2, x3, x4)


def shannon(probs: Iterable[float], base: float = 2.0) -> float:
    """Shannon entropy in the given base; zero-mass outcomes ignored."""
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


# ---------------------------------------------------------------------------
# Finite ensembles
# ---------------------------------------------------------------------------


def fair_worlds2() -> List[Tuple[World2, float]]:
    mass = 0.25
    return [((x1, x2), mass) for x1 in (0, 1) for x2 in (0, 1)]


def fair_worlds4() -> List[Tuple[World4, float]]:
    mass = 1.0 / 16.0
    out: List[Tuple[World4, float]] = []
    for x1 in (0, 1):
        for x2 in (0, 1):
            for x3 in (0, 1):
                for x4 in (0, 1):
                    out.append(((x1, x2, x3, x4), mass))
    return out


def pushforward(
    worlds: Sequence[Tuple[object, float]], f: Callable[[object], object]
) -> Dict[object, float]:
    dist: Dict[object, float] = {}
    for w, p in worlds:
        y = f(w)
        dist[y] = dist.get(y, 0.0) + p
    return dist


def conditional_entropy(
    worlds: Sequence[Tuple[object, float]],
    f_y: Callable[[object], object],
    f_u: Callable[[object], object],
) -> float:
    """H(U|Y) exact on finite support."""
    joint: Dict[Tuple[object, object], float] = {}
    py: Dict[object, float] = {}
    for w, p in worlds:
        y = f_y(w)
        u = f_u(w)
        joint[(y, u)] = joint.get((y, u), 0.0) + p
        py[y] = py.get(y, 0.0) + p

    h = 0.0
    for y, p_y in py.items():
        if p_y <= 0.0:
            continue
        masses = [mass / p_y for (yy, _u), mass in joint.items() if yy == y]
        h += p_y * shannon(masses)
    return h


def soft_decay_mass(
    worlds: Sequence[Tuple[object, float]],
    f: Callable[[object], object],
    input_coords: Sequence[Callable[[object], int]],
) -> float:
    """
    Mean soft lost-recoverability over declared gate inputs.

    Preimage size measured in projected gate-input space (Phase-1 style).
    For each y, each input coordinate: d = 0 if fixed on preimage, else
    1 - 1/|preimage_proj(y)|. Ensemble-average mean over coordinates under p.
    """
    pre: Dict[object, List[Tuple[object, float]]] = {}
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


# ---------------------------------------------------------------------------
# Maps on World2
# ---------------------------------------------------------------------------


def proj_x(w: World2) -> World2:
    return w


def y_wire(w: World2) -> int:
    """Circuit intermediate: Y = X1 (publish one wire)."""
    return w[0]


def z_and(w: World2) -> int:
    """AND: Z = X1 ∧ X2."""
    return w[0] & w[1]


def z_not_and(w: World2) -> int:
    """Pure cascade final: Z = NOT(X1 ∧ X2)."""
    return 1 - (w[0] & w[1])


# ---------------------------------------------------------------------------
# Results containers
# ---------------------------------------------------------------------------


@dataclass
class StageRow:
    path: str
    stage: str
    description: str
    H_c: float
    L_E: float
    L_S: float
    L_B: float
    L_disc: float
    export: float
    notes: str


@dataclass
class PathSummary:
    name: str
    H_final: float
    cum_L_E: float
    cum_L_S: float
    cum_L_B_stages: float  # sum of stage L_B (not a claimed additive law)
    cum_L_disc: float
    total_export_to_final: float  # H(X | final) for that path
    n_stages: int


def run_composition_ledger() -> Tuple[
    List[StageRow], Dict[str, PathSummary], Dict[str, float]
]:
    worlds = fair_worlds2()
    rows: List[StageRow] = []
    diagnostics: Dict[str, float] = {}

    H_X = shannon(pushforward(worlds, proj_x).values())  # 2
    assert abs(H_X - 2.0) < 1e-12
    h_and = binary_entropy(0.25)  # ≈ 0.811278

    # ===================================================================
    # Path Direct (D): Z = X1 ∧ X2  (one stage)
    # ===================================================================
    H_Z_D = shannon(pushforward(worlds, z_and).values())
    export_D = conditional_entropy(worlds, z_and, proj_x)  # H(X|Z)
    chain_D = abs(H_X - (H_Z_D + export_D))
    L_E_D = 1.0
    L_S_D = export_D
    L_B_D = soft_decay_mass(worlds, z_and, [lambda w: w[0], lambda w: w[1]])
    L_disc_D = L_E_D + L_S_D + L_B_D

    rows.append(
        StageRow(
            path="D",
            stage="1",
            description="Z = X1 AND X2 [direct]",
            H_c=H_Z_D,
            L_E=L_E_D,
            L_S=L_S_D,
            L_B=L_B_D,
            L_disc=L_disc_D,
            export=export_D,
            notes=f"chain |H(X)-H(Z)-H(X|Z)|={chain_D:.2e}; single-shot",
        )
    )
    path_D = PathSummary(
        name="Direct AND",
        H_final=H_Z_D,
        cum_L_E=L_E_D,
        cum_L_S=L_S_D,
        cum_L_B_stages=L_B_D,
        cum_L_disc=L_disc_D,
        total_export_to_final=export_D,
        n_stages=1,
    )

    # ===================================================================
    # Path Circuit (C): Y = X1 then Z = Y ∧ X2  (persistent wire X2)
    # Path-dependent Σ L_S; final law = AND. Not a pure g(Y) cascade.
    # ===================================================================
    H_Y_C = shannon(pushforward(worlds, y_wire).values())  # 1
    export_XY = conditional_entropy(worlds, y_wire, proj_x)  # H(X|Y) = 1
    chain_XY = abs(H_X - (H_Y_C + export_XY))
    L_B_C1 = soft_decay_mass(
        worlds, y_wire, [lambda w: w[0], lambda w: w[1]]
    )
    L_E_C1 = 1.0
    L_S_C1 = export_XY
    L_disc_C1 = L_E_C1 + L_S_C1 + L_B_C1

    rows.append(
        StageRow(
            path="C",
            stage="1",
            description="Y = X1 [circuit wire publish]",
            H_c=H_Y_C,
            L_E=L_E_C1,
            L_S=L_S_C1,
            L_B=L_B_C1,
            L_disc=L_disc_C1,
            export=export_XY,
            notes=f"chain |H(X)-H(Y)-H(X|Y)|={chain_XY:.2e}",
        )
    )

    H_Z_C = shannon(pushforward(worlds, z_and).values())  # same law as D
    # Stage-2 gate inputs (Y, X2) = (X1, X2); export H(Y,X2|Z) = H(X|Z)
    export_gate2 = conditional_entropy(worlds, z_and, proj_x)
    L_E_C2 = 1.0
    L_S_C2 = export_gate2
    L_B_C2 = soft_decay_mass(
        worlds, z_and, [lambda w: w[0], lambda w: w[1]]
    )
    L_disc_C2 = L_E_C2 + L_S_C2 + L_B_C2
    chain_gate2 = abs(H_X - (H_Z_C + export_gate2))

    rows.append(
        StageRow(
            path="C",
            stage="2",
            description="Z = Y AND X2 [circuit final AND]",
            H_c=H_Z_C,
            L_E=L_E_C2,
            L_S=L_S_C2,
            L_B=L_B_C2,
            L_disc=L_disc_C2,
            export=export_gate2,
            notes=(
                f"gate export H(Y,X2|Z)=H(X|Z); chain err={chain_gate2:.2e}; "
                f"X2 still on wire (not pure g(Y))"
            ),
        )
    )

    path_C = PathSummary(
        name="Circuit Y=X1 then AND",
        H_final=H_Z_C,
        cum_L_E=L_E_C1 + L_E_C2,
        cum_L_S=L_S_C1 + L_S_C2,
        cum_L_B_stages=L_B_C1 + L_B_C2,
        cum_L_disc=L_disc_C1 + L_disc_C2,
        total_export_to_final=export_gate2,
        n_stages=2,
    )

    # ===================================================================
    # Path Markov (M): pure cascade Y = AND(X), Z = NOT(Y)
    # Lemma B: H(X|Z) = H(X|Y) + H(Y|Z)
    # ===================================================================
    H_Y_M = shannon(pushforward(worlds, z_and).values())  # AND intermediate
    export_XY_M = conditional_entropy(worlds, z_and, proj_x)  # H(X|Y)
    chain_YM = abs(H_X - (H_Y_M + export_XY_M))
    L_E_M1 = 1.0
    L_S_M1 = export_XY_M
    L_B_M1 = soft_decay_mass(worlds, z_and, [lambda w: w[0], lambda w: w[1]])
    L_disc_M1 = L_E_M1 + L_S_M1 + L_B_M1

    rows.append(
        StageRow(
            path="M",
            stage="1",
            description="Y = X1 AND X2 [Markov intermediate]",
            H_c=H_Y_M,
            L_E=L_E_M1,
            L_S=L_S_M1,
            L_B=L_B_M1,
            L_disc=L_disc_M1,
            export=export_XY_M,
            notes=f"chain |H(X)-H(Y)-H(X|Y)|={chain_YM:.2e}",
        )
    )

    H_Z_M = shannon(pushforward(worlds, z_not_and).values())
    export_YZ_M = conditional_entropy(worlds, z_not_and, z_and)  # H(Y|Z)
    export_XZ_M = conditional_entropy(worlds, z_not_and, proj_x)  # H(X|Z)
    # Pure cascade: Z = NOT(Y) is bijective on {0,1} ⇒ H(Y|Z)=0, H(Z)=H(Y)
    L_E_M2 = 1.0
    L_S_M2 = export_YZ_M  # stage export of intermediate given final (0 for bijection)
    # Soft decay of Y as single declared input to NOT
    L_B_M2 = soft_decay_mass(worlds, z_not_and, [lambda w: w[0] & w[1]])
    L_disc_M2 = L_E_M2 + L_S_M2 + L_B_M2
    markov_sum = export_XY_M + export_YZ_M
    markov_err = abs(markov_sum - export_XZ_M)
    dpi_gap_M = H_Y_M - H_Z_M  # ≥ 0; =0 for NOT bijection

    rows.append(
        StageRow(
            path="M",
            stage="2",
            description="Z = NOT(Y) [pure cascade g(Y)]",
            H_c=H_Z_M,
            L_E=L_E_M2,
            L_S=L_S_M2,
            L_B=L_B_M2,
            L_disc=L_disc_M2,
            export=export_YZ_M,
            notes=(
                f"H(Y|Z)={export_YZ_M:.5f}; Markov H(X|Z)=H(X|Y)+H(Y|Z) "
                f"err={markov_err:.2e}; DPI H(Y)-H(Z)={dpi_gap_M:.2e}"
            ),
        )
    )

    path_M = PathSummary(
        name="Markov AND then NOT",
        H_final=H_Z_M,
        cum_L_E=L_E_M1 + L_E_M2,
        cum_L_S=L_S_M1 + L_S_M2,
        cum_L_B_stages=L_B_M1 + L_B_M2,
        cum_L_disc=L_disc_M1 + L_disc_M2,
        total_export_to_final=export_XZ_M,
        n_stages=2,
    )

    # ===================================================================
    # L_B non-additivity: product of two independent ANDs on 4 bits
    # ===================================================================
    worlds4 = fair_worlds4()

    def and_a(w: World4) -> int:
        return w[0] & w[1]

    def and_b(w: World4) -> int:
        return w[2] & w[3]

    def and_ab(w: World4) -> Tuple[int, int]:
        return (w[0] & w[1], w[2] & w[3])

    L_B_A = soft_decay_mass(
        worlds4, and_a, [lambda w: w[0], lambda w: w[1]]
    )
    L_B_B = soft_decay_mass(
        worlds4, and_b, [lambda w: w[2], lambda w: w[3]]
    )
    L_B_G = soft_decay_mass(
        worlds4,
        and_ab,
        [lambda w: w[0], lambda w: w[1], lambda w: w[2], lambda w: w[3]],
    )
    lb_sum = L_B_A + L_B_B
    lb_nonadd_gap = abs(lb_sum - L_B_G)
    lb_path_vs_direct = abs(path_C.cum_L_B_stages - path_D.cum_L_B_stages)

    # ===================================================================
    # Asserts
    # ===================================================================
    assert chain_D < 1e-12 and chain_XY < 1e-12 and chain_YM < 1e-12
    assert chain_gate2 < 1e-12
    # Lemma B: pure Markov cascade
    assert markov_err < 1e-12, "Markov export additivity H(X|Z)=H(X|Y)+H(Y|Z)"
    assert export_YZ_M < 1e-12, "NOT is bijective ⇒ H(Y|Z)=0"
    assert abs(export_XZ_M - export_XY_M) < 1e-12
    # DPI
    assert H_Z_M <= H_Y_M + 1e-15
    assert dpi_gap_M < 1e-12
    # Same final AND law for D and C
    assert abs(path_D.H_final - path_C.H_final) < 1e-12
    assert abs(path_D.H_final - h_and) < 1e-12
    # Path dependence: cumulative stage L_S differs
    assert path_C.cum_L_S > path_D.cum_L_S + 0.5, (
        f"expected circuit cum L_S > direct: {path_C.cum_L_S} vs {path_D.cum_L_S}"
    )
    # Total residual export H(X|Z) for same final AND map is path-independent
    assert abs(path_D.total_export_to_final - path_C.total_export_to_final) < 1e-12
    # L_E sums
    assert abs(path_C.cum_L_E - 2.0) < 1e-12
    assert abs(path_D.cum_L_E - 1.0) < 1e-12
    assert abs(path_M.cum_L_E - 2.0) < 1e-12
    # Phase-1 soft L_B for AND
    assert abs(L_B_D - 0.5) < 1e-12
    assert abs(L_B_A - 0.5) < 1e-12 and abs(L_B_B - 0.5) < 1e-12
    # L_B non-additivity (regional sum ≠ global soft mass)
    assert abs(L_B_A - 0.5) < 1e-12 and abs(L_B_B - 0.5) < 1e-12
    assert abs(lb_sum - 1.0) < 1e-12
    assert lb_nonadd_gap > 0.3, (
        f"expected L_B_A+L_B_B ≠ L_B_G; gap={lb_nonadd_gap}"
    )
    # Global four-input soft mass need not equal 0.5 (depends on joint preimages)
    # Circuit stage L_B sum ≠ direct single-stage L_B
    assert lb_path_vs_direct > 0.1
    # Locked reading: high stage export ⇒ high stage L_S
    assert L_S_D >= export_D - 1e-15
    assert L_S_C1 >= export_XY - 1e-15
    # Expected closed forms
    assert abs(export_D - (2.0 - h_and)) < 1e-12
    assert abs(export_XY - 1.0) < 1e-12
    assert abs(path_C.cum_L_S - (1.0 + export_D)) < 1e-12

    diagnostics.update(
        {
            "H_X": H_X,
            "H_Z_D": H_Z_D,
            "H_Y_C": H_Y_C,
            "H_Y_M": H_Y_M,
            "H_Z_M": H_Z_M,
            "export_D": export_D,
            "export_XY_C": export_XY,
            "export_XY_M": export_XY_M,
            "export_YZ_M": export_YZ_M,
            "export_XZ_M": export_XZ_M,
            "markov_sum": markov_sum,
            "markov_err": markov_err,
            "cum_L_S_D": path_D.cum_L_S,
            "cum_L_S_C": path_C.cum_L_S,
            "cum_L_E_D": path_D.cum_L_E,
            "cum_L_E_C": path_C.cum_L_E,
            "cum_L_E_M": path_M.cum_L_E,
            "L_B_D": L_B_D,
            "L_B_C1": L_B_C1,
            "L_B_C2": L_B_C2,
            "cum_L_B_C": path_C.cum_L_B_stages,
            "L_B_A": L_B_A,
            "L_B_B": L_B_B,
            "L_B_G": L_B_G,
            "lb_sum": lb_sum,
            "lb_nonadd_gap": lb_nonadd_gap,
            "dpi_gap_M": dpi_gap_M,
            "path_L_S_gap": path_C.cum_L_S - path_D.cum_L_S,
        }
    )

    paths = {"D": path_D, "C": path_C, "M": path_M}
    return rows, paths, diagnostics


def format_stage_table(rows: Sequence[StageRow]) -> str:
    header = (
        f"{'path':>4}  {'st':>4}  {'H_c':>8}  {'L_E':>5}  {'L_S':>8}  "
        f"{'L_B':>8}  {'L_disc':>8}  {'export':>8}  description"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.path:>4}  {r.stage:>4}  {r.H_c:8.5f}  {r.L_E:5.2f}  "
            f"{r.L_S:8.5f}  {r.L_B:8.5f}  {r.L_disc:8.5f}  {r.export:8.5f}  "
            f"{r.description}"
        )
    return "\n".join(lines)


def format_path_summary(paths: Dict[str, PathSummary]) -> str:
    header = (
        f"{'path':<28}  {'H_final':>8}  {'ΣL_E':>6}  {'ΣL_S':>8}  "
        f"{'ΣL_B*':>8}  {'ΣL_disc':>8}  {'H(X|fin)':>8}  stages"
    )
    lines = [header, "-" * len(header)]
    for key in ("D", "C", "M"):
        p = paths[key]
        lines.append(
            f"{p.name:<28}  {p.H_final:8.5f}  {p.cum_L_E:6.2f}  "
            f"{p.cum_L_S:8.5f}  {p.cum_L_B_stages:8.5f}  {p.cum_L_disc:8.5f}  "
            f"{p.total_export_to_final:8.5f}  {p.n_stages}"
        )
    lines.append(
        "  (* ΣL_B is sum of stage proxies — not claimed additive; see L_B section)"
    )
    return "\n".join(lines)


def main() -> None:
    rows, paths, d = run_composition_ledger()

    print("=" * 96)
    print("M11d — composition laws ledger (H_c^disc, L^disc on finite classical maps)")
    print("Design: synthesis/m11d-composition-laws.md")
    print("=" * 96)
    print()
    print("Stage ledger:")
    print(format_stage_table(rows))
    print()
    print("Path summaries:")
    print(format_path_summary(paths))
    print()
    print("Lemma B — Markov export additivity (pure cascade Y=AND, Z=NOT(Y)):")
    print(f"  H(X|Y)           = {d['export_XY_M']:.6f}")
    print(f"  H(Y|Z)           = {d['export_YZ_M']:.6f}  (bijection ⇒ 0)")
    print(f"  H(X|Y)+H(Y|Z)    = {d['markov_sum']:.6f}")
    print(f"  H(X|Z)           = {d['export_XZ_M']:.6f}")
    print(f"  |error|          = {d['markov_err']:.2e}  (expect 0)")
    print(f"  DPI: H(Y)-H(Z)   = {d['dpi_gap_M']:.2e}  (expect 0 for NOT)")
    print()
    print("Path dependence (key numeric) — same final AND law, different pipelines:")
    print(f"  H_final Direct = Circuit = {d['H_Z_D']:.6f}  (h2(1/4))")
    print(f"  H(X|Z)         = {d['export_D']:.6f}  (path-independent for same final map)")
    print(f"  Σ L_S Direct   = {d['cum_L_S_D']:.6f}")
    print(f"  Σ L_S Circuit  = {d['cum_L_S_C']:.6f}")
    print(f"  gap ΣL_S(C−D)  = {d['path_L_S_gap']:.6f}  "
          f"(circuit pays wire publish H(X|Y)=1 + AND export)")
    print(f"  Σ L_E Direct   = {d['cum_L_E_D']:.1f}   Circuit = {d['cum_L_E_C']:.1f}   "
          f"Markov = {d['cum_L_E_M']:.1f}")
    print()
    print("L_B non-additivity (two independent ANDs on 4 fair bits):")
    print(f"  L_B(A) + L_B(B)  = {d['L_B_A']:.5f} + {d['L_B_B']:.5f} = {d['lb_sum']:.5f}")
    print(f"  L_B(global mean) = {d['L_B_G']:.5f}  (mean soft mass over 4 coords)")
    print(f"  |sum − global|   = {d['lb_nonadd_gap']:.5f}  (≠ 0 ⇒ not additive)")
    print(f"  Circuit Σ stage L_B = {d['cum_L_B_C']:.5f}  vs Direct L_B = {d['L_B_D']:.5f}")
    print()
    print("Lemmas: A chain rule; B Markov export additivity; C DPI; D L_E sum;")
    print("  E path-dep ΣL_S (circuit); F L_B non-additivity.")
    print()
    print("NON-CLAIMS: not continuum L, not L≡G, not gravity, not dual-toy H_c;")
    print("            composition laws are finite classical only (Tag E / L^disc).")
    print("=" * 96)


if __name__ == "__main__":
    main()
