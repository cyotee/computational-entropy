#!/usr/bin/env python3
"""
Tier 2 toy — log-cardinality function unidentifiability d_f^# and a Toffoli-register
persistence toy (finite classical; no gravity, no quantum).

Definitions (see TIER2_INSTRUCTION_PERSISTENCE.md):
  X uniform on a finite set of size N; f: X -> Y deterministic, fibre sizes W_y.
  Observational (informational) equivalence: g ~ f  iff  g_* p_X = f_* p_X
  (same output law; Paper A Prop. 1 / canonical definition after 378e51c).
  [f] = {g : X -> Y : |g^{-1}(y)| = W_y for all y}, |[f]| = N! / prod_y W_y!
  d_f^# := log2 |[f]|  (bits).

Checks (all exact integer arithmetic; logs only for display):
  A. |[f]| by brute-force enumeration == multinomial; type-class bounds
     N*H(Y) - |Y|*log2(N+1) <= d_f^# <= N*H(Y)  (type-class bounds, Cover & Thomas Thm 11.1.3);
     uniform prior over all functions X->Y conditioned on "output law = f's"
     gives a uniform posterior on [f], whose Shannon entropy is d_f^#.
  B. Composition chain rule (pure cascade X -f-> Y -g-> Z):
       d_f^# = d_{g.f}^# + R(g|f),  R(g|f) = sum_z log2( V_z! / prod_{y in g^-1(z)} W_y! ),
     V_z = sum_{y in g^-1(z)} W_y.  Also shows naive additivity d_{g.f} = d_f + d_g FAILS.
  C. Toffoli toy: for every 2-input Boolean f, BFS over NOT/CNOT/Toffoli (NCT) circuits on
     w = 2,3,4 lines (inputs on lines 0,1; ancillas start at 0; garbage allowed). Report the
     minimum gate count per width and a joint cost
       J(w) = w + g_min(w) * log2(G_w) + log2(w)
     (register width + bits to store the gate list + output-line index), G_w = # NCT gate
     placements on w lines. For 3-input f, report which are computable with 0 ancillas (w=3).

NON-CLAIMS: J is one illustrative cost convention, not a proved resource bound; the
joint minimum of output capacity + instruction persistence is an OPEN problem.
"""

from __future__ import annotations

import itertools
import math
from collections import Counter, deque
from fractions import Fraction


def multinomial(n: int, parts: list[int]) -> int:
    out = math.factorial(n)
    for p in parts:
        out //= math.factorial(p)
    return out


def entropy_bits(counts: list[int]) -> float:
    n = sum(counts)
    return -sum((c / n) * math.log2(c / n) for c in counts if c)


def fibres(table: tuple) -> list[int]:
    return list(Counter(table).values())


# ---------------------------------------------------------------- A
def part_a() -> None:
    print("A. d_f^# = log2|[f]| for 2-input Boolean maps (X uniform on {0,1}^2, N=4)")
    xs = list(itertools.product((0, 1), repeat=2))
    N = len(xs)
    all_fns = list(itertools.product((0, 1), repeat=N))  # truth tables
    named = {
        "const0": lambda a, b: 0,
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "XOR": lambda a, b: a ^ b,
        "x1": lambda a, b: a,
    }
    print(f"  {'f':7s} {'W_y':10s} {'|[f]| enum':>10s} {'multinom':>9s} {'d_f#':>7s} "
          f"{'N*H(Y)':>7s} {'lower':>7s} {'post.H':>7s}")
    for name, fn in named.items():
        t = tuple(fn(a, b) for a, b in xs)
        W = sorted(fibres(t))
        law = Counter(t)
        cls = [g for g in all_fns if Counter(g) == law]
        m = multinomial(N, W)
        assert len(cls) == m
        d = math.log2(m)
        NH = N * entropy_bits(W)
        lower = NH - len(W) * math.log2(N + 1)
        assert lower - 1e-12 <= d <= NH + 1e-12
        # uniform prior over all 2^N functions, condition on output law == law
        post = [Fraction(1, len(cls))] * len(cls)
        postH = -sum(float(p) * math.log2(float(p)) for p in post)
        assert abs(postH - d) < 1e-12
        print(f"  {name:7s} {str(W):10s} {len(cls):10d} {m:9d} {d:7.4f} {NH:7.4f} "
              f"{lower:7.4f} {postH:7.4f}")
    print("  PASS: enumeration == multinomial; type bounds hold; uniform-prior posterior "
          "entropy == d_f^#.\n")


