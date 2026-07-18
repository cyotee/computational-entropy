# 5. Classical microstructure --- IDEM, decay, and discrete load (M11 + D12--D13)

## 2.1 The central gap

This research program has long carried two substantial threads that barely touched:

| Thread | Machinery | Gap |
|--------|-----------|-----|
| **Classical / lambda** | IDEM (arity, AST metrics, decay vector, $d_f$), games as maps, combinatorial density | Did not feed gravity recoveries |
| **Emergent gravity** | $\Phi_g$, $S_c$, load $L$, master equation, Path J/M Newton | Used only high-level "output entropy" language |

**M11** addresses that gap by a **discrete accounting dictionary**


$$
\text{IDEM / game / lambda step}\;\longrightarrow\; H_c^{\mathrm{disc}}\ \text{and candidate terms in }L^{\mathrm{disc}},
$$


implemented as pure bookkeeping on finite classical models --- **without** inventing continuum metric $G$, rewriting the master equation, or claiming Einstein-from-gates (Appendix A). Continuum role motivation of the three load slots is a separate design essay (Appendix A): **structural**, not a continuum limit theorem.

## 2.2 IDEM and the decay vector (brief)

An **IDEM** (expanded identity) pairs a map result with metadata: arity, result dimension, decay vector $\mathbf{d}$, function unidentifiability $d_f$, and optional AST complexity metrics. In recoverability models:

- $d_i=0$: input $x_i$ is recoverable from the declared output under the model;  
- $d_i=1$: that input information is **lost** to an observer of $Y$ alone;  
- Soft variants use $d_i\in[0,1]$ (e.g. $1-1/|\mathrm{preimage}|$).

For fair-bit AND, output $Y=1$ has a unique preimage $(1,1)$, while $Y=0$ has three preimages; recoverability fails on the latter branch, matching the large conditional entropy $H(X\mid Y)$. Decay flips $0\to 1$ are the classical image of **irreversible overwrite**; M11 feeds the **rate** of export or soft decay into the entropy-rate load slot, not an idle "identity stockpile."

**Rigor:** IDEM ontology and decay semantics are **semantic/structural** classical design. Concrete finite Shannon numbers below are **constructive**. Mapping decay to holographic screen degrees of freedom remains **analogical**, not a theorem.

## 2.3 Operational $H_c^{\mathrm{disc}}$ and three-slot discrete load

**Operational rule.** Computational entropy on a discrete model is the Shannon entropy of the **declared public output**, not residual dual-toy scores, not internal AST size alone, and not blackjack bankroll EV.

Continuum load has three **roles** (energy-like density, entropy-rate / export, boundary/capacity). M11 defines matching **proxies** with bookkeeping weights $\beta',\gamma',\delta'$ (default $1$), **not** continuum calibrations:


$$
L^{\mathrm{disc}}
=
\beta' L_E^{\mathrm{disc}}
+
\gamma' L_S^{\mathrm{disc}}
+
\delta' L_B^{\mathrm{disc}}.
$$


| Continuum role (master eq) | Discrete proxy | Locked reading |
|----------------------------|----------------|----------------|
| Energy-like work | $L_E$: ops / redexes / active evaluations this step | Idle identity $\Rightarrow$ low $L_E$; active work $\Rightarrow$ high |
| Entropy-rate / export flux | $L_S$: $H(X\mid Y)$ single-shot, or $|\Delta H_c^{\mathrm{disc}}|$ multi-step, or soft decay-flip rate | High flux / overwrite $\Rightarrow$ **high** $L_S$ even when $H(Y)$ falls |
| Boundary / capacity | $L_B$: mean soft lost-recoverability mass; residual ensemble entropy ratio; open redex fraction | Open distinguishability budget $\Rightarrow$ high $L_B$ |

**Locked $L$ reading (C14).** Prefer demand from **scale and rate of possible channel outcomes**. Reject as primary story: "how much unreduced identity stockpile remains." High entropy flux, many open results, and active scrambling raise load; fully reduced idle maps have low load.

**Type safety.** The three discrete slots share **roles** with continuum $L(\rho,g)$. They do **not** equal continuum coefficients, Newton's $G$, or the structure metric $G$. Same three axes of demand; different mathematical objects.

## 2.4 Phase 1 --- AND-gate pure ledger (constructive)

Artifact: Appendix A.1.

