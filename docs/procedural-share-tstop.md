# Stopping-time variants of the energy-bounded (Margolus–Levitin) pool (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model and proof-of-concept** in a two-qubit setting.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim. "Energy budget" and "Margolus–Levitin (ML) time" are used only in their textbook finite-dimensional sense.

**Status:** 2026-11-26 · computed. Follow-up to the [energy-bounded (Margolus–Levitin) candidate pool](procedural-share-mlpool.md) (CE-12 / CE-15). The energy budget, the \(\varepsilon\) clustering, the noiseless output law and every share function are **unchanged**. Only the stopping time varies: \(t = k\, t_{\rm ML}\) for \(k \in \{1,2,4,8\}\).

**Script:** [`simulations/classical/procedural_share_tstop.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share_tstop.py) (imports `procedural_share_mlpool.py` by path; built-in checks; about 130 s with the defaults, 8 s with `--seeds 0`). No pool JSON is written: every pool regenerates from the seed. Every number below is printed by:

```
python simulations/classical/procedural_share_tstop.py              # defaults: 40 draws
python simulations/classical/procedural_share_tstop.py --seeds 0    # canonical draw and CE-6 only
```

## Summary

| Question | Answer | Kind |
|---|---|---|
| Does the bound's survival rate depend on sitting exactly at \(t_{\rm ML}\)? | **No, not in the hold/fail counts that were the question.** On the two-qubit surfaces, at every multiple, the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) holds at every blind point (44/44 canonical; 1760/1760 over 40 draws) and the original form \(I(X;Y)+H(F\mid Y)\le H(Y)\) fails at every point (44/44; 1760/1760). The informed overlap-corrected bound holds everywhere; the informed corrected-hold counts are 40/44 (GAD, nested) and 11/44 (dephasing, nested) at every multiple, as in CE-12. On the one-bit pool A-ml set the corrected bound holds at every defined point at every multiple. The original-form *failure count* on that set does change (38, 40, 43, 54 of the defined points at \(1\times,2\times,4\times,8\times\)), because the 20 ML one-bit laws move and the \(\varepsilon\)-class of the GAD channel moves with them. 36 of the 38 failures at \(1\times\) fail at every multiple. | Empirical (this toy, this grid) |
| Are the \(2\times/4\times/8\times\) pools degenerate with \(1\times\), or with the identity? | **No.** The 200 Hamiltonians are the same (\(U(k)=U(1)^k\) to \(10^{-14}\)). Median TV between a sample's noiseless law at \(k\times\) and at \(1\times\) is 0.46–0.51; **no** sample is within \(\varepsilon=0.05\) of its \(1\times\) law or of the identity. Only \(4\times\) has any clustering: two merges, \(\lvert{\rm pool}\rvert=198\). | Check of the sampler + empirical |
| Does evolving past \(t_{\rm ML}\) wrap phases back? | In part, not as a collapse. At \(4\times\), \(t=2\pi/B\), so an eigenstate at the reference energy \(E=B\) returns to itself. \(E_{\max}\) reaches 4.416, so the unitary does not. 18/200 Hamiltonians have an excited eigenvalue within 0.1 rad of \(2\pi\mathbb{Z}\) at \(4\times\) (0/200 at \(1\times\)). Mean fidelity \(\lvert\langle m0\vert U\vert m0\rangle\rvert^2\) is 0.3679, 0.2670, 0.3693, 0.3868. The closest law to the identity at \(4\times\) has TV 0.0518, just above \(\varepsilon\). | Spectral fact + empirical |

Net result: **sitting exactly at the ML time is not what makes the corrected bound hold or the original form fail** on these grids. Slower evolutions are distinct pools, not wrapped-back copies of the \(1\times\) pool. On the one-bit set, which points are defined depends on the stopping time; the large-deficit failures at small \(g\) do not go away.

## 1. Model

This is a parameter sweep of the CE-12 / CE-15 construction, not a rewrite. The Hamiltonian sampler (`sample_unitaries`), leader clustering (`leader_cluster`), noiseless law and all share functions are imported from [`procedural_share_mlpool.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share_mlpool.py). The settings that are held fixed are those of the saved Stage 2 pool: draw 2026 with `default_rng([2026, 12])`, 200 GUE Hamiltonians, budget \(B=1\), \(\varepsilon=0.05\), reference state \(\sigma=(I/2)\otimes\lvert 0\rangle\langle 0\rvert\). Only \(t_{\rm frac}=t/t_{\rm ML}\) takes values in \(\{1,2,4,8\}\). The one-bit pool A-ml construction is the same as CE-15 (30 non-Haar members of pool A plus the one-bit laws of the first 20 representatives in draw order). The surface grid is the CE-12 grid: GAD at \(T=1\) and pure dephasing, \(g=0,0.1,\dots,1\), ranks \(2,4,8,16\), nested Z and random-basis readouts, blind and readable inputs. The ensemble is 40 independent draws (seeds \(1..40\)), with the same Hamiltonians evolved at each stopping time; sign-flip tests (20000 flips), bootstrap 95% CIs (10000 resamples) and Holm correction are those of CE-12.

