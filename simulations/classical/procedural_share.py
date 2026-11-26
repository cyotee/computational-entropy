#!/usr/bin/env python3
"""Tier 2 toy model (proof-of-concept for the SHAPE of a curve): procedural share
H(F|Y) on the generalized amplitude damping (GAD) channel.

Pure numpy. Imports thermal_channel_cost.py (Kraus helpers). Run:

    python simulations/classical/procedural_share.py
    python simulations/classical/procedural_share.py --eps 0.1 --dg 0.02

This is NOT evidence about hadronic/QCD physics and makes no claim that noise
is optionality ("noise = pre-paid optionality" is Cyotee's conjecture).

MODEL (all choices are conventions of this toy, fixed here)
-----------------------------------------------------------
GAD channel (Nielsen & Chuang §8.3.5; Khatri, Sharma & Wilde, arXiv:1903.07747
with N = 1 - p):
  A0 = sqrt(p)[[1,0],[0,sqrt(1-g)]],   A1 = sqrt(p)[[0,sqrt g],[0,0]],
  A2 = sqrt(1-p)[[sqrt(1-g),0],[0,1]], A3 = sqrt(1-p)[[0,0],[sqrt g,0]],
  g in [0,1] damping; p = bath ground-state population = 1/(1+e^{-beta omega}),
  hbar omega = k_B = 1, so T = 1/ln(p/(1-p)); p in [1/2,1] <=> T >= 0
  (p=1: plain AD, T=0; p=1/2: T=inf). Checked: TP; fixed point diag(p,1-p);
  p=1 equals AD.
Classical interface: X in {0,1} encoded as |X>, output Y = Z-measurement.
  GAD law: P(Y=1|X=0) = (1-p) g,  P(Y=1|X=1) = 1 - p g.
Input law pi(X): (i) uniform; (ii) capacity-achieving for the induced binary
  channel X -> Y (Blahut-Arimoto; this is NOT the Holevo-optimal ensemble).
Candidate pools (fixed in code before any channel output is computed;
  no AD/GAD members, nothing parametrized by g or p). Each candidate c is
  reduced to its conditional law (q0, q1) = (P_c(Y=1|X=0), P_c(Y=1|X=1)).
  POOL A: Boolean f:{0,1}^n->{0,1}, n=1,2 (4+16), first argument = X, the other
    n-1 arguments independent uniform bits; fixed ops on |X> then Z-readout:
    I, X, Y, Z, H, S, full dephasing, Z-measurement, reset|0>, reset|1>;
    20 Haar-random unitaries (numpy default_rng seed 11).            -> 50
  POOL B (robustness): Boolean n=3 (256, two auxiliary uniform bits) plus 40
    random CPTP maps (random 2-qubit unitary on system+|0> ancilla, trace out;
    seed 23).                                                         -> 296
Variant (a) hard eps-class, single joint model:
  C_eps = {c : max_x TV(P_c(.|x), P_GAD(.|x)) <= eps}; F ~ uniform(C_eps);
  X ~ pi independent of F; Y | F,X ~ P_F(.|X). Every quantity (H(Y), I(X;Y),
  H(Y|X), H(F|Y), I(F;Y)) is computed in this one joint law.
Variant (b) full pool, likelihood posterior:
  F ~ uniform(pool); posterior P(F|y) ∝ P_F(y), P_F(y) = sum_x pi(x) P_F(y|x);
  y is drawn from the true GAD channel with input pi. Procedural share
  H_b(F|Y) := sum_y P_GAD(y) H(P(F|Y=y)) (a cross/mismatched conditional
  entropy; labelled). Semantic share and H(Y) are the GAD channel's.
Shares: semantic = I(X;Y); procedural = H(F|Y).
Inequality under test (VERIFIED, not assumed): I(X;Y) + H(F|Y) <= H(Y),
  equivalently H(F|Y) <= H(Y|X).
Correct statements reported separately: H(Y) = I(X;Y) + H(Y|X) (identity);
  in (a), since F is independent of X, I(X;Y) + I(F;Y) <= I(X,F;Y) <= H(Y).

OUTPUT ALPHABET (CE-7). --alphabet M (a power of 2; default 16) realizes M
  output symbols as k = log2 M independent uses of the channel: GAD^{(x)k} with a
  product Z readout, Y in {0,1}^k, X in {0,1}^k with i.i.d. input law (uniform,
  or the 1-use Blahut-Arimoto law on every use), and every candidate acting as
  F^{(x)k}. A single qubit read out with ANY POVM gives at most 1 bit of
  accessible information (Holevo), so a 16-outcome measurement on one qubit
  could not lift the 1-bit cap; independent uses can. --alphabet 2 (k = 1)
  reproduces the CE-6 run exactly.
"""

from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import thermal_channel_cost as tcc  # noqa: E402

TOL = 1e-12


# ---------------------------------------------------------------------------
# Information helpers
# ---------------------------------------------------------------------------

def H(p) -> float:
    p = np.asarray(p, float).ravel()
    p = p[p > 1e-300]
    return float(-np.sum(p * np.log2(p)))


def h2(x: float) -> float:
    return H([x, 1 - x])


# ---------------------------------------------------------------------------
# GAD channel
# ---------------------------------------------------------------------------

def gad_kraus(g: float, p: float) -> list[np.ndarray]:
    sp, sq = math.sqrt(p), math.sqrt(1 - p)
    return [sp * np.array([[1, 0], [0, math.sqrt(1 - g)]], dtype=complex),
            sp * np.array([[0, math.sqrt(g)], [0, 0]], dtype=complex),
            sq * np.array([[math.sqrt(1 - g), 0], [0, 1]], dtype=complex),
            sq * np.array([[0, 0], [math.sqrt(g), 0]], dtype=complex)]