| Quantity | Value (fair bits) | Role |
|----------|-------------------|------|
| $H(X)$ | $2$ bits | Input possibility mass |
| $H_c^{\mathrm{disc}}=H(Y)$ | $h_2(1/4)\approx 0.811278$ | Declared output entropy (Tag **E**) |
| Export $H(X\mid Y)$ | $\approx 1.188722$ | Preimage / environment ledger |
| $L_E^{\mathrm{disc}}$ | $1$ (one gate op) | Active work |
| $L_S^{\mathrm{disc}}$ | $:=H(X\mid Y)\approx 1.188722$ | Single-shot export flux |
| $L_B^{\mathrm{disc}}$ | $0.5$ (mean soft lost-recoverability mass) | Open distinguishability after map |
| $L^{\mathrm{disc}}$ (weights $1$) | $\approx 2.689$ | Sum of independent role proxies |

**Observation.** Output $H_c^{\mathrm{disc}}$ **drops** ($\approx 2\to 0.811$) while demand **rises**. Any monist load proportional to residual output entropy alone would report *low* demand precisely when irreversible overwrite is *expensive* --- opposite of the locked reading. Three independent axes appear simultaneously: work ($L_E$), export flux ($L_S$), and residual recoverability mass ($L_B$).

Chain rule residual on the ledger is $<10^{-12}$. **Rigor:** $H_c^{\mathrm{disc}}$ and export **constructive**; three-slot assignment **structural bookkeeping**, not continuum $L$ ($L^{\mathrm{disc}}\neq L(\rho,g)$).

## 2.5 Phase 2 --- multi-step Boolean, tiny SKI, minimal shoe (brief)

Phase-2 multi-step, SKI, and shoe ledgers are summarized in Appendix A.

**Multi-step Boolean.** An identity baseline on $(X_1,X_2,X_3)$ has $L_E=L_S=L_B=0$ (idle). An AND step spikes export ($L_S\approx 1.189$); a subsequent OR-type step has **lower** export than AND. Ordering is asserted under the locked reading: larger export $\Rightarrow$ larger $L_S$. An optional discrete load-clock diagnostic $k_{\mathrm{eff}}=\sum 1/(1+\alpha' L^{\mathrm{disc}})$ with conventional $\alpha'=0.1$ is printed only as bookkeeping --- **not** continuum proper time.

**Tiny SKI ensemble.** Fixed finite combinator terms under normal-order redex steps: $L_E=$ mean redex count pre-step; $L_S=|\Delta H_c^{\mathrm{disc}}|$ under reduction; $H_c^{\mathrm{disc}}$ drops as term-shape classes concentrate under reduction. Exact Shannon on a finite ensemble; no continuum constants.

**Minimal R/B shoe.** Fixed-sequence multiset (e.g. 6 red + 6 black residual shoe): predictive $H_c^{\mathrm{game}}$-adjacent combinatorial entropy of next color; $L_E=1$ per count-bucket update; $L_S=|\Delta H_c^{\mathrm{game}}|$ spikes when predictive entropy jumps; $L_B=H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)$ residual order-entropy ratio as capacity-like pressure. Honesty: **not** bankroll EV, **not** ACD-EW residual dual $H_c^{\mathrm{toy}}$, and not multi-deck strategy science (M12 deferred).

**Rigor:** Phase 2 ledgers are **constructive** finite accounting with **structural** continuum role alignment only.

## 2.6 Coupled regions (one paragraph)

A two-region product ledger (Appendix A) places independent fair-bit pairs on regions $A$ and $B$, runs local ANDs, then a coupling XOR "screen" that redistributes shared information. The experiment shows: global chain-rule conservation on the product alphabet; local high export $\Rightarrow$ high local $L_S$ while an idle baseline region stays low; coupling redistributes / screens information without magical destruction; optional per-region diagnostic $k_{\mathrm{eff}}$. Product regions are **not** spacetime patches, **not** continuum $\rho$, and **not** a derivation of local energy density fields. They make multi-site classical conservation **constructive** before any hydrodynamic aspiration (Section 2.9 / Appendix A §5--6).

## 2.7 Composition path dependence (D13 / Appendix A.2)

**Evidence:** Appendix A.2. Entropy object: Tag **E**. Stage-1 classical only.

**Two composition models (must not be conflated).**