**Checks.** At \(t_{\rm frac}=1\) the two-qubit pool is bit-identical to `simulations/classical/data/ce15_ml_pool.json` (sha256 `d11fa3d1ec4594b7…`, 200 representatives, 0 rejected). The CE-6 one-bit run on pool A-ml reproduces the documented 38/81 failures and the median deficit 2.807 bits, and agrees with `ce6_overlap(pool_source="ml")`. `procedural_share_mlpool.py` is not modified; its default output is unchanged.

**Traps, in addition to those of the parent doc.** \(t_{\rm ML}\) is a time *scale* for the mixed reference \(\sigma\), not a guarantee that any input becomes orthogonal. For a Hamiltonian with spectrum in \([0,E_{\max}]\) rescaled so that \(\langle E-E_0\rangle_{\rm ref}=B\), evolving for \(k\,t_{\rm ML}\) can wrap some eigenphases: at \(k=4\), \(t=2\pi/B\), components near the reference energy return to themselves. That does not make \(U\) the identity unless the whole excited spectrum wraps together, which it does not (\(E_{\max}\) is not equal to \(B\)).

## 2. Pool sizes and distinctness

Canonical Hamiltonians (seed 2026). First 20 representative indices are \(0..19\) at every multiple, so the 20 ML members of pool A-ml are the same 20 Hamiltonians, evolved for longer.

| \(t_{\rm frac}\) | representatives | \(H(F)\) (bits) | rejected | sha256 (first 16) |
|---|---|---|---|---|
| 1 | 200 | 7.644 | 0 | `d11fa3d1ec4594b7` |
| 2 | 200 | 7.644 | 0 | `667ab54690c00f02` |
| 4 | 198 | 7.629 | 0 | `0c64d7c779e833e5` |
| 8 | 200 | 7.644 | 0 | `bc0aa58fd0d2e9e9` |

The only merges are at \(4\times\): sample 75 joins representative 36 (TV 0.0340) and sample 108 joins representative 79 (TV 0.0440). The four pool hashes are distinct. \(U(2)=U(1)^2\), \(U(4)=U(1)^4\) and \(U(8)=U(1)^8\) to at most \(7\times10^{-15}\).

Same-Hamiltonian TV between noiseless per-use laws (min / median / max; fraction \(\le\varepsilon\); fraction 0):

| pair | min | median | max | frac \(\le\varepsilon\) | frac \(=0\) |
|---|---|---|---|---|---|
| \(2\times\) vs \(1\times\) | 0.1795 | 0.4872 | 0.9155 | 0 | 0 |
| \(4\times\) vs \(1\times\) | 0.1692 | 0.5021 | 0.9006 | 0 | 0 |
| \(8\times\) vs \(1\times\) | 0.0848 | 0.4600 | 0.9245 | 0 | 0 |
| \(4\times\) vs \(2\times\) | 0.1389 | 0.5257 | 0.9771 | 0 | 0 |
| \(8\times\) vs \(2\times\) | 0.0987 | 0.4900 | 0.9581 | 0 | 0 |
| \(8\times\) vs \(4\times\) | 0.0851 | 0.4615 | 0.8957 | 0 | 0 |

TV to the identity law, and mean fidelity \(\lvert\langle m0\vert U\vert m0\rangle\rvert^2\):

| \(t_{\rm frac}\) | TV vs \(I\): min / median / max | # within \(\varepsilon\) of \(I\) | mean fidelity |
|---|---|---|---|
| 1 | 0.2690 / 0.7989 / 0.9998 | 0/200 | 0.3679 |
| 2 | 0.3221 / 0.8975 / 0.9989 | 0/200 | 0.2670 |
| 4 | 0.0518 / 0.7890 / 0.9919 | 0/200 | 0.3693 |
| 8 | 0.0968 / 0.7743 / 0.9966 | 0/200 | 0.3868 |

Rescaled spectra: \(E_0=0\), \(\langle E-E_0\rangle_{\rm ref}=1\), \(E_{\max}\) min/median/mean/max = 1.225 / 1.992 / 2.104 / 4.416. Phase distance of excited eigenvalues to \(2\pi\mathbb{Z}\) (the ground state is always at phase 0):

