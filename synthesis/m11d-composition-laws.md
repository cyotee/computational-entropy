# M11d — Composition Laws for \(H_c^{\mathrm{disc}}\) and \(L^{\mathrm{disc}}\)

**M-id:** M11d  
**Status:** **Finite classical theory + constructive witnesses** (2026-07-15)  
**Depends on:** [m11-idem-to-load.md](m11-idem-to-load.md) · [m11c-continuum-motivation.md](m11c-continuum-motivation.md) · [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) · [CLAIM_GATE.md](CLAIM_GATE.md)  
**Evidence:** [`simulations/classical/m11_composition_ledger.py`](../simulations/classical/m11_composition_ledger.py)  
**Entropy object:** Tag **E** — \(H_c^{\mathrm{disc}}\) (finite map / M11 ledger \(H(Y)\)); **not** Tag C toy residual, **not** continuum \(S_c\)  
**Layer:** Stage-1 classical microstructure only (no W/D/G/M gravity transfer)

**Stance:** Preliminary research. Prefer under-claiming. Every statement below is **finite classical** unless labeled otherwise. **\(L^{\mathrm{disc}} \neq L(\rho,g)\)**. Nothing here is continuum gravity, Einstein, or Bianconi GfE.

---

## 1. Scope

| In scope | Out of scope |
|----------|----------------|
| Finite alphabets, exact Shannon, deterministic maps | Continuum \(L(\rho,g)\), \(\Phi_g\), \(d\tau\) |
| Composition: pure cascade vs circuit (persistent wires) | \(L \equiv G\); Path J/M Newton; dual-toy residual \(H_c\) |
| Lemmas with proofs **or** counterexamples with numeric witnesses | Hydrodynamic limit of IDEM → continuum load |

**Notation (M11 dictionary):**

\[
H_c^{\mathrm{disc}}(f;p_X) := H(Y),\quad Y=f(X),\qquad
L^{\mathrm{disc}} = \beta' L_E^{\mathrm{disc}} + \gamma' L_S^{\mathrm{disc}} + \delta' L_B^{\mathrm{disc}}
\]

