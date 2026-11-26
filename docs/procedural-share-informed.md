# Informed-input procedural share: does an f-dependent input lower H(F|Y)? (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model and proof-of-concept** in a two-qubit setting.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim.

**Status:** 2026-11-26 · computed. Follow-up (CE-10) to the [procedural-share surface](procedural-share-surface.md) (CE-9). The CE-9 trends in rank and in damping were guaranteed by construction. Here the lever is different: let the **input depend on the selected unitary \(f\)**, and measure whether that lowers the procedural share \(H(F\mid Y)\).

**Script:** [`simulations/classical/procedural_share_informed.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share_informed.py) (pure numpy; imports `procedural_share_surface.py`; built-in self-checks; about 10 s). Every number below is printed by:

```
python simulations/classical/procedural_share_informed.py              # T=1, 40 pool draws, + T=0, inf re-tests
python simulations/classical/procedural_share_informed.py --markdown --no-robust-T   # the tables below
```

Flags: `--variants`, `--seed` (canonical pool, 2026), `--seeds K` (ensemble pool draws), `--pool`, `--T`, `--gammas`, `--ranks`, `--flips`, `--boot`, `--no-robust-T`, `--markdown`.

## 1. Summary

- **None of the three structural "hint" encodings lowers \(H(F\mid Y)\) detectably.** The eigenbasis, eigenphase-pattern and fixed-point variants are all **consistent with zero gap** over 40 independent pool draws, at \(T=1\), \(0\) and \(\infty\). The Holm-adjusted aggregate \(p\) is at least 0.81 everywhere, and no grid point survives the per-point Holm correction.
- **The power is limited but not negligible.** Positive mean gaps above about 0.004 bits are excluded for all three; the upper 95% bounds are 0.0008, 0.0011 and 0.0038. That is about 6% of the blind \(I(F;Y)\) grid mean of 0.061 bits.
- **They also do no better than a structureless label.** Relative to the random-label control, the paired differences are −0.003, −0.0025 and −0.0002 bits, with Holm \(p\ge 0.17\). There is no evidence that aligning the input with \(U_f\)'s structure helps.
- **Large input-side correlation, no operational gap.**
  - The eigen, fixedpt and rand inputs carry \(\chi_{\rm in}\approx1.9\) bits of Holevo information about \(f\), and phase carries 0.74–0.80 bits.
  - The ensemble-mean gap is about \(10^{-3}\) bits averaged over the grid, and at most 0.011 bits in magnitude at any point. It does not correlate with \(\chi_{\rm in}\) across pools (\(|r|\le0.16\)).
  - The global-phase tag carries the full \(\log_2 50\) bits as a classical label but \(\chi_{\rm in}=0\) and a gap of exactly 0.
  - So neither classical tag information nor \(\chi_{\rm in}\) predicts the gap here.
- **A single pool is misleading.** On the canonical pool (seed 2026) the eigen gap is positive at all 40 non-trivial points (up to +0.012 bits), and the phase gap is negative at most of them (down to −0.041). Over pool draws, both are indistinguishable from zero. Point estimates on one pool are not evidence.
- **Only the by-construction control shows a gap.** The readable-tag control, which writes one bit of \(f\) straight into the readout, has an aggregate gap of +0.22 bits (\(p_{\rm Holm}=3\times10^{-4}\)). That is the leak-through-the-input effect the controls were built to expose. It is not structure.
- **Why zero was expected for three of the variants:** for eigen, rand and blind-alt, zero expected gap is a theorem (Haar invariance, §4). The test confirms it, which calibrates the test. For phase and fixedpt, zero is an empirical result.
- **Balance sheet:**
  - With \(X\) = message, \(I(X;Y)+I(F;Y)\le H(Y)\) passes 44/44, as a theorem.
  - With \(X\) = full preparation label, it is no longer a theorem, and it fails at 4/44 points for the readable control.
  - \(I(X,F;Y)\le H(Y)\) holds everywhere.

**Zero-gap flags:** **eigen (a), phase (b), fixedpt (c), rand (control) and blind-alt (control) are all CONSISTENT WITH ZERO.** gphase is exactly zero by construction.

## 2. Setup (fixed before any result was computed)

**Pools.**

- Canonical pool: 50 Haar two-qubit unitaries \(U_f\), seed 2026, the same as CE-9.
- Ensemble: seeds 1–40, each a fresh pool.
- The structureless-control unitaries \(V_f\) come from an independent stream (`default_rng([seed, 5000])`) and are drawn in the same step.
- Everything is SHA-256 hashed before any noise parameter exists and re-checked after every condition. The canonical pool + \(V\) hash is `c88c1c0ec1023009…`.

**Block, noise and readout:** as in CE-9.

- 2 channel uses with the same unknown \(f\).
- Message \(M=(m_1,m_2)\), each \(m\in\{0,1\}\), uniform and **independent of \(F\)**. The prior over \(F\) is uniform.
- Each use applies the input \(\lvert\psi_{f,m}\rangle\), then \(U_f\), then GAD\((g,p)\) on each qubit, with \(p=1/(1+e^{-1/T})\).
- Nested Z readout, rank \(r\in\{2,4,8,16\}\), \(g\in\{0,0.1,\dots,1\}\).
- Everything is computed exactly from probabilities.

**Input variants.** In every variant, \(\lvert\psi_{f,0}\rangle\perp\lvert\psi_{f,1}\rangle\). The input state depends on \(f\); the message itself does not.

| Variant | \(\lvert\psi_{f,m}\rangle\) | Role | \(\chi_{\rm in}\) (canonical) |
|---|---|---|---|
| blind | \(\lvert m\,0\rangle\) | CE-9 reference | 0 |
| blind-alt | \(\lvert m\,1\rangle\) | another \(f\)-independent input (control) | 0 |
| **(a) eigen** | eigenvectors \(e_0,e_1\) of \(U_f\) (eigenphases sorted in \((-\pi,\pi]\)) | a basis \(U_f\) preserves: \(U_f\) acts only as a phase | 1.886 |
| **(b) phase** | \(\tfrac12\sum_k e^{i\phi_k(f)}(-1)^{m\,a(k)}\lvert k\rangle\), with \(\phi_k\) the sorted eigenphases and \(a(k)\) the qubit-A bit | phase pattern tied to the eigenvalues | 0.800 |
| **(c) fixedpt** | \((e_n\pm e_q)/\sqrt2\): \(e_n\) has the eigenvalue closest to \(+1\) (near-fixed), \(e_q\) the farthest | support split between the near-fixed and the most-moved eigenvector | 1.903 |
| rand | \(V_f\lvert m\,0\rangle\), \(V_f\) Haar and independent of \(U_f\) | **structureless label** control | 1.917 |
| readable | \(U_f^\dagger\lvert m\,b_f\rangle\), \(b_f=f \bmod 2\) | **leak-by-construction** control: the output is GAD\((\lvert m\,b_f\rangle)\) | 1.897 |
| gphase | \(e^{2\pi i f/50}\lvert m\,0\rangle\) | **null** control: physically identical to blind | 0 |

Eigenvector phase convention: the largest-modulus component of each eigenvector is made real and positive. It matters only for (c).

**Quantities.**

- Gap: \(H(F\mid Y)_{\rm blind}-H(F\mid Y)_{\rm variant}=I(F;Y)_{\rm variant}-I(F;Y)_{\rm blind}\), with blind and variant on the same pool.
- Input-function correlation:
  - \(\chi_{\rm in}\), the Holevo information between \(F\) and the block input state \(\sigma_f\otimes\sigma_f\), where \(\sigma_f=\tfrac12\sum_m\lvert\psi_{f,m}\rangle\langle\psi_{f,m}\rvert\);
  - \(I(S;F)\), the classical information in the hint label \(S\): \(\log_2 50\) for \(S=f\), 1 bit for readable, 0 for blind.
- \(\chi_{\rm out}(g)\): the Holevo information between \(F\) and the block output state.

## 3. Results on the canonical pool (seed 2026, \(T=1\))

**H(F|Y) BLIND [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.609 | 5.486 | 5.453 | 5.338 |
| 0.1 | 5.616 | 5.529 | 5.502 | 5.419 |
| 0.2 | 5.622 | 5.561 | 5.539 | 5.480 |
| 0.3 | 5.627 | 5.585 | 5.568 | 5.527 |
| 0.4 | 5.631 | 5.603 | 5.591 | 5.563 |
| 0.5 | 5.635 | 5.617 | 5.608 | 5.590 |
| 0.6 | 5.638 | 5.627 | 5.621 | 5.611 |
| 0.7 | 5.640 | 5.635 | 5.631 | 5.626 |
| 0.8 | 5.642 | 5.640 | 5.638 | 5.636 |
| 0.9 | 5.643 | 5.643 | 5.642 | 5.642 |
| 1.0 | 5.644 | 5.644 | 5.644 | 5.644 |

Each cell below is **informed \(H(F\mid Y)\) / gap** (bits). gphase is identical to blind (gap 0 at every point) and is omitted.

**eigen: H(F|Y) informed / gap [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.598 / +0.0112 | 5.484 / +0.0016 | 5.441 / +0.0118 | 5.334 / +0.0035 |
| 0.1 | 5.607 / +0.0087 | 5.526 / +0.0025 | 5.491 / +0.0105 | 5.414 / +0.0048 |
| 0.2 | 5.615 / +0.0068 | 5.558 / +0.0028 | 5.530 / +0.0092 | 5.475 / +0.0054 |
| 0.3 | 5.622 / +0.0051 | 5.582 / +0.0028 | 5.560 / +0.0077 | 5.522 / +0.0054 |
| 0.4 | 5.627 / +0.0038 | 5.601 / +0.0025 | 5.584 / +0.0061 | 5.558 / +0.0049 |
| 0.5 | 5.632 / +0.0026 | 5.615 / +0.0021 | 5.603 / +0.0046 | 5.586 / +0.0040 |
| 0.6 | 5.636 / +0.0017 | 5.626 / +0.0015 | 5.618 / +0.0032 | 5.608 / +0.0030 |
| 0.7 | 5.639 / +0.0010 | 5.634 / +0.0009 | 5.629 / +0.0019 | 5.624 / +0.0019 |
| 0.8 | 5.642 / +0.0005 | 5.639 / +0.0005 | 5.637 / +0.0009 | 5.635 / +0.0009 |
| 0.9 | 5.643 / +0.0001 | 5.643 / +0.0001 | 5.642 / +0.0002 | 5.642 / +0.0002 |
| 1.0 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 |

**phase: H(F|Y) informed / gap [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.617 / -0.0079 | 5.507 / -0.0214 | 5.481 / -0.0286 | 5.379 / -0.0408 |
| 0.1 | 5.622 / -0.0063 | 5.542 / -0.0127 | 5.520 / -0.0186 | 5.444 / -0.0248 |
| 0.2 | 5.627 / -0.0050 | 5.568 / -0.0072 | 5.551 / -0.0120 | 5.495 / -0.0144 |
| 0.3 | 5.631 / -0.0038 | 5.589 / -0.0037 | 5.576 / -0.0074 | 5.535 / -0.0076 |
| 0.4 | 5.634 / -0.0029 | 5.605 / -0.0016 | 5.595 / -0.0044 | 5.566 / -0.0034 |
| 0.5 | 5.637 / -0.0020 | 5.617 / -0.0005 | 5.611 / -0.0025 | 5.591 / -0.0010 |
| 0.6 | 5.639 / -0.0013 | 5.627 / +0.0000 | 5.623 / -0.0013 | 5.611 / +0.0000 |
| 0.7 | 5.641 / -0.0008 | 5.635 / +0.0002 | 5.632 / -0.0006 | 5.625 / +0.0003 |
| 0.8 | 5.643 / -0.0003 | 5.640 / +0.0001 | 5.638 / -0.0002 | 5.635 / +0.0003 |
| 0.9 | 5.644 / -0.0001 | 5.643 / +0.0000 | 5.642 / -0.0000 | 5.642 / +0.0001 |
| 1.0 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 |

**fixedpt: H(F|Y) informed / gap [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.604 / +0.0053 | 5.512 / -0.0264 | 5.474 / -0.0218 | 5.388 / -0.0502 |
| 0.1 | 5.612 / +0.0041 | 5.545 / -0.0160 | 5.514 / -0.0123 | 5.450 / -0.0309 |
| 0.2 | 5.619 / +0.0031 | 5.570 / -0.0094 | 5.546 / -0.0065 | 5.499 / -0.0184 |
| 0.3 | 5.624 / +0.0023 | 5.590 / -0.0051 | 5.571 / -0.0029 | 5.537 / -0.0102 |
| 0.4 | 5.629 / +0.0017 | 5.606 / -0.0025 | 5.591 / -0.0008 | 5.568 / -0.0050 |
| 0.5 | 5.634 / +0.0012 | 5.618 / -0.0009 | 5.608 / +0.0002 | 5.592 / -0.0019 |
| 0.6 | 5.637 / +0.0008 | 5.627 / -0.0002 | 5.621 / +0.0006 | 5.611 / -0.0004 |
| 0.7 | 5.640 / +0.0005 | 5.635 / +0.0001 | 5.631 / +0.0006 | 5.625 / +0.0002 |
| 0.8 | 5.642 / +0.0002 | 5.640 / +0.0001 | 5.638 / +0.0004 | 5.635 / +0.0003 |
| 0.9 | 5.643 / +0.0001 | 5.643 / +0.0000 | 5.642 / +0.0001 | 5.642 / +0.0001 |
| 1.0 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 |

**rand: H(F|Y) informed / gap [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.600 / +0.0088 | 5.503 / -0.0173 | 5.462 / -0.0094 | 5.370 / -0.0319 |
| 0.1 | 5.609 / +0.0073 | 5.540 / -0.0114 | 5.507 / -0.0048 | 5.441 / -0.0216 |
| 0.2 | 5.616 / +0.0058 | 5.568 / -0.0073 | 5.541 / -0.0018 | 5.495 / -0.0140 |
| 0.3 | 5.622 / +0.0045 | 5.589 / -0.0044 | 5.568 / -0.0001 | 5.536 / -0.0086 |
| 0.4 | 5.628 / +0.0034 | 5.606 / -0.0025 | 5.590 / +0.0008 | 5.568 / -0.0049 |
| 0.5 | 5.632 / +0.0024 | 5.618 / -0.0013 | 5.607 / +0.0011 | 5.593 / -0.0026 |
| 0.6 | 5.636 / +0.0016 | 5.628 / -0.0006 | 5.620 / +0.0010 | 5.612 / -0.0011 |
| 0.7 | 5.640 / +0.0009 | 5.635 / -0.0002 | 5.631 / +0.0007 | 5.626 / -0.0004 |
| 0.8 | 5.642 / +0.0004 | 5.640 / -0.0001 | 5.638 / +0.0004 | 5.636 / -0.0001 |
| 0.9 | 5.643 / +0.0001 | 5.643 / -0.0000 | 5.642 / +0.0001 | 5.642 / -0.0000 |
| 1.0 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 |

**readable: H(F|Y) informed / gap [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.644 / -0.0349 | 4.644 / +0.8420 | 4.644 / +0.8087 | 4.644 / +0.6938 |
| 0.1 | 5.644 / -0.0281 | 4.923 / +0.6054 | 4.923 / +0.5784 | 4.752 / +0.6672 |
| 0.2 | 5.644 / -0.0222 | 5.101 / +0.4594 | 5.101 / +0.4378 | 4.883 / +0.5972 |
| 0.3 | 5.644 / -0.0171 | 5.240 / +0.3452 | 5.240 / +0.3286 | 5.022 / +0.5053 |
| 0.4 | 5.644 / -0.0127 | 5.351 / +0.2522 | 5.351 / +0.2398 | 5.159 / +0.4039 |
| 0.5 | 5.644 / -0.0090 | 5.441 / +0.1758 | 5.441 / +0.1670 | 5.288 / +0.3019 |
| 0.6 | 5.644 / -0.0059 | 5.513 / +0.1138 | 5.513 / +0.1080 | 5.404 / +0.2064 |
| 0.7 | 5.644 / -0.0034 | 5.569 / +0.0653 | 5.569 / +0.0619 | 5.502 / +0.1234 |
| 0.8 | 5.644 / -0.0016 | 5.610 / +0.0298 | 5.610 / +0.0282 | 5.578 / +0.0581 |
| 0.9 | 5.644 / -0.0004 | 5.635 / +0.0077 | 5.635 / +0.0073 | 5.626 / +0.0153 |
| 1.0 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 |

**blindalt: H(F|Y) informed / gap [canonical pool, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.609 / +0.0000 | 5.488 / -0.0020 | 5.455 / -0.0019 | 5.341 / -0.0037 |
| 0.1 | 5.616 / +0.0001 | 5.530 / -0.0010 | 5.503 / -0.0009 | 5.421 / -0.0019 |
| 0.2 | 5.622 / +0.0001 | 5.561 / -0.0005 | 5.540 / -0.0004 | 5.481 / -0.0010 |
| 0.3 | 5.627 / +0.0001 | 5.585 / -0.0002 | 5.568 / -0.0001 | 5.528 / -0.0004 |
| 0.4 | 5.631 / +0.0001 | 5.603 / -0.0000 | 5.591 / +0.0000 | 5.563 / -0.0001 |
| 0.5 | 5.635 / +0.0001 | 5.617 / +0.0000 | 5.608 / +0.0001 | 5.590 / +0.0001 |
| 0.6 | 5.638 / +0.0000 | 5.627 / +0.0000 | 5.621 / +0.0001 | 5.611 / +0.0001 |
| 0.7 | 5.640 / +0.0000 | 5.635 / +0.0000 | 5.631 / +0.0001 | 5.626 / +0.0001 |
| 0.8 | 5.642 / +0.0000 | 5.640 / +0.0000 | 5.638 / +0.0000 | 5.636 / +0.0000 |
| 0.9 | 5.643 / +0.0000 | 5.643 / +0.0000 | 5.642 / +0.0000 | 5.642 / +0.0000 |
| 1.0 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 | 5.644 / +0.0000 |

## 4. Bounds: guaranteed vs empirical

| Statement | Status | Result |
|---|---|---|
| \(-I(F;Y)_{\rm blind}\le\) gap \(\le\min(\log_2 r,\log_2 50)-I(F;Y)_{\rm blind}\) | Guaranteed | holds, all variants |
| \(I(F;Y)\le\chi_{\rm out}(g)\) (Holevo) | Guaranteed | holds, all variants |
| gap \(=0\) at \(g=1\) | Guaranteed (output independent of input) | \(\lvert\text{gap}\rvert\le 3\times10^{-15}\) |
| gap \(\le\chi_{\rm in}\) | **Not a theorem.** It holds when \(F\to\)input\(\to Y\) is Markov (gphase; eigen, where \(U_f\) is a phase on its own eigenvectors). | holds 44/44 for every \(f\)-dependent variant (trivially: \(\chi_{\rm in}\approx0.8\)–1.9 bits ≫ gap). **Fails at 19/44 for blind-alt**: \(\chi_{\rm in}=0\) but the gap is nonzero, because the gap also measures how well an input *probes* \(U_f\), not only what it already says about \(f\). |
| readable: \(I(F;Y)\le H(b_f)=1\) bit | Guaranteed | holds |
| \(E_{\rm pool}[\text{gap}]=0\) for blind-alt, eigen, rand | **Theorem (Haar invariance).** In each case the output pair \((U_f\psi_{f,0},U_f\psi_{f,1})\) is a Haar orthonormal pair, independent across \(f\): Haar eigenvectors form a Haar basis independent of the eigenvalues that order them, and \(U_fV_f\) is Haar. The informed surface then has the same distribution as the blind one. | confirmed: consistent with zero (§5). This is a check that the test is calibrated. |
| \(E_{\rm pool}[\text{gap}]=0\) for phase, fixedpt | **Not implied**: their inputs reference the computational basis or an eigenvector phase convention | empirical: consistent with zero |
| Monotonicity of each \(H(F\mid Y)\) in rank and \(g\) | Guaranteed (CE-9: coarse-graining; GAD semigroup) | — |
| Monotonicity of the **gap** in \(g\) or rank | Not guaranteed (a difference of two monotone surfaces) | Canonical pool, non-increasing \(g\)-steps out of 40: eigen 35, phase 6, fixedpt 18, rand 15, readable 30, blind-alt 21. Non-decreasing rank-steps out of 30: 14, 13, 10, 10, 19, 18. The structural gaps are not monotone. Readable is negative at \(r=2\) (the tag sits on qubit B, which \(r=2\) does not read). |

## 5. Statistical test over independent pool draws

**What randomness:**

- The canonical pool is computed exactly and has **no sampling noise**, so a test on it alone is meaningless.
- The test is over **pool draws**: seeds 1–40, with \(U_f\) and \(V_f\) redrawn per seed. Blind and informed are paired on each pool.
- No finite-shot noise is used. The question is about the *kind* of encoding, not about one pool or a finite sample.

**Null rejected or not:** \(H_0\): \(E_{\rm pool}[\text{gap}(g,r)]=0\). In words, the informed input is on average no more informative about \(f\) than the blind input.

**Procedure:**

- Aggregate statistic: per seed, the mean gap over the 40 grid points with \(g<1\).
- Two-sided sign-flip permutation test (20 000 flips), bootstrap 95% CI (10 000 resamples).
- Holm correction across the 6 tested variants.
- Per-point sign-flip tests at all 40 points, Holm-corrected within each variant.
- "Consistent with zero" means a Holm-adjusted aggregate \(p>0.05\).

**\(T=1\)** (blind \(I(F;Y)\) grid mean 0.0610 bits; per-seed range 0.042–0.073):

| Variant | Mean gap (bits) | 95% CI | \(p\) | \(p_{\rm Holm}\) | Significant points (+/−), out of 40 | \(\chi_{\rm in}\) | \(r(\chi_{\rm in},\text{gap})\) | Verdict |
|---|---|---|---|---|---|---|---|---|
| blind-alt | −0.0001 | [−0.0004, 0.0002] | 0.49 | 1.0 | 0/0 | 0.000 | — | **consistent with zero** |
| (a) eigen | −0.0017 | [−0.0042, 0.0008] | 0.21 | 1.0 | 0/0 | 1.906 | 0.02 | **consistent with zero** |
| (b) phase | −0.0012 | [−0.0036, 0.0011] | 0.35 | 1.0 | 0/0 | 0.736 | 0.02 | **consistent with zero** |
| (c) fixedpt | +0.0011 | [−0.0015, 0.0038] | 0.41 | 1.0 | 0/0 | 1.903 | 0.15 | **consistent with zero** |
| rand (control) | +0.0013 | [−0.0013, 0.0040] | 0.34 | 1.0 | 0/0 | 1.906 | 0.04 | **consistent with zero** |
| readable (control) | +0.2240 | [0.2223, 0.2259] | \(5\times10^{-5}\) | \(3\times10^{-4}\) | 30/10 | 1.905 | −0.03 | gap > 0 (by construction) |
| gphase (null) | \(7\times10^{-18}\) | exact | — | — | — | 0 | — | exactly zero |

**Structure vs structureless label:** paired differences gap(variant) − gap(rand), aggregate, Holm across 3.

- eigen: −0.0030 [−0.0059, 0.0000], \(p_{\rm Holm}=0.17\).
- phase: −0.0025 [−0.0053, 0.0003], \(p_{\rm Holm}=0.18\).
- fixedpt: −0.0002 [−0.0032, 0.0028], \(p_{\rm Holm}=0.91\).
- No detectable structure effect.

**Robustness in \(T\):** at both \(T=0\) (plain AD) and \(T=\infty\), every verdict is unchanged.

- All five non-readable tested variants are consistent with zero (Holm \(p\ge0.81\)), and no point is significant.
- Readable stays positive: +0.286 at \(T=0\), +0.217 at \(T=\infty\), \(p_{\rm Holm}=3\times10^{-4}\).
- Structure vs rand: Holm \(p\ge0.15\).

**Ensemble mean gap over \(g\times r\)** (\(T=1\), 40 pools; * marks a Holm-adjusted per-point \(p<0.05\)):

**ensemble mean gap [eigen, T=1] (* = Holm-adjusted per-point p < 0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | -0.0002 | -0.0057 | -0.0059 | -0.0107 |
| 0.1 | -0.0002 | -0.0039 | -0.0041 | -0.0074 |
| 0.2 | -0.0002 | -0.0027 | -0.0029 | -0.0051 |
| 0.3 | -0.0002 | -0.0018 | -0.0020 | -0.0035 |
| 0.4 | -0.0001 | -0.0012 | -0.0013 | -0.0024 |
| 0.5 | -0.0001 | -0.0008 | -0.0009 | -0.0015 |
| 0.6 | -0.0001 | -0.0004 | -0.0005 | -0.0009 |
| 0.7 | -0.0000 | -0.0002 | -0.0003 | -0.0005 |
| 0.8 | -0.0000 | -0.0001 | -0.0001 | -0.0002 |
| 0.9 | -0.0000 | -0.0000 | -0.0000 | -0.0000 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

**ensemble mean gap [phase, T=1] (* = Holm-adjusted per-point p < 0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | -0.0005 | -0.0035 | -0.0039 | -0.0066 |
| 0.1 | -0.0004 | -0.0024 | -0.0028 | -0.0046 |
| 0.2 | -0.0003 | -0.0017 | -0.0021 | -0.0034 |
| 0.3 | -0.0003 | -0.0013 | -0.0015 | -0.0025 |
| 0.4 | -0.0002 | -0.0009 | -0.0011 | -0.0018 |
| 0.5 | -0.0001 | -0.0006 | -0.0008 | -0.0012 |
| 0.6 | -0.0001 | -0.0004 | -0.0005 | -0.0008 |
| 0.7 | -0.0000 | -0.0002 | -0.0003 | -0.0004 |
| 0.8 | -0.0000 | -0.0001 | -0.0001 | -0.0002 |
| 0.9 | -0.0000 | -0.0000 | -0.0000 | -0.0000 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

**ensemble mean gap [fixedpt, T=1] (* = Holm-adjusted per-point p < 0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | +0.0025 | +0.0013 | +0.0035 | +0.0025 |
| 0.1 | +0.0019 | +0.0013 | +0.0030 | +0.0025 |
| 0.2 | +0.0014 | +0.0012 | +0.0025 | +0.0023 |
| 0.3 | +0.0010 | +0.0010 | +0.0020 | +0.0019 |
| 0.4 | +0.0008 | +0.0008 | +0.0015 | +0.0016 |
| 0.5 | +0.0005 | +0.0006 | +0.0011 | +0.0012 |
| 0.6 | +0.0003 | +0.0004 | +0.0008 | +0.0008 |
| 0.7 | +0.0002 | +0.0003 | +0.0005 | +0.0005 |
| 0.8 | +0.0001 | +0.0001 | +0.0002 | +0.0002 |
| 0.9 | +0.0000 | +0.0000 | +0.0001 | +0.0001 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

**ensemble mean gap [rand, T=1] (* = Holm-adjusted per-point p < 0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | +0.0027 | +0.0018 | +0.0040 | +0.0033 |
| 0.1 | +0.0021 | +0.0016 | +0.0034 | +0.0030 |
| 0.2 | +0.0016 | +0.0014 | +0.0028 | +0.0027 |
| 0.3 | +0.0012 | +0.0012 | +0.0023 | +0.0023 |
| 0.4 | +0.0009 | +0.0009 | +0.0017 | +0.0018 |
| 0.5 | +0.0006 | +0.0007 | +0.0013 | +0.0014 |
| 0.6 | +0.0004 | +0.0005 | +0.0009 | +0.0009 |
| 0.7 | +0.0002 | +0.0003 | +0.0005 | +0.0006 |
| 0.8 | +0.0001 | +0.0001 | +0.0002 | +0.0003 |
| 0.9 | +0.0000 | +0.0000 | +0.0001 | +0.0001 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

**ensemble mean gap [readable, T=1] (* = Holm-adjusted per-point p < 0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | -0.0485* | +0.8435* | +0.7982* | +0.6966* |
| 0.1 | -0.0391* | +0.6049* | +0.5679* | +0.6662* |
| 0.2 | -0.0309* | +0.4577* | +0.4281* | +0.5941* |
| 0.3 | -0.0238* | +0.3431* | +0.3201* | +0.5013* |
| 0.4 | -0.0177* | +0.2501* | +0.2329* | +0.3998* |
| 0.5 | -0.0125* | +0.1740* | +0.1618* | +0.2984* |
| 0.6 | -0.0082* | +0.1125* | +0.1044* | +0.2037* |
| 0.7 | -0.0047* | +0.0644* | +0.0597* | +0.1217* |
| 0.8 | -0.0022* | +0.0294* | +0.0272* | +0.0572* |
| 0.9 | -0.0006* | +0.0076* | +0.0070* | +0.0151* |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

**ensemble mean gap [blindalt, T=1] (* = Holm-adjusted per-point p < 0.05)**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | +0.0000 | -0.0002 | -0.0002 | -0.0005 |
| 0.1 | -0.0001 | -0.0001 | -0.0002 | -0.0003 |
| 0.2 | -0.0002 | -0.0001 | -0.0002 | -0.0002 |
| 0.3 | -0.0002 | -0.0001 | -0.0002 | -0.0002 |
| 0.4 | -0.0001 | -0.0001 | -0.0002 | -0.0001 |
| 0.5 | -0.0001 | -0.0000 | -0.0001 | -0.0001 |
| 0.6 | -0.0001 | -0.0000 | -0.0001 | -0.0001 |
| 0.7 | -0.0000 | -0.0000 | -0.0000 | -0.0000 |
| 0.8 | -0.0000 | -0.0000 | -0.0000 | -0.0000 |
| 0.9 | -0.0000 | -0.0000 | -0.0000 | -0.0000 |
| 1.0 | +0.0000 | +0.0000 | +0.0000 | +0.0000 |

## 6. Balance sheet with correlated input

- **\(X=M\)** (the message, still independent of \(F\)): \(I(X;Y)+I(F;Y)\le H(Y)\) holds 44/44 for every variant. This is a theorem, as in CE-9.
- **\(X=(M,S)\)** (the full preparation label, correlated with \(F\) whenever the hint \(S\) depends on \(f\)): the bound is **no longer a theorem**. It holds 44/44 for every variant except readable, where it holds at 40/44.
- **What holds in general:** \(I(X,F;Y)\le H(Y)\), true at every point.

## 7. Status and non-claims

- This is a toy proof-of-concept. It is **not evidence about hadronic or QCD physics** and makes no physical claim.
- **The headline is a null result.** In this toy, giving the input structural information about the active unitary does not lower the procedural share by more than about 0.004 bits on average. That is despite \(\chi_{\rm in}\approx1.9\) bits of input-side correlation.
- The input-function correlation, as \(\chi_{\rm in}\) or as \(I(S;F)\), is **not** an operational proxy for the gap here.
- The only clear gap comes from the readable control, and it is by construction.
- The zero for eigen, rand and blind-alt is guaranteed in expectation by Haar invariance. The zero for phase and fixedpt is empirical.
- Modelling choices: a Haar pool (which drives the invariance null; a structured pool could behave differently), 2 channel uses, nested Z readout only, three hand-picked structural encodings, and uniform priors.