def law_from_kraus(kraus) -> tuple[float, float]:
    out = []
    for x in (0, 1):
        rho = np.zeros((2, 2), dtype=complex)
        rho[x, x] = 1
        out.append(float(np.real(tcc.apply(kraus, rho)[1, 1])))
    return out[0], out[1]


def gad_law(g: float, p: float) -> tuple[float, float]:
    return (1 - p) * g, 1 - p * g


def p_of_T(T: float) -> float:
    if T == 0:
        return 1.0
    if math.isinf(T):
        return 0.5
    return 1 / (1 + math.exp(-1 / T))


def T_of_p(p: float) -> float:
    if p >= 1:
        return 0.0
    if p <= 0.5:
        return math.inf
    return 1 / math.log(p / (1 - p))


# ---------------------------------------------------------------------------
# Candidate pools (channel-independent; fixed before any channel is evaluated)
# ---------------------------------------------------------------------------

def _boolean_laws(n: int) -> list[tuple[str, float, float]]:
    out = []
    m = 2 ** n
    for idx in range(2 ** m):
        table = [(idx >> k) & 1 for k in range(m)]
        # input index = x * 2^(n-1) + aux; first argument is X
        half = m // 2
        q0 = sum(table[:half]) / half
        q1 = sum(table[half:]) / half
        out.append((f"bool{n}:{idx}", q0, q1))
    return out


def _haar_unitary(rng) -> np.ndarray:
    z = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))


