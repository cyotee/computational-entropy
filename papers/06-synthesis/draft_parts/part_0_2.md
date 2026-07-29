# Computational Entropy and Emergent Gravity: Channels, Load, and a Euclidean Dual (Program Report)

**Document part:** Front matter + §1 Foundations + §2 Classical microstructure  
**Status:** Draft prose under CLAIM_GATE (2026-07-15) — preliminary research; no new theorems  
**Authority:** `synthesis/CURRENT_CLAIMS.md` · `foundations/computational-entropy/definition.md` · `synthesis/m11-idem-to-load.md` · `synthesis/m11d-composition-laws.md` · `synthesis/m11e-landauer-export.md`  
**Companion outline:** `papers/06-synthesis/OUTLINE.md`

---

## Abstract

Computational entropy is defined as the entropy of a map or channel’s **output** distribution: classical Shannon (or differential) \(H_c\), and quantum/gravity von Neumann \(S_c\). In this program, gravity is modeled as a CPTP channel \(\Phi_g\) whose instantaneous demand is a dimensionless **load** \(L\) that reparameterizes proper time via \(d\tau=dt/(1+\alpha L)\). Newtonian Poisson is recovered only through **Path J/M** (Clausius on local horizons → Einstein → weak-field GR, with on-shell load-clock calibration \(\alpha\beta=4\pi G/c^4\)), not a withdrawn pointwise Laplacian identity. A constructive Euclidean dual (**ACD-EW**) links Bianconi’s Gravity-from-Entropy **warm-up** (induced structure metric \(G[\phi]\), Perona–Malik flow) to an observation channel with split load and load clock; residual dual of PM versus heat is **time-windowed** (T1′ / unified pure window \(U_\star\)), and joint toys serve as **pattern witnesses**, not continuum gravity confirmation. Weak-field contact with continuum GfE is a **WEAK PASS** on shared Poisson and a **FAIL** of framework identity (M6/M6b).

This paper is an honest program report: it freezes settled claims, marks rigor labels (constructive / structural / semantic / calibration / external theorem), and states explicit non-claims. Classical IDEM/decay machinery is connected by a design dictionary plus constructive discrete ledgers (Phase 1 AND-gate; Phase 2 multi-step Boolean, tiny SKI, minimal shoe). Relationship witnesses (D13) include **path-dependent** cumulative export cost \(\sum L_S\) under circuit composition (Direct \(\sum L_S\approx 1.189\) vs Circuit \(\approx 2.189\), same final \(H(Z)\)) and **Landauer contact** in which single-shot \(L_S=H(X\mid Y)\) is the bit-count bounded by heat \(Q\ge k_B T\ln 2\cdot H(X\mid Y)\). Discrete load \(L^{\mathrm{disc}}\) is **not** continuum \(L\); scalar \(L\) is **not** metric \(G\); the master equation is **not** continuum GfE.

**Keywords:** computational entropy; CPTP channel; computational load; thermodynamic gravity; Jacobson Clausius; Gravity from Entropy; Perona–Malik; action–channel duality; IDEM; Landauer principle; information export

---

## Non-claims banner

This report is **preliminary research**. Constructions and numerical ledgers are real; **nothing has GR-level certainty**. Do **not** read the body as asserting any of the following without new work:

1. Master equation \(\Leftrightarrow\) Bianconi continuum Gravity-from-Entropy (GfE).  
2. \(L \equiv G\), \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\), or continuum load coefficients identified with Bianconi’s.  
3. Residual dual domination for all \(t\in(0,t_\star]\) (use T1′ / \(U_\star\) instead).  
4. Pure T1′ with no soft hypotheses (PCRH\(_b\) remains ensemble-certified).  
5. Newton from pointwise \(\Phi\propto\rho\) Laplacian (**withdrawn**).  
6. Next-order load terms \(\gamma_L,\delta_L\) equal GfE extras \(D_{\mu\nu},\Lambda_G\).  
7. Lattice denoising as empirical gravity.  
8. External GfE papers established on par with GR.  
9. IDEM/decay fully constructs continuum \(L\) or metric \(G\).

