# Williams–Beer PID binning sensitivity at the Stage 2 failure points (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model**.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim. All quantities are entropies or mutual informations in bits.

**Status:** 2026-11-26 · computed from existing output. No new simulation and no new simulation code in the repository. This is the first run of the dormant module in [pid-williams-beer.md](pid-williams-beer.md), done on Cyotee's instruction. It uses the Stage 2 channel-cost failure points of [channel-cost-stage2.md](channel-cost-stage2.md), with uniform input:

- Pool A (Haar): 58 failure points of the original form \(I(X;Y)+H(F\mid Y)\le H(Y)\). Deficit \(D\) min / median / max = 0.047 / 1.455 / 3.076 bits (see also [analysis-overlap-58.md](analysis-overlap-58.md)).
- Pool A-ml (energy-bounded pool, [procedural-share-mlpool.md](procedural-share-mlpool.md) §9; pool hash `d11fa3d1ec4594b7…`): 38 failure points of 81. Median \(D\) = 2.807 bits.

Sources are \(S_1=\) B′ (entropy exchange at the actual input) and \(S_2=\) C− or C+ (min or max output entropy of the complementary channel). Target is \(T=D\). Atoms are the Williams–Beer \(I_{\min}\) redundancy, unique B′, unique C and synergy. They sum to the total \(I(D;\text{B′},\text{C})\).

**Verdict.** On this dataset the Williams–Beer module is **underpowered**, and this note gives **no headline decomposition**. With C− as the second source, the split between redundancy and unique B′ flips with the binning on both pools. With C+ as the second source, redundancy dominates almost everywhere, but B′ and C+ are nearly the same variable, so that mostly restates their collinearity. It is not a finding about \(D\). What holds up is coarse: the binned costs carry information about \(D\) above a shuffle null, and unique C and synergy are at chance. This is a documented null. It belongs alongside the Stage 2 channel-cost nulls, which it does not change.

## Method

- **Data.** Per-point (B′, C−, C+, \(D\)) from `channel_cost.accounting(pool)["uniform"]` for `pool` in `"A"` and `"ml"`. Under uniform input B′ = A0 exactly; this was checked at every point.
- **PID.** `pid_williams_beer.pid_williams_beer` on the joint pmf of the binned points (equal weights). For the equal-width and quantile schemes, the result matches the module's own `pid_from_points` adapter to \(10^{-10}\).
- **Binning grid (192 configurations).** Bin counts \(b\in\{2,3,4,5,6,8\}\). The same \(b\) is used for both sources and the target. Four edge schemes:
    1. equal-width;
    2. quantile, linear quantiles with duplicate edges merged;
    3. half-bin-shifted equal-width: \(b\) bins of width \((\max-\min)/(b-\tfrac12)\), origin shifted half a bin below the minimum;
    4. jittered quantile: interior quantile levels moved by \(U(-0.3/b,\,0.3/b)\), 5 fixed seeds.

    That is 2 pools × 2 source pairs × 6 bin counts × 8 binnings = 192.
- **Shuffle null.** 200 permutations of \(D\) per configuration, with fixed seeds. For each atom and for the total, the note reports the null mean and a one-sided permutation p-value. The smallest attainable value is \(1/201\approx0.005\).
- **Dominance label.** The "split" of a configuration is whichever is largest: redundancy, unique B′ or unique C. The same label is also computed after subtracting each atom's null mean (null-corrected).

## Why the sample is thin

| variable | pool A: distinct of 58 | ties | pool A-ml: distinct of 38 | ties | range (bits) |
|---|---|---|---|---|---|
| B′ | 48 | 11 at 0 (\(g=0\)) | 28 | 11 at 0 | 0 to 2 |
| C− | 42 | 17 at 0 | 22 | 17 at 0 | 0 to 1 (cap) |
| C+ | 45 | 11 at 0 | 25 | 11 at 0 | 0 to 2 (cap) |
| \(D\) | 20 | 22 at 2.967 | 8 | 19 at 2.807 | 0.047 to 3.076 / 0.193 to 2.933 |

