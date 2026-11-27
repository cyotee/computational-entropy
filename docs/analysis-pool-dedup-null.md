# Candidate-pool de-duplication: the deficit-vs-set-size null (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model**.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim. All quantities are entropies or mutual informations in bits.

**Status:** 2026-11-26 · computed by re-evaluating existing code with one change to the candidate list. No new simulation design and no new simulation code in the repository. The run is the CE-6 one-bit computation, variant (a), uniform input, on pool A-ml ([procedural-share-mlpool.md](procedural-share-mlpool.md) §9; pool hash `d11fa3d1ec4594b7…`; ML pool at \(1\times t_{\rm ML}\)). The only change: each distinct noiseless one-bit law \((q_0,q_1)\) is kept once. Everything else is identical to the A-ml run:

- \(\varepsilon=0.05\); binary TV distance, maximised over the input \(x\); membership iff the distance is \(\le\varepsilon+10^{-12}\);
- the same \((g,p)\) grid;
- the same deficit \(D=I(X;Y)+H(F\mid Y)-H(Y)\) of the original form;
- \(F\) uniform on the class \(C_\varepsilon\), with \(k=\lvert C_\varepsilon\rvert\).

As a control, the un-de-duplicated pool still reproduces 38 failures of 81 defined points.

Earlier scratch analyses found that \(D\) correlates strongly with the class size \(k\) (Spearman 0.986 on A-ml). \(k\) was examined only as a computable proxy, a count of \(\varepsilon\)-consistent candidates. This note tests whether that correlation survives once duplicated laws are removed. Nothing here is a description-length or Kolmogorov-complexity claim.

**Verdict.** The deficit-versus-set-size correlation was a **construction artifact** of duplicated deterministic laws in the candidate pool. With each law kept once, no \(\varepsilon\)-class holds more than 2 distinct laws, and 31 of the 38 A-ml failures vanish. Every remaining failure has \(k=2\), so a correlation of \(D\) with \(k\) among failures is undefined. Across all defined points the association with \(k\) does not exceed what the bound \(D\le\log_2 k\) already forces (class-level permutation \(p=0.11\)). The surviving deficit tracks the input–output mutual information \(I(X;Y)\) (Pearson 0.998). The de-duplicated failure set is small: 7 points on the standard grid and 124 on the 0.01 grid, all with \(k=2\). This is a documented null. The corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) is unaffected.

## The identity and the bound

With \(F\) uniform on the \(k\) class members and uniform input,

\[
D \;=\; H(F\mid Y)-H(Y\mid X) \;=\; \log_2 k \;-\; I(F;Y) \;-\; H(Y\mid X).
\]

Both subtracted terms are non-negative, so \(D\le\log_2 k\) and \(H(F\mid Y)\le\log_2 k\) at every point. This holds by construction whether or not laws are duplicated. Both were checked at every point. A class of \(m\) copies of one deterministic law has \(I(F;Y)=H(Y\mid X)=0\), so \(D=\log_2 m\) exactly. For example, \(2.807=\log_2 7\) is the 7-member identity-law class.

## 1. Pool rebuild: 50 candidates → 29 distinct laws

Two candidates are duplicates iff their laws agree to within \(10^{-12}\) in both components. The first candidate in the existing order is kept. There are 9 merges, all among the 30 non-ML base candidates. The 20 ML one-bit laws are all distinct, and no two surviving laws are within \(10^{-6}\) of each other.

| law \((q_0,q_1)\) | multiplicity | kept | merged into it |
|---|---|---|---|
| (0, 1), identity | 7 | bool1:2 | bool2:12, I, Z, S, dephase, measZ |
| (1, 0) | 4 | bool1:1 | bool2:3, X, Y |
| (0, 0) | 3 | bool1:0 | bool2:0, reset0 |
| (1, 1) | 3 | bool1:3 | bool2:15, reset1 |
| (0.5, 0.5) | 5 | bool2:5 | bool2:6, bool2:9, bool2:10, H |
| (0.5, 0) | 2 | bool2:1 | bool2:2 |
| (0, 0.5) | 2 | bool2:4 | bool2:8 |
| (1, 0.5) | 2 | bool2:7 | bool2:11 |
| (0.5, 1) | 2 | bool2:13 | bool2:14 |

## 2. Failures