# ---------------------------------------------------------------- B
def d_sharp(N: int, W: list[int]) -> float:
    return math.log2(multinomial(N, W))


def chain(name: str, xs: list, f, g) -> None:
    N = len(xs)
    ys = [f(x) for x in xs]
    zs = [g(y) for y in ys]
    Wy = Counter(ys)
    Vz = Counter(zs)
    # exact integer factorisation  N!/prod W_y! = [N!/prod V_z!] * prod_z [V_z!/prod W_y!]
    lhs = multinomial(N, list(Wy.values()))
    rhs_outer = multinomial(N, list(Vz.values()))
    refine = 1
    for z, v in Vz.items():
        refine *= multinomial(v, [w for y, w in Wy.items() if g(y) == z])
    assert lhs == rhs_outer * refine, name
    df, dgf, R = math.log2(lhs), math.log2(rhs_outer), math.log2(refine)
    # d_g^# relative to g's own input law f_* p_X is NOT a multinomial in N in general;
    # compare with the naive "d_g relative to uniform input on image(f)".
    img = sorted(Wy)
    dg_unif = d_sharp(len(img), list(Counter(g(y) for y in img).values()))
    print(f"  {name:28s} d_f#={df:7.4f}  d_(g.f)#={dgf:7.4f}  R(g|f)={R:7.4f}  "
          f"check d_f#=d_(g.f)#+R: {abs(df - dgf - R) < 1e-9}   "
          f"naive d_f#+d_g#={df + dg_unif:7.4f} vs d_(g.f)#={dgf:7.4f}")


def part_b() -> None:
    print("B. Composition (pure cascade X -f-> Y -g-> Z): exact chain rule, naive additivity fails")
    x2 = list(itertools.product((0, 1), repeat=2))
    x3 = list(itertools.product((0, 1), repeat=3))
    chain("id ; AND", x2, lambda x: x, lambda y: y[0] & y[1])
    chain("AND ; NOT", x2, lambda x: x[0] & x[1], lambda y: 1 - y)
    chain("(x1&x2, x3) ; AND  (=AND3)", x3, lambda x: (x[0] & x[1], x[2]), lambda y: y[0] & y[1])
    chain("(x1^x2, x3) ; XOR  (=XOR3)", x3, lambda x: (x[0] ^ x[1], x[2]), lambda y: y[0] ^ y[1])
    print("  PASS: d_f# = d_(g.f)# + R(g|f) exactly (integer identity); d_(g.f)# <= d_f#.\n")


# ---------------------------------------------------------------- C
def nct_gates(w: int):
    for t in range(w):
        yield ("NOT", t)
    for c, t in itertools.permutations(range(w), 2):
        yield ("CNOT", c, t)
    for t in range(w):
        for a, b in itertools.combinations([i for i in range(w) if i != t], 2):
            yield ("TOF", a, b, t)


def apply(state: tuple, gate, full: int) -> tuple:
    s = list(state)
    if gate[0] == "NOT":
        s[gate[1]] ^= full
    elif gate[0] == "CNOT":
        s[gate[2]] ^= s[gate[1]]
    else:
        s[gate[3]] ^= s[gate[1]] & s[gate[2]]
    return tuple(s)