**Type safety (locked throughout):** load \(L\) is a **dimensionless scalar**; structure-induced \(G\) is a **metric** (or edgewise cousin). **\(L \neq G\)**. Discrete three-slot ledgers \(L^{\mathrm{disc}}\) are **not** numerically equal to continuum \(L(\rho,g)\). Entropy objects are tagged when ambiguous (M10: map \(H_c\), \(S_c\), \(H_c^{\mathrm{toy}}\), \(H_c^{\mathrm{game}}\), \(H_c^{\mathrm{disc}}\)).

---

# §1. Foundations — Computational entropy, equivalence, and conservation

## 1.1 Definition of computational entropy

The program’s primary classical and quantum objects are standard information-theoretic entropies of **outputs**, not of internal algorithm complexity alone. The canonical source is `foundations/computational-entropy/definition.md`.

**Premise.** Any map that transforms random inputs induces a marginal distribution on outputs. The predictability of that output law is an entropy. Computational entropy quantifies the statistical pattern of possible results of a computation, independent of the internal mechanics that produced it.

**General case.** For any map \(f\) — deterministic, stochastic, or quantum channel — taking input \(X\sim p_X\) and producing output \(Y\), computational entropy is the entropy of the induced marginal \(p_Y\):

- **Classical discrete** (Tag **A** when unambiguous; Tag **E** on finite M11 maps): Shannon entropy of the output mass function  
  \[
  H_c(f; p_X) := H(Y) = -\sum_y p_Y(y)\,\log_2 p_Y(y).
  \]

- **Classical continuous:** differential Shannon entropy of the output density  
  \[
  H_c(f; p_X) := h(Y) = -\int f_Y(y)\,\log_2 f_Y(y)\,dy.
  \]

- **Quantum / gravity channel** (Tag **B**): von Neumann entropy of the channel output  
  \[
  S_c(\Phi;\rho_X) := S\bigl(\Phi(\rho_X)\bigr) = -\operatorname{Tr}\bigl(\Phi(\rho_X)\log_2\Phi(\rho_X)\bigr).
  \]

In the gravity thread, the gravitational channel \(\Phi_g\) acts on a local density operator \(\rho\), and \(S_c = S(\Phi_g(\rho))\) is the corresponding output entropy (canonical master-equation side: `emergent-gravity/master-equation.md`). Classical \(H_c\) and quantum \(S_c\) share the **role** “entropy of what the channel emits,” not a free symbolic identity of every repository object named \(H_c\).

**Rigor:** definitions are **constructive** in the sense of standard Shannon/von Neumann theory on finite alphabets and density operators; the program’s use of \(S_c\) on \(\Phi_g\) is framework-canonical, not a new information-theory theorem.

## 1.2 Informational equivalence of maps

**Key property.** Two or more different maps — whether deterministic, probabilistic, or quantum — are **informationally equivalent** if they induce output distributions with the same computational entropy. The internal mechanics (algorithm, intermediate randomness, or quantum circuit layout) do not enter the definition; only the final statistical pattern of possible outputs does.

This property is what makes computational entropy a unifying measure across classical gates, lambda reduction, games-as-maps, and CPTP channels: any probability-based prediction that depends only on \(p_Y\) is shared by all maps with that \(p_Y\).

## 1.3 Worked continuous example: \(\sqrt{U}\) versus \(\max(U_1,U_2)\)

Consider two genuinely different functions on independent uniforms \(U,U_1,U_2\sim\mathrm{Uniform}[0,1]\):

- Function 1: \(Y_1=\sqrt{U}\) (square root of one uniform).  
- Function 2: \(Y_2=\max(U_1,U_2)\) (maximum of two independent uniforms).

Both induce the **same** output PDF on \([0,1]\),

\[
f(y)=2y,
\]

and therefore the same differential computational entropy

\[
H_c(Y)=-\int_0^1 2y\log_2(2y)\,dy = -1+\frac{1}{2\ln 2}\approx -0.27865\ \mathrm{bits}.
\]

(The reflected map \(Y_3=\min(U_1,U_2)\) is informationally equivalent under the substitution \(z=1-y\).) Despite completely different internal operations, any prediction that depends only on the law of \(Y\) — e.g. \(\mathbb{P}(Y>0.7)\), mean, variance — is identical. This is the exact content of informational equivalence for continuous classical maps (see foundations definition file).

## 1.4 Global conservation and local transfer: the AND-gate ledger

