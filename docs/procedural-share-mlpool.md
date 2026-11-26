# Energy-bounded (Margolus–Levitin) candidate pool for the procedural share (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model and proof-of-concept** in a two-qubit setting.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical claim. "Energy budget" and "Margolus–Levitin (ML) time" are used only in their textbook finite-dimensional sense.

**Status:** 2026-11-26 · computed. Follow-up (CE-12) to the [procedural-share surface](procedural-share-surface.md) (CE-9), the [informed-input](procedural-share-informed.md) (CE-10) and the [structured-pool](procedural-share-structured.md) (CE-11) runs. The CE-9 Haar pool is replaced by a pool of **ML-time evolutions under random Hamiltonians with an energy budget**, clustered by their noiseless output statistics. The doc also locates the "58" of CE-6 and computes the overlap term \(I(X;F\mid Y)\) of the corrected bound.

**Script:** [`simulations/classical/procedural_share_mlpool.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share_mlpool.py) (pure numpy; imports `procedural_share_surface.py`, `procedural_share_informed.py` and `procedural_share.py`; built-in self-checks; about 55 s with the defaults). Every number below is printed by:

```
python simulations/classical/procedural_share_mlpool.py                                   # defaults: eps 0.05, 200 samples, 40 draws
python simulations/classical/procedural_share_mlpool.py --eps 0.2 --n-samples 1000 --no-size-table
```

Options: `--budget`, `--tfrac`, `--ref {blind,mixed}`, `--eps`, `--n-samples`, `--seeds`, `--canonical`, `--channel gad,dephasing`, `--T`, `--dg`, `--markdown`.

## Summary

| Question | Answer | Kind |
|---|---|---|
| Does the budget matter? | **No.** At \(t = t_{\rm ML}\) the budget cancels; pools are bit-identical for every budget. | Theorem (dimensional analysis); hashes confirm |
| Pool size vs \(\varepsilon\) | At \(\varepsilon \le 0.1\) almost every sample is its own representative (\(|{\rm pool}| \approx\) n_samples). Saturation starts only near \(\varepsilon \approx 0.2\)–0.3. | Empirical |
| Corrected bound \(I(X;Y)+I(F;Y) \le H(Y)\), blind inputs | Holds at every point, both channels, both readouts (44/44 per surface). | Theorem (\(X \perp F\)) |
| Original form \(I(X;Y)+H(F\mid Y) \le H(Y)\) | Fails at every point of every surface (0/44). | Empirical, expected (§5) |
| ML pool vs Haar, normalised share | Differences of order \(10^{-4}\)–\(10^{-3}\) of \(H(F)\). Against a size-matched Haar pool the **sign flips with \(\varepsilon\)**: ML is slightly *less* identifiable at \(\varepsilon=0.05\), and *more* identifiable at \(\varepsilon=0.2\). | Empirical; set by the clustering, not by the energy bound |
| Source of the "58" | CE-6, [procedural-share.md §4](procedural-share.md): variant (a), pool A, \(\varepsilon=0.05\), one-bit alphabet. Of 72 defined grid points the original form fails at 58. Reproduced exactly. | Reproduction |
| Does the overlap term rescue the original form at the 58? | **No.** There \(I(X;F)=0\), and \(I(X;F\mid Y) \le 0.029\) bits against deficits of 0.047–3.076 bits; it covers the deficit at 0 of 58 points. It cannot rescue it in general (§5). | Theorem + empirical |
| Overlap-corrected bound \(I(X;Y)+I(F;Y) \le H(Y)+I(X;F)-I(X;F\mid Y)\) | Holds at every point, including the informed points where the corrected bound fails; the identity residual is below \(5\times10^{-15}\). | Theorem; checked numerically |

Net result: **no energy-bound effect.** The ML pool behaves like a Haar pool of the same size, up to differences whose sign depends on the clustering radius. This is a null result, not a confirmation.

## 1. Model

The channel, encoding, readouts and information quantities are those of CE-9 (two qubits, two channel uses per block, half encoding, nested Z readout of rank \(r \in \{2,4,8,16\}\), random-basis readout as a control). Only the **candidate pool** is new.

1. **Hamiltonian.** \(H = (A+A^\dagger)/2\) with \(A\) a \(4\times4\) complex Ginibre matrix (GUE). Shift so the ground energy is \(E_0=0\), then rescale so that \(\langle E-E_0\rangle_{\rm ref} = \operatorname{Tr}(\rho_{\rm ref}(H-E_0)) = B\), the budget.
2. **Reference state.** Default: the blind message-averaged input \(\sigma = (I/2)\otimes|0\rangle\langle0|\). Alternative (`--ref mixed`): \(I/4\).
3. **ML time.** \(t_{\rm ML} = \pi / (2\langle E-E_0\rangle_{\rm ref})\), and \(U = e^{-iHt}\) with \(t = t_{\rm frac}\, t_{\rm ML}\) (default \(t_{\rm frac}=1\)).
4. **Clustering.** For each sample, the noiseless per-use output law under the two blind inputs with full-rank Z readout, \(L_U(y\mid m) = |\langle y|U|m0\rangle|^2\). Leader clustering in draw order: a sample joins the first representative within \(\max_m {\rm TV} \le \varepsilon\); otherwise it becomes a new one. The pool is the list of representatives; the prior is uniform, so \(H(F) = \log_2|{\rm pool}|\).
5. **Order.** The pool is drawn and SHA-256 hashed before any noise parameter exists; the hash is re-checked after every sweep. Draw \(s\) uses `default_rng([s, 12])`; the canonical draw is \(s=2026\), the ensemble is \(s=1..40\).
6. **Channels.** GAD at \(T=1\) (\(p = 1/(1+e^{-1})\), as CE-9) and pure dephasing with Kraus operators \(\{\sqrt{1-g/2}\,I, \sqrt{g/2}\,Z\}\) on each qubit (\(g=1\) is full dephasing). Grid \(g = 0, 0.1, \dots, 1\).
7. **Informed condition** (for the overlap term only): CE-10's "readable" input \(\psi_{fm} = U_f^\dagger|m\,b_f\rangle\), \(b_f = f \bmod 2\), with \(X = (\text{block message}, b_f)\). Then \(I(X;F) = 1\) bit.

## 2. Traps

- **\(\langle E-E_0\rangle\) depends on the state.** It is taken in \(\rho_{\rm ref}\) only. The individual input kets have other energies, so nothing here is a statement about them.
- **ML at the bound means reaching an orthogonal state, for pure states.** \(\sigma\) is mixed (rank 2), so \(t_{\rm ML}\) is used only as a time scale. The blind inputs are not orthogonalised: the mean fidelity \(|\langle m0|U|m0\rangle|^2\) at \(t_{\rm ML}\) is 0.356.
- **The budget only sets the spectral scale.** \(U = \exp(-iH\pi/(2\langle E-E_0\rangle))\) is invariant under \(H \to cH\), so at \(t = t_{\rm ML}\) the budget cancels. Budgets 0.25, 1 and 4 give the same pool hash, and \(\max|U(B{=}0.25)-U(B{=}4)| = 0\) over 1000 samples. The only meaningful knob is the phase budget \(t/t_{\rm ML}\) (equivalently: fixed time, varying budget).
- **The sampling distribution of \(H\) is a choice.** GUE here. Another ensemble gives another pool; not tested.
- **Clustering uses noiseless statistics only**, so the pool cannot depend on the noise channel. It does depend on the readout basis (Z) and on the blind input. For the Z readout, TV distance between per-use laws can only shrink under GAD or dephasing followed by Z readout (data processing), so cluster members stay \(\varepsilon\)-close at every \(g\). For the random readout there is no such guarantee.
- **Pool size is set by n_samples, not by the physics, at small \(\varepsilon\).** The law space is 6-dimensional; its \(\varepsilon\)-covering number at \(\varepsilon = 0.05\) is far above any sample size used here (table below).
- **Pure dephasing commutes with the Z readout.** The nested-Z surface is flat in \(g\) by construction (max deviation \(7\times10^{-15}\)). Dephasing is therefore shown with the random-basis readout.
- **Normalisation.** \(H(F\mid Y)/H(F) = 1 - I(F;Y)/\log_2|{\rm pool}|\) and \(I(F;Y) \le \log_2 r\), so the normalised share rises with pool size at fixed \(I(F;Y)\). The fair comparison is a Haar pool of the **same size** per draw ("haar-matched"). The 50-unitary CE-9 pool ("haar-50") is reported, but differences against it are largely a size effect.

### Pool size (canonical draw, \(t_{\rm frac}=1\), ref = blind)

| n_samples | eps=0.02 | eps=0.05 | eps=0.1 | eps=0.2 | eps=0.3 |
|---|---|---|---|---|---|
| 200 | 200 | 200 | 190 | 97 | 35 |
| 1000 | 1000 | 996 | 788 | 180 | 52 |
| 5000 | 5000 | 4828 | 2548 | 304 | 70 |

| knob | value | pool size (eps=0.05, n=1000) | pool hash (first 12) |
|---|---|---|---|
| budget | 0.25 | 996 | 6878447d36a0 |
| budget | 1.0 | 996 | 6878447d36a0 |
| budget | 4.0 | 996 | 6878447d36a0 |
| tfrac | 0.1 | 3 | 53a4e6056b05 |
| tfrac | 0.25 | 70 | 94c83ba0023b |
| tfrac | 0.5 | 629 | de21f4f0885c |
| tfrac | 1.0 | 996 | 6878447d36a0 |
| tfrac | 2.0 | 994 | d8190d8d13e9 |
| ref | blind | 996 | 6878447d36a0 |
| ref | mixed | 995 | ad2579440914 |

The phase budget does control the pool: short evolutions stay near the identity and collapse into a few clusters. The surfaces below use only \(t_{\rm frac}=1\); smaller \(t_{\rm frac}\) was **not** swept.

## 3. Canonical ML pool (draw 2026, \(\varepsilon=0.05\), 200 samples)

\(|{\rm pool}| = 200\), \(H(F) = 7.644\) bits. GAD at \(T=1\), nested readout, blind inputs.

Normalised share \(H(F\mid Y)/H(F)\):

| g | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.9941 | 0.9795 | 0.9739 | 0.9602 |
| 0.2 | 0.9963 | 0.9889 | 0.9853 | 0.9782 |
| 0.4 | 0.9979 | 0.9944 | 0.9923 | 0.9889 |
| 0.6 | 0.9990 | 0.9977 | 0.9967 | 0.9954 |
| 0.8 | 0.9997 | 0.9994 | 0.9992 | 0.9989 |
| 1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

\(I(F;Y)\) (bits):

| g | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.045 | 0.157 | 0.199 | 0.305 |
| 0.2 | 0.029 | 0.085 | 0.112 | 0.167 |
| 0.4 | 0.016 | 0.043 | 0.059 | 0.085 |
| 0.6 | 0.008 | 0.018 | 0.025 | 0.035 |
| 0.8 | 0.002 | 0.004 | 0.006 | 0.009 |
| 1.0 | 0.000 | 0.000 | 0.000 | 0.000 |

\(I(X;Y)\) at \(g=0\) is 0.026 / 0.038 / 0.074 / 0.108 bits for \(r = 2/4/8/16\). The full 11-row tables (and \(H(F\mid Y)\) in bits, the random readout and dephasing) are in the script output.

Monotonicity in \(r\) and in \(g\) for the nested Z readout under GAD is **guaranteed** by data processing, as in CE-9; it is not a finding. Dephasing with nested Z is flat by construction. For the random readout (separate Haar basis per rank, GAD or dephasing) monotonicity is not guaranteed; it is observed here.

## 4. Bounds

Canonical pool, holds / grid points:

| channel | readout | blind: corrected | blind: original | blind max \(I(X;F\mid Y)\) | informed: corrected | informed: overlap-corrected | identity residual |
|---|---|---|---|---|---|---|---|
| GAD | nested | 44/44 | 0/44 | 0.479 | 40/44 | 44/44 | \(3.6\times10^{-15}\) |
| GAD | random | 44/44 | 0/44 | 0.429 | 44/44 | 44/44 | \(4.4\times10^{-15}\) |
| dephasing | nested | 44/44 | 0/44 | 0.479 | 11/44 | 44/44 | \(3.6\times10^{-15}\) |
| dephasing | random | 44/44 | 0/44 | 0.429 | 44/44 | 44/44 | \(3.6\times10^{-15}\) |

All 40 draws (1760 points per row): blind corrected and informed overlap-corrected hold everywhere; the original form holds nowhere. The informed corrected bound fails at 160/1760 points (GAD nested) and 1320/1760 points (dephasing nested), and never with the random readout.

- **Blind corrected: theorem** (\(X\perp F\)). **Overlap-corrected: theorem** (identity below).
- **Informed failures are by construction.** The readable input makes the noiseless output \(|m\,b_f\rangle\) a Z basis state. At \(g \approx 0\) (GAD) or at every \(g\) (dephasing, which Z cannot see) a rank-4+ readout reads both \(m\) and \(b_f\), so \(I(X;Y)+I(F;Y)\) exceeds \(H(Y)\) by up to \(I(X;F) = 1\) bit. The failures sit at \(g \in \{0, 0.1\}\), \(r \ge 4\) (GAD) and at all \(g\), \(r \ge 4\) (dephasing).

## 5. The overlap term and the "58"

**Identity (theorem).** From \(I(X,F;Y) = I(X;Y) + I(F;Y\mid X)\) and \(I(F;Y\mid X) = I(F;Y) + I(X;F\mid Y) - I(X;F)\):

\[
I(X;Y) + I(F;Y) = I(X,F;Y) + I(X;F) - I(X;F\mid Y) \;\le\; H(Y) + I(X;F) - I(X;F\mid Y).
\]

With \(X \perp F\), \(I(X;F)=0\) and this reads \(I(X;Y)+I(F;Y)+I(X;F\mid Y) = I(X,F;Y) \le H(Y)\): the overlap term is exactly part of the slack of the corrected bound. With an informed input, \(I(X;F) > 0\) and the corrected bound can fail (§4); the overlap-corrected form always holds. The script checks the identity on random joint laws and at every grid point (residual \(< 5\times10^{-15}\)).

**Source of the "58".** [procedural-share.md §4](procedural-share.md), table row "(a) eps-class | A | uniform | 0.05 | 72 | 14 | 58": CE-6's one-bit GAD toy, variant (a) (\(\varepsilon\)-class of the GAD law), pool A (50 candidates), \(\varepsilon = 0.05\), on the \(21\times11\) \((g,p)\) grid. 72 points have a non-empty class; the original form fails at 58; the corrected bound holds at all 72. The capacity-input row has the same counts. The script recomputes this run exactly:

| input | defined | original fails | corrected holds | \(\max|I(X;F)|\) | \(I(X;F\mid Y)\) at failures (min / median / max) | deficit \(H(F\mid Y)-H(Y\mid X)\) (min / median / max) | failures with \(I(X;F\mid Y) \ge\) deficit |
|---|---|---|---|---|---|---|---|
| uniform | 72 | 58 | 72/72 | \(4\times10^{-16}\) | 0.0000 / 0.0048 / 0.0285 | 0.047 / 1.455 / 3.076 | 0 |
| capacity | 72 | 58 | 72/72 | \(4\times10^{-16}\) | 0.0000 / 0.0048 / 0.0285 | 0.047 / 1.455 / 3.076 | 0 |

(The two rows agree to the printed precision but are not identical: the deficits differ by up to 0.10 bits at individual points.) At the uniform-input failures the corrected-bound slack ranges from 0 to 1 bit; 3 failures have zero slack and hence \(I(X;F\mid Y)=0\). Elsewhere the overlap term is at most 0.31 of the slack.

**Why the original form cannot be rescued (theorem).** \(I(X;Y)+H(F\mid Y) \le H(Y)\) is equivalent to \(H(F\mid Y) \le H(Y\mid X)\). Since \(I(F;Y) \le H(Y)\), \(H(F\mid Y) \ge H(F) - H(Y) = \log_2|C| - H(Y)\), which grows without bound with the class or pool size \(|C|\). Every candidate correction built from the same variables is bounded independently of \(|C|\): \(I(X;F\mid Y) \le H(X)\), \(I(X;F) \le H(X)\), and the remaining terms are at most \(H(X)\) or \(H(Y)\). So for a large enough pool the original form fails whatever term is added. On the ML pools here \(H(F) \approx 7.6\) bits against \(H(Y) \le 4\), and it fails at every point.

## 6. ML pool vs Haar (40 draws, blind inputs)

Per draw: the ML pool (size \(K_s\)), a Haar pool of the same size \(K_s\) (`draw_pool(K_s, 100000+s)`) and the CE-9 Haar-50 pool (`draw_pool(50, s)`), all on the same random readout bases. The per-draw statistic is the mean over the nontrivial points (\(g<1\) for GAD, all \(g\) for dephasing) of the paired difference ML − Haar. Two-sided sign-flip test (20000 flips), bootstrap 95% CI (10000 resamples), Holm across the 12 aggregate tests.

### Default (\(\varepsilon = 0.05\), 200 samples; pool sizes 199–200)

| channel | readout | metric | vs | ML | Haar | diff | 95% CI | p (Holm) | ML > Haar |
|---|---|---|---|---|---|---|---|---|---|
| GAD | nested | \(H(F\mid Y)/H(F)\) | haar-matched | 0.9923 | 0.9919 | +0.0004 | [+0.0002, +0.0006] | 0.0006 | 32/40 |
| GAD | nested | \(H(F\mid Y)/H(F)\) | haar-50 | 0.9923 | 0.9892 | +0.0031 | [+0.0027, +0.0035] | 0.0006 | 39/40 |
| GAD | nested | \(I(F;Y)\) | haar-matched | 0.0586 | 0.0620 | −0.0033 | [−0.0048, −0.0019] | 0.0012 | 8/40 |
| GAD | nested | \(I(F;Y)\) | haar-50 | 0.0586 | 0.0610 | −0.0024 | [−0.0047, +0.0001] | 0.31 | 15/40 |
| GAD | random | \(H(F\mid Y)/H(F)\) | haar-matched | 0.9974 | 0.9974 | +0.0000 | [−0.0000, +0.0000] | 0.84 | 21/40 |
| GAD | random | \(H(F\mid Y)/H(F)\) | haar-50 | 0.9974 | 0.9966 | +0.0009 | [+0.0008, +0.0009] | 0.0006 | 40/40 |
| GAD | random | \(I(F;Y)\) | haar-matched | 0.0196 | 0.0197 | −0.0001 | [−0.0003, +0.0001] | 0.84 | 19/40 |
| GAD | random | \(I(F;Y)\) | haar-50 | 0.0196 | 0.0195 | +0.0002 | [−0.0001, +0.0003] | 0.47 | 26/40 |
| dephasing | random | \(H(F\mid Y)/H(F)\) | haar-matched | 0.9973 | 0.9972 | +0.0001 | [+0.0001, +0.0001] | 0.0007 | 31/40 |
| dephasing | random | \(H(F\mid Y)/H(F)\) | haar-50 | 0.9973 | 0.9963 | +0.0010 | [+0.0009, +0.0011] | 0.0006 | 40/40 |
| dephasing | random | \(I(F;Y)\) | haar-matched | 0.0203 | 0.0210 | −0.0007 | [−0.0010, −0.0004] | 0.0006 | 9/40 |
| dephasing | random | \(I(F;Y)\) | haar-50 | 0.0203 | 0.0206 | −0.0003 | [−0.0007, +0.0001] | 0.47 | 16/40 |

Per point (GAD, nested, ML − haar-matched normalised share; \* / \*\* = Holm-adjusted \(p<0.05/0.01\) across the 40 points with \(g<1\); 26/40 significant):

| g | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.0009\*\* | 0.0012\*\* | 0.0019\*\* | 0.0023\*\* |
| 0.2 | 0.0005\*\* | 0.0004\* | 0.0009\*\* | 0.0008\* |
| 0.4 | 0.0003\*\* | 0.0001 | 0.0004\*\* | 0.0003 |
| 0.6 | 0.0001\*\* | 0.0000 | 0.0002\* | 0.0001 |
| 0.8 | 0.0000\*\* | 0.0000 | 0.0000\* | 0.0000 |

### Coarser clustering (\(\varepsilon = 0.2\), 1000 samples; pool sizes 171–200)

| channel | readout | metric | vs | ML | Haar | diff | 95% CI | p (Holm) | ML > Haar |
|---|---|---|---|---|---|---|---|---|---|
| GAD | nested | \(H(F\mid Y)/H(F)\) | haar-matched | 0.9906 | 0.9918 | −0.0012 | [−0.0014, −0.0010] | 0.0006 | 0/40 |
| GAD | nested | \(I(F;Y)\) | haar-matched | 0.0709 | 0.0621 | +0.0088 | [+0.0074, +0.0104] | 0.0006 | 40/40 |
| GAD | random | \(H(F\mid Y)/H(F)\) | haar-matched | 0.9974 | 0.9974 | +0.0000 | [−0.0000, +0.0000] | 0.66 | 24/40 |
| dephasing | random | \(H(F\mid Y)/H(F)\) | haar-matched | 0.9971 | 0.9972 | −0.0001 | [−0.0001, −0.0001] | 0.0006 | 8/40 |
| dephasing | random | \(I(F;Y)\) | haar-matched | 0.0218 | 0.0211 | +0.0007 | [+0.0005, +0.0009] | 0.0006 | 32/40 |

(Haar-50 rows and the GAD-random \(I(F;Y)\) row are in the script output.) For GAD nested, all 40 per-point differences are negative and significant, from −0.0059 at \(g=0\), \(r=16\) to below \(5\times10^{-5}\) in magnitude at \(g=0.9\).

### Reading

- **Haar-50 differences are mostly a size effect.** The ML pools have about 200 members against 50, and the normalised share rises with pool size (§2). These rows are not evidence for anything.
- **Against the size-matched Haar pool the differences are significant but tiny, and their sign depends on \(\varepsilon\).** At \(\varepsilon = 0.05\) (almost no clustering) the ML pool is slightly *less* identifiable than Haar, by at most 0.0023 of \(H(F)\). At \(\varepsilon = 0.2\) it is slightly *more* identifiable, by up to 0.0059. Coarse leader clustering keeps one member per \(\varepsilon\)-ball, which spreads the output laws apart and raises \(I(F;Y)\). The sign is therefore controlled by the **clustering radius**, not by the energy bound.
- **The energy budget itself does nothing** at \(t = t_{\rm ML}\) (theorem, §2). What remains at \(\varepsilon = 0.05\) is the difference between the GUE-at-ML-time distribution of unitaries and the Haar measure, a property of the chosen ensemble.
- **Random readout:** GAD shows no significant matched difference at either \(\varepsilon\). Dephasing shows a \(10^{-4}\) effect whose sign again flips with \(\varepsilon\).

## 7. Theorem vs empirical

**By construction or theorem:**

- budget invariance at \(t_{\rm ML}\) (dimensional analysis);
- corrected bound with blind inputs;
- the overlap identity and the overlap-corrected bound;
- the impossibility of rescuing the original form;
- monotonicity in \(g\) and \(r\) for GAD with nested Z (CE-9);
- the flat dephasing surface with nested Z;
- the informed corrected-bound failures (readable input);
- the reproduction of CE-6's 72/14/58 counts.

**Empirical (this run, this ensemble, these settings):**

- pool size vs \(\varepsilon\), n_samples and \(t_{\rm frac}\);
- the size of \(I(X;F\mid Y)\) at the 58 failures (≤ 0.029 bits) and on the canonical ML pools (≤ 0.48 bits at \(\varepsilon=0.05\), ≤ 0.57 bits at \(\varepsilon=0.2\), blind);
- the ML-vs-Haar differences and their sign flip with \(\varepsilon\);
- monotonicity under the random readout.

**Untested conjectures, not supported here:**

- that an energy (ML) bound on the candidate set lowers or raises the procedural share in a way that Haar pools do not;
- any dependence on \(t_{\rm frac} < 1\), another Hamiltonian ensemble, or a reference state other than \(\sigma\) and \(I/4\).

## 8. Scope

Tier 2 only. A two-qubit, two-use toy with one choice of Hamiltonian ensemble, clustering rule, encoding, channel family and readout. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this run beyond the information-theoretic bookkeeping above.
