# Structured-pool informed-input gap: shared eigenbasis and Clifford pools (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model and proof-of-concept** in a two-qubit setting.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim.

**Status:** 2026-11-26 · computed. Follow-up (CE-11) to the [informed-input procedural share](procedural-share-informed.md) (CE-10). There, the zero gap was partly a theorem, because of the Haar pool's symmetry. Here the Haar pool is replaced by **structured pools**, where a zero expected gap is no longer forced, and the blind vs informed comparison is rerun.

**Script:** [`simulations/classical/procedural_share_structured.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share_structured.py) (pure numpy; imports `procedural_share_informed.py` and `procedural_share_surface.py`; built-in self-checks; about 80 s for all pools at \(T=1,0,\infty\)). Every number below is printed by:

```
python simulations/classical/procedural_share_structured.py                     # all 7 pools, 40 draws, T = 1, 0, inf
python simulations/classical/procedural_share_structured.py --pool eigbasis-hadamard,eigbasis-pert --markdown --no-robust-T
```

Flags: `--pool`, `--variants`, `--seed`, `--seeds`, `--eps`, `--T`, `--no-robust-T`, `--gammas`, `--ranks`, `--flips`, `--boot`, `--markdown`.

## 1. Summary

**(i) Does the gap open?** On structured pools the gap is no longer zero in general: most variant × pool cells are significantly nonzero. But almost every nonzero gap is either **negative** (the informed input reveals *less* about \(f\) than the blind one) or **forced by construction**.

- **Negative gaps:** (b) phase on `eigbasis`; (a), (c) and rand on both Clifford subsets; (a) and (c) on `eigbasis-hadamard`.
- **Positive by construction:** `eigbasis-identity` and `clifford1-full`, where the blind condition sees nothing, and the readable control everywhere.

**Only two positive structural gaps are not forced by construction, and neither is clean:**

- **(b) phase on `eigbasis-hadamard`:** +0.0139 bits [0.0077, 0.0201], \(p_{\rm Holm}=3\times10^{-4}\), about 2.2× that pool's floor of 0.0062. It holds at all three temperatures.
  - It comes entirely from ranks 2 and 8, where the blind condition is blind *by construction*: its qubit-A populations are uniform for every \(f\).
  - At ranks 4 and 16 the phase gap is near zero or negative, and not significant.
  - So this is a readout blind spot of the blind input, not a hint that "aligns" with \(U_f\).
- **(a) eigen and (c) fixedpt on `eigbasis-pert`:** about +0.013 to +0.015 bits, about 1.2× the floor of 0.011–0.0125.
  - Significant only at \(T=\infty\) (\(p_{\rm Holm}\approx0.04\)); not at \(T=1\) (0.06) or \(T=0\) (0.13).
  - No single grid point survives Holm. Suggestive, not established.

**(ii) Does it track the Holevo information?** No.

- (a) and (c) carry \(\chi_{\rm in}\approx1.5\)–1.9 bits in every pool, yet their gaps run from −0.083 to +0.40 bits. The sign and size are set by the pool's geometry relative to the Z readout, not by \(\chi_{\rm in}\).
- (b) phase carries 1.2 bits on `eigbasis-identity` and has a gap of exactly 0 there.
- Per-draw correlations between \(\chi_{\rm in}\) and the gap are weak and of either sign (\(|r|\le0.61\)).
- The guaranteed bound \(I(F;Y)\le\chi_{\rm in}\) for (a) and (c) holds, but is loose by one to two orders of magnitude.

**(iii) Against the resolution floor.**

- CE-10's floor was about 0.004 bits. The per-pool floors here are larger: 0.0030 (deterministic `clifford1-full`) up to 0.0137 bits, because structured pools vary more from draw to draw.
- Construction-free positive gaps are at most about 2× their pool's floor.
- Normalised, every structural gap at \(T=1\) is ≤ 0.06 × H(F). The largest (0.06; 0.07 at \(T=0\)) is the construction-forced `eigbasis-identity` case.

**A correction to CE-10, found while setting this up.** For (a) eigen, (c) fixedpt and the readable control, the informed \(I(F;Y)\) is carried *entirely by the input* in every pool, including CE-10's Haar pool. The message-averaged input is a mixture of \(U_f\)'s own eigenprojectors, so \(U_f\) does nothing to it (§3). CE-10 stated this only for (a). Only (b) phase and rand let \(U_f\) act on the hint.

**Zero-gap flags (\(T=1\)):**

- Consistent with zero: (a), (c) and rand on `eigbasis`; (a), (b), (c) and blind-alt on `eigbasis-pert`; blind-alt on `eigbasis-hadamard` and `clifford1`; (b) and blind-alt on `clifford2`.
- Exactly zero by construction: gphase everywhere; (b) and blind-alt on `eigbasis-identity` and `clifford1-full`.

## 2. Method

**Unchanged from CE-10:**

- 2 channel uses with the same unknown \(f\).
- Message \(M\) uniform and independent of \(F\); uniform prior over \(F\).
- Generalized amplitude damping on each qubit: \(p=1/(1+e^{-1/T})\), \(T=1\) default, \(T=0\) and \(\infty\) as robustness.
- Nested Z readout, rank \(r\in\{2,4,8,16\}\), \(g\in\{0,0.1,\dots,1\}\), exact probabilities.
- Gap \(=H(F\mid Y)_{\rm blind}-H(F\mid Y)_{\rm variant}\), with blind and variant on the same pool.
- \(\chi_{\rm in}\) is the Holevo information between \(F\) and the block input state.

**Pools:**

- Every pool, and its control unitaries \(V_f\), is drawn from `default_rng([seed, tag])` and SHA-256 hashed **before any noise parameter exists**. The hash is re-checked after every condition.
- Canonical draw: seed 2026. Ensemble: seeds 1–40.
- The Clifford groups are generated by breadth-first search modulo global phase: 24 single-qubit elements and 11 520 two-qubit elements, both checked.

**Variants:** as in CE-10. The only change is that eigenvectors come from a joint diagonalization of the commuting Hermitian parts of \(U_f\), which stays orthonormal for degenerate Clifford spectra.

- Eigenphases are rounded to \(10^{-9}\) and sorted stably, with \(-\pi\) mapped to \(+\pi\).
- Inside a degenerate eigenspace the basis is whatever the eigensolver returns. It is deterministic, not canonical.
- It reproduces CE-10's eigenvectors on generic unitaries (self-check).

**Statistics:** as in CE-10.

- The randomness is **independent pool draws**: \(W\), phases, perturbations, Clifford subsets and \(V_f\).
- \(H_0\): \(E_{\rm draw}[\text{gap}]=0\).
- Grid-mean gap per draw over \(g<1\); two-sided sign-flip test (20 000 flips); bootstrap 95% CI; Holm across the tested variants within each pool. Per-point sign-flip tests are Holm-corrected across the 40 points.
- Gaps below \(10^{-12}\) are set to exactly 0 first, so floating-point residue of an exact zero cannot register as significant.
- A variant whose per-draw gap never varies is reported as an exact, deterministic value and is not tested.
- **Distinct output laws** = the number of distinct message-marginal laws \(P(y\mid f)\) at \(g=0\), \(r=16\). It bounds \(I(F;Y)\le\log_2\#\text{laws}\) (checked at every point).

## 3. Traps: what is forced by construction

1. **Only the message-averaged input matters.** The message is unknown and independent across uses, so \(P(y_1,y_2\mid f)=P_1(y_1\mid f)P_1(y_2\mid f)\), where \(P_1\) is the law of \(\mathcal N(U_f\sigma_fU_f^\dagger)\) and \(\sigma_f=\tfrac12\sum_m\lvert\psi_{f,m}\rangle\langle\psi_{f,m}\rvert\).
   - For (a) and (c), \(\sigma_f\) is a mixture of two eigenprojectors of \(U_f\) (the cross terms of (c) cancel), so \(U_f\sigma_fU_f^\dagger=\sigma_f\).
   - For readable, it equals the averaged state of \(\lvert m\,b_f\rangle\).
   - So in every pool, the informed \(I(F;Y)\) of (a), (c) and readable is **input-carried**: \(F\to\sigma_f\to Y\) is a Markov chain and \(I(F;Y)\le\chi_{\rm in}\). Self-checked.
2. **Shared eigenbasis, (a) eigen.** Every \(U_f\) has the same eigenvectors, but (a) picks the two with the smallest eigenphases, so *which* columns of \(W\) are used depends on \(f\). (a) is therefore not \(f\)-independent; it was redefined this way rather than left trivial.
   - \(\sigma_f\) carries only the unordered pair of columns, which has 6 values.
   - So there are at most 6 output laws (observed: 6.0), and \(I(F;Y)\le\log_2 6\).
   - The same holds for (c).
3. **\(W=I\)** (diagonal pool, Z readout). GAD maps diagonals to diagonals, so the Z readout sees only input populations, which a diagonal \(U_f\) does not change.
   - Blind and blind-alt: \(I(F;Y)=0\) exactly (1 law).
   - (b) phase: all populations are 1/4, so the gap is exactly 0, even though \(\chi_{\rm in}=1.2\) bits.
   - (a), (c) and rand: their populations reveal the \(f\)-dependent *selection* or the random label, not \(U_f\)'s action, so their gaps are positive by construction.
4. **\(W=H\otimes H\).** Every eigenprojector is a Hadamard-basis state with all Z populations equal to 1/4.
   - So (a) and (c) have \(I(F;Y)=0\) (1 law), and their gap equals \(-I(F;Y)_{\rm blind}\), by construction.
   - Also by construction, the blind qubit-A populations are uniform for every \(f\). Blind has \(I(F;Y)=0\) at \(r=2\), and \(r=8\) adds nothing over \(r=4\).
5. **Pools acting on one qubit, and Clifford structure.**
   - **`clifford1-full` (qubit A only):** the blind averaged input \((I/2)\otimes\lvert0\rangle\langle0\rvert\) is invariant, so blind \(I(F;Y)=0\) and every gap equals the informed \(I(F;Y)\ge0\).
   - **(b) on `clifford1-full`:** the sorted eigenphases come in equal pairs, making the hint state \(\lvert\psi_A\rangle\otimes\lvert+\rangle\). After the message average it becomes \(I/2\otimes\lvert+\rangle\langle+\rvert\), the same for every \(f\). So \(\chi_{\rm in}=0\) and the gap is 0.
   - **`clifford1` (C1 × C1):** blind sees only qubit B's Clifford acting on \(\lvert0\rangle\), so it has at most 3 laws (observed 3.0) and \(I(F;Y)=0\) at \(r=2\).
   - **`clifford2`:** the averaged blind state \((I+P)/4\) has a single stabilizing Pauli \(P\), so there are at most 7 Z laws (observed 6.0).
6. **rand on any pool:** \(U_fV_f\) is Haar for every \(U_f\), so rand compares a structured-pool blind condition with a Haar-like informed one.
7. **Exact zeros in every pool:** gphase, and \(g=1\). At \(T=\infty\), GAD is Pauli-covariant. This makes blind-alt exactly 0 on `eigbasis-hadamard` (where \(X_B\) commutes with every \(U_f\)) and on `clifford1` (observed per draw to \(10^{-12}\)).
8. **Guaranteed and checked at every point** (all hold, all pools, all variants):
   - \(-I(F;Y)_{\rm blind}\le\text{gap}\le\min(\log_2 r,H(F))-I(F;Y)_{\rm blind}\);
   - \(I(F;Y)\le\chi_{\rm out}\) (Holevo);
   - \(I(F;Y)\le\log_2\#\text{laws}\);
   - readable \(I(F;Y)\le1\) bit.

## 4. Results per pool (\(T=1\), 40 draws)

Columns: "Laws" is the mean number of distinct \(P(y\mid f)\) at \(g=0,r=16\); gap/H(F) and gap/\(I_{\rm blind}\) normalise the grid-mean gap. "Status" says whether a result is forced by construction or empirical.

### eigbasis

**Shared eigenbasis, random \(W\)** (`eigbasis`). \(U_f=W\,\mathrm{diag}(e^{i\phi_f})\,W^\dagger\), with one Haar \(W\) per draw shared by all 50 members and i.i.d. uniform eigenphases. Randomness per draw: \(W\), the phases and \(V_f\).

- Blind grid-mean \(I(F;Y)\) = 0.0582 bits; blind output laws at \(g=0,r=16\): 50.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0123 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | +0.0031 | [−0.0084, +0.0152] | 9.8e-01 | 0/0 | 1.745 | 6.0 | +0.0005 | 0.053 | **consistent with zero** | input-carried (≤ log₂6); value empirical |
| (b) phase | −0.0085 | [−0.0134, −0.0038] | 4.6e-03 | 0/26 | 1.188 | 50.0 | −0.0015 | −0.145 | gap < 0 | empirical |
| (c) fixedpt | +0.0046 | [−0.0073, +0.0172] | 9.8e-01 | 0/0 | 1.744 | 6.0 | +0.0008 | 0.080 | **consistent with zero** | input-carried (≤ log₂6); value empirical |
| readable | +0.2268 | [+0.2221, +0.2313] | 3.0e-04 | 30/10 | 1.850 | 2.0 | +0.0402 | 3.894 | gap > 0 | by construction |
| rand | +0.0034 | [−0.0013, +0.0081] | 4.9e-01 | 0/0 | 1.906 | 50.0 | +0.0006 | 0.059 | **consistent with zero** | empirical |
| blind-alt | −0.0017 | [−0.0025, −0.0008] | 2.5e-03 | 0/26 | 0.000 | 50.0 | −0.0003 | −0.028 | gap < 0 | empirical |
| gphase | +0.0000 | exact | – | – | 0.000 | 50.0 | +0.0000 | 0.000 | exactly zero | exact 0 (construction) |

Paired comparison with the random-label control, \(T=1\) (gap(variant) − gap(rand), Holm across 3): (a) eigen −0.0003 [−0.0095, +0.0097], \(p_{\rm Holm}\)=1.0e+00; (b) phase −0.0119 [−0.0153, −0.0083], \(p_{\rm Holm}\)=1.5e-04; (c) fixedpt +0.0012 [−0.0080, +0.0114], \(p_{\rm Holm}\)=1.0e+00.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | +0.0031 (0) | +0.0007 (0) | +0.0039 (0) |
| (b) phase | −0.0085 (−) | −0.0118 (−) | −0.0076 (−) |
| (c) fixedpt | +0.0046 (0) | +0.0025 (0) | +0.0054 (0) |
| rand | +0.0034 (0) | +0.0014 (0) | +0.0041 (0) |
| blind-alt | −0.0017 (−) | −0.0055 (−) | −0.0002 (0) |

### eigbasis-pert

**Perturbed shared eigenbasis** (`eigbasis-pert`). \(U_f=e^{i\varepsilon H_f}\,W\mathrm{diag}(e^{i\phi_f})W^\dagger\), with \(H_f\) drawn from the Gaussian unitary ensemble (spectral norm 1) and \(\varepsilon=0.1\). The eigenvectors now differ slightly between members.

- Blind grid-mean \(I(F;Y)\) = 0.0533 bits; blind output laws at \(g=0,r=16\): 50.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0112 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | +0.0144 | [+0.0033, +0.0256] | 6.0e-02 | 0/0 | 1.759 | 50.0 | +0.0026 | 0.271 | **consistent with zero** | input-carried; value empirical |
| (b) phase | −0.0026 | [−0.0070, +0.0018] | 2.5e-01 | 0/0 | 1.191 | 50.0 | −0.0005 | −0.049 | **consistent with zero** | empirical |
| (c) fixedpt | +0.0128 | [+0.0023, +0.0236] | 6.2e-02 | 0/0 | 1.771 | 50.0 | +0.0023 | 0.241 | **consistent with zero** | input-carried; value empirical |
| readable | +0.2318 | [+0.2278, +0.2360] | 3.0e-04 | 30/10 | 1.834 | 2.0 | +0.0411 | 4.352 | gap > 0 | by construction |
| rand | +0.0070 | [+0.0023, +0.0117] | 2.9e-02 | 11/0 | 1.906 | 50.0 | +0.0012 | 0.131 | gap > 0 | empirical |
| blind-alt | −0.0012 | [−0.0022, −0.0002] | 6.2e-02 | 0/24 | 0.000 | 50.0 | −0.0002 | −0.023 | **consistent with zero** | empirical |
| gphase | +0.0000 | exact | – | – | 0.000 | 50.0 | +0.0000 | 0.000 | exactly zero | exact 0 (construction) |

Paired comparison with the random-label control, \(T=1\) (gap(variant) − gap(rand), Holm across 3): (a) eigen +0.0075 [−0.0010, +0.0164], \(p_{\rm Holm}\)=2.0e-01; (b) phase −0.0096 [−0.0128, −0.0063], \(p_{\rm Holm}\)=1.5e-04; (c) fixedpt +0.0059 [−0.0023, +0.0143], \(p_{\rm Holm}\)=2.0e-01.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | +0.0144 (0) | +0.0132 (0) | +0.0152 (+) |
| (b) phase | −0.0026 (0) | −0.0060 (0) | −0.0015 (0) |
| (c) fixedpt | +0.0128 (0) | +0.0114 (0) | +0.0136 (+) |
| rand | +0.0070 (+) | +0.0048 (0) | +0.0078 (+) |
| blind-alt | −0.0012 (0) | −0.0062 (−) | +0.0007 (0) |

### eigbasis-hadamard

**Shared eigenbasis, \(W=H\otimes H\)** (`eigbasis-hadamard`). \(W\) is fixed and mutually unbiased with the Z readout; the randomness is the phases (and \(V_f\)).

- Blind grid-mean \(I(F;Y)\) = 0.0718 bits; blind output laws at \(g=0,r=16\): 50.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0062 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | −0.0718 | [−0.0754, −0.0686] | 3.0e-04 | 0/30 | 1.750 | 1.0 | −0.0127 | −1.000 | gap < 0 | = −I(F;Y)_blind (construction) |
| (b) phase | +0.0139 | [+0.0077, +0.0201] | 3.0e-04 | 20/0 | 1.195 | 50.0 | +0.0025 | 0.193 | gap > 0 | empirical; driven by r=2,8 where blind is blind by construction |
| (c) fixedpt | −0.0718 | [−0.0754, −0.0685] | 3.0e-04 | 0/30 | 1.753 | 1.0 | −0.0127 | −1.000 | gap < 0 | = −I(F;Y)_blind (construction) |
| readable | +0.2132 | [+0.2095, +0.2165] | 3.0e-04 | 30/0 | 1.716 | 2.0 | +0.0378 | 2.969 | gap > 0 | by construction |
| rand | −0.0096 | [−0.0137, −0.0057] | 3.0e-04 | 10/26 | 1.906 | 50.0 | −0.0017 | −0.133 | gap < 0 | empirical |
| blind-alt | −0.0002 | [−0.0005, +0.0002] | 4.3e-01 | 0/0 | 0.000 | 50.0 | −0.0000 | −0.002 | **consistent with zero** | empirical (exact 0 at T=∞) |
| gphase | +0.0000 | exact | – | – | 0.000 | 50.0 | +0.0000 | 0.000 | exactly zero | exact 0 (construction) |

Paired comparison with the random-label control, \(T=1\) (gap(variant) − gap(rand), Holm across 3): (a) eigen −0.0622 [−0.0642, −0.0603], \(p_{\rm Holm}\)=1.5e-04; (b) phase +0.0235 [+0.0190, +0.0282], \(p_{\rm Holm}\)=1.5e-04; (c) fixedpt −0.0622 [−0.0643, −0.0603], \(p_{\rm Holm}\)=1.5e-04.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | −0.0718 (−) | −0.0827 (−) | −0.0701 (−) |
| (b) phase | +0.0139 (+) | +0.0142 (+) | +0.0140 (+) |
| (c) fixedpt | −0.0718 (−) | −0.0827 (−) | −0.0701 (−) |
| rand | −0.0096 (−) | −0.0130 (−) | −0.0091 (−) |
| blind-alt | −0.0002 (0) | −0.0006 (0) | +0.0000 (=0) |

### eigbasis-identity

**Shared eigenbasis, \(W=I\)** (`eigbasis-identity`). The pool is diagonal in the readout basis. This is a **construction-forced** control (§3).

- Blind grid-mean \(I(F;Y)\) = 0.0000 bits; blind output laws at \(g=0,r=16\): 1.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0051 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | +0.3351 | [+0.3300, +0.3401] | 1.5e-04 | 40/0 | 1.749 | 6.0 | +0.0594 | n/a | gap > 0 | ≥ 0 by construction (blind = 0) |
| (b) phase | +0.0000 | exact | – | – | 1.202 | 1.0 | +0.0000 | n/a | exactly zero | exact 0 (construction) |
| (c) fixedpt | +0.3358 | [+0.3316, +0.3398] | 1.5e-04 | 40/0 | 1.745 | 6.0 | +0.0595 | n/a | gap > 0 | ≥ 0 by construction (blind = 0) |
| readable | +0.2850 | exact | – | – | 1.000 | 2.0 | +0.0505 | n/a | deterministic (exact) | by construction, deterministic |
| rand | +0.0609 | [+0.0590, +0.0629] | 1.5e-04 | 40/0 | 1.906 | 50.0 | +0.0108 | n/a | gap > 0 | label leak by construction |
| blind-alt | +0.0000 | exact | – | – | 0.000 | 1.0 | +0.0000 | n/a | exactly zero | exact 0 (construction) |
| gphase | +0.0000 | exact | – | – | 0.000 | 1.0 | +0.0000 | n/a | exactly zero | exact 0 (construction) |

Paired comparison with the random-label control, \(T=1\) (gap(variant) − gap(rand), Holm across 3): (a) eigen +0.2741 [+0.2687, +0.2792], \(p_{\rm Holm}\)=1.0e-04; (c) fixedpt +0.2749 [+0.2701, +0.2795], \(p_{\rm Holm}\)=1.0e-04.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | +0.3351 (+) | +0.4041 (+) | +0.3267 (+) |
| (b) phase | +0.0000 (=0) | +0.0000 (=0) | +0.0000 (=0) |
| (c) fixedpt | +0.3358 (+) | +0.4034 (+) | +0.3278 (+) |
| rand | +0.0609 (+) | +0.0682 (+) | +0.0597 (+) |
| blind-alt | +0.0000 (=0) | +0.0000 (=0) | +0.0000 (=0) |

### clifford1

**C1 × C1 subset** (`clifford1`). A random 50-element subset, per draw, of the 576 two-qubit products of single-qubit Cliffords (mod phase).

- Blind grid-mean \(I(F;Y)\) = 0.1087 bits; blind output laws at \(g=0,r=16\): 3.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0108 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | −0.0523 | [−0.0575, −0.0473] | 3.0e-04 | 10/30 | 1.898 | 16.9 | −0.0093 | −0.482 | gap < 0 | empirical; r=2 positive where blind = 0 by construction |
| (b) phase | −0.0133 | [−0.0241, −0.0025] | 5.0e-02 | 0/0 | 0.850 | 9.1 | −0.0024 | −0.122 | gap < 0 | empirical |
| (c) fixedpt | −0.0245 | [−0.0303, −0.0188] | 3.0e-04 | 10/30 | 1.880 | 19.1 | −0.0043 | −0.225 | gap < 0 | empirical; r=2 positive where blind = 0 by construction |
| readable | +0.1764 | [+0.1704, +0.1824] | 3.0e-04 | 30/0 | 1.558 | 2.0 | +0.0312 | 1.623 | gap > 0 | by construction |
| rand | −0.0476 | [−0.0538, −0.0415] | 3.0e-04 | 10/30 | 1.906 | 50.0 | −0.0084 | −0.438 | gap < 0 | empirical |
| blind-alt | +0.0006 | [−0.0002, +0.0014] | 1.4e-01 | 0/0 | 0.000 | 3.0 | +0.0001 | 0.006 | **consistent with zero** | empirical (exact 0 at T=∞) |
| gphase | +0.0000 | exact | – | – | 0.000 | 3.0 | +0.0000 | 0.000 | exactly zero | exact 0 (construction) |

Paired comparison with the random-label control, \(T=1\) (gap(variant) − gap(rand), Holm across 3): (a) eigen −0.0047 [−0.0084, −0.0012], \(p_{\rm Holm}\)=1.5e-02; (b) phase +0.0343 [+0.0283, +0.0404], \(p_{\rm Holm}\)=1.5e-04; (c) fixedpt +0.0231 [+0.0193, +0.0270], \(p_{\rm Holm}\)=1.5e-04.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | −0.0523 (−) | −0.0662 (−) | −0.0513 (−) |
| (b) phase | −0.0133 (−) | −0.0184 (−) | −0.0129 (−) |
| (c) fixedpt | −0.0245 (−) | −0.0292 (−) | −0.0253 (−) |
| rand | −0.0476 (−) | −0.0634 (−) | −0.0461 (−) |
| blind-alt | +0.0006 (0) | +0.0027 (0) | +0.0000 (=0) |

### clifford1-full

**C1 ⊗ I, full group** (`clifford1-full`). The 24 single-qubit Cliffords on qubit A, \(H(F)=\log_2 24=4.585\) bits. This pool is **deterministic**: only \(V_f\) (used by rand) changes with the draw.

- Blind grid-mean \(I(F;Y)\) = 0.0000 bits; blind output laws at \(g=0,r=16\): 1.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0030 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | +0.1479 | exact | – | – | 1.527 | 6.0 | +0.0322 | n/a | deterministic (exact) | deterministic; = informed I(F;Y) (blind = 0) |
| (b) phase | +0.0000 | exact | – | – | 0.000 | 1.0 | +0.0000 | n/a | exactly zero | exact 0 (construction: hint f-independent) |
| (c) fixedpt | +0.1769 | exact | – | – | 1.726 | 7.0 | +0.0386 | n/a | deterministic (exact) | deterministic; = informed I(F;Y) (blind = 0) |
| readable | +0.2850 | exact | – | – | 1.000 | 2.0 | +0.0622 | n/a | deterministic (exact) | by construction, deterministic |
| rand | +0.0587 | [+0.0558, +0.0617] | 5.0e-05 | 40/0 | 1.859 | 24.0 | +0.0128 | n/a | gap > 0 | label leak, sign by construction |
| blind-alt | +0.0000 | exact | – | – | 0.000 | 1.0 | +0.0000 | n/a | exactly zero | exact 0 (construction) |
| gphase | +0.0000 | exact | – | – | 0.000 | 1.0 | +0.0000 | n/a | exactly zero | exact 0 (construction) |

No paired comparison against rand: (a) and (c) are deterministic on this pool.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | +0.1479 (det) | +0.1841 (det) | +0.1413 (det) |
| (b) phase | +0.0000 (=0) | +0.0000 (=0) | +0.0000 (=0) |
| (c) fixedpt | +0.1769 (det) | +0.2243 (det) | +0.1689 (det) |
| rand | +0.0587 (+) | +0.0656 (+) | +0.0575 (+) |
| blind-alt | +0.0000 (=0) | +0.0000 (=0) | +0.0000 (=0) |

### clifford2

**Two-qubit Clifford subset** (`clifford2`). A random 50-element subset, per draw, of the 11 520-element two-qubit Clifford group (mod phase).

- Blind grid-mean \(I(F;Y)\) = 0.0727 bits; blind output laws at \(g=0,r=16\): 6.0.
- Resolution floor (largest 95% CI half-width among tested variants) = 0.0089 bits.

| Variant | Mean gap | 95% CI | \(p_{\rm Holm}\) | Sig. points +/− | \(\chi_{\rm in}\) | Laws | gap/H(F) | gap/\(I_{\rm blind}\) | Verdict | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| (a) eigen | −0.0136 | [−0.0190, −0.0079] | 3.0e-04 | 0/11 | 1.896 | 35.0 | −0.0024 | −0.187 | gap < 0 | empirical |
| (b) phase | −0.0061 | [−0.0149, +0.0028] | 2.1e-01 | 0/0 | 0.722 | 16.9 | −0.0011 | −0.084 | **consistent with zero** | empirical |
| (c) fixedpt | −0.0087 | [−0.0144, −0.0029] | 1.4e-02 | 0/3 | 1.897 | 30.5 | −0.0015 | −0.120 | gap < 0 | empirical |
| readable | +0.2124 | [+0.2065, +0.2181] | 3.0e-04 | 30/10 | 1.910 | 2.0 | +0.0376 | 2.923 | gap > 0 | by construction |
| rand | −0.0129 | [−0.0187, −0.0074] | 4.0e-04 | 0/8 | 1.906 | 50.0 | −0.0023 | −0.178 | gap < 0 | empirical |
| blind-alt | +0.0007 | [−0.0001, +0.0014] | 2.1e-01 | 0/0 | 0.000 | 6.0 | +0.0001 | 0.009 | **consistent with zero** | empirical |
| gphase | +0.0000 | exact | – | – | 0.000 | 6.0 | +0.0000 | 0.000 | exactly zero | exact 0 (construction) |

Paired comparison with the random-label control, \(T=1\) (gap(variant) − gap(rand), Holm across 3): (a) eigen −0.0006 [−0.0029, +0.0016], \(p_{\rm Holm}\)=5.8e-01; (b) phase +0.0068 [+0.0011, +0.0127], \(p_{\rm Holm}\)=5.6e-02; (c) fixedpt +0.0042 [+0.0008, +0.0076], \(p_{\rm Holm}\)=5.2e-02.

Verdicts across temperature (grid-mean gap in bits; 0 = consistent with zero, +/− = significant sign, =0 exact, det = deterministic):

| Variant | T=1 | T=0 | T=∞ |
|---|---|---|---|
| (a) eigen | −0.0136 (−) | −0.0192 (−) | −0.0135 (−) |
| (b) phase | −0.0061 (0) | −0.0083 (0) | −0.0063 (0) |
| (c) fixedpt | −0.0087 (−) | −0.0125 (−) | −0.0090 (−) |
| rand | −0.0129 (−) | −0.0192 (−) | −0.0126 (−) |
| blind-alt | +0.0007 (0) | +0.0028 (0) | +0.0000 (0) |

### The two construction-free positive cases in detail

**[eigbasis-hadamard] ensemble mean gap, phase, T=1 (* Holm per-point p<0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | +0.0903* | -0.0036 | +0.0769* | +0.0185 |
| 0.1 | +0.0708* | -0.0065 | +0.0579* | +0.0038 |
| 0.2 | +0.0551* | -0.0072 | +0.0439* | -0.0037 |
| 0.3 | +0.0420* | -0.0067 | +0.0328* | -0.0071 |
| 0.4 | +0.0309* | -0.0057 | +0.0239* | -0.0079 |
| 0.5 | +0.0217* | -0.0044 | +0.0166* | -0.0071 |
| 0.6 | +0.0141* | -0.0031 | +0.0107* | -0.0054 |
| 0.7 | +0.0081* | -0.0019 | +0.0062* | -0.0035 |
| 0.8 | +0.0037* | -0.0009 | +0.0028* | -0.0017 |
| 0.9 | +0.0010* | -0.0002 | +0.0007* | -0.0004 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

The positive cells sit at \(r=2\) and \(r=8\). There, blind's extra bit is a qubit-A population that is uniform for every \(f\) (trap 4). At \(r=4\) and \(r=16\), blind reads qubit B and does as well or better.

**[eigbasis-pert] ensemble mean gap, eigen, T=1 (* Holm per-point p<0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | +0.0168 | +0.0393 | +0.0518 | +0.0673 |
| 0.1 | +0.0134 | +0.0276 | +0.0383 | +0.0488 |
| 0.2 | +0.0106 | +0.0193 | +0.0282 | +0.0350 |
| 0.3 | +0.0081 | +0.0133 | +0.0204 | +0.0247 |
| 0.4 | +0.0060 | +0.0090 | +0.0145 | +0.0170 |
| 0.5 | +0.0042 | +0.0059 | +0.0098 | +0.0113 |
| 0.6 | +0.0028 | +0.0036 | +0.0063 | +0.0070 |
| 0.7 | +0.0016 | +0.0020 | +0.0036 | +0.0040 |
| 0.8 | +0.0007 | +0.0009 | +0.0016 | +0.0018 |
| 0.9 | +0.0002 | +0.0002 | +0.0004 | +0.0005 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

The (a) eigen gap on the perturbed pool is consistently positive and grows with rank. But no single point survives Holm, and the aggregate is significant only at \(T=\infty\).

## 5. Balance sheet

- **\(X=M\):** \(I(X;Y)+I(F;Y)\le H(Y)\) holds 44/44 for every pool and variant (a theorem, since \(M\perp F\)).
- **\(X=(M,\text{hint})\):** not a theorem. On the canonical draws it fails only for readable (40/44 on every pool) and for (a) eigen on `eigbasis-identity` (38/44).
- **\(I(X,F;Y)\le H(Y)\):** holds everywhere.

## 6. Status and non-claims

- This is a toy proof-of-concept. It is **not evidence about hadronic or QCD physics** and makes no physical claim.
- Removing Haar symmetry does open nonzero gaps, but they are mostly negative or forced by construction:
  - which basis the readout can see (traps 3–5);
  - informed information carried entirely by the input (trap 1).
- The only construction-free positive gaps are small (≤ about 2× the pool floor):
  - one comes from a blind spot of the blind input (`eigbasis-hadamard`, (b));
  - the other (`eigbasis-pert`, (a)/(c)) is not robustly significant.
- The input's Holevo information about \(f\) does not predict the gap.
- Modelling choices: 2 channel uses; nested Z readout only; \(\varepsilon=0.1\) for the perturbed pool; 50-element random subsets (24 for `clifford1-full`); the CE-10 encodings, unchanged apart from the degeneracy-safe eigensolver. Monotonicity of the gap in \(g\) and rank was not re-tested here (see CE-10). No energy-bounded pool was built.
