# Channel cost, Stage 3b: the measurement back-action null (Sweep P, Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model** of four qubits.

- It is **not** evidence about hadronic or QCD physics (**NOT QCD**).
- It makes no physical, gravitational or thermodynamic claim. All quantities are entropies or mutual informations in bits.

**Status:** 2026-11-26 · computed. This is the pre-registered run of [design-stage3b-measurement-backaction.md](design-stage3b-measurement-backaction.md), executed once against commit `b050d38` (doc SHA-256 `c69bc625e97e0439…`), with no change to code or rules after results were seen. A code-path pilot (strengths j = 1, 10, 20; pool members 0–9; not a result) preceded the full run and showed no gate, hash, bound or control failure.

**The full Sweep P setup.**

- **Register:** pure meter \(\lvert+\rangle^{\otimes2}\), the primary sweep.
- **Coupling:** \(U_\theta=\exp(-i\theta\sum_i\sigma_{\hat n}\otimes Y)\) with \(\beta=\pi/4\).
- **Strengths:** 20, \(\theta_j=\tfrac{j-1}{19}\cdot\tfrac\pi4\), with measurement strength \(s=\sin2\theta\) from 0 to projective.
- **Priors:** the same K = 20 priors as Stage 3 Sweep P (seed `20261126`).
- **Pool:** CE-15 (200 members, SHA-256 `d11fa3d1ec4594b7…`), applied before the measurement.
- **Cost:** \(\kappa=I(X;C\mid O,F)\).
- **Target:** \(\Delta D(\theta)=D(\theta)-D(0)\), with \(D=I(X;Y)+H(F\mid Y)-H(Y)\).
- **Checks:** the mandatory controls, plus the report-only diagnostics.

No simulation code is added to the repository with this note.

The *compilation reading* tested here is Cyotee's conjecture, not a claim of this repository: the deficit of the original form is tracked by an entropy cost paid in the channel's own register. Stage 3b tests it on a second coupling family, a measurement whose record is kept, after the XY null of [analysis-stage3-compilation-null.md](analysis-stage3-compilation-null.md).

**Verdict.** **Dead** for this architecture.

- **Count.** Under the pre-registered rule (≥ 15 standing hits = hit, 10–14 = ambiguous, ≤ 9 = dead), Sweep P has **0 standing hits of 20** and **0 raw hits** (\(r(\kappa,\Delta D)\ge0.8\)).
- **Sign.** \(r(\kappa,\Delta D)\) is negative at every non-zero strength (−0.999 to −0.983).
- **Sweep M** was **not triggered**, since 0 is outside the 10–14 band.
- **Corrected bound.** \(I(X;Y)+I(F;Y)\le H(Y)\) holds throughout.

This is a documented null, alongside the Stage 3 null and the Stage 2 channel-cost nulls ([channel-cost-stage2.md](channel-cost-stage2.md) §6).

## 1. Result per strength

All values are across the 20 priors at each strength.

- **⚑** marks \(R^2\ge0.95\) for \(\kappa\) on \(H(X\mid Y)\), \(H(X)\), \(H(Y)\) (control 2). A flag acts only on a strength with \(r\ge0.8\), and there are none.
- **"Classical-record r"** is control 3: the register dephased in its pointer basis.
- **"Raw shuffled r"** is \(r(\kappa_{\rm shuf},\Delta D)\). **\(r_{\Delta\rm shuf}\)** correlates \(\kappa_{\rm shuf}(\theta)-\kappa_{\rm shuf}(0)\) with \(\Delta D\), and is the carry statistic.
- **"Partial r"** is \(r(\kappa,\Delta D\mid H(Y),I(X;Y),H(X\mid Y),H(X))\), with df = 15 and critical value 0.412. It is a diagnostic.
- At \(j=1\), \(\kappa\equiv0\) and \(\Delta D\equiv0\), so every correlation is undefined and \(j=1\) counts as a non-hit.