A common apparent paradox is that a computation can **reduce** local entropy (high-entropy random inputs → lower-entropy structured outputs), seemingly violating the second law. The framework resolves this by **global conservation with local transfer**: entropy is not destroyed; it is exported from the declared system output into environment / preimage registers that an observer of \(Y\) alone does not hold.

### Classical irreversible AND (constructive)

Let \(X=(X_1,X_2)\) be i.i.d. fair bits, so \(H(X)=2\) bits. Let \(Y=X_1\land X_2\). Then

\[
P(Y=1)=\tfrac14,\qquad P(Y=0)=\tfrac34,
\]

and the **declared system** computational entropy is the binary entropy of \(Y\):

\[
H_c = H(Y) = h_2\bigl(\tfrac14\bigr)\approx 0.811278\ \mathrm{bits}.
\]

The “missing” mass relative to the input is **export**, not destruction:

\[
H(X\mid Y)\approx 1.188722\ \mathrm{bits},
\]

and the chain rule for a deterministic map is an identity,

\[
H(X)=H(Y)+H(X\mid Y),
\]

verified to machine precision (\(<10^{-12}\)) in the Phase 1 ledger (`simulations/classical/m11_and_gate_ledger.py`). Rounding for exposition: **output \(\approx 0.811\) bits**, **export \(\approx 1.189\) bits**, total \(2\).

Branch-wise, the export is concentrated on the ambiguous output:

| \(Y\) | \(P(Y)\) | Preimage size | \(H(X\mid Y=y)\) |
|-------|----------|---------------|------------------|
| \(1\) | \(1/4\)  | \(1\)         | \(0\)            |
| \(0\) | \(3/4\)  | \(3\)         | \(\log_2 3\approx 1.585\) |

\[
H(X\mid Y)=\tfrac34\log_2 3\approx 1.188722.
\]

**Program reading.** Local observers of \(Y\) see an apparent reduction; globally, system + environment entropy is accounted by the chain rule. In the gravity narrative, \(\Phi_g\) plays the analogous role of overwriting prior micro-details while exporting distinguishability; continuum load \(L\) quantifies demand of that process (preview in later parts; definition in `emergent-gravity/master-equation.md`). That narrative does **not** by itself prove Einstein equations or continuum GfE.

**Rigor:** finite classical chain-rule accounting is **constructive**; holographic / gravitational language for the environment register remains **semantic** until an explicit continuum map is built (explicitly not claimed here).

## 1.5 Three-stage mental model

The program is organized so that stages are not collapsed into symbolic identity of actions and master equations (see `THEORY.md`, `Claude.md` bootstrap):

```text
STAGE 1 — Computational induction (this paper’s discrete core)
  ρ, Φ_g, S_c / H_c, L, dτ = dt/(1+αL)
  IDEM / decay / games = discrete microstructure (M11 design + Phase 1–2 ledgers)
        │
        ▼
STAGE 2 — Geometric imprint (bridge)
  Structure-induced metric G  (or computational cousin)
  TYPE SAFETY: L is a dimensionless scalar; G is a metric — L ≠ G
        │
        ▼
STAGE 3 — Continuum GfE (macro target)
  Relative entropy of metrics → modified Einstein, Λ_G, G-field
```

**Discipline.** Stage-1 constructive bookkeeping (AND ledgers, composition laws, Landauer contact) **motivates** Stage-2/3 language structurally; it does **not** construct continuum \(L\) or \(G\). Euclidean dual results (ACD-EW, residual T1′) live on a warm-up lattice and are **not** continuum gravitational equivalence. Continuum GfE contact is treated later as shared weak-field Poisson (**WEAK PASS**) without framework identity (**FAIL**).

## 1.6 Notation and type-safety table

