#!/usr/bin/env python3
"""Tier 2 toy model (proof-of-concept): does an input that depends on the
selected function lower the procedural share H(F|Y)? Blind vs informed inputs
on the two-qubit procedural-share surface.

    *** TOY MODEL. Proof-of-concept for the shape of a curve in a two-qubit
    *** toy. It is NOT evidence about hadronic or QCD physics and makes no
    *** physical claim of any kind.

Pure numpy. Imports procedural_share_surface.py (pool draw + hash, GAD Kraus,
nested readout, information helpers). Run:

    python simulations/classical/procedural_share_informed.py              # T=1, 40 seeds, + T=0, inf
    python simulations/classical/procedural_share_informed.py --seeds 20 --no-robust-T
    python simulations/classical/procedural_share_informed.py --variants eigen,phase --markdown

SETUP (unchanged from procedural_share_surface.py unless stated)
-----------------------------------------------------------------
Pool: 50 Haar 2-qubit unitaries U_f, seed 2026 (canonical) or seeds 1..K
  (ensemble), drawn and SHA-256 hashed BEFORE any noise parameter exists. The
  structureless-control unitaries V_f (variant 'rand') are drawn in the same
  step from an independent stream, default_rng([seed, 5000]), and hashed with
  the pool. Hashes are re-checked after every condition.
Block: 2 channel uses, same unknown f on both; message M = (m1, m2), m in
  {0,1} uniform, independent of F; uniform prior over F. Per use: input ket
  |psi_{f,m}>, then U_f, then GAD(g,p) on each qubit (p = 1/(1+e^{-1/T})).
Readout: nested Z readout, rank r in {2,4,8,16} (procedural_share_surface.py).
All quantities exact from probabilities.

INPUT VARIANTS (|psi_{f,0}>, |psi_{f,1}> are orthonormal in every variant)
  blind     |m 0>  (CE-9 default; f-independent).            hint S = const
  blindalt  |m 1>  (another f-INDEPENDENT input; control).   hint S = const
  eigen  (a) eigenvectors of U_f, eigenphases sorted ascending in (-pi, pi]:
            m=0 -> e_0, m=1 -> e_1. U_f preserves them (U_f e = lambda e), so
            the output is GAD(x)GAD(|e><e|): U_f contributes nothing but a phase.
  phase  (b) |psi_{f,m}> = (1/2) sum_k exp(i phi_k(f)) (-1)^{m * a(k)} |k>,
            phi_k = sorted eigenphases of U_f, a(k) = qubit-A bit of k.
  fixedpt(c) n = eigenvector with eigenvalue closest to +1 (near-fixed),
            q = eigenvector with eigenvalue farthest from +1;
            |psi_{f,m}> = (e_n + (-1)^m e_q)/sqrt 2.
  rand      CONTROL, structureless label: |psi_{f,m}> = V_f |m 0>, V_f Haar,
            independent of U_f.                              hint S = f
  readable  CONTROL, leak by construction: |psi_{f,m}> = U_f^dag |m b_f>,
            b_f = f mod 2. U_f undoes the pre-rotation, so the output is
            GAD(|m b_f>): a 1-bit tag of f written straight into the readout.
                                                             hint S = b_f
  gphase    NULL CONTROL: exp(2 pi i f/50)|m 0>; f is carried only in a global
            phase, physically identical to blind. Gap == 0 exactly.
  For eigen/phase/fixedpt S = f. Eigenvector phase convention: the largest-
  modulus component of each eigenvector is made real positive (it matters
  only for fixedpt's superposition).

QUANTITIES
  gap(g,r) = H(F|Y)_blind - H(F|Y)_variant = I(F;Y)_variant - I(F;Y)_blind
  chi_in   = Holevo chi between F and the block input state
             tau_f = sigma_f (x) sigma_f, sigma_f = (1/2) sum_m |psi_fm><psi_fm|
             (the operational input-function correlation; noise-independent)
  I(S;F)   = classical MI between F and the hint label (log2 50, 1 or 0 bits)
  chi_out  = Holevo chi between F and the block OUTPUT state (per g)
BOUNDS (which are guaranteed)
  * I(F;Y) <= chi_out(g) <= ... (Holevo) and I(F;Y) <= min(log2 r, log2 50):
    so gap <= min(log2 r, log2 50) - I(F;Y)_blind and gap >= -I(F;Y)_blind.
    Guaranteed.
  * gap <= chi_in is NOT a theorem. It holds when the channel acts on f only
    through the input (F -> input -> Y Markov): gphase, eigen (U_f acts as a
    phase on its own eigenvectors). It fails in general: blindalt has
    chi_in = 0 but gap != 0, because the gap also measures how well each input
    PROBES U_f, not only what the input already knows about f.
  * readable: I(F;Y) <= H(b_f) = 1 bit. Guaranteed.
  * Haar-invariance null (exact in expectation): if, for every f, the output
    pair (U_f psi_{f,0}, U_f psi_{f,1}) is a Haar-distributed orthonormal pair,
    independent across f, then the informed surface has the same distribution
    over pool draws as the blind one, so E_pool[gap] = 0 at every (g, r).
    This holds for blindalt, eigen (Haar eigenvectors are a Haar basis,
    independent of the eigenvalues that order them) and rand (U_f V_f is Haar).
    It is not implied for phase and fixedpt (their inputs reference the
    computational basis or an eigenvector phase convention).
  * g = 1: output independent of input -> gap = 0 by construction.
  * Rank/g monotonicity of each H(F|Y) is guaranteed (CE-9); monotonicity
    of the GAP (a difference) is not, and is checked.
STATISTICAL TEST (what randomness, what null)
  The canonical pool is computed exactly, so it has no sampling noise. The
  test is over INDEPENDENT POOL DRAWS (seeds 1..K, default 40; pool and V_f
  redrawn per seed), with blind and informed paired on the same pool.
  Null H0: E_pool[gap(g,r)] = 0 (the informed input is no more informative
  about f than the blind input, on average over Haar pools).
  * Aggregate (one test per variant): per seed, mean gap over the 40 grid
    points with g < 1; two-sided sign-flip permutation test (20000 flips),
    bootstrap 95% CI; Holm correction across the tested variants.
  * Per point: sign-flip test at each of the 40 points, Holm across points.
  'Consistent with zero' = Holm-adjusted aggregate p > 0.05.
BALANCE SHEET
  With X = M (independent of F): I(X;Y) + I(F;Y) <= H(Y) is a theorem.
  With X = (M, S) (the full preparation label; correlated with F when S is
  f-dependent) it is NOT a theorem; reported pass rate. What always holds is
  I(X,F;Y) <= H(Y).
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
import procedural_share_surface as pss  # noqa: E402

TOL = 1e-10
VARIANTS = ("blindalt", "eigen", "phase", "fixedpt", "rand", "readable", "gphase")
STRUCTURAL = ("eigen", "phase", "fixedpt")
TESTED = ("blindalt", "eigen", "phase", "fixedpt", "rand", "readable")  # gphase is exact
LABELS = {"blind": "blind |m0>", "blindalt": "blind-alt |m1> (f-independent control)",
          "eigen": "(a) eigenbasis of U_f", "phase": "(b) eigenphase pattern",
          "fixedpt": "(c) near-fixed/far eigenvector superposition",
          "rand": "control: structureless random V_f|m0>",
          "readable": "control: readable 1-bit tag U_f^dag|m b_f>",
          "gphase": "null: global-phase tag"}


# ---------------------------------------------------------------------------
# Pool (+ structureless control unitaries), drawn before any noise
# ---------------------------------------------------------------------------

def draw_all(n: int, seed: int):
    pool = pss.draw_pool(n, seed)
    rng = np.random.default_rng([seed, 5000])
    V = np.stack([pss.haar_unitary(4, rng) for _ in range(n)])
    V.setflags(write=False)
    h = hashlib.sha256(pool.tobytes() + V.tobytes()).hexdigest()
    return pool, V, h


def all_hash(pool, V) -> str:
    return hashlib.sha256(np.ascontiguousarray(pool).tobytes() + np.ascontiguousarray(V).tobytes()).hexdigest()


def eig_sorted(U: np.ndarray):
    w, v = np.linalg.eig(U)
    order = np.argsort(np.angle(w))
    w, v = w[order], v[:, order]
    for k in range(4):
        i = int(np.argmax(np.abs(v[:, k])))
        v[:, k] *= np.conj(v[i, k]) / abs(v[i, k])
        v[:, k] /= np.linalg.norm(v[:, k])
    assert np.allclose(v.conj().T @ v, np.eye(4), atol=1e-8), "degenerate eigenbasis"
    return w, v


def inputs(variant: str, pool: np.ndarray, V: np.ndarray):
    """Input kets psi[f, m] (shape (F, 2, 4)) and hint labels S[f]."""
    nf = pool.shape[0]
    e = np.eye(4, dtype=complex)
    psi = np.zeros((nf, 2, 4), dtype=complex)
    S = np.zeros(nf, dtype=int)
    for f in range(nf):
        U = pool[f]
        if variant == "blind":
            psi[f] = [e[0], e[2]]
        elif variant == "blindalt":
            psi[f] = [e[1], e[3]]
        elif variant == "gphase":
            psi[f] = np.exp(2j * math.pi * f / nf) * np.array([e[0], e[2]])
            S[f] = f
        elif variant == "rand":
            psi[f] = [V[f][:, 0], V[f][:, 2]]
            S[f] = f
        elif variant == "readable":
            b = f % 2
            psi[f] = [U.conj().T @ e[0 + b], U.conj().T @ e[2 + b]]
            S[f] = b
        else:
            w, v = eig_sorted(U)
            S[f] = f
            if variant == "eigen":
                psi[f] = [v[:, 0], v[:, 1]]
            elif variant == "phase":
                ph = np.exp(1j * np.angle(w)) / 2
                sgn = np.array([1, 1, -1, -1])  # (-1)^{a(k)}, a(k) = k >> 1
                psi[f] = [ph, ph * sgn]
            elif variant == "fixedpt":
                d = np.abs(w - 1)
                n, q = int(np.argmin(d)), int(np.argmax(d))
                psi[f] = [(v[:, n] + v[:, q]) / math.sqrt(2), (v[:, n] - v[:, q]) / math.sqrt(2)]
            else:
                raise ValueError(variant)
    G = np.einsum("fma,fna->fmn", psi.conj(), psi)
    assert np.allclose(G, np.eye(2)[None], atol=1e-9), f"{variant}: inputs not orthonormal"
    return psi, S


# ---------------------------------------------------------------------------
# Channel, laws, entropies
# ---------------------------------------------------------------------------

def out_states(pool, psi, g, p):
    K = np.array(pss.two_qubit_gad_kraus(g, p))          # (16, 4, 4)
    phi = np.einsum("fab,fmb->fma", pool, psi)            # U_f psi
    a = np.einsum("kab,fmb->fmka", K, phi)
    return np.einsum("fmka,fmkc->fmac", a, a.conj())      # (F, 2, 4, 4)


def vn(rho) -> float:
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-14]
    return float(-np.sum(ev * np.log2(ev)))


def holevo_block(sig):
    """chi(F; sigma_f (x) sigma_f) for per-use states sig[f] (F, 4, 4)."""
    avg = np.mean([np.kron(s, s) for s in sig], axis=0)
    return vn(avg) - float(np.mean([2 * vn(s) for s in sig]))


def I_label_Y(cond, S):
    """I((M,S);Y) and I((M,F);Y) from P(y|f,m) with uniform priors."""
    nf, nm, ny = cond.shape
    P = cond / (nf * nm)
    Hy = pss.H(P.sum(axis=(0, 1)))
    labs = np.unique(S)
    Psm = np.stack([P[S == s].sum(axis=0) for s in labs])   # (s, m, y)
    IMS = pss.H(Psm.sum(axis=2)) + Hy - pss.H(Psm)
    IMF = math.log2(nf * nm) + Hy - pss.H(P)
    return IMS, IMF


def surface(pool, psi, S, gammas, ranks, p, want_extra=False):
    keys = ("HFgY", "IFY", "IXY", "Hy", "IMS", "IMF", "chi_out")
    R = {k: np.zeros((len(gammas), len(ranks))) for k in keys}
    for i, g in enumerate(gammas):
        rho = out_states(pool, psi, float(g), p)
        if want_extra:
            R["chi_out"][i, :] = holevo_block(rho.mean(axis=1))
        for j, r in enumerate(ranks):
            c = pss.joint_law_nested(rho, r)
            s = pss.shares(c)
            R["HFgY"][i, j], R["IFY"][i, j], R["IXY"][i, j], R["Hy"][i, j] = s["HFgY"], s["IFY"], s["IXY"], s["Hy"]
            if want_extra:
                R["IMS"][i, j], R["IMF"][i, j] = I_label_Y(c, S)
    return R


def chi_in(psi):
    sig = np.einsum("fma,fmb->fab", psi, psi.conj()) / 2
    return holevo_block(sig)


def I_S_F(S):
    _, cnt = np.unique(S, return_counts=True)
    return pss.H(cnt / cnt.sum())


# ---------------------------------------------------------------------------
# Statistics (pure numpy)
# ---------------------------------------------------------------------------

def signflip_p(X, B, rng):
    """Two-sided sign-flip permutation p-values for mean(X[:, j]) = 0. X: (K, J)."""
    X = np.atleast_2d(X.T).T
    K = X.shape[0]
    obs = np.abs(X.mean(axis=0))
    sg = rng.choice([-1.0, 1.0], size=(B, K))
    null = np.abs(sg @ X) / K                       # (B, J)
    return (1 + (null >= obs[None, :] - 1e-15).sum(axis=0)) / (B + 1)


def holm(pv):
    pv = np.asarray(pv, float)
    order = np.argsort(pv)
    m = len(pv)
    adj = np.empty(m)
    run = 0.0
    for k, idx in enumerate(order):
        run = max(run, (m - k) * pv[idx])
        adj[idx] = min(1.0, run)
    return adj


def boot_ci(x, B, rng):
    x = np.asarray(x, float)
    idx = rng.integers(0, len(x), size=(B, len(x)))
    m = x[idx].mean(axis=1)
    return float(np.quantile(m, 0.025)), float(np.quantile(m, 0.975))


def pearson(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    if a.std() < 1e-15 or b.std() < 1e-15:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


# ---------------------------------------------------------------------------
# Self-checks
# ---------------------------------------------------------------------------

def self_checks(pool, V):
    p = 0.73
    psi_b, _ = inputs("blind", pool, V)
    # blind reproduces procedural_share_surface (half encoding)
    rho_ref = pss.output_states(pool, 0.3, p, pss.ENCODINGS["half"])
    assert np.allclose(out_states(pool, psi_b, 0.3, p), rho_ref, atol=1e-12)
    # eigen: U_f acts as a phase -> output = GAD(input)
    psi_e, _ = inputs("eigen", pool, V)
    K = pss.two_qubit_gad_kraus(0.3, p)
    direct = np.array([[pss.apply_kraus(K, np.outer(v, v.conj())) for v in pf] for pf in psi_e])
    assert np.allclose(out_states(pool, psi_e, 0.3, p), direct, atol=1e-10)
    # readable: output = GAD(|m b_f>)
    psi_r, S_r = inputs("readable", pool, V)
    o = out_states(pool, psi_r, 0.0, p)
    for f in range(3):
        assert np.isclose(np.real(o[f, 1, 2 + S_r[f], 2 + S_r[f]]), 1.0)
    # gphase identical to blind
    psi_g, _ = inputs("gphase", pool, V)
    assert np.allclose(out_states(pool, psi_g, 0.4, p), out_states(pool, psi_b, 0.4, p), atol=1e-12)


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def z(M):
    return np.where(np.abs(M) < 5e-10, 0.0, M) + 0.0


def table(title, gammas, ranks, M, md=False, nd=3, cells=None):
    M = z(M)
    if md:
        lines = [f"**{title}**", "", "| \\(g\\) | " + " | ".join(f"r={r}" for r in ranks) + " |",
                 "|---|" + "---|" * len(ranks)]
        for i, g in enumerate(gammas):
            row = cells[i] if cells is not None else [f"{v:.{nd}f}" for v in M[i]]
            lines.append(f"| {g:.1f} | " + " | ".join(row) + " |")
        return "\n".join(lines) + "\n"
    lines = [title, "  g     " + "".join(f"  r={r:<6d}" for r in ranks)]
    for i, g in enumerate(gammas):
        row = cells[i] if cells is not None else [f"{v:8.{nd}f}" for v in M[i]]
        lines.append(f"  {g:4.2f}  " + "".join(f"  {c:>8s}" for c in row))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--variants", type=str, default=",".join(VARIANTS))
    ap.add_argument("--seed", type=int, default=2026, help="canonical pool seed")
    ap.add_argument("--seeds", type=int, default=40, help="ensemble pool draws (seeds 1..K)")
    ap.add_argument("--pool", type=int, default=50)
    ap.add_argument("--T", type=float, default=1.0, help="bath temperature; 0 = plain AD")
    ap.add_argument("--no-robust-T", action="store_true", help="skip the T = 0, inf aggregate re-tests")
    ap.add_argument("--gammas", type=str, default="0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0")
    ap.add_argument("--ranks", type=str, default="2,4,8,16")
    ap.add_argument("--flips", type=int, default=20000, help="sign-flip permutations")
    ap.add_argument("--boot", type=int, default=10000, help="bootstrap resamples")
    ap.add_argument("--markdown", action="store_true", help="print tables as Markdown")
    args = ap.parse_args()
    t0 = time.time()

    variants = [v for v in args.variants.split(",") if v]
    assert all(v in VARIANTS for v in variants), f"variants must be among {VARIANTS}"
    ranks = [int(r) for r in args.ranks.split(",")]
    gammas = np.array([float(g) for g in args.gammas.split(",")])
    nontriv = gammas < 1 - 1e-12
    md = args.markdown

    # ---- pools first (canonical + ensemble), hashed before any noise ----
    pool, V, h0 = draw_all(args.pool, args.seed)
    ens = [draw_all(args.pool, s) for s in range(1, args.seeds + 1)]
    self_checks(pool, V)
    assert all_hash(pool, V) == h0

    # ---- noise defined only now ----
    p = ps.p_of_T(args.T)
    print("TOY MODEL: informed-input procedural share (two qubits, GAD per qubit). Proof-of-concept")
    print("only; NOT evidence about hadronic or QCD physics. No physical claim is drawn.")
    print(f"canonical pool seed {args.seed} (pool+V sha256 {h0[:16]}...), ensemble seeds 1..{args.seeds}; "
          f"p = {p:.4f} (T = {ps.T_of_p(p):.4g}); log2|pool| = {math.log2(args.pool):.4f}")

    # ---- canonical pool: exact surfaces ----
    psi_b, S_b = inputs("blind", pool, V)
    Rb = surface(pool, psi_b, S_b, gammas, ranks, p, want_extra=True)
    print("\n" + table(f"H(F|Y) BLIND [canonical pool, T={args.T:g}]", gammas, ranks, Rb["HFgY"], md))
    canon = {}
    for v in variants:
        psi, S = inputs(v, pool, V)
        R = surface(pool, psi, S, gammas, ranks, p, want_extra=True)
        gap = Rb["HFgY"] - R["HFgY"]
        ci, isf = chi_in(psi), I_S_F(S)
        canon[v] = dict(R=R, gap=gap, chi_in=ci)
        print(f"\n===== {v}: {LABELS[v]} =====")
        print(f"  chi_in (Holevo F:input block) = {z(ci):.4f} bits; I(S;F) classical hint = {z(isf):.4f} bits")
        if md:
            cells = [[f"{z(R['HFgY'][i, j]):.3f} / {z(gap[i, j]):+.4f}" for j in range(len(ranks))]
                     for i in range(len(gammas))]
            print(table(f"{v}: H(F|Y) informed / gap [canonical pool, T={args.T:g}]", gammas, ranks,
                        gap, md, cells=cells))
        else:
            print(table(f"H(F|Y) INFORMED [{v}]", gammas, ranks, R["HFgY"], md))
            print(table(f"gap = H(F|Y)_blind - H(F|Y)_{v} [canonical pool]", gammas, ranks, gap, md, nd=4))
        # bounds
        lo = -Rb["IFY"]
        hi = np.minimum(np.log2(np.array(ranks))[None, :], math.log2(args.pool)) - Rb["IFY"]
        ok_g = bool(((gap >= lo - TOL) & (gap <= hi + TOL)).all())
        hol = bool((R["IFY"] <= R["chi_out"] + 1e-9).all())
        le_chi = int((gap <= ci + TOL).sum())
        print(f"  guaranteed: -I(F;Y)_blind <= gap <= min(log2 r, log2|pool|) - I(F;Y)_blind: {ok_g}; "
              f"I(F;Y) <= chi_out (Holevo): {hol}")
        print(f"  not guaranteed: gap <= chi_in at {le_chi}/{gap.size} points")
        dg = np.diff(gap[nontriv], axis=0) if nontriv.sum() > 1 else np.zeros((0, len(ranks)))
        dr = np.diff(gap[nontriv], axis=1)
        print(f"  gap monotone non-increasing in g at {int((np.diff(gap, axis=0) <= TOL).sum())}/"
              f"{(len(gammas) - 1) * len(ranks)} g-steps; non-decreasing in rank at "
              f"{int((dr >= -TOL).sum())}/{dr.size} rank-steps (g<1); gap at g=1: max |.| = "
              f"{np.abs(gap[~nontriv]).max() if (~nontriv).any() else float('nan'):.1e}")
        bs_M = int((R["IXY"] + R["IFY"] <= R["Hy"] + TOL).sum())
        bs_MS = int((R["IMS"] + R["IFY"] <= R["Hy"] + TOL).sum())
        bs_hold = bool((R["IMF"] <= R["Hy"] + TOL).all())
        print(f"  balance sheet: X=M: I(X;Y)+I(F;Y)<=H(Y) {bs_M}/{gap.size} (theorem); "
              f"X=(M,S): {bs_MS}/{gap.size} (not a theorem); I(X,F;Y)<=H(Y): {bs_hold}")
        assert all_hash(pool, V) == h0, "pool changed"

    # ---- ensemble test over pool draws ----
    def ensemble(pT):
        G = {v: [] for v in variants}
        CHI = {v: [] for v in variants}
        IB = []
        for (pl, VV, hh) in ens:
            pb, sb = inputs("blind", pl, VV)
            hb = surface(pl, pb, sb, gammas, ranks, pT)["HFgY"]
            IB.append(math.log2(args.pool) - hb)
            for v in variants:
                pv, sv = inputs(v, pl, VV)
                G[v].append(hb - surface(pl, pv, sv, gammas, ranks, pT)["HFgY"])
                CHI[v].append(chi_in(pv))
            assert all_hash(pl, VV) == hh, "ensemble pool changed"
        return ({v: np.array(G[v]) for v in variants}, {v: np.array(CHI[v]) for v in variants},
                np.array(IB))

    def report(pT, Tlab, full):
        rng = np.random.default_rng(12345)
        G, CHI, IB = ensemble(pT)
        tested = [v for v in variants if v in TESTED]
        agg = {v: G[v][:, nontriv, :].reshape(len(ens), -1).mean(axis=1) for v in variants}
        praw = {v: float(signflip_p(agg[v][:, None], args.flips, rng)[0]) for v in tested}
        padj = dict(zip(tested, holm([praw[v] for v in tested]))) if tested else {}
        print(f"\n===== ENSEMBLE TEST over {len(ens)} independent pool draws, T = {Tlab} =====")
        print("  randomness: pool draw (U_f and V_f); paired blind vs informed on each pool.")
        print("  H0: E_pool[gap] = 0. Aggregate = per-seed mean gap over the g<1 grid; two-sided sign-flip,")
        print(f"  Holm across {len(tested)} tested variants; per-point sign-flip with Holm across "
              f"{int(nontriv.sum()) * len(ranks)} points.")
        hdr = f"  {'variant':9s} {'mean gap':>9s} {'95% CI':>21s} {'p':>8s} {'p_Holm':>8s} {'pts+':>5s} {'pts-':>5s} {'chi_in':>7s} {'r(chi,gap)':>10s}  verdict"
        ib = IB[:, nontriv, :].reshape(len(ens), -1).mean(axis=1)
        print(f"  scale: blind I(F;Y) averaged over the g<1 grid = {ib.mean():.4f} bits (seed mean; "
              f"range {ib.min():.4f}-{ib.max():.4f})")
        print(hdr)
        out = {}
        for v in variants:
            m = float(agg[v].mean())
            if v == "gphase":
                print(f"  {v:9s} {m:9.2e} {'(exact zero)':>21s} {'-':>8s} {'-':>8s} {'-':>5s} {'-':>5s} "
                      f"{CHI[v].mean():7.3f} {'-':>10s}  exactly zero (null control)")
                continue
            lo, hi = boot_ci(agg[v], args.boot, rng)
            Xp = G[v][:, nontriv, :].reshape(len(ens), -1)
            pp = holm(signflip_p(Xp, args.flips, rng))
            mp = Xp.mean(axis=0)
            npos, nneg = int(((pp < 0.05) & (mp > 0)).sum()), int(((pp < 0.05) & (mp < 0)).sum())
            zero = padj[v] > 0.05
            verdict = "CONSISTENT WITH ZERO" if zero else ("gap > 0" if m > 0 else "gap < 0")
            out[v] = dict(mean=m, ci=(lo, hi), p=praw[v], padj=padj[v], npos=npos, nneg=nneg, zero=zero,
                          meanmap=G[v].mean(axis=0), ppmap=pp, chi=float(CHI[v].mean()))
            print(f"  {v:9s} {m:9.4f} [{lo:9.4f},{hi:9.4f}] {praw[v]:8.1e} {padj[v]:8.1e} {npos:5d} {nneg:5d} "
                  f"{CHI[v].mean():7.3f} {pearson(CHI[v], agg[v]):10.3f}  {verdict}")
        st = [v for v in STRUCTURAL if v in out and "rand" in out]
        if st:
            d = {v: agg[v] - agg["rand"] for v in st}
            pr = [float(signflip_p(d[v][:, None], args.flips, rng)[0]) for v in st]
            pa = holm(pr)
            print("  structure vs structureless-label control (gap_variant - gap_rand, aggregate; Holm across "
                  f"{len(st)}):")
            for v, p_, pa_ in zip(st, pr, pa):
                lo, hi = boot_ci(d[v], args.boot, rng)
                print(f"    {v:8s} mean {d[v].mean():+.4f} [{lo:+.4f},{hi:+.4f}] p {p_:.1e} p_Holm {pa_:.1e}"
                      f"  {'no detectable structure effect' if pa_ > 0.05 else 'DIFFERS from rand'}")
        if full:
            for v, o in out.items():
                cells = []
                k = 0
                pmap = np.ones((len(gammas), len(ranks)))
                pmap[nontriv] = o["ppmap"].reshape(int(nontriv.sum()), len(ranks))
                for i in range(len(gammas)):
                    row = []
                    for j in range(len(ranks)):
                        mk = "*" if pmap[i, j] < 0.05 else ""
                        row.append(f"{z(o['meanmap'][i, j]):+.4f}{mk}")
                    cells.append(row)
                print(table(f"ensemble mean gap [{v}, T={Tlab}] (* = Holm-adjusted per-point p < 0.05)",
                            gammas, ranks, o["meanmap"], md, cells=cells))
        return out

    report(p, f"{args.T:g}", full=True)
    if not args.no_robust_T:
        for Tr in (0.0, math.inf):
            if abs(ps.p_of_T(Tr) - p) > 1e-12:
                report(ps.p_of_T(Tr), f"{Tr:g}", full=False)

    assert all_hash(pool, V) == h0
    print(f"\ncanonical pool+V sha256 unchanged: {h0[:16]}...; runtime {time.time() - t0:.0f} s")
    print("TOY MODEL; no physics claim is drawn (not evidence about hadronic or QCD physics).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
