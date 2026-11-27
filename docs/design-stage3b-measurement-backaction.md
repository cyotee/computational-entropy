# Channel cost, Stage 3b: measurement back-action design (pre-registered, Tier 2 toy)

**Tier:** 2 of 3. This note belongs to the channel-level channel-cost line of research, after [channel-cost-stage2.md](channel-cost-stage2.md), the Stage 3 design [design-stage3-compilation-cost.md](design-stage3-compilation-cost.md) (FS-2 with Amendment 1) and the Stage 3 null [analysis-stage3-compilation-null.md](analysis-stage3-compilation-null.md). It is a **toy model** of four qubits.

- It is **not** evidence about hadronic or QCD physics (**NOT QCD**).
- It makes no gravitational, quantum-gravity or thermodynamic claim. A "cost" here is an entropy in bits. Pricing it at \(k_BT\ln2\) would be a convention only.
- The von Neumann entropies below are standard entropies of a toy register's reduced density matrices, used exactly as in Stage 3. No claim about any quantum layer of the programme is made.

**Status:** 2026-11-26 · **design only, pre-registered, nothing run.** No simulation code for this stage is committed, and no sweep or pilot has been run. Cyotee fixed every parameter in §2 and §7 on 2026-11-26, before any result exists. **The kill criterion (§4) is binding.** Numbers labelled *spot check* come from a scratch exact-linear-algebra check (16×16 matrices, five strengths, no sweep, not committed). No correlation between the cost and the deficit, or its change, was computed for this design, so the test has not been previewed (§9).

**What is being tested, and its label.** The *compilation reading* is Cyotee's conjecture: the deficit of the original form is tracked by an entropy cost paid in the channel's own register, namely input information moved into the register that the output does not carry. Stage 3 tested it with an XY exchange coupling. Sweep P was dead, with 1 standing hit of 20 ([analysis-stage3-compilation-null.md](analysis-stage3-compilation-null.md)). Before the reading is retired, Stage 3b tests it with a second mechanism: a register that **measures** the input qubits, weakly or projectively, and **keeps the measurement record**. It is a **conjecture under test, not a claim**. Nothing in this file is a result.

**Naming.** "Stage 3b" means a second architecture for Stage 3 of the channel-cost line. It is unrelated to the "Stage 3" of the three-stage workflow in [PROGRESS_REPORT.md](https://github.com/cyotee/computational-entropy/blob/master/PROGRESS_REPORT.md).

**Decisions recorded (2026-11-26, Cyotee).** These were made before any run, after a draft that flagged ten open parameters.

1. **Cost:** \(\kappa=I(X;C\mid O,F)\), Stage 3's adopted cost. The literal \(S(C)-2I(C;O)\) reading is not used (§3).
2. **Target:** the interaction-induced deficit change \(\Delta D(\theta)=D(\theta)-D(0)\). Plain \(D\) is not a valid target (§4, §6 risk 6).
3. **Priors:** Stage 3's seed `20261126` is reused, with the same \(K=20\) priors as Sweep P, so the run pairs directly with Sweep P.
4. **Diagnostics:** report-only, not binding on the hit rule (§4).
5. **Proposed defaults locked:**
   - coherent record as primary;
   - \(\beta=\pi/4\);
   - the \(\theta\) grid on \([0,\pi/4]\) at the total-energy ML bound;
   - the CE-15 pool applied before the measurement;
   - Sweep M as a noisy meter at \(p=0.7311\);
   - shuffle seed `2026112632`;
   - iso-entropy seed `2026112633`.

**Context carried over from Stage 3 (unchanged).**

- **The bound and the deficit.** The original form \(I(X;Y)+H(F\mid Y)\le H(Y)\) fails in the toys. The corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) is a theorem when \(X\perp F\). The deficit is \(D=I(X;Y)+H(F\mid Y)-H(Y)\). With \(F\) uniform on the pool, \(D=\log_2\lvert\text{pool}\rvert-I(F;Y)-H(Y\mid X)\).
- **What killed Sweep P.** Across priors, the cost tracked the priors' entropy, and every raw hit was flagged by the sufficiency check. A post-hoc look at the Sweep P outputs adds that the cost tracked the zero-coupling deficit \(D(0)\) at every strength ([analysis-stage3-compilation-null.md](analysis-stage3-compilation-null.md)). That is why the target here is \(\Delta D\).
- **Prior art.** \(H(X\mid Y)\)-type terms are prior art (Baez–Fritz–Leinster, Fullwood–Parzygnat). The overlap with this programme is independent convergence.
- **k is a proxy.** The candidate-set size \(k\) is used only as a computable proxy. No description-length or Kolmogorov-complexity claim is made.
- \(I(X;Y)\) is the input–output mutual information.

