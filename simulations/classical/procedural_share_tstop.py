#!/usr/bin/env python3
"""Tier 2 toy model (proof-of-concept): stopping-time sweep of the
energy-bounded (Margolus-Levitin) candidate pool.

    *** TOY MODEL. Proof-of-concept for the shape of a curve in a two-qubit
    *** toy. It is NOT evidence about hadronic or QCD physics and makes no
    *** physical claim of any kind. "Energy budget" and "Margolus-Levitin
    *** time" are used in their textbook finite-dimensional sense only.

The pool-generation criterion of CE-12 / CE-15 is held fixed (same 200
Hamiltonians, budget, eps clustering, noiseless law) except for the
stopping time: U = exp(-i H t) with t = tfrac * t_ML, tfrac in {1, 2, 4, 8}.
The sampler (sample_unitaries), leader_cluster, noiseless_law and every
share function are imported from procedural_share_mlpool.py and are not
modified. This is a parameter sweep, not a rewrite.

Question: does the bound's survival rate depend on sitting exactly at the
ML time, or does it hold for slower evolutions too?

Run:

    python simulations/classical/procedural_share_tstop.py              # defaults (~2-4 min)
    python simulations/classical/procedural_share_tstop.py --seeds 0    # canonical + CE-6 only
    python simulations/classical/procedural_share_tstop.py --markdown

No pool JSON is written: every pool regenerates from the seed. At tfrac=1
the two-qubit pool is bit-identical to simulations/classical/data/ce15_ml_pool.json
(sha256 d11fa3d1...) and the CE-6 one-bit counts reproduce 38/81.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import procedural_share as ps  # noqa: E402
import procedural_share_informed as pin  # noqa: E402
import procedural_share_mlpool as ml  # noqa: E402
import procedural_share_surface as pss  # noqa: E402

TFRACS = (1, 2, 4, 8)
EXPECTED_1X_SHA = "d11fa3d1ec4594b7d1235759fde33b8b98689646b44efd163fffba97084618e2"


# ---------------------------------------------------------------------------
# CE-6 driver (same loop as ml.ce6_overlap; takes an explicit candidate list
# so procedural_share_mlpool.py is not modified).
# ---------------------------------------------------------------------------

def ce6_on_pool(pool, eps=0.05, dg=0.05, dp=0.05):
    """CE-6 one-bit run, variant (a), on a given 50-candidate pool (name, q0, q1)."""
    ps.USES = 1
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


def ce6_summary(rows):
    fails = [r for r in rows if r["deficit"] > 1e-12]
    corr = sum(r["slack"] >= -1e-12 for r in rows)
    d = np.array([r["deficit"] for r in fails]) if fails else np.array([np.nan])
    return dict(defined=len(rows), orig_fail=len(fails), corr_hold=corr,
                med_def=float(np.median(d)), min_def=float(np.min(d)), max_def=float(np.max(d)),
                fail_keys=frozenset((r["g"], r["p"]) for r in fails),
                def_keys=frozenset((r["g"], r["p"]) for r in rows))


def tv_law(A, B):
    """max_m TV between paired laws, shape (n,) from (n, m, y) arrays."""
    return 0.5 * np.abs(A - B).sum(axis=2).max(axis=1)


def ident_law(n):
    L = np.zeros((n, 2, 4))
    L[:, 0, 0] = 1.0
    L[:, 1, 2] = 1.0
    return L


def true_spectra(n, seed, budget, ref):
    """Rescaled eigenvalues of the n Hamiltonians drawn by sample_unitaries (same RNG)."""
    rng = np.random.default_rng([seed, ml.TAG])
    rho = ml.ref_state(ref)
    ev = np.empty((n, 4))
    i = 0
    while i < n:
        A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        Hm = (A + A.conj().T) / 2
        w, v = np.linalg.eigh(Hm)
        w = w - w[0]
        if np.min(np.diff(w)) < 1e-9 * max(w[-1], 1e-300):
            continue
        E = float(np.real(np.einsum("ij,ji->", rho, (v * w) @ v.conj().T)))
        ev[i] = w * (budget / E)
        i += 1
    return ev


def surface_pack(pool, p, gammas, ranks, bases):
    """Blind + informed surfaces for all four (channel, readout) configs."""
    K = len(pool)
    psi_b = ml.blind_inputs(K)
    psi_i, S_i = pin.inputs("readable", np.asarray(pool), None)
    configs = [("gad", "nested"), ("gad", "random"), ("dephasing", "nested"), ("dephasing", "random")]
    out = {}
    for ch, ro in configs:
        Rb = ml.surface(pool, psi_b, None, ch, p, gammas, ranks, ro, bases)
        Ri = ml.surface(pool, psi_i, S_i, ch, p, gammas, ranks, ro, bases)
        out[(ch, ro)] = (Rb, Ri)
    return out


def pack_counts(pack):
    rows = {}
    for (ch, ro), (Rb, Ri) in pack.items():
        cb, ob, _, n = ml.pass_counts(Rb)
        ci, oi, vi, _ = ml.pass_counts(Ri)
        defb = (Rb["IXY"] + Rb["HFgY"] - Rb["Hy"]).ravel()
        fb = defb > 1e-12
        defi = (Ri["IXY"] + Ri["HFgY"] - Ri["Hy"]).ravel()
        fi = defi > 1e-12
        rows[(ch, ro)] = dict(
            n=n, blind_corr=cb, blind_orig_fail=n - ob,
            blind_med_def=float(np.median(defb[fb])) if fb.any() else 0.0,
            inf_corr=ci, inf_orig_fail=n - oi, inf_ovl=vi,
            inf_med_def=float(np.median(defi[fi])) if fi.any() else 0.0,
            max_IXFgY_blind=float(Rb["IXFgY"].max()),
            IFY_g0_r16=float(Rb["IFY"][0, -1]),
            IXY_g0_r16=float(Rb["IXY"][0, -1]),
            HFgY_g0_r16=float(Rb["HFgY"][0, -1]),
            ident=float(max(np.abs(Rb["ident"]).max(), np.abs(Ri["ident"]).max())),
        )
    return rows


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--budget", type=float, default=1.0)
    ap.add_argument("--ref", choices=("blind", "mixed"), default="blind")
    ap.add_argument("--eps", type=float, default=0.05)
    ap.add_argument("--n-samples", type=int, default=200)
    ap.add_argument("--seeds", type=int, default=40, help="ensemble draws 1..seeds (0 = skip)")
    ap.add_argument("--canonical", type=int, default=2026)
    ap.add_argument("--T", type=float, default=1.0)
    ap.add_argument("--dg", type=float, default=0.1)
    ap.add_argument("--flips", type=int, default=20000)
    ap.add_argument("--boot", type=int, default=10000)
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()
    t0 = time.time()
    p = ps.p_of_T(args.T) if args.T > 0 else 1.0
    gammas = np.round(np.arange(0, 1 + args.dg / 2, args.dg), 10)
    ranks = ml.RANKS
    S2 = ml.STAGE2_SETTINGS
    use_canonical_settings = (
        args.canonical == S2["seed"] and args.n_samples == S2["n_samples"]
        and args.eps == S2["eps"] and args.budget == S2["budget"] and args.ref == S2["ref"]
    )

    print("TOY MODEL (Tier 2). Two-qubit proof-of-concept; NOT evidence about hadronic or QCD physics;")
    print("no physical claim. 'Energy budget' / 'ML time' are textbook finite-dimensional notions only.\n")
    ml.self_checks()
    print("Self-checks passed (imported from procedural_share_mlpool.py).\n")
    print(f"Settings: budget={args.budget} tfracs={list(TFRACS)} ref={args.ref} eps={args.eps} "
          f"n_samples={args.n_samples} canonical={args.canonical} T={args.T} (p={p:.4f}) dg={args.dg}")
    print("Sampler, clustering, noiseless law and share functions: procedural_share_mlpool.py, reused by import.")
    print("No pool JSON written; pools regenerate from the seed.\n")

    # ---- sample the same Hamiltonians at each stopping time ----
    Us, rej = {}, {}
    for tf in TFRACS:
        U, r = ml.sample_unitaries(args.n_samples, args.canonical, args.budget, float(tf), args.ref)
        Us[tf], rej[tf] = U, r
        assert r == 0
        assert np.allclose(np.einsum("nab,ncb->nac", U, U.conj()), np.eye(4)[None], atol=1e-12)

    # U(k) = U(1)^k (same Hamiltonians)
    for tf in TFRACS:
        if tf == 1:
            continue
        Pk = Us[1].copy()
        for _ in range(tf - 1):
            Pk = Pk @ Us[1]
        err = float(np.abs(Us[tf] - Pk).max())
        assert err < 1e-12, f"U({tf}) != U(1)^{tf}: {err}"
        print(f"U({tf}) = U(1)^{tf}: max abs error {err:.1e}")

    # tfrac=1 reproduces the saved Stage 2 pool
    pool = {}
    laws = {}
    reps = {}
    hsh = {}
    for tf in TFRACS:
        laws[tf] = ml.noiseless_law(Us[tf])
        reps[tf] = ml.leader_cluster(laws[tf], args.eps)
        P = np.ascontiguousarray(Us[tf][reps[tf]])
        P.setflags(write=False)
        pool[tf] = P
        hsh[tf] = pss.pool_hash(P)
        # ml_pool must agree
        assert np.array_equal(P, ml.ml_pool(args.canonical, args.n_samples, args.eps,
                                            args.budget, float(tf), args.ref))

    if use_canonical_settings:
        saved, rec = ml.load_pool()
        assert rec["pool_sha256"] == EXPECTED_1X_SHA
        assert np.array_equal(pool[1], saved) and hsh[1] == rec["pool_sha256"]
        assert np.array_equal(pool[1], saved)  # bit-identical
        print(f"tfrac=1 two-qubit pool is bit-identical to ce15_ml_pool.json "
              f"(sha256 {hsh[1][:16]}…; {rec['n_clusters']} representatives, 0 rejected).")
    else:
        print("Non-default settings: skipped the saved-pool identity check.")

    # ---- pool sizes and distinctness ----
    print("\n## Pool sizes and distinctness (canonical Hamiltonians, eps clustering fixed)\n")
    print("| tfrac | t / t_ML | representatives | H(F) (bits) | rejected | first-20 rep indices | sha256 (first 16) |")
    print("|---|---|---|---|---|---|---|")
    for tf in TFRACS:
        idx20 = reps[tf][:20]
        same20 = idx20 == list(range(20))
        print(f"| {tf} | {tf} | {len(pool[tf])} | {math.log2(len(pool[tf])):.3f} | {rej[tf]} | "
              f"{'0-19' if same20 else idx20} | {hsh[tf][:16]} |")
    print()
    assert all(hsh[a] != hsh[b] for i, a in enumerate(TFRACS) for b in TFRACS[i+1:]), \
        "two tfracs produced the same pool hash"

    # merges at each tfrac
    print("Cluster merges (samples that joined an earlier representative):")
    for tf in TFRACS:
        dropped = [i for i in range(args.n_samples) if i not in reps[tf]]
        if not dropped:
            print(f"- tfrac={tf}: none (every sample is a representative).")
            continue
        lines = []
        for i in dropped:
            d = tv_law(laws[tf][i][None], laws[tf][reps[tf]])
            j = int(np.argmin(d))
            lines.append(f"sample {i} joins rep {reps[tf][j]} (TV {d[j]:.4f})")
        print(f"- tfrac={tf}: {len(dropped)} merge(s): " + "; ".join(lines) + ".")

    print("\nSame-Hamiltonian TV between noiseless laws (min / median / mean / max; fraction <= eps; fraction 0):\n")
    print("| pair | min | median | mean | max | frac <= eps | frac = 0 |")
    print("|---|---|---|---|---|---|---|")
    pairs = [(2, 1), (4, 1), (8, 1), (4, 2), (8, 2), (8, 4)]
    for a, b in pairs:
        d = tv_law(laws[a], laws[b])
        print(f"| {a}x vs {b}x | {d.min():.4f} | {np.median(d):.4f} | {d.mean():.4f} | {d.max():.4f} | "
              f"{(d <= args.eps + 1e-15).mean():.3f} | {(d <= 1e-12).mean():.3f} |")

    print("\nTV of each sample's noiseless law to the identity law; mean fidelity |<m0|U|m0>|^2:\n")
    print("| tfrac | TV vs I: min / median / max | # within eps of I | mean fidelity |")
    print("|---|---|---|---|")
    LI = ident_law(args.n_samples)
    for tf in TFRACS:
        d = tv_law(laws[tf], LI)
        fid = float((np.abs(np.einsum("nii->ni", Us[tf])[:, [0, 2]]) ** 2).mean())
        print(f"| {tf} | {d.min():.4f} / {np.median(d):.4f} / {d.max():.4f} | "
              f"{int((d <= args.eps + 1e-15).sum())}/{args.n_samples} | {fid:.4f} |")

    # phase wrapping from the true rescaled spectra (same RNG as the sampler)
    ev = true_spectra(args.n_samples, args.canonical, args.budget, args.ref)
    print(f"\nRescaled spectra (E0=0, <E-E0>_ref = {args.budget}): E_max min/median/mean/max = "
          f"{ev[:, -1].min():.3f}/{np.median(ev[:, -1]):.3f}/{ev[:, -1].mean():.3f}/{ev[:, -1].max():.3f}.")
    print("Phase distance of excited eigenvalues to 2πℤ (the ground state is always at phase 0):\n")
    print("| tfrac | median dist (rad) | frac < 0.1 rad | Hamiltonians with an excited wrap < 0.1 rad |")
    print("|---|---|---|---|")
    for tf in TFRACS:
        theta = ev * tf * math.pi / (2 * args.budget)
        wrap = np.minimum(np.mod(theta, 2 * math.pi), 2 * math.pi - np.mod(theta, 2 * math.pi))
        wrap_ex = wrap[:, 1:]
        n_h = int((wrap_ex < 0.1).any(axis=1).sum())
        print(f"| {tf} | {np.median(wrap_ex):.4f} | {(wrap_ex < 0.1).mean():.3f} | {n_h}/{args.n_samples} |")
    print("\nAt tfrac=4, t = 2π/B, so an eigenstate at the reference energy E=B returns to itself. "
          "That is a wrap of one part of the spectrum, not of the unitary: E_max reaches "
          f"{ev[:, -1].max():.3f}, so other eigenstates do not come back with it. "
          "The 2x/4x/8x pools are not degenerate with 1x or with the identity (tables above).")

    # ---- canonical two-qubit surfaces ----
    print("\n## Two-qubit surfaces (canonical draw, same grid as CE-12: g = 0(0.1)1, ranks 2/4/8/16)\n")
    bases = pss.random_readouts(ranks, args.canonical)
    packs = {}
    counts = {}
    for tf in TFRACS:
        packs[tf] = surface_pack(pool[tf], p, gammas, ranks, bases)
        counts[tf] = pack_counts(packs[tf])
        assert pss.pool_hash(pool[tf]) == hsh[tf], "pool changed during sweep"

    print("Blind inputs. Corrected bound I(X;Y)+I(F;Y) ≤ H(Y) and original form I(X;Y)+H(F|Y) ≤ H(Y). "
          "Median deficit is H(F|Y)−H(Y|X) at the original-form failures.\n")
    print("| tfrac | |pool| | channel | readout | corrected holds | original fails | median deficit (bits) | I(F;Y) at g=0,r=16 | I(X;Y) at g=0,r=16 |")
    print("|---|---|---|---|---|---|---|---|---|")
    for tf in TFRACS:
        for ch, ro in counts[tf]:
            r = counts[tf][(ch, ro)]
            print(f"| {tf} | {len(pool[tf])} | {ch} | {ro} | {r['blind_corr']}/{r['n']} | "
                  f"{r['blind_orig_fail']}/{r['n']} | {r['blind_med_def']:.3f} | "
                  f"{r['IFY_g0_r16']:.3f} | {r['IXY_g0_r16']:.3f} |")

    print("\nInformed (readable) inputs. The corrected bound is not a theorem here; the overlap-corrected bound is.\n")
    print("| tfrac | channel | readout | corrected holds | original fails | overlap-corrected holds | median orig. deficit | max \\|identity residual\\| |")
    print("|---|---|---|---|---|---|---|---|")
    for tf in TFRACS:
        for ch, ro in counts[tf]:
            r = counts[tf][(ch, ro)]
            print(f"| {tf} | {ch} | {ro} | {r['inf_corr']}/{r['n']} | {r['inf_orig_fail']}/{r['n']} | "
                  f"{r['inf_ovl']}/{r['n']} | {r['inf_med_def']:.3f} | {r['ident']:.1e} |")

    # ---- CE-6 one-bit pool A-ml per tfrac ----
    print("\n## CE-6 one-bit run on pool A-ml, per stopping time\n")
    print("Pool A-ml = 30 non-Haar members of CE-6 pool A plus the one-bit laws of the first 20 "
          "ML representatives (draw order), size 50. Same construction as CE-15; only tfrac changes.\n")
    ce6 = {}
    for tf in TFRACS:
        rec = ml.pool_record(args.canonical, args.n_samples, args.eps, args.budget, float(tf), args.ref)
        # the two-qubit pool in the record must match what we already have
        a = np.array(rec["pool"], dtype=float)
        rec_pool = a[..., 0] + 1j * a[..., 1]
        assert np.allclose(rec_pool, pool[tf], atol=0, rtol=0)
        cand = ml.pool_A_ml(rec)
        assert len(cand) == 50
        ce6[tf] = ce6_on_pool(cand)
        if tf == 1 and use_canonical_settings:
            # reproduce ce6_overlap on the saved pool, and the 38/81 counts
            ref = ml.ce6_overlap(pool_source="ml")
            for inp in ("uniform", "capacity"):
                assert len(ce6[1][inp]) == len(ref[inp])
                for a, b in zip(ce6[1][inp], ref[inp]):
                    assert a["g"] == b["g"] and a["p"] == b["p"] and a["k"] == b["k"]
                    assert abs(a["deficit"] - b["deficit"]) < 1e-14
            su = ce6_summary(ce6[1]["uniform"])
            assert su["defined"] == 81 and su["orig_fail"] == 38 and su["corr_hold"] == 81
            assert abs(su["med_def"] - 2.807) < 0.0005
            print("tfrac=1 CE-6 run matches ce6_overlap(pool_source='ml') and the documented 38/81 "
                  f"(median deficit {su['med_def']:.3f} bits).\n")

    print("| tfrac | input | defined pts | original fails | corrected holds | deficit min / median / max (bits) | failures also failing at 1x | defined also defined at 1x |")
    print("|---|---|---|---|---|---|---|---|")
    base = {inp: ce6_summary(ce6[1][inp]) for inp in ("uniform", "capacity")}
    for tf in TFRACS:
        for inp in ("uniform", "capacity"):
            s = ce6_summary(ce6[tf][inp])
            both_f = len(s["fail_keys"] & base[inp]["fail_keys"])
            both_d = len(s["def_keys"] & base[inp]["def_keys"])
            print(f"| {tf} | {inp} | {s['defined']} | {s['orig_fail']} | {s['corr_hold']}/{s['defined']} | "
                  f"{s['min_def']:.3f} / {s['med_def']:.3f} / {s['max_def']:.3f} | "
                  f"{both_f}/{s['orig_fail']} | {both_d}/{s['defined']} |")

    # ---- ensemble ----
    if args.seeds <= 0:
        print(f"\nDone in {time.time() - t0:.0f}s. TOY MODEL: no physical claim.")
        return 0

    print(f"\n## Ensemble: {args.seeds} independent draws (seeds 1..{args.seeds}), same Hamiltonians per draw at each tfrac\n")
    configs = [("gad", "nested"), ("gad", "random"), ("dephasing", "nested"), ("dephasing", "random")]
    # per-draw records
    sizes = {tf: [] for tf in TFRACS}
    recs = {(tf, c, "blind"): [] for tf in TFRACS for c in configs}
    recs.update({(tf, c, "inf"): [] for tf in TFRACS for c in configs})
    share = {(tf, c, k): [] for tf in TFRACS for c in configs for k in ("norm", "IFY")}
    for s in range(1, args.seeds + 1):
        bases_s = None
        for tf in TFRACS:
            pl = ml.ml_pool(s, args.n_samples, args.eps, args.budget, float(tf), args.ref)
            hs = pss.pool_hash(pl)
            sizes[tf].append(len(pl))
            if bases_s is None:
                bases_s = pss.random_readouts(ranks, s)
            pack = surface_pack(pl, p, gammas, ranks, bases_s)
            assert pss.pool_hash(pl) == hs
            cnt = pack_counts(pack)
            for c in configs:
                recs[(tf, c, "blind")].append((cnt[c]["blind_corr"], cnt[c]["blind_orig_fail"],
                                               cnt[c]["blind_med_def"], cnt[c]["n"]))
                recs[(tf, c, "inf")].append((cnt[c]["inf_corr"], cnt[c]["inf_orig_fail"],
                                             cnt[c]["inf_ovl"], cnt[c]["n"]))
                Rb = pack[c][0]
                share[(tf, c, "norm")].append(Rb["norm"])
                share[(tf, c, "IFY")].append(Rb["IFY"])

    print("Pool sizes over draws:\n")
    print("| tfrac | min | median | max |")
    print("|---|---|---|---|")
    for tf in TFRACS:
        a = np.array(sizes[tf])
        print(f"| {tf} | {a.min()} | {int(np.median(a))} | {a.max()} |")

    print("\nBlind pass counts summed over draws (holds or fails / points). Each draw is a 11×4 grid (44 points).\n")
    print("| tfrac | channel | readout | corrected holds | original fails | mean median-deficit (bits) |")
    print("|---|---|---|---|---|---|")
    orig_constant = True
    for tf in TFRACS:
        for c in configs:
            rows = recs[(tf, c, "blind")]
            ch, n = sum(r[0] for r in rows), sum(r[3] for r in rows)
            of = sum(r[1] for r in rows)
            md = float(np.mean([r[2] for r in rows]))
            if of != n:
                orig_constant = False
            print(f"| {tf} | {c[0]} | {c[1]} | {ch}/{n} | {of}/{n} | {md:.3f} |")

    print("\nInformed (readable) pass counts summed over draws:\n")
    print("| tfrac | channel | readout | corrected holds | original fails | overlap-corrected holds |")
    print("|---|---|---|---|---|---|")
    for tf in TFRACS:
        for c in configs:
            rows = recs[(tf, c, "inf")]
            n = sum(r[3] for r in rows)
            print(f"| {tf} | {c[0]} | {c[1]} | {sum(r[0] for r in rows)}/{n} | "
                  f"{sum(r[1] for r in rows)}/{n} | {sum(r[2] for r in rows)}/{n} |")

    if orig_constant:
        n_pts = args.seeds * 44
        print(f"\nThe original form failed at every blind and informed grid point of every draw and every "
              f"tfrac ({n_pts} points per (channel, readout, tfrac) on each input). The corrected bound "
              f"held at every blind point. Those two counts do not depend on the stopping time in this ensemble.")

    # paired tests: share metrics, tfrac vs 1, plus informed corrected-hold counts where they vary
    rng = np.random.default_rng(99)
    # mask: nontrivial points, as in CE-12
    tests = []  # (label, diffs_per_draw)
    for c in configs:
        ch, ro = c
        mask = np.ones((len(gammas), len(ranks)), bool)
        if ch == "gad":
            mask[gammas >= 1 - 1e-12, :] = False
        if c == ("dephasing", "nested"):
            # flat in g; still a pool-dependent number, but one effective point. Keep, using all g.
            pass
        for metric, lab in (("norm", "H(F|Y)/H(F)"), ("IFY", "I(F;Y)")):
            m1 = np.array(share[(1, c, metric)])  # (seeds, g, r)
            for tf in (2, 4, 8):
                mt = np.array(share[(tf, c, metric)])
                D = mt - m1
                D[np.abs(D) < ml.ZERO] = 0.0
                d = D[:, mask].mean(axis=1)  # per-draw mean over nontrivial points
                tests.append((f"{ch}/{ro} {lab} {tf}x−1x", d, float(m1[:, mask].mean()), float(mt[:, mask].mean())))
    # informed corrected holds, configs where 1x is not 44/44 or any tfrac varies
    for c in configs:
        h1 = np.array([r[0] for r in recs[(1, c, "inf")]], dtype=float)
        vary = False
        for tf in (2, 4, 8):
            ht = np.array([r[0] for r in recs[(tf, c, "inf")]], dtype=float)
            if np.any(ht != h1) or np.any(h1 != 44):
                vary = True
        if not vary:
            continue
        for tf in (2, 4, 8):
            ht = np.array([r[0] for r in recs[(tf, c, "inf")]], dtype=float)
            d = ht - h1
            d[np.abs(d) < ml.ZERO] = 0.0
            tests.append((f"{c[0]}/{c[1]} informed corrected holds {tf}x−1x", d, float(h1.mean()), float(ht.mean())))

    pv = [pin.signflip_p(d[:, None], args.flips, rng)[0] for _, d, _, _ in tests]
    pa = pin.holm(pv)
    print(f"\n### Paired tests, tfrac vs 1x (mean over nontrivial points; {args.seeds} draws; "
          f"sign-flip {args.flips}, bootstrap 95% CI {args.boot}, Holm across {len(tests)} tests)\n")
    print("| comparison | 1x mean | tfrac mean | diff | 95% CI | p | p (Holm) | tfrac > 1x draws |")
    print("|---|---|---|---|---|---|---|---|")
    for (lab, d, m1, mt), pval, padj in zip(tests, pv, pa):
        lo, hi = pin.boot_ci(d, args.boot, rng)
        print(f"| {lab} | {m1:.4f} | {mt:.4f} | {d.mean():+.4f} | [{lo:+.4f}, {hi:+.4f}] | "
              f"{pval:.4f} | {padj:.4f} | {int((d > 0).sum())}/{len(d)} |")

    print(f"\nDone in {time.time() - t0:.0f}s. TOY MODEL: no physical claim.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
