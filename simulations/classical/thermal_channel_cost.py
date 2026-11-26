#!/usr/bin/env python3
"""Tier 2 toy exploration (speculative): thermal amplitude-damping channel cost.

Pure numpy/python. No quantum library. Run:

    python simulations/classical/thermal_channel_cost.py            # full report
    python simulations/classical/thermal_channel_cost.py --eps 0.02 --grid 21 --n-bool 3

What this computes (all choices are conventions of this toy, stated here):

* Channel. Single-qubit amplitude damping AD(gamma), Kraus
  K0 = [[1,0],[0,sqrt(1-gamma)]], K1 = [[0,sqrt(gamma)],[0,0]].
* Output distribution. Fixed input |1>, computational-basis measurement:
  P(1) = 1 - gamma. Every candidate is reduced to a law on {0,1}:
    - Boolean f:{0,1}^n -> {0,1} with uniform inputs: P(f=1) = popcount(f)/2^n;
    - a Kraus channel E: same protocol as the target, P(1) = <1|E(|1><1|)|1>.
  The comparison is the total-variation distance between two Bernoulli laws,
  TV = |p - q|.  Comparing a 2-input function on uniform inputs with a
  1-qubit channel on a fixed input is a modelling choice: only the output law
  on {0,1} is compared, nothing else.
* Class and d#_eps. C_eps(gamma) = {candidates g : TV(g, AD(gamma)) <= eps};
  d#_eps(gamma) := log2 |C_eps(gamma)| (undefined, reported "-", when empty).
  This is an epsilon-ball relaxation of TIER2's d_f^# = log2|[f]| ([f] = maps
  with exactly the same output law). For Boolean-only sets at eps = 0 and
  gamma = 1 - k/2^n it reduces exactly to TIER2's count C(2^n, k) (checked).
* Temperature (Cyotee's toy parametrization, not standard physics).
  gamma = 1/(e^{bw}+1), bw = beta*hbar*omega, hbar*omega = k_B = 1, so
  T = 1/bw = 1/ln((1-gamma)/gamma).  T >= 0 covers gamma in [0, 1/2] only
  (T -> 0: gamma -> 0; T -> inf: gamma -> 1/2).  gamma in (1/2, 1] needs
  bw < 0, i.e. negative temperature; that branch is computed and labelled but
  kept out of every cost-vs-T statement.  Physically, finite-temperature
  amplitude damping is the generalized amplitude damping channel; that is
  NOT what is modelled here.
* Cost (pricing convention). cost = d#_eps * k_B * T * ln 2.  This prices
  retained (not erased) bits at the Landauer rate, which is itself a
  modelling choice.  The explicit factor T makes cost rise with T by
  construction, so the verdict is judged on d#_eps and on cost/T = d#_eps ln2.

No quantum or thermodynamic claim is made beyond the Landauer pricing
convention.
"""

from __future__ import annotations

import argparse
import itertools
import math
from dataclasses import dataclass

import numpy as np

LN2 = math.log(2.0)
TOL = 1e-12


# ---------------------------------------------------------------------------
# Channels (Kraus, numpy)
# ---------------------------------------------------------------------------

def _check_tp(kraus: list[np.ndarray]) -> None:
    s = sum(k.conj().T @ k for k in kraus)
    assert np.allclose(s, np.eye(2), atol=1e-12), "Kraus set not trace preserving"