| grid | pool | defined | failures | distinct \(D\) | largest tie | \(D\) min / median / max | class sizes \(k\) at failures |
|---|---|---|---|---|---|---|---|
| standard, step 0.05 | A-ml | 81 | 38 | 8 | 19 (log₂7) | 0.193 / 2.807 / 2.933 | 2, 3, 5, 6, 7, 8 |
| standard, step 0.05 | de-duplicated | 81 | **7** | 4 | 4 | 0.0020 / 0.797 / 0.797 | 2 only |
| step 0.01 (\(g=0\) counted once) | A-ml | 1547 | 529 | 9 | 248 (47%) | 0.023 / 2.807 / 2.933 | 2, 3, 5, 6, 7, 8 |
| step 0.01 (\(g=0\) counted once) | de-duplicated | 1547 | **124** | 5 | 84 (68%) | 0.0020 / 0.797 / 0.797 | 2 only |

On the 0.01 grid the de-duplicated failures fall into five two-member classes:

| \(D\) (bits) | points | class |
|---|---|---|
| 0.797 | 84 | identity law + ml0, \(g\) 0.04–0.10, \(p\) 0.50–0.71 |
| 0.1993 | 22 | ml5 + ml7 |
| 0.1932 | 12 | ml2 + ml10 |
| 0.0232 | 3 | ml13 + ml19 |
| 0.0020 | 3 | bool2:5 + ml17 |

No new failure cells appear on either grid. On the de-duplicated pool, every defined point with \(k=2\) is a failure (7/7 and 124/124). Every point with \(k=1\) is not: there \(D=-H(Y\mid X)\le 0\).

## 3. The 36 persistent failures

The 36 failures that persist across the stopping-time sweep ([procedural-share-tstop.md](procedural-share-tstop.md)) all lie on the standard grid. With duplicates removed:

| A-ml class | old \(D\) | points | de-duplicated \(k\), \(D\) | status |
|---|---|---|---|---|
| 7 identity-law copies | 2.807 | 19 | 1, 0 | vanished (single law) |
| 3 copies of (0, 0) | 1.585 | 3 | 1, 0 | vanished (single law) |
| 5 copies of (0.5, 0.5) | 1.322 | 3 | 1, −1 | vanished (single law) |
| two (0, 0.5) copies | 0.5 | 6 | 1, −0.5 | vanished (single law) |
| 7 identity-law copies + ml0 | 2.933 | 4 | 2, 0.797 | still fails |
| 5 copies of (0.5, 0.5) + ml17 | 1.585 | 1 | 2, 0.0020 | still fails |

So **5 of the 36 remain** and **31 vanish**, each because its class collapsed to a single law. The two A-ml failures outside the 36 (ml2 + ml10 and ml5 + ml7) are unchanged at 0.193 and 0.199 bits.

## 4. Deficit versus set size

- **Among de-duplicated failures:** \(k=2\) everywhere, so Spearman and Pearson correlations of \(D\) with \(k\) or \(\log_2 k\), and the class-collapsed versions, are **undefined**. No failure has \(D=\log_2 k\).
- **Across all defined points (auxiliary; includes non-failures; \(k\in\{1,2\}\)).** On the standard grid, Spearman(\(D,k\)) \(=0.493\).
  - Null with class membership randomised at fixed \(k\) (random \(k\)-subsets of the 29 laws, 200 draws): mean 0.450, 95% range 0.343–0.489. The observed value sits at the top edge of this point-level range.
  - Class-level permutation (\(k\) permuted across the 16 distinct class sets): \(p=0.11\).
  - Residual \(I(F;Y)+H(Y\mid X)\) versus \(k\): Spearman 0.019 (\(p=0.87\)).
  - Partial Spearman of \(D\) and \(\log_2 k\) given \(H(Y)\) and \(H(F\mid Y)\): 0.058.
  - The association amounts to "\(k=2\) can fail, \(k=1\) cannot", which is the bound.
- **0.01 grid, same auxiliary check:** Spearman 0.474 against a randomised-membership mean of 0.434 (95% range 0.419–0.446). The point-level null treats 1547 points as independent, but there are only 19 distinct class sets; the class-level permutation gives \(p=0.12\). Residual versus \(k\): −0.12. Partial correlation given \(H(Y)\) and \(H(F\mid Y)\): 0.092.
- **A-ml reference (standard grid, 38 failures):**
  - Spearman(\(D,k\)) \(=0.986\).
  - Randomised-membership null at the same \(k\): mean 0.89 (95% range 0.83–0.93). Most of the correlation is the bound.
  - \(D=\log_2 k\) exactly at 58% of failures, against 0.5% in the null; that excess is the duplicated deterministic laws.
  - Partial Spearman given \(H(Y)\) and \(H(F\mid Y)\): 0.12.

