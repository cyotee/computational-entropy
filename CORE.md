# CORE — Tier 1: channel-level entropy (the primary result)

**Status:** 2026-11-26 · Preliminary research · three-tier restructure  
**Tier:** 1 of 3. This is the primary result: computational entropy offered as a **proposed mathematical object for consideration**, with no GR-level certainty and no connection to physics beyond the standard Landauer bound. Tier 2 (secondary, finite-substrate instruction persistence) is in [TIER2_INSTRUCTION_PERSISTENCE.md](https://github.com/cyotee/computational-entropy/blob/master/TIER2_INSTRUCTION_PERSISTENCE.md). Tier 3 holds all conjectural extensions and lives in [README](https://github.com/cyotee/computational-entropy/blob/master/README.md#tier-3-conjecture) and [THEORY](https://github.com/cyotee/computational-entropy/blob/master/THEORY.md#tier-3-conjecture), not here.  
**Scope:** classical, finite (or countable) alphabets unless stated.
**Rule for this file:** every equation below either appears in the cited repo file or follows from one by a one-line derivation shown inline. Every numerical value is reproduced by the cited script. Anything not backed in this way is marked **open** or **conjecture**.

> **Author's note on standing.** The author has no credentials or formal training in information theory or statistical mechanics. For that reason every claim here is tied to an explicit derivation or computation in this repository, and standard results are attributed to their sources rather than presented as new.

---

## 1. Motivation: a Boltzmann–Shannon unification

The driving intent of this programme is a **Boltzmann–Shannon unification**: one notion of entropy that reads, on the same object, both as Shannon's measure of uncertainty about a signal and as Boltzmann's logarithmic count of the microstates compatible with what is observed. Shannon entropy is normally attached to a *static* distribution (a source, or a received signal). It says nothing about what a computation *does* to random inputs. Boltzmann's entropy \(S = k_B \ln W\) is attached to a *macrostate* through the number \(W\) of microstates compatible with it.

The mathematical object proposed to serve this intent is **entropy defined on a channel's action on its input distribution**, rather than on a static distribution. The object is the pair (channel, input law). An output value \(y\) then plays the role of a macrostate, and its preimage plays the role of the compatible microstates (§2.3). Section 5 says plainly how much of this is already standard and what remains open.

---

## 2. Definition

### 2.1 The object

Let \(X \sim p_X\) be an input random variable on a finite set \(\mathcal X\). Let \(f\) be a **channel**: a conditional law \(p(y\mid x)\). A **deterministic map** \(Y = f(X)\) is the special case \(p(y\mid x) \in \{0,1\}\). The channel acting on \(p_X\) induces the joint law \(p_{XY}(x,y) = p_X(x)\,p(y\mid x)\) and the output law \(p_Y\).

*Source:* [Paper A §1](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#1-definition), [Paper A Thm 1](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#3-the-export-identity-a3).

### 2.2 Channel-level entropy: output entropy and export

**Definition 1 (computational entropy).** The computational entropy of \(f\) on \(p_X\) is the Shannon entropy of the induced output law:

$$
H_c(f;p_X) := H(Y) = -\sum_y p_Y(y)\log_2 p_Y(y).
$$

**Definition 2 (export).** The **export** of \(f\) on \(p_X\) is the conditional entropy of the input given the output:

$$
\mathrm{Exp}(f;p_X) := H(X\mid Y).
$$

Paper A writes the single-shot export slot as \(L_S := H(X\mid Y)\). This is the same quantity under a ledger name.

**Identity (corrected Paper A Theorem 1, any channel).**

$$
H(X) - H(Y) = H(X\mid Y) - H(Y\mid X).
$$

For a deterministic map \(H(Y\mid X) = 0\), so

$$
H(X) - H_c(f;p_X) = H(X\mid Y) = \mathrm{Exp}(f;p_X).
$$

For a stochastic channel the visible drop \(H(X) - H(Y)\) is the export minus the channel noise \(H(Y\mid X)\), and it can be negative. The export \(H(X\mid Y)\) is well defined in both cases.

The channel-level entropy of \((f, p_X)\) is this pair of numbers, \(\big(H_c(f;p_X),\ \mathrm{Exp}(f;p_X)\big)\), together with the identity linking them. Both are functions of the channel *and* the input law, not of a single static distribution.

*Sources:* [Paper A §1, §3](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#3-the-export-identity-a3) and [`synthesis/m11d-composition-laws.md`](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11d-composition-laws.md) Lemma A.

> Paper A §1 also writes a non-classical form of the definition. No theorem in Papers A or C uses it, and it is not part of Tier 1 (see Tier 3).

### 2.3 The Boltzmann-form reading (uniform inputs, deterministic maps)

Let \(X\) be uniform on \(\mathcal X\), with \(|\mathcal X| = N\), and let \(Y = f(X)\) be deterministic. Write \(W_y := |f^{-1}(y)|\) for the number of inputs compatible with output \(y\). Given \(Y = y\), \(X\) is uniform on \(f^{-1}(y)\). So

$$
H(X\mid Y) = \sum_y p_Y(y)\,\log_2 W_y
$$

([Paper C §2](https://github.com/cyotee/computational-entropy/blob/master/papers/02-computational-models/PAPER_C_decay_algebra.md#2-the-decay-vector-bounds-export-exact-for-product-maps)), and \(k_B\ln 2\cdot H(X\mid Y=y) = k_B \ln W_y\) has Boltzmann's form with macrostate \(y\).

*One-line derivation of the split.* Since \(p_Y(y) = W_y/N\), we get \(H(Y) = -\sum_y \tfrac{W_y}{N}\log_2\tfrac{W_y}{N} = \log_2 N - \sum_y p_Y(y)\log_2 W_y\). Hence

$$
\underbrace{\log_2 N}_{H(X)} \;=\; \underbrace{H(Y)}_{\text{Shannon, output}} \;+\; \underbrace{\textstyle\sum_y p_Y(y)\log_2 W_y}_{\text{Boltzmann-form, mean log preimage count}}.
$$

This is the deterministic case of the identity in §2.2, specialised to uniform inputs. **Status: standard.** It is the grouping (recursivity) property of Shannon entropy, and it is a *formal* correspondence only. Nothing in the repo identifies \(W_y\) with a physical microstate count (see §5).

---

## 3. Results, with proofs or exact pointers

| # | Statement | Proof / pointer | Reproduction |
|---|-----------|-----------------|--------------|
| **P1** (informational equivalence) | **Definition:** \(f\) and \(g\) are *informationally equivalent* on \(p_X\) iff they induce the same output law \(p_Y\). Then \(H_c(f;p_X) = H_c(g;p_X)\), and every probability functional of the output agrees. **The converse fails:** equal \(H_c\) does not imply equal law. | Immediate: \(H_c\) is a functional of \(p_Y\). [Paper A §1.1](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#11-informational-equivalence-a2); canonical definition, Key Property and Note ([`foundations/computational-entropy/definition.md`](https://github.com/cyotee/computational-entropy/blob/master/foundations/computational-entropy/definition.md)); pitfall 1 in [`AGENTS.md`](https://github.com/cyotee/computational-entropy/blob/master/AGENTS.md) | \(\sqrt U\) and \(\max(U_1,U_2)\) share the density \(2y\) on \([0,1]\): mean \(2/3\), \(P(Y>0.7)=0.51\), variance \(1/18\), \(h_c = -1 + \tfrac{1}{2\ln 2}\approx -0.27865\) bits. \(\min(U_1,U_2)\) has the same \(h_c\) and the same variance \(1/18\), but density \(2(1-y)\), mean \(1/3\) and \(P(Y>0.7)=0.09\), so it is **not** equivalent (differential entropy is illustrative only) |
| **T1** (export identity, any channel) | \(H(X) - H(Y) = H(X\mid Y) - H(Y\mid X)\). Reduces to \(H(X\mid Y)\) when deterministic. | Chain rule on \(p_{XY}\) in both orders: \(H(X,Y) = H(X) + H(Y\mid X) = H(Y) + H(X\mid Y)\); rearrange. [Paper A Thm 1](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#3-the-export-identity-a3) | `simulations/classical/m11_and_gate_ledger.py`: AND gate \(H(X) = 2\), \(H(Y) = 0.811278\), export \(1.188722\), chain error \(<10^{-12}\) |
| **T2** (Landauer coincidence, deterministic maps) | \(Q \ge kT\ln 2\cdot H(X\mid Y)\). Export equals the Landauer erased-bit count. For stochastic channels the generalized bound charges \(H(X) - H(Y) = H(X\mid Y) - H(Y\mid X)\), so export is an upper bound on the charge. | **External theorem**, not re-proved in the repo. [Paper A Thm 2](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#4-landauer-exactness-a4), [`synthesis/m11e-landauer-export.md`](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11e-landauer-export.md) §3 | `simulations/classical/m11_landauer_and_ledger.py` (AND: \(Q \ge 1.188722\,kT\ln 2\)) |
| **T3** (stage-wise ledger is path-dependent: a *convention*) | Under the stage-wise ledger (each stage charged \(H(\text{declared inputs}\mid\text{stage output})\), charges summed), two pipelines with the same overall map can have different \(\sum L_S\). The gap is an accounting quantity, **not** a heat difference. | Witness: direct AND \(\sum L_S = 1.188722\); circuit (\(Y = X_1\), then \(Z = Y\wedge X_2\)) \(\sum L_S = 2.188722\); gap \(1.000000\) bit. Minimum heat is \(1.188722\,kT\ln 2\) on both paths. [Paper A Thm 3](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#5-path-dependence-of-cumulative-export-a5), [m11d](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11d-composition-laws.md) Lemma E | `simulations/classical/m11_composition_ledger.py` |
| **L1** (composition along a pure cascade) | If \(Y = f(X)\) and \(Z = g(Y)\) are deterministic, then \(H(X\mid Z) = H(X\mid Y) + H(Y\mid Z)\), and \(H(Z)\le H(Y)\) (data processing). | T1 applied twice. [m11d](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11d-composition-laws.md) Lemmas B, C | `m11_composition_ledger.py` (\(Z = \mathrm{NOT}(Y)\) witness) |
| **P2** (invariant carrier) | \(I(X;Y) = H(Y) - H(Y\mid X) = D_{\mathrm{KL}}(p_{XY}\parallel p_Xp_Y)\). For deterministic \(f\), \(I(X;Y) = H_c\). Differential \(h\) is not reparameterization-invariant. | Standard identity. [Paper A §6](https://github.com/cyotee/computational-entropy/blob/master/papers/01-foundations/PAPER_A_computational_entropy.md#6-the-invariant-carrier-of-information-imparted-a6) | n/a |
| **D1** (decay-vector bound) | For uniform inputs, \(H(X\mid Y) = \sum_y p(y)\log_2 W_y \le \sum_y p(y)\,\#\{\text{unrecoverable coords of } y\}\), with equality iff every preimage is a product subcube. | One line: \(f^{-1}(y)\) lies inside the subcube spanned by its unrecoverable coordinates, so \(W_y \le 2^{\#\text{unrecoverable}}\), with equality iff it fills that subcube. [Paper C §2](https://github.com/cyotee/computational-entropy/blob/master/papers/02-computational-models/PAPER_C_decay_algebra.md#2-the-decay-vector-bounds-export-exact-for-product-maps) | `simulations/classical/m11_idem_export_density.py` (AND(2): exact 1.18872 vs bound 1.5) |
| **C1** (1D density theorem) | For \(Y_i = b_i\wedge b_{i+1}\) on i.i.d. fair bits, the export density \(a = \lim_k E(k)/k\) exists and equals \(1 - h_Y\). The belief filter is a run-length chain with \(\pi_{r+1} = (1-\pi_r)/(2-\pi_r)\) and fixed point \(\pi^\star = (3-\sqrt5)/2\), giving \(a = 0.3007568\). | [Paper C Thm 1](https://github.com/cyotee/computational-entropy/blob/master/papers/02-computational-models/PAPER_C_decay_algebra.md#3-the-decay-algebra-and-the-1d-density-theorem); full proof in [`synthesis/m11f-decay-algebra-theorem.md`](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11f-decay-algebra-theorem.md) Lemmas 1–3, §5 | `simulations/classical/m11_decay_algebra.py` (\(a(R{=}200) = a(R{=}800) = 0.300756796612\); matches \(O(2^k)\) enumeration) |
| **C2** (general window \(w\), any gate) | (i) Existence: \((Y_i)\) is \((w-1)\)-dependent, so \(a = 1 - h_Y\) exists with \(E(k) = ak + O(1)\). (ii) Blackwell representation \(h_Y = \mathbb E_{\mu^\star}[H(Y\mid\pi)]\). (iii) Reset gates (some output with a singleton preimage) regenerate, so the algebra is exactly finite (renewal-reward). The converse is **open**. | [Paper C Thm 2](https://github.com/cyotee/computational-entropy/blob/master/papers/02-computational-models/PAPER_C_decay_algebra.md#4-general-w-theorem-any-gate-and-the-reset-dichotomy); [`synthesis/m11g-decay-algebra-general-w-theorem.md`](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11g-decay-algebra-general-w-theorem.md) Theorems 1–3, Corollary | `simulations/classical/m11_decay_algebra_general.py` (AND \(w = 2,3,4\): 0.30076 / 0.56568 / 0.74503; asserts exact ⇔ singleton preimage on the tested gates) |
| **C3** (2D strip; continuum field) | 2D density exists (proved, finite dependence). Strip-width convergence is **numerical**. Continuum field \(\sigma(x) = a(\theta(x)) = h_2(\theta(x)) - h_Y(\theta(x))\) at rate \(O(1/N)\) is **witnessed, not proved** (general theorem open). | [Paper C §5–§6](https://github.com/cyotee/computational-entropy/blob/master/papers/02-computational-models/PAPER_C_decay_algebra.md#5-2d-strip-transfer); [m11h](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11h-decay-algebra-2d.md), [m11i](https://github.com/cyotee/computational-entropy/blob/master/synthesis/m11i-continuum-embedding.md) | `m11_decay_algebra_2d.py`, `m11_continuum_embedding.py` (\(\int_0^1\sigma\,dx = 0.29937\) for \(\theta(x) = 0.35 + 0.30x\)) |

---

## 4. Genuinely new vs standard

Classification is the author's own, made conservatively. "Candidate" means the repo proves or computes the result, but **no systematic literature search has been done**. Any of these may already be known.

| GENUINELY NEW (candidates) | STANDARD (attributed) |
|----------------------------|-----------------------|
| **Framing** (candidate, not a theorem): the channel–input pair \((f,p_X)\) as the object, with output entropy and export \(H(X\mid Y)\) as its paired quantities, offered for a Boltzmann–Shannon unification. Nothing here claims \(H(X\mid Y)\) is a new principle. | **Conditional entropy \(H(X\mid Y)\) as the information loss of a map** is standard and already characterized: Baez, Fritz & Leinster, *Entropy* 13(11):1945–1957 (2011); Fullwood & Parzygnat, *Entropy* 23(8):1021 (2021). See §4.1. |
| **Composition rules and path accounting as a framework** (candidate): the stage-wise export ledger, its explicit non-functoriality, and the exact corrected statement that its path gap is accounting, not heat (Paper A Thm 3; m11d). The *identities* used (chain rule, cascade additivity, data processing) are standard; see the right column. | **Chain rule, cascade additivity, data processing** (T1, L1): Shannon (1948); Cover & Thomas ch. 2. |
| **Tier 2 resource-bound conjecture** (candidate research avenue, **unproved**): the log-cardinality \(d_f^{\#} = \log_2\lvert[f]\rvert\) of an observational equivalence class, read as a finite substrate's obligation to keep the next computation reconstructable, and the open joint minimum of output capacity plus instruction persistence ([TIER2_INSTRUCTION_PERSISTENCE.md](https://github.com/cyotee/computational-entropy/blob/master/TIER2_INSTRUCTION_PERSISTENCE.md)). | **Type-class counting** (\(\lvert[f]\rvert\) is a multinomial, \(\approx 2^{N H(Y)}\)): Boltzmann's combinatorial entropy; the method of types (Csiszár & Körner; Cover & Thomas ch. 11). Kolmogorov complexity and the invariance theorem, Bennett's logical depth, Toffoli-gate universality and Shannon's 1956 small universal machine are background (Tier 2 §4). |
| **C1**: closed-form export density \(a = 1 - h_Y = 0.3007568\) for the 1D nearest-neighbour AND lattice, via the run-length belief chain with \(\pi^\star = (3-\sqrt5)/2\) (Paper C Thm 1; m11f). The *method* is standard (entropy rate of a function of a Markov chain); the specific constant and derivation are the candidate. | **Shannon entropy, conditional entropy, chain rule**, and the two-sided form \(H(X) - H(Y) = H(X\mid Y) - H(Y\mid X)\) (T1). Shannon (1948); any textbook, e.g. Cover & Thomas, *Elements of Information Theory*, ch. 2. |
| **C2(iii)** + corollary: *reset gates* (a singleton-preimage, fully-recoverable decay branch) make the belief-transfer algebra exactly finite (renewal-reward), linking a single gate's IDEM decay vector to finite exactness of the composed algebra (Paper C Thm 2; m11g). Converse open. | **Export = information loss of a map.** For deterministic (measure-preserving) maps, \(H(X\mid f(X))\) is the unique (up to scale) information-loss measure that is functorial, convex-linear and continuous: Baez, Fritz & Leinster, *Entropy* 13 (2011) 1945. Stochastic extension, recovering conditional entropy: Fullwood & Parzygnat, *Entropy* 23 (2021) 1021. |
| **C2(i)** general-\(w\) existence, listed as a candidate *only as part of the C2 package*. Taken alone, existence follows from standard ergodic theory (finite dependence ⇒ stationary ergodic ⇒ Shannon–McMillan–Breiman). | **Landauer bound** \(Q \ge kT\ln2\cdot(\text{bits erased})\) (T2): Landauer (1961); Bennett (1982; 2003). **Generalized (Shannon-entropy) Landauer bound** for stochastic / information-processing operations: Sagawa & Ueda, PRL 102, 250602 (2009); Sagawa, J. Stat. Mech. (2014) P03025. |
| **D1** as a *framing*: the IDEM decay vector as an export bound that is exact iff preimages are product subcubes (Paper C §2). The mathematics is a one-line counting bound. | **Blackwell representation** of the entropy rate of a function of a Markov chain (C2(ii)): Blackwell (1957). **Renewal-reward theorem** (C2(iii) machinery). **Shannon–McMillan–Breiman** (C1, C2(i)). |
| **C3**: 2D strip-transfer numbers and the continuum density field \(\sigma(x)\). **Witnessed / numerical**, not theorems (general hydrodynamic theorem open). | **Data processing; composition along a Markov cascade** (L1); **mutual information as the invariant carrier** (P2); **non-invariance of differential entropy**: Cover & Thomas, ch. 2 and 8. |
| — | **Boltzmann-form split** under uniform inputs (§2.3): the grouping property of Shannon entropy (Shannon 1948). Formal correspondence only. |

**The path gap itself is a convention, not a physical result.** The path-dependent stage-wise export ledger (T3) is a property of the ledger *convention*. The framework is offered as a candidate (above), but its 1-bit gap carries no heat. Per the corrected Theorem 3, its 1-bit gap is not a heat difference. When the circuit is written as a composable chain of maps, the stage charges obey ordinary additivity: \((X_1,X_2)\mapsto(X_1,X_2)\) is a bijection (loss \(0\)), and \((X_1,X_2)\mapsto Z\) has loss \(H(X\mid Z) = 1.188722\), so the total equals the direct path (L1). The extra bit appears only because the ledger conditions stage 1 on the declared output \(X_1\) alone. That makes it non-functorial, so by Baez–Fritz–Leinster it cannot be a function of the composite map.

**Definitions are not results.** Definitions 1–2 name standard Shannon functionals of \(p_{XY}\). The *framing* (taking the channel–input pair as the object and calling \(H(X\mid Y)\) export) is the programme's choice, not a theorem.

### 4.1 Relation to prior work: independent convergence (added 2026-11-26)

The dates below are git author dates on `origin/master`. The author controls these dates, so they are the repository's record, not proof of when ideas were conceived.

- The first commit is `1eeec0e` (2025-05-03), with initial drafts in `2ff2ad3` the same day.
- Conditional entropy first appears in `b44b154` (2025-05-04, "second drafts") as \(H(S\mid O)\), used for secret-hiding in the lambda-calculus drafts, not yet as a channel's information loss.
- \(H(X\mid Y)\) first appears in the channel-level / export sense in `dd43fbe` (2026-07-17). Paper A was drafted in `ef60077` (2026-07-29).
- The published characterizations are Baez, Fritz & Leinster, "A characterization of entropy in terms of information loss," *Entropy* 13(11):1945–1957 (2011), arXiv:1106.1791; and Fullwood & Parzygnat, "The information loss of a stochastic map," *Entropy* 23(8):1021 (2021), arXiv:2107.01975.
- A search of the `origin/master` history through `378e51c` (2026-11-26) with `git log -S'Baez'`, `-S'Fullwood'`, `-S'Leinster'` and `-S'Parzygnat'` finds no citation of either work. The first citation is this restructure (2026-11-26).

**Reading.** This work postdates both papers by years. It is **not** a priority claim, and it is **not** a contemporaneous replication. It is *independent convergence*: the repository reached \(H(X\mid Y)\) as the channel-level loss quantity by its own route (lambda-calculus and computation drafts), without citing that literature at the time. The published characterization theorems corroborate that this choice of quantity is the canonical one. The repo history shows no citation of these works before 2026-11-26. No stronger claim of independence is made.

---

## 5. Is this more than Shannon entropy?

**What is established.**

1. Every core quantity (\(H_c\), export, T1, T2, L1, P2) is a Shannon functional of the joint law \(p_{XY} = p_X\,p(y\mid x)\). In that precise sense the core, *as currently stated*, **is Shannon entropy applied to a channel acting on an input law**. It is not a new entropy.
2. For deterministic maps, any information-loss measure satisfying functoriality, convex linearity and continuity must be a multiple of \(H(X\mid f(X))\) (Baez–Fritz–Leinster 2011). The stochastic case is treated by Fullwood–Parzygnat (2021). So entropy defined on a map's action has already been characterized, and the answer is conditional entropy.
3. The thermodynamic reading (T2) is an imported external theorem (Landauer / Bennett / Sagawa). The repo instantiates it on finite examples; it does not derive it.
4. What the repo does add is (a) a consistent bookkeeping framing with exact finite witnesses, and (b) the Paper C decay-algebra computations (C1, C2(iii), and the numerics in C3), which are candidates for new results subject to a literature check.

**What is not established.**

- **No separation theorem.** The repo contains no quantity, defined on the channel–input pair, that is provably *not* a functional of \(p_{XY}\) and still has an operational or physical meaning. No such claim should be made.
- **No physical Boltzmann identification.** The split in §2.3 is a formal identity. The repo does not show that \(W_y\) counts physical microstates of any system, or that \(k_B\ln 2\cdot H(X\mid Y)\) is a thermodynamic entropy change beyond what the external Landauer theorem already gives.
- The stage-wise ledger (T3) is not functorial, but it has **no established operational meaning**: by the corrected Theorem 3 its gap carries no heat.

**What would need to be proved (open problems).**

- **OP1 (separation).** Define a channel-level quantity \(Q(f, p_X, \mathcal F)\) that depends on more than \(p_{XY}\) (for example on a factorization \(\mathcal F\) of \(f\) into stages). Prove an operational theorem for it, such as a bound on dissipated heat for an explicitly specified class of physical implementations that is strictly tighter than \(kT\ln2\cdot H(X\mid Z)\) on some instance. Baez–Fritz–Leinster imply such a \(Q\) must give up functoriality, convex linearity or continuity. The theorem would have to say which one, and why that is physically natural.
- **OP2 (Boltzmann–Shannon unification proper).** For an explicit physical model, with stated equilibrium hypotheses, prove that the preimage count \(W_y\) is the thermodynamic microstate count of a macrostate. Then \(k_B\ln W_y\) is Boltzmann's entropy *by derivation*, not by formal analogy, and the §2.3 split becomes a physical statement.
- **OP3 (decay algebra).** Do a literature search on entropy rates of sliding-block / hidden-Markov factors to settle the novelty of C1–C2. Prove the converse of C2(iii) (non-reset ⇒ non-atomic \(\mu^\star\)). Prove a general hydrodynamic theorem for \(\sigma(x)\) (C3).

- **OP4 (Tier 2).** A separate finite-substrate question is the joint minimum of output capacity plus instruction persistence, built on the log-cardinality \(d_f^{\#}\). It is posed as a research avenue in [TIER2_INSTRUCTION_PERSISTENCE.md](https://github.com/cyotee/computational-entropy/blob/master/TIER2_INSTRUCTION_PERSISTENCE.md) and is **not** a Tier 1 result.

Until one of OP1–OP2 is proved, the honest one-line summary is: **channel-level entropy is a reorganization of standard Shannon quantities around a channel acting on an input law. It is offered as the mathematical object for a Boltzmann–Shannon unification, and that unification remains a research motivation, not a result.**

---

## 6. Reproduce the core

```bash
.venv/bin/python simulations/classical/m11_and_gate_ledger.py       # T1: H(Y)=0.811278, export=1.188722
.venv/bin/python simulations/classical/m11_landauer_and_ledger.py   # T2: export = Landauer erased bits (AND)
.venv/bin/python simulations/classical/m11_composition_ledger.py    # T3, L1: ΣL_S 1.188722 vs 2.188722
.venv/bin/python simulations/classical/m11_idem_export_density.py   # D1: decay bound, exact for product maps
.venv/bin/python simulations/classical/m11_decay_algebra.py         # C1: a = 0.3007568, π* = (3-√5)/2
.venv/bin/python simulations/classical/m11_decay_algebra_general.py # C2: general w; exact ⇔ reset
.venv/bin/python simulations/classical/m11_decay_algebra_2d.py      # C3: 2D strip
.venv/bin/python simulations/classical/m11_continuum_embedding.py   # C3: σ(x), O(1/N)
```

---

## 7. References (standard results cited above)

- C. E. Shannon, "A mathematical theory of communication," *Bell Syst. Tech. J.* 27 (1948).
- T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley (2006).
- R. Landauer, "Irreversibility and heat generation in the computing process," *IBM J. Res. Dev.* 5, 183 (1961).
- C. H. Bennett, "The thermodynamics of computation — a review," *Int. J. Theor. Phys.* 21, 905 (1982).
- C. H. Bennett, "Notes on Landauer's principle, reversible computation, and Maxwell's Demon," *Stud. Hist. Phil. Mod. Phys.* 34, 501 (2003).
- T. Sagawa and M. Ueda, "Minimal energy cost for thermodynamic information processing: measurement and information erasure," *Phys. Rev. Lett.* 102, 250602 (2009).
- T. Sagawa, "Thermodynamic and logical reversibilities revisited," *J. Stat. Mech.* (2014) P03025.
- J. C. Baez, T. Fritz and T. Leinster, "A characterization of entropy in terms of information loss," *Entropy* 13(11), 1945–1957 (2011); arXiv:1106.1791.
- J. Fullwood and A. J. Parzygnat, "The information loss of a stochastic map," *Entropy* 23(8), 1021 (2021); arXiv:2107.01975.
- D. Blackwell, "The entropy of functions of finite-state Markov chains," *Trans. First Prague Conf. Inf. Theory* (1957).

---

*Edit this file when a Tier 1 theorem, its proof location, or its classification changes. Tier 2 material belongs in TIER2_INSTRUCTION_PERSISTENCE.md, and Tier 3 (conjecture) material belongs in README/THEORY, not here.*