## 1. Architecture

**Qubits.** As in Stage 3:

- two input qubits \(A_1,A_2\), which are also the qubits read out at the end;
- two record qubits \(C_1,C_2\), where \(C_i\) records the measurement of \(A_i\);
- a product start between inputs and register, \(\rho_A\otimes\rho_{C,0}\).

**Mechanism: a two-outcome measurement of \(\sigma_{\hat n}\) on each input, with the record kept.**

- **Observable.** The measured observable is \(\sigma_{\hat n}=\sin\beta\,X+\cos\beta\,Z\), with \(\beta=\pi/4\) (**LOCKED**) and the same axis for both qubits.
- **Kraus pair.** With projectors \(P_\pm\) onto its eigenvectors and strength \(s\in[0,1]\), the symmetric Kraus pair on each \(A_i\) is
\[
M_0=\sqrt{\tfrac{1+s}{2}}\,P_++\sqrt{\tfrac{1-s}{2}}\,P_-,\qquad M_1=\sqrt{\tfrac{1-s}{2}}\,P_++\sqrt{\tfrac{1+s}{2}}\,P_- .
\]
- \(s=0\): \(M_0=M_1=I/\sqrt2\), so the register measures nothing.
- \(s=1\): a projective measurement of \(\sigma_{\hat n}\).

**Keeping the record (dilation, coherent record primary, LOCKED).** The record is kept as the register's state. Start each \(C_i\) in \(\lvert+\rangle\) and apply
\[
U_\theta=\exp\!\Big(-i\theta\sum_{i=1,2}(\sigma_{\hat n})_{A_i}\otimes Y_{C_i}\Big),\qquad \theta\in[0,\pi/4].
\]
On each pair, \(U_\theta\lvert\psi\rangle\lvert+\rangle=P_+\lvert\psi\rangle\lvert r_+\rangle+P_-\lvert\psi\rangle\lvert r_-\rangle\), with \(\lvert r_\pm\rangle=e^{\mp i\theta Y}\lvert+\rangle\) and \(\langle r_+\vert r_-\rangle=\cos2\theta\).

