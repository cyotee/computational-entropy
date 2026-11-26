# Williams–Beer PID module (dormant; Tier 2 toy)

**Tier:** 2 of 3. This is a **toy-model** information-theoretic module.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim. Every quantity below is an entropy or a mutual information in **bits**.

**Status:** **DORMANT** (2026-11-26). The code is written and unit-tested on synthetic joints only. It has **not** been run on the Stage 2 per-point tables (entropy exchange B′, complementary-channel entropy C±, deficit \(D\)). It stays dormant until the channel-cost line is revisited.

**Script:** [`simulations/classical/pid_williams_beer.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/pid_williams_beer.py) (pure numpy; no import of `channel_cost.py` or the energy-bounded pool). Tests: [`simulations/classical/test_pid_williams_beer.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/test_pid_williams_beer.py). The only `__main__` path is a synthetic self-check:

```
python simulations/classical/pid_williams_beer.py            # synthetic self-checks only
python -m pytest simulations/classical/test_pid_williams_beer.py
```

There is no flag that loads Stage 2 data.

## 1. What it is

A generic discrete [Williams–Beer](https://arxiv.org/abs/1004.2515) partial information decomposition (PID) for **two source variables** and one target, plus an adapter that bins continuous per-point arrays into a joint pmf. The intended sources and target, when the line is revisited, are:

| Role | Intended Stage 2 field | Meaning |
|---|---|---|
| \(S_1\) | `Bp` | entropy exchange at the actual input (B′) |
| \(S_2\) | `Cmin` or `Cmax` | min or max output entropy of the complementary channel (C− or C+) |
| \(T\) | `D` | deficit of the original form, \(H(F\mid Y)-H(Y\mid X)\) |

The module does not choose C− versus C+ for the caller. Map entropy A0 is not a default source: under uniform input, B′ equals A0 exactly ([channel-cost-stage2.md](channel-cost-stage2.md) §1).

This is a decomposition of \(I(T;S_1,S_2)\), not a new channel-cost definition and not a test of the original form.

## 2. Discrete interface

```
from pid_williams_beer import pid_williams_beer, example_joint, EXAMPLE_ATOMS

result = pid_williams_beer(joint)
```

**Input.** `joint` is either

- a 3-D ndarray `p[s1, s2, t]`, or
- a dict `{(s1, s2, t): mass}`.

Masses must be finite and non-negative. They are renormalised to a pmf if they do not already sum to 1. Dict keys are the level labels; levels are sorted for a deterministic dense array.

**Output.** A frozen `PIDResult` whose fields are all in bits:

| Field | Meaning |
|---|---|
| `redundancy` | \(I_{\min}(T;\{S_1,S_2\})\) |
| `unique1`, `unique2` | unique information about \(T\) in \(S_1\) or \(S_2\) |
| `synergy` | synergistic information |
| `I_T_S1`, `I_T_S2`, `I_T_S12` | \(I(T;S_1)\), \(I(T;S_2)\), \(I(T;S_1,S_2)\) |
| `H_T`, `H_S1`, `H_S2`, `H_S12` | Shannon entropies of \(T\), \(S_1\), \(S_2\), and \((S_1,S_2)\) |

`result.atoms()` is the tuple `(redundancy, unique1, unique2, synergy)`. These four numbers sum to \(I(T;S_1,S_2)\).

**Formulae** (Williams & Beer 2010). The specific information of outcome \(t\) about a source \(S_i\) is the Kullback–Leibler divergence \(I(T=t;S_i)=D_{\mathrm{KL}}\bigl(p(S_i\mid t)\,\|\,p(S_i)\bigr)\), in bits. Then

\[
\begin{aligned}
\mathrm{Red} &= I_{\min}(T;\{S_1,S_2\}) = \sum_t p(t)\,\min\bigl\{I(T=t;S_1),\,I(T=t;S_2)\bigr\},\\
\mathrm{Uniq}_1 &= I(T;S_1)-\mathrm{Red},\\
\mathrm{Uniq}_2 &= I(T;S_2)-\mathrm{Red},\\
\mathrm{Syn} &= I(T;S_1,S_2)-I(T;S_1)-I(T;S_2)+\mathrm{Red}.
\end{aligned}
\]

The atoms are theoretically non-negative. The implementation uses \(\log_2\) and the convention \(0\log 0=0\).

## 3. Adapter: binning continuous points

```
from pid_williams_beer import pid_from_points, discretise_to_joint

atoms, binned = pid_from_points(s1, s2, t, bins=4, method="quantile", weights=None)
# or, just the joint:
binned = discretise_to_joint(s1, s2, t, bins=(4, 4, 6), method="equal-width")
```

**Inputs.**

- `s1`, `s2`, `t`: 1-D arrays of equal length, one entry per point. Intended values: B′, C− or C+, and \(D\).
- `bins`: a single integer (the same requested bin count for all three variables) or a triple `(n_s1, n_s2, n_t)`. Each count must be \(\ge 1\).
- `method`: `"equal-width"` or `"quantile"`. There is no other rule.
- `weights`: optional non-negative masses of the same length. Default: every point has weight 1 (the equal-weight empirical measure). Weights are renormalised.

**Binning rules (deterministic; no RNG).**

- Equal-width: edges are `linspace(min, max, n+1)`. If `min == max`, a single bin of width 1 is used, centred on that value.
- Quantile: edges are the linear quantiles at \(0, 1/n, \dots, 1\), via `numpy.quantile(..., method="linear")`. Duplicate edges are merged, so the **effective** bin count can be smaller than the request (constant or few-valued data). If every value is identical, a single bin of width 1 is used. If the only remaining edges are \(\{\min,\max\}\), that single closed interval contains every point.
- A point is assigned by `searchsorted(..., side="right")` so the maximum falls in the last bin (the last bin is closed on the right).

**Output of the adapter.** `pid_from_points` returns `(PIDResult, BinnedJoint)`. `BinnedJoint` carries the normalised 3-D `joint`, the three `edges` arrays, per-point `indices` of shape `(n_points, 3)`, the effective `n_bins`, the `method`, the `weights`, and the `requested_bins`.

**Intended hook to the Stage 2 table** (not called by this module):

```
from channel_cost import accounting
rows = accounting("A")["uniform"]       # or accounting("ml"); input "capacity"
# each row has D, Bp, Cmin, Cmax, A0, g, p, k
pid_from_points([r["Bp"] for r in rows],
                [r["Cmax"] for r in rows],   # or r["Cmin"]
                [r["D"] for r in rows],
                bins=4, method="quantile")
```

`accounting` is defined in [`simulations/classical/channel_cost.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/channel_cost.py). Pool `"A"` is the original 58-point Haar-containing table; `"ml"` is the 38-point Margolus–Levitin Stage 2 pool of [procedural-share-mlpool.md](procedural-share-mlpool.md) §9.

## 4. Warnings

- **Binning sensitivity.** Williams–Beer on a few dozen binned points (38 on pool A-ml, 58 on pool A) is binning-sensitive. Changing the bin count, or switching equal-width for quantile, can move mass between redundancy, unique information and synergy. Any future run on those tables should report the binning rule and a small sensitivity check; this module does not perform that run.
- **Sources that are functions of \((g,p)\).** Under uniform input, B′ equals the map entropy A0. In the CE-6 one-bit run, all four channel costs are \(f\)-independent: they are deterministic functions of \((g,p)\) ([channel-cost-stage2.md](channel-cost-stage2.md) §1). A PID of B′ and C± versus \(D\) on those points is a PID of two functions of the channel parameters versus the deficit, not a PID of anything that sees \(f\).
- **Known limitations of \(I_{\min}\).** Williams–Beer \(I_{\min}\) can over-count redundancy when two independent sources are copied into the target. On the two-bit COPY gate (\(T=(S_1,S_2)\), \(S_1\perp S_2\) fair bits) it assigns 1 bit of redundancy and 1 bit of synergy, with both unique atoms zero. An independent-source reading of the same gate would assign the two unique bits and no redundancy. This is a documented property of \(I_{\min}\), pointed out by Harder, Salge and Polani (2013) and by Bertschinger, Rauh, Olbrich, Jost and Ay (2014). The tests assert the Williams–Beer values, not the independent-source alternative. This module does not implement later proposals (\(I_{\mathrm{BROJA}}\) and others).

## 5. Synthetic checks (the only numbers this module produces)

The following Williams–Beer values are computed from exact finite joints, in bits, and are checked by the unit tests and by `python simulations/classical/pid_williams_beer.py`. They are not Stage 2 results.

| Gate | Construction | Red | Uniq\(_1\) | Uniq\(_2\) | Syn |
|---|---|---|---|---|---|
| XOR | \(T=S_1\oplus S_2\), \(S_1\perp S_2\) fair | 0 | 0 | 0 | 1 |
| AND | \(T=S_1\land S_2\), \(S_1\perp S_2\) fair | \(h_2(1/4)-\frac12\approx 0.311278\) | 0 | 0 | \(\frac12\) |
| COPY | \(T=(S_1,S_2)\), \(S_1\perp S_2\) fair | 1 | 0 | 0 | 1 |
| RDN | \(S_1=S_2=T\) fair | 1 | 0 | 0 | 0 |
| UNQ | \(T=S_1\), \(S_2\) independent unused fair bit | 0 | 1 | 0 | 0 |

The tests also check that the atoms sum to \(I(T;S_1,S_2)\) and stay non-negative on random pmfs, that a dict joint agrees with the equivalent array, and that the adapter is deterministic (including “a point of weight 2 equals a duplicated unit-weight point,” and that already-discrete XOR bits with two equal-width bins recover the XOR atoms).

`example_joint(name)` and `EXAMPLE_ATOMS` in the module return these joints and the documented atoms.

## 6. Scope

Tier 2 only. A dormant bookkeeping tool for a one-qubit GAD toy, should the channel-cost line be revisited. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this module. No partial-information atom has been estimated from the 38- or 58-point tables.
