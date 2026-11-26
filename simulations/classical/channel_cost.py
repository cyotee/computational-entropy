#!/usr/bin/env python3
"""Tier 2 toy model: channel-cost Stage 2 accounting test on the CE-6
one-bit failure points, for the Stage 1 definition, two alternates and two pools.

    *** TOY MODEL. One-qubit (and, for one f-dependence check, two-qubit)
    *** proof-of-concept. It is NOT evidence about hadronic or QCD physics and
    *** makes no physical claim. "Cost" is an entropy in bits; any kT ln 2
    *** pricing is a convention only.

Pure numpy. Imports procedural_share.py (GAD Kraus, input laws),
procedural_share_surface.py (two-qubit GAD Kraus) and procedural_share_mlpool.py
(ce6_overlap = the Stage 2 hook named in CHANNEL_COST_STAGE1.md section 7, and
the saved ML pool). Deterministic: no random numbers except a fixed-seed
self-check. Run:

    python simulations/classical/channel_cost.py            # self-checks + full report (~10 s)
    python simulations/classical/channel_cost.py --check    # self-checks only

DEFINITIONS (noise channel N alone; CHANNEL_COST_STAGE1.md sections 3-4)
  Complementary channel. For Kraus {K_k}, [N^c(rho)]_kl = Tr(K_k rho K_l^dag);
  S(N^c(rho)) is the entropy exchange S_e(rho, N) (dilation-independent).
  A0  map entropy            S(J(N)/2) = S(N^c(I/2)); GAD closed form of Stage 1 section 5.1.
  B'  entropy exchange at the actual input of the CE-6 run at that grid point:
      rho_bar = diag(pi_0, pi_1), pi = uniform or Blahut-Arimoto capacity law
      (procedural_share.input_law). Uniform input: B' = A0 exactly.
  C-  min output entropy of N^c over pure inputs (= global min, by concavity;
      equals the min output entropy of N since S(N(psi)) = S(N^c(psi))).
  C+  max output entropy of N^c over all (mixed) inputs.
  Skipped by decision: the bath's starting entropy h2(p) (Stage 1 candidate A).
  It is not the map entropy: h2(p) > 0 at g = 0, where the map entropy is 0.

OPTIMISATION (C-, C+). GAD is phase covariant: N(R rho R^dag) = R N(rho) R^dag
  for Z rotations R, so S(N^c(.)) is invariant under R (checked numerically on
  random phases). C-: pure inputs cos(t/2)|0> + sin(t/2)|1>, t in [0, pi]; grid of
  4001 points, then golden-section refinement in the best grid cell (60
  iterations). C+: by covariance and concavity the maximiser can be taken
  diagonal, diag(q, 1-q); S is concave in q, so golden section on [0, 1] (100
  iterations) finds the global max. Convergence: grid 1001 vs 4001 agree to
  < 1e-9 bits; C+ is checked against 2000 random mixed states (never exceeded).

MODEL ORDERING. In the CE-6 one-bit run the noise channel is GAD acting
  directly on the input |x> (the target law is gad_law(g, p); candidates are
  laws compared with it). No candidate map precedes the noise, so all four costs
  are f-INDEPENDENT at the failure points: they can only track the (g, p) part
  of the deficit, not its pool/f part. In the two-qubit surfaces (CE-9 to CE-12)
  U_f acts before the noise, so B' there depends on f; the report includes a
  per-block (2 uses, 4 qubit uses) range over the saved ML pool as a check.

UNITS. Bits. The deficit D = H(F|Y) - H(Y|X) of the CE-6 one-bit run is per
  symbol, and a symbol is ONE use of ONE qubit (USES = 1), so the block is one
  qubit use and every cost here is per qubit use = per block. Each cost is
  <= 2 bits (environment dimension <= 4).

PASS 4 (combinations). Unweighted sums B'+C-, B'+C+, A0+B', A0+C+, A0+B'+C+;
  least-squares fits w.x to D with w >= 0 (exact, by subset enumeration) on
  (B', C-), (B', C+), (A0, B', C-, C+), without intercept and, flagged
  separately, with an unconstrained intercept. Validation: fit on pool A,
  test on pool A-ml and vice versa; leave-one-damping-row-out within each
  pool. Variance split of D (both pools pooled) into within-(g, p)-cell and
  between-cell parts: 1 - within is the ceiling on R^2 for any channel-only cost.

TEST (CHANNEL_COST_STAGE1.md section 8). At each failure point (D > 0) the
  cost-augmented original form H(F|Y) <= H(Y|X) + cost holds iff cost >= D.
"""
from __future__ import annotations

