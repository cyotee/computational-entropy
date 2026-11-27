# Channel cost, Stage 3: the compilation-cost null (Sweep P, Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model** of four qubits.

- It is **not** evidence about hadronic or QCD physics (**NOT QCD**).
- It makes no physical, gravitational or thermodynamic claim. All quantities are entropies or mutual informations in bits.

**Status:** 2026-11-26 · computed. This is the pre-registered run of [design-stage3-compilation-cost.md](design-stage3-compilation-cost.md) (FS-2), as amended by Amendment 1 (commit `0e2ff6c3`), executed once against that commit with no change to code or rules after results were seen. Sweep P (pure \(\lvert00\rangle\) register) is primary: 20 strengths \(\theta_j=\tfrac{j-1}{19}\cdot\tfrac\pi8\) (\(t_\ast=1\), so \(J=\theta\)), the K = 20 priors (seed `20261126`, Bell weight \(\ge0.10\)), the CE-15 pool (200 members, seed 2026, SHA-256 `d11fa3d1ec4594b7…`), cost \(\kappa=I(X;C\mid O,F)\), deficit \(D=I(X;Y)+H(F\mid Y)-H(Y)\), and the four mandatory controls. No simulation code is added to the repository with this note.

The *compilation reading* tested here is Cyotee's conjecture, not a claim of this repository: the deficit of the original form is tracked by an entropy cost paid in the channel's own register.

**Verdict.** **Dead** for this architecture. Under the pre-registered rule (≥ 15 standing hits = hit, 10–14 = ambiguous, ≤ 9 = dead), Sweep P has **1 standing hit of 20** (j = 2, where the cost-level shuffle correlation \(r_{\Delta\rm shuf}=0.382<0.412\)). Raw hits (\(r(\kappa,D)\ge0.8\)) number 10 of 20 (j = 2–11), all at the weak-coupling end, and every one of them is flagged as potentially definitional by the sufficiency check. Nine of the 10 flagged hits fail the shuffle carry rule of Amendment 1. Sweep M was **not triggered**, since 1 is outside the 10–14 band. The correlations that do appear are carried by the priors' entropy, not by anything specific to the interaction. This is a documented null, alongside the Stage 2 channel-cost nulls ([channel-cost-stage2.md](channel-cost-stage2.md) §6). The corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) holds throughout.

## 1. Result per strength

All values are across the 20 priors at each strength. ⚑ marks \(R^2\ge0.95\) (control 2, potentially definitional). "Partial r" is \(r(\kappa,D\mid H(Y),I(X;Y),H(X\mid Y),H(X))\), whose controls have rank 3 (df = 15, critical 0.412); it is reported as a diagnostic and does not enter the rule. \(\Delta\kappa_{\rm shuf}=\kappa_{\rm shuf}(J)-\kappa_{\rm shuf}(0)\) per prior; the table gives its mean over priors, and \(r_{\Delta\rm shuf}\) is its correlation with \(D\) (the carry statistic). "Raw hit" is \(r\ge0.8\); "standing" applies the carry rule to flagged hits. At \(J=0\), \(\kappa=0\) for every prior, so \(r\) is undefined and counts as a non-hit.

