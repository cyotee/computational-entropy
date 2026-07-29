#!/usr/bin/env python3
"""
M11.3 experiment — constructive coupled-regions load ledger.

Ontology (matches synthesis/m11-idem-to-load.md product-system open Q):
  Two finite classical regions A, B on a product microstate.

  Microstate: fair bits X=(X1,X2), Z=(Z1,Z2) i.i.d. — H(X,Z)=4.
  Channel steps:
    k=0  id prior on (X,Z)  [global] / X [A] / Z [B]
    k=1  independent local ANDs:  Y = X1∧X2,  V = Z1∧Z2
    k=2  product export screen:   S = Y ⊕ V
         declared post-coupling outputs:
           region A: O_A = (Y, S)   (keeps local AND + shared screen)
           region B: O_B = (V, S)
           global:   O_G = (Y, V, S)  (S determined by Y,V)
         plus a screen-only global diagnostic: O_screen = S
           (Y,V “forgotten” into environment — conservation still holds)

  H_c: exact Shannon of the declared regional / global output under the
       uniform pushforward on {0,1}^4.

Load proxies (weights β'=γ'=δ'=1; no continuum constants):
  L_E  — active ops this step (1 gate / 1 XOR)
  L_S  — export flux H(local inputs | declared output) for that evaluation
  L_B  — mean soft lost-recoverability mass on gate inputs
  L_disc = L_E + L_S + L_B

Optional discrete load clock (diagnostic only, not continuum τ):
  per-region cumulative k_eff = sum_j 1/(1 + α' L_disc,j), α' = 0.1.

Demonstrates:
  - Chain rules / conservation on independent ANDs and after coupling
  - Local high export ⇒ high local L_S (locked reading)
  - Coupling redistributes / screens information; no magic destruction
  - Idle baseline rows (k=0) for comparison

Non-claims (do not assert from this script):
  - continuum L(ρ,g) equality, L ≡ G, Einstein/Newton from product gates
  - GfE / dual-toy residual H_c identity
  - gravity recovery of any kind; discrete k_eff is not continuum proper time
  - product regions as spacetime patches or continuum ρ

Run:
  .venv/bin/python simulations/classical/m11_coupled_regions_ledger.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

# Conventional load-clock weight — diagnostic only (not continuum α).
ALPHA_PRIME = 0.1

World = Tuple[int, int, int, int]  # (x1, x2, z1, z2)
Region = str  # "A" | "B" | "G"


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
# Finite ensemble: uniform on {0,1}^4
# ---------------------------------------------------------------------------


def fair_worlds() -> List[Tuple[World, float]]:
    mass = 1.0 / 16.0
    out: List[Tuple[World, float]] = []
    for x1 in (0, 1):
        for x2 in (0, 1):
            for z1 in (0, 1):
                for z2 in (0, 1):
                    out.append(((x1, x2, z1, z2), mass))
    return out


def pushforward(
    worlds: Sequence[Tuple[World, float]], f: Callable[[World], object]
) -> Dict[object, float]:
    dist: Dict[object, float] = {}
    for w, p in worlds:
        y = f(w)
        dist[y] = dist.get(y, 0.0) + p
    return dist


def conditional_entropy(
    worlds: Sequence[Tuple[World, float]],
    f_y: Callable[[World], object],
    f_u: Callable[[World], object],
) -> float:
    """
    H(U|Y) where U = f_u(world), Y = f_y(world).

    Exact: sum_y p(y) H(U | Y=y) over finite support.
    """
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


def mutual_information(
    worlds: Sequence[Tuple[World, float]],
    f_a: Callable[[World], object],
    f_b: Callable[[World], object],
) -> float:
    """I(A;B) = H(A) + H(B) - H(A,B)."""
    ha = shannon(pushforward(worlds, f_a).values())
    hb = shannon(pushforward(worlds, f_b).values())
    hab = shannon(pushforward(worlds, lambda w: (f_a(w), f_b(w))).values())
    return ha + hb - hab


def soft_decay_mass(
    worlds: Sequence[Tuple[World, float]],
    f: Callable[[World], object],
    input_coords: Sequence[Callable[[World], int]],
) -> float:
    """
    Mean soft lost-recoverability over declared gate inputs.

    Preimage size measured in projected gate-input space (Phase-1/2 style).
    For each y, each input coordinate: d = 0 if fixed on preimage, else
    1 - 1/|preimage_proj(y)|. Ensemble-average mean over coordinates under p.
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