| \(t_{\rm frac}\) | median dist (rad) | frac \(<0.1\) rad | Hamiltonians with an excited wrap \(<0.1\) rad |
|---|---|---|---|
| 1 | 1.9017 | 0.000 | 0/200 |
| 2 | 1.7990 | 0.023 | 14/200 |
| 4 | 1.5811 | 0.030 | 18/200 |
| 8 | 1.5875 | 0.032 | 19/200 |

The \(2\times/4\times/8\times\) pools are **not** degenerate with \(1\times\) or with the identity. Partial wrapping is real and is strongest near \(4\times\), but it does not collapse the pool.

## 3. Two-qubit surfaces (canonical draw)

Same grid as CE-12: \(g=0,0.1,\dots,1\), ranks \(2/4/8/16\), 44 points per surface. Median deficit is \(H(F\mid Y)-H(Y\mid X)\) at the original-form failures. The \(I(F;Y)\) and \(I(X;Y)\) columns are the values at \(g=0\), \(r=16\), to show that share *values* can move a little even when hold/fail counts do not.

Blind inputs:

| \(t_{\rm frac}\) | \(\lvert{\rm pool}\rvert\) | channel | readout | corrected holds | original fails | median deficit (bits) | \(I(F;Y)\) at \(g=0,r=16\) | \(I(X;Y)\) at \(g=0,r=16\) |
|---|---|---|---|---|---|---|---|---|
| 1 | 200 | GAD | nested | 44/44 | 44/44 | 5.331 | 0.305 | 0.108 |
| 1 | 200 | GAD | random | 44/44 | 44/44 | 5.141 | 0.125 | 0.015 |
| 1 | 200 | dephasing | nested | 44/44 | 44/44 | 5.036 | 0.305 | 0.108 |
| 1 | 200 | dephasing | random | 44/44 | 44/44 | 5.132 | 0.125 | 0.015 |
| 2 | 200 | GAD | nested | 44/44 | 44/44 | 5.307 | 0.305 | 0.049 |
| 2 | 200 | GAD | random | 44/44 | 44/44 | 5.141 | 0.129 | 0.008 |
| 2 | 200 | dephasing | nested | 44/44 | 44/44 | 4.985 | 0.305 | 0.049 |
| 2 | 200 | dephasing | random | 44/44 | 44/44 | 5.130 | 0.129 | 0.008 |
| 4 | 198 | GAD | nested | 44/44 | 44/44 | 5.304 | 0.348 | 0.120 |
| 4 | 198 | GAD | random | 44/44 | 44/44 | 5.126 | 0.126 | 0.013 |
| 4 | 198 | dephasing | nested | 44/44 | 44/44 | 4.995 | 0.348 | 0.120 |
| 4 | 198 | dephasing | random | 44/44 | 44/44 | 5.117 | 0.126 | 0.013 |
| 8 | 200 | GAD | nested | 44/44 | 44/44 | 5.326 | 0.354 | 0.128 |
| 8 | 200 | GAD | random | 44/44 | 44/44 | 5.141 | 0.130 | 0.016 |
| 8 | 200 | dephasing | nested | 44/44 | 44/44 | 5.029 | 0.354 | 0.128 |
| 8 | 200 | dephasing | random | 44/44 | 44/44 | 5.133 | 0.130 | 0.016 |

That the original form fails at every point is the same size effect as in CE-12 §5: \(H(F)\approx 7.6\) bits against \(H(Y)\le 4\). The two merges at \(4\times\) do not change it. The corrected bound on blind inputs is a theorem (\(X\perp F\)); the counts are a check.

Informed (readable) inputs. The corrected bound is not a theorem here; the overlap-corrected bound is. The informed corrected-hold counts (40/44 GAD nested; 11/44 dephasing nested; 44/44 on both random readouts) are the same at every multiple, including \(4\times\) with 198 candidates. That is expected: the readable input makes the noiseless output a \(Z\)-basis state, so those failures are by construction of the input, as in CE-12 §4, and do not depend on which unitaries are in the pool. Identity residuals are at most \(5.3\times10^{-15}\). The original form still fails at 44/44.

## 4. CE-6 one-bit run on pool A-ml

Variant (a), \(\varepsilon=0.05\), same \((g,p)\) grid as CE-6. Pool size 50 at every multiple. The uniform and capacity inputs give the same defined and failure *counts* at each multiple (deficits at individual points can differ). Figures below are for the uniform input; the capacity row is in the script output and agrees on the counts.

| \(t_{\rm frac}\) | defined pts | original fails | corrected holds | deficit min / median / max (bits) | failures also failing at \(1\times\) | defined also defined at \(1\times\) |
|---|---|---|---|---|---|---|
| 1 | 81 | 38 | 81/81 | 0.193 / 2.807 / 2.933 | 38/38 | 81/81 |
| 2 | 70 | 40 | 70/70 | 0.045 / 2.807 / 2.807 | 36/40 | 45/70 |
| 4 | 87 | 43 | 87/87 | 0.008 / 2.807 / 2.807 | 36/43 | 38/87 |
| 8 | 101 | 54 | 101/101 | 0.199 / 1.585 / 2.916 | 36/54 | 64/101 |

