# Channel cost, Stage 3: compilation-cost experiment design (pre-registered, Tier 2 toy)

**Tier:** 2 of 3. This note belongs to the channel-level channel-cost line of research, after [CHANNEL_COST_STAGE1.md](https://github.com/cyotee/computational-entropy/blob/master/CHANNEL_COST_STAGE1.md) and [channel-cost-stage2.md](channel-cost-stage2.md). It is a **toy model** of four qubits.

- It is **not** evidence about hadronic or QCD physics (**NOT QCD**).
- It makes no gravitational, quantum-gravity or thermodynamic claim. A "cost" here is an entropy in bits. Pricing it at \(k_BT\ln2\) would be a convention only.
- The von Neumann entropies below are standard entropies of a toy register's reduced density matrices, used the same way as the entropy exchange of Stages 1–2. No claim about any quantum layer of the programme is made.

**Status:** 2026-11-26 · **design only, pre-registered, nothing run.** No simulation code for this stage is committed, and no sweep has been run. A scratch code-validation pilot (not committed, not a result) preceded Amendment 1. Cyotee fixed the parameters in §2 before any result exists. **The kill criterion (§4) is binding.** The items in §7 must be recorded before the first run. Numbers labelled *spot check* come from a scratch exact-linear-algebra check (16×16 matrices, a few \(\theta\) values, no sweep). It is not committed, and none of its numbers is a result of this experiment (§8).

**What is being tested, and its label.** The *compilation reading* is Cyotee's conjecture: the deficit of the original form is tracked by an entropy cost paid in the channel's own register, namely input information the interaction moves into the register that the output does not carry. The repository does not label this reading anywhere else. It sits inside the Tier 2 channel-cost line, whose Stage 2 definitions were all **tested and rejected** as rescues of the original form ([channel-cost-stage2.md](channel-cost-stage2.md) §6). Here it is a **conjecture under test, not a claim**. Nothing in this file is a result.

**Revision note (from the ZZ draft).** The first draft used a \(Z\otimes Z\) Ising coupling. Under ZZ, the evolution is controlled by the inputs' Z values. So the computational-basis output law, every deficit built from it, and the cost are all independent of the coupling strength. In addition, with pure inputs, a pure register and full readout, the per-input cost is identically zero for any coupling. The draft's kill criterion could therefore only fail by construction. Cyotee adopted a revised design ("FS-2"): XY coupling, the cost taken over an input ensemble, K = 20 pre-registered priors as the sample unit, a fixed pool for \(F\), a fixed time at the Margolus–Levitin bound of a stated reference state, and mandatory tautology controls. This file is that revision.

**Amendment 1 (2026-11-26, Cyotee).** Approved by Cyotee after a scratch pilot (code-path validation only: 3 strengths, 10 pool members, not committed, no result) exposed three gaps. These are formal amendments to the pre-registration. They were made before any full sweep was run, and they are applied inline in §4, §5 and §7.

1. **Partial-correlation critical value: 0.412 (df = 15).** The four controls of §4 control 1 overlap mathematically, because \(I(X;Y)=H(X)-H(X\mid Y)\). Only three are linearly independent. So df \(=20-2-3=15\), and the one-sided 5% critical value is \(r_c=0.412\), not 0.426.
2. **Carry rule for a flagged hit (cost-level shuffle baseline).** A strength flagged by control 2 (\(R^2\ge0.95\)) stands as a hit only if the orientation-shuffle control (control 4) loses the correlation once its \(J=0\) value is removed at the cost level. Define, per prior \(\pi_k\), \(\Delta\kappa_{\rm shuf}(\theta_j;\pi_k)=\kappa_{\rm shuf}(\theta_j;\pi_k)-\kappa_{\rm shuf}(0;\pi_k)\), and \(r_{\Delta\rm shuf}(\theta_j)=\) the Pearson correlation of \(\Delta\kappa_{\rm shuf}(\theta_j;\cdot)\) with \(D(\theta_j;\cdot)\) across the 20 priors. A flagged hit stands only if \(r_{\Delta\rm shuf}(\theta_j)<0.412\). An undefined \(r_{\Delta\rm shuf}\) means the flagged hit does not stand. The dephased-register control (control 3) is still mandatory and reported, but a flagged hit stands solely on this shuffle condition.
3. **Shuffle baseline.** Random rotations alone make the shuffled cost non-zero at \(J=0\). The baseline is subtracted from the shuffled **cost** \(\kappa_{\rm shuf}\), prior by prior, within the same sweep, the same 20 priors, the same pool and the same pre-registered rotations, and the subtraction is applied **before** hits are evaluated (in the carry rule), not only in reporting. A strong interaction that merely preserves what random rotations already create must not read as a hit. The raw shuffle correlation \(r_{\rm shuf}(\theta_j)=r(\kappa_{\rm shuf}(\theta_j),D(\theta_j))\) is still reported as a diagnostic.
   - *Replaced version (r-level).* An earlier form of this amendment subtracted the correlation instead: \(r_{\rm shuf}(\theta_j)-r_{\rm shuf}(0)<0.412\). It was replaced before any full-sweep run because it was vacuous. The \(J=0\) baseline was about 0.75 (pilot: 0.753 in Sweep P, 0.734 in Sweep M), so the condition held for every possible \(r_{\rm shuf}\le1\). The scratch pilot (strengths \(j=1,10,20\), pool members 0–9, not a result) gave \(r_{\Delta\rm shuf}=0.596\) and \(-0.190\) in Sweep P and \(0.665\) and \(-0.220\) in Sweep M at \(j=10\) and \(j=20\). Cyotee approved the cost-level form.
4. **Defaults locked as written.** \(t_\ast=1\) (\(\hbar=1\), \(J\) in units of \(1/t_\ast\), so \(J_{\max}=\pi/8\)); control 4 seed `202611264`; control 3 dephasing in the register's computational basis; Sweep M \(p=0.7311\), the value in this document.
5. **Run order confirmed.** Sweep P (pure \(\lvert00\rangle\) register) is primary. Sweep M (mixed register) runs only if Sweep P lands in the 10–14 band.

*Open note (not adopted).* Whether a baseline subtraction should also apply to the main \(r(\kappa,D)\) is left open. As written, it does not: the main \(r\) is undefined at \(J=0\) (\(\kappa=0\) there), so it has no \(J=0\) baseline to subtract.

**Naming.** "Stage 3" means the third stage of the channel-cost line. It is unrelated to the "Stage 3" of the three-stage workflow in [PROGRESS_REPORT.md](https://github.com/cyotee/computational-entropy/blob/master/PROGRESS_REPORT.md).

**Context (repository results this design must respect).**

- **The bound and the deficit.** The original form \(I(X;Y)+H(F\mid Y)\le H(Y)\) fails in the toys. The corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) is a theorem when \(X\perp F\). The deficit is \(D=I(X;Y)+H(F\mid Y)-H(Y)\).
- **Recent nulls.** These show \(D\) following whichever term of its own definition varies:
  - In the de-duplicated one-bit run, \(D\) against the input–output mutual information \(I(X;Y)\) gave Pearson 0.998, on points that all had \(k=2\) ([analysis-pool-dedup-null.md](analysis-pool-dedup-null.md)).
  - On the two-qubit surface, \(H(Y)\) carries about 97.5% of \(\operatorname{Var}D\) (scratch analysis, not committed).
  
  §4's controls are written with this in mind.
- **Prior art.** \(H(X\mid Y)\)-type terms are prior art (Baez–Fritz–Leinster, Fullwood–Parzygnat). The overlap with this programme is independent convergence.
- **k is a proxy.** The candidate-set size \(k\) is used only as a computable proxy. No description-length or Kolmogorov-complexity claim is made.

## 1. Architecture

**Qubits.**

- Two input qubits \(A_1,A_2\). These are also the qubits read out at the end.
- Two channel-register qubits \(C_1,C_2\). \(C_i\) is the channel partner of \(A_i\).
- The initial state is a product between inputs and register, \(\rho_A\otimes\rho_{C,0}\).

**Interaction: XY (flip-flop) coupling, single free parameter \(J\).**
\[
H_J=J\sum_{i=1,2}\big(X_{A_i}X_{C_i}+Y_{A_i}Y_{C_i}\big),\qquad U_J=e^{-iH_Jt}=U^{(1)}_J\otimes U^{(2)}_J,\qquad \theta:=Jt.
\]

- There are no \(A_1\)–\(A_2\) or \(C_1\)–\(C_2\) terms.
- The coupling exchanges excitations: \(\lvert10\rangle_{A_iC_i}\mapsto\cos2\theta\,\lvert10\rangle-i\sin2\theta\,\lvert01\rangle\), while \(\lvert00\rangle\) and \(\lvert11\rangle\) are stationary.
- Its input-side operators do not commute with \(Z_A\). So the output law depends on \(J\), which removes the ZZ degeneracy.

**The GAD identity (documented here, spot-checked).** Take a register start \(\mathrm{diag}(p,1-p)^{\otimes2}\). The channel this induces on each input qubit is exactly generalized amplitude damping, \(\mathrm{GAD}(\gamma,p)\) with \(\gamma=\sin^22\theta\), in the repository's convention (Nielsen & Chuang §8.3.5; [procedural-share.md](procedural-share.md) §2):

- \(P(0\mid1)=p\gamma\) and \(P(1\mid0)=(1-p)\gamma\).
- With \(p=1\), the \(\lvert00\rangle\) start, it is plain amplitude damping.

*Derivation.* Fix register \(\lvert0\rangle\). The Kraus operators on \(A\) are \(K_0=\lvert0\rangle\langle0\rvert+\cos2\theta\lvert1\rangle\langle1\rvert\) and \(K_1=-i\sin2\theta\lvert0\rangle\langle1\rvert\). Register \(\lvert1\rangle\) gives the mirror image. Mixing the two with weights \(p\) and \(1-p\) gives the four GAD Kraus operators.

*Spot check.* For input \(\lvert10\rangle\) at \(\theta=\pi/16\) and \(\pi/8\), with \(p=0.7311\) and with \(p=1\), \(P(A_1{=}0)\) equals \(p\gamma\) and \(P(A_2{=}1)\) equals \((1-p)\gamma\) to 8 decimals. This identity links Stage 3 directly to the GAD toy channel of Stages 1–2 and CE-6/CE-12.

**Readout.** Measure \(A_1A_2\) in the computational basis with full resolution: four outcomes, rank-1 projectors. This gives the classical outcome \(O\). For each input, outcome and pool member, log the register's conditional state \(\rho_{C\mid x,o,f}\), the register's reduced state, and \(P(o\mid x,f)\).

*Naming note.* The locked description "rank two (full resolution on both output qubits)" means full resolution. In the repository's readout convention, rank counts outcomes ([procedural-share-surface.md](procedural-share-surface.md) §2), so this readout is rank 4 there.

## 2. Parameters

| Parameter | Value | Status |
|---|---|---|
| Input states | Five: \(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle\) and \(\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2\) | locked (unchanged) |
| Input priors | \(K=20\) pre-registered priors over the five inputs, with Bell weight \(\ge w_{\min}=0.10\) (§6.4) | adopted (FS-2) |
| Coupling | XY flip-flop, single free parameter \(J\) | adopted (FS-2), replaces ZZ |
| Readout | Full resolution on both output qubits (four outcomes) | locked |
| Time and sweep | \(t\) fixed once; 20 equal steps \(\theta_j=\tfrac{j-1}{19}\cdot\tfrac{\pi}{8}\), \(j=1,\dots,20\); \(J=0\) included (§6.3) | locked range; total-energy ML adopted |
| Candidate pool \(F\) | The existing CE-15 Margolus–Levitin pool (200 two-qubit unitaries on \(A\), seed 2026, recorded SHA-256), applied before the coupling; no new pool (§6.2) | **locked** (Cyotee) |
| Cost | \(\kappa=I(X;C\mid O,F)\) over the input ensemble (§3) | adopted (FS-2) |
| Register start | Sweep P: \(\lvert00\rangle\) (pure). Sweep M: \(\mathrm{diag}(0.7311,0.2689)^{\otimes2}\) = GAD at \(T=1\) | locked order; states adopted |
| Kill criterion | Hit iff Pearson \(r(\kappa,D)\ge0.8\) at \(\ge15\) of 20 strengths, across the \(K=20\) priors, after the mandatory controls (§4); sufficiency tolerance \(R^2\ge0.95\) | locked; "\(\ge\)" per Cyotee; tolerance **locked** (Cyotee) |
| Ambiguity band | Sweep P hits 10–14 → run Sweep M; \(\ge15\) → hit; \(\le9\) → dead | adopted |

## 3. Cost

**Definition.** The cost is the input information that the interaction moved into the register and that the output does not carry. It is computed over the input ensemble under a prior \(\pi\), conditioned on the pool member:
\[
\kappa \;:=\; I(X;C\mid O,F)=\frac{1}{\lvert\text{pool}\rvert}\sum_f I(X;C\mid O,F{=}f),\qquad I(X;C\mid O,F{=}f)=S(C\mid O,F{=}f)-S(C\mid X,O,F{=}f).
\]
Each term is evaluated on the classical–quantum state \(\sum_{x,o}\pi(x)P(o\mid x,f)\,\lvert x\rangle\langle x\rvert\otimes\lvert o\rangle\langle o\rvert\otimes\rho_{C\mid x,o,f}\).

**Properties.**

- **Zero at \(J=0\) by construction.** At \(J=0\), \(\rho_{C\mid x,o,f}=\rho_{C,0}\) for every \(x\), so \(C\) is independent of \(X\) given \((O,F)\). This holds in both sweeps. *Spot check:* 0 to machine precision for both register starts.
- **Relation to the original candidate.** For a pure register start, every \(\rho_{C\mid x,o,f}\) is pure, so \(S(C\mid X,O,F)=0\) and \(\kappa=S(C\mid O,F)=S(C)-I(C;O)\) given \(F\), the locked formula. For a mixed start, \(\kappa\) subtracts the register's own leftover disorder \(S(C\mid X,O,F)\), which the original formula would have counted.
- **Not per input.** For a single input, \(\kappa\) is identically zero in Sweep P (pure input, pure register, rank-1 readout). The ensemble is what makes it non-zero.
- **Caps.** \(\kappa\le H(X\mid O,F)\le H(X\mid Y)\) and \(\kappa\le S(C)\le2\) bits. The first cap is the export-bookkeeping risk (§6.5).

## 4. Kill criterion, sample unit and mandatory controls (binding)

**Sample unit.** \(X\) is the five input states under each of the \(K=20\) pre-registered priors. At each strength \(\theta_j\), compute \((\kappa,D)\) once per prior, giving \(n=20\) pairs, and take their Pearson \(r_j\).

*Interpretation recorded.* Cyotee wrote "X = the 20 inputs". That is read here as the five input states under each of the \(K=20\) priors, not as 20 distinct input states.

**Hit rule.**

- A hit requires \(r_j\ge0.8\) at at least 15 of the 20 strengths.
- At \(J=0\), \(\kappa=0\) for every prior, so \(r_1\) is undefined and counts as a non-hit. At most 19 strengths can hit.
- Exact one-sided 5% critical value at \(n=20\): \(r_c=0.378\). The one-sided \(p\) at \(r=0.8\) is about \(1.2\times10^{-5}\). So 0.8 acts as an effect-size threshold well above significance. The 20 strengths are not independent tests.

**Mandatory controls before any hit call.** These are computed at every strength for every sweep that is run, and reported with the hit count. They do not change the count. They decide its label.

1. **Variance decomposition and partial correlations.**
   - Write \(D\) in its terms. With \(F\) uniform on the pool, \(D=\log_2\lvert\text{pool}\rvert-I(F;Y)-H(Y\mid X)\).
   - Report the shares \(\operatorname{Cov}(D,T_i)/\operatorname{Var}D\) and the same for \(\kappa\), over \(T_i\in\{H(Y),I(X;Y),H(X\mid Y),H(X),I(F;Y),H(Y\mid X)\}\).
   - Report the partial correlation \(r(\kappa,D\mid H(Y),I(X;Y),H(X\mid Y),H(X))\). Because \(I(X;Y)=H(X)-H(X\mid Y)\), only three of the four controls are independent, so df = 15 and the one-sided 5% critical value is **0.412** (Amendment 1).
2. **Sufficiency check.**
   - Across the 20 priors at each strength, fit \(\kappa\) linearly (with intercept) on features of the classical law alone: \(H(X\mid Y)\), \(H(X)\) and \(H(Y)\).
   - **Locked tolerance (Cyotee): \(R^2\ge0.95\).** At or above it, the classical output law is taken to predict the cost, and the hit is flagged as **potentially definitional**. A flagged hit stands only if the carry rule below holds (Amendment 1).
3. **Dephased classical-copy register.** Replace each \(\rho_{C\mid x,o,f}\) by its diagonal in the register's computational basis, recompute \(\kappa\) and \(r_j\), and report both. This isolates any coherent contribution from Shannon-level bookkeeping. It is mandatory and reported, but it does not enter the carry rule (Amendment 1).
4. **Register-orientation shuffle.** Replace each \(\rho_{C\mid x,o,f}\) by \(W\rho W^\dagger\), with \(W\) Haar-random and drawn independently per \((x,o,f)\) from a pre-registered seed. Recompute \(\kappa_{\rm shuf}\) and \(r_{\rm shuf}(\theta_j)\). This keeps per-branch spectra and destroys the overlaps the interaction created.
   - **Seed and scheme (LOCKED, Amendment 1).** Seed `202611264`. For pool member \(f\) in sweep \(s\) (P = 1, M = 2), `numpy.random.default_rng([202611264, s, f])` draws 20 Haar \(4\times4\) unitaries in \((x,o)\) order. The same \(W\) is used at every strength.
   - **Baseline (Amendment 1, cost level).** \(\Delta\kappa_{\rm shuf}(\theta_j;\pi_k)=\kappa_{\rm shuf}(\theta_j;\pi_k)-\kappa_{\rm shuf}(0;\pi_k)\), same sweep, priors, pool and rotations, and \(r_{\Delta\rm shuf}(\theta_j)=r(\Delta\kappa_{\rm shuf}(\theta_j),D(\theta_j))\) across the 20 priors. Both \(r_{\Delta\rm shuf}\) and the raw \(r_{\rm shuf}\) (diagnostic) are reported at every strength.

**Carry rule (Amendment 1).** A strength with \(r_j\ge0.8\) and \(R^2\ge0.95\) stands as a hit only if \(r_{\Delta\rm shuf}(\theta_j)<0.412\). If \(r_{\Delta\rm shuf}(\theta_j)\) is undefined, the flagged hit does not stand. The hit count compared with the 15 / 10–14 / ≤ 9 rule counts unflagged hits plus flagged hits that stand. The raw count of \(r_j\ge0.8\) is reported alongside it.

**Labels.**

- A hit that survives the controls is reported as a hit.
- A hit flagged by control 2 (\(R^2\ge0.95\)) is reported as "hit, potentially definitional". It counts as a hit only if the carry rule holds: the correlation of the baseline-subtracted shuffled cost with \(D\) is below 0.412 (Amendment 1).
- Below the hit rule, the compilation reading is dead for this architecture, and that is reported as a null in the same way as the earlier channel-cost nulls.

The criterion is fixed before any run and will not be revised after results are seen. Amendment 1 was made after a code-validation pilot and before any full sweep.

## 5. Two-sweep structure and run order

1. **Sweep P (pure register start \(\lvert00\rangle\)) is primary and runs first** (confirmed in Amendment 1). The induced channel is amplitude damping with \(\gamma=\sin^22\theta\le\tfrac12\) over the window. Every bit of \(\kappa\) comes from the interaction.
2. **Sweep M (register \(\mathrm{diag}(0.7311,0.2689)^{\otimes2}\)) runs only if Sweep P's hit count lies in the ambiguity band 10–14.** The value \(p=0.7311\approx1/(1+e^{-1})=0.73106\) is the repository's \(T=1\) value, rounded; the literal 0.7311 is locked (Amendment 1), so the induced channel is \(\mathrm{GAD}(\gamma,0.7311)\). The same rule, controls and labels apply. Sweep M tests whether a cost signal comes from the interaction or from the register's own disorder. Because \(\kappa\) subtracts \(S(C\mid X,O,F)\), the initial disorder is not counted as cost.
3. **Combination.** Sweep P at 15 or more is a hit and at 9 or fewer is dead; Sweep M does not run in either case. How a Sweep M outcome resolves an ambiguous Sweep P is a pre-registration item (§7).

Every run logs:

- the code commit and NumPy version (2.x, per `requirements.txt`);
- \(t\), the \(\theta\) grid, and the register start;
- the 20 priors (seed and rule) and the pool hash;
- per strength and prior: \(\kappa\), \(D\) and all terms of §4;
- the four controls, including \(r_{\Delta\rm shuf}\) and the raw \(r_{\rm shuf}\), and both hit counts (raw and after the carry rule).

Both sweeps are reported whenever they are run.

## 6. Design details and remaining open risks

### 6.1 Coupling choice (resolved)

- **Why ZZ was dropped.** ZZ commutes with the readout; see the revision note.
- **Why XY.** XY was chosen over:
  - XX: a bit-flip dilation, which does not conserve excitations;
  - Heisenberg: identical to XY from a \(\lvert00\rangle\) register, with a shorter ML window, \(\pi/12\);
  - ZZ plus an input field: local dynamics not attributable to the coupling, and a second parameter.
  
  XY is a single-parameter exchange coupling, and it reproduces the repository's GAD channel exactly (§1).
- **What changes about the physics.** The test is now about excitation transport into the register.

### 6.2 Roles and the deficit (resolved, with pre-registration items)

| Role | Assignment |
|---|---|
| \(X\) | the five input states under prior \(\pi_k\), \(k=1,\dots,20\) (§4) |
| \(Y\) | the 2-bit computational-basis outcome \(O\) |
| \(F\) | uniform over a fixed pool of two-qubit unitaries \(V_f\) on \(A_1A_2\), applied before the coupling: the input becomes \(V_f\rho_xV_f^\dagger\) |
| candidate set | the pool itself, so \(k=\lvert\text{pool}\rvert\) is constant and used only as a proxy |

- **Joint law.** \(P(f,x,o)=\lvert\text{pool}\rvert^{-1}\pi_k(x)\operatorname{Tr}[\Pi_o\,N_\theta(V_f\rho_xV_f^\dagger)]\), where \(N_\theta\) is the register-induced channel on \(A\).
- **\(X\perp F\) by construction.** The pool is fixed before the channel, and \(X\) is drawn from \(\pi_k\) independently of \(f\). So the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) is a theorem here and is checked at every point.
- **\(D\) is defined per (strength, prior),** as in the two-qubit surface ([procedural-share-surface.md](procedural-share-surface.md), [procedural-share-mlpool.md](procedural-share-mlpool.md)).
- **Pool (locked, Cyotee; no new pool).** The existing CE-15 Margolus–Levitin pool `simulations/classical/data/ce15_ml_pool.json`:
  - 200 two-qubit unitaries;
  - GUE Hamiltonians at \(t_{\rm frac}=1\), seed 2026, `default_rng([seed, 12])`;
  - recorded SHA-256 `d11fa3d1ec4594b7d1235759fde33b8b98689646b44efd163fffba97084618e2`.
  
  It is used here only as a fixed list of \(4\times4\) unitaries. Its clustering rule was defined for another encoding, which does not matter for this use. The cost is conditioned on \(F\) (§3). Marginalizing \(F\) instead would give \(\kappa\le H(X,F\mid O)\) and re-import \(H(F\mid Y)\).