# ---------------------------------------------------------------------------
# Observable projections
# ---------------------------------------------------------------------------


def proj_x(w: World) -> Tuple[int, int]:
    return (w[0], w[1])


def proj_z(w: World) -> Tuple[int, int]:
    return (w[2], w[3])


def proj_xz(w: World) -> World:
    return w


def y_and(w: World) -> int:
    return w[0] & w[1]


def v_and(w: World) -> int:
    return w[2] & w[3]


def yv(w: World) -> Tuple[int, int]:
    return (y_and(w), v_and(w))


def s_xor(w: World) -> int:
    return y_and(w) ^ v_and(w)


def o_a2(w: World) -> Tuple[int, int]:
    """Region A post-coupling: (Y, S)."""
    y = y_and(w)
    return (y, y ^ v_and(w))


def o_b2(w: World) -> Tuple[int, int]:
    """Region B post-coupling: (V, S)."""
    v = v_and(w)
    return (v, y_and(w) ^ v)


def o_g2(w: World) -> Tuple[int, int, int]:
    """Global post-coupling: (Y, V, S) with S = Y⊕V."""
    y, v = y_and(w), v_and(w)
    return (y, v, y ^ v)


# ---------------------------------------------------------------------------
# Ledger
# ---------------------------------------------------------------------------


@dataclass
class LedgerRow:
    region: Region
    k: int
    description: str
    H_c: float
    L_E: float
    L_S: float
    L_B: float
    L_disc: float
    export: float
    k_eff_cum: float
    notes: str


def _clock_step(k_eff: float, l_disc: float) -> float:
    return k_eff + 1.0 / (1.0 + ALPHA_PRIME * l_disc)