| Symbol | Meaning | Type / hygiene |
|--------|---------|----------------|
| \(H_c(f;p_X)\) | Classical computational entropy of map output | Scalar (bits); Tag **A** (foundations); Tag **E** on M11 finite maps |
| \(S_c(\Phi;\rho)\) | Quantum/gravity computational entropy | Von Neumann of channel output; Tag **B** |
| \(H_c^{\mathrm{toy}}\) | Dual-toy residual + edge score | Tag **C** — **not** map \(H(Y)\) |
| \(H_c^{\mathrm{game}}\) | Predictive game Shannon given filtration | Tag **D** — **not** belief-field dual residual |
| \(H_c^{\mathrm{disc}}\) | Finite map / IDEM ledger \(H(Y)\) | Tag **E** (M11) |
| \(\Phi_g\) | Gravitational CPTP channel | Map on density operators |
| \(L\) / \(L(\rho,g)\) | Continuum **computational load** (demand) | **Dimensionless scalar**; clocks \(d\tau\) |
| \(L^{\mathrm{disc}}\) | Discrete three-slot load ledger | Scalar bookkeeping; \(L^{\mathrm{disc}}\neq L(\rho,g)\) |
| \(G\) | Structure-/matter-induced **metric** (GfE / ACD-EW) | Metric (or edgewise cousin); **\(L\neq G\)** |
| \(G_{\mathrm{Newton}}\) | Newton’s constant | Distinct from metric \(G\); appear only in Path M calibration language |
| IDEM | Expanded identity + metadata | Result + arity, decay vector, \(d_f\), AST metrics |
| \(\mathbf{d}\) | Decay / recoverability flags | \(\{0,1\}^n\) or soft \([0,1]^n\) |
| \(d_f\) | Function unidentifiability | \([0,1]\) |
| GfE | Gravity from Entropy (Bianconi) | Continuum macro target; peer literature, not GR-peer foundation |
| ACD-EW | Action–Channel Duality (Euclidean warm-up) | Constructive dual on warm-up layer only |

**Locked type-safety rules.**