def apply(kraus: list[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ k.conj().T for k in kraus)


def p1_on_ket1(kraus: list[np.ndarray]) -> float:
    """P(1) after the channel acts on |1><1| (computational-basis readout)."""
    _check_tp(kraus)
    rho = np.array([[0, 0], [0, 1]], dtype=complex)
    out = apply(kraus, rho)
    return float(np.real(out[1, 1]))


def amplitude_damping(g: float) -> list[np.ndarray]:
    return [np.array([[1, 0], [0, math.sqrt(1 - g)]], dtype=complex),
            np.array([[0, math.sqrt(g)], [0, 0]], dtype=complex)]


def phase_damping(lam: float) -> list[np.ndarray]:
    return [np.array([[1, 0], [0, math.sqrt(1 - lam)]], dtype=complex),
            np.array([[0, 0], [0, math.sqrt(lam)]], dtype=complex)]


def depolarizing(p: float) -> list[np.ndarray]:
    i2 = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    return [math.sqrt(1 - 3 * p / 4) * i2] + [math.sqrt(p / 4) * m for m in (x, y, z)]


def bit_flip(p: float) -> list[np.ndarray]:
    return [math.sqrt(1 - p) * np.eye(2, dtype=complex),
            math.sqrt(p) * np.array([[0, 1], [1, 0]], dtype=complex)]


def unitary(u: np.ndarray) -> list[np.ndarray]:
    return [np.asarray(u, dtype=complex)]


def reset_to(b: int) -> list[np.ndarray]:
    ket = np.zeros((2, 1), dtype=complex)
    ket[b, 0] = 1
    return [ket @ np.array([[1, 0]], dtype=complex), ket @ np.array([[0, 1]], dtype=complex)]


def measure() -> list[np.ndarray]:
    return [np.diag([1, 0]).astype(complex), np.diag([0, 1]).astype(complex)]


def fixed_quantum_ops() -> dict[str, float]:
    h = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    ops = {
        "I": unitary(np.eye(2)),
        "X": unitary([[0, 1], [1, 0]]),
        "Z": unitary([[1, 0], [0, -1]]),
        "H": unitary(h),
        "dephase(1)": phase_damping(1.0),
        "measure": measure(),
        "reset|0>": reset_to(0),
        "reset|1>": reset_to(1),
    }
    return {k: p1_on_ket1(v) for k, v in ops.items()}


def family_quantum_ops(grid: int) -> dict[str, float]:
    """Parametrized families on a uniform grid of `grid` points in [0,1]."""
    out: dict[str, float] = {}
    for x in np.linspace(0.0, 1.0, grid):
        x = float(x)
        out[f"AD({x:.3f})"] = p1_on_ket1(amplitude_damping(x))
        out[f"PD({x:.3f})"] = p1_on_ket1(phase_damping(x))
        out[f"DEP({x:.3f})"] = p1_on_ket1(depolarizing(x))
        out[f"BF({x:.3f})"] = p1_on_ket1(bit_flip(x))
    return out


# ---------------------------------------------------------------------------
# Boolean functions: P(f=1) under uniform inputs, counted by popcount
# ---------------------------------------------------------------------------

def boolean_counts(n: int) -> dict[float, int]:
    """{P(f=1): number of f:{0,1}^n->{0,1} with that law} = {k/2^n: C(2^n,k)}."""
    m = 2 ** n
    return {k / m: math.comb(m, k) for k in range(m + 1)}


def boolean_counts_enumerated(n: int) -> dict[float, int]:
    m = 2 ** n
    out: dict[float, int] = {}
    for table in itertools.product((0, 1), repeat=m):
        q = sum(table) / m
        out[q] = out.get(q, 0) + 1
    return out


# ---------------------------------------------------------------------------
# Temperature map (toy)
# ---------------------------------------------------------------------------

def bw_of_gamma(g: float) -> float:
    if g <= 0:
        return math.inf
    if g >= 1:
        return -math.inf
    return math.log((1 - g) / g)


def T_of_gamma(g: float) -> float:
    bw = bw_of_gamma(g)
    if bw == 0:
        return math.inf
    if math.isinf(bw):
        return 0.0 if bw > 0 else -0.0
    return 1.0 / bw


def branch(g: float) -> str:
    if abs(g - 0.5) < TOL:
        return "T=inf"
    return "T>=0" if g < 0.5 else "T<0"


# ---------------------------------------------------------------------------
# Class sizes
# ---------------------------------------------------------------------------

@dataclass
class CandidateSet:
    name: str
    boolean_n: int | None
    fixed_q: bool
    grid: int  # 0 = no parametrized families

    def laws(self) -> list[tuple[float, int]]:
        """List of (P(1), multiplicity)."""
        items: list[tuple[float, int]] = []
        if self.boolean_n is not None:
            items += list(boolean_counts(self.boolean_n).items())
        if self.fixed_q:
            items += [(p, 1) for p in fixed_quantum_ops().values()]
        if self.grid:
            items += [(p, 1) for p in family_quantum_ops(self.grid).values()]
        return items

    def size(self) -> int:
        return sum(m for _, m in self.laws())


def class_size(laws: list[tuple[float, int]], target_p1: float, eps: float) -> int:
    return sum(m for p, m in laws if abs(p - target_p1) <= eps + TOL)


def dhash(size: int) -> float:
    return math.log2(size) if size > 0 else math.nan


# ---------------------------------------------------------------------------
# Knee detection
# ---------------------------------------------------------------------------

def knee_second_difference(x: np.ndarray, y: np.ndarray) -> tuple[float, float] | None:
    """x at max |discrete second derivative| (non-uniform 3-point formula)."""
    ok = ~np.isnan(y)
    x, y = x[ok], y[ok]
    if len(x) < 3:
        return None
    d2 = []
    for i in range(1, len(x) - 1):
        h1, h2 = x[i] - x[i - 1], x[i + 1] - x[i]
        d2.append(2 * (h1 * y[i + 1] - (h1 + h2) * y[i] + h2 * y[i - 1]) / (h1 * h2 * (h1 + h2)))
    d2 = np.abs(np.array(d2))
    i = int(np.argmax(d2))
    return float(x[i + 1]), float(d2[i])


def knee_two_segment(x: np.ndarray, y: np.ndarray) -> tuple[float, float] | None:
    """Best continuous 2-segment fit breakpoint; returns (x_break, SSE ratio 2seg/1seg)."""
    ok = ~np.isnan(y)
    x, y = x[ok], y[ok]
    if len(x) < 5:
        return None
    a1 = np.vstack([np.ones_like(x), x]).T
    sse1 = float(np.sum((y - a1 @ np.linalg.lstsq(a1, y, rcond=None)[0]) ** 2))
    best = (math.inf, None)
    for xb in x[2:-2]:
        a = np.vstack([np.ones_like(x), x, np.maximum(x - xb, 0)]).T
        sse = float(np.sum((y - a @ np.linalg.lstsq(a, y, rcond=None)[0]) ** 2))
        if sse < best[0]:
            best = (sse, float(xb))
    ratio = best[0] / sse1 if sse1 > 0 else math.nan
    return best[1], ratio


def jumps(x: np.ndarray, y: np.ndarray) -> list[float]:
    """x positions where y changes value (step edges); NaN treated as a value."""
    out = []
    for i in range(1, len(x)):
        a, b = y[i - 1], y[i]
        if (math.isnan(a) != math.isnan(b)) or (not math.isnan(a) and abs(a - b) > 1e-9):
            out.append(float(x[i]))
    return out


def binary_entropy(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-300, 1 - 1e-16)
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))