with default weights \(\beta'=\gamma'=\delta'=1\). Proxies as in [m11](m11-idem-to-load.md) §5.1:

| Slot | Finite proxy used here |
|------|------------------------|
| \(L_E\) | # active ops at a stage; path cost \(=\sum_{\mathrm{stages}} L_E\) |
| \(L_S\) | Stage export \(H(U\mid Y)\) for declared gate inputs \(U\); path cost \(=\sum_{\mathrm{stages}} L_S\) |
| \(L_B\) | Mean soft lost-recoverability mass on declared inputs |

**Two composition models (do not conflate):**

| Model | Definition | Used for |
|-------|------------|----------|
| **Pure cascade** | \(Y=f(X)\), \(Z=g(Y)\) — next stage sees **only** \(Y\) | Lemma B (export additivity) |
| **Circuit** | Stages may read residual input wires + intermediates | Lemma E (path-dependent \(\sum L_S\)) |

**Rigor labels:** **constructive** = exact finite identity / numerical assert; **structural** = bookkeeping convention consistent with M11; **semantic** = role language only.

---

## 2. Setup (finite classical)

Let \(X\) take values in a finite set \(\mathcal{X}\) with \(p_X>0\) on its support. Maps \(f,g,\ldots\) are deterministic functions unless noted. Declared **output** of a stage is the public result of that stage (foundations: entropy of the **output** marginal only).

**Path cost vs final map:** For a multi-stage pipeline, cumulative load slots are **sums of stage proxies**. These need **not** equal the single-shot proxies of the composed map \(g\circ f\). That gap is the main composition lesson of this note.

---

## 3. Lemmas

### Lemma A — Chain rule (export identity) for a deterministic map

**Statement.** If \(Y=f(X)\) is deterministic and \(H\) is Shannon entropy (any base), then

\[
H(X) = H(Y) + H(X\mid Y).
\]

**Proof (standard).** Chain rule \(H(X,Y)=H(Y)+H(X\mid Y)\). Determinism \(\Rightarrow Y\) is a function of \(X\) \(\Rightarrow H(Y\mid X)=0\) \(\Rightarrow H(X,Y)=H(X)\). ∎

**Rigor:** **constructive** (information theory; Phase-1 AND-gate error \(<10^{-12}\)).

**M11 reading:** \(H(X\mid Y)\) is **export** (environment / preimage register), not destruction ([definition](../foundations/computational-entropy/definition.md) global conservation). Single-shot \(L_S := H(X\mid Y)\) is a **structural** proxy for export flux ([m11](m11-idem-to-load.md) §5–6).

---

### Lemma B — Export additivity along a deterministic **pure** cascade

**Statement.** Let \(Y=f(X)\) and \(Z=g(Y)\) be deterministic (so \(Z=(g\circ f)(X)\) and the second stage does **not** read \(X\) except through \(Y\)). Then

\[
H(X\mid Z) = H(X\mid Y) + H(Y\mid Z).
\]

**Proof.** Apply Lemma A twice:

\[
H(X)=H(Y)+H(X\mid Y),\qquad H(Y)=H(Z)+H(Y\mid Z).
\]

Substitute:

\[
H(X)=H(Z)+H(Y\mid Z)+H(X\mid Y).
\]

Lemma A on \(Z=(g\circ f)(X)\): \(H(X)=H(Z)+H(X\mid Z)\). Equate the two expansions. ∎

**Corollary B.1.** Under the pure-cascade hypothesis, \(I(X;Z\mid Y)=0\) (Markov \(X\to Y\to Z\)), so the same identity is the conditional-entropy chain rule along that Markov chain.

**Warning.** If the “second stage” still reads a residual wire (circuit model), \(Z\) is **not** a function of \(Y\) alone and Lemma B **need not** hold in the form \(H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)\). Example: \(Y=X_1\), \(Z=Y\land X_2\) yields \(H(X\mid Y)+H(Y\mid Z)\neq H(X\mid Z)\) in general.

**Rigor:** **constructive** (proof + witness).  
**Witness:** Fair bits; \(Y=X_1\land X_2\), \(Z=\mathrm{NOT}(Y)\). Then \(H(Y\mid Z)=0\), \(H(X\mid Z)=H(X\mid Y)\approx 1.188722\), error \(<10^{-12}\).

---

### Lemma C — Data processing for declared output entropy (DPI)

**Statement.** If \(Z=g(Y)\) is a deterministic function of \(Y\), then

\[
H(Z) \le H(Y),
\]

with equality iff \(g\) is injective on the support of \(p_Y\).

**Proof.** \(H(Y)=H(Z)+H(Y\mid Z)\) and \(H(Y\mid Z)\ge 0\). Equality \(\Leftrightarrow H(Y\mid Z)=0\) \(\Leftrightarrow Y\) is determined by \(Z\) on \(\mathrm{supp}\,p_Y\). ∎

**M11 reading:** Declared \(H_c^{\mathrm{disc}}\) is **non-increasing** under post-processing of the same channel output. This is **not** a claim about continuum \(S_c\) or dual-toy residual \(H_c^{\mathrm{toy}}\).

**Rigor:** **constructive**.  
**Witness:** \(Z=\mathrm{NOT}(Y)\) on AND output: \(H(Z)=H(Y)\) (bijection on \(\{0,1\}\)). Strict drop: constant map \(Y\mapsto 0\) gives \(H=0\le H(Y)\).

---

### Lemma D — \(L_E\) additivity under sequential active ops

**Statement (definitional / structural).** If a path is a sequence of stages \(s=1,\ldots,n\) and each stage is assigned active work \(L_E^{(s)}\in\{0,1,2,\ldots\}\) (ops / gates / redexes this stage), define

