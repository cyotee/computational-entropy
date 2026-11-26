#!/usr/bin/env python3
"""Tier 2 toy exploration (speculative): joint encoding bound C_minus_K.

Extends thermal_channel_cost.py (same sweep, same toy map gamma <-> T, same
exclusion of the negative-T branch). Pure numpy. Run:

    python simulations/classical/joint_encoding_bound.py
    python simulations/classical/joint_encoding_bound.py --eps-k 0.01 --n-uses 1,10,100

Quantities (all conventions of this toy):

* C(gamma): Holevo capacity chi* of the amplitude-damping channel AD(gamma),
  the max over input ensembles of the Holevo information
  chi = S(sum_i p_i E(rho_i)) - sum_i p_i S(E(rho_i)), in bits per channel use.
  Computed two ways and cross-checked: (i) Nelder-Mead over a general
  two-pure-state ensemble on the Bloch sphere plus its probability (5 real
  parameters, random restarts); (ii) the closed form
  max_q [ h2((1-gamma) q) - h2((1 + sqrt(1 - 4 gamma (1-gamma) q^2))/2) ]
  (Giovannetti & Fazio 2005; Bennett et al. 1997). Literature check:
  C1 = 0.4717 at gamma = 1/2 (Giovannetti & Fazio 2005).  Unassisted classical
  capacity C = chi* (additivity) is stated in a 2026 preprint, Tang, Zhu, Bai &
  Wang, arXiv:2609.28592; we quote it, we do not reproduce it.
* K: crude UPPER-BOUND PROXIES for a description length of the channel. They
  are NOT Kolmogorov complexity, which is uncomputable and defined only up to an
  additive constant (invariance theorem).
    - K_eps: log2 of the number of eps-cells needed to cover the AD family in the
      Kraus-operator (Frobenius) metric, plus log2(#families in the CE-4 menu).
      The family's Kraus arc length is pi/2 (checked numerically), so
      K_eps = log2 ceil((pi/2)/eps_K) + log2 4. Independent of gamma.
    - K_circ: bits to write down one known Stinespring circuit for AD(gamma)
      (system + 1 ancilla: 3 CNOT + 2 Ry(+-theta/2), theta = 2 arcsin sqrt(gamma);
      not proved minimal): 5 gates x 2 bits (gate type x orientation) + one angle
      at log2 ceil(pi/eps_K) bits; 0 bits at gamma = 0 (identity).
* Units. C is bits per use; K is a one-time cost in bits. We report
  (a) per single use: C - K;
  (b) amortized over n uses: n*C - K (total bits) and C - K/n (bits per use);
  (c) break-even n* = K / C.
  For a fixed family K is (almost) independent of gamma, so C_minus_K tracks
  C(gamma) for every choice above.
* s for the "1/s" comparison: output entropy s = S(AD(|1><1|)) = h2(gamma) bits.
"""

from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thermal_channel_cost as tcc  # noqa: E402

LN2 = math.log(2.0)
RNG = np.random.default_rng(20261126)


# ---------------------------------------------------------------------------
# Entropy and Holevo information
# ---------------------------------------------------------------------------

def vn_entropy(rho: np.ndarray) -> float:
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-15]
    return float(-np.sum(w * np.log2(w)))


def h2(p: float) -> float:
    if p <= 0 or p >= 1:
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def ket(theta: float, phi: float) -> np.ndarray:
    return np.array([math.cos(theta / 2), np.exp(1j * phi) * math.sin(theta / 2)], dtype=complex)


def holevo(kraus, states, probs) -> float:
    outs = [tcc.apply(kraus, np.outer(s, s.conj())) for s in states]
    avg = sum(p * o for p, o in zip(probs, outs))
    return vn_entropy(avg) - sum(p * vn_entropy(o) for p, o in zip(probs, outs))


def chi_two_state(kraus, x: np.ndarray) -> float:
    t1, f1, t2, f2, a = x
    p = 1 / (1 + math.exp(-a))
    return holevo(kraus, [ket(t1, f1), ket(t2, f2)], [p, 1 - p])


