# Procedural share H(F|Y) on the generalized amplitude damping channel (Tier 2 toy)

**Tier:** 2 of 3, a **toy model and proof-of-concept for the shape of a curve**. It uses only classical output distributions of a one-qubit channel.

- It is **not** evidence about hadronic or QCD physics.
- It makes **no claim that noise is optionality**. "Noise is the channel pre-paying for optionality" is Cyotee's conjecture, stated here as a conjecture.
- It makes no quantum or thermodynamic claim.

**Status:** 2026-11-26 · computed.

- Accounting inequality: **fails at most points** (§4).
- Predicted concave, saturating shape: **not observed** (§5).

**Script:** [`simulations/classical/procedural_share.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share.py) (pure numpy; imports the [thermal-channel-cost](thermal-channel-cost.md) script for its Kraus helpers; built-in self-checks; about 20 s). Every number below is printed by the script.

## 1. Definitions under test

- **Procedural share** \(=H(F\mid Y)\): the expected number of bits needed to name which member of the candidate class is live, given the output.
- **Semantic share** \(=I(X;Y)\).
- **Inequality to verify, not assume:** \(I(X;Y)+H(F\mid Y)\le H(Y)\). Since \(I(X;Y)=H(Y)-H(Y\mid X)\), this is equivalent to \(H(F\mid Y)\le H(Y\mid X)\).
- *Analogy (Cyotee's framing):* realized microstate = asset, procedural overhang = liability, total capacity = credit line.

## 2. Model (fixed before any result was computed)

**Channel.** We use the generalized amplitude damping (GAD) channel with Kraus operators

- \(A_0=\sqrt p\,\begin{pmatrix}1&0\\0&\sqrt{1-g}\end{pmatrix}\), \(A_1=\sqrt p\,\begin{pmatrix}0&\sqrt g\\0&0\end{pmatrix}\),
- \(A_2=\sqrt{1-p}\,\begin{pmatrix}\sqrt{1-g}&0\\0&1\end{pmatrix}\), \(A_3=\sqrt{1-p}\,\begin{pmatrix}0&0\\\sqrt g&0\end{pmatrix}\).

Here \(g\in[0,1]\) is the damping and \(p\) is the bath's ground-state population.

- This matches Nielsen & Chuang §8.3.5 and Khatri, Sharma & Wilde (arXiv:1903.07747), whose \(N\) equals \(1-p\) and whose \(\beta=\ln((1-N)/N)\) gives the same map.
- The script checks that the Kraus set is trace preserving, that the fixed point is \(\mathrm{diag}(p,1-p)\), and that \(p=1\) gives amplitude damping.
- Temperature: \(p=1/(1+e^{-\beta\omega})\) with \(\hbar\omega=k_B=1\), so \(T=1/\ln(p/(1-p))\). The range \(p\in[1/2,1]\) is exactly \(T\ge0\): \(p=1\) is \(T=0\), and \(p=1/2\) is \(T=\infty\).

**Classical interface.** The input \(X\in\{0,1\}\) is encoded as \(|X\rangle\), and \(Y\) is a Z-measurement. This gives \(P(Y{=}1\mid X{=}0)=(1-p)g\) and \(P(Y{=}1\mid X{=}1)=1-pg\).

**Input law \(\pi(X)\).** Two choices: (i) uniform; (ii) capacity-achieving for the induced binary channel \(X\to Y\), computed by Blahut–Arimoto. The second is *not* the Holevo-optimal ensemble.

**Candidate pools.** Both are fixed in code and independent of the channel: no AD or GAD members, and nothing parametrized by \(g\) or \(p\). Each candidate is reduced to its conditional law \((P_c(Y{=}1\mid X{=}0),\,P_c(Y{=}1\mid X{=}1))\).

- **Pool A** (50 candidates, 29 distinct laws, \(\log_2 50=5.64\)):
  - all Boolean \(f:\{0,1\}^n\to\{0,1\}\) for \(n=1,2\) (4 + 16). The first argument is \(X\); any extra argument is an independent uniform bit.
  - I, X, Y, Z, H, S, full dephasing, Z-measurement, reset to \(|0\rangle\), reset to \(|1\rangle\), each applied to \(|X\rangle\) and then read out in Z.
  - 20 Haar-random unitaries (numpy `default_rng(11)`).
- **Pool B** (296 candidates, 65 distinct laws, \(\log_2 296=8.21\)), used as the robustness check:
  - all Boolean functions with \(n=3\) (256, with two auxiliary uniform bits);
  - 40 random CPTP maps (a random 2-qubit unitary acting on the system plus an ancilla in \(|0\rangle\), with the ancilla traced out; `default_rng(23)`).

**Joint model, variant (a): a hard ε-class, with every quantity taken from one joint law.**

- The class is \(C_\varepsilon=\{c:\max_x \mathrm{TV}(P_c(\cdot\mid x),P_{\rm GAD}(\cdot\mid x))\le\varepsilon\}\), with \(\varepsilon\in\{0.02,0.05,0.1\}\) (default 0.05).
- \(F\) is uniform on \(C_\varepsilon\); \(X\sim\pi\) is independent of \(F\); and \(Y\mid F,X\sim P_F(\cdot\mid X)\).
- The posterior \(P(F\mid Y)\) comes from Bayes' rule using each candidate's own law.

**Variant (b): the full pool, uniform prior, likelihood posterior.**

- \(P(F\mid y)\propto P_F(y)\), where \(P_F(y)=\sum_x\pi(x)P_F(y\mid x)\).
- \(y\) is drawn from the real GAD channel. The procedural share is \(\sum_y P_{\rm GAD}(y)\,H(P(F\mid y))\), a cross (mismatched-model) conditional entropy.
- \(I(X;Y)\) and \(H(Y)\) are those of the GAD channel.

**Grid.** \(g\) runs over \([0,1]\) and \(p\) over \([1/2,1]\), both in steps of 0.05 (231 points). The 1D slices use steps of 0.01.

## 3. Results

**Slices vs \(g\)** (pool A, uniform input, \(\varepsilon=0.05\)). Each cell lists \(\lvert C\rvert\), \(H(F\mid Y)\) for (a), \(H(F\mid Y)\) for (b), \(I(X;Y)\) and \(H(Y)\); "-" means the class is empty.

| g | T=0.0: \|C\|, a, b, I, H(Y) | T=0.5: \|C\|, a, b, I, H(Y) | T=1.0: \|C\|, a, b, I, H(Y) | T=2.0: \|C\|, a, b, I, H(Y) | T=inf: \|C\|, a, b, I, H(Y) |
|---|---|---|---|---|---|
| 0.0 | 8, 3.00, 5.49, 1.00, 1.00 | 8, 3.00, 5.49, 1.00, 1.00 | 8, 3.00, 5.49, 1.00, 1.00 | 8, 3.00, 5.49, 1.00, 1.00 | 8, 3.00, 5.49, 1.00, 1.00 |
| 0.1 | 0, -, 5.49, 0.76, 0.99 | 0, -, 5.49, 0.73, 1.00 | 1, 0.00, 5.49, 0.72, 1.00 | 2, 1.00, 5.49, 0.72, 1.00 | 9, 3.17, 5.49, 0.71, 1.00 |
| 0.2 | 0, -, 5.49, 0.61, 0.97 | 0, -, 5.49, 0.57, 0.98 | 0, -, 5.49, 0.54, 0.99 | 3, 1.58, 5.49, 0.53, 1.00 | 4, 2.00, 5.49, 0.53, 1.00 |
| 0.3 | 0, -, 5.49, 0.49, 0.93 | 0, -, 5.49, 0.43, 0.96 | 0, -, 5.49, 0.40, 0.99 | 2, 1.00, 5.49, 0.39, 1.00 | 4, 2.00, 5.49, 0.39, 1.00 |
| 0.4 | 0, -, 5.49, 0.40, 0.88 | 0, -, 5.49, 0.33, 0.93 | 0, -, 5.49, 0.29, 0.98 | 0, -, 5.49, 0.28, 0.99 | 1, 0.00, 5.49, 0.28, 1.00 |
| 0.5 | 2, 1.00, 5.49, 0.31, 0.81 | 0, -, 5.49, 0.23, 0.89 | 0, -, 5.49, 0.20, 0.96 | 0, -, 5.49, 0.19, 0.99 | 0, -, 5.49, 0.19, 1.00 |
| 0.6 | 0, -, 5.49, 0.24, 0.72 | 0, -, 5.49, 0.16, 0.84 | 0, -, 5.49, 0.13, 0.94 | 0, -, 5.49, 0.12, 0.98 | 0, -, 5.49, 0.12, 1.00 |
| 0.7 | 0, -, 5.49, 0.17, 0.61 | 0, -, 5.49, 0.10, 0.78 | 0, -, 5.49, 0.07, 0.92 | 0, -, 5.49, 0.07, 0.98 | 3, 1.58, 5.49, 0.07, 1.00 |
| 0.8 | 0, -, 5.49, 0.11, 0.47 | 0, -, 5.49, 0.05, 0.71 | 0, -, 5.49, 0.03, 0.90 | 0, -, 5.49, 0.03, 0.97 | 4, 2.00, 5.49, 0.03, 1.00 |
| 0.9 | 0, -, 5.49, 0.05, 0.29 | 0, -, 5.49, 0.01, 0.63 | 0, -, 5.49, 0.01, 0.87 | 0, -, 5.49, 0.01, 0.96 | 6, 2.58, 5.49, 0.01, 1.00 |
| 1.0 | 3, 1.58, 5.49, 0.00, 0.00 | 0, -, 5.49, 0.00, 0.53 | 0, -, 5.49, 0.00, 0.84 | 0, -, 5.49, 0.00, 0.96 | 5, 2.32, 5.49, 0.00, 1.00 |

**Slices vs \(T\)** (same settings). Each cell lists \(\lvert C\rvert\), (a), (b) and \(I(X;Y)\).

| p | T | g=0.25 | g=0.5 | g=0.75 | g=1.0 |
|---|---|---|---|---|---|
| 1.00 | 0.000 | 0, -, 5.49, 0.55 | 2, 1.00, 5.49, 0.31 | 0, -, 5.49, 0.14 | 3, 1.58, 5.49, 0.00 |
| 0.95 | 0.340 | 0, -, 5.49, 0.52 | 2, 1.00, 5.49, 0.27 | 0, -, 5.49, 0.09 | 3, 1.58, 5.49, 0.00 |
| 0.90 | 0.455 | 0, -, 5.49, 0.50 | 2, 1.00, 5.49, 0.24 | 0, -, 5.49, 0.07 | 0, -, 5.49, 0.00 |
| 0.85 | 0.577 | 0, -, 5.49, 0.49 | 0, -, 5.49, 0.23 | 0, -, 5.49, 0.06 | 0, -, 5.49, 0.00 |
| 0.80 | 0.721 | 0, -, 5.49, 0.48 | 0, -, 5.49, 0.21 | 0, -, 5.49, 0.06 | 0, -, 5.49, 0.00 |
| 0.75 | 0.910 | 0, -, 5.49, 0.47 | 0, -, 5.49, 0.21 | 0, -, 5.49, 0.05 | 0, -, 5.49, 0.00 |
| 0.70 | 1.180 | 0, -, 5.49, 0.47 | 0, -, 5.49, 0.20 | 0, -, 5.49, 0.05 | 0, -, 5.49, 0.00 |
| 0.65 | 1.615 | 1, 0.00, 5.49, 0.46 | 0, -, 5.49, 0.19 | 0, -, 5.49, 0.05 | 0, -, 5.49, 0.00 |
| 0.60 | 2.466 | 3, 1.58, 5.49, 0.46 | 0, -, 5.49, 0.19 | 0, -, 5.49, 0.05 | 0, -, 5.49, 0.00 |
| 0.55 | 4.983 | 4, 2.00, 5.49, 0.46 | 0, -, 5.49, 0.19 | 2, 1.00, 5.49, 0.05 | 5, 2.32, 5.49, 0.00 |
| 0.50 | inf | 5, 2.32, 5.49, 0.46 | 0, -, 5.49, 0.19 | 4, 2.00, 5.49, 0.05 | 5, 2.32, 5.49, 0.00 |

## 4. The accounting inequality: verdict **fails at most points**

| variant | pool | input | eps | defined pts | holds | fails | fails when log2\|class\| > H(Y)+H(Y\|X) (sufficient) | max violation (bits) | I(X;Y)+I(F;Y) <= H(Y) holds |
|---|---|---|---|---|---|---|---|---|---|
| (a) eps-class | A | uniform | 0.02 | 34 | 16 | 18 | 13 | 2.807 | yes |
| (a) eps-class | A | uniform | 0.05 | 72 | 14 | 58 | 40 | 3.076 | yes |
| (a) eps-class | A | uniform | 0.1 | 128 | 9 | 119 | 85 | 3.414 | yes |
| (b) full pool | A | uniform | - | 231 | 0 | 231 | - | 5.494 | n/a |
| (a) eps-class | A | capacity | 0.02 | 34 | 16 | 18 | 13 | 2.807 | yes |
| (a) eps-class | A | capacity | 0.05 | 72 | 14 | 58 | 40 | 3.076 | yes |
| (a) eps-class | A | capacity | 0.1 | 128 | 9 | 119 | 85 | 3.414 | yes |
| (b) full pool | A | capacity | - | 231 | 0 | 231 | - | 5.494 | n/a |
| (a) eps-class | B | uniform | 0.02 | 25 | 17 | 8 | 8 | 4.170 | yes |
| (a) eps-class | B | uniform | 0.05 | 103 | 60 | 43 | 43 | 4.209 | yes |
| (a) eps-class | B | uniform | 0.1 | 218 | 72 | 146 | 130 | 4.321 | yes |
| (b) full pool | B | uniform | - | 231 | 0 | 231 | - | 8.119 | n/a |
| (a) eps-class | B | capacity | 0.02 | 25 | 17 | 8 | 8 | 4.170 | yes |
| (a) eps-class | B | capacity | 0.05 | 103 | 60 | 43 | 43 | 4.209 | yes |
| (a) eps-class | B | capacity | 0.1 | 218 | 72 | 146 | 130 | 4.321 | yes |
| (b) full pool | B | capacity | - | 231 | 0 | 231 | - | 8.119 | n/a |

**Why it fails (analytic).** The inequality is equivalent to \(H(F\mid Y)\le H(Y\mid X)\). The right-hand side is at most 1 bit, because \(Y\) is a single bit. The left-hand side is the uncertainty over the class:

- In (a), \(F\) is independent of \(X\), and \(H(F\mid Y)=\log_2\lvert C\rvert-I(F;Y)\ge\log_2\lvert C\rvert-H(Y)\). So the inequality **must fail whenever \(\log_2\lvert C\rvert>H(Y)+H(Y\mid X)\)**, which is guaranteed for any class with more than 4 members. It holds only where the class is tiny, so that one output bit can nearly name the live member.
- In (b), \(H(F\mid Y)\ge\log_2\lvert\text{pool}\rvert-1\), so it fails at all 231 points for both pools.

This is the "large class whose members give similar outputs" failure: one output bit cannot carry several bits of class identity. **The quantities were not redefined to rescue the inequality.**

**Correct statements, reported separately as different statements:**

- \(H(Y)=I(X;Y)+H(Y\mid X)\) holds exactly (an identity).
- In (a), because \(F\) and \(X\) are independent, \(I(X;Y)+I(F;Y)\le I(X,F;Y)\le H(Y)\). The script verifies this at every defined point, as the last column shows.

So the bounded quantity is the **information about \(F\) that is revealed**, \(I(F;Y)\), not the residual uncertainty \(H(F\mid Y)\).

## 5. Shape: the predicted concave, saturating curve is **not observed**

The tests use the sign of the interior discrete second derivative (on two grids, 0.05 and 0.01), monotonicity, and saturation. A curve counts as saturated at the first point after which it stays within 2 % of its range of its end value. The script prints the full table; the tally is:

> Shape tally over all slices above: (a) other: 4; (a) step artifact: 60; (a) undefined (empty classes): 8; (b) constant/flat: 18; (b) other: 2

**Deviations from the prediction (every one found):**

1. **(a) is a step artifact.** \(H(F\mid Y)\) is piecewise constant in \(g\) and \(T\), because it is a function of a finite hard class. 60 of 72 slices are labelled step artifact, and all are non-monotone or have mixed curvature.
   - The class is empty at many grid points (pool A, \(\varepsilon=0.05\): only 72 of 231 points are defined). The GAD law moves continuously while the pool's laws are fixed points.
   - The remaining 4 slices are built from very few defined points: two "concave" single bumps that start and end at 0, and two convex step-ups. None is monotone and concave.
   - On pool A, (a) generally *falls* from \(g=0\), where 8 members (identity-like and reset ops) match exactly, rather than rising.
2. **(b) is flat or constant.** With uniform input on pool A, (b) is exactly constant (5.494 bits), because pool A is symmetric under output flips. On pool B it varies by less than 0.001 bit.
   - Analytically, with uniform input (b) is **exactly linear in \(g\)** at fixed \(T\): it equals \(\sum_y P_{\rm GAD}(y)h_y\) with constants \(h_y\) fixed by the pool, and \(P_{\rm GAD}(Y{=}1)=\tfrac12-\tfrac{g(2p-1)}2\). It has no curvature at all.
3. **"Saturation" is not a plateau reached late.**
   - (b) sits at 0.973 (pool A) and 0.989 (pool B) of \(\log_2\lvert\text{pool}\rvert\) at every grid point. It is at its ceiling from the start, because one output bit can remove at most 1 bit.
   - The maxima of (a) reach only 0.31–0.66 of \(\log_2\lvert\text{pool}\rvert\), and they come from step segments, not plateaus.
   - Nowhere does a curve rise and then flatten toward \(\log_2\lvert\text{pool}\rvert\).
4. **The one slice that resembles the prediction is not robust.** Pool A, capacity-achieving input, plotted against \(T\) at \(g=0.5\), is non-decreasing and mostly concave (47 concave / 1 convex interior points).
   - Its total rise is 0.013 bit (5.481 → 5.494), about 0.2 % of \(\log_2\lvert\text{pool}\rvert\). It is caused by the Blahut–Arimoto input law drifting toward uniform as \(T\) rises.
   - The same slice on pool B is flat (0.004 bit).

## 6. Branching width vs noise amplitude

Correlations over the 2D grid (uniform input, \(\varepsilon=0.05\)), Spearman with Pearson in brackets:

| variant | pool | vs log2\|class\| | vs \|class\| | vs 1 - C_bin | vs purity loss (\|+>) | vs 1 - sqrt(1-g) | vs g |
|---|---|---|---|---|---|---|---|
| (a) | A | 1.00 (1.00) | 1.00 (0.96) | -0.53 (-0.50) | -0.52 (-0.30) | -0.55 (-0.21) | -0.55 (-0.32) |
| (b) | A | n/a (fixed pool) | n/a | H(F\|Y) range 1.78e-15 bit: correlations not meaningful | | | |
| (a) | B | 1.00 (1.00) | 1.00 (0.91) | 0.30 (0.39) | 0.34 (0.39) | 0.31 (0.34) | 0.31 (0.36) |
| (b) | B | n/a (fixed pool) | n/a | H(F\|Y) range 8.18e-04 bit: correlations not meaningful | | | |

- **Against branching width:** in (a), \(H(F\mid Y)\) correlates perfectly with \(\log_2\lvert C\rvert\). That is **built into the definition**: \(H(F\mid Y)=\log_2\lvert C\rvert-I(F;Y)\) with \(0\le I(F;Y)\le1\). It is not an independent confirmation that the share "tracks branching width".
- **Against noise:** the correlations with standard decoherence measures change sign between pools (−0.55 on pool A, +0.31 on pool B), so there is no robust relation either way.
- In (b), the share hardly varies, so correlations are not meaningful.

## 7. Status and non-claims

- The model choices in §2 are conventions of this toy. Other joint models, such as several observations or conditioning on \(X\), would give different numbers.
- The inequality \(I(X;Y)+H(F\mid Y)\le H(Y)\) is **false in general** and false at most points here. The correct bound is \(I(X;Y)+I(F;Y)\le H(Y)\) when \(F\) is independent of \(X\).
- Nothing here bears on hadronic or QCD physics, on gravity, or on whether noise "is" anything. The conjecture remains Cyotee's framing.
- **Tier placement:** GAD is a quantum channel, but only the classical output laws of a single qubit read out in Z are used. As in the [thermal-channel-cost](thermal-channel-cost.md) note, this is labelled a Tier 2 toy.