\[
L_E^{\mathrm{path}} := \sum_{s=1}^{n} L_E^{(s)}.
\]

Then \(L_E^{\mathrm{path}}\) is additive by construction under concatenation of paths.

**Proof.** Finite sum of scalars is associative; concatenation of stage lists concatenates summands. ∎

**Interpretation:** Comparing a **direct** one-op map to a **two-op circuit** realizing the same final function, \(L_E^{\mathrm{path}}\) **counts machinery used along the way**, not merely the existence of a one-op realization.

**Rigor:** **structural** (accounting convention) + **constructive** on Boolean ledgers (\(L_E=1\) per gate).  
**Witness:** Direct AND: \(\sum L_E=1\); circuit publish+AND: \(\sum L_E=2\); Markov AND+NOT: \(\sum L_E=2\).

**Non-claim:** \(L_E^{\mathrm{path}}\) is **not** continuum energy density \(E[\rho]/(V\epsilon_0)\).

---

### Lemma E — Path dependence of cumulative \(L_S\) (same final \(H(Z)\))

**Statement.** There exist finite models and two **circuit** pipelines \(P,P'\) such that:

1. Final declared outputs \(Z,Z'\) are **equal in law** (same \(H_c^{\mathrm{disc}}=H(Z)=H(Z')\));  
2. Final maps realize the **same** function of \(X\);  
3. Cumulative stage export costs differ:

\[
\sum_s L_S^{(s)}(P) \;\neq\; \sum_{s'} L_S^{(s')}(P').
\]

In particular, **\(\sum L_S\) is not a function of the final map alone**.

**Proof (by explicit construction).** Fair bits \(X=(X_1,X_2)\). Circuit model: later stages may still read residual wires.

| Path | Stages | Final \(Z\) | \(\sum L_S\) (stage exports) |
|------|--------|-------------|------------------------------|
| **Direct \(D\)** | \(Z=X_1\land X_2\) | AND law, \(H(Z)=h_2(1/4)\) | \(H(X\mid Z)\approx 1.188722\) |
| **Circuit \(C\)** | \(Y=X_1\), then \(Z=Y\land X_2\) (wire \(X_2\) retained) | same AND law | \(H(X\mid Y)+H(X\mid Z)=1+1.188722=2.188722\) |

Stage \(L_S\) at circuit step 2 uses gate-input export \(H(Y,X_2\mid Z)=H(X\mid Z)\) (same single-shot proxy as Direct). Circuit **additionally** pays intermediate wire-publish export \(H(X\mid Y)=1\).

Same final \(H(Z)\); \(\sum L_S(C)-\sum L_S(D)=1\neq 0\). ∎

**Relation to Lemma B.** Total residual export to the **final** output, \(H(X\mid Z)\), **is** path-independent for a fixed final map (depends only on \((X,Z)\)). Cumulative **stage** cost \(\sum L_S\) counts **every** stage’s export proxy — including intermediate publishes that later feed the same \(Z\). Thus:

```text
H(X|Z)           — property of the final I/O pair (path-independent for fixed map)
Σ_s L_S^(s)      — property of the pipeline (path-dependent; circuit stages)
```

**Rigor:** **constructive** (closed-form + ledger asserts).  
**Key numeric:** \(\sum L_S(D)\approx 1.188722\), \(\sum L_S(C)\approx 2.188722\), \(H(Z)\approx 0.811278\) both paths; \(H(X\mid Z)\) identical.

**Structural reading (locked \(L\)):** Paying for an intermediate publish/export that is later re-used in an irreversible gate **raises demand along the path**, even when the **final** output law is unchanged. Load is not “final \(H_c\) alone.”

---

### Lemma F — \(L_B\) non-additivity (characterization + witnesses)

**Statement.** Soft-recoverability \(L_B\) (mean soft lost-recoverability mass) is **not** additive under either:

