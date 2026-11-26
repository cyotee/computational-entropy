#!/usr/bin/env python3
"""Tier 2 toy model (proof-of-concept): an ENERGY-BOUNDED (Margolus-Levitin)
candidate pool for the procedural-share surface, compared with the Haar pool
of CE-9, plus the overlap term I(X;F|Y) in the corrected bound.

    *** TOY MODEL. Proof-of-concept for the shape of a curve in a two-qubit
    *** toy. It is NOT evidence about hadronic or QCD physics and makes no
    *** physical claim of any kind. "Energy budget" and "Margolus-Levitin
    *** time" are used in their textbook finite-dimensional sense only.

Pure numpy. Imports procedural_share_surface.py (GAD Kraus, nested readout,
random readout bases, Haar pools), procedural_share_informed.py (inputs,
statistics) and procedural_share.py (the CE-6 one-bit run for the "58").
Run:

    python simulations/classical/procedural_share_mlpool.py                 # defaults (~1-3 min)
    python simulations/classical/procedural_share_mlpool.py --eps 0.1 --n-samples 500
    python simulations/classical/procedural_share_mlpool.py --channel gad --T 0 --seeds 20
    python simulations/classical/procedural_share_mlpool.py --markdown

MODEL (conventions of this toy, fixed here)
-------------------------------------------
Hamiltonian sampling. H = (A + A^dag)/2, A a 4x4 complex Ginibre matrix
  (GUE). Spectrum shifted so the ground energy E0 = 0, then rescaled so that
  the mean energy above the ground state in a REFERENCE state rho_ref is the
  budget: <E - E0>_ref = Tr(rho_ref (H - E0)) = B (--budget, default 1).
  Draws with a spectral gap < 1e-9 (relative) would be rejected; none occur
  in practice.
Reference state (--ref). "blind" (default): the message-averaged blind input
  sigma = (I/2) (x) |0><0| of the CE-9 half encoding. "mixed": I/4.
ML time. t_ML = pi / (2 <E - E0>_ref); the unitary is U = exp(-i H t),
  t = tfrac * t_ML (--tfrac, default 1).
Pool. Leader clustering of the samples (in draw order) on their NOISELESS
  per-use output law under the blind inputs with full-rank Z readout,
  L_U(y|m) = |<y|U|m 0>|^2, m in {0,1}, y in {0,..,3}, with distance
  max_m TV(L_U(.|m), L_V(.|m)). A sample joins the first representative
  within eps (--eps, default 0.05); otherwise it becomes a new
  representative. The pool is the list of representatives, prior uniform,
  H(F) = log2 |pool|. Drawn and SHA-256 hashed before any noise parameter
  exists; hash re-checked after the sweep. Draw s uses default_rng([s, 12]).
Channels (--channel gad,dephasing). U_f, then per qubit:
  gad        generalized amplitude damping, strength g, p = 1/(1+e^{-1/T})
             (--T, default 1), Kraus as procedural_share_surface.py.
  dephasing  pure dephasing, Kraus {sqrt(1-g/2) I, sqrt(g/2) Z}; g = 1 is
             full dephasing.
Readouts. nested Z (rank r = first log2 r of the bits A1 B1 A2 B2) and the
  CE-9 random-basis readout (one Haar basis of C^16 per rank).
Inputs. blind (CE-9 half encoding, X = the block message, X independent of F)
  and, for the overlap term, the informed "readable" input of CE-10
  (psi_fm = U_f^dag |m b_f>, b_f = f mod 2) with X = (block message, b_f),
  so I(X;F) = 1 bit.

TRAPS (stated, not hidden)
  * <E - E0> depends on the state. Here it is taken in rho_ref, not in each
    input ket; the per-input energies differ, so the bound is about the
    reference state only.
  * ML at the bound is about reaching an ORTHOGONAL state, for PURE states.
    rho_ref = sigma is mixed (rank 2); t_ML is used as a time SCALE, not as
    a guarantee that any input becomes orthogonal. The script prints the
    mean fidelity |<m0|U|m0>|^2 of the blind inputs at t_ML: it is not 0.
  * The budget only sets the spectral scale. U = exp(-i H pi/(2<E-E0>)) is
    invariant under H -> c H, so with t = t_ML the budget CANCELS: the pool
    is identical for every B (dimensional analysis, checked bit-for-bit
    below). The only meaningful knob is the phase budget tfrac = t/t_ML
    (or a fixed time with a varying budget, which is the same thing).
  * The sampling distribution of H (GUE here) is a choice; a different
    ensemble gives a different pool. Not tested.
  * Clustering uses noiseless statistics only, so the pool is independent of
    the noise channel. It DOES depend on the readout basis (Z) and on the
    blind input. For the Z readout, TV between two candidates' per-use
    laws can only shrink under GAD or dephasing followed by Z readout
    (data processing), so members of one cluster stay eps-close at every g;
    for the random readout no such guarantee holds.
  * Pool size vs eps: the 6-dimensional law space has a large eps-covering
    number, so at eps <= 0.1 almost every sample is its own representative
    and |pool| ~ n_samples (the pool is NOT saturated). The table printed
    below shows this; only eps ~ 0.2 begins to saturate.
  * Pure dephasing commutes with the Z readout: the nested-Z surface is FLAT
    in g by construction (checked). Dephasing is therefore shown with the
    random-basis readout.
  * Normalisation. H(F|Y)/H(F) rises with |pool| at fixed I(F;Y) (and I(F;Y)
    <= log2 r). So the fair Haar comparison is a Haar pool of the SAME size
    per draw ("haar-matched"); the 50-unitary CE-9 pool ("haar-50") is
    reported but differences against it are partly a size effect.

THE OVERLAP TERM (theorem; checked numerically)
  I(X,F;Y) = I(X;Y) + I(F;Y|X) and I(F;Y|X) = I(F;Y) + I(X;F|Y) - I(X;F),
  hence  I(X;Y) + I(F;Y) = I(X,F;Y) + I(X;F) - I(X;F|Y)
                         <= H(Y) + I(X;F) - I(X;F|Y).
  With X independent of F this is I(X;Y)+I(F;Y)+I(X;F|Y) = I(X,F;Y) <= H(Y):
  I(X;F|Y) >= 0 is exactly (part of) the slack. With an informed input the
  corrected bound I(X;Y)+I(F;Y) <= H(Y) can FAIL, and the overlap-corrected
  bound above always holds. The original form I(X;Y)+H(F|Y) <= H(Y), i.e.
  H(F|Y) <= H(Y|X), cannot be rescued by any such term: H(F|Y) >= H(F) - H(Y)
  grows like log2 |pool| while I(X;F|Y) <= H(X) and the other terms are
  bounded by H(X) and H(Y).
  The "58" is CE-6's count (docs/procedural-share.md, section 4): variant (a),
  pool A, eps = 0.05, alphabet 2, 72 defined grid points, the ORIGINAL form
  fails at 58. This script recomputes that run and I(X;F|Y) at those points.

STATISTICS. Canonical draw s = 2026; ensemble s = 1..--seeds (default 40),
  each with an ML pool, a Haar pool of the same size (draw_pool(K, 10^5+s))
  and the CE-9 Haar-50 pool (draw_pool(50, s)). Per draw, paired difference
  of the mean over nontrivial grid points (g < 1 for GAD, all g for
  dephasing) of the normalised share and of I(F;Y); two-sided sign-flip test
  (20000 flips), bootstrap 95% CI (10000), Holm across the aggregate tests;
  per-point tests Holm-corrected across points. |diff| < 1e-12 counts as 0.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedural_share as ps  # noqa: E402
import procedural_share_informed as pin  # noqa: E402
import procedural_share_surface as pss  # noqa: E402

TAG = 12
ZERO = 1e-12
RANKS = (2, 4, 8, 16)


# ---------------------------------------------------------------------------
# ML pool
# ---------------------------------------------------------------------------

def ref_state(kind: str) -> np.ndarray:
    if kind == "blind":
        return np.diag([0.5, 0.0, 0.5, 0.0]).astype(complex)  # (I/2) (x) |0><0|, index 2a+b
    if kind == "mixed":
        return np.eye(4, dtype=complex) / 4
    raise ValueError(kind)


def sample_unitaries(n: int, seed: int, budget: float = 1.0, tfrac: float = 1.0, ref: str = "blind"):
    """n ML-time unitaries. Depends only on (n, seed, budget, tfrac, ref)."""
    rng = np.random.default_rng([seed, TAG])
    rho = ref_state(ref)
    Us = np.empty((n, 4, 4), dtype=complex)
    rej = 0
    i = 0
    while i < n:
        A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        Hm = (A + A.conj().T) / 2
        w, v = np.linalg.eigh(Hm)
        w = w - w[0]
        if np.min(np.diff(w)) < 1e-9 * max(w[-1], 1e-300):
            rej += 1
            continue
        E = float(np.real(np.einsum("ij,ji->", rho, (v * w) @ v.conj().T)))
        w = w * (budget / E)                       # <E - E0>_ref = budget
        t = tfrac * math.pi / (2 * budget)         # t_ML
        Us[i] = (v * np.exp(-1j * w * t)) @ v.conj().T
        i += 1
    return Us, rej


def noiseless_law(Us: np.ndarray) -> np.ndarray:
    """L[n, m, y] = |<y|U|m 0>|^2 (blind inputs |00>, |10>; full-rank Z)."""
    return np.transpose(np.abs(Us[:, :, [0, 2]]) ** 2, (0, 2, 1))


def leader_cluster(L: np.ndarray, eps: float) -> list[int]:
    reps: list[int] = []
    R = np.zeros((0,) + L.shape[1:])
    for i, l in enumerate(L):
        if reps:
            d = 0.5 * np.abs(R - l[None]).sum(axis=2).max(axis=1)
            if d.min() <= eps + 1e-15:
                continue
        reps.append(i)
        R = np.concatenate([R, l[None]])
    return reps


def ml_pool(seed: int, n: int, eps: float, budget=1.0, tfrac=1.0, ref="blind"):
    Us, _ = sample_unitaries(n, seed, budget, tfrac, ref)
    reps = leader_cluster(noiseless_law(Us), eps)
    pool = np.ascontiguousarray(Us[reps])
    pool.setflags(write=False)
    return pool


# ---------------------------------------------------------------------------
# Channels, laws, information quantities
# ---------------------------------------------------------------------------

def kraus(channel: str, g: float, p: float) -> np.ndarray:
    if channel == "gad":
        return np.array(pss.two_qubit_gad_kraus(g, p))
    if channel == "dephasing":
        one = [math.sqrt(1 - g / 2) * np.eye(2), math.sqrt(g / 2) * np.diag([1.0, -1.0])]
        return np.array([np.kron(a, b) for a in one for b in one]).astype(complex)
    raise ValueError(channel)


def out_states(pool, psi, K):
    phi = np.einsum("fab,fmb->fma", pool, psi)
    a = np.einsum("kab,fmb->fmka", K, phi)
    return np.einsum("fmka,fmkc->fmac", a, a.conj())


def law_random_fast(rho: np.ndarray, basis: np.ndarray, r: int) -> np.ndarray:
    """Vectorised pss.joint_law_random: P(y|f,(x1,x2)), shape (F, m*m, r)."""
    nf, m = rho.shape[0], rho.shape[1]
    Bm = basis.T.reshape(16, 4, 4)                       # Bm[a, i1, i2] = basis[4 i1 + i2, a]
    C = np.einsum("fxij,ajk->fxaik", rho, Bm)            # rho1 @ B_a
    P = np.real(np.einsum("aim,fymn,fxain->fxya", Bm.conj(), rho, C))
    P = np.clip(P, 0, None).reshape(nf, m * m, r, 16 // r).sum(axis=3)
    return P


def law(rho, readout, r, bases):
    if readout == "nested":
        return pss.joint_law_nested(rho, r)
    return law_random_fast(rho, bases[r], r)


def quantities(cond: np.ndarray, S=None) -> dict:
    """All terms from P(y|f,x), uniform F and block message; X = (x, S[f]) if S given."""
    nf, nx, ny = cond.shape
    P = cond / (nf * nx)                                  # (f, x, y)
    if S is not None:
        labs = np.unique(S)
        Q = np.zeros((nf, nx * len(labs), ny))
        for k, s in enumerate(labs):
            Q[S == s, k * nx:(k + 1) * nx] = P[S == s]
        P = Q
    H = pss.H
    Hy, Hxy, Hfy, Hfxy = H(P.sum(axis=(0, 1))), H(P.sum(axis=0)), H(P.sum(axis=1)), H(P)
    Hf, Hx, Hfx = H(P.sum(axis=(1, 2))), H(P.sum(axis=(0, 2))), H(P.sum(axis=2))
    d = dict(Hy=Hy, HF=Hf, HFgY=Hfy - Hy, IFY=Hf + Hy - Hfy, IXY=Hx + Hy - Hxy,
             IXFY=Hfx + Hy - Hfxy, IXF=Hx + Hf - Hfx, IXFgY=Hxy + Hfy - Hy - Hfxy, HYgX=Hxy - Hx)
    d["ident"] = (d["IXY"] + d["IFY"]) - (d["IXFY"] + d["IXF"] - d["IXFgY"])
    return d


def surface(pool, psi, S, channel, p, gammas, ranks, readout, bases):
    keys = ("Hy", "HF", "HFgY", "IFY", "IXY", "IXFY", "IXF", "IXFgY", "HYgX", "ident")
    R = {k: np.zeros((len(gammas), len(ranks))) for k in keys}
    for i, g in enumerate(gammas):
        rho = out_states(pool, psi, kraus(channel, float(g), p))
        for j, r in enumerate(ranks):
            q = quantities(law(rho, readout, r, bases), S)
            for k in keys:
                R[k][i, j] = q[k]
    R["norm"] = R["HFgY"] / R["HF"]
    return R


def blind_inputs(nf):
    e = np.eye(4, dtype=complex)
    return np.broadcast_to(np.array([e[0], e[2]]), (nf, 2, 4)).copy()


def pass_counts(R, informed=False):
    """corrected, original, overlap-corrected: (#holds, #points)."""
    n = R["Hy"].size
    corr = int((R["IXY"] + R["IFY"] <= R["Hy"] + 1e-10).sum())
    orig = int((R["IXY"] + R["HFgY"] <= R["Hy"] + 1e-10).sum())
    ovl = int((R["IXY"] + R["IFY"] - R["IXF"] + R["IXFgY"] <= R["Hy"] + 1e-10).sum())
    return corr, orig, ovl, n


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks():
    rng = np.random.default_rng(5)
    pool = pss.draw_pool(3, 9)
    psi = blind_inputs(3)
    # fast random law == CE-9 loop
    b = pss.haar_unitary(16, rng)
    rho = out_states(pool, psi, kraus("gad", 0.3, 0.7))
    for r in RANKS:
        assert np.allclose(law_random_fast(rho, b, r), pss.joint_law_random(rho, b, r), atol=1e-12)
    # GAD path equals CE-9 output_states (half encoding)
    assert np.allclose(rho, pss.output_states(pool, 0.3, 0.7, inputs=(0, 2)), atol=1e-12)
    # dephasing TP; g=1 kills off-diagonals; Z statistics unchanged by dephasing
    for g in (0.0, 0.4, 1.0):
        K = kraus("dephasing", g, 0.0)
        assert np.allclose(np.einsum("kba,kbc->ac", K.conj(), K), np.eye(4), atol=1e-12)
    r0 = out_states(pool, psi, kraus("dephasing", 0.0, 0.0))
    r1 = out_states(pool, psi, kraus("dephasing", 1.0, 0.0))
    assert np.allclose(np.einsum("fmii->fmi", r0), np.einsum("fmii->fmi", r1), atol=1e-12)
    # budget cancels (bit-for-bit up to rounding)
    U1, _ = sample_unitaries(20, 3, 1.0)
    U2, _ = sample_unitaries(20, 3, 3.7)
    assert np.allclose(U1, U2, atol=1e-12)
    # <E-E0>_ref = budget and unitarity
    assert np.allclose(np.einsum("nab,ncb->nac", U1, U1.conj()), np.eye(4)[None], atol=1e-12)
    # identity on a random joint law with an informed label
    c = rng.random((6, 4, 8))
    c /= c.sum(axis=2, keepdims=True)
    q = quantities(c, np.arange(6) % 2)
    assert abs(q["ident"]) < 1e-10 and q["IXF"] > 0.99 and q["IXFgY"] >= -1e-12
    q = quantities(c)
    assert abs(q["IXF"]) < 1e-12 and q["IXY"] + q["IFY"] + q["IXFgY"] <= q["Hy"] + 1e-10


# ---------------------------------------------------------------------------
# CE-6 "58"
# ---------------------------------------------------------------------------

def ce6_overlap(eps=0.05, dg=0.05, dp=0.05):
    ps.USES = 1
    pool = ps.pool_A()
    gs = np.round(np.arange(0, 1 + dg / 2, dg), 10)
    pvals = np.round(np.arange(1.0, 0.5 - dp / 2, -dp), 10)
    out = {}
    for inp in ("uniform", "capacity"):
        rows = []
        for g in gs:
            for p in pvals:
                pi = ps.input_law(inp, float(g), float(p))
                Q = ps.gad_law(float(g), float(p))
                cls = [c for c in pool if ps.tv_max(c, Q) <= eps + ps.TOL]
                k = len(cls)
                if k == 0:
                    continue
                q = np.array([[c[1], c[2]] for c in cls])
                P = np.zeros((k, 2, 2))
                for x in (0, 1):
                    P[:, x, 1] = pi[x] * q[:, x] / k
                    P[:, x, 0] = pi[x] * (1 - q[:, x]) / k
                H = pss.H
                Hy, Hxy, Hfy, Hfxy = H(P.sum((0, 1))), H(P.sum(0)), H(P.sum(1)), H(P)
                Hf, Hx, Hfx = math.log2(k), H(pi), H(P.sum(2))
                IXY, IFY = Hx + Hy - Hxy, Hf + Hy - Hfy
                HFgY, HYgX = Hfy - Hy, Hxy - Hx
                IXF, IXFgY, IXFY = Hx + Hf - Hfx, Hxy + Hfy - Hy - Hfxy, Hfx + Hy - Hfxy
                rows.append(dict(g=float(g), p=float(p), k=k, deficit=IXY + HFgY - Hy, IXFgY=IXFgY,
                                 IXF=IXF, slack=Hy - IXY - IFY, ident=IXY + IFY - (IXFY + IXF - IXFgY)))
        out[inp] = rows
    return out


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def table(title, gammas, ranks, M, nd=3, md=False, marks=None):
    print(f"\n{title}")
    if md:
        print("| g | " + " | ".join(f"r={r}" for r in ranks) + " |")
        print("|---|" + "---|" * len(ranks))
    else:
        print("   g  " + "".join(f"{'r=' + str(r):>10}" for r in ranks))
    for i, g in enumerate(gammas):
        cells = []
        for j in range(len(ranks)):
            v = M[i, j]
            s = f"{0.0 if abs(v) < 0.5 * 10 ** -nd else v:.{nd}f}"
            if marks is not None:
                s += marks[i, j]
            cells.append(s)
        if md:
            print(f"| {g:.1f} | " + " | ".join(cells) + " |")
        else:
            print(f"{g:5.1f} " + "".join(f"{c:>10}" for c in cells))


def fz(v, nd=4) -> str:
    """Format, printing values below half a unit in the last place as 0 (no '-0.000')."""
    v = float(v)
    return f"{0.0 if abs(v) < 0.5 * 10 ** -nd else v:.{nd}f}"


def stars(p):
    return "**" if p < 0.01 else "*" if p < 0.05 else ""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--budget", type=float, default=1.0, help="<E-E0>_ref (cancels at t = t_ML)")
    ap.add_argument("--tfrac", type=float, default=1.0, help="t / t_ML (phase budget)")
    ap.add_argument("--ref", choices=("blind", "mixed"), default="blind")
    ap.add_argument("--eps", type=float, default=0.05, help="clustering TV radius")
    ap.add_argument("--n-samples", type=int, default=200)
    ap.add_argument("--seeds", type=int, default=40, help="ensemble draws 1..seeds (0 = skip)")
    ap.add_argument("--canonical", type=int, default=2026)
    ap.add_argument("--channel", default="gad,dephasing")
    ap.add_argument("--T", type=float, default=1.0, help="GAD temperature (hbar omega = k_B = 1)")
    ap.add_argument("--dg", type=float, default=0.1)
    ap.add_argument("--flips", type=int, default=20000)
    ap.add_argument("--boot", type=int, default=10000)
    ap.add_argument("--no-size-table", action="store_true")
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    md = args.markdown
    channels = [c.strip() for c in args.channel.split(",") if c.strip()]
    for c in channels:
        if c not in ("gad", "dephasing"):
            ap.error(f"unknown channel {c}")
    p = ps.p_of_T(args.T) if args.T > 0 else 1.0
    gammas = np.round(np.arange(0, 1 + args.dg / 2, args.dg), 10)
    ranks = RANKS
    print("TOY MODEL (Tier 2). Two-qubit proof-of-concept; NOT evidence about hadronic or QCD physics;")
    print("no physical claim. 'Energy budget' / 'ML time' are textbook finite-dimensional notions only.\n")
    self_checks()
    print("Self-checks passed: fast random readout = CE-9 loop; GAD path = CE-9; dephasing TP and")
    print("Z-invisible; budget cancels at t_ML; overlap identity and X-indep-F slack on random laws.\n")
    print(f"Settings: budget={args.budget} tfrac={args.tfrac} ref={args.ref} eps={args.eps} "
          f"n_samples={args.n_samples} T={args.T} (p={p:.4f}) dg={args.dg} channels={channels}")

    # ---- pool size vs eps / n / budget / tfrac / ref (canonical draw) ----
    if not args.no_size_table:
        print("\n## Pool size (canonical draw) vs eps and n_samples (ref=blind, tfrac=1, budget=1)\n")
        epss = (0.02, 0.05, 0.1, 0.2, 0.3)
        print("| n_samples | " + " | ".join(f"eps={e}" for e in epss) + " |")
        print("|---|" + "---|" * len(epss))
        for n in (200, 1000, 5000):
            L = noiseless_law(sample_unitaries(n, args.canonical)[0])
            print(f"| {n} | " + " | ".join(str(len(leader_cluster(L, e))) for e in epss) + " |")
        print("\n| knob | values | pool size at eps=0.05, n=1000 | pool hash (first 12) |")
        print("|---|---|---|---|")
        for B in (0.25, 1.0, 4.0):
            P_ = ml_pool(args.canonical, 1000, 0.05, budget=B)
            print(f"| budget | {B} | {len(P_)} | {pss.pool_hash(P_)[:12]} |")
        Ub1 = sample_unitaries(1000, args.canonical, 0.25)[0]
        Ub2 = sample_unitaries(1000, args.canonical, 4.0)[0]
        print(f"(max |U(B=0.25) - U(B=4)| over 1000 samples = {np.abs(Ub1 - Ub2).max():.1e}: the budget cancels)")
        for tf in (0.1, 0.25, 0.5, 1.0, 2.0):
            P_ = ml_pool(args.canonical, 1000, 0.05, tfrac=tf)
            print(f"| tfrac | {tf} | {len(P_)} | {pss.pool_hash(P_)[:12]} |")
        for rf in ("blind", "mixed"):
            P_ = ml_pool(args.canonical, 1000, 0.05, ref=rf)
            print(f"| ref | {rf} | {len(P_)} | {pss.pool_hash(P_)[:12]} |")
        Us = sample_unitaries(1000, args.canonical)[0]
        fid = (np.abs(np.einsum("nii->ni", Us)[:, [0, 2]]) ** 2).mean()
        print(f"\nMean fidelity |<m0|U|m0>|^2 of the blind inputs at t_ML: {fid:.3f} (ML is a time scale "
              f"for the mixed reference, not orthogonality of each input).")

    # ---- canonical draw ----
    pool = ml_pool(args.canonical, args.n_samples, args.eps, args.budget, args.tfrac, args.ref)
    h0 = pss.pool_hash(pool)
    K = len(pool)
    print(f"\n## Canonical ML pool: draw {args.canonical}, |pool| = {K} (H(F) = {math.log2(K):.3f} bits), "
          f"sha256 {h0[:16]}")
    bases = pss.random_readouts(ranks, args.canonical)
    psi_b = blind_inputs(K)
    psi_i, S_i = pin.inputs("readable", np.asarray(pool), None)
    configs = []
    for ch in channels:
        configs.append((ch, "nested"))
        configs.append((ch, "random"))
    canon = {}
    for ch, ro in configs:
        Rb = surface(pool, psi_b, None, ch, p, gammas, ranks, ro, bases)
        Ri = surface(pool, psi_i, S_i, ch, p, gammas, ranks, ro, bases)
        canon[(ch, ro)] = (Rb, Ri)
    assert pss.pool_hash(pool) == h0, "pool changed during sweep"
    print("pool hash re-checked after the sweep: unchanged.")

    for ch, ro in configs:
        Rb, Ri = canon[(ch, ro)]
        lab = f"{ch} ({'T=' + str(args.T) if ch == 'gad' else 'pure dephasing'}), {ro} readout"
        if ch == "dephasing" and ro == "nested":
            flat = max(np.abs(Rb[k] - Rb[k][0:1]).max() for k in ("HFgY", "IXY", "IFY"))
            print(f"\n### {lab}: FLAT in g by construction (max deviation from g=0 over the surface {flat:.1e});"
                  f" I(F;Y) at r=16 = {Rb['IFY'][0, -1]:.3f}")
            continue
        print(f"\n### {lab}, blind inputs")
        table("H(F|Y) (bits)", gammas, ranks, Rb["HFgY"], md=md)
        table("normalised share H(F|Y)/H(F)", gammas, ranks, Rb["norm"], nd=4, md=md)
        table("I(F;Y) (bits)", gammas, ranks, Rb["IFY"], md=md)
        table("I(X;Y) (bits)", gammas, ranks, Rb["IXY"], md=md)

    print("\n## Bounds on the canonical pool (counts of holds / grid points)\n")
    print("| channel | readout | blind: corrected | blind: original | blind max I(X;F\\|Y) | informed: corrected "
          "| informed: original | informed: overlap-corrected | informed I(X;F) | informed I(X;F\\|Y) range | max \\|identity residual\\| |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for ch, ro in configs:
        Rb, Ri = canon[(ch, ro)]
        cb, ob, _, n = pass_counts(Rb)
        ci, oi, vi, _ = pass_counts(Ri)
        res = max(np.abs(Rb["ident"]).max(), np.abs(Ri["ident"]).max())
        print(f"| {ch} | {ro} | {cb}/{n} | {ob}/{n} | {Rb['IXFgY'].max():.4f} | {ci}/{n} | {oi}/{n} | {vi}/{n} | "
              f"{fz(Ri['IXF'].min(), 3)} | {fz(Ri['IXFgY'].min(), 3)} - {fz(Ri['IXFgY'].max(), 3)} | {res:.1e} |")

    # ---- CE-6 "58" ----
    print("\n## The '58': CE-6 one-bit run (docs/procedural-share.md section 4), variant (a), pool A, eps=0.05\n")
    print("| input | defined pts | original fails | corrected holds | max \\|I(X;F)\\| | I(X;F\\|Y) at failures "
          "(min / median / max) | deficit H(F\\|Y)-H(Y\\|X) at failures (min / median / max) | failures with I(X;F\\|Y) >= deficit | max \\|identity\\| |")
    print("|---|---|---|---|---|---|---|---|---|")
    for inp, rows in ce6_overlap().items():
        fails = [r for r in rows if r["deficit"] > 1e-12]
        corr = sum(r["slack"] >= -1e-12 for r in rows)
        a = np.array([r["IXFgY"] for r in fails])
        d = np.array([r["deficit"] for r in fails])
        resc = int((a >= d).sum())
        print(f"| {inp} | {len(rows)} | {len(fails)} | {corr}/{len(rows)} | {max(abs(r['IXF']) for r in rows):.1e} | "
              f"{fz(a.min())} / {fz(np.median(a))} / {fz(a.max())} | {d.min():.3f} / {np.median(d):.3f} / {d.max():.3f} | "
              f"{resc} | {max(abs(r['ident']) for r in rows):.1e} |")
        if inp == "uniform":
            slack_f = np.array([r["slack"] for r in fails])
            pos = slack_f > 1e-9
            print(f"\n(uniform: at the failures the corrected-bound slack H(Y)-I(X;Y)-I(F;Y) ranges "
                  f"{fz(slack_f.min())} to {fz(slack_f.max())} ({int((~pos).sum())} failures have zero slack, i.e. "
                  f"I(X;F|Y) = 0 there); where the slack is positive, I(X;F|Y)/slack ranges "
                  f"{fz((a[pos] / slack_f[pos]).min(), 3)} to {fz((a[pos] / slack_f[pos]).max(), 3)}.)\n")

    if args.seeds <= 0:
        print(f"\nDone in {time.time() - t0:.0f}s.")
        return 0

    # ---- ensemble: ML vs Haar ----
    print(f"\n## Ensemble: {args.seeds} independent draws, ML pool vs Haar pools (blind inputs)\n")
    ens = {c: {"ml": [], "hm": [], "h50": []} for c in configs if c != ("dephasing", "nested")}
    sizes, cnt = [], {c: np.zeros(4, int) for c in configs}
    for s in range(1, args.seeds + 1):
        mlp = ml_pool(s, args.n_samples, args.eps, args.budget, args.tfrac, args.ref)
        hs = pss.pool_hash(mlp)
        Kd = len(mlp)
        sizes.append(Kd)
        hm = pss.draw_pool(Kd, 100000 + s)
        h50 = pss.draw_pool(50, s)
        bs = pss.random_readouts(ranks, s)
        psi_i, S_i = pin.inputs("readable", np.asarray(mlp), None)
        for c in configs:
            ch, ro = c
            Ri = surface(mlp, psi_i, S_i, ch, p, gammas, ranks, ro, bs)
            ci, oi, vi, n = pass_counts(Ri)
            cnt[c] += (ci, oi, vi, n)
            if c not in ens:
                continue
            for key, pl in (("ml", mlp), ("hm", hm), ("h50", h50)):
                ens[c][key].append(surface(pl, blind_inputs(len(pl)), None, ch, p, gammas, ranks, ro, bs))
        assert pss.pool_hash(mlp) == hs
    sizes = np.array(sizes)
    print(f"ML pool sizes over draws: min {sizes.min()}, median {int(np.median(sizes))}, max {sizes.max()} "
          f"(n_samples={args.n_samples}, eps={args.eps}); every pool hash re-checked.")
    print("\nInformed (readable) pass counts over all draws (holds / points): corrected bound is NOT a theorem here;")
    print("overlap-corrected bound is.\n")
    print("| channel | readout | corrected | original | overlap-corrected |")
    print("|---|---|---|---|---|")
    for c in configs:
        ci, oi, vi, n = cnt[c]
        print(f"| {c[0]} | {c[1]} | {ci}/{n} | {oi}/{n} | {vi}/{n} |")

    rng = np.random.default_rng(99)
    agg = []
    for c, E in ens.items():
        ch, ro = c
        mask = np.ones((len(gammas), len(ranks)), bool)
        if ch == "gad":
            mask[gammas >= 1 - 1e-12, :] = False
        for metric in ("norm", "IFY"):
            ml = np.array([R[metric] for R in E["ml"]])
            for ref in ("hm", "h50"):
                hh = np.array([R[metric] for R in E[ref]])
                D = ml - hh
                D[np.abs(D) < ZERO] = 0.0
                agg.append((c, metric, ref, D[:, mask].mean(axis=1), D, mask, ml, hh))
    pv = [pin.signflip_p(a[3][:, None], args.flips, rng)[0] for a in agg]
    pa = pin.holm(pv)
    print(f"\n### Aggregate paired tests (mean over nontrivial points; ML minus Haar; Holm across {len(agg)} tests)\n")
    print("| channel | readout | metric | vs | ML mean | Haar mean | diff | 95% CI | p | p (Holm) | ML > Haar draws |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for (c, metric, ref, d, D, mask, ml, hh), pval, padj in zip(agg, pv, pa):
        lo, hi = pin.boot_ci(d, args.boot, rng)
        print(f"| {c[0]} | {c[1]} | {'H(F|Y)/H(F)' if metric == 'norm' else 'I(F;Y)'} | "
              f"{'haar-matched' if ref == 'hm' else 'haar-50'} | {ml[:, mask].mean():.4f} | {hh[:, mask].mean():.4f} | "
              f"{d.mean():+.4f} | [{lo:+.4f}, {hi:+.4f}] | {pval:.4f} | {padj:.4f} | {(d > 0).sum()}/{len(d)} |")

    print("\n### Per-point: mean normalised share on the ML pool, and ML minus haar-matched "
          "(* / ** = Holm-adjusted p < 0.05 / 0.01 across the nontrivial points)")
    for (c, metric, ref, d, D, mask, ml, hh) in agg:
        if metric != "norm" or ref != "hm":
            continue
        idx = np.argwhere(mask)
        pp = pin.signflip_p(D[:, mask], args.flips, rng)
        padj = pin.holm(pp)
        marks = np.full(mask.shape, "", dtype=object)
        for (i, j), q in zip(idx, padj):
            marks[i, j] = stars(q)
        print(f"\n#### {c[0]}, {c[1]} readout ({int((padj < 0.05).sum())}/{len(padj)} points significant)")
        table("mean H(F|Y)/H(F), ML pool", gammas, ranks, ml.mean(axis=0), nd=4, md=md)
        table("mean H(F|Y)/H(F), haar-matched pool", gammas, ranks, hh.mean(axis=0), nd=4, md=md)
        table("ML minus haar-matched", gammas, ranks, D.mean(axis=0), nd=4, md=md, marks=marks)

    print(f"\nDone in {time.time() - t0:.0f}s. TOY MODEL: no physical claim.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