## 5. What the surviving deficit tracks

| grid | failures | Pearson \(D\) vs \(I(X;Y)\) | Spearman \(D\) vs \(H(Y)\) | Spearman \(D\) vs \(H(F\mid Y)\) |
|---|---|---|---|---|
| standard | 7 | 0.998 | 0.83 | 0.35 |
| 0.01 | 124 | 0.998 | 0.92 | 0.29 |

Separation of large (\(D\ge 0.5\) bit) from small failures, by AUC:

| grid | pool | large / small | \(k\) | \(H(Y)\) | \(I(X;Y)\) | \(H(F\mid Y)\) |
|---|---|---|---|---|---|---|
| standard | de-duplicated | 4 / 3 | 0.5 | 1.0 (\(p=0.03\)) | 1.0 (\(p=0.03\)) | 0.67 |
| 0.01 | de-duplicated | 84 / 40 | 0.5 | 1.0 | 1.0 | 0.70 |
| standard | A-ml (reference) | 36 / 2 | 0.92 | 0.75 | 0.81 | 1.0 |

With \(k\) fixed at 2, \(D = 1 - I(F;Y) - H(Y\mid X)\), and what is left varies with the input–output mutual information \(I(X;Y)\). This describes the small remaining set; it is not offered as a general law.

## 6. PID: skipped

The Williams–Beer binning-sensitivity design of [analysis-pid-binning-sensitivity.md](analysis-pid-binning-sensitivity.md) was not run on the de-duplicated set. It fails all three thin-sample gates set in advance:

| gate | required | de-duplicated, 0.01 grid |
|---|---|---|
| distinct \(D\) values | at least ~30 | 5 |
| largest tie block | under ~20% | 68% |
| failure points | at least ~200 | 124 |

## 7. Corrected bound

\(I(X;Y)+I(F;Y)\le H(Y)\) holds at every defined point of both pools on both grids. The minimum slack is \(-2.8\times10^{-16}\) (rounding) and \(\max\lvert I(X;F)\rvert=1.3\times10^{-15}\).

## Conclusion

On A-ml, much of the strong deficit-versus-set-size association came from the built-in bound \(D\le\log_2 k\). The rest came from duplicated deterministic laws, whose classes give \(D=\log_2 k\) exactly. Keeping each law once removes 31 of the 38 failures and leaves only two-member classes. Among these, \(k\) carries no information about \(D\), and the remaining deficit follows \(I(X;Y)\). \(k\) was only ever a proxy, and this result gives it no support as a measure of description length. The note is a documented null and a companion to [channel-cost-stage2.md](channel-cost-stage2.md) and [analysis-pid-binning-sensitivity.md](analysis-pid-binning-sensitivity.md).

## Reproduction

- **Inputs, unmodified, at base commit `dffe3d4`:**
  - `simulations/classical/procedural_share.py`: GAD law, `tv_max`, `TOL`, pool A.
  - `simulations/classical/procedural_share_mlpool.py`: `pool_A_ml`, `load_pool`, `pool_record`, `ce6_overlap`.
  - `simulations/classical/procedural_share_tstop.py`: `ce6_on_pool`.
  - `simulations/classical/procedural_share_surface.py`: entropy helper.
  - `simulations/classical/data/ce15_ml_pool.json`.

  NumPy 2.x per `requirements.txt` (the run used 2.5.5). The saved and regenerated ML pools both hash to `d11fa3d1ec4594b7…`, and the un-de-duplicated control reproduces 38/81.
- **Scripts.** The de-duplication, grid, correlation and null drivers are scratch scripts **not in the repository**; no simulation code is added with this note. They import only the functions above, apply the de-duplication rule of §1, and use fixed seeds for the randomised-membership null and the permutations.
- **What can be checked from the repo alone.**
  - The merge table: compare the laws in `pool_A_ml()`.
  - The 7/81 count: run `ce6_on_pool` on the de-duplicated list with the default grid.
  - The identity of §1 at any point.

## Scope

Tier 2 only. This is a one-qubit, one-use toy with fixed candidate pools, read out of an existing deterministic computation. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this readout beyond the bookkeeping above.