import argparse
import functools
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedural_share as ps  # noqa: E402
import procedural_share_mlpool as mlp  # noqa: E402
import procedural_share_surface as pss  # noqa: E402

DEFS = ("A0", "Bp", "Cmin", "Cmax")
LABEL = {"A0": "A0 map entropy", "Bp": "B' entropy exchange", "Cmin": "C- min output", "Cmax": "C+ max output"}
GOLD = (math.sqrt(5) - 1) / 2


# ---------------------------------------------------------------------------
# Entropies of the complementary channel
# ---------------------------------------------------------------------------

def S(rho: np.ndarray) -> float:
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-15]
    return float(-(w * np.log2(w)).sum()) if w.size else 0.0


def comp_state(K: np.ndarray, rho: np.ndarray) -> np.ndarray:
    """[N^c(rho)]_kl = Tr(K_k rho K_l^dag)."""
    return np.einsum("kab,bc,lac->kl", K, rho, K.conj())


def map_entropy_numeric(K: np.ndarray) -> float:
    d = K.shape[1]
    J = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            Eij = np.zeros((d, d), dtype=complex)
            Eij[i, j] = 1
            J += np.kron(Eij, np.einsum("kab,bc,kdc->ad", K, Eij, K.conj()))
    return S(J / d)


def map_entropy_closed(g: float, p: float) -> float:
    a = 1 - g / 2
    s = math.sqrt(max(a * a - p * (1 - p) * g * g, 0.0))
    return ps.H([(a + s) / 2, (a - s) / 2, p * g / 2, (1 - p) * g / 2])


def entropy_exchange(K: np.ndarray, rho: np.ndarray) -> float:
    return S(comp_state(K, rho))


def _pure(t: float) -> np.ndarray:
    v = np.array([math.cos(t / 2), math.sin(t / 2)], dtype=complex)
    return np.outer(v, v.conj())


def _golden(f, lo, hi, iters, maximise=False):
    sgn = -1.0 if maximise else 1.0
    a, b = lo, hi
    c, d = b - GOLD * (b - a), a + GOLD * (b - a)
    fc, fd = sgn * f(c), sgn * f(d)
    for _ in range(iters):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - GOLD * (b - a)
            fc = sgn * f(c)
        else:
            a, c, fc = c, d, fd
            d = a + GOLD * (b - a)
            fd = sgn * f(d)
    x = (a + b) / 2
    return x, f(x)


def c_min(K: np.ndarray, grid: int = 4001) -> tuple[float, float]:
    """(min over pure inputs of S(N^c(psi)), Bloch polar angle of the minimiser)."""
    f = lambda t: entropy_exchange(K, _pure(t))  # noqa: E731
    ts = np.linspace(0, math.pi, grid)
    v = np.array([f(t) for t in ts])
    i = int(v.argmin())
    lo, hi = ts[max(i - 1, 0)], ts[min(i + 1, grid - 1)]
    t, val = _golden(f, lo, hi, 60)
    if v[i] < val:
        t, val = float(ts[i]), float(v[i])
    return val, t


def c_max(K: np.ndarray) -> tuple[float, float]:
    """(max over all inputs of S(N^c(rho)), q of the diagonal maximiser diag(q, 1-q))."""
    f = lambda q: entropy_exchange(K, np.diag([q, 1 - q]).astype(complex))  # noqa: E731
    q, val = _golden(f, 0.0, 1.0, 100, maximise=True)
    for q0 in (0.0, 0.5, 1.0):
        if f(q0) > val:
            q, val = q0, f(q0)
    return val, q