1. **Regional sum vs joint mean** on a product system; or  
2. **Sum of stage \(L_B\)** vs \(L_B\) of the composed / direct map.

**F.1 Product / regional sum.**  
Let \(A\) and \(B\) be independent AND maps on disjoint fair-bit pairs; let \(L_B(A)\), \(L_B(B)\) be Phase-1 soft masses on each pair’s two inputs; let \(L_B(G)\) be the mean soft mass over **all four** input coordinates under the joint map \((Y,V)=(f_A,f_B)\). Then in general

\[
L_B(A)+L_B(B) \;\neq\; L_B(G).
\]

**Witness:** \(L_B(A)=L_B(B)=0.5\), sum \(=1.0\), but \(L_B(G)=0.5\) (averaging four coordinates does not sum regional means).

**Why:** \(L_B\) is an **average** of per-coordinate soft losses under a chosen input set. Changing the coordinate set (2 vs 4) or averaging vs summing changes the scalar. There is no theorem that regional loads **sum** to the global mean proxy.

**F.2 Stage sum vs direct map.**  
Circuit stages each report a soft-decay mass on their declared inputs; Direct reports one mass on \((X_1,X_2)\) under AND. In the witness:

\[
L_B^{(1)}(C)+L_B^{(2)}(C) \;\neq\; L_B(D)
\]

(intermediate wire publish has its own recoverability profile; summing stage diagnostics mixes incompatible input declarations).

**When additivity can hold (limited cases).**  
If one **defines** a different proxy — e.g. **total** (not mean) soft-loss mass summed over a fixed global coordinate set, and stages partition those coordinates without overlap — then that **total** may add. That is a **different bookkeeping convention**, not the Phase-1 mean soft \(L_B\).

**Rigor:** **constructive counterexamples** (not a uniqueness theorem about all possible \(L_B\) formulas).  
**Structural:** \(L_B\) tracks **open distinguishability budget** for a **declared** input/output cut; composition changes the cut.

---

### Remark G — Stochastic maps (brief)

For a general channel \(p(y\mid x)\), Lemma A becomes \(H(X)=I(X;Y)+H(X\mid Y)\) with \(H(Y)\) no longer equal to \(I(X;Y)\) in general. DPI for mutual information \(I(X;Z)\le I(X;Y)\) under \(X\to Y\to Z\) is standard; export additivity \(H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)\) requires the pure-cascade / appropriate Markov hypotheses. M11d **does not** elevate stochastic composition to continuum \(S_c\).

**Rigor:** standard IT (background); **not** re-proved in the ledger.

---

## 4. Rigor board

| Claim | Level | Status |
|-------|-------|--------|
| Lemma A chain rule \(H(X)=H(Y)+H(X\mid Y)\) | **Constructive** | Standard; Phase 1–2 asserts |
| Lemma B \(H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)\) (pure cascade) | **Constructive** | Proof §3 + Markov path in ledger |
| Lemma C DPI \(H(g(Y))\le H(Y)\) | **Constructive** | Proof + NOT∘AND witness |
| Lemma D \(L_E\) path sum | **Structural** (defn) + constructive counts | Ledger |
| Lemma E path-dependent \(\sum L_S\) (circuit) | **Constructive** | Explicit Direct vs Circuit |
| \(H(X\mid Z)\) path-independent for fixed final map | **Constructive** | Same \((X,Z)\) |
| Lemma F \(L_B\) non-additivity | **Constructive counterexamples** | Product + circuit stages |
| Continuum composition of \(L(\rho,g)\) | **Not claimed** | Deferred |
| Gravity / Einstein / \(L\equiv G\) | **Not claimed** | Forbidden |

---

## 5. Explicit non-claims

Do **not** assert from this note or `m11_composition_ledger.py`:

