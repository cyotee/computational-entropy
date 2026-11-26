# Thermal amplitude-damping channel: a toy cost of the ε-class (Tier 2 toy exploration)

**Tier:** 2 of 3, **toy exploration (speculative)**. This note makes **no quantum or thermodynamic claim** beyond the Landauer pricing convention below, and pricing *retained* (not erased) bits at the Landauer rate is itself a modelling choice. The only quantum content is the classical output law of a one-qubit toy channel.  
**Status:** 2026-11-26 · computed. The ε-class verdict is **inconclusive** (§5). The joint encoding bound C_minus_K **falls** with T (§7).  
**Script:** [`simulations/classical/thermal_channel_cost.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/thermal_channel_cost.py) (pure numpy; built-in self-checks; runs in well under a second). Every number below is printed by that script.  
**Parent:** [Tier 2: instruction persistence](tier2-instruction-persistence.md), which defines \(d_f^{\#} = \log_2\lvert[f]\rvert\).

## 1. Question

Cyotee's conjecture: the storage cost of keeping the instruction class rises with temperature, with a soft knee near a crossover. This note tests that conjecture on a toy.

## 2. Method (every choice is a convention of this toy)

**Channel and output law.** We use single-qubit amplitude damping \(\mathrm{AD}(\gamma)\), with Kraus operators \(K_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix}\) and \(K_1=\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix}\). We fix the input \(|1\rangle\) and measure in the computational basis, so the output law is Bernoulli with \(P(1)=1-\gamma\). We sweep \(\gamma\) from 0 to 1 in steps of 0.01.

**Candidates.** Each candidate is reduced to a law on \(\{0,1\}\):

- **Boolean functions** \(f:\{0,1\}^n\to\{0,1\}\) on uniform inputs have \(P(f=1)=\mathrm{popcount}(f)/2^n\). The default is \(n=2\), the 16 two-input functions. The count is done by popcount, \(\binom{2^n}{k}\) functions per law; this was checked against explicit enumeration for \(n\le3\). The set extends to \(n=3,4,6\).
- **Fixed Kraus channels**, read out the same way as the target (input \(|1\rangle\)): I, X, Z, H, full dephasing, measurement, reset to \(|0\rangle\), reset to \(|1\rangle\).
- **Parametrized families** on a configurable grid of points in \([0,1]\) (default 11): amplitude damping, phase damping, depolarizing, bit flip. On a grid the class size depends on the grid resolution, so results are reported with and without the families.

Comparing a two-input function on uniform inputs with a one-qubit channel on a fixed input is a modelling choice. Only the output law on \(\{0,1\}\) is compared.

**ε-class and \(d^{\#}_{\varepsilon}\).** We define \(C_\varepsilon(\gamma)=\{g:\ \mathrm{TV}(g,\mathrm{AD}(\gamma))\le\varepsilon\}\), where the total-variation distance is \(\mathrm{TV}=|p-q|\) for two Bernoulli laws. We set \(d^{\#}_{\varepsilon}(\gamma):=\log_2\lvert C_\varepsilon(\gamma)\rvert\), shown as "-" when the class is empty. The default is \(\varepsilon=0.05\); the robustness sweep uses \(\varepsilon\in\{0.01,0.02,0.05,0.1\}\).

This is a **relaxation** of Tier 2's \(d_f^{\#}\). There, \([f]\) contains the maps with *exactly* the same output law on the same domain. Here we use an ε-ball over a mixed, finite candidate set. The two agree only in one case, which the script checks: Boolean-only candidates, \(\varepsilon=0\), and \(\gamma=1-k/4\), where the class size is \(\binom4k=4!/(k!(4-k)!)\), Tier 2's \(N!/\prod_y W_y!\).

**Temperature (Cyotee's toy parametrization, not standard physics).** We set \(\gamma=1/(e^{\beta\omega}+1)\) with \(\hbar\omega=k_B=1\), so \(T=1/\ln((1-\gamma)/\gamma)\).

- For \(T\ge0\) this covers only \(\gamma\in[0,1/2]\): \(T\to0\) gives \(\gamma\to0\), and \(T\to\infty\) gives \(\gamma\to1/2\).
- \(\gamma\in(1/2,1]\) requires \(\beta\omega<0\), i.e. **negative temperature**. That branch is computed and labelled \(T<0\), but it is excluded from every cost and cost-vs-T statement.
- Physically, finite-temperature amplitude damping is the *generalized* amplitude damping channel. That channel is not what is modelled here.

**Cost (pricing convention).** \(\mathrm{cost}=d^{\#}_{\varepsilon}\,k_BT\ln2\). The explicit factor \(T\) makes the cost rise with \(T\) **by construction**, so a rising cost is not evidence for the conjecture. Knees are therefore judged on \(d^{\#}_{\varepsilon}(\gamma)\) and on \(\mathrm{cost}/T=d^{\#}_{\varepsilon}\ln2\).

**Knee detection.** We use three methods on the \(T\ge0\) branch (\(\gamma\in[0,0.49]\)):

- (a) the \(\gamma\) at the maximum |discrete second derivative| of \(d^{\#}_{\varepsilon}(\gamma)\);
- (b) the breakpoint of the best continuous two-segment linear fit, with its SSE relative to a single line;
- (c) the \(T\) at the maximum |second derivative| of \(d^{\#}_{\varepsilon}(T)\).

On a finite set, \(d^{\#}_{\varepsilon}\) is a **step function** of \(\gamma\), so method (a) always lands on a step edge. The script checks this.

## 3. Results at ε = 0.05

The primary set is 16 Boolean functions + 8 fixed channels + 4 families × 11 grid points = 68 candidates. The cost column uses the primary set; no cost is given for \(T<0\) or \(T=\infty\).

| gamma | bw | T | branch | \|C\| Bool | \|C\| +fixed Q | \|C\| +families | d# Bool | d# +fixed Q | d# primary | cost = d# T ln2 (primary) | cost/T |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.00 | inf | 0.000 | T>=0 | 1 | 6 | 21 | 0.000 | 2.585 | 4.392 | 0.000 | 3.045 |
| 0.05 | 2.944 | 0.340 | T>=0 | 1 | 6 | 24 | 0.000 | 2.585 | 4.585 | 1.079 | 3.178 |
| 0.10 | 2.197 | 0.455 | T>=0 | 0 | 0 | 5 | - | - | 2.322 | 0.732 | 1.609 |
| 0.15 | 1.735 | 0.577 | T>=0 | 0 | 0 | 7 | - | - | 2.807 | 1.122 | 1.946 |
| 0.20 | 1.386 | 0.721 | T>=0 | 4 | 4 | 9 | 2.000 | 2.000 | 3.170 | 1.585 | 2.197 |
| 0.25 | 1.099 | 0.910 | T>=0 | 4 | 4 | 11 | 2.000 | 2.000 | 3.459 | 2.183 | 2.398 |
| 0.30 | 0.847 | 1.180 | T>=0 | 4 | 4 | 9 | 2.000 | 2.000 | 3.170 | 2.593 | 2.197 |
| 0.35 | 0.619 | 1.615 | T>=0 | 0 | 0 | 7 | - | - | 2.807 | 3.143 | 1.946 |
| 0.40 | 0.405 | 2.466 | T>=0 | 0 | 0 | 5 | - | - | 2.322 | 3.969 | 1.609 |
| 0.45 | 0.201 | 4.983 | T>=0 | 6 | 7 | 14 | 2.585 | 2.807 | 3.807 | 13.151 | 2.639 |
| 0.50 | 0.000 | inf | T=inf | 6 | 7 | 11 | 2.585 | 2.807 | 3.459 | - | 2.398 |
| 0.55 | -0.201 | -4.983 | T<0 | 6 | 7 | 12 | 2.585 | 2.807 | 3.585 | - | 2.485 |
| 0.60 | -0.405 | -2.466 | T<0 | 0 | 0 | 2 | - | - | 1.000 | - | 0.693 |
| 0.65 | -0.619 | -1.615 | T<0 | 0 | 0 | 4 | - | - | 2.000 | - | 1.386 |
| 0.70 | -0.847 | -1.180 | T<0 | 4 | 4 | 6 | 2.000 | 2.000 | 2.585 | - | 1.792 |
| 0.75 | -1.099 | -0.910 | T<0 | 4 | 4 | 8 | 2.000 | 2.000 | 3.000 | - | 2.079 |
| 0.80 | -1.386 | -0.721 | T<0 | 4 | 4 | 6 | 2.000 | 2.000 | 2.585 | - | 1.792 |
| 0.85 | -1.735 | -0.577 | T<0 | 0 | 0 | 4 | - | - | 2.000 | - | 1.386 |
| 0.90 | -2.197 | -0.455 | T<0 | 0 | 0 | 2 | - | - | 1.000 | - | 0.693 |
| 0.95 | -2.944 | -0.340 | T<0 | 1 | 3 | 7 | 0.000 | 1.585 | 2.807 | - | 1.946 |
| 1.00 | -inf | -0.000 | T<0 | 1 | 3 | 5 | 0.000 | 1.585 | 2.322 | - | 1.609 |

What the table shows:

- **Boolean only (the requested 16):** \(d^{\#}_{\varepsilon}\) takes only the values \(0,2,\log_26\). The class is empty for 28 of the 50 \(T\ge0\) grid points. On this set, \(d^{\#}_{\varepsilon}\) is a three-level staircase.
- **With channels:** adding the fixed channels makes \(d^{\#}_{\varepsilon}\) *largest* at \(\gamma=0\) (\(T=0\)): I, Z, measurement and reset to \(|1\rangle\) all give \(P(1)=1\). Adding the families on a grid strengthens this, because every phase-damping point has \(P(1)=1\). With channels included, \(d^{\#}_{\varepsilon}\) **falls** from \(T=0\) toward \(\gamma\approx0.1\) and is non-monotone afterwards.
- **Cost:** with the primary set, cost rises from 0 to 13.2 at \(\gamma=0.45\) (\(T\approx5\)) and to 59.9 at \(\gamma=0.49\) (\(T\approx25\)); it diverges as \(\gamma\to1/2\). This rise is driven by the factor \(T\). Over the full 0.01 grid, \(\mathrm{cost}/T\) stays between 1.39 and 3.18 with no monotone trend.

## 4. Knee findings and robustness (T ≥ 0 branch)

| candidate set | eps | d# at gamma 0 / 0.25 / 0.49 | distinct d# values | empty-class gammas | monotone in gamma | step edges | (a) gamma | (b) break, SSE ratio | (c) T | (a) at a step edge |
|---|---|---|---|---|---|---|---|---|---|---|
| Bool n=2 | 0.01 | 0.00 / 2.00 / 2.58 | 3 | 44 | yes | 4 | 0.24 | 0.24, 0.01 | 0.868 | yes |
| Bool n=2 | 0.02 | 0.00 / 2.00 / 2.58 | 3 | 40 | yes | 4 | 0.23 | 0.23, 0.02 | 0.257 | yes |
| Bool n=2 | 0.05 | 0.00 / 2.00 / 2.58 | 3 | 28 | yes | 4 | 0.05 | 0.20, 0.09 | 0.340 | yes |
| Bool n=2 | 0.1 | 0.00 / 2.00 / 2.58 | 3 | 8 | yes | 4 | 0.10 | 0.18, 0.36 | 0.455 | yes |
| Bool n=2 + fixed Q | 0.01 | 2.58 / 2.00 / 2.81 | 3 | 44 | no | 4 | 0.26 | 0.25, 0.00 | 0.868 | yes |
| Bool n=2 + fixed Q | 0.02 | 2.58 / 2.00 / 2.81 | 3 | 40 | no | 4 | 0.27 | 0.25, 0.00 | 0.257 | yes |
| Bool n=2 + fixed Q | 0.05 | 2.58 / 2.00 / 2.81 | 3 | 28 | no | 4 | 0.30 | 0.26, 0.02 | 0.340 | yes |
| Bool n=2 + fixed Q | 0.1 | 2.58 / 2.00 / 2.81 | 3 | 8 | no | 4 | 0.40 | 0.27, 0.15 | 0.455 | yes |
| Bool n=2 + fixed Q + fam(11) | 0.01 | 4.32 / 2.32 / 3.32 | 5 | 20 | no | 20 | 0.04 | 0.04, 0.59 | 0.315 | yes |
| Bool n=2 + fixed Q + fam(11) | 0.02 | 4.32 / 2.32 / 3.32 | 5 | 0 | no | 10 | 0.02 | 0.03, 0.67 | 0.288 | yes |
| Bool n=2 + fixed Q + fam(11) | 0.05 | 4.39 / 3.46 / 3.46 | 9 | 0 | no | 18 | 0.05 | 0.08, 0.53 | 0.340 | yes |
| Bool n=2 + fixed Q + fam(11) | 0.1 | 4.58 / 3.70 / 3.81 | 9 | 0 | no | 16 | 0.10 | 0.14, 0.57 | 0.455 | yes |
| Bool n=2 + fixed Q + fam(21) | 0.01 | 4.91 / 2.81 / 3.32 | 5 | 0 | no | 20 | 0.02 | 0.02, 0.66 | 0.257 | yes |
| Bool n=2 + fixed Q + fam(21) | 0.02 | 4.91 / 2.81 / 3.46 | 7 | 0 | no | 23 | 0.03 | 0.04, 0.39 | 0.288 | yes |
| Bool n=2 + fixed Q + fam(21) | 0.05 | 5.09 / 3.91 / 3.81 | 9 | 0 | no | 20 | 0.05 | 0.08, 0.42 | 0.340 | yes |
| Bool n=2 + fixed Q + fam(21) | 0.1 | 5.25 / 4.52 / 4.32 | 12 | 0 | no | 21 | 0.10 | 0.14, 0.54 | 0.455 | yes |
| Bool n=2 + fixed Q + fam(101) | 0.01 | 6.83 / 3.91 / 4.17 | 5 | 0 | no | 5 | 0.01 | 0.02, 0.16 | 0.257 | yes |
| Bool n=2 + fixed Q + fam(101) | 0.02 | 6.88 / 4.52 / 4.58 | 7 | 0 | no | 7 | 0.02 | 0.04, 0.17 | 0.288 | yes |
| Bool n=2 + fixed Q + fam(101) | 0.05 | 7.02 / 5.55 / 5.39 | 13 | 0 | no | 13 | 0.05 | 0.09, 0.24 | 0.363 | yes |
| Bool n=2 + fixed Q + fam(101) | 0.1 | 7.23 / 6.44 / 6.17 | 23 | 0 | no | 23 | 0.10 | 0.16, 0.52 | 0.455 | yes |
| Bool n=3 | 0.01 | 0.00 / 4.81 / 6.13 | 5 | 40 | yes | 8 | 0.12 | 0.24, 0.12 | 0.502 | yes |
| Bool n=3 | 0.02 | 0.00 / 4.81 / 6.13 | 5 | 32 | yes | 8 | 0.02 | 0.23, 0.14 | 0.478 | yes |
| Bool n=3 | 0.05 | 0.00 / 4.81 / 6.13 | 5 | 8 | yes | 8 | 0.05 | 0.20, 0.33 | 0.409 | yes |
| Bool n=3 | 0.1 | 0.00 / 4.81 / 6.13 | 9 | 0 | no | 8 | 0.02 | 0.04, 0.55 | 0.288 | yes |
| Bool n=4 | 0.01 | 0.00 / 10.83 / 13.65 | 9 | 32 | yes | 16 | 0.01 | 0.18, 0.08 | 0.387 | yes |
| Bool n=4 | 0.02 | 0.00 / 10.83 / 13.65 | 9 | 16 | yes | 16 | 0.02 | 0.17, 0.14 | 0.409 | yes |
| Bool n=4 | 0.05 | 0.00 / 10.83 / 13.65 | 17 | 0 | no | 16 | 0.01 | 0.20, 0.32 | 0.409 | yes |
| Bool n=4 | 0.1 | 4.09 / 12.72 / 15.13 | 16 | 0 | no | 15 | 0.02 | 0.17, 0.28 | 0.409 | yes |
| Bool n=6 | 0.01 | 0.00 / 48.80 / 61.65 | 48 | 0 | no | 47 | 0.01 | 0.20, 0.10 | 0.387 | yes |
| Bool n=6 | 0.02 | 6.02 / 50.85 / 61.65 | 49 | 0 | no | 48 | 0.01 | 0.20, 0.09 | 0.363 | yes |
| Bool n=6 | 0.05 | 15.42 / 53.68 / 63.12 | 48 | 0 | no | 47 | 0.01 | 0.20, 0.08 | 0.363 | yes |
| Bool n=6 | 0.1 | 26.31 / 57.11 / 63.82 | 38 | 0 | no | 37 | 0.01 | 0.21, 0.07 | 0.363 | yes |

**Smooth reference.** For large \(n\) and \(\varepsilon\to0\), the Boolean count satisfies \(d^{\#}/2^n\to H_b(\gamma)\) (method of types). For \(n=6\) and \(\varepsilon=0.02\), the largest deviation is 0.094 bits per input.

- \(H_b(\gamma)\) is concave on \((0,1/2)\), so it has **no interior knee in \(\gamma\)**; it is steepest as \(\gamma\to0\). The same two-segment fit applied to \(H_b\) itself breaks at \(\gamma=0.19\), with SSE ratio 0.09.
- As a function of temperature, \(h(T)=H_b(\gamma(T))\) has its maximum curvature at \(T\approx0.17\) and its maximum slope at \(T\approx0.31\), and it saturates near 1 by \(T\approx5\). This soft onset is the Schottky-like activation of the Fermi-type map \(\gamma(T)\). Any increasing function of \(\gamma\) would show it.

Findings:

1. **Method (a) is a step artifact in every one of the 32 configurations.** Its location jumps between \(\gamma=0.01\) and \(0.40\) depending on \(\varepsilon\) and the candidate set. It is not robust.
2. **Method (b) for Boolean-only sets with \(n\ge4\)** gives a stable break at \(\gamma\approx0.17\)–\(0.21\) (\(T\approx0.6\)–\(0.75\)) across \(\varepsilon\). That matches the break of the smooth concave \(H_b\) (0.19), so it is a two-segment fit of a concave curve, not a crossover feature. With quantum families included, the break moves with the grid and \(\varepsilon\) (0.02–0.16), and the fit is poor (SSE ratio 0.16–0.67).
3. **Method (c)** puts the \(d^{\#}_{\varepsilon}(T)\) curvature peak at \(T\approx0.26\)–\(0.50\) for every configuration except the two \(n=2\) sets at \(\varepsilon=0.01\), which give 0.87. That is near the smooth reference value (0.22 on the same grid) and is inherited from \(\gamma(T)\), not from the class structure.
4. **Direction depends on the candidate set.** Boolean-only: \(d^{\#}_{\varepsilon}\) rises from \(\gamma=0\) to \(0.49\) (e.g. \(n=6\): 0.00 → 61.65 at \(\varepsilon=0.01\)). With channels: it falls (e.g. families at 101 grid points, \(\varepsilon=0.05\): 7.02 → 5.39). Class sizes with families scale with the grid resolution.

## 5. Verdict: **inconclusive**

The verdict is based on \(d^{\#}_{\varepsilon}\), not on the factor \(T\).

- For Boolean-only sets, the rise of \(d^{\#}_{\varepsilon}\) with \(T\) and its soft onset are both explained by two things: the method-of-types limit \(H_b(\gamma)\), and the activation built into the toy map \(\gamma(T)\).
- No knee survives that is tied to a crossover and is independent of \(\varepsilon\), the candidate set, and the grid.
- Adding quantum operations reverses the trend.

So the curves neither support nor contradict the conjecture: the toy, as parametrized, cannot separate a real knee from features built into its construction. A discriminating test would need:

- a candidate set fixed independently of the channel family;
- an exact (\(\varepsilon=0\)) or measure-based class (Tier 2 §7, item 3);
- the generalized amplitude damping channel for genuine finite-\(T\) physics, which would be Tier 3 material.

## 6. Non-claims

- \(d^{\#}_{\varepsilon}\) is not a physical entropy. The cost is a pricing convention, not a derived heat bound.
- The \(\gamma\leftrightarrow T\) map is a toy parametrization.
- Nothing here bears on gravity, quantum thermodynamics, or the Tier 3 conjecture.

## 7. Joint Encoding Bound

*Added 2026-11-26. Same toy and same caveats as §2, including the same exclusion of the negative-T branch. Script: [`simulations/classical/joint_encoding_bound.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/joint_encoding_bound.py), which imports the §2 script.*