def run_coupled_regions_ledger() -> Tuple[List[LedgerRow], Dict[str, float]]:
    worlds = fair_worlds()
    rows: List[LedgerRow] = []
    k_eff: Dict[Region, float] = {"A": 0.0, "B": 0.0, "G": 0.0}

    # ---- k=0: idle identity baselines ----
    H_X = shannon(pushforward(worlds, proj_x).values())  # 2
    H_Z = shannon(pushforward(worlds, proj_z).values())  # 2
    H_XZ = shannon(pushforward(worlds, proj_xz).values())  # 4

    for region, hc, desc in (
        ("A", H_X, "id prior on X=(X1,X2) [baseline]"),
        ("B", H_Z, "id prior on Z=(Z1,Z2) [baseline]"),
        ("G", H_XZ, "id prior on (X,Z) [baseline]"),
    ):
        rows.append(
            LedgerRow(
                region=region,
                k=0,
                description=desc,
                H_c=hc,
                L_E=0.0,
                L_S=0.0,
                L_B=0.0,
                L_disc=0.0,
                export=0.0,
                k_eff_cum=0.0,
                notes="idle identity — low L (not stockpile-as-load)",
            )
        )

    # ---- k=1: independent local ANDs ----
    H_Y = shannon(pushforward(worlds, y_and).values())
    H_V = shannon(pushforward(worlds, v_and).values())
    H_YV = shannon(pushforward(worlds, yv).values())

    export_A1 = conditional_entropy(worlds, y_and, proj_x)  # H(X|Y)
    export_B1 = conditional_entropy(worlds, v_and, proj_z)  # H(Z|V)
    export_G1 = conditional_entropy(worlds, yv, proj_xz)  # H(X,Z|Y,V)

    chain_A = abs(H_X - (H_Y + export_A1))
    chain_B = abs(H_Z - (H_V + export_B1))
    chain_G = abs(H_XZ - (H_YV + export_G1))
    # Independence of regions at k=1: H(Y,V)=H(Y)+H(V), exports add
    indep_yv = abs(H_YV - (H_Y + H_V))
    export_add = abs(export_G1 - (export_A1 + export_B1))

    L_B_A1 = soft_decay_mass(worlds, y_and, [lambda w: w[0], lambda w: w[1]])
    L_B_B1 = soft_decay_mass(worlds, v_and, [lambda w: w[2], lambda w: w[3]])
    # Global: mean soft decay over all four input bits under joint map (Y,V)
    L_B_G1 = soft_decay_mass(
        worlds,
        yv,
        [lambda w: w[0], lambda w: w[1], lambda w: w[2], lambda w: w[3]],
    )

    for region, hc, export, lb, gate_desc, chain_err in (
        (
            "A",
            H_Y,
            export_A1,
            L_B_A1,
            "Y = X1 AND X2 [local]",
            chain_A,
        ),
        (
            "B",
            H_V,
            export_B1,
            L_B_B1,
            "V = Z1 AND Z2 [local]",
            chain_B,
        ),
        (
            "G",
            H_YV,
            export_G1,
            L_B_G1,
            "(Y,V) independent ANDs [global]",
            chain_G,
        ),
    ):
        le = 1.0 if region != "G" else 2.0  # two gates globally
        ls = export
        ld = le + ls + lb
        k_eff[region] = _clock_step(k_eff[region], ld)
        note = f"chain err={chain_err:.2e}"
        if region == "G":
            note += (
                f"; |H(Y,V)-H(Y)-H(V)|={indep_yv:.2e}; "
                f"|export_G-(A+B)|={export_add:.2e}"
            )
        rows.append(
            LedgerRow(
                region=region,
                k=1,
                description=gate_desc,
                H_c=hc,
                L_E=le,
                L_S=ls,
                L_B=lb,
                L_disc=ld,
                export=export,
                k_eff_cum=k_eff[region],
                notes=note,
            )
        )

    # ---- k=2: coupling via shared screen S = Y ⊕ V ----
    H_S = shannon(pushforward(worlds, s_xor).values())
    H_OA = shannon(pushforward(worlds, o_a2).values())  # H(Y,S)
    H_OB = shannon(pushforward(worlds, o_b2).values())  # H(V,S)
    H_OG = shannon(pushforward(worlds, o_g2).values())  # H(Y,V,S)=H(Y,V)

    # Local input export given post-coupling observables
    export_A2 = conditional_entropy(worlds, o_a2, proj_x)  # H(X|Y,S)
    export_B2 = conditional_entropy(worlds, o_b2, proj_z)  # H(Z|V,S)
    export_G2 = conditional_entropy(worlds, o_g2, proj_xz)  # H(X,Z|Y,V,S)

    # Screen-only global: forget local (Y,V) into environment
    export_screen = conditional_entropy(worlds, s_xor, proj_xz)  # H(X,Z|S)
    export_yv_given_s = conditional_entropy(worlds, s_xor, yv)  # H(Y,V|S)

    # Coupling bijectivity: (Y,S) ↔ (Y,V) given S=Y⊕V
    bij_as = abs(H_OA - H_YV)
    bij_bs = abs(H_OB - H_YV)
    bij_g = abs(H_OG - H_YV)
    # Local export unchanged by learning the other side via S
    export_A_stable = abs(export_A2 - export_A1)
    export_B_stable = abs(export_B2 - export_B1)
    export_G_stable = abs(export_G2 - export_G1)
    # Screen-only conservation: H(X,Z) = H(S) + H(X,Z|S)
    chain_screen = abs(H_XZ - (H_S + export_screen))
    # Also H(Y,V) = H(S) + H(Y,V|S)
    chain_yv_s = abs(H_YV - (H_S + export_yv_given_s))
    # Global full post-coupling conservation
    chain_g2 = abs(H_XZ - (H_OG + export_G2))

    # Soft decay: A inputs from O_A=(Y,S); B from O_B; G from O_G
    L_B_A2 = soft_decay_mass(worlds, o_a2, [lambda w: w[0], lambda w: w[1]])
    L_B_B2 = soft_decay_mass(worlds, o_b2, [lambda w: w[2], lambda w: w[3]])
    L_B_G2 = soft_decay_mass(
        worlds,
        o_g2,
        [lambda w: w[0], lambda w: w[1], lambda w: w[2], lambda w: w[3]],
    )
    # Screen-only: recoverability of all four bits from S alone
    L_B_screen = soft_decay_mass(
        worlds,
        s_xor,
        [lambda w: w[0], lambda w: w[1], lambda w: w[2], lambda w: w[3]],
    )

    # I(Y;S) etc. diagnostics
    i_y_s = mutual_information(worlds, y_and, s_xor)
    i_v_s = mutual_information(worlds, v_and, s_xor)

    for region, hc, export, lb, desc, extra_note in (
        (
            "A",
            H_OA,
            export_A2,
            L_B_A2,
            "O_A=(Y,S)  S=Y⊕V [coupled]",
            f"|H(Y,S)-H(Y,V)|={bij_as:.2e}; |H(X|Y,S)-H(X|Y)|={export_A_stable:.2e}; "
            f"I(Y;S)={i_y_s:.5f}",
        ),
        (
            "B",
            H_OB,
            export_B2,
            L_B_B2,
            "O_B=(V,S)  S=Y⊕V [coupled]",
            f"|H(V,S)-H(Y,V)|={bij_bs:.2e}; |H(Z|V,S)-H(Z|V)|={export_B_stable:.2e}; "
            f"I(V;S)={i_v_s:.5f}",
        ),
        (
            "G",
            H_OG,
            export_G2,
            L_B_G2,
            "O_G=(Y,V,S) [coupled full]",
            f"|H(Y,V,S)-H(Y,V)|={bij_g:.2e}; chain H(XZ)=H(OG)+export err={chain_g2:.2e}",
        ),
    ):
        le = 1.0  # one XOR interaction
        ls = export  # single-shot export proxy (locked: still high for AND preimages)
        ld = le + ls + lb
        k_eff[region] = _clock_step(k_eff[region], ld)
        rows.append(
            LedgerRow(
                region=region,
                k=2,
                description=desc,
                H_c=hc,
                L_E=le,
                L_S=ls,
                L_B=lb,
                L_disc=ld,
                export=export,
                k_eff_cum=k_eff[region],
                notes=extra_note,
            )
        )

    # Screen-only global diagnostic row (k=2, region G*, not clocked into G)
    le_s = 1.0
    ls_s = export_screen  # high: local AND results + preimages in environment
    lb_s = L_B_screen
    ld_s = le_s + ls_s + lb_s
    rows.append(
        LedgerRow(
            region="G*",
            k=2,
            description="O=S only (forget Y,V → env) [screen]",
            H_c=H_S,
            L_E=le_s,
            L_S=ls_s,
            L_B=lb_s,
            L_disc=ld_s,
            export=export_screen,
            k_eff_cum=float("nan"),
            notes=(
                f"chain |H(XZ)-H(S)-H(XZ|S)|={chain_screen:.2e}; "
                f"|H(YV)-H(S)-H(YV|S)|={chain_yv_s:.2e}; "
                f"H(Y,V|S)={export_yv_given_s:.5f}"
            ),
        )
    )

    # ---- Asserts: conservation + locked reading ----
    assert chain_A < 1e-12 and chain_B < 1e-12 and chain_G < 1e-12
    assert indep_yv < 1e-12, "Y ⊥ V expected under product priors + independent ANDs"
    assert export_add < 1e-12, "global export must equal sum of regional exports at k=1"
    assert bij_as < 1e-12 and bij_bs < 1e-12 and bij_g < 1e-12
    assert export_A_stable < 1e-12 and export_B_stable < 1e-12
    assert export_G_stable < 1e-12
    assert chain_screen < 1e-12 and chain_yv_s < 1e-12 and chain_g2 < 1e-12

    # Locked reading: independent AND ⇒ high regional L_S
    row_A1 = next(r for r in rows if r.region == "A" and r.k == 1)
    row_B1 = next(r for r in rows if r.region == "B" and r.k == 1)
    assert row_A1.L_S > 1.0 and row_B1.L_S > 1.0
    assert row_A1.L_S >= row_A1.export - 1e-15
    assert abs(row_A1.L_S - row_B1.L_S) < 1e-12  # symmetric regions
    # High export pairs with high L_S (not inverse): screen-only export >
    # regional full-view export at k=2, so screen L_S must be larger
    row_A2 = next(r for r in rows if r.region == "A" and r.k == 2)
    row_Gs = next(r for r in rows if r.region == "G*" and r.k == 2)
    assert row_Gs.export > row_A2.export
    assert row_Gs.L_S > row_A2.L_S
    # Phase-1 soft L_B for AND = 0.5
    assert abs(row_A1.L_B - 0.5) < 1e-12
    assert abs(row_B1.L_B - 0.5) < 1e-12

    diagnostics = {
        "H_X": H_X,
        "H_Z": H_Z,
        "H_XZ": H_XZ,
        "H_Y": H_Y,
        "H_V": H_V,
        "H_YV": H_YV,
        "H_S": H_S,
        "H_OA": H_OA,
        "H_OB": H_OB,
        "H_OG": H_OG,
        "export_A1": export_A1,
        "export_B1": export_B1,
        "export_G1": export_G1,
        "export_A2": export_A2,
        "export_screen": export_screen,
        "export_yv_given_s": export_yv_given_s,
        "chain_A": chain_A,
        "chain_G": chain_G,
        "chain_screen": chain_screen,
        "P_S1": pushforward(worlds, s_xor).get(1, 0.0),
        "P_Y1": pushforward(worlds, y_and).get(1, 0.0),
    }
    return rows, diagnostics