1. Master equation \(\Leftrightarrow\) continuum GfE.  
2. \(L \equiv G\), \(L^{\mathrm{disc}} \equiv L(\rho,g)\), or \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\).  
3. Composition laws of continuum load, \(\lvert dS_c/d\tau\rvert\), or proper-time clocks.  
4. Einstein / Newton recovery from Boolean cascades (Newton remains Path J/M only).  
5. IDEM/decay constructs continuum \(L\) or \(G\).  
6. Dual-toy residual \(H_c^{\mathrm{toy}}\) equals \(H_c^{\mathrm{disc}}\).  
7. \(\sum L_S\) or \(\sum L_B\) are unique “the” composition functors for load (they are M11 bookkeeping choices).  
8. Path dependence of \(\sum L_S\) is a gravitational redshift theorem.

**Allowed claim form:**

> *On finite classical maps, export obeys the Shannon chain rule and pure-cascade additivity; DPI holds for deterministic post-processing of declared outputs; \(L_E^{\mathrm{path}}\) sums ops; cumulative stage \(L_S\) is path-dependent on circuits even when final \(H(Z)\) and \(H(X\mid Z)\) match; mean soft \(L_B\) is not additive under naive regional or stage sums. These are discrete accounting laws (Tag E), not continuum gravity.*

---

## 6. One-sentence conclusions

1. **Export / chain rule:** For deterministic finite maps, information is conserved as \(H(X)=H(Y)+H(X\mid Y)\); along a pure cascade \(Z=g(Y)\), residual export **adds**: \(H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)\).  
2. **DPI:** Declared output entropy is nonincreasing under deterministic post-processing of that output.  
3. **\(L_E\):** Sequential active ops add in the path ledger by construction — more machinery, higher work slot.  
4. **\(L_S\):** Cumulative stage export cost is **path-dependent** on circuits (Direct AND \(\sum L_S\approx 1.189\) vs publish-then-AND \(\sum L_S\approx 2.189\)) even when final \(H(Z)\) and \(H(X\mid Z)\) coincide.  
5. **\(L_B\):** Mean soft recoverability is a **cut-dependent** scalar: regional sums and stage sums **fail** additivity in explicit product and circuit witnesses.  
6. **Program:** Composition laws tighten Stage-1 bookkeeping; they **do not** derive continuum \(L\) or gravity.

---

## 7. Links

| Resource | Role |
|----------|------|
| [m11-idem-to-load.md](m11-idem-to-load.md) | Discrete \(H_c\), \(L^{\mathrm{disc}}\) dictionary |
| [m11c-continuum-motivation.md](m11c-continuum-motivation.md) | Role motivation only (not limit theorem) |
| [CLAIM_GATE.md](CLAIM_GATE.md) | Under-claim / Tag E / \(L^{\mathrm{disc}}\neq L(\rho,g)\) |
| [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) | Canonical \(H_c\); AND conservation |
| [`m11_composition_ledger.py`](../simulations/classical/m11_composition_ledger.py) | Constructive witnesses |
| Phase 1–2 ledgers | AND, multi-step Boolean, coupled regions |

---

## 8. One-screen summary

```text
M11d — composition laws (finite classical only; 2026-07-15)

H_c^disc:  H(Y) of declared output (Tag E)
EXPORT:    H(X)=H(Y)+H(X|Y)
           pure cascade H(X|Z)=H(X|Y)+H(Y|Z)     [proved + witness]
DPI:       H(g(Y)) ≤ H(Y) for deterministic g    [proved]
L_E:       Σ ops along path (additive by defn)   [structural]
L_S:       Σ stage exports PATH-DEPENDENT (circuit)
           Direct AND ΣL_S ≈ 1.189  vs  Circuit ≈ 2.189
           same final H(Z)≈0.811 and same H(X|Z) [witness]
L_B:       mean soft mass NOT additive (0.5+0.5 ≠ 0.5 global) [witness]

NEVER: L^disc = continuum L; L≡G; Einstein from gates; dual-toy H_c
```

---

*Update PACK_INDEX / OPEN_MATH when composition laws are cited in paper prose. Keep Tag E and non-claims intact.*