### 6.3 Time and the Margolus–Levitin bound (resolved)

- **Reference state.** \(\sigma=\bar\rho_A\otimes\rho_{C,0}\), with \(\bar\rho_A\) the uniform average of the five inputs. Every single-qubit Pauli expectation of \(\bar\rho_A\) is 0, so \(\langle H_1\rangle_\sigma=0\) for the XY coupling \(H_1\), with either register start. Hence \(\langle H_1-E_0(H_1)\rangle_\sigma=\lvert E_0\rvert=4\), using the **total** energy of both pairs (per-pair would be 2).
- **ML phase budget.** \(\theta_{\max}=\pi/(2\cdot4)=\pi/8\) for both sweeps. *Spot check:* this matches exact diagonalization for both register starts.
- **Fixed time.** Fix \(t=t_\ast\) once. Then \(J_{\max}=\pi/(8t_\ast)\), and \(t_\ast\) is exactly the ML time of \(\sigma\) at \(J_{\max}\). Sweep \(J_j=J_{\max}(j-1)/19\), 20 equal steps including \(J=0\).
- **Why this works.** The 20 strengths give 20 distinct unitaries, and the ML bound is stated once for a state with finite ML time.
  - A per-strength \(t_{\rm ML}(J)\) would fix \(Jt\) and collapse the sweep, the same budget cancellation as in [procedural-share-mlpool.md](procedural-share-mlpool.md) §1.
  - Individual states can have infinite ML time. Under ZZ, \(\lvert11\rangle_A\lvert00\rangle_C\) is a ground state.
