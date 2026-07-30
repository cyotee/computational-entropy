# M11f — Decay-algebra density theorem (1D nearest-neighbour)

**M-id:** M11f · **Status:** **Constructive theorem (proved)** — 1D nearest-neighbour AND lattice
**Date:** 2026-07-30 · **Stance:** Preliminary research; finite/algorithmic rigor, **not** a continuum theorem.
**Witness (numeric):** `simulations/classical/m11_decay_algebra.py` (matches to \(<10^{-8}\))
**Depends on:** [m11-idem-to-load.md](m11-idem-to-load.md) §6 · export identity (Paper A) · [OPEN_AVENUES.md](OPEN_AVENUES.md) O1

This note upgrades O1 rung 3 from a **numerical witness** to a **proved theorem**: for the 1D nearest-neighbour AND lattice the coupled export **density exists** and **equals** the belief-transfer (decay-algebra) value, with a bounded boundary term. It rigorously closes the loop discrete-export → *local-transfer-computable density* for one coupling family.

---

## 1. Setup

Bits \(b_0,\dots,b_k\) i.i.d. \(\mathrm{Bernoulli}(1/2)\). Outputs (shared-input AND lattice)


$$
Y_i = b_i \wedge b_{i+1},\qquad i = 0,\dots,k-1 .
$$


Inputs \(X=(b_0,\dots,b_k)\), \(H(X)=k+1\). Since \(Y\) is a deterministic function of \(X\),


$$
E(k) \;:=\; H(X\mid Y_{0:k-1}) \;=\; H(X)-H(Y_{0:k-1}) \;=\; (k+1) - H(Y_{0:k-1}).
$$


**Density** (if it exists): \(a := \lim_{k\to\infty} E(k)/k\).

**Claim (Theorem).** \(a\) exists, and


$$
\boxed{\,a \;=\; 1 - h_Y,\qquad h_Y \;=\; \sum_{r\ge 0}\rho(r)\,h_2\!\big(p_1(r)\big)\,}
$$


where \(h_2\) is binary entropy and \((\rho,p_1)\) are the explicit run-length data of §3. Moreover \(E(k)=a\,k+b+o(1)\) for a finite constant \(b\). Numerically \(a = 0.3007568\).

---

## 2. Lemma 1 — the output entropy rate exists

\((Y_i)_{i\ge 0}\) is a **sliding-block factor** (window 2) of the i.i.d. process \((b_i)\): \(Y_i=\Phi(b_i,b_{i+1})\) with \(\Phi(u,v)=u\wedge v\). A finite-window factor of an i.i.d. process is **stationary and ergodic**. Hence by Shannon–McMillan–Breiman the entropy rate


$$
h_Y \;=\; \lim_{m\to\infty}\frac{1}{m}H(Y_{0:m-1}) \;=\; \lim_{i\to\infty} H(Y_i\mid Y_{0:i-1})
$$


exists. Therefore


$$
\frac{E(k)}{k} \;=\; \frac{k+1}{k} - \frac{H(Y_{0:k-1})}{k} \;\xrightarrow{k\to\infty}\; 1 - h_Y \;=:\; a. \qquad\square
$$


*Rigor:* **proved** (standard ergodic theory; the input-rate \((k+1)/k\to1\) is exact because there are \(k+1\) fair input bits for \(k\) outputs).

---

## 3. Lemma 2 — belief filter collapses to a run-length chain

Let \(\pi_i := \Pr(b_i=1\mid Y_{0:i-1})\) (the Bayesian filter on the shared boundary bit). Because \(b_{i+1}\) is fresh fair and independent,


$$
\Pr(Y_i=1\mid Y_{0:i-1}) \;=\; \Pr(b_i=1\mid Y_{0:i-1})\,\Pr(b_{i+1}=1) \;=\; \pi_i/2 .
$$


Bayes update of the boundary belief on the *new* bit \(b_{i+1}\):


$$
Y_i=1 \;\Rightarrow\; \pi_{i+1}=1;\qquad
Y_i=0 \;\Rightarrow\; \pi_{i+1}=\frac{1-\pi_i}{\,2-\pi_i\,}.
$$


(The first line is forced: \(Y_i=1\) requires \(b_i=b_{i+1}=1\).)

Because \(Y_i=1\) **resets** \(\pi\) to \(1\) deterministically, the filter value is a function of the **run length** \(r_i\) = number of consecutive \(0\)-outputs since the last \(1\)-output. Define


$$
\pi_0=1,\qquad \pi_{r+1}=\frac{1-\pi_r}{2-\pi_r},\qquad p_1(r):=\pi_r/2 .
$$


Then \((r_i)\) is a Markov chain on \(\{0,1,2,\dots\}\): from \(r\), emit \(1\) w.p. \(p_1(r)\) → state \(0\); emit \(0\) w.p. \(1-p_1(r)\) → state \(r+1\).