| j | θ/π | s | mean κ | r(κ,ΔD) | R² (flag ≥ 0.95) | classical-record r | raw shuffled r | r_Δshuf | partial r (diag.) | raw hit | standing |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.00000 | 0.000 | 0.0000 | undef. | undef. | undef. | undef. | undef. | undef. | – | – |
| 2 | 0.01316 | 0.083 | 0.0159 | −0.999 | 0.976 ⚑ | −0.998 | −0.892 | −0.123 | −0.981 | – | – |
| 3 | 0.02632 | 0.165 | 0.0524 | −0.999 | 0.976 ⚑ | −0.998 | −0.893 | −0.382 | −0.981 | – | – |
| 4 | 0.03947 | 0.245 | 0.1027 | −0.999 | 0.975 ⚑ | −0.998 | −0.894 | −0.550 | −0.981 | – | – |
| 5 | 0.05263 | 0.325 | 0.1628 | −0.998 | 0.974 ⚑ | −0.998 | −0.896 | −0.657 | −0.982 | – | – |
| 6 | 0.06579 | 0.402 | 0.2297 | −0.998 | 0.973 ⚑ | −0.998 | −0.898 | −0.729 | −0.983 | – | – |
| 7 | 0.07895 | 0.476 | 0.3009 | −0.998 | 0.971 ⚑ | −0.997 | −0.900 | −0.780 | −0.983 | – | – |
| 8 | 0.09211 | 0.547 | 0.3743 | −0.997 | 0.969 ⚑ | −0.997 | −0.902 | −0.818 | −0.984 | – | – |
| 9 | 0.10526 | 0.614 | 0.4481 | −0.997 | 0.967 ⚑ | −0.997 | −0.904 | −0.848 | −0.984 | – | – |
| 10 | 0.11842 | 0.677 | 0.5206 | −0.996 | 0.964 ⚑ | −0.997 | −0.906 | −0.872 | −0.984 | – | – |
| 11 | 0.13158 | 0.736 | 0.5903 | −0.995 | 0.962 ⚑ | −0.996 | −0.908 | −0.891 | −0.984 | – | – |
| 12 | 0.14474 | 0.789 | 0.6559 | −0.994 | 0.959 ⚑ | −0.996 | −0.909 | −0.907 | −0.985 | – | – |
| 13 | 0.15789 | 0.837 | 0.7164 | −0.993 | 0.955 ⚑ | −0.995 | −0.910 | −0.920 | −0.985 | – | – |
| 14 | 0.17105 | 0.879 | 0.7708 | −0.992 | 0.952 ⚑ | −0.995 | −0.910 | −0.929 | −0.986 | – | – |
| 15 | 0.18421 | 0.916 | 0.8182 | −0.991 | 0.949 | −0.994 | −0.910 | −0.936 | −0.986 | – | – |
| 16 | 0.19737 | 0.946 | 0.8580 | −0.990 | 0.946 | −0.993 | −0.910 | −0.942 | −0.986 | – | – |
| 17 | 0.21053 | 0.969 | 0.8895 | −0.988 | 0.943 | −0.992 | −0.909 | −0.945 | −0.986 | – | – |
| 18 | 0.22368 | 0.986 | 0.9124 | −0.987 | 0.941 | −0.991 | −0.907 | −0.947 | −0.983 | – | – |
| 19 | 0.23684 | 0.997 | 0.9263 | −0.985 | 0.942 | −0.989 | −0.905 | −0.948 | −0.975 | – | – |
| 20 | 0.25000 | 1.000 | 0.9310 | −0.983 | 0.949 | −0.988 | −0.901 | −0.949 | −0.955 | – | – |

Over the sweep, \(\kappa\) spans 0.000 to 1.148 bits, \(D\) spans 5.413–5.670 bits (\(\log_2\lvert\text{pool}\rvert=7.644\)), and \(\Delta D\) spans −0.0240 to 0.1393 bits.

## 2. Hit count and label

| count | value |
|---|---|
| raw hits, \(r(\kappa,\Delta D)\ge0.8\) | 0 / 20 |
| flagged hits (raw hit with \(R^2\ge0.95\)) | 0 |
| **standing hits** | **0 / 20** |
| **label** | **dead** (≤ 9) |
| Sweep M | not run (trigger is 10–14 standing hits) |

No strength comes near the threshold. The correlation is strong but has the opposite sign.

## 3. Controls