def _random_cptp(rng) -> list[np.ndarray]:
    z = (rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    u = q * (np.diag(r) / np.abs(np.diag(r)))
    # system (first) x ancilla |0>; Kraus K_a = <a|_anc U |0>_anc
    u4 = u.reshape(2, 2, 2, 2)  # out_sys, out_anc, in_sys, in_anc
    return [u4[:, a, :, 0] for a in (0, 1)]


def fixed_ops() -> dict[str, list[np.ndarray]]:
    h = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    return {
        "I": tcc.unitary(np.eye(2)), "X": tcc.unitary([[0, 1], [1, 0]]),
        "Y": tcc.unitary([[0, -1j], [1j, 0]]), "Z": tcc.unitary([[1, 0], [0, -1]]),
        "H": tcc.unitary(h), "S": tcc.unitary([[1, 0], [0, 1j]]),
        "dephase": tcc.phase_damping(1.0), "measZ": tcc.measure(),
        "reset0": tcc.reset_to(0), "reset1": tcc.reset_to(1),
    }


def pool_A() -> list[tuple[str, float, float]]:
    pool = _boolean_laws(1) + _boolean_laws(2)
    pool += [(k, *law_from_kraus(v)) for k, v in fixed_ops().items()]
    rng = np.random.default_rng(11)
    pool += [(f"haar{i}", *law_from_kraus(tcc.unitary(_haar_unitary(rng)))) for i in range(20)]
    return pool


def pool_B() -> list[tuple[str, float, float]]:
    pool = _boolean_laws(3)
    rng = np.random.default_rng(23)
    pool += [(f"cptp{i}", *law_from_kraus(_random_cptp(rng))) for i in range(40)]
    return pool


# ---------------------------------------------------------------------------
# Input law
# ---------------------------------------------------------------------------

def blahut_arimoto(q0: float, q1: float, iters: int = 400) -> tuple[np.ndarray, float]:
    W = np.array([[1 - q0, q0], [1 - q1, q1]])
    r = np.array([0.5, 0.5])
    for _ in range(iters):
        py = r @ W
        with np.errstate(divide="ignore", invalid="ignore"):
            d = np.where(W > 0, W * np.log2(np.where(W > 0, W, 1) / np.where(py > 0, py, 1)), 0).sum(1)
        r = r * np.exp2(d)
        r = r / r.sum()
    py = r @ W
    cap = H(py) - sum(r[x] * H(W[x]) for x in (0, 1))
    return r, cap


def input_law(kind: str, g: float, p: float) -> np.ndarray:
    if kind == "uniform":
        return np.array([0.5, 0.5])
    return blahut_arimoto(*gad_law(g, p))[0]


# ---------------------------------------------------------------------------
# Variants
# ---------------------------------------------------------------------------

USES = 1  # channel uses per symbol; alphabet = 2**USES (set in main)
_TENSOR_CACHE: dict = {}


def kpow(m: np.ndarray, k: int) -> np.ndarray:
    """k-fold Kronecker power (vectors or matrices)."""
    out = m
    for _ in range(k - 1):
        out = np.kron(out, m)
    return out


def law_matrix(q0: float, q1: float) -> np.ndarray:
    return np.array([[1 - q0, q0], [1 - q1, q1]])


def pool_tensor(pool, k: int) -> np.ndarray:
    """N x 2^k x 2^k array of k-use conditional laws P_F(y|x) = prod_i P_F(y_i|x_i)."""
    key = (id(pool), k)
    if key not in _TENSOR_CACHE:
        _TENSOR_CACHE[key] = np.array([kpow(law_matrix(c[1], c[2]), k) for c in pool])
    return _TENSOR_CACHE[key]


def tv_max(c, Q) -> float:
    return max(abs(c[1] - Q[0]), abs(c[2] - Q[1]))


def variant_a(pool, g, p, eps, pi):
    if USES > 1:
        return variant_a_k(pool, g, p, eps, pi, USES)
    Q = gad_law(g, p)
    cls = [c for c in pool if tv_max(c, Q) <= eps + TOL]
    k = len(cls)
    if k == 0:
        return {"size": 0}
    q = np.array([[c[1], c[2]] for c in cls])  # k x 2 : P(Y=1|X=x)
    # joint P(f,x,y)
    pf = np.full(k, 1 / k)
    P = np.zeros((k, 2, 2))
    for x in (0, 1):
        P[:, x, 1] = pf * pi[x] * q[:, x]
        P[:, x, 0] = pf * pi[x] * (1 - q[:, x])
    Py = P.sum((0, 1))
    Pxy = P.sum(0)
    Pfy = P.sum(1)
    HY = H(Py)
    HYgX = H(Pxy) - H(pi)
    IXY = HY - HYgX
    HFgY = H(Pfy) - HY
    IFY = H(pf) - HFgY
    HXFY = H(P)
    IXF_Y = H(pi) + H(pf) + HY - HXFY  # I(X,F;Y) = H(XF) + H(Y) - H(XFY), X indep F
    return {"size": k, "HY": HY, "HYgX": HYgX, "IXY": IXY, "HFgY": HFgY, "IFY": IFY,
            "IXF_Y": IXF_Y, "logk": math.log2(k)}


def variant_b(pool, g, p, pi):
    if USES > 1:
        return variant_b_k(pool, g, p, pi, USES)
    q = np.array([[c[1], c[2]] for c in pool])
    n = len(pool)
    pfy1 = q @ pi                       # P_F(Y=1)
    lik = np.vstack([1 - pfy1, pfy1]).T  # n x 2
    Q = gad_law(g, p)
    py_true = np.array([1 - (pi[0] * Q[0] + pi[1] * Q[1]), pi[0] * Q[0] + pi[1] * Q[1]])
    hpost = []
    for y in (0, 1):
        w = lik[:, y]
        hpost.append(H(w / w.sum()) if w.sum() > 0 else math.log2(n))
    HFgY = float(py_true @ np.array(hpost))
    W = np.array([[1 - Q[0], Q[0]], [1 - Q[1], Q[1]]])
    HY = H(py_true)
    HYgX = float(sum(pi[x] * H(W[x]) for x in (0, 1)))
    return {"size": n, "HY": HY, "HYgX": HYgX, "IXY": HY - HYgX, "HFgY": HFgY,
            "logk": math.log2(n), "hpost": hpost}


def variant_a_k(pool, g, p, eps, pi, k):
    """Variant (a) over k independent uses (alphabet 2^k); same eps-class (1-use TV)."""
    Q = gad_law(g, p)
    idx = [i for i, c in enumerate(pool) if tv_max(c, Q) <= eps + TOL]
    n = len(idx)
    if n == 0:
        return {"size": 0}
    W = pool_tensor(pool, k)[idx]                      # n x X x Y
    pik = kpow(np.asarray(pi, float), k)
    P = (1.0 / n) * pik[None, :, None] * W              # joint P(f, x, y)
    Py, Pxy, Pfy = P.sum((0, 1)), P.sum(0), P.sum(1)
    HY = H(Py)
    HYgX = H(Pxy) - H(pik)
    HFgY = H(Pfy) - HY
    HXFY = H(P)
    pf_ent = math.log2(n)
    # Hamming-weight statistic of y (sufficient for F when X is unobserved and i.i.d.)
    wt = np.array([bin(y).count("1") for y in range(2 ** k)])
    Pfw = np.zeros((n, k + 1))
    for w in range(k + 1):
        Pfw[:, w] = Pfy[:, wt == w].sum(1)
    IFW = pf_ent + H(Pfw.sum(0)) - H(Pfw)
    return {"size": n, "HY": HY, "HYgX": HYgX, "IXY": HY - HYgX, "HFgY": HFgY,
            "IFY": pf_ent - HFgY, "IXF_Y": H(pik) + pf_ent + HY - HXFY, "logk": pf_ent,
            "HFgXY": HXFY - H(Pxy), "IFW": IFW}


def variant_b_k(pool, g, p, pi, k):
    """Variant (b) over k uses: full pool, uniform prior, likelihood posterior, y ~ GAD^{(x)k}."""
    W = pool_tensor(pool, k)
    n = len(pool)
    pik = kpow(np.asarray(pi, float), k)
    lik = np.einsum("x,fxy->fy", pik, W)                # P_F(y)
    Gk = kpow(law_matrix(*gad_law(g, p)), k)
    py_true = pik @ Gk
    tot = lik.sum(0)
    post = lik / np.where(tot > 0, tot, 1)
    with np.errstate(divide="ignore", invalid="ignore"):
        hpost = -np.sum(np.where(post > 0, post * np.log2(np.where(post > 0, post, 1)), 0), axis=0)
    hpost = np.where(tot > 0, hpost, math.log2(n))
    HFgY = float(py_true @ hpost)
    HY = H(py_true)
    HYgX = float(sum(pik[x] * H(Gk[x]) for x in range(2 ** k)))
    return {"size": n, "HY": HY, "HYgX": HYgX, "IXY": HY - HYgX, "HFgY": HFgY,
            "logk": math.log2(n), "hpost": list(hpost), "gain": math.log2(n) - HFgY}


def law_counts(pool, pi=None):
    """Distinct 1-use conditional laws, and distinct output marginals under input law pi."""
    cond: dict = {}
    marg: dict = {}
    pi = np.array([0.5, 0.5]) if pi is None else pi
    for _, q0, q1 in pool:
        kc = (round(q0, 9), round(q1, 9))
        cond[kc] = cond.get(kc, 0) + 1
        km = round(pi[0] * q0 + pi[1] * q1, 9)
        marg[km] = marg.get(km, 0) + 1
    return cond, marg


def floor_bits(counts: dict) -> float:
    """H(F | law label) for a uniform prior over the pool: sum_L (n_L/N) log2 n_L."""
    n = sum(counts.values())
    return sum(v / n * math.log2(v) for v in counts.values())


def self_checks_k(poolA, k) -> None:
    pi = np.array([0.5, 0.5])
    r = variant_a_k(poolA, 0.0, 1.0, 0.25, pi, k)
    assert abs(r["HY"] - (r["IXY"] + r["HYgX"])) < 1e-9
    assert r["IXY"] + r["IFY"] <= r["IXF_Y"] + 1e-9 <= r["HY"] + 2e-9
    assert abs(r["IFY"] - r["IFW"]) < 1e-9, "Hamming weight not sufficient?"
    assert r["IFY"] <= math.log2(k + 1) + 1e-9
    b = variant_b_k(poolA, 0.3, 0.8, pi, k)
    b1 = variant_b_k(poolA, 0.3, 0.8, pi, 1)
    assert abs(b["IXY"] - k * b1["IXY"]) < 1e-9  # memoryless GAD, product input
    # (b), uniform input: H(F|Y) depends on (g, p) only through the GAD output marginal
    # r = 1/2 - g(2p-1)/2;  (0.4, 1.0) and (0.8, 0.75) both give r = 0.3
    assert abs(variant_b_k(poolA, 0.4, 1.0, pi, k)["HFgY"] - variant_b_k(poolA, 0.8, 0.75, pi, k)["HFgY"]) < 1e-9
    # k = 1 general path agrees with the original CE-6 code path
    global USES
    saved, USES = USES, 1
    a1 = variant_a(poolA, 0.5, 1.0, 0.25, pi)
    USES = saved
    a1k = variant_a_k(poolA, 0.5, 1.0, 0.25, pi, 1)
    assert abs(a1["HFgY"] - a1k["HFgY"]) < 1e-9 and abs(a1["IXY"] - a1k["IXY"]) < 1e-9


# ---------------------------------------------------------------------------
# Noise / decoherence measures
# ---------------------------------------------------------------------------

def noise_measures(g, p):
    _, cap = blahut_arimoto(*gad_law(g, p))
    plus = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex)
    out = tcc.apply(gad_kraus(g, p), plus)
    purity_loss = 1 - float(np.real(np.trace(out @ out)))
    return {"one_minus_C": 1 - cap, "purity_loss": purity_loss,
            "coh_decay": 1 - math.sqrt(1 - g), "g": g}