- **Range.** Over the window, \(\gamma=\sin^22\theta\in[0,\tfrac12]\). Full transfer (\(\gamma=1\), iSWAP) lies outside it. ML is evaluated on \(\sigma\) without the pool unitaries; this is recorded as a convention.

### 6.4 Priors and the Bell-weight minimum (resolved; spot-checked)

**Construction rule.**

1. Draw \(d_k\sim\mathrm{Dirichlet}(1,1,1,1,1)\), \(k=1,\dots,20\), with `numpy.random.default_rng(20261126)` (one call, `size=20`). The order of the coordinates is \((\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle,\lvert\Phi^+\rangle)\).
2. Set \(\pi_k=(1-w_{\min})\,d_k+w_{\min}\,e_{\Phi^+}\), with \(w_{\min}=0.10\).

This affine map keeps the Dirichlet draw's diversity and guarantees every prior a Bell weight of at least 0.10.

**Why a floor is needed.** On basis-only priors, the register records for different inputs are orthogonal given the outcome, so \(\kappa=H(X\mid Y)\) exactly. That is the export-bookkeeping equality. *Spot check:* \(\lvert\kappa-H(X\mid Y)\rvert\le7\times10^{-16}\) at all four test \(\theta\) values, with no pool unitary.

**Why 0.10** (spot check). The worst case is no pool unitary, Sweep P, at \(\theta\in\{\pi/32,\pi/16,3\pi/32,\pi/8\}\).

