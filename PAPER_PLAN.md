# Paper plan: the corrected accounting bound

**Status:** decision recorded 2026-11-26. **This is a plan, not a paper.** Nothing below is a new result. Every result named here is already derived or computed in this repository, with a pointer. Section 7 is labelled speculative (Tier 3): it is a framing device, not a claim.

**Related:** [README.md](README.md) (three tiers) · [CORE.md](CORE.md) (Tier 1) · [TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md) (Tier 2) · [THEORY.md §C.8](THEORY.md#c8-three-linked-conjectures-ranked-by-testability) (Tier 3 conjectures) · [PLAN.md](PLAN.md) (research reorganisation) · [papers/06-synthesis/PUBLISHING.md](papers/06-synthesis/PUBLISHING.md) (rendering notes).

---

## 1. Decision (2026-11-26)

Publish one paper whose **primary claim** is an information-theoretic result about channels: the **corrected accounting bound**

\[
I(X;Y) + I(F;Y) \le H(Y) \qquad \text{for } X \perp F,
\]

where \(X\) is the message, \(F\) is the unknown channel (procedure) drawn from a candidate pool, and \(Y\) is the readout.

- **It replaced an original form that fails.** The original accounting \(I(X;Y) + H(F\mid Y) \le H(Y)\) (the equality version is stronger, so it fails too) is equivalent to \(H(F\mid Y) \le H(Y\mid X)\). It fails at 58 of 72 defined points in the CE-6 run. No correction term capped by \(H(X)\) or \(H(Y)\) can close the gap (§3).
- **Physics interpretations are excluded from the main text.** The alphabet cascade, the capacity-saturation reading and the radiation signature ([THEORY.md §C.8](THEORY.md#c8-three-linked-conjectures-ranked-by-testability)) may appear **only** in clearly labelled speculative appendices, with the C.8 testability ranking and its *conjecture: not derived, not tested* status.
- The paper is not a step in a Boltzmann–Shannon unification argument. It is a stand-alone channel-level accounting result. Any mention of that motivation stays in the introduction as motivation.

## 2. Sequencing

1. **The bound comes first.** The paper rests only on Tier 1/Tier 2 material and the procedural-share numerics already in the repo.
2. **Channel-cost research continues separately, in parallel.** That covers the thermal channel cost ([docs/thermal-channel-cost.md](docs/thermal-channel-cost.md); commits 088e4ed, 703ac78), the joint encoding bound C_minus_K, and \(d^{\#}\) / Conjecture T2 ([TIER2_INSTRUCTION_PERSISTENCE.md](TIER2_INSTRUCTION_PERSISTENCE.md)). **None of it is a dependency of the paper.** If channel-cost results mature, they belong in a later paper.
3. **The overlap-first resolution sequence is demoted** pending a channel-cost definition (§4).

## 3. Provenance and accurate statement of the results

### 3.1 Commit trail

| Run | Commit | What it established | Doc |
|---|---|---|---|
| CE-6 | 26b3589 | Procedural share \(H(F\mid Y)\) on generalized amplitude damping (GAD), one-bit readout. **The 58/72 failure count first appears here:** variant (a), pool A, \(\varepsilon = 0.05\), 72 defined grid points, the original form fails at 58, and the corrected bound holds at all 72. | [docs/procedural-share.md §4](docs/procedural-share.md) |
| CE-7 | b12882d | Same with a 16-symbol readout (4 channel uses). No saturation of the procedural share. | [docs/procedural-share.md](docs/procedural-share.md) |
| CE-9 | 16b9e98 | Surface over noise × readout rank on a pool fixed before the channel. Rank and noise trends are **guaranteed by data processing**. | [docs/procedural-share-surface.md](docs/procedural-share-surface.md) |
| CE-10 | 681cade | Informed (\(f\)-dependent) inputs. Null result for the structural variants. With \(X\) the full preparation label, the corrected bound is no longer a theorem: the readable control holds at 40/44 (fails at 4/44). | [docs/procedural-share-informed.md](docs/procedural-share-informed.md) |
| CE-11 | 64bae9a | Structured pools (shared eigenbasis, Clifford). Most gaps negative or construction-forced. Readable control again holds at 40/44 (fails at 4/44) on every pool. | [docs/procedural-share-structured.md](docs/procedural-share-structured.md) |
| CE-12 | ff7972f | Energy-bounded (Margolus–Levitin) pool. **Reproduces 72/14/58 exactly.** Adds the overlap-term result (covers **0/58** failures) and the derivation that the original form cannot be rescued. | [docs/procedural-share-mlpool.md §5](docs/procedural-share-mlpool.md) |

### 3.2 The theorem and its scope

- **Identity** (chain rules; checked numerically in CE-12, residual \(< 5\times10^{-15}\)):
  \[
  I(X;Y) + I(F;Y) = I(X,F;Y) + I(X;F) - I(X;F\mid Y).
  \]
- **General bound:** \(I(X;Y) + I(F;Y) \le H(Y) + I(X;F) - I(X;F\mid Y)\), i.e. \(I(X,F;Y) \le H(Y)\).
- **Corrected bound:** when \(X \perp F\), \(I(X;F) = 0\) and \(I(X;F\mid Y) \ge 0\), so \(I(X;Y) + I(F;Y) \le H(Y)\). The **independence hypothesis is essential and must be stated in the paper.**
- **It fails without independence.** With \(f\)-dependent inputs (the readable control of CE-10/11/12, where \(X\) includes a hint correlated with \(F\)) the corrected bound fails:
  - 4/44 points in CE-10 and in CE-11 (GAD, nested readout);
  - in CE-12, 160/1760 points (GAD, nested) and 1320/1760 (pure dephasing, nested) over 40 draws.

  The general bound holds everywhere.
- **Why the original form cannot be rescued:**
  - \(H(F\mid Y) \ge H(F) - H(Y) = \log_2|C| - H(Y)\), which grows with the pool size \(|C|\).
  - Every correction term built from the same variables is capped independently of \(|C|\): \(I(X;F\mid Y) \le H(X)\), \(I(X;F) \le H(X)\), and the other terms are at most \(H(X)\) or \(H(Y)\).
  - Empirically, at the 58 CE-6 failures \(I(X;F) = 0\), and \(I(X;F\mid Y) \le 0.029\) bits against deficits of 0.047–3.076 bits.

### 3.3 Novelty: be conservative

The bound is a **short consequence of standard Shannon inequalities** (chain rule for mutual information, \(I(X,F;Y) \le H(Y)\), non-negativity of conditional mutual information). The paper must **not** present the inequality itself as new. The contribution has to be the framing and application:

- channel-level accounting of a **semantic share** \(I(X;Y)\) vs a **procedural share** (\(I(F;Y)\), \(H(F\mid Y)\)) of one readout;
- the **negative result**: the natural original identity \(I(X;Y) + H(F\mid Y) = H(Y)\) is false, its failure is generic (grows with the pool), and no capped correction term repairs it;
- the link to the exact \(d^{\#}\) chain rule \(d_f^{\#} = d^{\#}_{g\circ f} + R(g\mid f)\) (Tier 2, proved).

The author has no formal credentials in this field. Every statement in the paper must therefore be backed by an in-repo derivation or computation, with a pointer.

## 4. The overlap-first resolution sequence (demoted)

**Where it is written.** The phrase "overlap-first" does not appear anywhere in the repository (searched README, PLAN.md, THEORY.md, PROGRESS_REPORT.md, CORE.md, synthesis/, docs/ on 2026-11-26). It is recorded here for the first time, as:

> the plan to resolve the accounting via the overlap term \(I(X;F\mid Y)\) first, i.e. to repair the original identity by adding an overlap term before anything else.

**Status: demoted, pending a channel-cost definition.**

- CE-12 (ff7972f) found that the overlap term covers **0 of the 58** CE-6 failure points.
- §3.2 shows that no term capped by \(H(X)\) or \(H(Y)\) can close the gap.
- The overlap term is retained only as **part of the slack** of the corrected bound (with \(X\perp F\): \(I(X;Y)+I(F;Y)+I(X;F\mid Y) = I(X,F;Y) \le H(Y)\)), and as the correction in the general bound for \(f\)-dependent inputs.
- Revisit only if a channel-cost definition supplies a term that grows with the pool.

## 5. Open items before drafting

1. **Formal statement and proof write-up** of the bound, covering:
   - hypotheses: finite alphabets, uniform or general prior on \(F\), \(X \perp F\);
   - the identity and the general (dependent-input) form;
   - the impossibility result for the original form, with its exact hypotheses.
2. **Which repo numerics go in.** Most trends in CE-9 to CE-12 were **by construction**:
   - monotonicity in rank and noise is guaranteed by data processing;
   - Haar-invariance forces zero expected gaps;
   - readable-control failures are construction-forced;
   - pure dephasing is invisible to the Z readout;
   - at the Margolus–Levitin time the budget cancels.

   Candidates for inclusion:
   - the CE-6 72/14/58 table and its CE-12 reproduction;
   - the overlap-term numbers at the 58;
   - the dependent-input failure counts.

   Present the by-construction trends as sanity checks, not findings.
3. **Prior-art check** (pre-submission, required):
   - Baez, Fritz & Leinster, *Entropy* 13 (2011) 1945, and Fullwood & Parzygnat, *Entropy* 23 (2021) 1021 (see [CORE.md §4.1](CORE.md), "independent convergence");
   - Cover & Thomas, *Elements of Information Theory* (chain rule; \(I(X,F;Y)\));
   - co-information / interaction information (McGill 1954; Bell 2003; to verify);
   - any existing treatment of "message vs channel identity" information in one output (e.g. channel identification / hypothesis testing literature).

   Record what is already known and narrow the claims to match.
4. **Venue decision**, after the prior-art check. Pick a venue suited to a short, conservative information-theory note.
5. **Appendix list**, all speculative and labelled:
   - (A) the THEORY.md §C.8 conjectures in their testability ranking: radiation signature (most testable, load-bearing), capacity-saturation reading (middle; checkable against existing calculations), alphabet cascade (interpretive);
   - (B) the framing device of §7.

   Each must carry the C.8 status line *conjecture: not derived, not tested*. They must also note that "alphabet" has no physical definition yet and that the toy runs found no saturation.

## 6. Out of scope for the paper

- Channel cost, C_minus_K, thermal toys, Conjecture T2 (parallel research, §2).
- Any gravitational, black-hole, cosmological, hadronic or QCD claim.
- The overlap-first repair (§4).

## 7. Speculative framing device (Tier 3; NOT a claim)

> **Speculative / Tier 3. Motivation only.** This section records a framing device for the introduction or an appendix. It is not derived, not tested, and not a claim of the programme or of the paper. Nothing in §1–§6 depends on it.

Each prior framework drew a boundary and then worked inside it:

- Shannon assumed the **channel**;
- Jaynes assumed the **constraints**;
- Feynman summed over the **paths**, given the endpoints;
- Bekenstein bounded the entropy of a **region**.

The accounting bound is a statement about what a readout can reveal about *both* the message and the procedure that was used, which is one way to ask what drawing such a boundary costs. Cyotee's motivating question extends this: *what did it cost to draw the hard boundary at the Big Bang?* That question is Tier 3. It has no definition in this repository (no physical "alphabet", no cost functional for a cosmological boundary), and the paper must present it, if at all, only as an open motivating question in a labelled speculative section.