def smooth_reference() -> dict[str, float]:
    """Large-n, eps->0 limit: d#/2^n -> H_b(1-gamma) = H_b(gamma) (method of types).

    Returns the location of maximal curvature of h(T) = H_b(gamma(T)) on T>0,
    and of H_b(gamma) on gamma in (0, 1/2).  This curvature is a property of the
    Fermi-type map gamma(T) and of H_b, not of any class structure.
    """
    T = np.linspace(0.01, 5.0, 4991)
    g = 1.0 / (np.exp(1.0 / T) + 1.0)
    h = binary_entropy(g)
    d1 = np.gradient(h, T)
    d2 = np.gradient(d1, T)
    i_curv = int(np.argmax(d2))
    i_slope = int(np.argmax(d1))
    gg = np.linspace(0.001, 0.499, 4981)
    hg = binary_entropy(gg)
    d2g = np.gradient(np.gradient(hg, gg), gg)
    return {
        "T_max_curvature": float(T[i_curv]),
        "gamma_at_T_max_curvature": float(g[i_curv]),
        "T_max_slope": float(T[i_slope]),
        "gamma_at_T_max_slope": float(g[i_slope]),
        "h_at_T5": float(h[-1]),
        "Hb_gamma_concave_everywhere": bool(np.all(d2g < 0)),
    }


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks() -> None:
    # Kraus completeness and AD output law
    for g in np.linspace(0, 1, 11):
        assert abs(p1_on_ket1(amplitude_damping(float(g))) - (1 - g)) < 1e-12
        for fam in (phase_damping, depolarizing, bit_flip):
            _check_tp(fam(float(g)))
    # Boolean popcount counting matches explicit enumeration
    for n in (1, 2, 3):
        assert boolean_counts(n) == boolean_counts_enumerated(n), n
    assert sum(boolean_counts(2).values()) == 16
    # eps = 0, Boolean only: class at gamma = 1 - k/4 equals TIER2 |[f]| = C(4,k)
    laws = list(boolean_counts(2).items())
    for k in range(5):
        assert class_size(laws, k / 4, 0.0) == math.comb(4, k)
    # Temperature map: gamma in [0, 1/2] iff T >= 0, round trip
    for T in (0.05, 0.3, 1.0, 10.0, 1e3):
        g = 1 / (math.exp(1 / T) + 1)
        assert 0 <= g < 0.5 and abs(T_of_gamma(g) - T) / T < 1e-9
    assert T_of_gamma(0.7) < 0 and branch(0.7) == "T<0"


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt(v: float, nd: int = 3) -> str:
    if isinstance(v, float) and math.isnan(v):
        return "-"
    if isinstance(v, float) and math.isinf(v):
        return "inf" if v > 0 else "-inf"
    return f"{v:.{nd}f}"