| \(w_{\min}\) | Bell weight range | \(H(X)\) range (bits) | min gap \(H(X\mid Y)-\kappa\) over priors and \(\theta\) | min relative gap |
|---|---|---|---|---|
| 0 (plain Dirichlet) | 0.009–0.595 | 0.763–2.221 | 0.054 | 4.4% |
| 0.05 | 0.059–0.616 | 0.897–2.272 | 0.191 | 13.6% |
| **0.10** | **0.108–0.636** | **1.001–2.295** | **0.268** | **17.7%** |
| 0.20 | 0.207–0.676 | 1.141–2.282 | 0.354 | 21.8% |
| 0.30 | 0.306–0.717 | 1.214–2.206 | 0.352 | 23.3% |

- \(w_{\min}=0.10\) raises the worst-case margin about fivefold over the plain draw (0.268 vs 0.054 bits), at a small cost to the spread of \(H(X)\). Larger floors add little margin and narrow the spread.
- With pool unitaries the gap is larger: at least 0.49 bits at \(\theta=\pi/8\) for the three pool members checked (relative gap at least 31%), because rotated inputs no longer leave orthogonal register records.
- At \(\theta=\pi/8\) with the chosen priors and no pool unitary, \(\kappa\) ranges over 0.315–1.327 bits across priors (0.239–0.730 in Sweep M).