def nelder_mead(f, x0, step=0.5, iters=400, tol=1e-12):
    """Minimal Nelder-Mead (minimizes f)."""
    n = len(x0)
    pts = [np.array(x0, float)] + [np.array(x0, float) + step * np.eye(n)[i] for i in range(n)]
    vals = [f(p) for p in pts]
    for _ in range(iters):
        order = np.argsort(vals)
        pts = [pts[i] for i in order]
        vals = [vals[i] for i in order]
        if abs(vals[-1] - vals[0]) < tol:
            break
        c = np.mean(pts[:-1], axis=0)
        xr = c + (c - pts[-1])
        fr = f(xr)
        if fr < vals[0]:
            xe = c + 2 * (c - pts[-1])
            fe = f(xe)
            pts[-1], vals[-1] = (xe, fe) if fe < fr else (xr, fr)
        elif fr < vals[-2]:
            pts[-1], vals[-1] = xr, fr
        else:
            xc = c + 0.5 * (pts[-1] - c)
            fc = f(xc)
            if fc < vals[-1]:
                pts[-1], vals[-1] = xc, fc
            else:
                pts = [pts[0]] + [pts[0] + 0.5 * (p - pts[0]) for p in pts[1:]]
                vals = [vals[0]] + [f(p) for p in pts[1:]]
    i = int(np.argmin(vals))
    return pts[i], vals[i]


def holevo_capacity_numeric(gamma: float, restarts: int = 12) -> float:
    kraus = tcc.amplitude_damping(gamma)
    best = 0.0
    for _ in range(restarts):
        x0 = np.array([RNG.uniform(0, math.pi), RNG.uniform(0, 2 * math.pi),
                       RNG.uniform(0, math.pi), RNG.uniform(0, 2 * math.pi), RNG.normal()])
        _, v = nelder_mead(lambda x: -chi_two_state(kraus, x), x0)
        best = max(best, -v)
    return best


def holevo_capacity_closed(gamma: float) -> tuple[float, float]:
    """max_q h2((1-g) q) - h2((1+sqrt(1-4 g (1-g) q^2))/2); returns (C, q*)."""
    def obj(q):
        return h2((1 - gamma) * q) - h2((1 + math.sqrt(max(0.0, 1 - 4 * gamma * (1 - gamma) * q * q))) / 2)
    qs = np.linspace(0, 1, 2001)
    vals = [obj(q) for q in qs]
    i = int(np.argmax(vals))
    lo, hi = qs[max(0, i - 1)], qs[min(len(qs) - 1, i + 1)]
    for _ in range(80):  # golden-section refine
        m1, m2 = lo + (hi - lo) * 0.382, lo + (hi - lo) * 0.618
        if obj(m1) < obj(m2):
            lo = m1
        else:
            hi = m2
    q = (lo + hi) / 2
    return max(obj(q), vals[i]), q


# ---------------------------------------------------------------------------
# Complexity proxies (crude upper bounds; NOT Kolmogorov complexity)
# ---------------------------------------------------------------------------

N_FAMILIES = 4  # AD, PD, DEP, BF in the CE-4 menu


def kraus_arc_length(npts: int = 200001) -> float:
    g = np.linspace(0, 1, npts)
    k0 = np.sqrt(1 - g)
    k1 = np.sqrt(g)
    return float(np.sum(np.sqrt(np.diff(k0) ** 2 + np.diff(k1) ** 2)))


def K_eps(eps_k: float) -> float:
    return math.log2(math.ceil((math.pi / 2) / eps_k)) + math.log2(N_FAMILIES)


def K_circ(gamma: float, eps_k: float) -> float:
    if gamma <= 0:
        return 0.0
    return 5 * 2 + math.log2(math.ceil(math.pi / eps_k))