- **Small n.** \(n=58\) and \(n=38\).
- **One point per cell.** Every failure point is a distinct \((g,p)\) cell (58/58 and 38/38).
- **Sources depend only on the channel.** Every source is a deterministic function of \((g,p)\) and does not depend on \(f\) (channel-cost-stage2.md §1). The PID therefore splits information about \(D\) between two functions of the channel parameters. It is not a PID of anything that sees the candidate.
- **The target is heavily tied.** With only 20 and 8 distinct values of \(D\), quantile edges merge, and the effective target bins fall to 3–6.
- **Too few points per cell.** At \(b=8\) there are 1.61–4.22 points per occupied joint cell, and at most 0.158 per nominal cell.

## Results

Atoms at \(b=4\), plus counts over all 48 configurations per pool and pair. Entries are redundancy / unique B′ / unique C / synergy, then total \(I\) with its null mean in brackets. "Redundancy wins" means redundancy is larger than both unique atoms.

| pool, pair | \(b=4\) equal-width | \(b=4\) quantile | redundancy wins (all 48) | redundancy wins, \(b=3\)–5 (24) | null-corrected, all 48 |
|---|---|---|---|---|---|
| A, (B′, C−) | 0.47/0.30/0.06/0.06 · 0.88 [0.20] | 0.50/0.30/0.04/0.30 · 1.14 [0.45] | 40 (unique B′ 7, unique C 1) | 20 (unique B′ 4) | 39 (unique B′ 8, unique C 1) |
| A, (B′, C+) | 0.74/0.03/0.08/0.04 · 0.88 [0.17] | 0.80/0.00/0.02/0.11 · 0.93 [0.26] | 47 (unique C 1) | 24 | 47 (unique C 1) |
| A-ml, (B′, C−) | 0.63/0.62/0.00/0.11 · 1.35 [0.31] | 0.41/0.48/0.00/0.13 · 1.02 [0.36] | 28 (unique B′ 20) | 12 (unique B′ 12) | 23 (unique B′ 25) |
| A-ml, (B′, C+) | 1.23/0.02/0.00/0.01 · 1.25 [0.23] | 0.74/0.16/0.00/0.18 · 1.07 [0.36] | 47 (unique C 1) | 24 | 47 (unique C 1) |

The full 192-row grid has, for every configuration: atoms, null means, 95th percentiles, p-values and cell occupancy. It is held with the analysis script outside the repository (see Reproduction).

### C−: the split flips on both pools

- **Pool A, (B′, C−).** Redundancy beats unique B′ in 40/48 configurations. The flips are:
    - \(b=2\): equal-width (unique C wins), half-bin-shifted equal-width, and jittered quantile seed 1 (both unique B′);
    - \(b=3\): jittered quantile seeds 1–4 (unique B′);
    - \(b=6\): equal-width (unique B′; 0.61 vs redundancy 0.60).

    After null correction, equal-width at \(b=5\) also flips.
- **Pool A-ml, (B′, C−).** Redundancy wins 28/48 and unique B′ wins 20/48. Within \(b=3\)–5 the split is 12/12. After null correction, unique B′ leads in 25/48. Neither label holds across reasonable binnings.

By Cyotee's decision rule, a unique/redundant split that flips across reasonable binnings means the module is flagged as underpowered and no single number is given.

### C+: redundancy dominance is collinearity

Redundancy wins in 47/48 configurations on both pools, and in 24/24 within \(b=3\)–5. The only exception on each pool is equal-width at \(b=2\). But B′ and C+ are close to identical on these points:

- Pearson 0.997 (pool A) and 0.996 (pool A-ml); Spearman 0.979 and 0.940;
- \(\max\lvert\text{B′}-\text{C+}\rvert = 0.224\) bits on both pools.

When two sources overlap this much, \(I_{\min}\) puts the shared part into redundancy by construction. It is also known to over-count redundancy for overlapping or copied sources (Harder, Salge and Polani 2013; Bertschinger et al. 2014; see [pid-williams-beer.md](pid-williams-beer.md) §4). The stable label is therefore not evidence of a redundant structure in \(D\). For comparison, B′ vs C− has Spearman 0.808 (A) and 0.834 (A-ml).

### What holds up