1. **Discard (sanity check).** With the record traced out and the register reset, \(\max\lvert\kappa\rvert=8.6\times10^{-16}\) at every strength, as built. The output law and \(\Delta D\) are unchanged.
2. **Classical record (control 3).** Keeping only the pointer-basis record lowers the cost a lot: mean classical-record \(\kappa\) is 0.12–0.21 of mean \(\kappa\) across strengths. Its correlation with \(\Delta D\) stays within 0.004 of the coherent one at every non-zero strength. So the record's coherence changes the size of the cost, not its relation to \(\Delta D\).
3. **Orientation shuffle (control 4).** The raw shuffled correlation is −0.910 to −0.892, and \(r_{\Delta\rm shuf}\) is −0.949 to −0.123. At \(\theta=0\), the shuffled cost is already 0.638–1.287 bits from random rotations alone. Registers whose overlaps were destroyed reproduce the sign of the main correlation, and from mid-sweep they reproduce its size too. So the relation is not specific to the measurement.
4. **Sufficiency (control 2).** \(R^2\) of \(\kappa\) on \(H(X\mid Y)\), \(H(X)\), \(H(Y)\) lies in 0.941–0.976, with 13 of 19 non-zero strengths at or above 0.95 (j = 2–14). These flags have no effect on the count, since no strength has \(r\ge0.8\).
5. **Partial correlation (control 1, diagnostic).** −0.986 to −0.955. Since \(\Delta D=-\Delta I(F;Y)-\Delta H(Y\mid X)\), the change in pool identifiability carries 0.954–0.984 of \(\operatorname{Var}\Delta D\) (share \(-\operatorname{Cov}(\Delta D,\Delta I(F;Y))/\operatorname{Var}\Delta D\)).

## 4. What drives the correlation: the priors' entropy

- Across priors, \(\kappa\) tracks \(H(X)\) at \(r\) = 0.947–0.957 at every non-zero strength. This is consistent with the cap \(\kappa\le H(X\mid O,F)\le H(X\mid Y)\) recorded in the design.
- \(\Delta D\) tracks \(H(X)\) at −0.940 to −0.906, and \(H(X\mid Y)\) at −0.935 to −0.906.
- Priors with higher entropy carry a larger cost and a smaller interaction-induced deficit change. That is consistent with the negative correlation arising from the sample unit rather than from any property of the measurement. The iso-entropy diagnostic (§8) shows that \(H(X)\) is not its only carrier.
- *Post hoc, not a finding.* The negative sign was not predicted and is not offered as a result. One untested possibility is an information–disturbance tradeoff: the more input information the record takes, the more the induced disturbance degrades what the output reveals about the pool. Nothing here tests it.

## 5. Why the target is ΔD and not D (warning)

Plain \(D\) would have produced **19 of 19 false hits**.

- \(r(\kappa,D)\) is 0.983–0.991 at every non-zero strength.
- That is entirely the coupling-independent part. \(r(\kappa,D(0))\) is 0.987–0.991, and \(r(D(\theta),D(0))\ge0.998\).
- \(D(0)\) is fixed by the prior and the pool, and the measurement never touches it.

That is why \(\Delta D\) was pre-registered ([design-stage3b-measurement-backaction.md](design-stage3b-measurement-backaction.md) §6, risk 6). With \(D\) as the target, this run would have read as a hit.

## 6. Pairing with Stage 3 Sweep P

Both runs use the same 20 priors and the same pool. Their \(\theta=0\) output laws coincide, so \(D(0)\) is identical across the stages (max difference \(3.6\times10^{-15}\)).

- **Cost ordering.** Across priors, the 3b cost orders the priors almost exactly as the XY cost did: \(r(\kappa_{3},\kappa_{3b})\) = 0.980–0.999 over j = 2–20.
- **Deficit-change ordering.** It agrees less closely, at 0.784–0.824.
- **Sign.** Both architectures give a negative \(r(\kappa,\Delta D)\): −0.910 to −0.791 in Stage 3, computed post hoc from its outputs, and −0.999 to −0.983 here.