- Read in the register's computational basis, the record gives exactly the symmetric pair above with \(s=\sin2\theta\). *Spot check:* the POVM elements agree to \(3\times10^{-16}\) at \(\theta=0.1,\pi/8,\pi/4\).
- So the register's computational basis is the **pointer basis** of the record. Stage 3's locked control-3 convention (dephase in the register's computational basis) therefore means "keep only the classical record", with no change (§4).
- \(\theta=\pi/4\) is the projective point (\(s=1\), orthogonal records).

**Induced channel on the inputs.** Tracing the record gives
\[
\mathcal N_\theta(\rho)=\cos^2\theta\,\rho+\sin^2\theta\,\sigma_{\hat n}\rho\,\sigma_{\hat n}
\]
on each qubit. This is dephasing in the \(\hat n\) basis with coherence factor \(\cos2\theta\), a **unital** channel. Stage 3's XY coupling induced generalized amplitude damping, which is non-unital. In the readout basis, \(\langle Z\rangle\mapsto\cos2\theta\,\langle Z\rangle+(1-\cos2\theta)\cos\beta\,\langle\sigma_{\hat n}\rangle\).

**Readout.** As in Stage 3: measure \(A_1A_2\) in the computational basis with full resolution (four outcomes, rank-1 projectors), giving \(O\). That is rank 4 in the repository's readout convention ([procedural-share-surface.md](procedural-share-surface.md) §2). For each input, outcome and pool member, log \(\rho_{C\mid x,o,f}\) and \(P(o\mid x,f)\).

## 2. Parameters

| Parameter | Value | Status |
|---|---|---|
| Input states | Five: \(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle,\lvert\Phi^+\rangle\) | locked (Stage 3) |
| Input priors | \(K=20\); \(\pi_k=0.9\,d_k+0.1\,e_{\Phi^+}\), \(d_k\sim\mathrm{Dirichlet}(\mathbf 1)\), `default_rng(20261126)`, one call, `size=20`. These are the same 20 priors as Stage 3 Sweep P: Bell weight 0.108–0.636, \(H(X)\) = 1.001–2.295 bits | **LOCKED** (2026-11-26) |
| Mechanism | Two-outcome measurement of \(\sigma_{\hat n}\) per input qubit, record kept coherently (§1) | **LOCKED** |
| Measurement axis | \(\hat n=(\sin\beta,0,\cos\beta)\), \(\beta=\pi/4\), same for both qubits | **LOCKED** |
| Strength sweep | \(\theta_j=\tfrac{j-1}{19}\cdot\tfrac{\pi}{4}\), \(j=1,\dots,20\); \(s_j=\sin2\theta_j\) from 0 (measures nothing) to 1 (projective) | **LOCKED** |
| Resource normalization | Fixed dilation time \(t_\ast=1\) (\(\hbar=1\)), coupling \(g\) in units of \(1/t_\ast\), \(g_{\max}=\pi/4\): the total-energy Margolus–Levitin bound of \(\sigma\) (§6, risk 5) | **LOCKED** |
| Readout | Full resolution on \(A_1A_2\) (four outcomes, rank 4) | locked (Stage 3) |
| Candidate pool \(F\) | CE-15 ML pool, 200 two-qubit unitaries on \(A_1A_2\), seed 2026, SHA-256 `d11fa3d1ec4594b7d1235759fde33b8b98689646b44efd163fffba97084618e2`, applied **before** the measurement | **LOCKED** |
| Register start | Sweep P: \(\lvert+\rangle^{\otimes2}\) (pure). Sweep M: \(\big(0.7311\lvert+\rangle\langle+\rvert+0.2689\lvert-\rangle\langle-\rvert\big)^{\otimes2}\) (noisy meter) | **LOCKED** |
| Cost | \(\kappa=I(X;C\mid O,F)\) (§3) | **LOCKED** |
| Target | \(\Delta D(\theta_j)=D(\theta_j)-D(0)\), per prior (§4) | **LOCKED** |
| Kill criterion | Hit iff \(r(\kappa,\Delta D)\ge0.8\) at \(\ge15\) of 20 strengths across the 20 priors; 10–14 ambiguous; \(\le9\) dead; \(R^2\ge0.95\) flag; partial-\(r\) critical value 0.412; cost-level shuffle carry rule | **LOCKED** |

## 3. Cost and its mapping to the stated readout

**Definition (unchanged from Stage 3 §3).**
\[
\kappa:=I(X;C\mid O,F)=\frac{1}{\lvert\text{pool}\rvert}\sum_f\Big[S(C\mid O,F{=}f)-S(C\mid X,O,F{=}f)\Big],
\]
on the classical–quantum state \(\sum_{x,o}\pi(x)P(o\mid x,f)\,\lvert x\rangle\langle x\rvert\otimes\lvert o\rangle\langle o\rvert\otimes\rho_{C\mid x,o,f}\).

**Mapping to the stated readout (decision 1).** The cost candidate was stated as "S of the channel given the output minus I of the channel and the output".

- Stage 3 locked the formula \(S(C)-I(C;O)\). Because \(O\) is classical, \(S(C)-I(C;O)=S(C\mid O)\).
- Read literally, "\(S(C\mid O)-I(C;O)\)" would be \(S(C)-2I(C;O)\). That subtracts the mutual information twice and can be negative.
- **The literal \(S(C)-2I(C;O)\) reading is not used.** The cost is \(\kappa\) as defined above.

**Equality with the locked formula for the pure meter start.**

- The inputs are pure, the Sweep P register start \(\lvert+\rangle^{\otimes2}\) is pure, \(U_\theta\) is unitary and the readout is rank 1.
- So every \(\rho_{C\mid x,o,f}\) is pure and \(S(C\mid X,O,F)=0\), which gives
\[
\kappa=S(C\mid O,F)=\frac{1}{\lvert\text{pool}\rvert}\sum_f\big[S(C)-I(C;O)\big]_{F=f}.
\]
That is the locked formula given \(F\), averaged over the pool.
- The noisy-meter start of Sweep M is mixed. There \(\kappa\) subtracts the leftover disorder \(S(C\mid X,O,F)\), as in Stage 3's Sweep M.

**Properties.**

- **Zero at \(\theta=0\) by construction.** The record is \(\lvert+\rangle^{\otimes2}\) in every branch.
- **Zero per input.** For a single pure input, \(\kappa=0\). The ensemble is what makes it non-zero.
- **Caps.** \(\kappa\le H(X\mid O,F)\le H(X\mid Y)\) and \(\kappa\le S(C)\le2\) bits. The first is the export-bookkeeping cap (prior art; independent convergence).
- *Spot check (Sweep P, Sweep P priors).* Taking no pool unitary and pool member 0 in turn, \(I(X;C\mid O,F{=}f)\) lies in 0.083–0.260 bits at \(\theta=\pi/16\) and 0.418–1.149 bits at \(\theta=\pi/4\) across the 20 priors.

## 4. Kill criterion, sample unit and controls (binding)

**Sample unit and target.** At each strength \(\theta_j\), compute \(\kappa(\theta_j;\pi_k)\) and
\[
\Delta D(\theta_j;\pi_k)=D(\theta_j;\pi_k)-D(0;\pi_k)
\]
for each of the \(K=20\) priors. That gives \(n=20\) pairs, and \(r_j=r(\kappa,\Delta D)\) is their Pearson correlation.

- \(D\) comes from the joint law \(P(f,x,o)=\lvert\text{pool}\rvert^{-1}\pi_k(x)\operatorname{Tr}[\Pi_o\,\mathcal N_\theta^{\otimes2}(V_f\rho_xV_f^\dagger)]\). \(D(0)\) is the same quantity at \(\theta=0\) (identity channel), with the same prior and pool.
- **Plain \(D\) is not a valid target** (decision 2; §6 risk 6). \(r(\kappa,D)\) is reported only as diagnostic B-1.

**Hit rule.**

- A hit requires \(r_j\ge0.8\) at at least 15 of the 20 strengths. 10–14 is ambiguous, and 9 or fewer is dead.
- At \(j=1\) (\(\theta=0\)), \(\kappa\equiv0\) and \(\Delta D\equiv0\) for every prior. So \(r_1\) is undefined and counts as a non-hit, as in Sweep P. The count stays at 20 strengths with the same thresholds, so at most 19 can hit.
- At \(n=20\), the one-sided 5% critical value is 0.378. The threshold 0.8 acts as an effect-size line, and the 20 strengths are not independent tests.

**Mandatory controls before any hit call.** These are computed at every strength in every sweep that runs, in the same pass as the main statistic. Nothing is labelled until all of them are in.

1. **Variance decomposition and partial correlation.**
   - Since \(\Delta D=-\Delta I(F;Y)-\Delta H(Y\mid X)\), report the shares \(\operatorname{Cov}(\Delta D,\Delta T_i)/\operatorname{Var}\Delta D\) and \(\operatorname{Cov}(\kappa,T_i)/\operatorname{Var}\kappa\).
   - Here \(T_i\in\{H(Y),I(X;Y),H(X\mid Y),H(X),I(F;Y),H(Y\mid X)\}\) is evaluated at \(\theta_j\), and \(\Delta T_i=T_i(\theta_j)-T_i(0)\).
   - Report the partial correlation \(r(\kappa,\Delta D\mid H(Y),I(X;Y),H(X\mid Y),H(X))\), with the controls at \(\theta_j\). Only three of the four controls are independent, so df = 15 and the one-sided 5% critical value is **0.412** (as in Amendment 1).
2. **Sufficiency check.**
   - Fit \(\kappa\) linearly (with intercept) on \(H(X\mid Y)\), \(H(X)\) and \(H(Y)\) at \(\theta_j\) across the 20 priors.
   - A strength with \(r(\kappa,\Delta D)\ge0.8\) and \(R^2\ge0.95\) is flagged as **potentially definitional**.
3. **Classical-record register (Stage 3 control 3, same convention).**
   - Replace each \(\rho_{C\mid x,o,f}\) by its diagonal in the register's computational basis. In this design that is the pointer basis (§1).
   - Recompute \(\kappa\) and \(r(\kappa_{\rm deph},\Delta D)\).
   - This is the register that measures and keeps only the classical outcome record. It is mandatory and reported, and it does not enter the carry rule.
4. **Register-orientation shuffle with the cost-level carry rule.**
   - Replace each \(\rho_{C\mid x,o,f}\) by \(W\rho W^\dagger\), with Haar \(W\) drawn independently per \((x,o,f)\).
   - Set \(\Delta\kappa_{\rm shuf}(\theta_j;\pi_k)=\kappa_{\rm shuf}(\theta_j;\pi_k)-\kappa_{\rm shuf}(0;\pi_k)\), and \(r_{\Delta\rm shuf}(\theta_j)=r(\Delta\kappa_{\rm shuf}(\theta_j),\Delta D(\theta_j))\) across the 20 priors.
   - **Seed and scheme (LOCKED).** Seed `2026112632`. For pool member \(f\) in sweep \(s\) (P = 1, M = 2), `numpy.random.default_rng([2026112632, s, f])` draws 20 Haar \(4\times4\) unitaries in \((x,o)\) order. The same \(W\) is used at every strength.
   - The raw \(r(\kappa_{\rm shuf},\Delta D)\) is reported as a diagnostic.

**Carry rule (as in Amendment 1, now on \(\Delta D\)).** A flagged strength stands as a hit only if \(r_{\Delta\rm shuf}(\theta_j)<0.412\). An undefined value means it does not stand. The count compared with 15 / 10–14 / ≤ 9 is unflagged hits plus flagged hits that stand. The raw count of \(r(\kappa,\Delta D)\ge0.8\) is reported alongside it.

**Brief-requested controls, with their status** (§6, risks 4 and 6).

- **(a) A register that measures nothing.** This is the \(j=1\) sweep point (\(s=0\)). \(\kappa\equiv0\) and \(\Delta D\equiv0\) there by construction. It is the anchor of \(\Delta D\) and of the shuffle baseline, not an independent control.
- **(b) A register that measures but discards the record.** Tracing out or resetting the record gives \(\kappa\equiv0\) at every strength. The output law, \(D\) and \(\Delta D\) are **identical** to the main run. It is reported as a **sanity check, not a control**. The informative version of "measures without keeping a quantum record" is control 3.

**Diagnostics (report-only, not binding on the hit rule; decision 4).** These are reported at every strength in every sweep. They do not change the count or the label.

- **T-a, iso-entropy priors.** Draw \(d_k\sim\mathrm{Dirichlet}(\mathbf 1)\) with `default_rng(2026112633)`, one call, `size=20`. Set \(\pi_k(b)=0.9\,d_k^{\,b}/\lVert d_k^{\,b}\rVert_1+0.1\,e_{\Phi^+}\), and bisect \(b\ge0\) so that \(H(\pi_k)=2.000\) bits. Report \(r(\kappa,\Delta D)\) across this set.
- **T-b.** \(r(\kappa,\Delta D\mid H(X))\), with df = 17 and a one-sided 5% critical value of 0.389.
- **T-c.** The single-member sufficiency \(R^2\) (no pool unitary, and pool member 0) and the export ratio \(\kappa/H(X\mid O,F)\).
- **B-1, baseline.** \(r(\kappa,D)\), \(r(\kappa,D(0))\) and \(r(D(\theta_j),D(0))\).

**Labels.**

- A hit that survives is reported as a hit.
- A flagged hit that fails the carry rule is reported as "flagged, does not stand".
- Below the hit rule, the compilation reading is dead for this architecture as well, and that is reported as a null.

The criterion is fixed and will not be revised after results are seen.

## 5. Sweeps and run order

1. **Sweep P** (pure meter \(\lvert+\rangle^{\otimes2}\)) is primary and runs first. The controls and diagnostics are computed in the same pass.
2. **Sweep M** (noisy meter, \(p=0.7311\)) runs only if Sweep P lands in 10–14.
   - A \(\lvert-\rangle\) start mirrors the pointer, so Sweep M is a meter whose classical record is flipped with probability \(1-p\).
   - Its induced channel on \(A\) is identical to Sweep P's, because \(\langle r_+\vert r_-\rangle=\cos2\theta\) for either start. So its \(D\) and \(\Delta D\) are identical too, and only \(\kappa\) changes.
   - *Spot check:* at \(\theta=\pi/4\) with no pool unitary, \(\kappa\) = 0.097–0.207 bits, against 0.418–1.149 bits in Sweep P.
3. **Combination.** As in Stage 3: 15 or more is a hit and 9 or fewer is dead, with Sweep M not run in either case. A Sweep M hit after an ambiguous Sweep P is reported as a conditional hit, and anything else as dead.

**Pairing with Stage 3.** The priors and pool are those of Stage 3 Sweep P, and the \(\theta=0\) output law equals Stage 3's \(J=0\) law. So \(D(0)\) is the same 20 numbers in both stages, and the two runs pair prior by prior.

**What every run logs:**

- the code commit and NumPy version;
- \(\beta\), the \(\theta\) grid and the register start;
- the prior seed and rule, and the pool hash;
- per (strength, prior): \(\kappa\), \(D\), \(D(0)\), \(\Delta D\) and every term of §4;
- every control and diagnostic;
- both hit counts.

## 6. Risks (analysed before pre-registration)

**Verdict summary.**

| # | Risk | Verdict |
|---|---|---|
| 1 | Stinespring equivalence | **Not fixable; reframed.** A different coupling family in the same template, not a new architecture class. |
| 2 | Commuting-readout trap | **Fixed** by the tilted axis \(\beta=\pi/4\). |
| 3 | Tautology and prior-entropy driver | **Partly fixable.** The cap is structural; diagnostics T-a to T-c are report-only. |
| 4 | Discard control is \(\kappa\equiv0\) | **Not a control.** Reported as a sanity check; control 3 does the job. |
| 5 | No ML time for a measurement | **Fixed** by the dilation's ML bound, which lands exactly on the projective point. |
| 6 | Degeneracy with measure-nothing | **Fixed** by the target \(\Delta D\) (decision 2). Plain \(D\) would have decided the test through \(D(0)\). |

**Risk 1. Stinespring equivalence.**

- Measure-and-retain is, by Stinespring, a controlled unitary into a record register. Here it is exactly \(U_\theta=e^{-i\theta\sum\sigma_{\hat n}\otimes Y}\): a two-body single-parameter coupling on the same four qubits, from a product start, with the same readout, pool and cost.
- So it is not a "no joint Hamiltonian" architecture. No such architecture exists at this level, and keeping the record coherently *is* entangling with it.

What genuinely differs from Stage 3:

- **Neither coupling family contains the other.** The XY coupling commutes with no single-qubit observable on \(A\) alone. \(\sigma_{\hat n}\otimes Y\) commutes with \(\sigma_{\hat n}\) on \(A\), which makes it a quantum-non-demolition coupling.
- **The induced input channel is unital** \(\hat n\)-dephasing, not non-unital amplitude damping.
- **The window reaches a complete record.** The strength runs to a projective measurement inside the ML window.
- **The record has a pointer basis, so control 3 separates the classical record from its coherence.** *Spot check:* the classical record holds much less than the coherent one, for example 0.006–0.022 bits against 0.083–0.260 bits at \(\theta=\pi/16\) with no pool unitary.

Verdict: Stage 3b tests whether the Stage 3 null is specific to excitation-transport channels. A null here retires the reading only for these two single-parameter channel families of the four-qubit template.

**Risk 2. Commuting-readout trap.**

- *\(\hat n=z\).* The dilation becomes the rejected ZZ draft with the register in \(\lvert+\rangle\). The output law does not depend on \(\theta\), and \(\kappa\equiv0\).
  - *Spot check:* on the full pool, \(\max\lvert P(o\mid x,f)-P_0\rvert\le3\times10^{-16}\) and \(\max\lvert\kappa\rvert\le7\times10^{-16}\) at four strengths.
- *\(\hat n=x\).* At the projective point, \(D=\log_2200-2\) for every prior.
  - *Spot check:* \(D\)'s spread across priors falls from 0.063 to \(5\times10^{-15}\).
- *\(\beta=\pi/4\) (locked).* The law moves with \(\theta\) (largest total-variation shift 0.519 at \(\pi/4\)), and \(D\) keeps a spread at the projective point (standard deviation 0.023).
- \(F\) acts before the measurement.
- Verdict: fixed.

**Risk 3. Tautology and the prior-entropy driver.**

- With \(\beta=\pi/4\) the record never copies \(X\). The cap \(\kappa\le H(X\mid O,F)\) remains, and it is structural.
- *Spot check:* on basis-only priors with no pool unitary, \(\kappa\) comes within 0.004 bits of \(H(X\mid O)\) at \(\theta=\pi/16\). With the Bell floor \(w_{\min}=0.10\), the minimum gap over the test strengths is 0.31 bits (no pool unitary) and 0.51 bits (pool member 0).
- *Spot check:* on the Sweep P priors, the single-member fit of \(\kappa\) on \(H(X\mid Y)\), \(H(X)\) and \(H(Y)\) already gives \(R^2\) = 0.92–0.97, with \(r(\kappa,H(X))\) = 0.94–0.96. So control 2 is likely to flag, as in Sweep P.
- The priors' entropy is a property of the sample unit, not of the coupling. The target \(\Delta D\) removes the coupling-independent part \(D(0)\), but not the shared dependence on \(H(X)\) of \(\kappa\) and of \(D\)'s change.
- The report-only diagnostics are T-a (*spot check:* the iso-entropy set is feasible for 20/20 draws at \(H(X)=2.000000\), with Bell weight 0.100–0.472, and \(D\) still varies across it), T-b and T-c.
- Verdict: partly fixable.

**Risk 4. The discard control.**

- With the record traced out or reset, \(\kappa\equiv0\). *Spot check:* \(\le6\times10^{-15}\).
- The output law, \(D\) and \(\Delta D\) are unchanged.
- So it is a sanity check, not a control. It shows only that \(D\) is blind to retention. Control 3 is the informative comparison.

**Risk 5. Resource normalization.**

- An abstract instrument has no duration. A time exists only through the dilation.
- Take \(H_1=\sum_i\sigma_{\hat n}\otimes Y\) and \(\sigma=\bar\rho_A\otimes\lvert+\rangle\langle+\rvert^{\otimes2}\). Then \(\langle H_1\rangle_\sigma=0\) and \(E_0=-2\) (total energy of both pairs).
- So \(\theta_{\rm ML}=\pi/4\) for every \(\beta\) (spot check). The window ends exactly at the projective point.
- *Caveat.* The bound is not saturated: a Bell input keeps overlap 0.5 at \(\pi/4\) and becomes orthogonal at \(\pi/2\). The per-pair convention would give \(\pi/2\), past the projective point.
- Verdict: fixed.

**Risk 6. Degeneracy with the measure-nothing baseline (resolved by the target \(\Delta D\)).**

- \(\theta=0\) is the identity channel on \(A\), and its output law equals Stage 3's \(J=0\) law to \(4\times10^{-16}\). So \(D(0)\) depends only on the prior and the pool.
- *Spot check (D only, full pool, Sweep P priors).* \(r(D(\theta),D(0))\ge0.997\) at every test strength up to \(\pi/4\). The spread of \(D(\theta)-D(0)\) is \(3\times10^{-4}\) at \(\pi/76\) and 0.040 at \(\pi/4\), against 0.023–0.063 for \(D\).
- With plain \(D\) as the target, \(r(\kappa,D)\approx r(\kappa,D(0))\) across the whole window. That would correlate the cost with a deficit the measurement never touched.
- Stage 3 Sweep P shows the same effect post hoc. The cost tracked \(D(0)\) at every strength, and the raw hits sat where \(D(\theta)\) still tracked \(D(0)\) ([analysis-stage3-compilation-null.md](analysis-stage3-compilation-null.md)).
- The target is therefore \(\Delta D\), whose \(j=1\) value is identically 0. The plain-\(D\) correlation is kept only as diagnostic B-1.
- The \(\Delta D\) spread is small at weak strength (\(3\times10^{-4}\) at \(\pi/76\)). It is exact to machine precision, but at the lowest strengths a hit there should be read together with control 1.

**Other risks carried from Stage 3.**

- *The 2-bit cap and pool independence.* \(\kappa\le2\) bits does not grow with \(\lvert\text{pool}\rvert\). This design tests correlation, not coverage of \(D\).
- *Placement.* Channel-cost research stays parallel to the paper.

**Expected outcome, recorded in advance.** The prior-entropy mechanism of Sweep P comes from the sample unit, not the coupling, so another null is the likely outcome. The informative value is whether the null holds across both channel families once the coupling-independent \(D(0)\) is removed.

## 7. Pre-registration items (recorded 2026-11-26, Cyotee)

1. **Cost:** \(\kappa=I(X;C\mid O,F)\). It equals \(S(C)-I(C;O)\) given \(F\) for the pure meter start. The literal \(S(C)-2I(C;O)\) reading is not used. **LOCKED.**
2. **Mechanism:** coherent record primary (dilation of §1). The classical record is control 3. **LOCKED.**
3. **Axis:** \(\beta=\pi/4\) in the \(x\)–\(z\) plane, the same for both qubits. **LOCKED.**
4. **Priors:** seed `20261126`, the Stage 3 rule, \(K=20\), \(w_{\min}=0.10\). These are the same priors as Sweep P. **LOCKED.**
5. **Strength grid and normalization:** \(\theta_j=\tfrac{j-1}{19}\cdot\tfrac{\pi}{4}\) with \(t_\ast=1\), at the total-energy ML bound of \(\sigma\). **LOCKED.**
6. **Pool:** CE-15, seed 2026, SHA-256 `d11fa3d1ec4594b7d1235759fde33b8b98689646b44efd163fffba97084618e2`, applied to \(A_1A_2\) before the measurement. **LOCKED.**
7. **Target:** \(\Delta D(\theta_j)=D(\theta_j)-D(0)\). Plain \(D\) is not a valid target. Hit rule, \(R^2\) flag, partial-\(r\) 0.412 and the shuffle carry rule all apply to \(r(\kappa,\Delta D)\). The undefined \(r_1\) is a non-hit. **LOCKED.**
8. **Diagnostics:** T-a, T-b, T-c and B-1 are report-only, not binding on the hit rule. **LOCKED.**
9. **Sweep M:** noisy meter, \(p=0.7311\), run only if Sweep P lands in 10–14. **LOCKED.**
10. **Seeds:** shuffle `2026112632`; iso-entropy `2026112633`. **LOCKED.**
11. **Carried unchanged from Stage 3 with Amendment 1:**
    - five inputs with \(\lvert\Phi^+\rangle\);
    - rank-4 readout;
    - 20 strengths including zero;
    - \(r\ge0.8\); \(\ge15\) alive, 10–14 ambiguous, \(\le9\) dead;
    - \(R^2\ge0.95\) on \(H(X\mid Y)\), \(H(X)\), \(H(Y)\);
    - partial-\(r\) critical value 0.412 (df 15);
    - the cost-level carry rule;
    - controls in the same pass, before any label;
    - control-3 dephasing in the register's computational basis (here the pointer basis).

## 8. Run gate

The pilot and the full sweep run only after this file is on master. The run script checks this file's SHA-256 and the pool hash before computing anything. A code-validation pilot, if run, is not a result and is reported as such.

## 9. Spot checks used in this design

Scratch only and not committed: exact 16×16 linear algebra at \(\theta\in\{0,\pi/16,\pi/8,3\pi/16,\pi/4\}\) (plus \(\pi/76\) for risk 6), on the Sweep P priors, loading the CE-15 pool read-only (hash checked).

- \(\kappa\) was evaluated only with no pool unitary and with pool member 0.
- \(D\) was evaluated on the full pool. No correlation of \(\kappa\) with \(D\) or \(\Delta D\) was computed for this design.
- Corrected-bound slack on the full pool was at least 1.67 bits at every test point, and \(\lvert I(X;F)\rvert\le4\times10^{-15}\).

None of these numbers is a result of the experiment, which has not been run.

## 10. Scope

Tier 2 only: a four-qubit toy with one measurement coupling, one readout and five input states under 20 priors. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this design beyond the information-theoretic bookkeeping above. Once run, the results will be reported against §4 as recorded here, including a null.