def sweep(cs: CandidateSet, gammas: np.ndarray, eps: float):
    laws = cs.laws()
    rows = []
    for g in gammas:
        g = float(g)
        size = class_size(laws, 1 - g, eps)
        d = dhash(size)
        T = T_of_gamma(g)
        br = branch(g)
        cost = math.nan
        if br == "T>=0" and not math.isnan(d):
            cost = d * T * LN2
        rows.append((g, bw_of_gamma(g), T, br, size, d, cost))
    return rows


def analyse(rows) -> dict:
    pos = [r for r in rows if r[3] == "T>=0"]
    x = np.array([r[0] for r in pos])
    d = np.array([r[5] for r in pos])
    T = np.array([r[2] for r in pos])
    j = jumps(x, d)
    k2 = knee_second_difference(x, d)
    seg = knee_two_segment(x, d)
    distinct = len({round(v, 9) for v in d if not math.isnan(v)})
    empty = int(np.sum(np.isnan(d)))
    # knee in d vs T (finite T only)
    kT = knee_second_difference(T, d)
    artifact = k2 is not None and any(abs(k2[0] - jj) < 1e-9 or abs(k2[0] - jj) <= (x[1] - x[0]) + 1e-9 for jj in j)
    mono = all(np.diff(d[~np.isnan(d)]) >= -1e-9)
    def at(gv):
        i = int(np.argmin(np.abs(x - gv)))
        return float(d[i])
    return {"trend": (at(0.0), at(0.25), at(0.49)), "jumps": j, "knee_d2": k2, "knee_2seg": seg, "knee_d2_T": kT,
            "distinct": distinct, "empty": empty, "step_artifact": artifact,
            "monotone_nondecreasing": mono}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--eps", type=float, default=0.05)
    ap.add_argument("--grid", type=int, default=11, help="points per parametrized Kraus family (0 = none)")
    ap.add_argument("--n-bool", type=int, default=2, help="Boolean functions {0,1}^n -> {0,1}")
    ap.add_argument("--dgamma", type=float, default=0.01)
    ap.add_argument("--table-step", type=float, default=0.05, help="gamma step for the printed table")
    args = ap.parse_args()

    self_checks()
    print("Self-checks passed (Kraus TP, AD law P(1)=1-gamma, Boolean enumeration n<=3,")
    print("eps=0 Boolean class = TIER2 C(4,k), T>=0 <=> gamma in [0,1/2]).\n")

    gammas = np.round(np.arange(0.0, 1.0 + args.dgamma / 2, args.dgamma), 10)

    print("Fixed quantum ops, P(1) on input |1>:",
          ", ".join(f"{k}={v:.3g}" for k, v in fixed_quantum_ops().items()))
    print()

    primary = CandidateSet(f"Bool n={args.n_bool} + fixed Q + families(grid={args.grid})",
                           args.n_bool, True, args.grid)
    bool_only = CandidateSet(f"Bool n={args.n_bool} only", args.n_bool, False, 0)
    no_fam = CandidateSet(f"Bool n={args.n_bool} + fixed Q", args.n_bool, True, 0)

    tstep = max(1, round(args.table_step / args.dgamma))
    print(f"## Main table (eps = {args.eps}); class size and d# for three candidate sets")
    print("Cost uses the primary set (with families). T<0 rows: no cost reported.\n")
    print("| gamma | bw | T | branch | \\|C\\| Bool | \\|C\\| +fixed Q | \\|C\\| +families | d# Bool | d# +fixed Q | d# primary | cost = d# T ln2 (primary) | cost/T |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    r_p = sweep(primary, gammas, args.eps)
    r_b = sweep(bool_only, gammas, args.eps)
    r_n = sweep(no_fam, gammas, args.eps)
    for i in range(0, len(gammas), tstep):
        g, bw, T, br, s, d, c = r_p[i]
        cpt = d * LN2 if not math.isnan(d) else math.nan
        print(f"| {g:.2f} | {fmt(bw)} | {fmt(T)} | {br} | {r_b[i][4]} | {r_n[i][4]} | {s} | {fmt(r_b[i][5])} | {fmt(r_n[i][5])} | {fmt(d)} | {fmt(c)} | {fmt(cpt)} |")
    print(f"\nCandidate-set sizes: {bool_only.name}: {bool_only.size()}; {no_fam.name}: {no_fam.size()}; "
          f"{primary.name}: {primary.size()}\n")

    print("## Knee / steepening on the T>=0 branch (gamma in [0, 0.49]), judged on d#_eps")
    print("Methods: (a) gamma at max |discrete 2nd derivative| of d#(gamma); (b) best continuous")
    print("two-segment linear fit (breakpoint, SSE ratio vs one line); (c) T at max |2nd derivative|")
    print("of d#(T). On a finite candidate set d# is piecewise constant in gamma, so (a) always lands on a\n"
          "step edge: last column checks this. A knee found by (a) is therefore a step artifact.\n")
    print("| candidate set | eps | d# at gamma 0 / 0.25 / 0.49 | distinct d# values | empty-class gammas | monotone in gamma | step edges | (a) gamma | (b) break, SSE ratio | (c) T | (a) at a step edge |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    sets = [CandidateSet("Bool n=2", 2, False, 0),
            CandidateSet("Bool n=2 + fixed Q", 2, True, 0),
            CandidateSet("Bool n=2 + fixed Q + fam(11)", 2, True, 11),
            CandidateSet("Bool n=2 + fixed Q + fam(21)", 2, True, 21),
            CandidateSet("Bool n=2 + fixed Q + fam(101)", 2, True, 101),
            CandidateSet("Bool n=3", 3, False, 0),
            CandidateSet("Bool n=4", 4, False, 0),
            CandidateSet("Bool n=6", 6, False, 0)]
    for cs in sets:
        for eps in (0.01, 0.02, 0.05, 0.1):
            a = analyse(sweep(cs, gammas, eps))
            edges = a["jumps"]
            es = ",".join(f"{e:.2f}" for e in edges[:6]) + ("…" if len(edges) > 6 else "")
            ka = fmt(a["knee_d2"][0], 2) if a["knee_d2"] else "-"
            kb = f"{a['knee_2seg'][0]:.2f}, {a['knee_2seg'][1]:.2f}" if a["knee_2seg"] and a["knee_2seg"][0] is not None else "-"
            kc = fmt(a["knee_d2_T"][0], 3) if a["knee_d2_T"] else "-"
            tr = " / ".join(fmt(v, 2) for v in a["trend"])
            print(f"| {cs.name} | {eps} | {tr} | {a['distinct']} | {a['empty']} | {'yes' if a['monotone_nondecreasing'] else 'no'} | "
                  f"{len(edges)} | {ka} | {kb} | {kc} | {'yes' if a['step_artifact'] else 'no'} |")

    pos_g = np.array([g for g in gammas if g < 0.5 - TOL])
    hb = binary_entropy(pos_g)
    sref = knee_two_segment(pos_g, hb)
    Tg = np.array([T_of_gamma(float(g)) for g in pos_g])
    cref = knee_second_difference(Tg, hb)
    r6 = sweep(CandidateSet("Bool n=6", 6, False, 0), gammas, 0.02)
    dev = max(abs(r[5] / 64 - float(binary_entropy(np.array([r[0]]))[0])) for r in r6 if r[3] == "T>=0" and not math.isnan(r[5]))
    print(f"\nSame methods applied to the smooth curve H_b(gamma) on the same gamma grid: (b) break "
          f"{sref[0]:.2f}, SSE ratio {sref[1]:.2f}; (c) T = {cref[0]:.3f}.")
    print(f"Bool n=6, eps=0.02: max |d#/64 - H_b(gamma)| on T>=0 = {dev:.3f} bits per input "
          "(finite-n and eps corrections; method of types).")
    ref = smooth_reference()
    print("\n## Smooth reference (large-n Boolean, eps -> 0): d#/2^n -> H_b(gamma)")
    print(f"H_b(gamma) concave on (0,1/2): {ref['Hb_gamma_concave_everywhere']} (no interior knee in gamma;"
          " steepest at gamma -> 0).")
    print(f"h(T) = H_b(gamma(T)): max curvature at T = {ref['T_max_curvature']:.3f} (gamma = "
          f"{ref['gamma_at_T_max_curvature']:.4f}); max slope at T = {ref['T_max_slope']:.3f} "
          f"(gamma = {ref['gamma_at_T_max_slope']:.4f}); h(5) = {ref['h_at_T5']:.3f}.")
    print("This onset comes from the Fermi-type map gamma(T) (Schottky-like activation),")
    print("not from the class structure of d#_eps.\n")

    print("Negative-T branch (gamma > 1/2): classes are computed in the table above but no cost")
    print("and no cost-vs-T statement is made there. Toy parametrization; not the generalized")
    print("amplitude damping channel. No quantum or thermodynamic claim beyond Landauer pricing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