def costs(g: float, p: float, pi: np.ndarray) -> dict:
    K = np.array(ps.gad_kraus(g, p))
    return {"A0": map_entropy_closed(g, p),
            "Bp": entropy_exchange(K, np.diag(pi).astype(complex)),
            "Cmin": c_min(K)[0], "Cmax": c_max(K)[0]}


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks() -> list[str]:
    out = []
    rng = np.random.default_rng(7)
    err = 0.0
    for g in np.linspace(0, 1, 11):
        for p in np.linspace(0.5, 1, 11):
            K = np.array(ps.gad_kraus(float(g), float(p)))
            a = map_entropy_closed(float(g), float(p))
            err = max(err, abs(a - map_entropy_numeric(K)), abs(a - entropy_exchange(K, np.eye(2) / 2)))
    assert err < 1e-12, err
    out.append(f"A0 closed form = numeric S(J/2) = S(N^c(I/2)) on an 11x11 (g, p) grid (max diff {err:.1e})")
    for p in (0.5, 0.7311, 1.0):
        K0 = np.array(ps.gad_kraus(0.0, p))
        vals = [map_entropy_closed(0.0, p), c_min(K0)[0], c_max(K0)[0]]
        assert max(vals) < 1e-9, vals
        K1 = np.array(ps.gad_kraus(1.0, p))
        assert abs(c_min(K1)[0] - ps.h2(p)) < 1e-9 and abs(c_max(K1)[0] - (1 + ps.h2(p))) < 1e-9
        assert abs(map_entropy_closed(1.0, p) - (1 + ps.h2(p))) < 1e-12
    out.append("g=0 (identity): A0 = C- = C+ = 0 at p in {0.5, 0.7311, 1}; g=1 (replacement by diag(p,1-p)): "
               "C- = h2(p), C+ = A0 = 1 + h2(p)")
    for g in (0.3, 0.8):
        assert c_min(np.array(ps.gad_kraus(g, 1.0)))[0] < 1e-9
    out.append("plain AD (p=1): C- = 0 (|0> is a fixed pure state)")
    worst_cov = worst_max = worst_min = 0.0
    for g, p in ((0.3, 0.7), (0.6, 0.55), (0.9, 0.95)):
        K = np.array(ps.gad_kraus(g, p))
        cmx, cmn = c_max(K)[0], c_min(K)[0]
        for _ in range(500):
            v = rng.standard_normal(2) + 1j * rng.standard_normal(2)
            v /= np.linalg.norm(v)
            psi = np.outer(v, v.conj())
            ph = np.diag([1, np.exp(1j * rng.uniform(0, 2 * np.pi))])
            worst_cov = max(worst_cov, abs(entropy_exchange(K, psi) - entropy_exchange(K, ph @ psi @ ph.conj().T)))
            worst_min = max(worst_min, cmn - entropy_exchange(K, psi))
            A = rng.standard_normal((2, 2)) + 1j * rng.standard_normal((2, 2))
            rho = A @ A.conj().T
            rho /= np.trace(rho).real
            worst_max = max(worst_max, entropy_exchange(K, rho) - cmx)
        assert abs(c_min(K, 1001)[0] - cmn) < 1e-9
    assert worst_cov < 1e-12 and worst_max < 1e-12 and worst_min < 1e-12
    out.append(f"phase covariance of S(N^c) (max diff {worst_cov:.1e}); no random pure state below C- and no random "
               f"mixed state above C+ (1500 each); C- grid 1001 vs 4001 agree < 1e-9")
    return out


# ---------------------------------------------------------------------------
# Stage 2 accounting at the CE-6 failure points
# ---------------------------------------------------------------------------

def rankdata(x: np.ndarray) -> np.ndarray:
    """Average ranks; values equal to 12 decimals are ties (closed form vs numeric rounding)."""
    x = np.round(np.asarray(x, dtype=float), 12)
    order = np.argsort(x, kind="mergesort")
    r = np.empty(len(x))
    xs = x[order]
    i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and xs[j + 1] == xs[i]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return r


def corr(a: np.ndarray, b: np.ndarray) -> float:
    if np.ptp(a) < 1e-12 or np.ptp(b) < 1e-12:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


@functools.lru_cache(maxsize=None)
def ce6(pool_source: str) -> dict:
    return mlp.ce6_overlap(pool_source=pool_source)