# ---------------------------------------------------------------------------
# Shape analysis
# ---------------------------------------------------------------------------

def shape(x: np.ndarray, y: np.ndarray) -> dict:
    ok = ~np.isnan(y)
    x, y = x[ok], y[ok]
    if len(y) < 4:
        return {"n": len(y)}
    dy = np.diff(y)
    rng_y = float(y.max() - y.min())
    tol = 1e-9 + 1e-6 * rng_y
    mono = "non-decreasing" if np.all(dy >= -tol) else ("non-increasing" if np.all(dy <= tol) else "non-monotone")
    d2 = []
    for i in range(1, len(x) - 1):
        h1, h2_ = x[i] - x[i - 1], x[i + 1] - x[i]
        d2.append(2 * (h1 * y[i + 1] - (h1 + h2_) * y[i] + h2_ * y[i - 1]) / (h1 * h2_ * (h1 + h2_)))
    d2 = np.array(d2)
    t2 = 1e-6 * max(1e-3, rng_y) / max(1e-12, (x[-1] - x[0]) ** 2)
    neg, pos = int(np.sum(d2 < -t2)), int(np.sum(d2 > t2))
    zero = len(d2) - neg - pos
    flat_steps = int(np.sum(np.abs(dy) <= tol))
    # saturation: first x after which y stays within 2% of range of its final value
    sat = None
    if rng_y > 0:
        band = 0.02 * rng_y
        for i in range(len(y)):
            if np.all(np.abs(y[i:] - y[-1]) <= band):
                sat = float(x[i])
                break
    return {"n": len(y), "mono": mono, "d2_neg": neg, "d2_pos": pos, "d2_zero": zero,
            "flat_steps": flat_steps, "range": rng_y, "y0": float(y[0]), "y_end": float(y[-1]),
            "y_max": float(y.max()), "y_min": float(y.min()),
            "sat_x": sat if rng_y >= FLAT_BITS else None}


FLAT_BITS = 0.01


