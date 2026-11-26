# Tier 2 — Instruction persistence on a finite substrate (research avenue)

**Tier:** 2 of 3 (secondary result, a research avenue). It makes **no gravitational and no quantum claims**. It rests on the Tier 1 definitions in [CORE.md](https://github.com/cyotee/computational-entropy/blob/master/CORE.md).  
**Status:** 2026-11-26 · Preliminary research. One counting identity and one exact chain rule are proved below. The hypothesis and the conjecture are **unproved** and labelled as such.  
**Script:** `simulations/classical/tier2_instruction_persistence.py` (exact integer arithmetic; runs in under a second).

---

## 1. Question and hypothesis

Tier 1 measures what a channel does to its input law. Tier 2 asks what a **finite substrate that is not free** must keep so that computation can continue: storage is bounded, and instructions occupy the same cells as data.

**Hypothesis H2 (the author's; informal, unproved).** When the substrate is finite and not free, a channel's output must encode not only the result but also the capability to compute *every* observationally equivalent function: the whole equivalence class, not one representative. The resulting quantity measures the **substrate's obligation to preserve reconstructability**, not an observer's ignorance.

## 2. Definition: log-cardinality function unidentifiability \(d_f^{\#}\)

Let \(X\) be uniform on a finite set \(\mathcal X\) with \(|\mathcal X| = N\), and let \(f:\mathcal X\to\mathcal Y\) be deterministic with fibre sizes \(W_y = |f^{-1}(y)|\).

- **Observational equivalence** uses the Tier 1 definition, which is law-based (CORE P1; canonical definition after commit `378e51c`; pitfall 1 in [AGENTS.md](https://github.com/cyotee/computational-entropy/blob/master/AGENTS.md)). We set \(g\sim f\) iff \(g_*p_X = f_*p_X\). Equal entropy is **not** enough.
- **Equivalence class.** \([f] := \{g:\mathcal X\to\mathcal Y \;:\; |g^{-1}(y)| = W_y\ \forall y\}\), and


$$
|[f]| = \frac{N!}{\prod_y W_y!}.
$$


  This is a one-line count: the number of ways to assign the \(N\) inputs to outputs with the prescribed fibre sizes.
- **Definition.**


$$
d_f^{\#} := \log_2 |[f]| \quad\text{(bits)}.
$$


**Relation to the legacy Bayesian \(d_f\).** The repo's original \(d_f\) is \(1 - P_{\max}\) of a Bayesian posterior over candidate functions ([`Defining d_f for Function Unidentifiability in Lambda Calculus.markdown`](https://github.com/cyotee/computational-entropy/blob/master/Defining%20d_f%20for%20Function%20Unidentifiability%20in%20Lambda%20Calculus.markdown); \(d_f\in[0,1]\) in `synthesis/m11-idem-to-load.md`). Take a uniform prior on all maps \(\mathcal X\to\mathcal Y\) and condition on the observed output law. The posterior is then uniform on \([f]\), so its Shannon entropy is exactly \(d_f^{\#}\), and the legacy measure is \(d_f = 1 - 2^{-d_f^{\#}}\) (one line, since \(P_{\max} = 1/|[f]|\)). The reframing drops the prior and the observer and keeps the count. The legacy \(d_f\) is not silently redefined: \(d_f^{\#}\) is a separate symbol.

**Type-class bounds (standard).** \(f\), read as the string \((f(x))_{x\in\mathcal X}\), has type \(W/N\), and \([f]\) is its type class. Hence


$$
N H(Y) - |\mathcal Y|\log_2(N+1) \;\le\; d_f^{\#} \;\le\; N H(Y),
$$


so \(d_f^{\#}/N \to H(Y) = H_c(f;p_X)\) when the type is held fixed and \(N\) grows. This is Boltzmann's combinatorial route to entropy and the method of types (Csiszár & Körner; Cover & Thomas Thm 11.1.3). **Standard**, not new.

## 3. Composition: exact chain rule, and when additivity holds

**Proposition (exact chain rule; proved).** Consider a pure cascade \(X\xrightarrow{f}Y\xrightarrow{g}Z\) with \(Z = g(Y)\) deterministic. Write \(V_z = \sum_{y\in g^{-1}(z)} W_y\). Then


$$
d_f^{\#} = d_{g\circ f}^{\#} + R(g\mid f),\qquad R(g\mid f) := \sum_z \log_2\frac{V_z!}{\prod_{y\in g^{-1}(z)} W_y!}\;\ge 0 .
$$


*Proof (one line).* \(\dfrac{N!}{\prod_y W_y!} = \dfrac{N!}{\prod_z V_z!}\cdot\prod_z \dfrac{V_z!}{\prod_{y\in g^{-1}(z)}W_y!}\); take \(\log_2\). \(\square\)

**Consequences.**
1. *Monotonicity.* \(d_{g\circ f}^{\#}\le d_f^{\#}\), with equality iff \(R(g\mid f)=0\). That happens iff every \(z\) has at most one \(y\) with \(W_y>0\) in its preimage, i.e. iff \(g\) is injective on the image of \(f\).
2. *Telescoping.* Along a cascade \(f_1, f_2, \dots, f_T\), \(d_{f_1}^{\#} = d_{F_T}^{\#} + \sum_{t=2}^{T} R(f_t\mid F_{t-1})\), where \(F_t = f_t\circ\cdots\circ f_1\). Additivity holds **exactly in this form**.
3. *Naive additivity fails.* \(d_{g\circ f}^{\#} = d_f^{\#} + d_g^{\#}\) is **false** in general. Witness (script, part B): \(f=\mathrm{id}\) on \(\{0,1\}^2\) and \(g=\mathrm{AND}\) give \(d_f^{\#} = \log_2 4! = 4.585\) and \(d_{g\circ f}^{\#} = 2.000\), while \(d_f^{\#}+d_g^{\#} = 6.585\).
4. *Asymptotics.* By the type bounds, \(R(g\mid f) = N\,[H(Y)-H(Z)] + O(|\mathcal Y|\log N) = N\,H(Y\mid Z) + O(|\mathcal Y|\log N)\). The chain rule is therefore the finite-\(N\) combinatorial form of \(H(Y) = H(Z) + H(Y\mid Z)\) (Tier 1 T1/L1).

The same section of the script checks the identity exactly for AND3 = \((x_1\wedge x_2, x_3)\mapsto\wedge\) (\(10.129 = 3.000 + 7.129\)) and XOR3 (\(11.299 = 6.129 + 5.170\)).

## 4. Background, cited

- **Kolmogorov complexity and the invariance theorem.** \(K_U(x)\le K_V(x) + c_{U,V}\) for universal machines \(U,V\) (Solomonoff 1964; Kolmogorov 1965; Chaitin 1966; Li & Vitányi). For a finite, computably given set \(S\), every \(x\in S\) has \(K(x\mid S)\le\log_2|S| + O(1)\), and at least a fraction \(1-2^{-c}\) of its members have \(K(x\mid S)\ge\log_2|S| - c\). So \(d_f^{\#}\) is the description length of a *typical* member of \([f]\) given the class. A *particular* simple member, such as AND, can have far smaller \(K\). The contrast between class-generic cost (\(d_f^{\#}\)) and representative cost (\(K(f)\)) is exactly what H2 is about.
- **Bennett's logical depth** (Bennett 1988) measures the running time of near-shortest programs, a time-like resource. \(d_f^{\#}\) is a pure count. A full persistence theory would have to say how the two trade off. That is open.
- **Toffoli-gate universality.** The Toffoli (controlled-controlled-NOT) gate is universal for reversible Boolean logic when constant ancilla inputs and garbage outputs are allowed (Toffoli 1980; Fredkin & Toffoli 1982). Ancilla-free NOT/CNOT/Toffoli synthesis and its one-ancilla limits are characterized by Shende, Prasad, Markov & Hayes (2003). Reversible time/space trade-offs (pebbling) are in Bennett (1989).
- **Shannon's 1956 question.** Shannon showed that a universal Turing machine can be built with only two internal states (at the cost of more tape symbols), and with two symbols (at the cost of more states). This established the state–symbol trade-off and opened the question of the smallest universal machine (Shannon 1956).

## 5. The gap, stated precisely

To the author's knowledge, the following *joint* minimum has not been posed in this form. The related literature above treats register width (ancillae), reversible space–time, program size, and universal-machine size **separately**.

**Problem T2 (joint minimum of output capacity and instruction persistence).** Fix \(n\), a gate set \(\mathcal G\) (NOT, CNOT, Toffoli), and a pipeline of maps \(f_1,\dots,f_T\) with \(F_t := f_t\circ\cdots\circ f_1:\{0,1\}^n\to\mathcal Y_t\), input uniform on \(\{0,1\}^n\).

A *finite-substrate realization* is a register of \(w\) bits that holds both data and the stored program. It is initialised to the input, zeros, and an encoded gate list \(\gamma_1,\dots,\gamma_m\in\mathcal G_w\), cut into \(T\) stages. After stage \(t\) the register must
- (i) hold \(F_t(x)\) on designated cells, and
- (ii) still hold, without outside input, the instructions for stages \(t+1,\dots,T\) and every data bit those stages read.

Let \(b_t\) be the number of live cells after stage \(t\). Determine


$$
B^\star(f_1,\dots,f_T;\mathcal G) := \min_{\text{realizations}}\ \max_t\ b_t,
$$


and its split \(b_t = \lceil\log_2|\mathrm{im}\,F_t|\rceil + P_t\) into **output capacity** (a pigeonhole lower bound, proved) and a **persistence overhead** \(P_t\).

**Counting lemma (proved, elementary).** Suppose the realization is *class-generic*: the same layout must serve every \(g\in[f_{t+1}]\), with the member selected by stored bits. Here the class ranges over maps \(g\) on \(\mathrm{im}\,F_t\), with equivalence judged by the induced law of \(g(F_t(X))\). The multinomial formula of §2 applies directly when \(F_t\) is a bijection; otherwise \(\lvert[f_{t+1}]\rvert\) is the corresponding finite count. Then \(P_t\ge\lceil d_{f_{t+1}}^{\#}\rceil\). By pigeonhole, \(|[f_{t+1}]|\) distinct members need that many distinct stored selections.

**Conjecture T2 (open).** On a finite, non-free substrate, the class-generic regime is the operative one. The minimum persistent storage needed to keep the next stage computable then scales with \(d^{\#}_{f_{t+1}}\), the class log-cardinality, and not with the description length \(K(f_{t+1})\) of one representative. *Counterpoint (stated so the conjecture can fail):* if the specific next function is fixed in advance, a stored program of length about \(K(f_{t+1})\) plus an invariance constant suffices. The conjecture is therefore exactly the claim that a finite, non-free substrate cannot assume this. Neither direction is proved.

## 6. Toy model (computed)

The script's part C searches the smallest instance: a single stage, \(n=2\), gates NOT/CNOT/Toffoli on \(w\in\{2,3,4\}\) lines, ancillas starting at 0, garbage allowed. For every one of the 16 two-input Boolean functions it reports the minimum gate count \(g_{\min}(w)\) and an illustrative joint cost


$$
J(w) = w + g_{\min}(w)\,\log_2 G_w + \log_2 w,
$$


that is, register width plus the bits needed to store the gate list and the output-line index. Here \(G_w\) is the number of NCT gate placements: \(G_2=4\), \(G_3=12\), \(G_4=28\).

| \(f\) | \(d_f^{\#}\) | \(g_{\min}\) at \(w=2,3,4\) | min \(w\) | \(J\) at \(w=2,3,4\) |
|---|---|---|---|---|
| \(x_1\) | 2.585 | 0, 0, 0 | 2 | 3.00, 4.58, 6.00 |
| XOR | 2.585 | 1, 1, 1 | 2 | 5.00, 8.17, 10.81 |
| XNOR | 2.585 | 2, 2, 2 | 2 | 7.00, 11.75, 15.61 |
| AND | 2.000 | –, 1, 1 | 3 | –, 8.17, 10.81 |
| NAND | 2.000 | –, 2, 2 | 3 | –, 11.75, 15.61 |
| OR | 2.000 | –, 3, 3 | 3 | –, 15.34, 20.42 |

Findings, all from the script:
- \(w=2\), with no ancilla, reaches exactly the 6 non-constant affine functions. All 16 are reachable at \(w=3\) (one ancilla).
- \(d_f^{\#}\) does **not** order the register requirement. XOR has \(d_f^{\#}=2.585\) and needs no ancilla; AND has \(d_f^{\#}=2.000\) and needs one. So a single-stage, representative-fixed realization is governed by nonlinearity and gate count, not by \(d_f^{\#}\). This is consistent with the counterpoint in Conjecture T2, and it says nothing yet about the class-generic regime.
- For three-input functions at \(w=3\) (no ancilla), 70 of the 256 functions appear on some line. MAJ3 needs 3 gates, XOR3 needs 2, and AND3 is not reachable.

\(J\) is one cost convention among many, not a proved bound.

## 7. Next steps (future work)

1. Extend the search to class-generic realizations, where the layout serves all of \([f]\) with stored selector bits, and to \(T\ge2\) stages. Then compare \(\max_t b_t\) against \(\lceil\log_2|\mathrm{im}\,F_t|\rceil + \lceil d^{\#}_{f_{t+1}}\rceil\).
2. Search \(n=3\) at \(w=4\) (about \(5\times10^8\) states, which needs a smarter search than plain BFS).
3. Handle stochastic channels: \([f]\) is then a continuum, and a measure-based replacement for \(\log|[f]|\) is needed.
4. Do a literature search on reversible synthesis with stored programs, to test the "to the author's knowledge" statement in §5.

## 8. Status and non-claims

| Statement | Status |
|---|---|
| \(\lvert[f]\rvert = N!/\prod W_y!\); type-class bounds; uniform-prior posterior entropy \(= d_f^{\#}\) | proved (one line) / standard; script part A |
| Exact chain rule \(d_f^{\#} = d^{\#}_{g\circ f} + R(g\mid f)\); monotonicity; telescoping | **proved**; script part B |
| \(d^{\#}_{g\circ f} = d_f^{\#} + d_g^{\#}\) | **false** in general (counterexample) |
| Counting lemma \(P_t\ge\lceil d^{\#}_{f_{t+1}}\rceil\) under class-genericity | proved (pigeonhole), conditional on the class-generic requirement |
| Hypothesis H2 / Conjecture T2 | **open** |
| Toy table (§6) | computed; illustrative cost convention |

**Non-claims.** \(d_f^{\#}\) is not a physical entropy, a heat bound, or a gravitational quantity. Problem T2 is a research avenue, not a result.

## References

- L. Boltzmann, "Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung …," *Wiener Berichte* 76, 373–435 (1877).
- I. Csiszár and J. Körner, *Information Theory: Coding Theorems for Discrete Memoryless Systems*, Academic Press (1981).
- T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley (2006), ch. 11.
- R. J. Solomonoff, "A formal theory of inductive inference," *Information and Control* 7, 1–22 and 224–254 (1964).
- A. N. Kolmogorov, "Three approaches to the quantitative definition of information," *Problems of Information Transmission* 1(1), 1–7 (1965).
- G. J. Chaitin, "On the length of programs for computing finite binary sequences," *J. ACM* 13(4), 547–569 (1966).
- M. Li and P. Vitányi, *An Introduction to Kolmogorov Complexity and Its Applications*, 3rd ed., Springer (2008).
- C. H. Bennett, "Logical depth and physical complexity," in R. Herken (ed.), *The Universal Turing Machine: A Half-Century Survey*, Oxford University Press (1988), 227–257.
- C. H. Bennett, "Time/space trade-offs for reversible computation," *SIAM J. Comput.* 18(4), 766–776 (1989).
- T. Toffoli, "Reversible computing," in *Automata, Languages and Programming (ICALP 1980)*, LNCS 85, Springer (1980), 632–644.
- E. Fredkin and T. Toffoli, "Conservative logic," *Int. J. Theor. Phys.* 21(3–4), 219–253 (1982).
- V. V. Shende, A. K. Prasad, I. L. Markov and J. P. Hayes, "Synthesis of reversible logic circuits," *IEEE Trans. CAD* 22(6), 710–722 (2003).
- C. E. Shannon, "A universal Turing machine with two internal states," in *Automata Studies*, Annals of Mathematics Studies 34, Princeton University Press (1956), 157–165.
