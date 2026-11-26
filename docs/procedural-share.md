# Procedural share H(F|Y) on the generalized amplitude damping channel (Tier 2 toy)

**Tier:** 2 of 3, a **toy model and proof-of-concept for the shape of a curve**. It uses only classical output distributions of a one-qubit channel.

- It is **not** evidence about hadronic or QCD physics.
- It makes **no claim that noise is optionality**. "Noise is the channel pre-paying for optionality" is Cyotee's conjecture, stated here as a conjecture.
- It makes no quantum or thermodynamic claim.

**Status:** 2026-11-26 · computed.

- Accounting inequality: **fails at most points** (§4).
- Predicted concave, saturating shape: **not observed** (§5).
- 16-symbol rerun (§8): the original inequality now holds at 44/72 points (pool A) and 60/103 (pool B). The share now moves with \(g\), but it falls with damping and tracks output bias. The bottleneck is the pool's distinct output laws, not the alphabet.
- Follow-up: [procedural-share surface over noise × readout rank](procedural-share-surface.md), a two-qubit toy whose candidate pool is drawn independently of the channel.

**Script:** [`simulations/classical/procedural_share.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share.py) (pure numpy; imports the [thermal-channel-cost](thermal-channel-cost.md) script for its Kraus helpers; built-in self-checks; about 20 s). Every number below is printed by the script. §3–§6 are the CE-6 one-bit run, reproduced with `--alphabet 2`; §8 is the 16-symbol run, which is now the default.

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

## 8. 16-symbol output alphabet: 4 channel uses (added 2026-11-26)

*Run: `python simulations/classical/procedural_share.py` (now the default, `--alphabet 16`, about 22 s). `--alphabet 2` reproduces §3–§6 byte-for-byte. The pools, the GAD channel, the grid, ε, and the shape and correlation tests are unchanged.*

### 8.1 Realization

One qubit read out with **any** measurement, however many outcomes it has, carries at most 1 bit of accessible information (Holevo bound). A 16-outcome measurement on a single qubit therefore cannot lift the 1-bit cap.

The 16 symbols are instead realized as **4 independent uses** of the channel:

- the channel is \(\mathrm{GAD}^{\otimes4}\), read out by a product Z measurement, so \(Y\in\{0,1\}^4\);
- the input \(X\in\{0,1\}^4\) is i.i.d., either uniform or with the 1-use Blahut–Arimoto law on each use;
- each candidate acts as \(F^{\otimes4}\), so its law factorizes over the uses and the script uses that product directly.

\(I(X;Y)\) and \(H(Y)\) below are per 4 uses unless marked "per use". For the GAD channel, \(I(X;Y)\) per 4 uses is exactly 4 × the 1-use value (self-checked).

A single 16-level system would be a different channel, not GAD, so it was not added.

### 8.2 Why the alphabet is not the main bottleneck (analytic, self-checked)

- **Only the count of 1s in \(Y\) matters.** With \(X\) unobserved and i.i.d., \(P_F(y)=\prod_i r_F(y_i)\), where \(r_F(1)=\pi_0q_0+\pi_1q_1\) is the candidate's 1-use output marginal. \(Y\) therefore enters only through its Hamming weight \(W\in\{0,\dots,4\}\), so \(I(F;Y)=I(F;W)\le\log_2 5=2.32\) bits, not 4.
- **Candidates with the same output marginal can never be told apart from \(Y\), for any number of uses.** \(H(F\mid Y)\) therefore has a floor of \(\sum_L (n_L/N)\log_2 n_L\), where \(L\) runs over distinct marginals.
- If \(X\) is observed as well, \(F\) enters through the counts of each \((x_i,y_i)\) pair, and the floor uses the distinct *conditional* laws instead.

| pool | N | log2 N | distinct cond. laws | distinct output marginals (uniform pi) | floor H(F\|marginal) | floor H(F\|cond. law) | max I(F;Y) any k = log2N - floor | cap now log2(k+1) | min gap between marginals |
|---|---|---|---|---|---|---|---|---|---|
| A | 50 | 5.644 | 29 | 5 | 4.233 | 1.135 | 1.411 | 2.322 | 0.2500 |
| B | 296 | 8.209 | 65 | 49 | 4.719 | 3.406 | 3.491 | 2.322 | 0.0001 |

- **Pool A:** only 5 distinct output marginals (0, ¼, ½, ¾, 1; every Haar unitary gives ½). So from \(Y\) alone, \(I(F;Y)\le1.41\) bits whatever the alphabet. That is already below the 4-use cap of 2.32, so **for pool A the distinct-law count is the bottleneck, not the alphabet.**
- **Pool B:** 49 distinct marginals, with a ceiling of 3.49 bits, above 2.32. Here 4 uses are still partly limiting, but the floor of 4.72 bits (57 % of \(\log_2 296\)) can never be beaten.

### 8.3 Inequalities: pass rates vs CE-6

| variant | pool | input | eps | defined pts | holds | fails | fails when log2\|class\| > H(Y)+H(Y\|X) (sufficient) | max violation (bits) | I(X;Y)+I(F;Y) <= H(Y) holds |
|---|---|---|---|---|---|---|---|---|---|
| (a) eps-class | A | uniform | 0.02 | 34 | 22 | 12 | 1 | 2.807 | yes |
| (a) eps-class | A | uniform | 0.05 | 72 | 44 | 28 | 3 | 2.868 | yes |
| (a) eps-class | A | uniform | 0.1 | 128 | 68 | 60 | 6 | 2.802 | yes |
| (b) full pool | A | uniform | - | 231 | 0 | 231 | - | 5.274 | n/a |
| (a) eps-class | A | capacity | 0.02 | 34 | 22 | 12 | 1 | 2.807 | yes |
| (a) eps-class | A | capacity | 0.05 | 72 | 44 | 28 | 3 | 2.868 | yes |
| (a) eps-class | A | capacity | 0.1 | 128 | 68 | 60 | 6 | 2.802 | yes |
| (b) full pool | A | capacity | - | 231 | 0 | 231 | - | 5.274 | n/a |
| (a) eps-class | B | uniform | 0.02 | 25 | 17 | 8 | 0 | 1.170 | yes |
| (a) eps-class | B | uniform | 0.05 | 103 | 60 | 43 | 0 | 1.209 | yes |
| (a) eps-class | B | uniform | 0.1 | 218 | 89 | 129 | 0 | 1.319 | yes |
| (b) full pool | B | uniform | - | 231 | 0 | 231 | - | 7.965 | n/a |
| (a) eps-class | B | capacity | 0.02 | 25 | 17 | 8 | 0 | 1.170 | yes |
| (a) eps-class | B | capacity | 0.05 | 103 | 60 | 43 | 0 | 1.209 | yes |
| (a) eps-class | B | capacity | 0.1 | 218 | 89 | 129 | 0 | 1.319 | yes |
| (b) full pool | B | capacity | - | 231 | 0 | 231 | - | 7.965 | n/a |

| Check | CE-6 (1 bit) | CE-7 (16 symbols) |
|---|---|---|
| original, (a), pool A, ε = 0.05 | 14 / 72 | **44 / 72** |
| original, (a), pool B, ε = 0.05 | 60 / 103 | **60 / 103** |
| original, (b), both pools | 0 / 231 | **0 / 231** |
| corrected \(I(X;Y)+I(F;Y)\le H(Y)\), (a) | all points | **all points** |

**Why (a) improves.** In (a), \(I(F;Y)=0.00\) at every point. The ε-class members share their output marginal: they are law-duplicates such as I, Z, S, dephasing, Z-measurement and the Boolean identity at \(g=0\). So \(H(F\mid Y)=\log_2\lvert C\rvert\) exactly, and the original inequality holds iff \(\log_2\lvert C\rvert\le H(Y\mid X)\). The right-hand side can now reach 4 bits instead of 1, so more points pass.

**Why (b) still fails everywhere.** \(H(F\mid Y)\ge\log_2N-I(F;Y)\ge\log_2N-2.32\), which exceeds \(H(Y\mid X)\) at every grid point.

### 8.4 Results (uniform input, ε = 0.05)

Each cell lists: \(\lvert C\rvert\); \(H(F\mid Y)\), \(I(F;Y)\) and \(H(F\mid X,Y)\) for (a); \(H(F\mid Y)\) and \(\log_2N-H(F\mid Y)\) for (b); \(I(X;Y)\) per use; and \(H(Y)\) per 4 uses.

Pool A:

| g | T=0.0 | T=1.0 | T=inf |
|---|---|---|---|
| 0.0 | 8, 3.00, 0.00, 2.96, 5.274, 0.370, 1.000, 4.00 | 8, 3.00, 0.00, 2.96, 5.274, 0.370, 1.000, 4.00 | 8, 3.00, 0.00, 2.96, 5.274, 0.370, 1.000, 4.00 |
| 0.1 | 0, -, -, -, 5.266, 0.377, 0.758, 3.97 | 1, 0.00, 0.00, 0.00, 5.272, 0.371, 0.720, 3.99 | 9, 3.17, 0.00, 3.06, 5.274, 0.370, 0.714, 4.00 |
| 0.2 | 0, -, -, -, 5.244, 0.400, 0.610, 3.88 | 0, -, -, -, 5.268, 0.376, 0.543, 3.98 | 4, 2.00, 0.00, 1.98, 5.274, 0.370, 0.531, 4.00 |
| 0.3 | 0, -, -, -, 5.205, 0.438, 0.493, 3.74 | 0, -, -, -, 5.259, 0.384, 0.404, 3.94 | 4, 2.00, 0.00, 1.99, 5.274, 0.370, 0.390, 4.00 |
| 0.4 | 0, -, -, -, 5.151, 0.493, 0.396, 3.53 | 0, -, -, -, 5.248, 0.396, 0.293, 3.90 | 1, 0.00, 0.00, 0.00, 5.274, 0.370, 0.278, 4.00 |
| 0.5 | 2, 1.00, 0.00, 1.00, 5.080, 0.564, 0.311, 3.25 | 0, -, -, -, 5.233, 0.410, 0.203, 3.84 | 0, -, -, -, 5.274, 0.370, 0.189, 4.00 |
| 0.6 | 0, -, -, -, 4.990, 0.654, 0.236, 2.89 | 0, -, -, -, 5.215, 0.428, 0.130, 3.78 | 0, -, -, -, 5.274, 0.370, 0.119, 4.00 |
| 0.7 | 0, -, -, -, 4.882, 0.762, 0.169, 2.44 | 0, -, -, -, 5.194, 0.450, 0.074, 3.69 | 3, 1.58, 0.00, 1.58, 5.274, 0.370, 0.066, 4.00 |
| 0.8 | 0, -, -, -, 4.753, 0.891, 0.108, 1.88 | 0, -, -, -, 5.169, 0.475, 0.034, 3.60 | 4, 2.00, 0.00, 2.00, 5.274, 0.370, 0.029, 4.00 |
| 0.9 | 0, -, -, -, 4.602, 1.042, 0.052, 1.15 | 0, -, -, -, 5.141, 0.503, 0.009, 3.49 | 6, 2.58, 0.00, 2.57, 5.274, 0.370, 0.007, 4.00 |
| 1.0 | 3, 1.58, 0.00, 1.58, 4.426, 1.218, 0.000, 0.00 | 0, -, -, -, 5.109, 0.535, 0.000, 3.36 | 5, 2.32, 0.00, 2.32, 5.274, 0.370, 0.000, 4.00 |

Pool B:

| g | T=0.0 | T=1.0 | T=inf |
|---|---|---|---|
| 0.0 | 1, 0.00, 0.00, 0.00, 7.965, 0.245, 1.000, 4.00 | 1, 0.00, 0.00, 0.00, 7.965, 0.245, 1.000, 4.00 | 1, 0.00, 0.00, 0.00, 7.965, 0.245, 1.000, 4.00 |
| 0.1 | 0, -, -, -, 7.958, 0.251, 0.758, 3.97 | 0, -, -, -, 7.963, 0.246, 0.720, 3.99 | 1, 0.00, 0.00, 0.00, 7.965, 0.245, 0.714, 4.00 |
| 0.2 | 4, 2.00, 0.00, 2.00, 7.940, 0.269, 0.610, 3.88 | 0, -, -, -, 7.959, 0.251, 0.543, 3.98 | 0, -, -, -, 7.965, 0.245, 0.531, 4.00 |
| 0.3 | 4, 2.00, 0.00, 2.00, 7.911, 0.299, 0.493, 3.74 | 0, -, -, -, 7.952, 0.257, 0.404, 3.94 | 1, 0.00, 0.00, 0.00, 7.965, 0.245, 0.390, 4.00 |
| 0.4 | 0, -, -, -, 7.870, 0.339, 0.396, 3.53 | 1, 0.00, 0.00, 0.00, 7.944, 0.266, 0.293, 3.90 | 16, 4.00, 0.00, 4.00, 7.965, 0.245, 0.278, 4.00 |
| 0.5 | 6, 2.58, 0.00, 2.58, 7.818, 0.392, 0.311, 3.25 | 0, -, -, -, 7.932, 0.277, 0.203, 3.84 | 16, 4.00, 0.00, 4.00, 7.965, 0.245, 0.189, 4.00 |
| 0.6 | 0, -, -, -, 7.754, 0.456, 0.236, 2.89 | 0, -, -, -, 7.919, 0.291, 0.130, 3.78 | 17, 4.09, 0.00, 4.08, 7.965, 0.245, 0.119, 4.00 |
| 0.7 | 4, 2.00, 0.00, 2.00, 7.677, 0.532, 0.169, 2.44 | 0, -, -, -, 7.902, 0.307, 0.074, 3.69 | 0, -, -, -, 7.965, 0.245, 0.066, 4.00 |
| 0.8 | 4, 2.00, 0.00, 2.00, 7.589, 0.621, 0.108, 1.88 | 1, 0.00, 0.00, 0.00, 7.884, 0.326, 0.034, 3.60 | 1, 0.00, 0.00, 0.00, 7.965, 0.245, 0.029, 4.00 |
| 0.9 | 0, -, -, -, 7.488, 0.722, 0.052, 1.15 | 0, -, -, -, 7.863, 0.347, 0.009, 3.49 | 37, 5.21, 0.00, 5.21, 7.965, 0.245, 0.007, 4.00 |
| 1.0 | 1, 0.00, 0.00, 0.00, 7.374, 0.836, 0.000, 0.00 | 16, 4.00, 0.00, 4.00, 7.839, 0.370, 0.000, 3.36 | 36, 5.17, 0.00, 5.17, 7.965, 0.245, 0.000, 4.00 |

### 8.5 Shape

The tally over all slices:

> Shape tally over all slices above: (a) other: 5; (a) step artifact: 59; (a) undefined (empty classes): 8; (b) concave & monotone: 7; (b) constant/flat: 4; (b) other: 9

The (b) slices:

| variant | pool | input | eps | grid | slice | shape | start → end (min..max) | saturates at | plateau vs log2\|pool\| |
|---|---|---|---|---|---|---|---|---|---|
| (b) | A | uniform | - | dg=0.01 | vs g, T=0.0 | non-increasing, concave | 5.274 → 4.426 (4.426..5.274) | 1.00 | 0.934 of 5.64 |
| (b) | A | uniform | - | dg=0.01 | vs g, T=1.0 | non-increasing, concave | 5.274 → 5.109 (5.109..5.274) | 1.00 | 0.934 of 5.64 |
| (b) | A | uniform | - | dg=0.01 | vs g, T=inf | constant | 5.274 → 5.274 (5.274..5.274) | - | 0.934 of 5.64 |
| (b) | A | uniform | - | dp=0.01 | vs T, g=0.5 | non-decreasing, mixed curvature (42 concave / 6 convex interior pts) | 5.080 → 5.274 (5.080..5.274) | 3.55 | 0.934 of 5.64 |
| (b) | A | uniform | - | dp=0.01 | vs T, g=1.0 | non-decreasing, mixed curvature (43 concave / 5 convex interior pts) | 4.426 → 5.274 (4.426..5.274) | 3.55 | 0.934 of 5.64 |
| (b) | A | capacity | - | dg=0.01 | vs g, T=0.0 | non-increasing, concave | 5.274 → 4.426 (4.426..5.274) | 1.00 | 0.934 of 5.64 |
| (b) | A | capacity | - | dg=0.01 | vs g, T=1.0 | non-increasing, concave | 5.274 → 5.109 (5.109..5.274) | 1.00 | 0.934 of 5.64 |
| (b) | A | capacity | - | dg=0.01 | vs g, T=inf | constant | 5.274 → 5.274 (5.274..5.274) | - | 0.934 of 5.64 |
| (b) | A | capacity | - | dp=0.01 | vs T, g=0.5 | non-decreasing, mixed curvature (44 concave / 4 convex interior pts) | 4.981 → 5.274 (4.981..5.274) | 3.10 | 0.934 of 5.64 |
| (b) | A | capacity | - | dp=0.01 | vs T, g=1.0 | non-decreasing, mixed curvature (43 concave / 5 convex interior pts) | 4.426 → 5.274 (4.426..5.274) | 3.55 | 0.934 of 5.64 |
| (b) | B | uniform | - | dg=0.01 | vs g, T=0.0 | non-increasing, concave | 7.965 → 7.374 (7.374..7.965) | 1.00 | 0.970 of 8.21 |
| (b) | B | uniform | - | dg=0.01 | vs g, T=1.0 | non-increasing, concave | 7.965 → 7.839 (7.839..7.965) | 0.99 | 0.970 of 8.21 |
| (b) | B | uniform | - | dg=0.01 | vs g, T=inf | constant | 7.965 → 7.965 (7.965..7.965) | - | 0.970 of 8.21 |
| (b) | B | uniform | - | dp=0.01 | vs T, g=0.5 | non-decreasing, mixed curvature (42 concave / 6 convex interior pts) | 7.818 → 7.964 (7.818..7.964) | 4.15 | 0.970 of 8.21 |
| (b) | B | uniform | - | dp=0.01 | vs T, g=1.0 | non-decreasing, mixed curvature (42 concave / 6 convex interior pts) | 7.374 → 7.964 (7.374..7.964) | 4.15 | 0.970 of 8.21 |
| (b) | B | capacity | - | dg=0.01 | vs g, T=0.0 | non-monotone, mixed curvature (96 concave / 3 convex interior pts) | 7.965 → 7.374 (7.353..7.965) | 1.00 | 0.970 of 8.21 |
| (b) | B | capacity | - | dg=0.01 | vs g, T=1.0 | non-increasing, concave | 7.965 → 7.839 (7.839..7.965) | 0.99 | 0.970 of 8.21 |
| (b) | B | capacity | - | dg=0.01 | vs g, T=inf | constant | 7.965 → 7.965 (7.965..7.965) | - | 0.970 of 8.21 |
| (b) | B | capacity | - | dp=0.01 | vs T, g=0.5 | non-decreasing, mixed curvature (44 concave / 4 convex interior pts) | 7.742 → 7.964 (7.742..7.964) | 3.55 | 0.970 of 8.21 |
| (b) | B | capacity | - | dp=0.01 | vs T, g=1.0 | non-decreasing, mixed curvature (42 concave / 6 convex interior pts) | 7.374 → 7.964 (7.374..7.964) | 4.15 | 0.970 of 8.21 |

**(a) Does the share now move with g?** Variant (b) does, but in the **opposite direction** to the prediction.

- At \(T=0\) it **falls** with damping: pool A goes from 5.274 to 4.426 bits, pool B from 7.965 to 7.374. The curve is concave and non-increasing, and it starts at 0.934 (A) and 0.970 (B) of \(\log_2N\).
- At \(T=\infty\) it is constant.
- **Exact reason** (self-checked): with uniform input, \(H(F\mid Y)\) in (b) is a function of the GAD output bias \(b=g(2p-1)/2\) alone. Its Spearman correlation with \(b\) over the grid is −0.999 (A) and −1.000 (B). Damping biases the outputs toward 0, and more biased outputs separate the pool's marginals better.

**(b) Concave rise or saturation?**

- Against \(T\), (b) rises and is mostly concave (42–44 concave vs 4–6 convex interior points). It saturates near \(T\approx3\)–\(4\) at the unbiased-output value of 0.934 or 0.970 of \(\log_2N\).
- This is the \(p(T)\) logistic map driving the bias \(b\) to 0. It is the same kind of built-in mapping artifact as in CE-4, not class growth. The plateau is the "output unbiased" value, not \(\log_2N\) and not a full function space.
- Variant (a) is still a **step artifact** in 59 of 72 slices, with 8 undefined because of empty classes. The other 5 slices have few points and none is concave and monotone.
- Measured against \(g\), the 7 "(b) concave & monotone" slices are all **decreasing**, the opposite of the predicted rise.

### 8.6 Correlation with noise measures

| variant | pool | vs log2\|class\| | vs \|class\| | vs 1 - C_bin | vs purity loss (\|+>) | vs 1 - sqrt(1-g) | vs g |
|---|---|---|---|---|---|---|---|
| (a) | A | 1.00 (1.00) | 1.00 (0.96) | -0.52 (-0.50) | -0.53 (-0.30) | -0.54 (-0.21) | -0.54 (-0.32) |
| (b) | A | n/a (fixed pool; H(F\|Y) range 0.8478 bit) | n/a | -0.55 (-0.44) | -0.23 (0.08) | -0.63 (-0.57) | -0.63 (-0.56) |
| (a) | B | 1.00 (1.00) | 1.00 (0.91) | 0.30 (0.39) | 0.34 (0.39) | 0.31 (0.34) | 0.31 (0.36) |
| (b) | B | n/a (fixed pool; H(F\|Y) range 0.5910 bit) | n/a | -0.55 (-0.45) | -0.23 (0.07) | -0.62 (-0.58) | -0.62 (-0.56) |

- **Variant (a)** is unchanged from CE-6 and sign-unstable across pools: −0.52 to −0.54 on A, +0.30 to +0.34 on B. Its perfect correlation with \(\log_2\lvert C\rvert\) is still true by definition, because \(I(F;Y)=0\) here.
- **Variant (b)** is now defined and **sign-stable**: about −0.55 against 1 − C, and about −0.63 against \(1-\sqrt{1-g}\) and against \(g\), on both pools. It is weak against purity loss (−0.23).
- It is **negative**: the share falls as damping noise rises, because it tracks the output bias. That is a property of noise amplitude, not of branching width.

### 8.7 Was 16 enough? Estimate for a larger run (not run)

**No**, and a larger alphabet would not fix the main problem. The share now moves, by up to 0.85 bit (A) and 0.59 bit (B), but it stays at or above 0.78 (A) and about 0.90 (B) of \(\log_2N\). Its ceiling is set by the pool's **distinct output marginals**. For pool A that ceiling is 1.41 bits of identifiable information, already reachable in principle with 4 uses.

The table below estimates what a bigger run would need (rule-of-thumb uses count \(k\sim\ln M/\text{gap}^2\), order of magnitude only):

| pool | delta | merged marginals M | k needed | alphabet 2^k | I(F;Y) ceiling at delta (bits) | weight-statistic cost per 231-pt sweep | naive tensor cost per sweep |
|---|---|---|---|---|---|---|---|
| A | 0.05 | 5 | 26 | 2^26 | 1.41 | ~3.1e+05 ops (< 1 s) | ~10^20 ops (infeasible) |
| A | 0.01 | 5 | 26 | 2^26 | 1.41 | ~3.1e+05 ops (< 1 s) | ~10^20 ops (infeasible) |
| B | 0.05 | 14 | 1021 | 2^1021 | 2.85 | ~7.0e+07 ops (< 1 s) | ~10^620 ops (infeasible) |
| B | 0.01 | 29 | 32176 | 2^32176 | 3.24 | ~2.2e+09 ops (seconds) | ~10^19377 ops (infeasible) |

Using the Hamming-weight statistic, such a run costs seconds. The naive \(2^k\times2^k\) tensor is infeasible beyond \(k\approx12\). Even at very large \(k\), identifiable information is capped at \(\log_2N-\text{floor}\): 1.41 bits (A) and about 3.5 bits (B), not \(\log_2N\). Giving the class room to breathe needs a pool with more distinct output laws, or a model where \(X\) is observed (conditional-law floors 1.14 and 3.41 bits). It does not need more symbols.

### 8.8 Non-claims (unchanged)

This is a toy proof-of-concept for the shape of a curve.

- It is not evidence about hadronic or QCD physics.
- It makes no claim that noise is optionality, which remains Cyotee's conjecture.
- Using 4 channel uses is a modelling choice; correlated (entangled) inputs or adaptive readout were not considered.