def accounting(pool_source: str) -> dict:
    res = {}
    for inp, rows in ce6(pool_source).items():
        fails = []
        for r in rows:
            if r["deficit"] <= 1e-12:
                continue
            pi = ps.input_law(inp, r["g"], r["p"])
            fails.append(dict(g=r["g"], p=r["p"], D=r["deficit"], k=r["k"], **costs(r["g"], r["p"], pi)))
        res[inp] = fails
    return res


def summary(fails: list[dict]) -> dict:
    D = np.array([f["D"] for f in fails])
    out = {"n": len(D), "D": (D.min(), np.median(D), D.max())}
    for c in DEFS:
        v = np.array([f[c] for f in fails])
        r = D - v
        out[c] = dict(covers=int((v >= D - 1e-12).sum()), res=(r.min(), np.median(r), r.max()),
                      cost=(v.min(), np.median(v), v.max()), pearson=corr(v, D),
                      spearman=corr(rankdata(v), rankdata(D)))
    return out


def f_dependence_Bp(gs=(0.0, 0.2, 0.5, 0.8, 1.0), T=1.0) -> list[tuple]:
    """B' per 2-use block on the saved two-qubit ML pool, input U_f (I/2 (x) |0><0|) U_f^dag per use."""
    pool, _ = mlp.load_pool()
    p = ps.p_of_T(T)
    sig = mlp.ref_state("blind")
    rows = []
    for g in gs:
        K = np.array(pss.two_qubit_gad_kraus(g, p))
        v = np.array([2 * entropy_exchange(K, U @ sig @ U.conj().T) for U in pool])   # 2 uses, product input
        rows.append((g, v.min(), np.median(v), v.max(), 4 * map_entropy_closed(g, p)))
    return rows


# ---------------------------------------------------------------------------
# Pass 4: linear combinations of the costs (t23u). Fitted to D by least squares.
# ---------------------------------------------------------------------------

SUMS = (("Bp", "Cmin"), ("Bp", "Cmax"), ("A0", "Bp"), ("A0", "Cmax"), ("A0", "Bp", "Cmax"))
FITS = (("Bp", "Cmin"), ("Bp", "Cmax"), ("A0", "Bp", "Cmin", "Cmax"))


def nnls(X: np.ndarray, y: np.ndarray, free: int = 0) -> np.ndarray:
    """Exact least squares with w >= 0 on columns free.. (columns < free unconstrained), by subset enumeration."""
    n = X.shape[1]
    best, bw = math.inf, np.zeros(n)
    for mask in range(2 ** (n - free)):
        cols = list(range(free)) + [free + i for i in range(n - free) if mask >> i & 1]
        w = np.zeros(n)
        if cols:
            w[cols] = np.linalg.lstsq(X[:, cols], y, rcond=None)[0]
        if (w[free:] < -1e-12).any():
            continue
        r = float(((X @ w - y) ** 2).sum())
        if r < best - 1e-12:
            best, bw = r, np.clip(w, [-math.inf] * free + [0.0] * (n - free), None)
    return bw


def design(fails, feats, intercept):
    X = np.array([[f[c] for c in feats] for f in fails], dtype=float)
    return np.hstack([np.ones((len(fails), 1)), X]) if intercept else X


def metrics(D: np.ndarray, c: np.ndarray) -> dict:
    ss = float(((D - D.mean()) ** 2).sum())
    return dict(R2=1 - float(((D - c) ** 2).sum()) / ss, RMSE=math.sqrt(float(((D - c) ** 2).mean())),
                covers=int((c >= D - 1e-12).sum()), n=len(D), med=float(np.median(D - c)),
                rho=corr(rankdata(c), rankdata(D)))