def stinespring_circuit_check(gamma: float) -> float:
    """Max |error| of the 3-CNOT + 2-Ry circuit vs AD(gamma) Kraus action on random states."""
    th = 2 * math.asin(math.sqrt(gamma))

    def ry(a):
        return np.array([[math.cos(a / 2), -math.sin(a / 2)], [math.sin(a / 2), math.cos(a / 2)]], dtype=complex)
    i2 = np.eye(2, dtype=complex)
    p0, p1 = np.diag([1, 0]).astype(complex), np.diag([0, 1]).astype(complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    cnot_sa = np.kron(p0, i2) + np.kron(p1, x)  # control system (first), target ancilla
    cnot_as = np.kron(i2, p0) + np.kron(x, p1)  # control ancilla, target system
    # controlled-Ry(th) (system controls ancilla) = (I x Ry(th/2)) CNOT (I x Ry(-th/2)) CNOT
    cry = np.kron(i2, ry(th / 2)) @ cnot_sa @ np.kron(i2, ry(-th / 2)) @ cnot_sa
    u = cnot_as @ cry
    err = 0.0
    for _ in range(5):
        v = RNG.normal(size=2) + 1j * RNG.normal(size=2)
        v /= np.linalg.norm(v)
        rho = np.outer(v, v.conj())
        big = u @ np.kron(rho, np.diag([1, 0])) @ u.conj().T
        red = big.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)
        err = max(err, float(np.max(np.abs(red - tcc.apply(tcc.amplitude_damping(gamma), rho)))))
    return err


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks() -> dict:
    out = {}
    # closed form vs numeric (general two-pure-state ensemble)
    diffs = []
    for g in (0.0, 0.1, 0.25, 0.5, 0.75, 0.9):
        cn = holevo_capacity_numeric(g)
        cc, _ = holevo_capacity_closed(g)
        diffs.append(abs(cn - cc))
    out["max_numeric_vs_closed"] = max(diffs)
    assert out["max_numeric_vs_closed"] < 1e-5, diffs
    c_half, q_half = holevo_capacity_closed(0.5)
    out["C_half"] = c_half
    assert abs(c_half - 0.4717) < 5e-4, c_half  # Giovannetti & Fazio 2005
    assert abs(holevo_capacity_closed(0.0)[0] - 1.0) < 1e-9
    assert holevo_capacity_closed(1.0)[0] < 1e-9
    # AD composition: AD(a) o AD(b) = AD(1-(1-a)(1-b))  (so C is non-increasing in gamma)
    for a, b in ((0.2, 0.3), (0.5, 0.1), (0.05, 0.7)):
        rho = np.array([[0.3, 0.2 - 0.1j], [0.2 + 0.1j, 0.7]])
        lhs = tcc.apply(tcc.amplitude_damping(a), tcc.apply(tcc.amplitude_damping(b), rho))
        rhs = tcc.apply(tcc.amplitude_damping(1 - (1 - a) * (1 - b)), rho)
        assert np.allclose(lhs, rhs, atol=1e-12)
    out["arc_length"] = kraus_arc_length()
    assert abs(out["arc_length"] - math.pi / 2) < 1e-3
    out["circuit_err"] = max(stinespring_circuit_check(g) for g in (0.1, 0.4, 0.9))
    assert out["circuit_err"] < 1e-12
    # output entropy for input |1> is h2(gamma)
    for g in (0.1, 0.3):
        s = vn_entropy(tcc.apply(tcc.amplitude_damping(g), np.diag([0, 1]).astype(complex)))
        assert abs(s - h2(g)) < 1e-12
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--eps-k", type=float, default=0.05, help="description precision for K proxies")
    ap.add_argument("--eps", type=float, default=0.05, help="CE-4 TV ball for d#_eps")
    ap.add_argument("--grid", type=int, default=11)
    ap.add_argument("--n-uses", default="1,10,100,1000")
    ap.add_argument("--dgamma", type=float, default=0.01)
    ap.add_argument("--table-step", type=float, default=0.05)
    args = ap.parse_args()
    ns = [int(v) for v in args.n_uses.split(",")]

    sc = self_checks()
    print("Self-checks passed:")
    print(f"  numeric (5-parameter two-pure-state Nelder-Mead) vs closed form: max |diff| = {sc['max_numeric_vs_closed']:.1e}")
    print(f"  C(1/2) = {sc['C_half']:.4f} (literature 0.4717, Giovannetti & Fazio 2005); C(0)=1, C(1)=0")
    print("  AD(a) o AD(b) = AD(1-(1-a)(1-b)) => C non-increasing in gamma (data processing)")
    print(f"  Kraus arc length of AD family = {sc['arc_length']:.6f} (pi/2 = {math.pi/2:.6f})")
    print(f"  Stinespring circuit (3 CNOT + 2 Ry) reproduces AD: max err {sc['circuit_err']:.1e}")
    print("  s = S(AD(|1><1|)) = h2(gamma)\n")

    ke = K_eps(args.eps_k)
    print(f"K_eps (eps_K = {args.eps_k}) = log2 ceil((pi/2)/eps_K) + log2 {N_FAMILIES} = {ke:.3f} bits (all gamma)")
    print(f"K_circ (eps_K = {args.eps_k}) = {K_circ(0.3, args.eps_k):.3f} bits for gamma > 0; 0 at gamma = 0")
    print("Both are crude upper-bound proxies, NOT Kolmogorov complexity.\n")

    gammas = np.round(np.arange(0.0, 1.0 + args.dgamma / 2, args.dgamma), 10)
    prim = tcc.CandidateSet("primary", 2, True, args.grid)
    rows_d = tcc.sweep(prim, gammas, args.eps)
    rows = []
    for g, rd in zip(gammas, rows_d):
        g = float(g)
        c, _ = holevo_capacity_closed(g)
        s = h2(g)
        rows.append({"g": g, "T": rd[2], "br": rd[3], "C": c, "d": rd[5], "cost": rd[6], "s": s,
                     "inv_s": (1 / s) if s > 0 else math.inf})

    nshow = ns[min(2, len(ns) - 1)]
    tstep = max(1, round(args.table_step / args.dgamma))
    print(f"## Table (K = K_eps = {ke:.2f} bits; amortized column uses n = {nshow}; d#_eps, cost from CE-4 primary set, eps = {args.eps})\n")
    print(f"| gamma | T | branch | C (bits/use) | K (bits) | C - K (n=1) | C - K/n (n={nshow}) | nC - K (n={nshow}) | d#_eps | cost = d# T ln2 | s = h2(gamma) | 1/s |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i in range(0, len(rows), tstep):
        r = rows[i]
        print(f"| {r['g']:.2f} | {tcc.fmt(r['T'])} | {r['br']} | {r['C']:.4f} | {ke:.2f} | {r['C'] - ke:.3f} | "
              f"{r['C'] - ke / nshow:.4f} | {nshow * r['C'] - ke:.2f} | {tcc.fmt(r['d'])} | {tcc.fmt(r['cost'])} | "
              f"{r['s']:.4f} | {tcc.fmt(r['inv_s'])} |")

    pos = [r for r in rows if r["br"] == "T>=0"]
    T = np.array([r["T"] for r in pos])
    C = np.array([r["C"] for r in pos])
    inv_s = np.array([r["inv_s"] for r in pos])
    print("\n## Trend on the T >= 0 branch (gamma in [0, 0.49])\n")
    print("| combination | value at T=0 | value at gamma=0.49 (T~25) | monotone in T | direction |")
    print("|---|---|---|---|---|")

    def trend(name, y):
        dif = np.diff(y)
        mono = "yes" if (np.all(dif <= 1e-12) or np.all(dif >= -1e-12)) else "no"
        direction = "falls" if y[-1] < y[0] else "rises"
        print(f"| {name} | {y[0]:.4f} | {y[-1]:.4f} | {mono} | {direction} |")
    trend("C (bits/use)", C)
    for n in ns:
        trend(f"C - K_eps/n, n={n} (bits/use)", C - ke / n)
    trend(f"nC - K_eps, n={nshow} (bits)", nshow * C - ke)
    kc = np.array([K_circ(r["g"], args.eps_k) for r in pos])
    trend(f"C - K_circ/n, n={nshow} (bits/use)", C - kc / nshow)
    trend("s = h2(gamma) (bits)", np.array([r["s"] for r in pos]))
    fin = np.isfinite(inv_s)
    print(f"| 1/s (finite part, gamma>0) | {inv_s[fin][0]:.4f} (gamma=0.01) | {inv_s[fin][-1]:.4f} | "
          f"{'yes' if np.all(np.diff(inv_s[fin]) <= 0) else 'no'} | {'falls' if inv_s[fin][-1] < inv_s[fin][0] else 'rises'} |")

    print("\nBreak-even n* = K/C (uses needed before nC - K > 0):")
    for gv in (0.0, 0.1, 0.25, 0.4, 0.49):
        c = holevo_capacity_closed(gv)[0]
        print(f"  gamma={gv:.2f} T={tcc.fmt(tcc.T_of_gamma(gv))}: C={c:.4f}, n* = {ke / c:.1f}")

    co = bool(np.all(np.diff(C) <= 1e-12))
    assert co, "C not non-increasing on T>=0 branch"
    print("\nVerdict on the T >= 0 branch: C is non-increasing in T, so for every fixed")
    print("combination above C_minus_K FALLS as T rises, in the same region where 1/s falls.")
    print("It does not rise with T. No physics claim is drawn from this toy.")
    print("Negative-T branch (gamma > 1/2): C computed for completeness, no T statement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