**Re-verified \(\pi/8\) figures.**

- **Total-variation shift of 0.750.** This is the largest change in the output law across the five inputs, compared with \(\theta=0\). It refers to register \(\lvert00\rangle\) (Sweep P), no pool unitary, and is attained at input \(\lvert11\rangle\), where \(\gamma=\tfrac12\). It does not depend on the prior.
- **Cost of 1.329** (1.328890). This is the **ensemble** value: register \(\lvert00\rangle\), uniform prior over the five inputs, no pool unitary. It is the same as \(I(X;C\mid O)\), since the start is pure. It was never a per-input number; the per-input \(S(C)-I(C;O)\) is 0 at every input.
- **Under the adopted design** at \(\pi/8\), the cost conditioned on a pool member, \(I(X;C\mid O,F{=}f)\), lies in 0.315–1.327 (no pool unitary) and 0.443–1.304 (pool member 0) across the 20 priors.
- **Where the six-decimal match comes from.** The GAD match was checked separately, with the \(\mathrm{diag}(0.7311,0.2689)\) register (§1). It is not what produced the 0.750 or the 1.329.

### 6.5 Remaining open risks

- **Tautology cap.** \(\kappa\le H(X\mid O,F)\le H(X\mid Y)\). The cost is still bounded by the export term (prior art; independent convergence), and the Bell floor only breaks the equality.
  - *Spot check:* across the 20 adopted priors, a linear fit of \(\kappa\) on \(H(X\mid Y)\), \(H(X)\) and \(H(Y)\) already gives \(R^2\) = 0.85–0.93 (Sweep P, no pool unitary) and 0.89–0.97 (pool member 0) over the four test \(\theta\). For Sweep M it gives 0.36–0.96.
  - So the cost is largely, though not exactly, predicted by the classical law. Control 2 may come close to its locked \(R^2\ge0.95\) line (§4).