| Model | Definition |
|-------|------------|
| **Pure cascade** | $Y=f(X)$, $Z=g(Y)$ --- next stage sees only $Y$ |
| **Circuit** | Later stages may still read residual input wires + intermediates |

Standard lemmas (finite classical):

- **Lemma A (chain rule):** $H(X)=H(Y)+H(X\mid Y)$ for deterministic $Y=f(X)$.  
- **Lemma B (export additivity on pure cascade):** $H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)$.  
- **Lemma C (DPI):** $H(g(Y))\le H(Y)$.  
- **Lemma D:** path $L_E$ is additive by counting ops.  
- **Lemma E (path dependence of cumulative $L_S$):** $\sum L_S$ is **not** a function of the final map alone.

**Explicit Direct vs Circuit witness (fair bits $X=(X_1,X_2)$).**

| Path | Stages | Final $Z$ | $H(Z)$ | $\sum L_S$ (stage exports) |
|------|--------|-------------|----------|------------------------------|
| **Direct $D$** | $Z=X_1\land X_2$ | AND law | $\approx 0.811278$ | $H(X\mid Z)\approx 1.188722$ |
| **Circuit $C$** | $Y=X_1$, then $Z=Y\land X_2$ (wire $X_2$ retained) | same AND law | $\approx 0.811278$ | $H(X\mid Y)+H(X\mid Z)=1+1.188722=2.188722$ |

Thus, in rounded form used for program citation:


$$
\sum L_S(D)\approx 1.189,\qquad
\sum L_S(C)\approx 2.189,\qquad
H(Z)\ \text{identical on both paths}.
$$


**Crucial distinction.**

```text
H(X|Z)           --- property of the final I/O pair (path-independent for fixed final map)
Σ_s L_S^(s)      --- property of the pipeline (path-dependent under circuit stages)
```

Paying for an intermediate publish/export that is later re-used in an irreversible gate **raises demand along the path**, even when the final output law is unchanged. Load is not "final $H_c^{\mathrm{disc}}$ alone." Soft-recoverability $L_B$ is likewise **not** freely additive under regional sums or stage sums without a fixed global coordinate convention (Lemma F counterexamples).

**Rigor:** Lemmas A--C and the Direct/Circuit numbers are **constructive**; continuum composition of $L(\rho,g)$ is **not claimed**.

## 2.8 Landauer contact for export and $L_S$ (D13 / Appendix A.3)

**Evidence:** Appendix A.3.

On the same finite AND model, fix an explicit **Protocol R** (reset after AND): compute $Y=f(X)$, keep only $Y$ as public system output, and thermalize residual input registers conditional on $Y$. The average number of erased bits is the export


$$
n_{\mathrm{erased}} := H(X\mid Y).
$$


**Landauer's principle** (external theorem; not re-proved here) then supplies the standard lower bound on average heat dissipated to a bath at temperature $T$:


$$
Q \;\ge\; k_B T \ln 2 \cdot H(X\mid Y)
\qquad\text{(Shannon in bits)}.
$$


In units of $k_B T\ln 2$, the bound **equals** the export ledger quantity. M11's single-shot entropy-rate slot is defined as that same object:


$$
L_S^{\mathrm{disc}} := H(X\mid Y)
\quad\Rightarrow\quad
Q \;\ge\; k_B T \ln 2 \cdot L_S^{\mathrm{disc}}
\quad\text{(single-shot AND / Protocol R)}.
$$


| Quantity | Fair-bit AND |
|----------|----------------|
| $H(Y)=H_c^{\mathrm{disc}}$ | $\approx 0.811278$ |
| Export $H(X\mid Y)$ | $\approx 1.188722$ |
| Landauer $Q_{\min}/(k_B T\ln 2)$ | $=H(X\mid Y)\approx 1.188722$ |
| $L_S^{\mathrm{disc}}$ | $=$ export by definition |

**Optional reversible dilation (Bennett-style, structural).** A reversible embedding can park preimage information in **garbage** $G$; public $H(Y)$ may match the irreversible case, but eventual erasure of $G$ still costs $\ge H(X\mid Y)$. Export does not vanish under reversible accounting; it is deferred until garbage reset.

**What this contact is and is not.**