def combo_eval(pools: dict, inp: str) -> list[tuple]:
    """Rows (model, evaluation, metrics, weights). pools = {name: accounting(...)}."""
    F = {k: v[inp] for k, v in pools.items()}
    D = {k: np.array([f["D"] for f in v]) for k, v in F.items()}
    names = list(F)
    out = []
    for feats in SUMS:
        lab = " + ".join(LABEL[c].split()[0] for c in feats)
        for k in names:
            out.append((lab, f"{k} (no fit)", metrics(D[k], design(F[k], feats, False).sum(axis=1)), None))
    for feats in FITS:
        for icpt in (False, True):
            lab = ("fit " if not icpt else "fit+intercept ") + ", ".join(LABEL[c].split()[0] for c in feats)
            fr = 1 if icpt else 0
            for k in names:
                w = nnls(design(F[k], feats, icpt), D[k], fr)
                out.append((lab, f"in-sample {k}", metrics(D[k], design(F[k], feats, icpt) @ w), w))
            for a, b in ((names[0], names[1]), (names[1], names[0])):
                w = nnls(design(F[a], feats, icpt), D[a], fr)
                out.append((lab, f"train {a} -> test {b}", metrics(D[b], design(F[b], feats, icpt) @ w), w))
            for k in names:
                pred = np.zeros(len(F[k]))
                gk = np.array([f["g"] for f in F[k]])
                for g in np.unique(gk):
                    tr, te = gk != g, gk == g
                    Xk = design(F[k], feats, icpt)
                    pred[te] = Xk[te] @ nnls(Xk[tr], D[k][tr], fr)
                out.append((lab, f"leave-one-g-row-out {k}", metrics(D[k], pred), None))
    return out


def variance_split(pools: dict, inp: str) -> dict:
    """Share of D's variance (both pools pooled) lying WITHIN (g, p) cells, i.e. across pools / f-sets.

    1 - within is an upper bound on the R^2 of ANY function of the channel parameters alone.
    """
    pts = [(f["g"], f["p"], f["D"]) for v in pools.values() for f in v[inp]]
    D = np.array([d for *_, d in pts])
    cells: dict = {}
    for g, p, d in pts:
        cells.setdefault((g, p), []).append(d)
    within = sum(((np.array(v) - np.mean(v)) ** 2).sum() for v in cells.values())
    tot = float(((D - D.mean()) ** 2).sum())
    shared = [v for v in cells.values() if len(v) > 1]
    # signed deficits at ALL defined points (failing or not) of cells defined in both pools
    A = {(r["g"], r["p"]): r["deficit"] for r in ce6("A")[inp]}
    M = {(r["g"], r["p"]): r["deficit"] for r in ce6("ml")[inp]}
    both = sorted(set(A) & set(M))
    Ds = np.array([A[c] for c in both] + [M[c] for c in both])
    ws = sum((A[c] - M[c]) ** 2 / 2 for c in both)
    fa = {c for c in A if A[c] > 1e-12}
    fm = {c for c in M if M[c] > 1e-12}
    return dict(n=len(D), cells=len(cells), shared=len(shared), within=within / tot,
                sgn_cells=len(both), sgn_within=ws / float(((Ds - Ds.mean()) ** 2).sum()),
                flip=len([c for c in both if (c in fa) != (c in fm)]),
                shared_absdiff=float(np.median([abs(v[0] - v[1]) for v in shared])) if shared else float("nan"),
                shared_maxdiff=float(max(abs(v[0] - v[1]) for v in shared)) if shared else float("nan"))


def report_combos(pools: dict) -> None:
    for inp in ("uniform", "capacity"):
        vs = variance_split(pools, inp)
        print(f"\n### Linear combinations, {inp} input\n")
        print(f"Variance of D over both pools ({vs['n']} failure points, {vs['cells']} (g, p) cells, {vs['shared']} cells "
              f"failing in both pools): {100 * vs['within']:.1f}% lies WITHIN cells (between pools at the same channel). "
              f"Upper bound on R^2 of any channel-only cost on the pooled set: {1 - vs['within']:.3f}. At shared cells "
              f"|D_A - D_A-ml| median {fmt(vs['shared_absdiff'])}, max {fmt(vs['shared_maxdiff'])} bits. Signed D at all "
              f"{vs['sgn_cells']} cells defined in both pools: {100 * vs['sgn_within']:.1f}% within cells (ceiling "
              f"{1 - vs['sgn_within']:.3f}); {vs['flip']} of these cells fail in one pool and hold in the other at the "
              f"SAME channel. In the CE-6 run D is a class-level number (one per cell per pool), so 'variation across f' "
              f"is variation across pools. Within one pool each cell has one point, so in-pool fits have no ceiling.\n")
        if inp == "uniform":
            print("(Uniform input: B' = A0 exactly, so B'+A0 = 2 A0 and fits with both are collinear; lstsq takes the "
                  "minimum-norm solution.)\n")
        print("| model | evaluation | R^2 | RMSE | covers | median D - cost | Spearman | weights |")
        print("|---|---|---|---|---|---|---|---|")
        for lab, ev, m, w in combo_eval(pools, inp):
            ws = "" if w is None else "(" + ", ".join(fmt(x) for x in w) + ")"
            print(f"| {lab} | {ev} | {fmt(m['R2'])} | {fmt(m['RMSE'])} | {m['covers']}/{m['n']} | {fmt(m['med'])} | "
                  f"{fmt(m['rho'])} | {ws} |")


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt(x, nd=3):
    if isinstance(x, float) and math.isnan(x):
        return "n/a"
    return f"{0.0 if abs(x) < 0.5 * 10 ** -nd else x:.{nd}f}"