**How the failure set moves.** 36 of the 38 failures at \(1\times\) fail at every multiple; they include the entire \(g=0\) and \(g=0.05\) rows that are defined. The two that drop are \((g,p)=(0.5,0.5)\) and \((0.6,0.75)\): at each later multiple each of them is either undefined or holds with class size \(k=1\). New failures appear as the \(\varepsilon\)-class moves (4 at \(2\times\), 7 at \(4\times\), 18 at \(8\times\)). Those new failures have small deficits (medians 0.121, 0.212, 0.330 bits). The median deficit of the 36 persistent failures stays 2.807 bits at every multiple. The drop of the *overall* median at \(8\times\) (to 1.585 bits) is from the added mid-\(g\) failures, not from a shrinking of the persistent deficit.

Original-form hold rates among defined points are 43/81, 30/70, 44/87 and 47/101 (53.1%, 42.9%, 50.6%, 46.5%). There is no trend that favours sitting at \(t_{\rm ML}\), and no multiple at which the original form starts to hold in general. The corrected bound holds at every defined point.

## 5. Ensemble (40 draws)

Pool sizes stay large: \(1\times\) 199–200 (median 200); \(2\times\) 198–200 (200); \(4\times\) 197–200 (200); \(8\times\) 194–200 (198). A few more merges appear at \(8\times\) than on the canonical draw, but not enough to change \(H(F)\) by much.

Blind pass counts, summed over draws (1760 = 40 × 44 points), are the same at every multiple and every (channel, readout): corrected bound 1760/1760, original form fails 1760/1760. Mean median-deficits remain between 4.98 and 5.33 bits. Informed overlap-corrected holds are 1760/1760 everywhere. Informed corrected holds are 1600/1760 (GAD nested; 40/44 per draw) and 440/1760 (dephasing nested; 11/44 per draw) at every multiple, and 1760/1760 on both random readouts. The original form fails at every informed point too. Those hold/fail counts do not depend on the stopping time in this ensemble.

Share *values* on the nested readout do move slightly. Paired tests of each multiple versus \(1\times\), mean over nontrivial grid points (sign-flip 20000, bootstrap 95% CI 10000, Holm across 30 tests): on GAD nested, mean \(I(F;Y)\) is 0.0586 bits at \(1\times\) and higher by 0.0036 / 0.0068 / 0.0093 bits at \(2\times/4\times/8\times\) (Holm \(p=0.0015\); 31, 37 and 40 of 40 draws). The normalised share \(H(F\mid Y)/H(F)\) moves in the other direction by about \(10^{-3}\), as it must at nearly fixed pool size. Dephasing nested is similar, with a larger \(I(F;Y)\) shift (0.011 to 0.026 bits). On the random readout the GAD differences are consistent with zero after Holm; dephasing random shows a \(+0.0007\) to \(+0.0010\) bit shift in \(I(F;Y)\). Informed corrected-hold counts do not differ from \(1\times\) in any draw. These are share-value differences, not a change in whether the bounds hold or fail.

## 6. Reading

- **Survival of the bounds, as hold/fail counts, does not depend on sitting at the ML time** on the two-qubit grid, in this toy, with this budget and this \(\varepsilon\). The original form fails everywhere there because \(H(F)\) is still about 7.6 bits. The corrected bound on blind inputs is a theorem and holds at every multiple, as checked.
- **Slower evolutions are distinct pools.** Partial phase wrapping occurs and is stated above; it does not make the \(2\times/4\times/8\times\) pools copies of \(1\times\) or of the identity.
- **On the one-bit A-ml set the \(\varepsilon\)-class moves with the stopping time**, so the number of defined points and of original-form failures changes. The corrected bound still holds at every defined point. The 36 large-deficit failures at small \(g\) persist. That is a change in class membership, not evidence that sitting at \(t_{\rm ML}\) is special for the bound.
- \(t_{\rm frac}<1\) is still untested on the surfaces. The parent size table already shows that short evolutions collapse toward the identity (3 clusters at \(t_{\rm frac}=0.1\), \(n=1000\), \(\varepsilon=0.05\)).

## 7. Scope

Tier 2 only. A two-qubit, two-use toy with one Hamiltonian ensemble, one clustering rule, one encoding, one channel family and the stopping times \(t_{\rm frac}\in\{1,2,4,8\}\). Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this run beyond the information-theoretic bookkeeping above.