| j | r(κ₃, κ₃b) | r(ΔD₃, ΔD₃b) | Stage 3 r(κ,ΔD) | Stage 3b r(κ,ΔD) | mean κ₃ | mean κ₃b |
|---|---|---|---|---|---|---|
| 2 | 0.980 | 0.824 | −0.910 | −0.999 | 0.015 | 0.016 |
| 6 | 0.990 | 0.812 | −0.873 | −0.998 | 0.202 | 0.230 |
| 11 | 0.996 | 0.790 | −0.825 | −0.995 | 0.529 | 0.590 |
| 15 | 0.998 | 0.784 | −0.798 | −0.991 | 0.786 | 0.818 |
| 20 | 0.999 | 0.805 | −0.795 | −0.983 | 1.062 | 0.931 |

Two different channel families give nearly the same ranking of priors by cost. That is consistent with the cost being set mainly by the priors rather than by the coupling.

## 7. Corrected bound and independence

\(I(X;Y)+I(F;Y)\le H(Y)\) holds at all 400 (strength, prior) points, with a minimum margin of 1.677 bits. \(\max\lvert I(X;F)\rvert=3.6\times10^{-15}\), so \(X\perp F\) holds to rounding, as built.

## 8. Report-only diagnostics (not binding)

| diagnostic | range over j = 2–20 |
|---|---|
| T-a: \(r(\kappa,\Delta D)\) on the iso-entropy priors (\(H(X)=2.000\) bits, seed `2026112633`) | −0.993 to −0.959 |
| T-b: \(r(\kappa,\Delta D\mid H(X))\) (df 17, critical 0.389) | −0.991 to −0.946 |
| T-c: single-member \(R^2\), no pool unitary | 0.940–0.962 |
| T-c: single-member \(R^2\), pool member 0 | 0.888–0.973 |
| B-1: \(r(\kappa,D)\) / \(r(\kappa,D(0))\) / \(r(D(\theta),D(0))\) | 0.983–0.991 / 0.987–0.991 / 0.998–1.000 |

With \(H(X)\) fixed, the negative correlation persists (T-a). So the priors' entropy is not its only carrier, and \(H(X\mid Y)\) and related terms still vary across that set. None of these values enters the rule.

## Conclusion

The pre-registered test of the compilation reading on the four-qubit measurement-record toy is dead: 0 standing hits of 20, and 0 raw hits.

- The cost is strongly and negatively correlated with the interaction-induced deficit change.
- That correlation is reproduced by registers whose overlaps were shuffled away and by the classical record alone, and it is consistent with both quantities being driven by the priors.
- With the Stage 3 XY null, the compilation-cost reading is **not supported for either the XY coupling or the measurement-record coupling in this four-qubit template**. Nothing here bears on other templates, register sizes or channel families.
- \(H(X\mid Y)\)-type terms are prior art (Baez–Fritz–Leinster, Fullwood–Parzygnat); this note adds nothing to them.
- \(k=\lvert\text{pool}\rvert\) is constant and used only as a proxy.

## Reproduction

- **Spec:** [design-stage3b-measurement-backaction.md](design-stage3b-measurement-backaction.md), commit `b050d38` (doc SHA-256 `c69bc625e97e0439…`).
- **Code (scratch, not in the repository):**
  - `stage3b_sim/channel_cost_stage3b.py` (SHA-256 `8b9e5847d4088e23…`);
  - the Stage 3 library, vendored unchanged (`0309202529df4633…`);
  - `stage3b_sim/run_full.py` (`82b53d55bc8e7657…`), which aborts unless the spec doc and pool hashes match.
  - NumPy 2.5.5.
- **Locked settings:** \(\beta=\pi/4\); prior seed `20261126`; pool seed 2026, SHA-256 `d11fa3d1ec4594b7…`; shuffle seed `2026112632`; iso-entropy seed `2026112633`; \(R^2\) tolerance 0.95; critical r 0.412.
- **Raw outputs are not committed.**
  - The per-prior matrices and full per-strength records are kept locally in `/workspace/ce-stage3b-sim/outputs/full/` (`full_results.json`, `full_per_prior.csv`, `full_table.md`, `full.log`). The pilot is in `/workspace/ce-stage3b-sim/outputs/pilot/`.
  - The tables here are generated from those files by script. The Stage 3 pairing columns come from the Stage 3 outputs listed in its null note.

## Scope

Tier 2 only: a four-qubit toy with one measurement coupling, one readout and five input states under 20 priors. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this result beyond the information-theoretic bookkeeping above.