- **The 2-bit cap and pool independence.** \(\kappa\le2\) bits. It is an average over pool members and does not grow with \(\lvert\text{pool}\rvert\), whereas \(D\) contains \(\log_2\lvert\text{pool}\rvert\). So the Stage 1 §8 cap argument and the [PAPER_PLAN.md](https://github.com/cyotee/computational-entropy/blob/master/PAPER_PLAN.md) §4 revisit condition (a term that grows with the pool) are still not met. This design tests correlation, not coverage of \(D\).
- **Shared drivers across priors.** The priors move \(H(X)\), which feeds both \(\kappa\) (through its cap) and \(D\) (through \(H(Y)\) and \(H(Y\mid X)\)). Control 1 includes \(H(X)\) for this reason.
- **Scope of the Bell-floor evidence.** The floor was spot-checked at four \(\theta\) values, with no pool unitary and three pool members, not over the whole pool.
- **Placement.** [PAPER_PLAN.md](https://github.com/cyotee/computational-entropy/blob/master/PAPER_PLAN.md) §2 keeps channel-cost research parallel to the paper, not a dependency of it. Whether Stage 3 belongs in the paper's methods section is open.
  - If it does, one option is to describe it as a pre-registered sequential design: Sweep P is primary and binding; Sweep M is a conditional secondary analysis with its trigger (the 10–14 band) stated in advance; and both are reported whenever run.

## 7. Pre-registration items (to be recorded before the first run)

Items 1, 5 and 7 were updated by Amendment 1.

1. **Energy convention:** total energy of both pairs (not per pair), on \(\sigma=\bar\rho_A\otimes\rho_{C,0}\); \(\theta_{\max}=\pi/8\); 20 equal steps including \(J=0\); \(t_\ast=1\) with \(\hbar=1\) and \(J\) in units of \(1/t_\ast\), so \(J_{\max}=\pi/8\) (**LOCKED**, Amendment 1).
2. **Priors:** \(K=20\); seed `20261126`; the rule \(\pi_k=0.9\,d_k+0.1\,e_{\Phi^+}\) with \(d_k\sim\mathrm{Dirichlet}(\mathbf 1)\).
3. **Bell-weight minimum:** \(w_{\min}=0.10\).
4. **Ambiguity band:** 10–14 of 20 (≥ 15 hit, ≤ 9 dead), with the undefined \(r\) at \(J=0\) counted as a non-hit.
5. **Sweep M:** \(p=0.7311\) (\(T=1\), **LOCKED**, Amendment 1); it runs only if Sweep P lands in 10–14 (Amendment 1). Still to record: how its outcome resolves an ambiguous Sweep P. Proposal: a Sweep M hit is reported as a conditional hit; anything else is dead.
6. **Pool (LOCKED):** the existing CE-15 Margolus–Levitin pool, 200 members, seed 2026, SHA-256 `d11fa3d1ec4594b7d1235759fde33b8b98689646b44efd163fffba97084618e2`. No new pool.
7. **Controls:** sufficiency tolerance **LOCKED** at \(R^2\ge0.95\) for the linear fit on \(H(X\mid Y)\), \(H(X)\), \(H(Y)\) (flag as potentially definitional); partial-correlation critical value **0.412** (df = 15); carry rule **LOCKED**: a flagged hit stands only if \(r(\kappa_{\rm shuf}(\theta_j)-\kappa_{\rm shuf}(0),\,D(\theta_j))<0.412\) across the 20 priors (cost-level baseline; undefined means it does not stand); control 4 seed **LOCKED** at `202611264` (scheme in §4); control 3 dephasing basis **LOCKED** as the register's computational basis (Amendment 1).
8. **Bell state:** \(\lvert\Phi^+\rangle\).

## 8. Spot checks used in this design

Scratch only and not committed: exact 16×16 linear algebra at \(\theta\in\{0,\pi/32,\pi/16,3\pi/32,\pi/8\}\) (plus \(\pi/4\) in an earlier ZZ-draft review), no sweep. The script loads the saved CE-15 pool read-only. These numbers check the derivations above; they are not results of the experiment, which has not been run.

## 9. Scope

Tier 2 only: a four-qubit toy with one coupling, one readout and five input states under 20 priors. Nothing here bears on gravity, black holes or QCD. The Boltzmann–Shannon unification programme is not advanced or tested by this design beyond the information-theoretic bookkeeping above. No committed simulation output exists for this stage. Once run, the results will be reported against §4 as written here, including a null.