def shape_label(s: dict) -> str:
    if s.get("n", 0) < 4:
        return "too few points"
    if s["range"] < 1e-9:
        return "constant"
    if s["range"] < FLAT_BITS:
        return f"flat (total range {s['range']:.4f} bit < {FLAT_BITS} bit; curvature not meaningful)"
    parts = [s["mono"]]
    if s["d2_pos"] == 0 and s["d2_neg"] > 0:
        parts.append("concave")
    elif s["d2_neg"] == 0 and s["d2_pos"] > 0:
        parts.append("convex")
    elif s["d2_neg"] == 0 and s["d2_pos"] == 0:
        parts.append("linear")
    else:
        parts.append(f"mixed curvature ({s['d2_neg']} concave / {s['d2_pos']} convex interior pts)")
    if s["flat_steps"] >= max(2, s["n"] // 4) and s["d2_pos"] > 0 and s["d2_neg"] > 0:
        parts.append("STEP ARTIFACT (piecewise constant)")
    return ", ".join(parts)


def spearman(a, b) -> float:
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = ~(np.isnan(a) | np.isnan(b))
    a, b = a[ok], b[ok]
    if len(a) < 3 or np.ptp(a) < 1e-9 or np.ptp(b) < 1e-9:
        return math.nan

    def rank(v):
        order = np.argsort(v, kind="mergesort")
        r = np.empty(len(v))
        r[order] = np.arange(len(v))
        for val in np.unique(v):  # average ties
            m = v == val
            r[m] = r[m].mean()
        return r
    return float(np.corrcoef(rank(a), rank(b))[0, 1])


def pearson(a, b) -> float:
    a, b = np.asarray(a, float), np.asarray(b, float)
    ok = ~(np.isnan(a) | np.isnan(b))
    a, b = a[ok], b[ok]
    if len(a) < 3 or np.ptp(a) < 1e-9 or np.ptp(b) < 1e-9:
        return math.nan
    return float(np.corrcoef(a, b)[0, 1])


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks(poolA, poolB) -> None:
    for g in (0.0, 0.3, 1.0):
        for p in (0.5, 0.8, 1.0):
            k = gad_kraus(g, p)
            tcc._check_tp(k)
            assert np.allclose(law_from_kraus(k), gad_law(g, p), atol=1e-12)
    # fixed point diag(p, 1-p) for g > 0
    for g, p in ((0.3, 0.8), (0.9, 0.6)):
        fp = np.diag([p, 1 - p]).astype(complex)
        assert np.allclose(tcc.apply(gad_kraus(g, p), fp), fp, atol=1e-12)
    # p = 1 reduces to amplitude damping
    rho = np.array([[0.3, 0.2 - 0.1j], [0.2 + 0.1j, 0.7]])
    assert np.allclose(tcc.apply(gad_kraus(0.4, 1.0), rho), tcc.apply(tcc.amplitude_damping(0.4), rho))
    # thermal map round trip
    for T in (0.2, 1.0, 7.0):
        assert abs(T_of_p(p_of_T(T)) - T) < 1e-9
    assert len(poolA) == 50 and len(poolB) == 296
    # pools contain no AD/GAD member names
    assert not any(n.startswith(("AD", "GAD")) for n, _, _ in poolA + poolB)
    # variant (a): identities
    pi = np.array([0.5, 0.5])
    r = variant_a(poolA, 0.5, 1.0, 0.25, pi)
    assert abs(r["HY"] - (r["IXY"] + r["HYgX"])) < 1e-12
    assert r["IXY"] + r["IFY"] <= r["IXF_Y"] + 1e-12 <= r["HY"] + 2e-12


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def fmt(v, nd=3):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "-"
    if isinstance(v, float) and math.isinf(v):
        return "inf"
    if abs(v) < 0.5 * 10 ** (-nd):
        v = 0.0
    return f"{v:.{nd}f}"


def print_bottleneck(pA, pB, k, gs, ps, eps) -> None:
    print(f"\n## Identifiability bottleneck and alphabet estimate (k = {k} uses)\n")
    print("With X unobserved and i.i.d., P_F(y) = prod_i r_F(y_i), r_F(1) = pi0 q0 + pi1 q1: Y enters only")
    print("through its Hamming weight W, so I(F;Y) = I(F;W) <= log2(k+1), and candidates with equal r_F")
    print("are indistinguishable from Y for every k: H(F|Y) >= floor = sum_L (n_L/N) log2 n_L.")
    print("Given X as well, F enters through the (x_i, y_i) type counts; the floor uses conditional laws.\n")
    print("| pool | N | log2 N | distinct cond. laws | distinct output marginals (uniform pi) | floor H(F\\|marginal) | floor H(F\\|cond. law) | max I(F;Y) any k = log2N - floor | cap now log2(k+1) | min gap between marginals |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    est = {}
    for pn, pool in (("A", pA), ("B", pB)):
        cond, marg = law_counts(pool)
        n = len(pool)
        fm, fc = floor_bits(marg), floor_bits(cond)
        mv = sorted(marg)
        gap = min(b - a for a, b in zip(mv, mv[1:])) if len(mv) > 1 else math.nan
        est[pn] = (len(marg), gap, math.log2(n) - fm)
        print(f"| {pn} | {n} | {math.log2(n):.3f} | {len(cond)} | {len(marg)} | {fm:.3f} | {fc:.3f} | "
              f"{math.log2(n) - fm:.3f} | {math.log2(k + 1):.3f} | {gap:.4f} |")
    print("\nEstimate (NOT run). Merge output marginals closer than a resolution delta; separating the")
    print("rest needs about k ~ ln(M)/gap^2 uses (gap = closest merged pair, >= delta; Chernoff-type")
    print("rule of thumb, order of magnitude only), and at least k+1 >= M weight values.")
    print("Ceiling at that resolution = log2 N - floor(merged).")
    print("Cost: with the weight statistic ~ N (k+1) per grid point; naive tensor ~ N 4^k per point.\n")
    print("| pool | delta | merged marginals M | k needed | alphabet 2^k | I(F;Y) ceiling at delta (bits) | weight-statistic cost per 231-pt sweep | naive tensor cost per sweep |")
    print("|---|---|---|---|---|---|---|---|")
    for pn, pool in (("A", pA), ("B", pB)):
        _, marg = law_counts(pool)
        n = len(pool)
        for delta in (0.05, 0.01):
            groups: list[list[float]] = []
            for v in sorted(marg):
                if groups and v - groups[-1][0] < delta:
                    groups[-1].append(v)
                else:
                    groups.append([v])
            merged = {tuple(gv): sum(marg[v] for v in gv) for gv in groups}
            m = len(merged)
            reps = [gv[0] for gv in groups]
            gap_m = min((b - a for a, b in zip(reps, reps[1:])), default=1.0)
            k_need = max(m - 1, math.ceil(math.log(max(m, 2)) / gap_m ** 2))
            ceil_bits = math.log2(n) - floor_bits(merged)
            npts = len(gs) * len(ps)
            w_ops = n * (k_need + 1) * npts
            naive_log10 = math.log10(n * npts) + k_need * math.log10(4)
            print(f"| {pn} | {delta} | {m} | {k_need} | 2^{k_need} | {ceil_bits:.2f} | ~{w_ops:.1e} ops ({'< 1 s' if w_ops < 1e8 else 'seconds'}) | ~10^{naive_log10:.0f} ops ({'infeasible' if naive_log10 > 12 else 'feasible'}) |")
    print("\nNo alphabet size lifts I(F;Y) above log2 N - floor: candidates with the same output law stay")
    print("indistinguishable. The bottleneck is the pool's distinct laws, not the alphabet.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--eps", type=float, default=0.05)
    ap.add_argument("--dg", type=float, default=0.05, help="g grid step")
    ap.add_argument("--dp", type=float, default=0.05, help="p grid step (2D grid)")
    ap.add_argument("--alphabet", type=int, default=16,
                    help="output alphabet size, a power of 2, realized as log2(M) channel uses (2 = CE-6 run)")
    args = ap.parse_args()
    k = int(round(math.log2(args.alphabet)))
    if k < 1 or 2 ** k != args.alphabet:
        ap.error("--alphabet must be a power of 2 (>= 2)")

    pA, pB = pool_A(), pool_B()
    self_checks(pA, pB)
    global USES
    USES = k
    print("Self-checks passed: GAD TP; law (1-p)g, 1-pg; fixed point diag(p,1-p); p=1 is AD;")
    print("T<->p round trip; pools fixed (A=50, B=296), no AD/GAD members;")
    print("H(Y)=I(X;Y)+H(Y|X) and I(X;Y)+I(F;Y) <= I(XF;Y) <= H(Y) in variant (a).\n")
    print(f"log2|pool A| = {math.log2(len(pA)):.3f}; log2|pool B| = {math.log2(len(pB)):.3f}")
    distinctA = len({(round(a, 9), round(b, 9)) for _, a, b in pA})
    distinctB = len({(round(a, 9), round(b, 9)) for _, a, b in pB})
    print(f"distinct conditional laws: pool A {distinctA}, pool B {distinctB}\n")
    if k > 1:
        self_checks_k(pA, k)
        print(f"OUTPUT ALPHABET {args.alphabet} = {k} independent uses of GAD, product Z readout, Y in {{0,1}}^{k};")
        print(f"candidates act as F^(x){k}; i.i.d. input law; I(X;Y) and H(Y) below are per {k} uses unless marked.")
        print("(One qubit with any POVM carries at most 1 bit (Holevo); a 16-outcome POVM on one qubit would not help.)")
        print(f"Extra self-checks passed (k={k}): identity, corrected bound, Hamming weight of y sufficient for F")
        print(f"(I(F;Y) = I(F;W) <= log2(k+1)), GAD I(X;Y) = k x 1-use value; k=1 general path = CE-6 path.\n")

    gs = np.round(np.arange(0, 1 + args.dg / 2, args.dg), 10)
    ps = np.round(np.arange(1.0, 0.5 - args.dp / 2, -args.dp), 10)
    pools = {"A": pA, "B": pB}

    # ---- 2D grid: inequality check (all variants, pools, input laws, eps) ----
    print("## Inequality I(X;Y) + H(F|Y) <= H(Y)  (equivalently H(F|Y) <= H(Y|X)), every grid point\n")
    print(f"Grid: g step {args.dg} on [0,1] x p step {args.dp} on [1/2,1] ({len(gs)}x{len(ps)} points).\n")
    print("| variant | pool | input | eps | defined pts | holds | fails | fails when log2\\|class\\| > H(Y)+H(Y\\|X) (sufficient) | max violation (bits) | I(X;Y)+I(F;Y) <= H(Y) holds |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    eps_list = sorted({0.02, 0.05, 0.1, args.eps})
    for pn, pool in pools.items():
        for inp in ("uniform", "capacity"):
            for eps in eps_list:
                tot = holds = fails = suff = 0
                worst = 0.0
                corr_ok = True
                for g in gs:
                    for p in ps:
                        pi = input_law(inp, float(g), float(p))
                        r = variant_a(pool, float(g), float(p), eps, pi)
                        if r["size"] == 0:
                            continue
                        tot += 1
                        v = r["IXY"] + r["HFgY"] - r["HY"]
                        if v <= 1e-12:
                            holds += 1
                        else:
                            fails += 1
                            worst = max(worst, v)
                            if r["logk"] > r["HY"] + r["HYgX"] + 1e-12:
                                suff += 1
                        corr_ok &= r["IXY"] + r["IFY"] <= r["HY"] + 1e-12
                print(f"| (a) eps-class | {pn} | {inp} | {eps} | {tot} | {holds} | {fails} | {suff} | {worst:.3f} | {'yes' if corr_ok else 'NO'} |")
            tot = holds = fails = 0
            worst = 0.0
            for g in gs:
                for p in ps:
                    pi = input_law(inp, float(g), float(p))
                    r = variant_b(pool, float(g), float(p), pi)
                    tot += 1
                    v = r["IXY"] + r["HFgY"] - r["HY"]
                    if v <= 1e-12:
                        holds += 1
                    else:
                        fails += 1
                        worst = max(worst, v)
            print(f"| (b) full pool | {pn} | {inp} | - | {tot} | {holds} | {fails} | - | {worst:.3f} | n/a |")

    # ---- 1D slices: procedural share vs g at several T ----
    T_list = [0.0, 0.5, 1.0, 2.0, math.inf]
    print(f"\n## Slices vs g (pool A, uniform input, eps = {args.eps}); columns per T: |class|, H(F|Y) (a), H(F|Y) (b), I(X;Y), H(Y)\n")
    hdr = "| g | " + " | ".join(f"T={fmt(T, 1)}: \\|C\\|, a, b, I, H(Y)" for T in T_list) + " |"
    print(hdr)
    print("|---|" + "---|" * len(T_list))
    for g in np.round(np.arange(0, 1.0001, 0.1), 10):
        cells = []
        for T in T_list:
            p = p_of_T(T)
            pi = input_law("uniform", g, p)
            a = variant_a(pA, g, p, args.eps, pi)
            b = variant_b(pA, g, p, pi)
            cells.append(f"{a['size']}, {fmt(a.get('HFgY', math.nan), 2)}, {fmt(b['HFgY'], 2)}, {fmt(b['IXY'], 2)}, {fmt(b['HY'], 2)}")
        print(f"| {g:.1f} | " + " | ".join(cells) + " |")

    # ---- 1D slices: vs T at several g ----
    print(f"\n## Slices vs T (pool A, uniform input, eps = {args.eps}): |class|, H(F|Y) (a), H(F|Y) (b), I(X;Y)\n")
    g_list = [0.25, 0.5, 0.75, 1.0]
    print("| p | T | " + " | ".join(f"g={g}" for g in g_list) + " |")
    print("|---|---|" + "---|" * len(g_list))
    for p in np.round(np.arange(1.0, 0.4999, -0.05), 10):
        cells = []
        for g in g_list:
            pi = input_law("uniform", g, p)
            a = variant_a(pA, g, p, args.eps, pi)
            b = variant_b(pA, g, p, pi)
            cells.append(f"{a['size']}, {fmt(a.get('HFgY', math.nan), 2)}, {fmt(b['HFgY'], 2)}, {fmt(b['IXY'], 2)}")
        print(f"| {p:.2f} | {fmt(T_of_p(p), 3)} | " + " | ".join(cells) + " |")

    if USES > 1:
        print(f"\n## {USES}-use detail (uniform input, eps = {args.eps}): |C|, H(F|Y) (a), I(F;Y) (a), "
              "H(F|X,Y) (a), H(F|Y) (b), log2N - H(F|Y) (b), I(X;Y) per use (GAD), H(Y) (GAD, k uses)\n")
        for pn, pool in (("A", pA), ("B", pB)):
            print(f"Pool {pn} (log2 N = {math.log2(len(pool)):.3f}):\n")
            print("| g | " + " | ".join(f"T={fmt(T, 1)}" for T in (0.0, 1.0, math.inf)) + " |")
            print("|---|---|---|---|")
            for g in np.round(np.arange(0, 1.0001, 0.1), 10):
                cells = []
                for T in (0.0, 1.0, math.inf):
                    pp = p_of_T(T)
                    pi = input_law("uniform", g, pp)
                    a = variant_a(pool, g, pp, args.eps, pi)
                    b = variant_b(pool, g, pp, pi)
                    cells.append(f"{a['size']}, {fmt(a.get('HFgY', math.nan), 2)}, {fmt(a.get('IFY', math.nan), 2)}, "
                                 f"{fmt(a.get('HFgXY', math.nan), 2)}, {fmt(b['HFgY'], 3)}, {fmt(b['gain'], 3)}, "
                                 f"{fmt(b['IXY'] / USES, 3)}, {fmt(b['HY'], 2)}")
                print(f"| {g:.1f} | " + " | ".join(cells) + " |")
            print()

    # ---- shape analysis ----
    print("\n## Shape of H(F|Y) along 1D slices (prediction: monotone, concave, saturating)\n")
    print("Interior discrete 2nd derivative signs; saturation = first point after which the curve stays")
    print("within 2% of its range of the end value ('-' = none before the end).\n")
    tally: dict[str, int] = {}
    print("| variant | pool | input | eps | grid | slice | shape | start → end (min..max) | saturates at | plateau vs log2\\|pool\\| |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    fine = np.round(np.arange(0, 1 + 0.01 / 2, 0.01), 10)
    for pn, pool in pools.items():
        lp = math.log2(len(pool))
        for inp in ("uniform", "capacity"):
            for eps in eps_list:
                for grid_name, gg in (("dg=%.2f" % args.dg, gs), ("dg=0.01", fine)):
                    for T in (0.0, 1.0, math.inf):
                        p = p_of_T(T)
                        ya = np.array([variant_a(pool, float(g), p, eps, input_law(inp, float(g), p)).get("HFgY", math.nan) for g in gg])
                        s = shape(gg, ya)
                        lab = shape_label(s)
                        key = ("(a) concave & monotone" if ("concave" in lab and "mixed" not in lab and "non-monotone" not in lab)
                               else "(a) step artifact" if "STEP" in lab else "(a) undefined (empty classes)" if s.get("n", 0) < 4
                               else "(a) other")
                        tally[key] = tally.get(key, 0) + 1
                        if s.get("n", 0) < 4:
                            print(f"| (a) | {pn} | {inp} | {eps} | {grid_name} | vs g, T={fmt(T,1)} | {shape_label(s)} | - | - | - |")
                            continue
                        print(f"| (a) | {pn} | {inp} | {eps} | {grid_name} | vs g, T={fmt(T,1)} | {shape_label(s)} | "
                              f"{s['y0']:.2f} → {s['y_end']:.2f} ({s['y_min']:.2f}..{s['y_max']:.2f}) | {fmt(s['sat_x'], 2)} | {s['y_max'] / lp:.2f} of {lp:.2f} |")
            for T in (0.0, 1.0, math.inf):
                p = p_of_T(T)
                yb = np.array([variant_b(pool, float(g), p, input_law(inp, float(g), p))["HFgY"] for g in fine])
                s = shape(fine, yb)
                lab = shape_label(s)
                key = "(b) constant/flat" if ("constant" in lab or "flat" in lab) else ("(b) concave & monotone" if ("concave" in lab and "mixed" not in lab and "non-monotone" not in lab) else "(b) other")
                tally[key] = tally.get(key, 0) + 1
                print(f"| (b) | {pn} | {inp} | - | dg=0.01 | vs g, T={fmt(T,1)} | {shape_label(s)} | "
                      f"{s['y0']:.3f} → {s['y_end']:.3f} ({s['y_min']:.3f}..{s['y_max']:.3f}) | {fmt(s['sat_x'], 2)} | {s['y_max'] / lp:.3f} of {lp:.2f} |")
            for g in (0.5, 1.0):
                pp = np.round(np.arange(1.0, 0.5 - 0.005, -0.01), 10)
                Ts = np.array([T_of_p(float(p)) for p in pp])
                fin = np.isfinite(Ts)
                yb = np.array([variant_b(pool, g, float(p), input_law(inp, g, float(p)))["HFgY"] for p in pp])
                s = shape(Ts[fin], yb[fin])
                lab = shape_label(s)
                key = "(b) constant/flat" if ("constant" in lab or "flat" in lab) else ("(b) concave & monotone" if ("concave" in lab and "mixed" not in lab and "non-monotone" not in lab) else "(b) other")
                tally[key] = tally.get(key, 0) + 1
                print(f"| (b) | {pn} | {inp} | - | dp=0.01 | vs T, g={g} | {shape_label(s)} | "
                      f"{s['y0']:.3f} → {s['y_end']:.3f} ({s['y_min']:.3f}..{s['y_max']:.3f}) | {fmt(s['sat_x'], 2)} | {s['y_max'] / lp:.3f} of {lp:.2f} |")

    print("\nShape tally over all slices above: " + "; ".join(f"{k}: {v}" for k, v in sorted(tally.items())))

    # ---- correlations: branching width vs noise amplitude ----
    print(f"\n## Correlation over the 2D grid (uniform input, eps = {args.eps}): Spearman (Pearson)\n")
    print("| variant | pool | vs log2\\|class\\| | vs \\|class\\| | vs 1 - C_bin | vs purity loss (\\|+>) | vs 1 - sqrt(1-g) | vs g |")
    print("|---|---|---|---|---|---|---|---|")
    for pn, pool in pools.items():
        rows_a, rows_b = [], []
        for g in gs:
            for p in ps:
                pi = input_law("uniform", float(g), float(p))
                a = variant_a(pool, float(g), float(p), args.eps, pi)
                b = variant_b(pool, float(g), float(p), pi)
                nm = noise_measures(float(g), float(p))
                rows_a.append((a.get("HFgY", math.nan), a.get("logk", math.nan), a["size"] if a["size"] else math.nan,
                               nm["one_minus_C"], nm["purity_loss"], nm["coh_decay"], nm["g"]))
                rows_b.append((b["HFgY"], nm["one_minus_C"], nm["purity_loss"], nm["coh_decay"], nm["g"]))
        A = np.array(rows_a)
        cells = [f"{spearman(A[:, 0], A[:, j]):.2f} ({pearson(A[:, 0], A[:, j]):.2f})" for j in range(1, 7)]
        print(f"| (a) | {pn} | " + " | ".join(cells) + " |")
        B = np.array(rows_b)
        if np.ptp(B[:, 0]) < FLAT_BITS:
            print(f"| (b) | {pn} | n/a (fixed pool) | n/a | H(F\\|Y) range {np.ptp(B[:, 0]):.2e} bit: correlations not meaningful | | | |")
            continue
        cells = [f"n/a (fixed pool; H(F\\|Y) range {np.ptp(B[:, 0]):.4f} bit)", "n/a"] + [f"{spearman(B[:, 0], B[:, j]):.2f} ({pearson(B[:, 0], B[:, j]):.2f})" for j in range(1, 5)]
        print(f"| (b) | {pn} | " + " | ".join(cells) + " |")

    if USES > 1:
        print("\nVariant (b), uniform input: H(F|Y) is a function of the GAD output bias b = |r - 1/2| = g(2p-1)/2")
        print("alone (self-checked). Spearman of H(F|Y) (b) vs b over the 2D grid:")
        for pn, pool in pools.items():
            yb, bias = [], []
            for g in gs:
                for p in ps:
                    yb.append(variant_b(pool, float(g), float(p), np.array([0.5, 0.5]))["HFgY"])
                    bias.append(float(g) * (2 * float(p) - 1) / 2)
            print(f"  pool {pn}: {spearman(yb, bias):.3f} (Pearson {pearson(yb, bias):.3f})")
        print_bottleneck(pA, pB, USES, gs, ps, args.eps)
        print("No physics claim is drawn from this toy.")
        return 0

    # ---- analytic notes ----
    hp = variant_b(pA, 0.3, 0.8, np.array([0.5, 0.5]))["hpost"]
    print("\nAnalytic notes (printed for the record):")
    print("* Inequality <=> H(F|Y) <= H(Y|X). In (a), F is independent of X and I(F;Y) <= H(Y), so")
    print("  H(F|Y) >= log2|C| - H(Y); it must fail whenever log2|C| > H(Y) + H(Y|X) (at most 2 bits, so")
    print("  any class with more than 4 members). In (b), H(F|Y) >= log2|pool| - H(Y) >= log2|pool| - 1.")
    print(f"* (b) with uniform input: H(F|Y) = sum_y P_GAD(y) h_y with pool constants h_0, h_1 "
          f"(pool A: {hp[0]:.4f}, {hp[1]:.4f}); P_GAD(Y=1) = 1/2 - g(2p-1)/2 is linear in g, so H(F|Y)")
    print("  is exactly LINEAR in g at fixed T (curvature 0), and varies by at most |h_0 - h_1|.")
    print("* (a) H(F|Y) = log2|C| - I(F;Y) with 0 <= I(F;Y) <= H(Y) <= 1 bit, so its correlation with")
    print("  log2|C| is built in by the definition; it is not an independent test of 'branching width'.")
    print("* (a) sparsity: the GAD law moves continuously in (q0,q1) while the pool's laws are fixed")
    print("  points, so C_eps is empty at many grid points and H(F|Y) is undefined there.")
    print("No physics claim is drawn from this toy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
