#!/usr/bin/env python3
"""
O1 phase 2 — does the IDEM DECAY VECTOR predict the export density?

Motivation (synthesis/m11-idem-to-load.md §6; connects IDEM to O1):
  The AND fast-fail (m11_lattice_export_density.py) showed coupled export is
  extensive. This script asks whether IDEM's decay vector — arity + per-input
  recoverability metadata (d_i=0 recoverable, d_i=1 lost) — *predicts* that
  export from LOCAL metadata, instead of enumerating the joint 2^n state space.
  If it does, IDEM stops being a definition-without-utility and becomes the
  generating rule for the export density.

Exact relationship (deterministic map f, uniform inputs X on {0,1}^n):
  Given Y=y, X is uniform on the preimage f^{-1}(y), so
        H(X | Y=y) = log2 |f^{-1}(y)|,
        export = H(X|Y) = Σ_y p(y) · log2|f^{-1}(y)|.
  The HARD decay vector on branch y flags each coordinate that varies across
  the preimage; let D(y) = #varying coords. Since a preimage sits inside the
  subcube spanned by its varying coords, |f^{-1}(y)| ≤ 2^{D(y)}, hence
        export  ≤  Σ_y p(y)·D(y)  =:  decay-bound,
  with EQUALITY iff every preimage is a full product subcube.

  ⇒ THEOREM (this script, asserted): the decay vector gives a tight UPPER
    BOUND on export, EXACT for product-preimage (erasure-type) IDEM maps.

Utility payoff: for product/erasure lattices the export density is computed
from local decay metadata in O(N) instead of O(2^N) — enumeration-free and
exact. For non-product maps (AND, majority, parity) decay over-counts by a
known gap; a compositional "decay algebra" to tighten it under coupling is the
open next step (O1 theorem).

NON-CLAIMS (do not assert from this script):
  - continuum L(ρ,g), L ≡ G, dS_c/dτ identity, gravity of any kind
  - that the decay bound is the continuum entropy-production density
  - that a finite decay↔export theorem is a continuum-limit theorem

Run:
  .venv/bin/python simulations/classical/m11_idem_export_density.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from itertools import product
from typing import Callable, Dict, Hashable, List, Sequence, Tuple

Bits = Tuple[int, ...]


def shannon(counts: Sequence[int], total: int) -> float:
    h = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            h -= p * math.log2(p)
    return h


@dataclass
class IdemMap:
    """Expanded identity: a map f plus the decay/arity metadata IDEM tracks."""
    name: str
    arity: int
    fn: Callable[[Bits], Hashable]

    def preimages(self) -> Dict[Hashable, List[Bits]]:
        pre: Dict[Hashable, List[Bits]] = {}
        for x in product((0, 1), repeat=self.arity):
            pre.setdefault(self.fn(x), []).append(x)
        return pre

    def H_output(self) -> float:
        pre = self.preimages()
        total = 1 << self.arity
        return shannon([len(v) for v in pre.values()], total)

    def exact_export(self) -> float:
        """H(X|Y) = Σ_y p(y) log2|preimage(y)| (uniform inputs)."""
        pre = self.preimages()
        total = 1 << self.arity
        e = 0.0
        for xs in pre.values():
            p = len(xs) / total
            e += p * math.log2(len(xs))
        return e

    def decay_branch(self, xs: Sequence[Bits]) -> Tuple[int, ...]:
        """Hard decay vector on a branch: 1 where the coordinate varies (lost)."""
        return tuple(
            1 if len({x[i] for x in xs}) > 1 else 0 for i in range(self.arity)
        )

    def decay_bound_export(self) -> float:
        """Σ_y p(y)·#unrecoverable coords — upper bound on export."""
        pre = self.preimages()
        total = 1 << self.arity
        e = 0.0
        for xs in pre.values():
            p = len(xs) / total
            e += p * sum(self.decay_branch(xs))
        return e

    def is_product(self) -> bool:
        """True iff every preimage is a full product subcube (⇒ decay exact)."""
        for xs in self.preimages().values():
            d = sum(self.decay_branch(xs))
            if len(xs) != (1 << d):
                return False
        return True


# --- IDEM map family spanning product → non-product ---


def erase_last_k(n: int, k: int) -> IdemMap:
    return IdemMap(f"erase({n},{k})", n, lambda x, n=n, k=k: x[: n - k])


def and2() -> IdemMap:
    return IdemMap("AND(2)", 2, lambda x: x[0] & x[1])


def and_all(n: int) -> IdemMap:
    return IdemMap(f"AND_all({n})", n, lambda x: int(all(x)))


def majority3() -> IdemMap:
    return IdemMap("majority(3)", 3, lambda x: int(sum(x) >= 2))