def bfs_min_gates(n_in: int, w: int) -> dict[int, int]:
    """Return {truth-table mask: min #gates for it to appear on some line}."""
    npts = 2 ** n_in
    full = (1 << npts) - 1
    inputs = []
    for i in range(n_in):
        m = 0
        for p in range(npts):
            if (p >> (n_in - 1 - i)) & 1:
                m |= 1 << p
        inputs.append(m)
    start = tuple(inputs + [0] * (w - n_in))
    gates = list(nct_gates(w))
    seen = {start: 0}
    best: dict[int, int] = {}
    dq = deque([start])
    while dq:
        s = dq.popleft()
        d = seen[s]
        for line in s:
            if line not in best:
                best[line] = d
        for gt in gates:
            nxt = apply(s, gt, full)
            if nxt not in seen:
                seen[nxt] = d + 1
                dq.append(nxt)
    return best


def part_c() -> None:
    print("C. Toffoli-register toy (NCT gates; inputs on lines 0,1; ancillas start 0)")
    names = {0b0000: "0", 0b1111: "1", 0b1000: "AND", 0b1110: "OR", 0b0110: "XOR",
             0b1001: "XNOR", 0b0111: "NAND", 0b0001: "NOR", 0b1100: "x1", 0b1010: "x2",
             0b0011: "NOT x1", 0b0101: "NOT x2", 0b0100: "x1&~x2", 0b0010: "~x1&x2",
             0b1101: "x1|~x2", 0b1011: "~x1|x2"}
    res = {w: bfs_min_gates(2, w) for w in (2, 3, 4)}
    Gw = {w: sum(1 for _ in nct_gates(w)) for w in (2, 3, 4)}
    print(f"  NCT gate placements G_w: {Gw}")
    print(f"  {'f':8s} {'W_y':7s} {'d_f#':>6s} | g_min(w=2,3,4) | min w | J(w)=w+g*log2(G_w)+log2(w) (w=2,3,4) | argmin J")
    for mask in sorted(names):
        ones = bin(mask).count("1")
        W = [c for c in (ones, 4 - ones) if c]
        d = d_sharp(4, W)
        gm = [res[w].get(mask) for w in (2, 3, 4)]
        minw = next(w for w, g in zip((2, 3, 4), gm) if g is not None)
        J = {w: (w + g * math.log2(Gw[w]) + math.log2(w)) if g is not None else None
             for w, g in zip((2, 3, 4), gm)}
        jstr = " ".join(f"{J[w]:6.2f}" if J[w] is not None else "   -  " for w in (2, 3, 4))
        arg = min((w for w in J if J[w] is not None), key=lambda w: J[w])
        gstr = ",".join("-" if g is None else str(g) for g in gm)
        print(f"  {names[mask]:8s} {str(sorted(W)):7s} {d:6.3f} | {gstr:14s} | {minw:5d} | {jstr:36s} | w={arg}")
    reach2 = {m for m in names if res[2].get(m) is not None}
    nonconst_affine = {0b1100, 0b1010, 0b0011, 0b0101, 0b0110, 0b1001}
    assert reach2 == nonconst_affine
    assert all(res[3].get(m) is not None for m in names)
    print(f"  w=2 (no ancilla) reaches exactly {len(reach2)} of 16 functions (the non-constant affine"
          " ones); all 16 are reachable at w=3 (one ancilla).")
    print("  Observation: d_f# does not order register need (XOR: d_f#=2.585, 0 ancillas;"
          " AND: d_f#=2.000, 1 ancilla).\n")

    best3 = bfs_min_gates(3, 3)
    print(f"  3-input functions computable with 0 ancillas (w=3): {len(best3)} of 256")
    for nm, mask in (("AND3", 0b10000000), ("MAJ3", 0b11101000), ("XOR3", 0b10010110)):
        print(f"    {nm:5s}: {'g_min=' + str(best3[mask]) if mask in best3 else 'NOT reachable at w=3'}")
    print("  (w=4 for 3-input functions not searched here: future work.)\n")


def main() -> None:
    print("=" * 96)
    print("Tier 2 toy: log-cardinality d_f^# and Toffoli-register persistence (finite classical)")
    print("=" * 96)
    part_a()
    part_b()
    part_c()
    print("NON-CLAIMS: J(w) is an illustrative cost convention, not a proved bound; the joint minimum")
    print("of output capacity + instruction persistence is OPEN (TIER2 problem statement). No gravity.")
    print("=" * 96)


if __name__ == "__main__":
    main()
