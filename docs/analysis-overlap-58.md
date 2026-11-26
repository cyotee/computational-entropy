# Overlap term \(I(X;F\mid Y)\) at the 58 CE-6 failure points (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model**.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim.

**Status:** 2026-11-26 · computed from existing output. No new simulation. The numbers are read out of the deterministic CE-6 one-bit run already computed in [procedural-share-mlpool.md](procedural-share-mlpool.md) §5 (`procedural_share_mlpool.ce6_overlap`, `pool_source="A"`). That run reproduces [procedural-share.md](procedural-share.md) §4: variant (a), pool A, \(\varepsilon=0.05\), one-bit alphabet. Of 72 defined \((g,p)\) points the original form \(I(X;Y)+H(F\mid Y)\le H(Y)\) fails at 58. The deficit is \(D = H(F\mid Y)-H(Y\mid X)\). "Covers" means \(I(X;F\mid Y)\ge D\).

**Script:** [`simulations/classical/analysis_overlap_58.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/analysis_overlap_58.py). Pure numpy; calls `ce6_overlap` only; no new sampling and no parameter change. Built-in self-checks lock the printed headlines below. Every number in the tables is printed by:

```
python simulations/classical/analysis_overlap_58.py
```

## Result (pool A)

| pool | input | defined | original fails | \(I(X;F\mid Y)\) min / median / max | \(D\) min / median / max | \(D - I(X;F\mid Y)\) min / median / max | covers | Spearman vs \(g\) | Spearman vs \(p\) | \(\max|I(X;F)|\) | max identity residual |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | uniform | 72 | 58 | 0.0000 / 0.0048 / 0.0285 | 0.047 / 1.455 / 3.076 | 0.047 / 1.452 / 3.048 | 0/58 | −0.892 | 0.005 | \(4.4\times10^{-16}\) | \(8.9\times10^{-16}\) |
| A | capacity | 72 | 58 | 0.0000 / 0.0048 / 0.0285 | 0.047 / 1.455 / 3.076 | 0.047 / 1.452 / 3.048 | 0/58 | −0.901 | −0.044 | \(4.4\times10^{-16}\) | \(8.9\times10^{-16}\) |

The overlap values and the printed deficit range agree with [procedural-share-mlpool.md](procedural-share-mlpool.md) §5. At the uniform-input failures, 12 of 58 have \(I(X;F\mid Y)\) consistent with 0 (numerical floor \(10^{-15}\)), including the 3 with zero corrected-bound slack already noted there. The two input rows agree to the printed precision on the overlap and on the deficit range; individual deficits still differ by up to 0.10 bits.

**Headline (uniform input, the 58).** Median overlap \(0.0048\) bits against median deficit \(1.455\) bits. The overlap covers the deficit at **0 of 58** points. Median residual \(D - I(X;F\mid Y) = 1.452\) bits: subtracting the overlap barely moves the deficit.

## Identity and independence

From the chain rule,

\[
I(X;Y) + I(F;Y) = I(X,F;Y) + I(X;F) - I(X;F\mid Y).
\]

The identity holds at every defined point (residual below \(10^{-15}\)). The CE-6 inputs (uniform and capacity) do not depend on the candidate, so \(X \perp F\) and \(I(X;F)=0\), checked: \(\max|I(X;F)|=4.4\times10^{-16}\). With that, the overlap term is exactly part of the slack of the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\). It cannot close a deficit that grows with class size (theorem in procedural-share-mlpool.md §5). This readout is consistent with that: the overlap is at most \(0.0285\) bits, two orders of magnitude below the median deficit.

## Correlations, and the absence of rank

The CE-6 one-bit grid is \((g,p)\) only. The run is a single use of a two-outcome readout (`USES = 1`). There is **no rank dimension**, so no rank correlation is reported. Rank \(r\in\{2,4,8,16\}\) is a coordinate of the two-qubit surfaces of CE-9 and CE-12, which are a different run and are not recomputed here.

At the 58 uniform-input failures:

- Spearman(\(I(X;F\mid Y), g\)) \(= -0.892\): the overlap falls as the damping rises.
- Spearman(\(I(X;F\mid Y), p\)) \(= +0.005\): no material correlation with the GAD thermal parameter \(p\).
- Spearman(\(I(X;F\mid Y), D\)) \(= 0.781\): overlap and deficit move together with \(g\), but the residual is essentially \(D\) itself (median \(1.452\) against median \(D = 1.455\)).

The capacity-input Spearmans are \(-0.901\) vs \(g\) and \(-0.044\) vs \(p\), the same reading.

## Pool A-ml, one-line comparison

On the Stage 2 pool (pool A-ml; 81 defined points, 38 failures; [procedural-share-mlpool.md](procedural-share-mlpool.md) §9), uniform input: \(I(X;F\mid Y)\) min / median / max = 0.0000 / 0.0000 / 0.0242 bits; covers 0/38; median \(D - I(X;F\mid Y) = 2.807\) bits (the median overlap is 0, because 31 of 38 failures have overlap consistent with 0); Spearman vs \(g\) / \(p\) = \(-0.097\) / \(-0.224\). Same conclusion: the overlap covers none of the failures.

## Scope

Tier 2 only. A one-qubit, one-use toy with a fixed candidate pool, read out of an existing deterministic computation. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this readout beyond the bookkeeping above.