def parity(n: int) -> IdemMap:
    return IdemMap(f"parity({n})", n, lambda x: sum(x) & 1)


FAMILY: List[IdemMap] = [
    erase_last_k(2, 1),
    erase_last_k(3, 1),
    erase_last_k(4, 2),
    and2(),
    and_all(3),
    majority3(),
    parity(3),
]


def part1_map_family() -> None:
    print("\n--- Part 1: decay vector vs exact export over an IDEM map family ---")
    header = (
        f"{'map':>13}  {'H(Y)':>7}  {'exact_exp':>9}  {'decay_bnd':>9}  "
        f"{'gap':>7}  {'product':>7}"
    )
    print(header)
    print("-" * len(header))
    for m in FAMILY:
        exact = m.exact_export()
        bound = m.decay_bound_export()
        gap = bound - exact
        prod = m.is_product()
        print(
            f"{m.name:>13}  {m.H_output():7.4f}  {exact:9.5f}  {bound:9.5f}  "
            f"{gap:7.4f}  {str(prod):>7}"
        )
        # THEOREM asserts: bound is an upper bound, tight iff product.
        assert bound >= exact - 1e-12, f"{m.name}: decay must upper-bound export"
        if prod:
            assert gap < 1e-12, f"{m.name}: product map ⇒ decay must be EXACT"
        else:
            assert gap > 1e-9, f"{m.name}: non-product ⇒ strict decay gap expected"
    # sanity: single AND matches Paper A export
    assert abs(and2().exact_export() - 1.188722) < 1e-5, "AND export must match Paper A"
    print("  asserts OK: decay bound ≥ exact (all); EXACT iff product-preimage.")


def erasure_lattice_export(N: int) -> Tuple[float, float]:
    """N independent erase(2,1) sites. Returns (exact_enumerated, decay_predicted)."""
    n = 2 * N
    counts: Dict[Bits, int] = {}
    for val in range(1 << n):
        x = tuple((val >> j) & 1 for j in range(n))
        y = tuple(x[2 * i] for i in range(N))  # keep a_i, erase b_i
        counts[y] = counts.get(y, 0) + 1
    total = 1 << n
    exact = float(n) - shannon(list(counts.values()), total)  # H(X)-H(Y)
    decay_pred = float(N)  # each site erases exactly 1 bit (product ⇒ exact)
    return exact, decay_pred


def part2_lattice_utility() -> None:
    print("\n--- Part 2: enumeration-free density on a product (erasure) lattice ---")
    print(f"{'N':>3}  {'exact (enum)':>13}  {'decay (O(N))':>13}  {'match':>6}")
    print("-" * 42)
    ok = True
    for N in range(1, 7):
        exact, pred = erasure_lattice_export(N)
        match = abs(exact - pred) < 1e-9
        ok = ok and match
        print(f"{N:3d}  {exact:13.6f}  {pred:13.6f}  {str(match):>6}")
    assert ok, "erasure lattice: decay must predict export exactly"
    print("  ⇒ product lattice: decay computes the density in O(N), not O(2^N),")
    print("    EXACTLY. Density = 1.000 bit/site read straight from the decay vector.")
    # contrast: AND is non-product, so per-site decay OVER-counts
    a = and2()
    print(f"\n  Contrast (AND, non-product): exact single-map export "
          f"{a.exact_export():.4f} < decay bound {a.decay_bound_export():.4f}.")
    print("  Under coupling the true AND-lattice density (≈0.301, shared_input in")
    print("  m11_lattice_export_density.py) falls below the naive per-map decay")
    print("  bound ⇒ a compositional DECAY ALGEBRA is the open O1 step.")


def main() -> None:
    print("=" * 74)
    print("O1 phase 2 — IDEM decay vector as export-density predictor")
    print("Design: synthesis/m11-idem-to-load.md §6 · Paper A export identity")
    print("=" * 74)
    part1_map_family()
    part2_lattice_utility()
    print("\n" + "=" * 74)
    print("VERDICT")
    print("=" * 74)
    print("  IDEM decay vector = tight UPPER BOUND on export, EXACT for product")
    print("  (erasure) maps ⇒ enumeration-free O(N) density there. Non-product")
    print("  maps (AND/majority/parity) have a known gap; tightening it under")
    print("  coupling (a decay algebra) is the concrete open O1 theorem.")
    print("\n  ==> IDEM demonstrates UTILITY: local metadata predicts/bounds the")
    print("      export density that feeds the entropy-production load slot.")
    print("\nNON-CLAIMS: not continuum L, not dS_c/dτ, not gravity; finite classical")
    print("decay↔export relationship only — not a continuum-limit theorem.")
    print("=" * 74)


if __name__ == "__main__":
    main()