**Ergodicity.** \(p_1(r)=\pi_r/2\le 1/2<1\) for all \(r\) (so every \(r\!\to\!r{+}1\) transition has positive probability), and \(\pi_r\to\pi_\star=\frac{3-\sqrt5}{2}\) (the attracting fixed point of \(\pi\mapsto(1-\pi)/(2-\pi)\), root of \(\pi^2-3\pi+1=0\)), so \(p_1(r)\to p_{1\star}=\frac{3-\sqrt5}{4}\approx0.19098>0\). Thus resets keep positive probability, the chain is **irreducible**, **aperiodic** (self-loop at \(0\): \(p_1(0)=\tfrac12>0\)), and **positive recurrent** (geometric tail, below). Its unique stationary law is


$$
\rho(r) \;=\; \rho(0)\prod_{j=0}^{r-1}\big(1-p_1(j)\big),\qquad
\rho(0)=\Big(\textstyle\sum_{r\ge0}\prod_{j<r}(1-p_1(j))\Big)^{-1},
$$


and the sum converges because \(1-p_1(j)\to 1-p_{1\star}\approx0.809<1\) gives geometric decay. \(\square\)

*Rigor:* **proved** (finite-state-per-level Markov chain; standard Perron–Frobenius/renewal).

---

## 4. Lemma 3 — entropy rate as averaged emission entropy

The filter \(\pi_i\) is a sufficient statistic for \(Y_i\) given the past, so


$$
H(Y_i\mid Y_{0:i-1}) \;=\; \mathbb{E}\big[h_2(\pi_i/2)\big].
$$


By Lemma 2 the law of \(r_i\) (hence of \(\pi_i\)) converges to \(\rho\); by bounded convergence


$$
h_Y \;=\; \lim_i H(Y_i\mid Y_{0:i-1}) \;=\; \mathbb{E}_\rho\big[h_2(p_1(r))\big] \;=\; \sum_{r\ge0}\rho(r)\,h_2\!\big(p_1(r)\big). \qquad\square
$$


*Rigor:* **proved** (sufficiency of the filter + convergence of its law).

---

## 5. Theorem & boundary term

Combining Lemmas 1–3: \(a=1-h_Y=1-\sum_r\rho(r)h_2(p_1(r))\).

**Boundary.** \(H(Y_i\mid Y_{0:i-1})\to h_Y\) geometrically (the run-length chain mixes geometrically), so \(\sum_{i}\big(H(Y_i\mid Y_{0:i-1})-h_Y\big)\) converges; hence \(H(Y_{0:k-1})=k\,h_Y - b' + o(1)\) and


$$
E(k) \;=\; a\,k + b + o(1),\qquad b=1+b'\ \text{finite}.
$$


\(\square\)

---

## 6. Numerical confirmation

`simulations/classical/m11_decay_algebra.py` and the series above agree to 12 digits and match the **independent** \(O(2^k)\) enumeration of \(E(k)\):

| Quantity | Value |
|----------|-------|
| \(\pi_\star=(3-\sqrt5)/2\) | \(0.3819660113\) |
| \(p_{1\star}=\pi_\star/2\) | \(0.1909830056\) |
| density \(a=1-h_Y\) (series, \(R\ge200\)) | \(0.300756796612\) |
| enumerated \(\lim E(k)/k\) (linfit) | \(0.30076\) |
| \(|{\text{series}}-{\text{enumeration}}|\) | \(<10^{-8}\) |
| fitted boundary \(b\) | \(\approx 0.847\) |

The naive hard-decay bound was \(1.5\) bits/site; the theorem gives the exact \(0.3007568\).

---

## 7. Scope, rigor labels, non-claims

| Statement | Rigor |
|-----------|-------|
| Output entropy rate exists (Lemma 1) | **proved** |
| Run-length reduction + unique stationary law (Lemma 2) | **proved** |
| \(a=1-h_Y=1-\sum\rho\,h_2(p_1)\) (Theorem) | **proved** |
| \(E(k)=ak+b+o(1)\), \(b\) finite | **proved** |
| Decay algebra (belief transfer) computes \(a\) via local \(O(R)\) recursion | **constructive** (this note + script) |

**Explicitly still open (next ladder rungs):**

1. **General couplings** — the same transfer/belief argument for 2D and range-\(r\) coupling (boundary becomes a finite set of bits; a transfer *operator* on a larger belief space). **Witnessed numerically** for range-\(r\) 1D (`simulations/classical/m11_decay_algebra_general.py`): the operator on the \(2^{w-1}\) window states reproduces the enumerated density for AND/OR/threshold, and is exactly finite **iff** the gate has a fully-recoverable decay branch (reset gate). A general-\(w\) **theorem** and 2D remain open.
2. **Continuum embedding** — a scaling limit (lattice spacing \(h\to0\)) sending the discrete density \(a\) to a continuum **entropy-production density**, i.e. the actual bridge to the load term \(\gamma\lvert dS_c/d\tau\rvert\). **Not** attempted here; may carry an obstruction.

**Non-claims (stand):** not continuum \(L(\rho,g)\); not \(dS_c/d\tau\) identity; not gravity; \(a\) is a discrete entropy-production density for one coupling family, **not** the continuum load term.

---

*Update O1 in [OPEN_AVENUES.md](OPEN_AVENUES.md) and [RESULTS_LEDGER.md](RESULTS_LEDGER.md) when general-graph or continuum rungs advance.*