| j | θ/π | mean κ | r(κ,D) | R² (flag ≥ 0.95) | partial r (diag.) | dephased r | raw r_shuf | r_Δshuf | mean Δκ_shuf | raw hit | standing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.00000 | 0.0000 | undef. | undef. | undef. | undef. | 0.862 | undef. | 0.0000 | – | – |
| 2 | 0.00658 | 0.0145 | 0.975 | 0.965 ⚑ | 0.397 | 0.977 | 0.862 | 0.382 | 0.0011 | yes | **yes** |
| 3 | 0.01316 | 0.0471 | 0.976 | 0.972 ⚑ | 0.562 | 0.976 | 0.862 | 0.716 | 0.0044 | yes | – |
| 4 | 0.01974 | 0.0912 | 0.975 | 0.979 ⚑ | 0.788 | 0.975 | 0.862 | 0.858 | 0.0098 | yes | – |
| 5 | 0.02632 | 0.1436 | 0.972 | 0.981 ⚑ | 0.924 | 0.972 | 0.861 | 0.914 | 0.0170 | yes | – |
| 6 | 0.03289 | 0.2018 | 0.966 | 0.981 ⚑ | 0.952 | 0.966 | 0.858 | 0.939 | 0.0255 | yes | – |
| 7 | 0.03947 | 0.2640 | 0.957 | 0.980 ⚑ | 0.945 | 0.958 | 0.853 | 0.949 | 0.0351 | yes | – |
| 8 | 0.04605 | 0.3289 | 0.942 | 0.978 ⚑ | 0.935 | 0.944 | 0.843 | 0.949 | 0.0454 | yes | – |
| 9 | 0.05263 | 0.3952 | 0.921 | 0.977 ⚑ | 0.927 | 0.924 | 0.827 | 0.941 | 0.0562 | yes | – |
| 10 | 0.05921 | 0.4622 | 0.891 | 0.975 ⚑ | 0.921 | 0.895 | 0.801 | 0.922 | 0.0673 | yes | – |
| 11 | 0.06579 | 0.5291 | 0.849 | 0.974 ⚑ | 0.917 | 0.855 | 0.765 | 0.891 | 0.0783 | yes | – |
| 12 | 0.07237 | 0.5954 | 0.795 | 0.972 ⚑ | 0.915 | 0.802 | 0.718 | 0.848 | 0.0893 | – | – |
| 13 | 0.07895 | 0.6605 | 0.730 | 0.970 ⚑ | 0.913 | 0.739 | 0.659 | 0.791 | 0.1000 | – | – |
| 14 | 0.08553 | 0.7241 | 0.657 | 0.969 ⚑ | 0.911 | 0.666 | 0.591 | 0.724 | 0.1103 | – | – |
| 15 | 0.09211 | 0.7860 | 0.579 | 0.967 ⚑ | 0.909 | 0.589 | 0.518 | 0.650 | 0.1202 | – | – |
| 16 | 0.09868 | 0.8458 | 0.501 | 0.965 ⚑ | 0.906 | 0.512 | 0.444 | 0.575 | 0.1297 | – | – |
| 17 | 0.10526 | 0.9034 | 0.426 | 0.963 ⚑ | 0.904 | 0.438 | 0.373 | 0.501 | 0.1386 | – | – |
| 18 | 0.11184 | 0.9586 | 0.358 | 0.962 ⚑ | 0.901 | 0.370 | 0.308 | 0.431 | 0.1470 | – | – |
| 19 | 0.11842 | 1.0114 | 0.297 | 0.960 ⚑ | 0.898 | 0.310 | 0.249 | 0.368 | 0.1549 | – | – |
| 20 | 0.12500 | 1.0617 | 0.244 | 0.959 ⚑ | 0.895 | 0.257 | 0.197 | 0.311 | 0.1623 | – | – |

\(\kappa\) spans 0 to 1.316 bits over the sweep; \(D\) spans 5.413–6.076 bits (with \(\log_2\lvert\text{pool}\rvert=7.644\)).

## 2. Hit count and label

| count | value |
|---|---|
| raw hits, \(r\ge0.8\) | 10 / 20 (j = 2–11) |
| flagged (\(R^2\ge0.95\)) among raw hits | 10 |
| flagged hits that stand (\(r_{\Delta\rm shuf}<0.412\)) | 1 (j = 2) |
| **standing hits** | **1 / 20** |
| **label** | **dead** (≤ 9) |
| Sweep M | not run (trigger is 10–14 standing hits) |

Without the carry rule, the raw count of 10 would have fallen in the ambiguous band. The pre-registered rule counts standing hits, so the label is dead.

## 3. The raw correlation trajectory

\(r(\kappa,D)\) is 0.975 at the first non-zero strength (j = 2), peaks at 0.976 at j = 3, then falls monotonically to 0.24 at \(\theta=\pi/8\). It crosses below 0.8 between j = 11 and j = 12. A cost signal that strengthened with the interaction would have shown the opposite trend.

## 4. Controls

1. **Sufficiency (control 2).** Every non-zero strength is flagged: \(R^2\) of \(\kappa\) on \(H(X\mid Y)\), \(H(X)\), \(H(Y)\) (with intercept) lies in 0.959–0.981. The classical output law predicts the cost at the locked tolerance everywhere.
2. **Dephased classical-copy register (control 3).** The dephased correlation is within 0.013 of \(r\) at every non-zero strength. The correlation is not carried by coherence in the register; it is present at the Shannon level.
3. **Orientation shuffle (control 4).** The raw shuffled correlation is already 0.862 at \(J=0\), from random rotations alone. After removing that baseline at the cost level, \(r_{\Delta\rm shuf}\) is within 0.074 of \(r\) from j = 5 on. The part of the shuffled cost added by the interaction tracks \(D\) about as well as \(\kappa\) does, although the shuffle destroys the register overlaps the interaction created. So the correlation is not specific to the interaction. Only at j = 2, where \(\kappa\) is at most 0.018 bits, does \(r_{\Delta\rm shuf}\) fall below 0.412.
4. **Variance decomposition and partial correlation (control 1).** See §5.

## 5. What drives the correlation: the priors' entropy

