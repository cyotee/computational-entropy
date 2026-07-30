# M11g — General-\(w\) decay-algebra theorem (any gate, sliding window)

**M-id:** M11g · **Status:** **Theorem (proved)** — general window width \(w\), any Boolean gate
**Date:** 2026-07-30 · **Stance:** Preliminary research; finite/algorithmic rigor, **not** a continuum theorem.
**Generalizes:** [m11f-decay-algebra-theorem.md](m11f-decay-algebra-theorem.md) (\(w=2\), AND)
**Witness (numeric):** `simulations/classical/m11_decay_algebra_general.py`
**Depends on:** export identity (Paper A) · [OPEN_AVENUES.md](OPEN_AVENUES.md) O1

This note proves the range-\(r\) generalization we witnessed: for a sliding-window lattice of **any** Boolean gate, the coupled export density exists and is computed by the boundary-belief transfer operator; and it identifies *exactly* which gates make that operator finitely exact — the **reset gates**, via a regeneration/renewal-reward argument.

---

## 1. Setup

Fix a gate \(g:\{0,1\}^{w}\to\{0,1\}\). Bits \(b_0,b_1,\dots\) i.i.d. \(\mathrm{Bernoulli}(1/2)\). Sliding-window outputs


$$
Y_i \;=\; g(b_i,b_{i+1},\dots,b_{i+w-1}),\qquad i\ge 0 .
$$


With \(k\) outputs from \(n=k+w-1\) input bits, and \(Y\) a deterministic function of \(X=(b_0,\dots,b_{n-1})\),


$$
E(k) := H(X\mid Y_{0:k-1}) = n - H(Y_{0:k-1}),\qquad a := \lim_{k\to\infty}\frac{E(k)}{k}.
$$


**Hidden boundary state** \(s_i:=(b_i,\dots,b_{i+w-2})\in\{0,1\}^{w-1}\); fresh bit \(f_i:=b_{i+w-1}\). Then


$$
Y_i=g(s_i,f_i),\qquad s_{i+1}=(s_i[1{:}],\,f_i)\quad(\text{shift-append}).
$$


---

## 2. Theorem 1 — the density exists (all \(g\), all \(w\))

**Claim.** \(a\) exists and \(a=1-h_Y\), where \(h_Y=\lim_m H(Y_{0:m-1})/m\) is the output entropy rate; moreover \(E(k)=a\,k+O(1)\).

**Proof.** \(Y_i=g(b_i,\dots,b_{i+w-1})\) depends only on bits in the block \([i,i+w-1]\). Blocks of outputs \(\ge w\) apart use disjoint input bits, so \((Y_i)\) is **\((w-1)\)-dependent** — in particular stationary and strongly mixing, hence ergodic. Its entropy rate \(h_Y\) exists (Shannon–McMillan–Breiman, or directly by subadditivity), and finite dependence gives finite excess entropy \(H(Y_{0:k-1})-k\,h_Y = O(1)\). Since \(n/k=(k+w-1)/k\to 1\),


$$
\frac{E(k)}{k}=\frac{n}{k}-\frac{H(Y_{0:k-1})}{k}\xrightarrow{k\to\infty}1-h_Y=:a,\qquad E(k)=a k+O(1). \qquad\square
$$


*Rigor:* **proved** (finite-dependence + SMB). This already generalizes m11f's existence claim to every gate and width.

---

## 3. Theorem 2 — transfer-operator (Blackwell) representation of \(h_Y\)

Let \(\pi_i\in\Delta(\{0,1\}^{w-1})\) be the Bayesian filter \(\pi_i(s)=\Pr(s_i=s\mid Y_{0:i-1})\). Standard filtering gives the predictive law \(\Pr(Y_i=\cdot\mid Y_{0:i-1})=P_g(\cdot\mid\pi_i)\) and a deterministic update \(\pi_{i+1}=\Phi_{Y_i}(\pi_i)\), where \(\Phi_y\) is the (normalized) belief-transfer operator on the \(2^{w-1}\)-vertex simplex.

**Claim.** The belief process \((\pi_i)\) is a Markov chain on the simplex with a unique invariant (Blackwell) measure \(\mu^\star\), and


$$
h_Y \;=\; \int H\!\big(P_g(\cdot\mid\pi)\big)\,d\mu^\star(\pi)
\;=\; \mathbb{E}_{\mu^\star}\big[\,H(Y\mid\pi)\,\big].
$$


**Proof.** The filter is a sufficient statistic: \(H(Y_i\mid Y_{0:i-1})=\mathbb E\,[H(P_g(\cdot\mid\pi_i))]\). By \((w-1)\)-dependence the chain \((\pi_i)\) mixes and its law converges to the unique invariant \(\mu^\star\) (Blackwell 1957, *The entropy of functions of finite-state Markov chains*). Taking \(i\to\infty\) and using \(h_Y=\lim_i H(Y_i\mid Y_{0:i-1})\) gives the integral. \(\square\)

*Rigor:* **proved** (imported Blackwell theorem + sufficiency). This is precisely the general "decay algebra": propagate a belief over the boundary and average the emission entropy.

---

