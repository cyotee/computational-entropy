#!/usr/bin/env python3
"""
O1 fast-fail witness — is the discrete export ledger EXTENSIVE?

Question (reformulation stance, synthesis/OPEN_AVENUES.md O1):
  The continuum load's entropy-production term γ|dS_c/dτ| would be a *local
  density*. Paper A's per-step export L_S = H(X|Y) is a finite classical
  quantity that is PATH-DEPENDENT (Thm 3) and whose L_B slot is NON-ADDITIVE
  (Thm F). So a continuum density is NOT obviously well-defined.

  This script tests the one thing that must hold before any continuum limit is
  worth proving: for a lattice of COUPLED local maps, does the total export
  become extensive —
        E(k) = a·k + b + o(1),   a = bulk density (bits/site),  b = boundary
  so that ε(k) = E(k)/k → a — and does the path-dependence surplus vanish per
  site? If yes, O1 has merit (a density exists) and IDEM maps are worth
  wiring in next. If ε(k) drifts with no stable slope, the naive local density
  fails and the continuum load hides a computational gauge (reframe, no theorem).

Model (AND archetype; fair input bits, uniform):
  export of a block = H(X | Y_published) = H(X) − H(Y_published)
  (Y is a deterministic function of X, so H(X,Y)=H(X)=#input bits.)

  Note on the two export notions (both are the same path-dependence):
    * BLOCK export H(X|Y_pub) used here DECREASES as more wires are published
      (revealing more of X leaves less hidden).
    * Paper A's CUMULATIVE ΣL_S (sum of per-step conditional exports) INCREASES
      for the circuit. Same phenomenon, opposite sign convention. What matters
      for a continuum density is that the publication-gauge difference is
      SUBLEADING: it saturates to an O(1) boundary term, so per-site → 0.

  Couplings:
    independent  — k disjoint ANDs (2 fresh bits each). Additive baseline /
                   unit test: ε(k) ≡ h... = 1.188722 exactly.
    shared_input — 1D lattice: bits b_0..b_k; site i outputs b_i ∧ b_{i+1}
                   (nearest-neighbour shared randomness). Translation-invariant
                   bulk ⇒ the interesting extensivity test.
    chained      — b_0,b_1,..,b_k; y_0=b_0∧b_1, y_i=y_{i-1}∧b_{i+1}. Output
                   statistics drift (bias → 0): a non-stationary stress test.
                   'all' publishes every wire (circuit); 'final' publishes only
                   y_{k-1} (direct) — their difference is the path-dependence
                   surplus.

NON-CLAIMS (do not assert from this script):
  - continuum L(ρ,g), L ≡ G, dS_c/dτ identity, gravity of any kind
  - that a proven extensivity witness is a continuum-limit theorem (it is not)
  - anything about IDEM maps yet (this is the AND fast-fail only)

Run:
  .venv/bin/python simulations/classical/m11_lattice_export_density.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Callable, Dict, List, Sequence, Tuple

H2_QUARTER = -(0.25 * math.log2(0.25) + 0.75 * math.log2(0.75))  # h2(1/4) = 0.811278
AND_EXPORT = 2.0 - H2_QUARTER  # single fair AND export = 1.188722 bits


def shannon(counts: Sequence[int], total: int) -> float:
    """Shannon entropy (bits) of a distribution given integer counts and total."""
    h = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            h -= p * math.log2(p)
    return h


# --- coupling output maps: given the input bit list, return the output tuple ---


def out_independent(bits: Sequence[int], k: int) -> Tuple[int, ...]:
    return tuple(bits[2 * i] & bits[2 * i + 1] for i in range(k))


def out_shared_input(bits: Sequence[int], k: int) -> Tuple[int, ...]:
    return tuple(bits[i] & bits[i + 1] for i in range(k))


def out_chained(bits: Sequence[int], k: int) -> Tuple[int, ...]:
    ys: List[int] = []
    prev = bits[0] & bits[1]
    ys.append(prev)
    for i in range(1, k):
        prev = prev & bits[i + 1]
        ys.append(prev)
    return tuple(ys)


# (name, output fn, #input bits as a function of k)
COUPLINGS: Dict[str, Tuple[Callable[[Sequence[int], int], Tuple[int, ...]], Callable[[int], int]]] = {
    "independent": (out_independent, lambda k: 2 * k),
    "shared_input": (out_shared_input, lambda k: k + 1),
    "chained": (out_chained, lambda k: k + 1),
}


def block_export(coupling: str, k: int, publish: str = "all") -> float:
    """Exact export E(k) = H(X) − H(Y_published) by full enumeration.

    publish='all'   → every gate output is published (circuit transcript)
    publish='final' → only the last gate output (chained 'direct' realization)
    """
    out_fn, nbits_fn = COUPLINGS[coupling]
    n = nbits_fn(k)
    if n > 24:
        raise ValueError(f"{coupling} k={k} needs 2^{n} states — too large for exact enum")
    counts: Dict[Tuple[int, ...], int] = {}
    for val in range(1 << n):
        bits = [(val >> j) & 1 for j in range(n)]
        y = out_fn(bits, k)
        if publish == "final":
            y = (y[-1],)
        counts[y] = counts.get(y, 0) + 1
    total = 1 << n
    h_y = shannon(list(counts.values()), total)
    h_x = float(n)  # uniform over n fair bits
    return h_x - h_y


def linfit(xs: Sequence[float], ys: Sequence[float]) -> Tuple[float, float, float]:
    """Ordinary least squares y = a·x + b. Returns (a, b, max_abs_residual)."""
    n = len(xs)
    sx = sum(xs)
    sy = sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    denom = n * sxx - sx * sx
    a = (n * sxy - sx * sy) / denom
    b = (sy - a * sx) / n
    max_resid = max(abs(y - (a * x + b)) for x, y in zip(xs, ys))
    return a, b, max_resid


@dataclass
class Row:
    k: int
    E: float
    eps: float  # per-site E/k
    fit_a_k: float  # a·k+b prediction
    resid: float


def extensivity_table(coupling: str, K: int, publish: str = "all") -> Tuple[List[Row], float, float, float]:
    ks = list(range(1, K + 1))
    Es = [block_export(coupling, k, publish) for k in ks]
    # fit on the upper half to skip any transient
    lo = max(1, K // 2)
    fit_ks = [k for k in ks if k >= lo]
    fit_Es = [E for k, E in zip(ks, Es) if k >= lo]
    a, b, max_resid = linfit(fit_ks, fit_Es)
    rows = [Row(k, E, E / k, a * k + b, E - (a * k + b)) for k, E in zip(ks, Es)]
    return rows, a, b, max_resid


def fmt_table(rows: Sequence[Row]) -> str:
    header = f"{'k':>3}  {'E(k)':>10}  {'eps=E/k':>10}  {'a*k+b':>10}  {'residual':>10}"
    lines = [header, "-" * len(header)]
    for r in rows:
        lines.append(
            f"{r.k:3d}  {r.E:10.5f}  {r.eps:10.5f}  {r.fit_a_k:10.5f}  {r.resid:+10.2e}"
        )
    return "\n".join(lines)


def main() -> None:
    print("=" * 74)
    print("O1 fast-fail — extensivity of discrete export (AND archetype)")
    print("Design: synthesis/OPEN_AVENUES.md O1 · Paper A Thm 3 (path-dep), Thm F")
    print("=" * 74)

    # --- unit-test anchors (Paper A) ---
    for c in ("independent", "shared_input", "chained"):
        e1 = block_export(c, 1)
        assert abs(e1 - AND_EXPORT) < 1e-12, f"{c} k=1 export must equal single AND {AND_EXPORT}"
    # independent must be exactly additive
    assert abs(block_export("independent", 5) - 5 * AND_EXPORT) < 1e-12, "independent not additive"
    print(f"\nAnchors OK: single-AND export = {AND_EXPORT:.6f} bits (all couplings, k=1);"
          f" independent additive.")

    # --- extensivity per coupling ---
    verdicts: Dict[str, str] = {}
    for coupling, K in (("independent", 8), ("shared_input", 14), ("chained", 14)):
        rows, a, b, max_resid = extensivity_table(coupling, K)
        eps_last = rows[-1].eps
        # Extensivity = the block export is LINEAR in k: E(k)=a*k+b with tiny
        # residual. ε(k)=E(k)/k then approaches a only as fast as the boundary
        # b/k, so ε(K)-a ≈ b/K is EXPECTED, not a failure.
        rel_resid = max_resid / abs(rows[-1].E)
        extensive = rel_resid < 1e-3
        verdicts[coupling] = "EXTENSIVE" if extensive else "NOT clearly extensive"
        print(f"\n--- {coupling} (publish=all) ---")
        print(fmt_table(rows))
        print(f"  linear fit (upper half): E(k) ≈ {a:.5f}·k {'+' if b >= 0 else '-'} {abs(b):.5f}")
        print(f"  bulk density a = {a:.5f} bits/site | boundary b = {b:+.5f} | "
              f"max residual = {max_resid:.2e} (rel {rel_resid:.1e})")
        print(f"  ε(K)={eps_last:.5f}; residual gap ε(K)-a={eps_last - a:+.5f} ≈ b/K={b / K:+.5f}"
              f"  ⇒  {verdicts[coupling]}")

    # --- path-dependence: does the publication gauge move the BULK density? ---
    # Block export decreases when more wires are published, so |surplus| grows
    # with k but must SATURATE to an O(1) boundary term ⇒ surplus/k → 0.
    print("\n--- path-dependence (chained): |publish=all − publish=final| ---")
    print(f"{'k':>3}  {'E_circuit':>10}  {'E_direct':>10}  {'|surplus|':>9}  {'|surplus|/k':>11}")
    print("-" * 52)
    abs_surplus: List[float] = []
    per_site: List[float] = []
    K_PD = 18
    for k in range(1, K_PD + 1):
        e_all = block_export("chained", k, "all")
        e_fin = block_export("chained", k, "final")
        s = abs(e_all - e_fin)
        abs_surplus.append(s)
        per_site.append(s / k)
        print(f"{k:3d}  {e_all:10.5f}  {e_fin:10.5f}  {s:9.5f}  {s / k:11.5f}")
    # saturation: successive change in the surplus shrinks toward zero
    tail_step = abs(abs_surplus[-1] - abs_surplus[-2])
    pd_vanishes = per_site[-1] < per_site[1] and per_site[-1] < 0.1
    assert tail_step < 0.05, "surplus should saturate (boundary term), not grow linearly"
    print(f"  surplus saturates → {abs_surplus[-1]:.4f} bits (Δ last step {tail_step:.4f});"
          f" per-site → {per_site[-1]:.4f}")

    # --- verdict ---
    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    for c, v in verdicts.items():
        print(f"  {c:13s}: {v}")
    print(f"  path-dependence per-site: {per_site[1]:.4f} (k=2) → "
          f"{per_site[-1]:.4f} (k={K_PD})  ⇒  "
          f"{'vanishes (subleading boundary)' if pd_vanishes else 'persists'}")
    merit = verdicts["shared_input"] == "EXTENSIVE" and verdicts["chained"] == "EXTENSIVE"
    print()
    if merit and pd_vanishes:
        print("  ==> MERIT: coupled export is extensive (a well-defined bulk density")
        print("      exists) and per-site path-dependence vanishes. A continuum")
        print("      export density is plausible; proceed to swap AND -> IDEM maps.")
    else:
        print("  ==> CAUTION: extensivity or path-dependence-vanishing not clean;")
        print("      inspect which coupling failed before investing in a theorem.")
    print("\nNON-CLAIMS: not continuum L, not dS_c/dτ, not gravity; a discrete")
    print("extensivity witness only — not a continuum-limit theorem.")
    print("=" * 74)


if __name__ == "__main__":
    main()