**Idea (Cyotee's framing).** The result and the instructions for the next stage are one joint encoding, not two separate strings. The quantity of interest is then the channel's capacity minus a description cost of the channel: how much of the output's capacity is used up by making the output self-executing.

### 7.1 Construction

**C(γ), the Holevo capacity** \(\chi^\*\) of \(\mathrm{AD}(\gamma)\), in bits per use. It is computed two ways that agree to \(3\times10^{-13}\):

- Nelder–Mead over a general two-pure-state ensemble: two Bloch-sphere points plus a probability, 5 parameters, with random restarts.
- The closed form \(\max_q\,[h_2((1-\gamma)q) - h_2(\tfrac12(1+\sqrt{1-4\gamma(1-\gamma)q^2}))]\) (Giovannetti & Fazio, *Phys. Rev. A* 71, 032314 (2005)).

Checks: \(C(1/2)=0.4717\), matching the value Giovannetti & Fazio report; \(C(0)=1\); \(C(1)=0\). A 2026 preprint (Tang, Zhu, Bai & Wang, arXiv:2609.28592) states that this single-use value equals the unassisted classical capacity (additivity). We quote that result and do not reproduce it.

**K, a description cost.** Two crude upper-bound proxies are used. **Neither is Kolmogorov complexity**, which is uncomputable and defined only up to an additive constant (invariance theorem).

- \(K_\varepsilon=\log_2\lceil(\pi/2)/\varepsilon_K\rceil+\log_2 4\). The first term counts the \(\varepsilon_K\)-cells covering the AD family in the Kraus-operator (Frobenius) metric; the family's arc length is \(\pi/2\), checked numerically. The second term selects one of the 4 families in §2. At \(\varepsilon_K=0.05\), \(K_\varepsilon=7.00\) bits for every \(\gamma\).
- \(K_{\rm circ}\) is the cost of writing down one known Stinespring circuit: system + 1 ancilla, 3 CNOT + 2 \(R_y\). It is not proved minimal; the script checks that it reproduces AD exactly. Its cost is 5 gates × 2 bits plus one angle at \(\log_2\lceil\pi/\varepsilon_K\rceil\) bits, which is 15.98 bits for \(\gamma>0\) and 0 at \(\gamma=0\).

**Units and how they are combined.** \(C\) is in bits per use; \(K\) is a one-time cost in bits. The script reports three combinations:

- (a) per single use: \(C-K\);
- (b) amortized over \(n\) uses: \(nC-K\) in bits, or \(C-K/n\) in bits per use;
- (c) the break-even \(n^\*=K/C\).

The sign depends on the choice: \(C-K\) is negative at every \(\gamma\) (about −6 to −7 bits), while \(C-K/n\) is positive for \(n\gtrsim 15\). For a fixed parametrized family, \(K\) is (almost) independent of \(\gamma\), so **C_minus_K tracks \(C(\gamma)\) for every combination**. The only \(\gamma\)-dependence in \(K\) is \(K_{\rm circ}=0\) at \(\gamma=0\).

**s for the 1/s comparison.** \(s\) is the output entropy for input \(|1\rangle\): \(s=S(\mathrm{AD}(|1\rangle\langle1|))=h_2(\gamma)\) bits per qubit.

### 7.2 Results (\(T\ge0\) branch; \(K=K_\varepsilon\); amortized at \(n=100\); \(d^{\#}_{\varepsilon}\) and cost from §3)

| gamma | T | branch | C (bits/use) | K (bits) | C - K (n=1) | C - K/n (n=100) | nC - K (n=100) | d#_eps | cost = d# T ln2 | s = h2(gamma) | 1/s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.00 | 0.000 | T>=0 | 1.0000 | 7.00 | -6.000 | 0.9300 | 93.00 | 4.392 | 0.000 | 0.0000 | inf |
| 0.05 | 0.340 | T>=0 | 0.9069 | 7.00 | -6.093 | 0.8369 | 83.69 | 4.585 | 1.079 | 0.2864 | 3.492 |
| 0.10 | 0.455 | T>=0 | 0.8405 | 7.00 | -6.160 | 0.7705 | 77.05 | 2.322 | 0.732 | 0.4690 | 2.132 |
| 0.15 | 0.577 | T>=0 | 0.7833 | 7.00 | -6.217 | 0.7133 | 71.33 | 2.807 | 1.122 | 0.6098 | 1.640 |
| 0.20 | 0.721 | T>=0 | 0.7316 | 7.00 | -6.268 | 0.6616 | 66.16 | 3.170 | 1.585 | 0.7219 | 1.385 |
| 0.25 | 0.910 | T>=0 | 0.6837 | 7.00 | -6.316 | 0.6137 | 61.37 | 3.459 | 2.183 | 0.8113 | 1.233 |
| 0.30 | 1.180 | T>=0 | 0.6383 | 7.00 | -6.362 | 0.5683 | 56.83 | 3.170 | 2.593 | 0.8813 | 1.135 |
| 0.35 | 1.615 | T>=0 | 0.5949 | 7.00 | -6.405 | 0.5249 | 52.49 | 2.807 | 3.143 | 0.9341 | 1.071 |
| 0.40 | 2.466 | T>=0 | 0.5530 | 7.00 | -6.447 | 0.4830 | 48.30 | 2.322 | 3.969 | 0.9710 | 1.030 |
| 0.45 | 4.983 | T>=0 | 0.5120 | 7.00 | -6.488 | 0.4420 | 44.20 | 3.807 | 13.151 | 0.9928 | 1.007 |
| 0.50 | inf | T=inf | 0.4717 | 7.00 | -6.528 | 0.4017 | 40.17 | 3.459 | - | 1.0000 | 1.000 |

The script also prints the negative-T rows (\(\gamma>1/2\)) for completeness. They are excluded from every statement about T.

| combination | value at T=0 | value at gamma=0.49 (T~25) | monotone in T | direction |
|---|---|---|---|---|
| C (bits/use) | 1.0000 | 0.4797 | yes | falls |
| C - K_eps/n, n=1 (bits/use) | -6.0000 | -6.5203 | yes | falls |
| C - K_eps/n, n=10 (bits/use) | 0.3000 | -0.2203 | yes | falls |
| C - K_eps/n, n=100 (bits/use) | 0.9300 | 0.4097 | yes | falls |
| C - K_eps/n, n=1000 (bits/use) | 0.9930 | 0.4727 | yes | falls |
| nC - K_eps, n=100 (bits) | 93.0000 | 40.9745 | yes | falls |
| C - K_circ/n, n=100 (bits/use) | 1.0000 | 0.3200 | yes | falls |
| s = h2(gamma) (bits) | 0.0000 | 0.9997 | yes | rises |
| 1/s (finite part, gamma>0) | 12.3773 (gamma=0.01) | 1.0003 | yes | falls |

### 7.3 Does C_minus_K behave as predicted?

**C_minus_K falls with T.** For every combination above it falls monotonically on the \(T\ge0\) branch, from \(C=1\) at \(T=0\) to \(0.48\) at \(T\approx25\), approaching \(0.4717\) as \(T\to\infty\). Over the same range \(1/s\) also falls, and \(s\) rises. So C_minus_K does **not** rise in the region where \(1/s\) falls. This matches the expectation that AD capacity falls as \(\gamma\to1/2\).

The monotonicity is proved, not just observed:

- \(\mathrm{AD}(a)\circ\mathrm{AD}(b)=\mathrm{AD}(1-(1-a)(1-b))\). The script checks this identity numerically; it is standard.
- So a larger \(\gamma\) is a post-processing of a smaller one, and the data-processing inequality for Holevo information gives that \(C\) is non-increasing in \(\gamma\).
- \(\gamma(T)\) is increasing on \(T>0\), so \(C\) is non-increasing in \(T\).

The Landauer cost in §3 rises with \(T\) only through its explicit factor \(T\). \(d^{\#}_{\varepsilon}\) shows no trend on this candidate set.

### 7.4 Connection to capacity (a framing, not a theorem)

Shannon/Holevo capacity is the ceiling on what an output can carry. Any self-executing overhead can therefore only use up part of that ceiling, not add to it. The one precise version we can state is a direct use of the standard capacity converse, not a new result:

- Suppose the instructions are one of \(2^K\) equally likely descriptions that the receiver does not already know.
- Suppose they are sent jointly with \(nR\) payload bits over \(n\) uses.
- Then reliable decoding requires \(nR+K\le nC+o(n)\).

A description the receiver already knows costs no capacity. So "capacity used up by self-execution" is meaningful only when the description itself carries information. The proxies \(K_\varepsilon\) and \(K_{\rm circ}\) are not shown to be the right \(K\) for that statement.

For a physics reframing, see the Tier 3 conjecture note: [Tier 3 note (conjecture)](qcd-entropy-density-note.md).