- Across priors, \(\kappa\) tracks \(H(X)\) at \(r\) = 0.93–0.96 and \(H(X\mid Y)\) at 0.92–0.95 over all non-zero strengths. This is consistent with the cap \(\kappa\le H(X\mid O,F)\le H(X\mid Y)\) recorded in the design (§3, §6.5).
- \(D\) tracks \(H(X)\) at \(r\) = 0.92 at j = 2, falling to 0.23 at j = 20 (\(H(X\mid Y)\): 0.91 to 0.23).
- \(D=\log_2\lvert\text{pool}\rvert-I(F;Y)-H(Y\mid X)\). Its two subtracted terms split \(\operatorname{Var}D\) exactly (shares \(-\operatorname{Cov}(D,T)/\operatorname{Var}D\) sum to 1). \(I(F;Y)\) carries 0.977–0.983 of it at j = 2–6. At \(\theta=\pi/8\), \(I(F;Y)\) carries 0.079 and \(H(Y\mid X)\) carries 0.921; there \(\operatorname{Cov}(D,H(Y))/\operatorname{Var}D=-0.912\).
- So the raw hits sit where both \(\kappa\) and \(D\) are driven by the prior's entropy, and \(r\) collapses as \(D\)'s variance moves from \(I(F;Y)\) to \(H(Y\mid X)\).
- *Diagnostic only.* The partial correlation given the three independent classical controls is 0.90–0.95 from j = 5 on (range over all non-zero strengths 0.40–0.95). With those controls fixed, \(D\)'s residual is \(-I(F;Y)\)'s residual, so this compares \(\kappa\) with pool-identifiability residuals. It does not enter the pre-registered rule and does not change the label. It is not offered as a finding.

**Post-hoc observation (not pre-registered; does not change the verdict).** Across the 20 priors, the cost tracks the zero-coupling deficit \(D(0)\), not the change the coupling makes to it. \(r(\kappa,D(0))\) is 0.976–0.989 at every non-zero strength, while \(r(\kappa,D-D(0))\) is negative at every non-zero strength (−0.791 to −0.910). The raw hits (j = 2–11) sit where \(D(\theta)\) still tracks \(D(0)\): \(r(D(\theta),D(0))\) is 0.895–1.000 there, and falls from 0.842 at j = 12 to 0.266 at j = 20. So the raw correlation with \(D\) is consistent with \(\kappa\) following the coupling-independent part of \(D\), not the deficit change the interaction produces. This is a diagnostic on the existing Sweep P outputs, generated by script from the local files listed under Reproduction. The Stage 3b design ([design-stage3b-measurement-backaction.md](design-stage3b-measurement-backaction.md)) pre-registers \(\Delta D=D(\theta)-D(0)\) as its target for this reason.

## 6. Corrected bound and independence

\(I(X;Y)+I(F;Y)\le H(Y)\) holds at all 400 (strength, prior) points, with a minimum margin of 1.429 bits. \(\max\lvert I(X;F)\rvert=3.6\times10^{-15}\), so \(X\perp F\) holds to rounding, as built.

## Conclusion

The pre-registered test of the compilation reading on the four-qubit XY toy is dead: 1 standing hit of 20. The strong weak-coupling correlations are all flagged as potentially definitional, change by at most 0.013 under dephasing, and, from j = 3 on, are reproduced well enough by the shuffle control that the carry rule fails. They are consistent with the shared dependence of \(\kappa\) and \(D\) on the priors' entropy, which is the export-bookkeeping risk recorded in the design (§6.5). \(H(X\mid Y)\)-type terms are prior art (Baez–Fritz–Leinster, Fullwood–Parzygnat); this note adds nothing to them. \(k=\lvert\text{pool}\rvert\) is constant and used only as a proxy.

## Reproduction

- **Spec:** [design-stage3-compilation-cost.md](design-stage3-compilation-cost.md) with Amendment 1, commit `0e2ff6c3` (doc SHA-256 `6478b1cf335d6f82…`).
- **Code (scratch, not in the repository):** `stage3_sim/channel_cost_stage3.py` (SHA-256 `0309202529df4633…`) and `stage3_sim/run_full.py` (`45622a1b8a558451…`). They import `procedural_share`, `procedural_share_surface` and `procedural_share_mlpool` (`load_pool`) unmodified. The full-run script aborts unless the spec doc and pool hashes match. NumPy 2.5.5 (2.x per `requirements.txt`).
- **Locked settings:** prior seed `20261126`; pool seed 2026, SHA-256 `d11fa3d1ec4594b7…`; shuffle seed `202611264`; dephasing in the register computational basis; \(R^2\) tolerance 0.95; critical r 0.412.
- **Raw outputs are not committed.** The per-prior matrices and full per-strength records are kept locally in `/workspace/ce-stage3-sim/outputs/full/` (`full_results.json`, `full_per_prior.csv`, `full_table.md`, `full.log`), produced by `stage3_sim/run_full.py` with the pre-registered seeds and pool. The table in §1 is generated from those files by script.

## Scope

Tier 2 only. A four-qubit toy with one coupling, one readout and five input states under 20 priors. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this result beyond the bookkeeping above.
