#!/usr/bin/env python3
"""Tier 2 toy model (proof-of-concept for the SHAPE of a surface): procedural
share H(F|Y) and semantic share I(X;Y) over noise strength x readout rank.

    *** TOY MODEL. This is a proof-of-concept for the shape of a curve/surface
    *** in a two-qubit toy. It is NOT evidence about hadronic or QCD physics,
    *** and it makes no physical claim of any kind.

Pure numpy. Imports procedural_share.py (GAD Kraus operators and the p <-> T
convention). Run:

    python simulations/classical/procedural_share_surface.py
    python simulations/classical/procedural_share_surface.py --T 0      # plain AD
    python simulations/classical/procedural_share_surface.py --T 1 --seed 7 --pool 50
    python simulations/classical/procedural_share_surface.py --shots 4  # finite-shot check

MODEL (all choices are conventions of this toy, fixed here)
-----------------------------------------------------------
Candidate pool (step 1, channel-independent). POOL_SIZE (default 50) Haar-random
  2-qubit unitaries U_f (4x4; QR of a complex Ginibre matrix with the R-diagonal
  phase fix), drawn from numpy default_rng(--seed, default 2026) BEFORE any
  noise parameter exists. The draw function takes only (n, seed). A SHA-256 of
  the pool bytes is taken immediately after the draw and re-checked after every
  grid point of the sweep; the run aborts if it ever changes. No candidate is
  added, removed, filtered or reweighted by any channel quantity. Prior over F
  is uniform on the pool.
Message X and encoding (--encoding). The block is 2 channel uses; X is the
  pair of per-use messages, uniform and independent of F; the same unknown
  candidate U_f acts on both uses.
  * half (default): one message bit per use on qubit A, qubit B is a fixed
    reference prepared in |0>: input |x 0>, x in {0,1}; X in {0..3}.
  * full (degenerate control): x in {0,1,2,3} encoded as |x_A x_B>; X in
    {0..15}. Here the X-averaged input is I/4 and U_f (I/4) U_f^dag = I/4 for
    EVERY unitary, so P(y|f) does not depend on f: I(F;Y) = 0 and
    H(F|Y) = log2|pool| exactly, at every noise level and every rank. The
    candidate is identifiable only if the receiver also knows X; for this we
    also report H(F|X,Y) (procedural share with a known/pilot message).
Noise. Per use: U_f, then GAD(g, p) applied independently to qubit A and to
  qubit B (Nielsen & Chuang §8.3.5; Khatri, Sharma & Wilde arXiv:1903.07747
  with N = 1 - p). p = bath ground-state population = 1/(1 + e^{-1/T})
  (hbar omega = k_B = 1); --T 0 gives p = 1 (plain amplitude damping).
Readout (step 2). Both uses are read jointly as ONE outcome Y of a projective
  measurement on the 16-dim two-use output space. "Rank" r = number of
  outcomes, r in {2,4,8,16} (each projector has rank 16/r).
  * nested (default, primary): Z-readout of the 4 output qubits ordered
    (use1 A, use1 B, use2 A, use2 B); rank r keeps the first log2 r of these
    bits. So r=2: use 1, qubit A only; r=4: use 1, both qubits (use 2 not
    read); r=8: use 1 + use 2 qubit A; r=16: both uses, all 4 bits. Channel
    uses actually read: 1, 1, 2, 2. Rank r is an exact coarse-graining of
    rank 2r.
  * random (control): for each r an independent Haar-random orthonormal basis
    {v_i} of the 16-dim two-use space (seed --seed + 1000 + r, fixed before any
    noise), outcome j = block {v_i : i in [j*16/r, (j+1)*16/r)}. Entangled
    across uses; the bases for different r are NOT nested.
Joint law: P(f, x, y) = (1/|pool|) (1/|X|) Tr[Pi_y (N o U_f)(|x1><x1|) (x)
  (N o U_f)(|x2><x2|)], computed EXACTLY (no sampling).
Quantities (steps 3, 6), all in this one joint law:
  procedural share  H(F|Y) = sum_y P(y) H(P(F|Y=y)),  P(f|y) ∝ sum_x P(f,x,y)
  semantic share    I(X;Y)    (F marginalized: receiver does not know f)
  also              I(F;Y), I(X;Y|F) (semantic share if f were known),
                    H(F|X,Y) (procedural share if x were known), H(Y), H(Y|X,F).
  Exact identity:   H(Y) = I(F;Y) + I(X;Y|F) + H(Y|X,F)   (checked).
  Corrected bound:  I(X;Y) + I(F;Y) <= H(Y). Because X is independent of F,
    I(X;Y) <= I(X;Y|F) and so the bound HOLDS AS A THEOREM in this joint law;
    its 100% pass rate is a consistency check of the code, not a finding.
  Original bound:   I(X;Y) + H(F|Y) <= H(Y)  (reported for contrast; it is
    equivalent to H(F|Y) <= H(Y|X) and is not a theorem).
  Floors/caps: I(F;Y) <= H(Y) <= log2 r, so H(F|Y) >= log2|pool| - log2 r.
Monotonicity in rank (step 5) -- HONEST STATUS. For the nested readout,
  rank r is a deterministic function of rank 2r, so by data processing
  I(F;Y_r) <= I(F;Y_2r), i.e. H(F|Y) is non-increasing in rank AT EVERY
  NOISE SETTING BY CONSTRUCTION. That check is guaranteed, not a test. The
  same holds in g: GAD at fixed p is a semigroup in (1-g) and maps diagonal
  to diagonal, so Z-readout after GAD(g2 > g1) is a classical garbling of
  Z-readout after GAD(g1); H(F|Y) non-decreasing in g is also guaranteed for
  the nested readout. The random-basis control is not nested, so there the
  rank- and g-monotonicity are genuine (toy) checks.
Finite shots (optional, --shots N): N i.i.d. blocks with the same f and fresh
  X; H(F|Y^N) estimated by Monte Carlo (--mc trials). Exact runs need none.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedural_share as ps  # noqa: E402  (gad_kraus, p_of_T, T_of_p)

TOL = 1e-10
RANKS_DEFAULT = (2, 4, 8, 16)
USES = 2  # channel uses per block (4-qubit output = 16 outcomes at full rank)


# ---------------------------------------------------------------------------
# Step 1: channel-independent candidate pool
# ---------------------------------------------------------------------------

def haar_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    ph = np.diag(r) / np.abs(np.diag(r))
    return q * ph


def draw_pool(n: int, seed: int) -> np.ndarray:
    """Pool of n Haar 4x4 unitaries. Depends ONLY on (n, seed)."""
    rng = np.random.default_rng(seed)
    pool = np.stack([haar_unitary(4, rng) for _ in range(n)])
    pool.setflags(write=False)
    return pool


def pool_hash(pool: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(pool).tobytes()).hexdigest()


def random_readouts(ranks, seed: int) -> dict[int, np.ndarray]:
    """For each rank r, a Haar basis of C^16 (columns). Depends only on seed."""
    out = {}
    for r in ranks:
        b = haar_unitary(16, np.random.default_rng(seed + 1000 + r))
        b.setflags(write=False)
        out[r] = b
    return out


# ---------------------------------------------------------------------------
# Channel: U_f then GAD on each qubit
# ---------------------------------------------------------------------------

def two_qubit_gad_kraus(g: float, p: float) -> list[np.ndarray]:
    k1 = ps.gad_kraus(g, p)
    return [np.kron(a, b) for a in k1 for b in k1]


def apply_kraus(kraus, rho):
    return sum(k @ rho @ k.conj().T for k in kraus)


ENCODINGS = {"half": (0, 2), "full": (0, 1, 2, 3)}  # basis index 2*x_A + x_B


def output_states(pool: np.ndarray, g: float, p: float, inputs=(0, 1, 2, 3)) -> np.ndarray:
    """rho[f, i] = GAD(x)GAD (U_f |in_i><in_i| U_f^dag), shape (F, len(inputs), 4, 4)."""
    kraus = two_qubit_gad_kraus(g, p)
    nf = pool.shape[0]
    rho = np.zeros((nf, len(inputs), 4, 4), dtype=complex)
    for f in range(nf):
        for i, x in enumerate(inputs):
            psi = pool[f][:, x]
            rho[f, i] = apply_kraus(kraus, np.outer(psi, psi.conj()))
    return rho


def joint_law_nested(rho: np.ndarray, r: int) -> np.ndarray:
    """P(y | f, x) for the nested Z readout, shape (F, |X|, r)."""
    d = np.real(np.einsum("fxii->fxi", rho))  # (F, m, 4): P1(y1|x,f)
    d = np.clip(d, 0, None)
    nf, m = d.shape[0], d.shape[1]
    # full 16-outcome law over (x1,x2) -> (y1,y2), y index = 4*y1 + y2,
    # with y1 = (A1 B1), y2 = (A2 B2): bit order (A1, B1, A2, B2), MSB first.
    full = np.einsum("fai,fbj->fabij", d, d).reshape(nf, m * m, 16)
    return full.reshape(nf, m * m, r, 16 // r).sum(axis=3)  # keep first log2 r bits


def joint_law_random(rho: np.ndarray, basis: np.ndarray, r: int) -> np.ndarray:
    nf, m = rho.shape[0], rho.shape[1]
    out = np.zeros((nf, m * m, r))
    blk = 16 // r
    for f in range(nf):
        for x1 in range(m):
            for x2 in range(m):
                big = np.kron(rho[f, x1], rho[f, x2])
                diag = np.real(np.einsum("ia,ij,ja->a", basis.conj(), big, basis))
                out[f, m * x1 + x2] = np.clip(diag, 0, None).reshape(r, blk).sum(axis=1)
    return out


# ---------------------------------------------------------------------------
# Information quantities in the joint law P(f,x,y) = P(y|f,x)/(F*16)
# ---------------------------------------------------------------------------

def H(p) -> float:
    p = np.asarray(p, float).ravel()
    p = p[p > 1e-300]
    return float(-np.sum(p * np.log2(p)))


def shares(cond: np.ndarray) -> dict:
    nf, nx, ny = cond.shape
    assert np.allclose(cond.sum(axis=2), 1, atol=1e-9), "P(y|f,x) not normalized"
    P = cond / (nf * nx)
    Pfy, Pxy, Py = P.sum(axis=1), P.sum(axis=0), P.sum(axis=(0, 1))
    Hy, Hfxy = H(Py), H(P)
    Hf, Hx, Hfx = math.log2(nf), math.log2(nx), math.log2(nf * nx)
    HFgY = H(Pfy) - Hy
    IFY = Hf - HFgY
    IXY = Hx + Hy - H(Pxy)
    HYgXF = Hfxy - Hfx
    HYgF = H(Pfy) - Hf
    IXYgF = HYgF - HYgXF
    HYgX = H(Pxy) - Hx
    HFgXY = Hfxy - H(Pxy)
    return dict(HFgY=HFgY, IFY=IFY, IXY=IXY, IXYgF=IXYgF, HFgXY=HFgXY, Hy=Hy,
                HYgXF=HYgXF, HYgX=HYgX)


def finite_shot_HFgY(cond: np.ndarray, shots: int, trials: int, rng) -> float:
    """MC estimate of H(F | Y^shots), N i.i.d. blocks, same f, fresh uniform X."""
    nf = cond.shape[0]
    Pyf = cond.mean(axis=1)  # P(y|f), X marginalized, (F, r)
    logL = np.log(np.clip(Pyf, 1e-300, None))
    acc = 0.0
    for _ in range(trials):
        f = rng.integers(nf)
        ys = rng.choice(Pyf.shape[1], size=shots, p=Pyf[f] / Pyf[f].sum())
        ll = logL[:, ys].sum(axis=1)
        post = np.exp(ll - ll.max())
        post /= post.sum()
        acc += H(post)
    return acc / trials


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks(pool: np.ndarray) -> None:
    for u in pool:
        assert np.allclose(u.conj().T @ u, np.eye(4), atol=1e-12)
    for g, p in [(0.0, 1.0), (0.3, 0.8), (1.0, 0.5)]:
        k = two_qubit_gad_kraus(g, p)
        assert np.allclose(sum(a.conj().T @ a for a in k), np.eye(4), atol=1e-12)
    # g=1: output is diag(p,1-p)^{(x)2} for every input -> no information
    rho = output_states(pool[:3], 1.0, 0.7)
    fixed = np.kron(np.diag([0.7, 0.3]), np.diag([0.7, 0.3]))
    assert np.allclose(rho, fixed, atol=1e-12)
    # nested coarse-graining consistency: rank 8 from rank 16 by marginalizing
    rho = output_states(pool[:4], 0.2, 0.9)
    c16, c8 = joint_law_nested(rho, 16), joint_law_nested(rho, 8)
    assert np.allclose(c16.reshape(4, 16, 8, 2).sum(axis=3), c8)
    # GAD Z-readout semigroup / garbling: GAD(g2) = GAD(g') o GAD(g1)
    g1, gp, p = 0.3, 0.4, 0.8
    g2 = 1 - (1 - g1) * (1 - gp)
    r1 = output_states(pool[:2], g1, p)
    kk = two_qubit_gad_kraus(gp, p)
    r12 = np.array([[apply_kraus(kk, r1[f, x]) for x in range(4)] for f in range(2)])
    assert np.allclose(r12, output_states(pool[:2], g2, p), atol=1e-12)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def fmt_table(title, gammas, ranks, M, nd=3):
    M = np.where(np.abs(M) < 5e-10, 0.0, M) + 0.0  # print -0.000 as 0.000
    lines = [title, "  g     " + "".join(f"  r={r:<5d}" for r in ranks)]
    for i, g in enumerate(gammas):
        lines.append(f"  {g:4.2f}  " + "".join(f"  {M[i, j]:7.{nd}f}" for j in range(len(ranks))))
    return "\n".join(lines)


def run_surface(pool, phash, gammas, ranks, p, readout, bases, inputs):
    keys = ("HFgY", "IFY", "IXY", "IXYgF", "HFgXY", "Hy", "HYgXF", "HYgX")
    S = {k: np.zeros((len(gammas), len(ranks))) for k in keys}
    conds = {}
    for i, g in enumerate(gammas):
        rho = output_states(pool, float(g), p, inputs)
        for j, r in enumerate(ranks):
            c = joint_law_nested(rho, r) if readout == "nested" else joint_law_random(rho, bases[r], r)
            s = shares(c)
            for k in keys:
                S[k][i, j] = s[k]
            conds[(i, j)] = c
        assert pool_hash(pool) == phash, "candidate pool changed during sweep"
    return S, conds


def analyse(S, gammas, ranks, nf, label, out):
    hf, ixy, ify, hy = S["HFgY"], S["IXY"], S["IFY"], S["Hy"]
    ident = np.abs(hy - (S["IFY"] + S["IXYgF"] + S["HYgXF"])).max()
    assert ident < 1e-9, ident
    corr = (ixy + ify <= hy + TOL)
    orig = (ixy + hf <= hy + TOL)
    out(f"\n[{label}] checks")
    out(f"  identity H(Y)=I(F;Y)+I(X;Y|F)+H(Y|X,F): max residual {ident:.1e}")
    out(f"  corrected bound I(X;Y)+I(F;Y)<=H(Y): {corr.sum()}/{corr.size} (theorem here)")
    out(f"  original  bound I(X;Y)+H(F|Y)<=H(Y): {orig.sum()}/{orig.size}")
    floor = math.log2(nf) - np.log2(np.array(ranks))[None, :]
    out(f"  floor H(F|Y) >= log2|pool| - log2 r respected: {bool((hf >= floor - TOL).all())}")
    dr = np.diff(hf, axis=1)  # along rank
    viol_r = [(gammas[i], ranks[j], ranks[j + 1], dr[i, j])
              for i in range(dr.shape[0]) for j in range(dr.shape[1]) if dr[i, j] > TOL]
    out(f"  H(F|Y) non-increasing in rank at every g: {not viol_r}"
        + ("" if not viol_r else f"  violations (g, r->2r, increase): "
           + ", ".join(f"({a:.2f},{b}->{c},+{d:.4f})" for a, b, c, d in viol_r)))
    drop = np.where(np.abs(hf[:, 0] - hf[:, -1]) < 5e-10, 0.0, hf[:, 0] - hf[:, -1]) + 0.0
    out(f"  drop H(F|Y)[r={ranks[0]}] - H(F|Y)[r={ranks[-1]}]: min {drop.min():.3f} (g={gammas[drop.argmin()]:.2f}),"
        f" max {drop.max():.3f} (g={gammas[drop.argmax()]:.2f}) bits")
    dg = np.diff(hf, axis=0)
    viol_g = int((dg < -TOL).sum())
    out(f"  H(F|Y) non-decreasing in g at every rank: {viol_g == 0} ({viol_g} decreasing steps)")
    # concavity in g of H(F|Y) and of I(F;Y)
    if len(gammas) >= 3:
        d2 = np.diff(hf, n=2, axis=0)
        out("  sign of 2nd difference of H(F|Y) in g per rank (+ convex, - concave): "
            + ", ".join(f"r={r}: {int((d2[:, j] > 1e-9).sum())}+/{int((d2[:, j] < -1e-9).sum())}-"
                        for j, r in enumerate(ranks)))
    # step sizes along rank (diminishing returns?)
    steps = np.where(np.abs(dr.mean(axis=0)) < 5e-10, 0.0, -dr.mean(axis=0)) + 0.0
    out("  mean decrease of H(F|Y) per rank doubling: "
        + ", ".join(f"{ranks[j]}->{ranks[j+1]}: {steps[j]:.3f}" for j in range(len(steps))))
    return dict(corr=(int(corr.sum()), corr.size), orig=(int(orig.sum()), orig.size),
                viol_r=viol_r, viol_g=viol_g)


def maybe_plot(S, gammas, ranks, label, path):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        print(f"  (matplotlib unavailable; skipped {path})")
        return
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    for ax, (k, t) in zip(axes, [("HFgY", "H(F|Y) procedural"), ("IFY", "I(F;Y)"), ("IXY", "I(X;Y) semantic")]):
        im = ax.imshow(S[k], aspect="auto", origin="lower", cmap="viridis",
                       extent=[-0.5, len(ranks) - 0.5, gammas[0], gammas[-1]])
        ax.set_xticks(range(len(ranks)), [str(r) for r in ranks])
        ax.set_xlabel("readout rank r")
        ax.set_ylabel("damping g")
        ax.set_title(t)
        fig.colorbar(im, ax=ax, label="bits")
    fig.suptitle(f"TOY MODEL ({label}) - shape only; not evidence about hadronic/QCD physics")
    fig.tight_layout()
    fig.savefig(path, dpi=90)
    print(f"  wrote {path}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seed", type=int, default=2026, help="pool seed (default 2026)")
    ap.add_argument("--pool", type=int, default=50, help="pool size (default 50)")
    ap.add_argument("--ranks", type=str, default="2,4,8,16", help="subset of 2,4,8,16")
    ap.add_argument("--gammas", type=str, default="0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0")
    ap.add_argument("--T", type=float, default=1.0,
                    help="bath temperature (hbar omega = k_B = 1); 0 = plain AD; default 1")
    ap.add_argument("--gad", type=float, default=None,
                    help="set bath ground population p in [0.5,1] directly (overrides --T)")
    ap.add_argument("--encoding", choices=tuple(ENCODINGS), default="half",
                    help="half: message bit on qubit A, B=|0> (default); full: 4 messages/use")
    ap.add_argument("--readout", choices=("nested", "random", "both"), default="both")
    ap.add_argument("--shots", type=int, default=0, help="finite-shot MC check (blocks); 0 = off")
    ap.add_argument("--mc", type=int, default=2000, help="MC trials for --shots")
    ap.add_argument("--robust", type=int, default=0,
                    help="also re-run the random-basis control over seeds 1..N (pool and bases)")
    ap.add_argument("--plot", type=str, default="", help="directory for PNG heatmaps (optional)")
    args = ap.parse_args()

    # ---- Step 1: pool drawn and hashed before any noise parameter exists ----
    pool = draw_pool(args.pool, args.seed)
    phash = pool_hash(pool)
    ranks = [int(r) for r in args.ranks.split(",")]
    assert all(r in RANKS_DEFAULT for r in ranks), "ranks must be among 2,4,8,16"
    bases = random_readouts(ranks, args.seed)
    self_checks(pool)
    assert pool_hash(pool) == phash

    # ---- noise parameters defined only now ----
    p = float(args.gad) if args.gad is not None else ps.p_of_T(args.T)
    assert 0.5 <= p <= 1.0
    T = ps.T_of_p(p)
    gammas = np.array([float(g) for g in args.gammas.split(",")])
    inputs = ENCODINGS[args.encoding]
    nx = len(inputs) ** USES

    print("TOY MODEL: procedural-share surface (two qubits, GAD on each qubit). Shape only;")
    print("NOT evidence about hadronic or QCD physics. No physical claim is drawn.")
    print(f"pool: {args.pool} Haar 2-qubit unitaries, seed {args.seed}, sha256 {phash[:16]}...")
    print(f"noise: GAD per qubit, p = {p:.4f} (T = {T:.4g}{', plain AD' if p == 1 else ''}); "
          f"block = {USES} channel uses, encoding '{args.encoding}', X uniform on {nx} messages")
    print(f"log2|pool| = {math.log2(args.pool):.4f} bits")

    modes = ["nested", "random"] if args.readout == "both" else [args.readout]
    for mode in modes:
        S, conds = run_surface(pool, phash, gammas, ranks, p, mode, bases, inputs)
        lab = f"{mode} readout"
        print(f"\n===== {lab} =====")
        for k, t in [("HFgY", "H(F|Y) procedural share [bits]"), ("IXY", "I(X;Y) semantic share [bits]"),
                     ("IFY", "I(F;Y) [bits]"), ("IXYgF", "I(X;Y|F) semantic share if f known [bits]"),
                     ("HFgXY", "H(F|X,Y) procedural share if x known [bits]"),
                     ("Hy", "H(Y) [bits]")]:
            print(fmt_table(t, gammas, ranks, S[k]))
        analyse(S, gammas, ranks, args.pool, lab, print)
        if args.shots > 0:
            rng = np.random.default_rng(args.seed + 99)
            print(f"  finite shots: MC H(F|Y^N), N={args.shots} blocks, {args.mc} trials (g, r: exact N=1 / MC N):")
            for i in [0, len(gammas) // 2]:
                for j, r in enumerate(ranks):
                    est = finite_shot_HFgY(conds[(i, j)], args.shots, args.mc, rng)
                    print(f"    g={gammas[i]:.2f} r={r:2d}: {S['HFgY'][i, j]:.3f} / {est:.3f}")
        if args.plot:
            os.makedirs(args.plot, exist_ok=True)
            maybe_plot(S, gammas, ranks, f"{lab}, p={p:.3f}",
                       os.path.join(args.plot, f"procedural_share_surface_{mode}_p{p:.3f}.png"))

    if args.robust > 0:
        vr = vg = tot = 0
        worst = 0.0
        for sd in range(1, args.robust + 1):
            pl = draw_pool(args.pool, sd)
            h = pool_hash(pl)
            S, _ = run_surface(pl, h, gammas, ranks, p, "random", random_readouts(ranks, sd), inputs)
            d = np.diff(S["HFgY"], axis=1)
            vr += int((d > TOL).sum())
            tot += d.size
            worst = max(worst, float(d.max()))
            vg += int((np.diff(S["HFgY"], axis=0) < -TOL).sum())
        print(f"\n[random readout, seeds 1..{args.robust}] rank-doubling steps where H(F|Y) INCREASES: "
              f"{vr}/{tot} (largest increase {worst:.2e} bits); g-steps where it decreases: {vg}")

    assert pool_hash(pool) == phash, "candidate pool changed"
    print(f"\npool sha256 unchanged after sweep: {phash[:16]}...")
    print("No physics claim is drawn from this toy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