| Allowed | Forbidden from Appendix A.3 alone |
|---------|---------------------------|
| Export $H(X\mid Y)$ is the average erased-bit count under Protocol R | Newton $G$ or Path J/M calibration from Landauer |
| $L_S^{\mathrm{disc}}$ is that information object | $\hbar$, holography, or $S_{\mathrm{BH}}=A/4G\hbar$ from AND heat |
| Thermodynamic bookkeeping contact only | Continuum $L_S$ density = GR/GfE heat flux |
| | $L\equiv G$ or $L^{\mathrm{disc}}\equiv L(\rho,g)$ |

**Rigor:** finite Shannon identities **constructive**; Landauer inequality **external theorem**; identification of $L_S$ with the Landauer bit-count **structural contact**. Conversion factor $k_B T\ln 2$ is standard thermodynamics, **not** fitted to gravity scales.

### Numbered Stage-1 theorems (finite classical)

The following are **finite classical** statements on declared I/O cuts (entropy Tag **E**). They are **constructive** on finite alphabets and ledgers unless labeled otherwise. They do **not** transfer to continuum $L(\rho,g)$, $\Phi_g$, Path J/M, dual residual $H_c^{\mathrm{toy}}$, or GfE without a new map. Sources: Appendix A.2, Appendix A.3; witnesses Appendix A.2, Appendix A.3, Appendix A.1.

**Theorem T1 (chain rule / export for deterministic maps).**  
Let $X$ be a finite-alphabet random variable and $Y=f(X)$ a deterministic map. Then


$$
H(X)=H(Y)+H(X\mid Y).
$$


**Reading:** $H(X\mid Y)$ is **export** (preimage / environment register), not destruction of information. Single-shot $L_S^{\mathrm{disc}}:=H(X\mid Y)$ is a structural export-flux proxy (M11).  
**Rigor:** **constructive** (Shannon chain rule; Phase 1 AND residual $<10^{-12}$).  
**Cite:** Appendix A.2 Lemma A · §1.4 · §2.4.

**Theorem T2 (Markov cascade export additivity).**  
Let $Y=f(X)$ and $Z=g(Y)$ be deterministic with pure cascade (second stage sees only $Y$). Then


$$
H(X\mid Z)=H(X\mid Y)+H(Y\mid Z).
$$


**Warning:** Circuit stages that re-read residual input wires need not obey this identity in the cascade form.  
**Rigor:** **constructive** (proof + ledger witness; e.g. AND then NOT).  
**Cite:** Appendix A.2 Lemma B · §2.7.

**Theorem T3 (path dependence of cumulative $\sum L_S$).**  
There exist finite models and two pipelines realizing the **same** final map $X\mapsto Z$ (same law, same $H(Z)$) such that cumulative stage export costs differ. Explicit fair-bit witness:


$$
\sum L_S(\mathrm{Direct})\approx 1.188722,\qquad
\sum L_S(\mathrm{Circuit})\approx 2.188722,\qquad
H(Z)\approx 0.811278\ \text{on both paths}
$$


(rounded **1.189** vs **2.189**). Thus $\sum L_S$ is **not** a function of the final map alone; final residual $H(X\mid Z)$ remains path-independent for fixed $(X,Z)$.  
**Rigor:** **constructive** (closed form + composition ledger).  
**See:** Theorem T3; Appendix A.2; Results P4.

**Theorem T4 (Landauer identification of $L_S$ under Protocol R).**  
On Protocol R for a finite deterministic map (compute $Y=f(X)$, keep public $Y$, thermalize residual input registers conditional on $Y$), the average erased-bit count is $H(X\mid Y)$. Landauer's principle (external) supplies


$$
Q\ge k_B T\ln 2\cdot H(X\mid Y).
$$


M11 single-shot $L_S^{\mathrm{disc}}:=H(X\mid Y)$ is that same information object, so $Q\ge k_B T\ln 2\cdot L_S^{\mathrm{disc}}$. On fair-bit AND, export $=$ Landauer bit-count $\approx 1.188722$.  
**Rigor:** finite Shannon **constructive**; Landauer inequality **external theorem**; $L_S$ identification **structural contact**. Not Newton, not continuum $L$, not $L\equiv G$.  
**See:** Theorem T4; Appendix A.3; Results P3.