| pool, pair | total \(I\) beats null (p ≤ 0.05) | redundancy p ≤ 0.05 | unique B′ p ≤ 0.05 | unique C p ≤ 0.05 | synergy p ≤ 0.05 | mean excess over null: red / unique B′ / unique C / syn |
|---|---|---|---|---|---|---|
| A, (B′, C−) | 48/48 | 47/48 | 42/48 | 6/48 | 5/48 | 0.40 / 0.23 / 0.00 / −0.01 |
| A, (B′, C+) | 47/48 | 47/48 | 3/48 | 13/48 | 5/48 | 0.64 / −0.01 / 0.04 / −0.03 |
| A-ml, (B′, C−) | 48/48 | 46/48 | 46/48 | 1/48 | 2/48 | 0.34 / 0.39 / −0.03 / −0.04 |
| A-ml, (B′, C+) | 48/48 | 48/48 | 3/48 | 5/48 | 4/48 | 0.73 / 0.00 / 0.01 / −0.04 |

- **Total \(I\) beats the shuffle null nearly everywhere.** The binned costs carry information about \(D\) above chance (191/192 configurations; the exception is pool A, (B′, C+), equal-width \(b=2\), \(p=0.10\)). This matches the negative cost–deficit correlations already reported in Stage 2.
- **Unique C and synergy are at chance.** Their mean excess over the null is between −0.04 and +0.04 bits in every pool and pair. The largest exception: unique C clears the null in 13/48 configurations on pool A, (B′, C+), with a mean excess of only 0.04 bits.
- **Plug-in bias dominates at high bin counts.** The null mean accounts for this share of observed total \(I\):

| pool, pair | \(b\le3\) | \(b=8\) | all \(b\) |
|---|---|---|---|
| A, (B′, C−) | 0.17 | 0.61 | 0.36 |
| A, (B′, C+) | 0.15 | 0.56 | 0.31 |
| A-ml, (B′, C−) | 0.19 | 0.56 | 0.35 |
| A-ml, (B′, C+) | 0.13 | 0.50 | 0.31 |

About 50–61% of the total at \(b=8\) is estimation bias. The rise of total \(I\) with \(b\) (for example 0.11 → 1.58 bits on pool A, (B′, C−), equal-width) is mostly that bias. Since every point is its own \((g,p)\) cell, any fine enough binning of the sources would separate points that differ in \(D\).

## Conclusion

The PID adds nothing robust beyond what Stage 2 already showed: the channel-only costs track part of \(D\). The redundancy-versus-unique-B′ split with C− depends on the binning on both pools. The stable result with C+ reflects B′ ≈ C+. Unique C and synergy are at chance. This is a documented null, suitable as an appendix companion to the Stage 2 channel-cost nulls ([channel-cost-stage2.md](channel-cost-stage2.md)) and to the module note ([pid-williams-beer.md](pid-williams-beer.md)). A finer decomposition would need more failure points with more distinct \(D\) values, sources that see \(f\), or a different redundancy measure. None of these is attempted here. The corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) (a theorem for \(X\perp F\)) is not affected.

## Reproduction

- **Inputs.** `simulations/classical/channel_cost.py` (`accounting`) and `simulations/classical/pid_williams_beer.py`, both unmodified, at base commit `0dfe425`. NumPy 2.x (the run used 2.5.5), per `requirements.txt`. The ML pool array hash is `d11fa3d1ec4594b7…` (checked).
- **Script.** The binning-grid and permutation driver is a scratch script that is **not in the repository**; no simulation code is added with this note. It calls only the two module functions above. It applies the four edge schemes and the 200-permutation null with fixed seeds, as described in Method, so it is deterministic. A run at `67b9230` and a rerun at `0dfe425` gave byte-identical grid output (192 rows).
- **What can be checked from the repo alone.** The failure-point counts and \(D\) ranges (channel-cost-stage2.md), B′ = A0 under uniform input, the source and target value counts in the "Why the sample is thin" table, and any single configuration. For example, \(b=4\) quantile on pool A, (B′, C−) is `pid_from_points(Bp, Cmin, D, bins=4, method="quantile")` on the `accounting("A")["uniform"]` rows.

## Scope

Tier 2 only. This is a one-qubit, one-use toy with fixed candidate pools, read out of an existing deterministic computation. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this readout beyond the bookkeeping above.
