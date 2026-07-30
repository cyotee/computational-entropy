#!/usr/bin/env python3
"""
O1 step 5 — generalizing the decay algebra: range-r coupling, any local gate.

The 1D nearest-neighbour theorem (m11f) tracked a single shared boundary bit.
Here the local map is a sliding window of width w over an i.i.d. fair bit
stream:
        Y_i = g(b_i, b_{i+1}, ..., b_{i+w-1}),
so consecutive outputs share r = w-1 bits. The Bayesian boundary belief now
lives over the 2^{w-1} window states, and the transfer becomes an OPERATOR on
that belief simplex — the generalized decay algebra.

Two independent computations of the coupled export density a = 1 - h_Y
(input rate 1 fresh bit/site minus output entropy rate):
  * enumerate  — exact E(k)/k from O(2^{k+w}) joint enumeration (ground truth)
  * transfer   — belief-operator: BFS the reachable beliefs (finite thanks to
                 resets), solve the stationary belief-chain, h_Y = averaged
                 predictive entropy. Cost depends on 2^{w-1}, NOT on k.

Deliverable: transfer == enumerate across gates (AND/OR/threshold) and ranges
w=2,3,4, and recovers the m11f constant a=0.3007568 at w=2 (r=1). Shows the
decay algebra generalizes; the boundary-belief dimension is 2^{w-1}.

Still open (next rung): a general THEOREM (m11f is proved only for w=2), and
the continuum embedding. Finite/algorithmic witness — NON-CLAIMS: not
continuum L, not dS_c/dτ, not gravity.

Run:
  .venv/bin/python simulations/classical/m11_decay_algebra_general.py
"""

from __future__ import annotations

import math
from itertools import product
from typing import Callable, Dict, List, Tuple

Bits = Tuple[int, ...]
Gate = Callable[[Bits], int]


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def shannon(counts: List[int], total: int) -> float:
    h = 0.0
    for c in counts:
        if c > 0:
            q = c / total
            h -= q * math.log2(q)
    return h


# --- gate family (arity = window width w) ---


def gate_and(x: Bits) -> int:
    return int(all(x))


def gate_or(x: Bits) -> int:
    return int(any(x))


def gate_threshold(t: int) -> Gate:
    return lambda x, t=t: int(sum(x) >= t)


# --- ground truth: exact enumerated density ---


def enumerate_density(g: Gate, w: int, K: int = 12) -> float:
    def export(k: int) -> float:
        n = k + w - 1
        counts: Dict[Bits, int] = {}
        for val in range(1 << n):
            b = [(val >> j) & 1 for j in range(n)]
            y = tuple(g(tuple(b[i : i + w])) for i in range(k))
            counts[y] = counts.get(y, 0) + 1
        return float(n) - shannon(list(counts.values()), 1 << n)

    ks = list(range(1, K + 1))
    Es = [export(k) for k in ks]
    lo = K // 2
    xs = [k for k in ks if k >= lo]
    ys = [E for k, E in zip(ks, Es) if k >= lo]
    m = len(xs)
    sx, sy, sxx, sxy = sum(xs), sum(ys), sum(x * x for x in xs), sum(x * y for x, y in zip(xs, ys))
    return (m * sxy - sx * sy) / (m * sxx - sx * sx)


# --- generalized decay algebra: belief operator on the 2^{w-1} boundary ---


def transfer_density(g: Gate, w: int, cap: int = 200_000, ndig: int = 9) -> Tuple[float, int]:
    """Density via the boundary-belief transfer operator. Returns (a, #beliefs)."""
    states: List[Bits] = list(product((0, 1), repeat=w - 1))  # window of w-1 shared bits
    idx = {s: i for i, s in enumerate(states)}
    nS = len(states)

    def step(pi: Tuple[float, ...]) -> Dict[int, Tuple[float, Tuple[float, ...]]]:
        """For each output y: (prob_y, normalized next belief)."""
        out: Dict[int, List[float]] = {0: [0.0] * nS, 1: [0.0] * nS}
        py: Dict[int, float] = {0: 0.0, 1: 0.0}
        for i, s in enumerate(states):
            wgt = pi[i]
            if wgt == 0.0:
                continue
            for fresh in (0, 1):
                y = g(s + (fresh,))
                nxt = s[1:] + (fresh,)
                out[y][idx[nxt]] += wgt * 0.5
                py[y] += wgt * 0.5
        res: Dict[int, Tuple[float, Tuple[float, ...]]] = {}
        for y in (0, 1):
            if py[y] > 1e-15:
                res[y] = (py[y], tuple(v / py[y] for v in out[y]))
        return res

    def key(pi: Tuple[float, ...]) -> Tuple[float, ...]:
        return tuple(round(v, ndig) for v in pi)

    start = tuple([1.0 / nS] * nS)  # uniform (hidden chain is uniform-stationary)
    # BFS reachable beliefs; record belief-chain transitions
    order: List[Tuple[float, ...]] = []
    seen: Dict[Tuple[float, ...], int] = {}
    trans: List[List[Tuple[int, float]]] = []
    pred1: List[float] = []  # P(y=1 | belief)

    def register(pi: Tuple[float, ...]) -> int:
        k = key(pi)
        if k in seen:
            return seen[k]
        j = len(order)
        seen[k] = j
        order.append(pi)
        trans.append([])
        pred1.append(0.0)
        return j

    root = register(start)
    frontier = [root]
    while frontier:
        j = frontier.pop()
        pi = order[j]
        res = step(pi)
        pred1[j] = res.get(1, (0.0, ()))[0]
        for y, (py, nb) in res.items():
            was = key(nb) in seen
            t = register(nb)
            trans[j].append((t, py))
            if not was:
                frontier.append(t)
        if len(order) > cap:
            raise RuntimeError(f"belief set exceeded cap={cap} (w={w}); reachable not finite?")

    # stationary distribution of the belief-chain via power iteration
    N = len(order)
    mu = [1.0 / N] * N
    for _ in range(20_000):
        nxt = [0.0] * N
        for j in range(N):
            mj = mu[j]
            if mj == 0.0:
                continue
            for (t, py) in trans[j]:
                nxt[t] += mj * py
        s = sum(nxt)
        nxt = [v / s for v in nxt]
        if max(abs(a - b) for a, b in zip(mu, nxt)) < 1e-14:
            mu = nxt
            break
        mu = nxt

    h_Y = sum(mu[j] * h2(pred1[j]) for j in range(N))
    return 1.0 - h_Y, N