**Proposition T5 ($L_B$ non-additivity witness).**  
Mean soft-recoverability $L_B$ is **not** freely additive under (i) regional sum vs joint mean on product systems, or (ii) sum of stage $L_B$ vs $L_B$ of a direct map. Explicit product witness: two independent AND regions with $L_B(A)=L_B(B)=0.5$ give sum $1.0$ but joint mean $L_B(G)=0.5$.  
**Rigor:** **constructive counterexamples** (not a uniqueness theorem for every possible $L_B$ formula).  
**See:** Proposition T5; Appendix A.2.

| ID | Statement | Rigor |
|----|-----------|-------|
| **T1** | $H(X)=H(Y)+H(X\mid Y)$ (deterministic) | constructive |
| **T2** | Pure-cascade export additivity $H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)$ | constructive |
| **T3** | $\sum L_S$ path-dependent (Direct $\approx 1.189$ vs Circuit $\approx 2.189$) | constructive |
| **T4** | $L_S=H(X\mid Y)$ Landauer bit-count under Protocol R | constructive + external |
| **T5** | Mean soft $L_B$ non-additive (product / stage witnesses) | constructive counterexamples |

**Non-claims for T1--T5.** Continuum composition of $L(\rho,g)$; Einstein from Boolean cascades; $\sum L_S$ as gravitational redshift; dual-toy residual $=$ gate export.

## 2.9 Why three load terms? (structural motivation)

Discrete evidence simultaneously requires three independent **axes of demand** (Section 2.9 / Appendix A):

1. **How hard is the machine working?** ($L_E$)  
2. **How fast is possibility being realized / exported?** ($L_S$)  
3. **How much distinguishability budget remains open versus capacity?** ($L_B$)

A monist load $L\propto H_c^{\mathrm{disc}}$ alone fails on irreversible AND (output entropy low, export high). A monist "remaining AST size" fails the locked reading when the stockpile is idle. Shoe dynamics separate nearly constant update cost ($L_E$), flux spikes ($L_S$), and smoothly shrinking residual multiset capacity ($L_B$). Continuum three-term $L$ is the **same role split** at continuum language level --- **structural motivation**, not uniqueness, and not a hydrodynamic limit of IDEM.

## 2.10 Section non-claims

Do **not** assert from M11 Phase 1--2, composition, Landauer contact, or coupled-region ledgers:

1. Master equation $\Leftrightarrow$ continuum GfE.  
2. $L\equiv G$, $L^{\mathrm{disc}}\equiv L(\rho,g)$, or $S_c\equiv\operatorname{Tr} g\ln G^{-1}$.  
3. IDEM/decay **constructs** continuum $L$ or metric $G$ (PROGRESS non-claim §2.3.9).  
4. Newton / Einstein recovery from gates, SKI terms, shoes, or Landauer heat.  
5. Lattice dual toys or blackjack-belief dual **are** gravity or **are** true game predictive $H_c^{\mathrm{game}}$.  
6. Path J/M calibration constants $\alpha,\beta,\gamma,\delta,\epsilon_0$ are fixed by discrete proxies.  
7. Decay vector components **are** Hawking radiation degrees of freedom.  
8. Primary load = idle remaining identity stockpile.  
9. Continuum composition laws of $L(\rho,g)$ or $\lvert dS_c/d\tau\rvert$ from finite Boolean cascades.  
10. Dual-toy residual $H_c^{\mathrm{toy}}$ equals gate export or Landauer bits.

**Allowed claim form (program-level).** On finite classical models $\mathcal{M}$, we define constructive $H_c^{\mathrm{disc}}$ and a three-term discrete load ledger whose terms play the same *roles* as master-equation load slots under the locked high-flux reading; cumulative stage export $\sum L_S$ is path-dependent under circuits even when final $H(Z)$ is fixed; and single-shot $L_S=H(X\mid Y)$ is the information object bounded by Landauer heat under Protocol R. Continuum gravity remains deferred.

---

## Source map for Parts 0--2

| Topic | Canonical / primary path |
|-------|--------------------------|
| $H_c$ / $S_c$ definitions | Section 1 |
| Claims freeze C1--C14, non-claims | Section 3 and Appendix B |
| M11 design + Phase 1--2 | Appendix A · Appendix A |
| Continuum role motivation | Appendix A |
| Composition / path $\sum L_S$ | Appendix A.2 |
| Landauer / $L_S$ | Appendix A.3 |
| Entropy tags A--E | Appendix A · Appendix A |
| Outline / product form | Appendix A |

---
