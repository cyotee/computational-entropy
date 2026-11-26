# Channel-cost Stage 2: accounting test at the CE-6 failure points (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model and proof-of-concept** for a one-qubit channel.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim. A "cost" here is an entropy in bits. Pricing it at \(k_BT\ln2\) is a convention only.

**Status:** 2026-11-26 · computed. This is the Stage 2 test planned in [CHANNEL_COST_STAGE1.md](https://github.com/cyotee/computational-entropy/blob/master/CHANNEL_COST_STAGE1.md) §8, run after review on Cyotee's instruction. It uses the Stage 1 definition (A0), two alternates (B′, C) and their linear combinations, on two candidate pools.

**Verdict.** All three definitions are **tested and rejected as rescues of the original form** \(I(X;Y)+H(F\mid Y)\le H(Y)\). None covers the deficit at all failure points, on either pool, for either input. All are **negatively** correlated with the deficit. Non-negative linear combinations of the definitions also fail, both in sample and out of sample (§4). This is a clean null across three definitions and their combinations. It stands alongside the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) (a theorem for \(X\perp F\)) and does not weaken it. The channel-cost line of research continues.

**Script:** [`simulations/classical/channel_cost.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/channel_cost.py). It is pure numpy and deterministic, has built-in self-checks and runs in about 15 s. It hooks into `procedural_share_mlpool.ce6_overlap`, which supplies the failure points, and uses the saved ML pool of [procedural-share-mlpool.md](procedural-share-mlpool.md) §9. Every number below is printed by:

```
python simulations/classical/channel_cost.py            # self-checks + full report
python simulations/classical/channel_cost.py --check    # self-checks only
```

## 1. Definitions

All three are entropies of the **noise channel alone**. Here that channel is \(N=\mathrm{GAD}_{g,p}\) on one qubit, with the Kraus set of Stage 1 §1. The complementary channel is \([N^c(\rho)]_{kl}=\operatorname{Tr}(K_k\rho K_l^\dagger)\), and \(S(N^c(\rho))\) is the entropy exchange \(S_e(\rho,N)\), which does not depend on the dilation.

| | Definition | Formula | Depends on |
|---|---|---|---|
| **A0** | map entropy (Stage 1 primary) | \(S(J(N)/2)=S(N^c(I/2))\), closed form Stage 1 §5.1 | \((g,p)\) |
| **B′** | entropy exchange at the actual input | \(S(N^c(\bar\rho))\), \(\bar\rho=\mathrm{diag}(\pi_0,\pi_1)\), with \(\pi\) the CE-6 input law at that point (uniform or Blahut–Arimoto capacity) | \((g,p)\), input law |
| **C−** | min output entropy of \(N^c\) | \(\min_\psi S(N^c(\psi))\) over pure states (the global minimum, by concavity) | \((g,p)\) |
| **C+** | max output entropy of \(N^c\) | \(\max_\rho S(N^c(\rho))\) over all states | \((g,p)\) |

- **Uniform input:** \(\bar\rho=I/2\), so B′ = A0 exactly. Because \(I/2\) is feasible for C+, \(\text{C−}\le\text{A0}\le\text{C+}\le 2\) bits.
- **Skipped by decision:** the bath's starting entropy \(h_2(p)\) (Stage 1 candidate A). It is not the same quantity as the map entropy, since \(h_2(p)>0\) at \(g=0\), where the map entropy is 0.

**Optimisation (C−, C+).** GAD is phase covariant, so \(S(N^c(\cdot))\) is invariant under \(Z\) rotations (checked on random phases, difference \(<2\times10^{-15}\)).

- **C−:** a search over pure states \(\cos(t/2)|0\rangle+\sin(t/2)|1\rangle\), \(t\in[0,\pi]\). It uses a 4001-point grid, then golden-section refinement in the best cell. A 1001-point grid agrees to \(<10^{-9}\) bits.
- **C+:** by covariance and concavity the maximiser can be taken diagonal, \(\mathrm{diag}(q,1-q)\). \(S\) is concave in \(q\), so golden section on \([0,1]\) finds the global maximum.
- **Cross-check:** no random pure state goes below C−, and no random mixed state goes above C+ (1500 of each).

**Self-checks.**

- A0's closed form equals the numeric \(S(J/2)\) and \(S(N^c(I/2))\) on an \(11\times11\) grid (difference \(1.2\times10^{-15}\)).
- \(g=0\): A0 = C− = C+ = 0.
- \(g=1\): C− = \(h_2(p)\) and C+ = A0 = \(1+h_2(p)\).
- Plain AD (\(p=1\)): C− = 0.

**Units and normalisation.** The deficit \(D=H(F\mid Y)-H(Y\mid X)\) of the CE-6 one-bit run is per symbol. A symbol is one use of one qubit (`USES = 1`), so per block = per qubit use, and every cost is in bits per qubit use. For the two-qubit, two-use blocks of CE-9 to CE-12 the corresponding block total is \(4\times\)A0 (§4).

**\(f\)-dependence.** In the CE-6 run the noise acts directly on the input \(|x\rangle\). The target law is `gad_law(g, p)` and no candidate map precedes the noise. So **all four costs are \(f\)-independent** at the failure points. They can follow only the \((g,p)\) part of the deficit, never its pool part. In the two-qubit surfaces, \(U_f\) acts before the noise and B′ does depend on \(f\) (§4).

**Test.** At each failure point, the cost-augmented original form \(H(F\mid Y)\le H(Y\mid X)+\text{cost}\) holds iff cost \(\ge D\). "Closes the gap" means this holds at every failure point.

## 2. Results: pool A-ml (the ML-derived Stage 2 pool; 38 of 81 points fail)

Pool A-ml is CE-6 pool A with its 20 Haar members replaced by 20 Margolus–Levitin one-bit laws ([procedural-share-mlpool.md](procedural-share-mlpool.md) §9). The run is variant (a), \(\varepsilon=0.05\), on the \(21\times11\) \((g,p)\) grid.

**Uniform input** (\(D\) = 0.193 / 2.807 / 2.933 bits, min / median / max):

| definition | cost min / median / max | covers (cost >= D) | D - cost min / median / max | Pearson(cost, D) | Spearman(cost, D) |
|---|---|---|---|---|---|
| A0 map entropy | 0.000 / 0.195 / 2.000 | 12/38 | -1.081 / 2.618 / 2.807 | -0.754 | -0.648 |
| B' entropy exchange | 0.000 / 0.195 / 2.000 | 12/38 | -1.081 / 2.618 / 2.807 | -0.754 | -0.648 |
| C- min output | 0.000 / 0.049 / 1.000 | 2/38 | -0.408 / 2.746 / 2.838 | -0.454 | -0.295 |
| C+ max output | 0.000 / 0.259 / 2.000 | 12/38 | -1.096 / 2.559 / 2.807 | -0.788 | -0.733 |

**Capacity input** (same failure set; \(D\) = 0.193 / 2.807 / 2.933):

| definition | cost min / median / max | covers (cost >= D) | D - cost min / median / max | Pearson(cost, D) | Spearman(cost, D) |
|---|---|---|---|---|---|
| A0 map entropy | 0.000 / 0.195 / 2.000 | 12/38 | -1.071 / 2.618 / 2.807 | -0.764 | -0.648 |
| B' entropy exchange | 0.000 / 0.194 / 2.000 | 12/38 | -1.063 / 2.620 / 2.807 | -0.743 | -0.651 |
| C- min output | 0.000 / 0.049 / 1.000 | 2/38 | -0.408 / 2.746 / 2.838 | -0.468 | -0.316 |
| C+ max output | 0.000 / 0.259 / 2.000 | 12/38 | -1.086 / 2.559 / 2.807 | -0.796 | -0.734 |

**Per damping row** (uniform input; means over the failing \(p\) values of each row):

| g | failures | mean D | mean A0 | mean B' | mean C- | mean C+ | max cost | min D |
|---|---|---|---|---|---|---|---|---|
| 0.00 | 11 | 2.807 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.807 |
| 0.05 | 11 | 2.842 | 0.188 | 0.188 | 0.067 | 0.234 | 0.286 | 2.807 |
| 0.10 | 1 | 2.933 | 0.344 | 0.344 | 0.172 | 0.344 | 0.344 | 2.933 |
| 0.45 | 1 | 0.500 | 0.769 | 0.769 | 0.000 | 0.993 | 0.993 | 0.500 |
| 0.50 | 4 | 0.423 | 0.980 | 0.980 | 0.260 | 1.074 | 1.202 | 0.193 |
| 0.55 | 2 | 0.500 | 0.909 | 0.909 | 0.089 | 1.030 | 1.060 | 0.500 |
| 0.60 | 1 | 0.199 | 1.280 | 1.280 | 0.555 | 1.295 | 1.295 | 0.199 |
| 0.90 | 1 | 1.585 | 1.853 | 1.853 | 0.927 | 1.853 | 1.853 | 1.585 |
| 0.95 | 2 | 1.453 | 1.463 | 1.463 | 0.482 | 1.464 | 1.927 | 1.322 |
| 1.00 | 4 | 1.453 | 1.570 | 1.570 | 0.570 | 1.570 | 2.000 | 1.322 |

## 3. Results: pool A (CE-6 continuity; 58 of 72 points fail)

**Uniform input** (\(D\) = 0.047 / 1.455 / 3.076 bits, min / median / max; the median is 1.455 and the maximum 3.076, at \(g=0.1\), \(p=0.5\), \(|C|=9\)):

| definition | cost min / median / max | covers (cost >= D) | D - cost min / median / max | Pearson(cost, D) | Spearman(cost, D) |
|---|---|---|---|---|---|
| A0 map entropy | 0.000 / 0.534 / 2.000 | 17/58 | -1.571 / 0.586 / 2.967 | -0.661 | -0.691 |
| B' entropy exchange | 0.000 / 0.534 / 2.000 | 17/58 | -1.571 / 0.586 / 2.967 | -0.661 | -0.691 |
| C- min output | 0.000 / 0.162 / 1.000 | 5/58 | -0.758 / 1.048 / 2.967 | -0.512 | -0.512 |
| C+ max output | 0.000 / 0.537 / 2.000 | 17/58 | -1.571 / 0.585 / 2.967 | -0.676 | -0.728 |

**Capacity input:**

| definition | cost min / median / max | covers (cost >= D) | D - cost min / median / max | Pearson(cost, D) | Spearman(cost, D) |
|---|---|---|---|---|---|
| A0 map entropy | 0.000 / 0.534 / 2.000 | 17/58 | -1.571 / 0.586 / 2.967 | -0.664 | -0.699 |
| B' entropy exchange | 0.000 / 0.533 / 2.000 | 17/58 | -1.570 / 0.598 / 2.967 | -0.654 | -0.696 |
| C- min output | 0.000 / 0.162 / 1.000 | 5/58 | -0.758 / 1.048 / 2.967 | -0.521 | -0.542 |
| C+ max output | 0.000 / 0.537 / 2.000 | 17/58 | -1.571 / 0.585 / 2.967 | -0.677 | -0.751 |

**Per damping row** (uniform input):

| g | failures | mean D | mean A0 | mean B' | mean C- | mean C+ | max cost | min D |
|---|---|---|---|---|---|---|---|---|
| 0.00 | 11 | 2.807 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.807 |
| 0.05 | 11 | 2.842 | 0.188 | 0.188 | 0.067 | 0.234 | 0.286 | 2.807 |
| 0.10 | 1 | 2.933 | 0.344 | 0.344 | 0.172 | 0.344 | 0.344 | 2.933 |
| 0.45 | 1 | 0.500 | 0.769 | 0.769 | 0.000 | 0.993 | 0.993 | 0.500 |
| 0.50 | 4 | 0.423 | 0.980 | 0.980 | 0.260 | 1.074 | 1.202 | 0.193 |
| 0.55 | 2 | 0.500 | 0.909 | 0.909 | 0.089 | 1.030 | 1.060 | 0.500 |
| 0.60 | 1 | 0.199 | 1.280 | 1.280 | 0.555 | 1.295 | 1.295 | 0.199 |
| 0.90 | 1 | 1.585 | 1.853 | 1.853 | 0.927 | 1.853 | 1.853 | 1.585 |
| 0.95 | 2 | 1.453 | 1.463 | 1.463 | 0.482 | 1.464 | 1.927 | 1.322 |
| 1.00 | 4 | 1.453 | 1.570 | 1.570 | 0.570 | 1.570 | 2.000 | 1.322 |

## 4. Pass 4: linear combinations

**Hypothesis tested.** Channel cost depends on the condition and decomposes as a linear combination of A0, B′, C− and C+. All terms are in bits per qubit use, as in §1.

**Models.**

- **Unweighted sums:** B′+C−, B′+C+, A0+B′, A0+C+ and A0+B′+C+.
- **Least-squares fits to \(D\):** non-negative weights and no intercept, on (B′, C−), (B′, C+) and (A0, B′, C−, C+). The fits are exact, by subset enumeration.
- **The same fits with an unconstrained intercept, flagged separately.** An intercept is a constant offset, not a property of the channel. Negative weights are excluded by design.

**Validation.** Each model is fitted on pool A and tested on pool A-ml, and vice versa. Within each pool it is also run leave-one-damping-row-out (LORO): every \(g\) row is predicted from a fit on the other rows. R² is computed against the mean of \(D\) on the evaluation set, so it can be negative.

**Results, uniform input.** R² columns give the cross-pool test, with the in-sample value in brackets. Covers, median and Spearman are for the cross-pool test. The sums have no fit.

| model | weights (fit on A; fit on A-ml) | R² on A | R² on A-ml | LORO R² A / A-ml | covers A | covers A-ml | median D − cost A / A-ml | Spearman A / A-ml |
|---|---|---|---|---|---|---|---|---|
| B' + C- | 1 each (no fit) | -2.407 | -3.856 | — | 21/58 | 12/38 | 0.293 / 2.545 | -0.685 / -0.666 |
| B' + C+ | 1 each (no fit) | -2.982 | -4.437 | — | 29/58 | 15/38 | 0.001 / 2.365 | -0.715 / -0.725 |
| A0 + B' | 1 each (no fit) | -2.989 | -4.444 | — | 27/58 | 15/38 | 0.012 / 2.428 | -0.691 / -0.648 |
| A0 + C+ | 1 each (no fit) | -2.982 | -4.437 | — | 29/58 | 15/38 | 0.001 / 2.365 | -0.715 / -0.725 |
| A0 + B' + C+ | 1 each (no fit) | -5.219 | -6.694 | — | 35/58 | 15/38 | -0.347 / 2.184 | -0.713 / -0.722 |
| fit B', C- | (0.934, 0.000); (0.959, 0.000) | -2.188 (in -2.188) | -3.666 (in -3.666) | -2.232 / -3.752 | 17/58 | 12/38 | 0.627 / 2.630 | -0.691 / -0.648 |
| **fit + intercept (flagged)** B', C- | (1.753, 0.000, 0.000); (2.073, 0.000, 0.000) | -0.094 (in 0.000) | -0.103 (in 0.000) | -0.301 / -0.433 | 35/58 | 15/38 | -0.618 / 1.055 | n/a / n/a |
| fit B', C+ | (0.000, 0.940); (0.000, 0.963) | -2.155 (in -2.154) | -3.616 (in -3.616) | -2.242 / -3.778 | 17/58 | 12/38 | 0.622 / 2.574 | -0.728 / -0.733 |
| **fit + intercept (flagged)** B', C+ | (1.753, 0.000, 0.000); (2.073, 0.000, 0.000) | -0.094 (in 0.000) | -0.103 (in 0.000) | -0.301 / -0.433 | 35/58 | 15/38 | -0.618 / 1.055 | n/a / n/a |
| fit A0, B', C-, C+ | (0.000, 0.000, 0.000, 0.940); (0.000, 0.000, 0.000, 0.963) | -2.155 (in -2.154) | -3.616 (in -3.616) | -2.242 / -3.778 | 17/58 | 12/38 | 0.622 / 2.574 | -0.728 / -0.733 |
| **fit + intercept (flagged)** A0, B', C-, C+ | (1.753, 0.000, 0.000, 0.000, 0.000); (2.073, 0.000, 0.000, 0.000, 0.000) | -0.094 (in 0.000) | -0.103 (in 0.000) | -0.301 / -0.433 | 35/58 | 15/38 | -0.618 / 1.055 | n/a / n/a |

The capacity input agrees with these numbers to within 0.25 in R² and 0.02 bits in the medians, with identical covers counts. The full tables for both inputs are printed by the script.

**What a channel-only cost could explain at most.**

- **Where pool dependence can show up.** In the CE-6 run \(D\) is a class-level number, one per \((g,p)\) cell per pool. So variation "across \(f\) at fixed channel parameters" can only appear as variation between pools at the same cell.
- **Failure points only.** Over the 96 failure points of both pools (60 cells, 36 of them failing in both pools), 0.2% of the variance of \(D\) lies within cells, so the R² ceiling for any channel-only cost is 0.998. At shared cells \(|D_A-D_{A\text{-ml}}|\) is at most 0.159 bits.
- **All defined points.** Using the signed deficit at all 54 cells defined in both pools, 5.2% of the variance lies within cells (ceiling 0.948). 11 of those cells fail in one pool and hold in the other at the **same** channel.
- **Conclusion from the split.** Channel-only costs are not ruled out here by the variance split. The ceiling is high, because within one pool \(D\) is a single function of \((g,p)\). The combinations fail for a different reason: every term is near 0 where \(D\) is largest (small \(g\)), and the terms grow where \(D\) is small.

**Reading.**

- **Non-negative weights give no explanatory power.** Every no-intercept fit has negative R² both in-sample and out of sample (−2.2 to −3.8). The fit collapses onto a single term with weight of about 0.94–0.96, A0/B′ or C+, and the other weights are zero.
- **The intercept fits use no channel term at all.** With an intercept, every channel weight is 0. The fit is the constant mean deficit (1.75 bits on A, 2.07 on A-ml), and out of sample R² is −0.09 to −0.43. The constant raises the covers count to 35/58 and 15/38 only by being a constant, which is not a channel cost.
- **The best unweighted sum still falls short.** A0+B′+C+ covers 35/58 on pool A and 15/38 on pool A-ml. Spearman is about −0.7 throughout.
- **Status: the hypothesis is not supported.** Linear combinations are TESTED-AND-REJECTED as rescues of the original form, out of sample as well as in sample.

## 5. \(f\)-dependence check (two-qubit surfaces, not a failure-point test)

B′ per two-use block on the saved two-qubit ML pool (200 candidates), GAD at \(T=1\), with per-use input \(U_f(\tfrac I2\otimes|0\rangle\langle0|)U_f^\dagger\) and \(U_f\) before the noise, as in CE-9 to CE-12. The block total is twice the per-use value (product input, product channel).

| g | B' block min | median | max | 4 x A0 (f-independent) |
|---|---|---|---|---|
| 0.0 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.2 | 1.769 | 2.015 | 2.294 | 2.301 |
| 0.5 | 3.437 | 3.770 | 4.141 | 4.548 |
| 0.8 | 4.682 | 4.892 | 5.175 | 6.328 |
| 1.0 | 5.360 | 5.360 | 5.360 | 7.360 |

B′ varies across candidates by up to about 0.7 bits per block. That makes it the only one of the four that can see \(f\) at all, and it does so only in the two-qubit model. In the CE-6 run, where the failure points live, it does not.

## 6. Reading

- **No definition closes the gap.** On either pool, with either input, every definition fails at 26/38 or more (pool A-ml) and 41/58 or more (pool A) points. The 2-bit cap alone rules out the 23 points with \(D>2\) on each pool, as Stage 1 §8 anticipated.
- **The zero-damping row is decisive.** At \(g=0\) all four costs are 0. The deficit there is \(H(F\mid Y)=2.807\) bits (pool A-ml) or \(2.967\) bits (pool A), since \(H(Y\mid X)=0\).
- **No definition tracks the deficit.** Pearson and Spearman correlations are negative for all four definitions on both pools (between −0.36 and −0.81). The costs rise with \(g\). The deficit is largest at small \(g\), where the GAD law is near the identity and the \(\varepsilon\)-class is large. Where a cost does cover \(D\) (12/38 and 17/58 points for A0, B′ and C+; 2/38 and 5/58 for C−), it is at large \(g\) and small classes. That is not evidence of accounting.
- **Structural reason (consistent with CE-12 and Stage 1 §8).** \(H(F\mid Y)\ge\log_2|C|-H(Y)\) grows with the class, while every cost here is a channel-only quantity of at most 2 bits that is independent of \(f\) and of the pool.
- **Status:** TESTED-AND-REJECTED as rescues of the original form: A0 (map entropy), B′ (entropy exchange at the actual input) and C± (min/max output entropy of the complementary channel). This does not reject channel cost as a quantity. It may still be useful as a separate ledger entry next to the corrected bound (Stage 1 §8 (ii)). That is not tested here.
- **Combinations (§4).** Sums and non-negative least-squares blends do no better. Out of sample they track the deficit no better than the definitions alone, and they explain less of its variance than a constant.
- **Relation to PAPER_PLAN §4.** None of the definitions or combinations supplies a term that grows with the pool. The revisit condition for overlap-first is still not met.

## 7. Scope

Tier 2 only. One-qubit GAD toy, one clustering rule and two candidate pools. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this run beyond the information-theoretic bookkeeping above.