def report(name: str, res: dict) -> None:
    for inp, fails in res.items():
        sm = summary(fails)
        d = sm["D"]
        print(f"\n### {name}, {inp} input: {sm['n']} failure points; D min / median / max = "
              f"{fmt(d[0])} / {fmt(d[1])} / {fmt(d[2])} bits\n")
        print("| definition | cost min / median / max | covers (cost >= D) | D - cost min / median / max "
              "| Pearson(cost, D) | Spearman(cost, D) |")
        print("|---|---|---|---|---|---|")
        for c in DEFS:
            s = sm[c]
            print(f"| {LABEL[c]} | {' / '.join(fmt(x) for x in s['cost'])} | {s['covers']}/{sm['n']} | "
                  f"{' / '.join(fmt(x) for x in s['res'])} | {fmt(s['pearson'])} | {fmt(s['spearman'])} |")
        if inp != "uniform":
            continue
        print(f"\nPer damping row ({name}, uniform input; means over the failing p values of the row):\n")
        print("| g | failures | mean D | mean A0 | mean B' | mean C- | mean C+ | max cost | min D |")
        print("|---|---|---|---|---|---|---|---|---|")
        for g in sorted({f["g"] for f in fails}):
            row = [f for f in fails if f["g"] == g]
            m = {c: np.mean([f[c] for f in row]) for c in ("D",) + DEFS}
            mx = max(max(f[c] for c in DEFS) for f in row)
            print(f"| {g:.2f} | {len(row)} | {fmt(m['D'])} | {fmt(m['A0'])} | {fmt(m['Bp'])} | {fmt(m['Cmin'])} | "
                  f"{fmt(m['Cmax'])} | {fmt(mx)} | {fmt(min(f['D'] for f in row))} |")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="self-checks only")
    args = ap.parse_args()
    print("TOY MODEL (Tier 2). One-qubit proof-of-concept; NOT evidence about hadronic or QCD physics;")
    print("no physical claim. Costs are entropies in bits.\n")
    for line in self_checks():
        print("check: " + line)
    if args.check:
        return 0
    print("\nAll four costs are f-independent at the CE-6 failure points (noise acts on |x> directly; no U_f).")
    print("Per block = per qubit use here (CE-6 one-bit run, USES = 1). Every cost is <= 2 bits.")
    pools = {}
    for src, name in (("ml", "pool A-ml"), ("A", "pool A")):
        print(f"\n## {name} (ce6_overlap(pool_source={src!r}), variant (a), eps = 0.05)")
        pools[name] = accounting(src)
        report(name, pools[name])
    print("\n## Pass 4: linear combinations (unweighted sums; least-squares fits to D with non-negative weights,")
    print("## no intercept; intercept fits FLAGGED separately; cross-pool and leave-one-g-row-out validation)")
    pools = {"A": pools["pool A"], "A-ml": pools["pool A-ml"]}
    report_combos(pools)
    print("\n## f-dependence check: B' per 2-use block on the saved two-qubit ML pool (200 candidates), GAD T=1")
    print("(input per use U_f (I/2 (x) |0><0|) U_f^dag; U_f before the noise, as in CE-9 to CE-12)\n")
    print("| g | B' block min | median | max | 4 x A0 (f-independent) |")
    print("|---|---|---|---|---|")
    for g, a, b, c, d in f_dependence_Bp():
        print(f"| {g:.1f} | {fmt(a)} | {fmt(b)} | {fmt(c)} | {fmt(d)} |")
    print("\nTOY MODEL: no physical claim.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