1. **\(L\) is a dimensionless scalar.** **\(G\) is a metric.** Never write \(L\equiv G\).  
2. **\(H_c\) / \(S_c\) are entropies of declared outputs**, not internal AST size alone (AST size may enter **energy-like** load proxies).  
3. **\(L^{\mathrm{disc}}\neq L(\rho,g)\)** and discrete bookkeeping weights \(\beta',\gamma',\delta'\) are not Newton-calibrated \(\alpha\beta=4\pi G/c^4\).  
4. Dual-toy lattice field \(\phi\) is a **test signal**, not spacetime geometry and not the M11 microstate of continuum \(\rho\).

## 1.7 Entropy object tags (M10, brief)

Repository prose historically overloaded the token “\(H_c\).” M10 freezes five tags so that load rates \(|\Delta H_c|\) cannot be mixed across layers (`synthesis/m10-sc-vs-toy-hc.md`, `GLOSSARY.md`):

| Tag | Symbol | Object |
|-----|--------|--------|
| **A** | \(H_c(f;p_X)\) | Classical **map** output Shannon / differential entropy (foundations) |
| **B** | \(S_c(\Phi;\rho)\) | Von Neumann entropy of **channel** output \(\Phi(\rho)\) |
| **C** | \(H_c^{\mathrm{toy}}\) | Dual-toy residual + edge entropy (ACD-EW scorecards); supervised residual quality, not unsupervised \(H(Y)\) alone |
| **D** | \(H_c^{\mathrm{game}}\) | Predictive game Shannon \(H(Y_k\mid\mathcal{F}_{k-1})\) |
| **E** | \(H_c^{\mathrm{disc}}\) | Finite map / IDEM / M11 ledger \(H(Y)\) |

**Non-identities (do not assert):** \(H_c^{\mathrm{toy}}\not\equiv S_c\); \(H_c^{\mathrm{disc}}\not\equiv S_c\); \(H_c^{\mathrm{game}}\not\equiv H_c^{\mathrm{toy}}\); \(H_c\not\equiv S_{\mathrm{GfE}}\). House style: bare \(H_c\) only for Tag **A** when unambiguous; theory claims mixing layers must tag.

**Semantic preview of demand (C14).** Prefer reading continuum load \(L\) as demand from the **scale and rate of channel outcomes** — energy-like work, entropy flux / export, and boundary or distinguishability budget — so that active scrambling and high export raise \(L\). That reading is a **semantic** program convention until continuum matching exists; it is the same polarity that discrete ledgers enforce by construction in §2.

---

# §2. Classical microstructure — IDEM, decay, and discrete load (M11 + D12–D13)

## 2.1 The central gap

The repository has long carried two substantial threads that barely touched:

| Thread | Machinery | Gap |
|--------|-----------|-----|
| **Classical / lambda** | IDEM (arity, AST metrics, decay vector, \(d_f\)), games as maps, combinatorial density | Did not feed gravity recoveries |
| **Emergent gravity** | \(\Phi_g\), \(S_c\), load \(L\), master equation, Path J/M Newton | Used only high-level “output entropy” language |

**M11** addresses that gap by a **discrete accounting dictionary**

\[
\text{IDEM / game / lambda step}\;\longrightarrow\; H_c^{\mathrm{disc}}\ \text{and candidate terms in }L^{\mathrm{disc}},
\]

implemented as pure bookkeeping on finite classical models — **without** inventing continuum metric \(G\), rewriting the master equation, or claiming Einstein-from-gates (`synthesis/m11-idem-to-load.md`). Continuum role motivation of the three load slots is a separate design essay (`synthesis/m11c-continuum-motivation.md`): **structural**, not a continuum limit theorem.

## 2.2 IDEM and the decay vector (brief)

An **IDEM** (expanded identity) pairs a map result with metadata: arity, result dimension, decay vector \(\mathbf{d}\), function unidentifiability \(d_f\), and optional AST complexity metrics. In recoverability models:

- \(d_i=0\): input \(x_i\) is recoverable from the declared output under the model;  
- \(d_i=1\): that input information is **lost** to an observer of \(Y\) alone;  
- Soft variants use \(d_i\in[0,1]\) (e.g. \(1-1/|\mathrm{preimage}|\)).

For fair-bit AND, output \(Y=1\) has a unique preimage \((1,1)\), while \(Y=0\) has three preimages; recoverability fails on the latter branch, matching the large conditional entropy \(H(X\mid Y)\). Decay flips \(0\to 1\) are the classical image of **irreversible overwrite**; M11 feeds the **rate** of export or soft decay into the entropy-rate load slot, not an idle “identity stockpile.”

**Rigor:** IDEM ontology and decay semantics are **semantic/structural** classical design. Concrete finite Shannon numbers below are **constructive**. Mapping decay to holographic screen degrees of freedom remains **analogical**, not a theorem.

## 2.3 Operational \(H_c^{\mathrm{disc}}\) and three-slot discrete load

**Operational rule.** Computational entropy on a discrete model is the Shannon entropy of the **declared public output**, not residual dual-toy scores, not internal AST size alone, and not blackjack bankroll EV.

Continuum load has three **roles** (energy-like density, entropy-rate / export, boundary/capacity). M11 defines matching **proxies** with bookkeeping weights \(\beta',\gamma',\delta'\) (default \(1\)), **not** continuum calibrations:

\[
L^{\mathrm{disc}}
=
\beta' L_E^{\mathrm{disc}}
+
\gamma' L_S^{\mathrm{disc}}
+
\delta' L_B^{\mathrm{disc}}.
\]

| Continuum role (master eq) | Discrete proxy | Locked reading |
|----------------------------|----------------|----------------|
| Energy-like work | \(L_E\): ops / redexes / active evaluations this step | Idle identity \(\Rightarrow\) low \(L_E\); active work \(\Rightarrow\) high |
| Entropy-rate / export flux | \(L_S\): \(H(X\mid Y)\) single-shot, or \(|\Delta H_c|\) multi-step, or soft decay-flip rate | High flux / overwrite \(\Rightarrow\) **high** \(L_S\) even when \(H(Y)\) falls |
| Boundary / capacity | \(L_B\): mean soft lost-recoverability mass; residual ensemble entropy ratio; open redex fraction | Open distinguishability budget \(\Rightarrow\) high \(L_B\) |

**Locked \(L\) reading (C14).** Prefer demand from **scale and rate of possible channel outcomes**. Reject as primary story: “how much unreduced identity stockpile remains.” High entropy flux, many open results, and active scrambling raise load; fully reduced idle maps have low load.

**Type safety.** The three discrete slots share **roles** with continuum \(L(\rho,g)\). They do **not** equal continuum coefficients, Newton’s \(G\), or the structure metric \(G\). Same three axes of demand; different mathematical objects.

## 2.4 Phase 1 — AND-gate pure ledger (constructive)

Artifact: `simulations/classical/m11_and_gate_ledger.py`.

| Quantity | Value (fair bits) | Role |
|----------|-------------------|------|
| \(H(X)\) | \(2\) bits | Input possibility mass |
| \(H_c^{\mathrm{disc}}=H(Y)\) | \(h_2(1/4)\approx 0.811278\) | Declared output entropy (Tag **E**) |
| Export \(H(X\mid Y)\) | \(\approx 1.188722\) | Preimage / environment ledger |
| \(L_E^{\mathrm{disc}}\) | \(1\) (one gate op) | Active work |
| \(L_S^{\mathrm{disc}}\) | \(:=H(X\mid Y)\approx 1.188722\) | Single-shot export flux |
| \(L_B^{\mathrm{disc}}\) | \(0.5\) (mean soft lost-recoverability mass) | Open distinguishability after map |
| \(L^{\mathrm{disc}}\) (weights \(1\)) | \(\approx 2.689\) | Sum of independent role proxies |

**Observation.** Output \(H_c\) **drops** (\(\approx 2\to 0.811\)) while demand **rises**. Any monist load proportional to residual output entropy alone would report *low* demand precisely when irreversible overwrite is *expensive* — opposite of the locked reading. Three independent axes appear simultaneously: work (\(L_E\)), export flux (\(L_S\)), and residual recoverability mass (\(L_B\)).

Chain rule residual on the ledger is \(<10^{-12}\). **Rigor:** \(H_c\) and export **constructive**; three-slot assignment **structural bookkeeping**, not continuum \(L\).

## 2.5 Phase 2 — multi-step Boolean, tiny SKI, minimal shoe (brief)

Artifacts under `simulations/classical/`: `m11_multistep_boolean_ledger.py`, `m11_tiny_lambda_ledger.py`, `m11_minimal_shoe_ledger.py`.

**Multi-step Boolean.** An identity baseline on \((X_1,X_2,X_3)\) has \(L_E=L_S=L_B=0\) (idle). An AND step spikes export (\(L_S\approx 1.189\)); a subsequent OR-type step has **lower** export than AND. Ordering is asserted under the locked reading: larger export \(\Rightarrow\) larger \(L_S\). An optional discrete load-clock diagnostic \(k_{\mathrm{eff}}=\sum 1/(1+\alpha' L^{\mathrm{disc}})\) with conventional \(\alpha'=0.1\) is printed only as bookkeeping — **not** continuum proper time.

**Tiny SKI ensemble.** Fixed finite combinator terms under normal-order redex steps: \(L_E=\) mean redex count pre-step; \(L_S=|\Delta H_c|\) under reduction; \(H_c^{\mathrm{disc}}\) drops as term-shape classes concentrate under reduction. Exact Shannon on a finite ensemble; no continuum constants.

**Minimal R/B shoe.** Fixed-sequence multiset (e.g. 6 red + 6 black residual shoe): predictive \(H_c^{\mathrm{game}}\)-adjacent combinatorial entropy of next color; \(L_E=1\) per count-bucket update; \(L_S=|\Delta H_c|\) spikes when predictive entropy jumps; \(L_B=H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)\) residual order-entropy ratio as capacity-like pressure. Honesty: **not** bankroll EV, **not** ACD-EW residual dual \(H_c^{\mathrm{toy}}\), and not multi-deck strategy science (M12 deferred).

**Rigor:** Phase 2 ledgers are **constructive** finite accounting with **structural** continuum role alignment only.

## 2.6 Coupled regions (one paragraph)

A two-region product ledger (`simulations/classical/m11_coupled_regions_ledger.py`) places independent fair-bit pairs on regions \(A\) and \(B\), runs local ANDs, then a coupling XOR “screen” that redistributes shared information. The experiment shows: global chain-rule conservation on the product alphabet; local high export \(\Rightarrow\) high local \(L_S\) while an idle baseline region stays low; coupling redistributes / screens information without magical destruction; optional per-region diagnostic \(k_{\mathrm{eff}}\). Product regions are **not** spacetime patches, **not** continuum \(\rho\), and **not** a derivation of local energy density fields. They make multi-site classical conservation **constructive** before any hydrodynamic aspiration (`m11c` §5–6).

## 2.7 Composition path dependence (D13 / M11d)

Source: `synthesis/m11d-composition-laws.md`; witness `simulations/classical/m11_composition_ledger.py`. Entropy object: Tag **E**. Layer: Stage-1 classical only.

**Two composition models (must not be conflated).**

| Model | Definition |
|-------|------------|
| **Pure cascade** | \(Y=f(X)\), \(Z=g(Y)\) — next stage sees only \(Y\) |
| **Circuit** | Later stages may still read residual input wires + intermediates |

Standard lemmas (finite classical):

- **Lemma A (chain rule):** \(H(X)=H(Y)+H(X\mid Y)\) for deterministic \(Y=f(X)\).  
- **Lemma B (export additivity on pure cascade):** \(H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)\).  
- **Lemma C (DPI):** \(H(g(Y))\le H(Y)\).  
- **Lemma D:** path \(L_E\) is additive by counting ops.  
- **Lemma E (path dependence of cumulative \(L_S\)):** \(\sum L_S\) is **not** a function of the final map alone.

**Explicit Direct vs Circuit witness (fair bits \(X=(X_1,X_2)\)).**

| Path | Stages | Final \(Z\) | \(H(Z)\) | \(\sum L_S\) (stage exports) |
|------|--------|-------------|----------|------------------------------|
| **Direct \(D\)** | \(Z=X_1\land X_2\) | AND law | \(\approx 0.811278\) | \(H(X\mid Z)\approx 1.188722\) |
| **Circuit \(C\)** | \(Y=X_1\), then \(Z=Y\land X_2\) (wire \(X_2\) retained) | same AND law | \(\approx 0.811278\) | \(H(X\mid Y)+H(X\mid Z)=1+1.188722=2.188722\) |

Thus, in rounded form used for program citation:

\[
\sum L_S(D)\approx 1.189,\qquad
\sum L_S(C)\approx 2.189,\qquad
H(Z)\ \text{identical on both paths}.
\]

**Crucial distinction.**

```text
H(X|Z)           — property of the final I/O pair (path-independent for fixed final map)
Σ_s L_S^(s)      — property of the pipeline (path-dependent under circuit stages)
```

Paying for an intermediate publish/export that is later re-used in an irreversible gate **raises demand along the path**, even when the final output law is unchanged. Load is not “final \(H_c\) alone.” Soft-recoverability \(L_B\) is likewise **not** freely additive under regional sums or stage sums without a fixed global coordinate convention (Lemma F counterexamples).

**Rigor:** Lemmas A–C and the Direct/Circuit numbers are **constructive**; continuum composition of \(L(\rho,g)\) is **not claimed**.

## 2.8 Landauer contact for export and \(L_S\) (D13 / M11e)

Source: `synthesis/m11e-landauer-export.md`; witness `simulations/classical/m11_landauer_and_ledger.py`.

On the same finite AND model, fix an explicit **Protocol R** (reset after AND): compute \(Y=f(X)\), keep only \(Y\) as public system output, and thermalize residual input registers conditional on \(Y\). The average number of erased bits is the export

\[
n_{\mathrm{erased}} := H(X\mid Y).
\]

**Landauer’s principle** (external theorem; not re-proved here) then supplies the standard lower bound on average heat dissipated to a bath at temperature \(T\):

\[
Q \;\ge\; k_B T \ln 2 \cdot H(X\mid Y)
\qquad\text{(Shannon in bits)}.
\]

In units of \(k_B T\ln 2\), the bound **equals** the export ledger quantity. M11’s single-shot entropy-rate slot is defined as that same object:

\[
L_S^{\mathrm{disc}} := H(X\mid Y)
\quad\Rightarrow\quad
Q \;\ge\; k_B T \ln 2 \cdot L_S^{\mathrm{disc}}
\quad\text{(single-shot AND / Protocol R)}.
\]

| Quantity | Fair-bit AND |
|----------|----------------|
| \(H(Y)=H_c^{\mathrm{disc}}\) | \(\approx 0.811278\) |
| Export \(H(X\mid Y)\) | \(\approx 1.188722\) |
| Landauer \(Q_{\min}/(k_B T\ln 2)\) | \(=H(X\mid Y)\approx 1.188722\) |
| \(L_S^{\mathrm{disc}}\) | \(=\) export by definition |

**Optional reversible dilation (Bennett-style, structural).** A reversible embedding can park preimage information in **garbage** \(G\); public \(H(Y)\) may match the irreversible case, but eventual erasure of \(G\) still costs \(\ge H(X\mid Y)\). Export does not vanish under reversible accounting; it is deferred until garbage reset.

**What this contact is and is not.**

| Allowed | Forbidden from M11e alone |
|---------|---------------------------|
| Export \(H(X\mid Y)\) is the average erased-bit count under Protocol R | Newton \(G\) or Path J/M calibration from Landauer |
| \(L_S^{\mathrm{disc}}\) is that information object | \(\hbar\), holography, or \(S_{\mathrm{BH}}=A/4G\hbar\) from AND heat |
| Thermodynamic bookkeeping contact only | Continuum \(L_S\) density = GR/GfE heat flux |
| | \(L\equiv G\) or \(L^{\mathrm{disc}}\equiv L(\rho,g)\) |

**Rigor:** finite Shannon identities **constructive**; Landauer inequality **external theorem**; identification of \(L_S\) with the Landauer bit-count **structural contact**. Conversion factor \(k_B T\ln 2\) is standard thermodynamics, **not** fitted to gravity scales.

## 2.9 Why three load terms? (structural motivation)

Discrete evidence simultaneously requires three independent **axes of demand** (`m11c`):

1. **How hard is the machine working?** (\(L_E\))  
2. **How fast is possibility being realized / exported?** (\(L_S\))  
3. **How much distinguishability budget remains open versus capacity?** (\(L_B\))

A monist load \(L\propto H_c\) alone fails on irreversible AND (output entropy low, export high). A monist “remaining AST size” fails the locked reading when the stockpile is idle. Shoe dynamics separate nearly constant update cost (\(L_E\)), flux spikes (\(L_S\)), and smoothly shrinking residual multiset capacity (\(L_B\)). Continuum three-term \(L\) is the **same role split** at continuum language level — **structural motivation**, not uniqueness, and not a hydrodynamic limit of IDEM.

## 2.10 Section non-claims

Do **not** assert from M11 Phase 1–2, composition, Landauer contact, or coupled-region ledgers:

1. Master equation \(\Leftrightarrow\) continuum GfE.  
2. \(L\equiv G\), \(L^{\mathrm{disc}}\equiv L(\rho,g)\), or \(S_c\equiv\operatorname{Tr} g\ln G^{-1}\).  
3. IDEM/decay **constructs** continuum \(L\) or metric \(G\) (PROGRESS non-claim §2.3.9).  
4. Newton / Einstein recovery from gates, SKI terms, shoes, or Landauer heat.  
5. Lattice dual toys or blackjack-belief dual **are** gravity or **are** true game predictive \(H_c^{\mathrm{game}}\).  
6. Path J/M calibration constants \(\alpha,\beta,\gamma,\delta,\epsilon_0\) are fixed by discrete proxies.  
7. Decay vector components **are** Hawking radiation degrees of freedom.  
8. Primary load = idle remaining identity stockpile.  
9. Continuum composition laws of \(L(\rho,g)\) or \(\lvert dS_c/d\tau\rvert\) from finite Boolean cascades.  
10. Dual-toy residual \(H_c^{\mathrm{toy}}\) equals gate export or Landauer bits.

**Allowed claim form (program-level).** On finite classical models \(\mathcal{M}\), we define constructive \(H_c^{\mathrm{disc}}\) and a three-term discrete load ledger whose terms play the same *roles* as master-equation load slots under the locked high-flux reading; cumulative stage export \(\sum L_S\) is path-dependent under circuits even when final \(H(Z)\) is fixed; and single-shot \(L_S=H(X\mid Y)\) is the information object bounded by Landauer heat under Protocol R. Continuum gravity remains deferred.

---

## Source map for Parts 0–2

| Topic | Canonical / primary path |
|-------|--------------------------|
| \(H_c\) / \(S_c\) definitions | `foundations/computational-entropy/definition.md` |
| Claims freeze C1–C14, non-claims | `synthesis/CURRENT_CLAIMS.md` |
| M11 design + Phase 1–2 | `synthesis/m11-idem-to-load.md` · `simulations/classical/` |
| Continuum role motivation | `synthesis/m11c-continuum-motivation.md` |
| Composition / path \(\sum L_S\) | `synthesis/m11d-composition-laws.md` |
| Landauer / \(L_S\) | `synthesis/m11e-landauer-export.md` |
| Entropy tags A–E | `synthesis/m10-sc-vs-toy-hc.md` · `GLOSSARY.md` |
| Outline / product form | `papers/06-synthesis/OUTLINE.md` |

---

*End of draft Parts 0–2. Subsequent parts (channels/load, Path J/M Newton, ACD-EW dual, M6 contact, open program, conclusion) are out of scope for this file.*