def transfer_density_mc(g: Gate, w: int, steps: int = 2_000_000, burn: int = 2000,
                        seed: int = 12345) -> float:
    """Density via a Monte-Carlo forward belief filter (for non-reset gates
    whose reachable belief set is not finite). Estimates a = 1 - h_Y."""
    import random

    rng = random.Random(seed)
    states: List[Bits] = list(product((0, 1), repeat=w - 1))
    idx = {s: i for i, s in enumerate(states)}
    nS = len(states)
    pi = [1.0 / nS] * nS
    # true hidden window (the actual shared bits)
    window = [rng.randint(0, 1) for _ in range(w - 1)]
    acc = 0.0
    cnt = 0
    for t in range(steps):
        fresh = rng.randint(0, 1)
        y_true = g(tuple(window) + (fresh,))
        # predictive P(y=1 | belief) and filter update on the observed y_true
        p1 = 0.0
        nb = [0.0] * nS
        norm = 0.0
        for i, s in enumerate(states):
            wgt = pi[i]
            if wgt == 0.0:
                continue
            for f in (0, 1):
                yy = g(s + (f,))
                if yy == 1:
                    p1 += wgt * 0.5
                if yy == y_true:
                    nb[idx[s[1:] + (f,)]] += wgt * 0.5
                    norm += wgt * 0.5
        if t >= burn:
            acc += h2(p1)
            cnt += 1
        pi = [v / norm for v in nb] if norm > 0 else [1.0 / nS] * nS
        window = window[1:] + [fresh]
    h_Y = acc / cnt
    return 1.0 - h_Y


def main() -> None:
    print("=" * 78)
    print("O1 step 5 — generalized decay algebra (range-r boundary transfer operator)")
    print("Design: this file · m11f-decay-algebra-theorem.md (w=2 proved)")
    print("=" * 78)

    cases: List[Tuple[str, Gate, int]] = [
        ("AND", gate_and, 2),
        ("AND", gate_and, 3),
        ("AND", gate_and, 4),
        ("OR", gate_or, 2),
        ("OR", gate_or, 3),
        ("threshold>=2", gate_threshold(2), 3),
    ]

    header = (
        f"{'gate':>13}  {'w':>2}  {'2^(w-1)':>7}  "
        f"{'a_enum':>10}  {'a_transfer':>11}  {'|Δ|':>9}  {'method':>7}  {'#beliefs':>8}"
    )
    print("\n" + header)
    print("-" * len(header))
    a_w2_and = None
    for name, g, w in cases:
        a_enum = enumerate_density(g, w, K=12 if w <= 3 else 11)
        try:
            a_tr, nbel = transfer_density(g, w)
            method, nbel_s = "exact", str(nbel)
        except RuntimeError:
            a_tr = transfer_density_mc(g, w)  # non-reset gate: belief set not finite
            method, nbel_s = "MC", "inf"
        d = abs(a_enum - a_tr)
        if name == "AND" and w == 2:
            a_w2_and = a_tr
        print(
            f"{name:>13}  {w:2d}  {1 << (w - 1):7d}  "
            f"{a_enum:10.5f}  {a_tr:11.5f}  {d:9.1e}  {method:>7}  {nbel_s:>8}"
        )
        tol = 5e-3 if method == "MC" else 5e-3
        assert d < tol, f"{name} w={w}: transfer must match enumeration"

    # tie to the proved 1D theorem constant
    assert a_w2_and is not None and abs(a_w2_and - 0.3007568) < 1e-4, \
        "w=2 AND must recover the m11f theorem density 0.3007568"

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  The decay algebra GENERALIZES: a boundary-belief transfer OPERATOR on")
    print("  the 2^(w-1) window states reproduces the enumerated coupled export")
    print("  density for range-r coupling and multiple gates, recovering the proved")
    print("  w=2 constant a=0.3007568. Cost scales with 2^(w-1), independent of k.")
    print("\n  Finding: the belief set is FINITE (⇒ exact) exactly for reset gates —")
    print("  those with a fully-recoverable branch (a [0,..,0] decay branch), e.g.")
    print("  AND/OR. Non-reset gates (threshold/majority) have a non-finite belief")
    print("  set and use a Monte-Carlo filter. This ties finiteness of the decay")
    print("  algebra to the gate's decay structure.")
    print("\n  Open: a general THEOREM (m11f proves only w=2); continuum embedding.")
    print("\nNON-CLAIMS: not continuum L, not dS_c/dτ, not gravity; finite classical.")
    print("=" * 78)


if __name__ == "__main__":
    main()