def format_table(rows: Sequence[LedgerRow]) -> str:
    header = (
        f"{'reg':>3}  {'k':>2}  {'H_c':>8}  {'L_E':>5}  {'L_S':>8}  {'L_B':>8}  "
        f"{'L_disc':>8}  {'export':>8}  {'k_eff':>8}  description"
    )
    lines = [header, "-" * len(header)]
    for r in rows:
        k_eff_s = f"{r.k_eff_cum:8.5f}" if r.k_eff_cum == r.k_eff_cum else f"{'—':>8}"
        lines.append(
            f"{r.region:>3}  {r.k:2d}  {r.H_c:8.5f}  {r.L_E:5.2f}  {r.L_S:8.5f}  "
            f"{r.L_B:8.5f}  {r.L_disc:8.5f}  {r.export:8.5f}  {k_eff_s}  "
            f"{r.description}"
        )
    return "\n".join(lines)


def main() -> None:
    rows, d = run_coupled_regions_ledger()

    print("=" * 96)
    print("M11.3 — coupled-regions product ledger (export screen S = Y ⊕ V)")
    print("Design: synthesis/m11-idem-to-load.md §11 Q5 (product systems)")
    print("=" * 96)
    print()
    print(format_table(rows))
    print()
    print(f"Load clock α' = {ALPHA_PRIME} (diagnostic only; not continuum τ).")
    for reg in ("A", "B", "G"):
        last = [r for r in rows if r.region == reg][-1]
        print(f"  region {reg}: final k_eff cumulative = {last.k_eff_cum:.6f}")
    print()
    print("Sanity / conservation:")
    print(f"  H(X,Z)           = {d['H_XZ']:.6f}  (expect 4)")
    print(f"  H(Y) = H(V)      = {d['H_Y']:.6f}  (expect h2(1/4) ≈ 0.811278)")
    print(f"  H(Y,V)           = {d['H_YV']:.6f}  (expect 2·H(Y) ≈ 1.622556)")
    print(f"  export_A = H(X|Y)= {d['export_A1']:.6f}  (expect ≈ 1.188722)")
    print(f"  export_G (k=1)   = {d['export_G1']:.6f}  (expect 2·export_A ≈ 2.377443)")
    print(f"  H(S), P(S=1)     = {d['H_S']:.6f}, {d['P_S1']:.4f}  "
          f"(expect h2(3/8)≈0.954434, P=0.375)")
    print(f"  H(Y,S)=H(Y,V)    = {d['H_OA']:.6f}  (coupling bijection)")
    print(f"  H(X,Z|S)         = {d['export_screen']:.6f}  "
          f"(screen-only export; chain err={d['chain_screen']:.2e})")
    print(f"  H(Y,V|S)         = {d['export_yv_given_s']:.6f}  "
          f"(AND results forgotten into env when only S kept)")
    print()
    print("Reading:")
    print("  • Independent ANDs: local high export ⇒ high local L_S (locked).")
    print("  • Coupling (Y,S)/(V,S): each region learns the other AND via S;")
    print("    local input export H(X|Y) unchanged; global full bookkeeping intact.")
    print("  • Screen-only G*: H(S) low, export high — information moved to env,")
    print("    not destroyed (chain H(X,Z)=H(S)+H(X,Z|S)).")
    print()
    print("Locked reading check: high export ⇒ high L_S (PASS);")
    print("  G* screen export > regional A post-coupling export (PASS).")
    print()
    print("NON-CLAIMS: not continuum L, not L≡G, not gravity, not dual-toy H_c;")
    print("            not spacetime regions; k_eff diagnostic only (not τ).")
    print("=" * 96)


if __name__ == "__main__":
    main()