## 4. Theorem 3 — reset gates regenerate ⇒ exact renewal-reward

Call \(g\) a **reset gate** if some output value \(y^\star\) has a **singleton preimage** in \(\{0,1\}^{w}\) (equivalently, a fully-recoverable \([0,\dots,0]\) decay branch on \(y^\star\)).

**Claim.** If \(g\) is a reset gate then the filter **regenerates**: whenever \(Y_i=y^\star\), \(\pi_{i+1}\) is the *same* point mass \(\delta_{s^\star}\). Consequently the inter-reset cycles are i.i.d., the reset time has finite mean, and by renewal–reward


$$
h_Y \;=\; \frac{\mathbb{E}\big[\sum_{i\in\text{cycle}} H(Y_i\mid Y_{0:i-1})\big]}{\mathbb{E}[\text{cycle length}]},
$$


so \(a=1-h_Y\) is computed **exactly** from the single-cycle law — the finite belief-chain of the witness. Moreover \(\mu^\star\) is **purely atomic**, supported on the (geometrically clustering) beliefs reachable within one cycle.

**Proof.** \(Y_i=y^\star\) forces \((b_i,\dots,b_{i+w-1})\) to be the unique preimage of \(y^\star\); in particular the new boundary \(s_{i+1}=(b_{i+1},\dots,b_{i+w-1})\) is determined, so \(\pi_{i+1}=\delta_{s^\star}\) regardless of the past — a regeneration point. The gaps between successive regenerations are therefore i.i.d.\ (the process restarts in the same state). Because \(\Pr(Y_i=y^\star\mid\pi)\ge 2^{-w}>0\) uniformly, the cycle length \(T\) has geometric tail, \(\mathbb{E}[T]<\infty\). The per-step reward \(H(Y_i\mid Y_{0:i-1})=H(P_g(\cdot\mid\pi_i))\) depends only on \(\pi_i\), which within a cycle is a function of the outputs since the last reset — hence a function of the current cycle alone; rewards are i.i.d.\ across cycles. The renewal–reward theorem then gives the stated ratio, and equals \(h_Y\) by the Cesàro identity \(h_Y=\lim_n\frac1n\sum_{i<n}H(Y_i\mid Y_{0:i-1})\). Atomicity of \(\mu^\star\) follows because the reachable beliefs form the countable orbit \(\{\Phi_0^m\delta_{s^\star}\}_{m\ge0}\cup\dots\) generated within a cycle. \(\square\)

*Rigor:* **proved** (regeneration + renewal–reward). For \(w=2\), AND, \(y^\star=1\), this reduces exactly to the run-length chain of [m11f](m11f-decay-algebra-theorem.md).

---

## 5. Corollary — finiteness dichotomy


$$
\boxed{\text{belief-transfer algebra is exactly finite (atomic }\mu^\star)\ \Longleftarrow\ g\text{ is a reset gate.}}
$$


The witness verifies both directions on the tested family (assert in `m11_decay_algebra_general.py`: `method=="exact" ⇔ is_reset_gate`):

| gate | \(w\) | reset? (singleton preimage) | \(\mu^\star\) | method | \(a\) |
|------|------|------------------------------|--------------|--------|-------|
| AND | 2,3,4 | yes (\(y^\star=1\)) | atomic | exact | 0.30076 / 0.56568 / 0.74503 |
| OR | 2,3 | yes (\(y^\star=0\)) | atomic | exact | 0.30076 / 0.56568 |
| threshold\(\ge2\) | 3 | **no** | non-atomic | MC | 0.23734 |

The converse (non-reset \(\Rightarrow\) \(\mu^\star\) non-atomic) is **observed**, not proved here: Blackwell measures of non-regenerative functions of Markov chains are generically singular continuous, but a proof for a specific gate family is a separate question. Marked **conjectural**.

---

## 6. Scope, rigor, non-claims

| Statement | Rigor |
|-----------|-------|
| \(a=1-h_Y\) exists, \(E(k)=ak+O(1)\), all gates/widths (Thm 1) | **proved** |
| \(h_Y=\mathbb E_{\mu^\star}[H(Y\mid\pi)]\), transfer operator on \(2^{w-1}\) simplex (Thm 2) | **proved** (Blackwell, imported) |
| Reset gate ⇒ regenerative ⇒ renewal-reward ⇒ exact finite algebra (Thm 3) | **proved** |
| Non-reset ⇒ \(\mu^\star\) non-atomic (needs MC) | **conjectural** (observed) |

**Open (next rungs):** 2D strip transfer (boundary = a whole cut); the **continuum embedding** (scaling limit of \(a\) to a continuum entropy-production density — the bridge to the load term \(\gamma\lvert dS_c/d\tau\rvert\)).

**Non-claims (stand):** not continuum \(L(\rho,g)\); not \(dS_c/d\tau\) identity; not gravity. \(a\) is a discrete entropy-production density for sliding-window classical maps.

---

*Update O1 in [OPEN_AVENUES.md](OPEN_AVENUES.md) / [RESULTS_LEDGER.md](RESULTS_LEDGER.md) when 2D or continuum rungs advance.*
