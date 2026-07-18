# M11 — IDEM / Decay / Classical Models → \(H_c\) and Load \(L\)

**M-id:** M11  
**Status:** **Design + Phase 1 + Phase 2 constructive** (2026-07-15) — AND-gate + multi-step Boolean + tiny SKI + minimal shoe ledgers; no continuum derivation  
**Depends on:** [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) · [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) · [../THEORY.md](../THEORY.md) §3 · [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2.1 / §7.1.B  
**Feeds:** M12 true game channel (shoe is M12-adjacent seed); eventual microstructure story for \(\Phi_g\)  
**Phase 1 artifact:** [`simulations/classical/m11_and_gate_ledger.py`](../simulations/classical/m11_and_gate_ledger.py)  
**Phase 2 artifacts:** [`m11_multistep_boolean_ledger.py`](../simulations/classical/m11_multistep_boolean_ledger.py) · [`m11_tiny_lambda_ledger.py`](../simulations/classical/m11_tiny_lambda_ledger.py) · [`m11_minimal_shoe_ledger.py`](../simulations/classical/m11_minimal_shoe_ledger.py) · [README](../simulations/classical/README.md)  
**Related:** [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) (D9) · [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) · [../simulations/bridging/DESIGN_blackjack_belief_dual.md](../simulations/bridging/DESIGN_blackjack_belief_dual.md) (honesty limits) · root IDEM drafts  

**Stance:** Preliminary research. Every mapping below is labeled **semantic / structural / constructive**. Prefer structural candidates over forced formulas with fake continuum constants. Nothing here claims Einstein equations, continuum GfE, or \(L \equiv G\).

---

## 1. Problem & motivation (central gap)

The repository has two substantial threads that barely touch:

| Thread | Machinery | Gap |
|--------|-----------|-----|
| **Classical / lambda** | IDEM (arity, AST metrics, decay vector, \(d_f\)), games as maps, combinatorial density | Never feeds gravity recoveries |
| **Emergent gravity** | \(\Phi_g\), \(S_c\), load \(L\), master eq, Path J/M Newton | Uses only high-level “output entropy” language |

**THEORY central gap:** gravity work does **not** use lambda/IDEM/decay-vector/AST machinery.  
**PROGRESS §7.1.B:** M11 is the highest-leverage unique-value avenue once the Euclidean dual is frozen: define how IDEM/decay (and games) contribute to \(H_c\) and optionally to \(L\), with the locked reading that **high entropy flux / many open results / active scrambling ⇒ higher \(L\)**, not “identity stockpile remaining.”

**M11 scope (this note):** design a **discrete accounting dictionary**  
\[
\text{IDEM / game / lambda step} \;\longrightarrow\; H_c \;\text{and candidate terms in } L
\]  
so a later session can implement pure bookkeeping on one model **without** inventing continuum \(G\) or rewriting the master equation.

**Out of scope for M11 design/impl:** continuum metric \(G\), Bianconi GfE identity, Lorentzian lift, ACD-EW lattice \(\phi\) as spacetime, Newton recovery from discrete toys.

---

## 2. Notation & type safety

| Symbol | Meaning | Type | Source |
|--------|---------|------|--------|
| \(H_c(f; p_X)\) | Classical computational entropy | scalar (bits) = Shannon/differential of **output** \(Y\) | foundations |
| \(S_c(\Phi;\rho)\) | Quantum/gravity computational entropy | von Neumann of channel **output** | master-equation |
| \(\Phi\) / \(\Phi_g\) | Computation / gravitational CPTP channel | map on distributions / density ops | master-equation |
| \(L\) | Computational **load** (demand scalar) | dimensionless scalar | master-equation |
| \(G\) | Matter/structure-induced **metric** (GfE / ACD-EW) | metric (or Euclidean scalar field proxy) | GfE / dual toys |
| IDEM\(_f\) | Expanded identity: \((f(\mathbf{x}), \mathrm{info}_f)\) | result + metadata | classical drafts |
| \(\mathbf{d}=(d_1,\ldots,d_n)\) | Input recoverability flags | \(\{0,1\}^n\) (or soft \([0,1]^n\)) | IDEM |
| \(d_f\) | Function unidentifiability | \([0,1]\) | IDEM / \(d_f\) notes |
| \(\phi\) (dual toys) | Test signal / belief field on lattice | **not** M11 microstate | ACD-EW |

### Type safety (locked)

1. **\(L\) is a dimensionless scalar.** **\(G\) is a metric (or metric-like field).** Never write \(L \equiv G\).  
2. **\(H_c\) / \(S_c\) are entropies of the channel’s *output* distribution/state**, not of internal algorithm complexity alone, not residual vs ground truth unless that residual *is* the defined output (see §4 honesty).  
3. **Discrete state ≠ lattice \(\phi\) from dual toys as spacetime.** Dual-toy \(\phi\) is a Euclidean warm-up test signal; M11 microstates are terms, beliefs, or game registers.  
4. **Locked \(L\) reading** ([PROGRESS_REPORT](../PROGRESS_REPORT.md) §2.1 / §4): demand from scale/rate of possible channel outcomes (energy-like work + entropy production/flux + boundary/distinguishability budget).  
   - Active identity loss, scrambling, many open results, high entropy **flux** ⇒ **higher** \(L\).  
   - **Not:** “how much unreduced identity stockpile remains” as the primary load story.

Canonical continuum template (for *structural* term alignment only — not claimed as discrete definition):

\[
L(\rho,g)
=
\beta \frac{E[\rho]}{V\epsilon_0}
+
\gamma \left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}}
+
\delta \frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)}.
\]

M11 proposes **discrete proxies** \(L_E^{\mathrm{disc}}, L_S^{\mathrm{disc}}, L_B^{\mathrm{disc}}\) with the **same three-slot roles**, not numerical equality of \(\beta,\gamma,\delta\) to continuum calibrations.

---

## 3. Discrete ontology

### 3.1 What is a microstate?

Pick **one** primary discrete world per experiment. Do not mix ontologies in a single accounting ledger without an explicit product construction.

| Ontology | Microstate \(s\) | Ensemble / prior | Preferred first model |
|----------|------------------|------------------|------------------------|
| **Lambda / term** | Term \(t\) (or AST) + optional environment; or IDEM pair \((y,\mathrm{info}_f)\) after a reduction step | Distribution over input terms / free variables | Small closed combinator fragment or irreversible gate |
| **IDEM metadata state** | \((y, \mathbf{d}, d_f, \text{arity}, \text{AST metrics})\) for a fixed map \(f\) under input measure \(p_X\) | \(p_X\) (or Bayesian posterior over \(f\)) | AND-gate / \(f_{\mathrm{max}}\) style examples from foundations |
| **Game belief** | Hidden deck / shoe state \(\omega\); agent belief \(b\) (count, residual multiset, strategy state) | Shoe prior + observation channel | Blackjack **strategy/count** as channel (true \(H_c\)), not belief-field dual |

**Explicit exclusion:** lattice field \(\phi\) from ACD-EW joint toys is **not** the M11 microstate of spacetime. It may later be a *separate* dual-pattern IC (already done for blackjack *belief*). M11 targets classical computational models → \(H_c\) and \(L\) **bookkeeping**.

**Rigor:** ontology choice itself is **semantic** (stage-1 microstructure intent). Concrete state spaces below are **structural** candidates once fixed in code.

### 3.2 What is one channel step \(\Phi\)?

| Ontology | One step of \(\Phi\) | Clock unit |
|----------|----------------------|------------|
| Lambda | One reduction step (β-reduce redex; or small-step operational semantics); optionally multi-step “macro step” = one normal-order redex | Discrete step index \(k\); \(\tau\) only if load clock is defined |
| IDEM / pure map | One application of \(f\) (or one observation of \((X,Y=f(X))\)); metadata \(\mathbf{d},d_f\) updated from I/O | One evaluation |
| Game | One observation update (card drawn → belief \(b\mapsto b'\)) **or** one strategy action (hit/stand/bet given state) | Draw index / decision index |

**Semantic:** \(\Phi\) = computation/observation that produces a new output distribution (or posterior).  
**Structural:** step must induce a well-defined map on the chosen state space and a measurable output \(Y_k\).  
**Constructive:** not yet — no implemented discrete \(\Phi\) ledger in-repo for M11.

### 3.3 What is “output” for \(H_c\)?

Canonical rule: **entropy of the induced marginal of whatever the channel emits as its public result**, not of hidden internal registers unless those *are* declared the output.

| Model | Declared output \(Y\) | \(H_c\) |
|-------|----------------------|---------|
| Gate / function \(f\) | \(Y=f(X)\) under \(p_X\) | \(H(Y)\) (Shannon) |
| Reduction stream | Observable normal form / WHNF / typed result after \(k\) steps (choose once) | \(H(Y_k)\) under input measure |
| Game prediction | Predicted next-card class / action / EV bin — **must match classical game notes if claiming strategy \(H_c\)** | \(H(Y\mid b)\) or \(H(Y)\) of predictor map |
| Game belief dual (existing) | Residual/edge channel on lattice \(\phi\) | **Different object** — dual-toy \(H_c\); do not confuse with strategy \(H_c\) ([DESIGN_blackjack_belief_dual](../simulations/bridging/DESIGN_blackjack_belief_dual.md) §3) |

---

## 4. Operational \(H_c\)

### 4.1 Canonical definition (do not reinvent)

From [foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md):

\[
H_c(f; p_X) := H(Y),\qquad Y = f(X),\quad
H(Y)=-\sum_y p_Y(y)\log_2 p_Y(y)
\]

(or differential \(h(Y)\); quantum: \(S_c=S(\Phi(\rho))\)).

**Key property:** only the **statistical pattern of outputs** matters; two algorithms with the same \(p_Y\) share \(H_c\).

### 4.2 Operational recipes for IDEM / games

| Setting | Operational \(H_c\) | Notes |
|---------|---------------------|-------|
| **Finite map** | Exact \(H(Y)\) from pushforward \(p_Y = f_\# p_X\) | Prefer exact when \(|X|\) small |
| **Sampled map** | Histogram / kernel estimate of \(p_Y\) under Monte Carlo \(X\sim p_X\) | Report bias; not continuum \(S_c\) |
| **IDEM-enriched output** | Default: entropy of **result component** \(Y\) only. Optional: joint \(H(Y,\mathrm{info}_f)\) only if info is *emitted* as part of the channel output | Metadata for free does not automatically change \(H_c\) |
| **Sequential game** | At step \(k\): \(H_c^{(k)} = H(Y_k \mid \mathcal{F}_{k-1})\) for one-step predictive channel, **or** \(H(Y_k)\) for unconditional map | Fix filtration \(\mathcal{F}\) (info available to agent) once |
| **Lambda multi-step** | After \(k\) reductions: entropy of observable result under random inputs / random reduction strategy if nondeterministic | Strategy choice is part of channel definition |

### 4.3 Honesty boundaries

| Allowed | Forbidden as “\(H_c\)” without rename |
|---------|--------------------------------------|
| Shannon of declared output | Internal AST size alone (that is complexity / energy proxy → \(L_E\)) |
| Predictive entropy of next card under count \(b\) | Dual-toy residual \(H_R+\lambda_e H_{\mathrm{edge}}\) **called** classical strategy entropy |
| Drop \(\Delta H_c = H_c^{(k)}-H_c^{(k+1)}\) as **flux** into \(L_S\) | Claiming local drop violates second law without environment export (§6) |

**Rigor of operational \(H_c\):** **constructive** in pure finite models (gates, small decks with exact combinatorics); **structural** for lambda fragments once output observable is fixed; **semantic** for continuum \(S_c\) identification (M10, out of scope).

---

## 5. Candidate map \(L \leftarrow\) IDEM / game quantities

Continuum three-term template → discrete **roles**. Coefficients \(\beta',\gamma',\delta'\) are **bookkeeping weights** (set to 1 or tuned within one model), **not** Newton-calibrated \(\alpha\beta=4\pi G/c^4\).

\[
L^{\mathrm{disc}}
=
\beta' \, L_E^{\mathrm{disc}}
+
\gamma' \, L_S^{\mathrm{disc}}
+
\delta' \, L_B^{\mathrm{disc}}.
\]

| Continuum term | Discrete proxy (candidate) | Interpretation under locked \(L\) reading | Rigor |
|----------------|----------------------------|------------------------------------------|-------|
| \(\beta E[\rho]/(V\epsilon_0)\) **energy-like** | **Active work / complexity load** \(L_E^{\mathrm{disc}}\): # active redexes; AST size of current term; # SUCC/ops per step; stake or bet mass under strategy; count-update arithmetic cost | More simultaneous computational work ⇒ higher demand | **Structural** (complexity ↔ energy density analogy); **not** constructive continuum match |
| \(\gamma \|dS_c/d\tau\|_{\mathrm{reg}}\) **entropy-rate** | \(L_S^{\mathrm{disc}} = \bigl\|\Delta H_c / \Delta k\bigr\|\) **or** \(N_{\mathrm{flip}}/ \Delta k\) = # decay-vector component flips per step (soft: \(\sum_i |\Delta d_i|\)) | Fast output-entropy drop **or** rapid irreversible overwrite rate ⇒ high flux ⇒ **high** \(L\) | **Structural (strong candidate)** — THEORY §3.2 |
| \(\delta S_{\mathrm{boundary}}/S_{\mathrm{BH}}\) **boundary / capacity** | \(L_B^{\mathrm{disc}}\): ensemble \(d_f\) (unidentifiability of \(f\)); log of # still-distinguishable world-lines / residual shoe multisets; fraction of inputs with \(d_i=1\) (lost recoverability) averaged over ensemble; “distinguishability budget” vs max register size | Large open possibility space at the boundary of what can still be registered ⇒ high load; saturated unique ID ⇒ high holographic-like pressure | **Structural (candidate)** — THEORY §3.2; softest of the three |

### 5.1 Preferred concrete proxies (no fake continuum constants)

| Term | Preferred first-implementation formula | Avoid initially |
|------|----------------------------------------|-----------------|
| \(L_E\) | \(L_E = n_{\mathrm{redex}}\) or \(L_E = \|\mathrm{AST}\| / \|\mathrm{AST}\|_{\mathrm{ref}}\) or ops-per-step | Planck \(\epsilon_0\), \(G\), \(c\) |
| \(L_S\) | \(L_S = |H_c^{(k)}-H_c^{(k+1)}|\) with exact \(H_c\); dual option \(L_S^{\mathrm{decay}}=\|\mathbf{d}^{(k+1)}-\mathbf{d}^{(k)}\|_1\) | Claiming equality to continuum \(\|dS_c/d\tau\|\) |
| \(L_B\) | \(L_B = \langle d_f \rangle_{\mathrm{ens}}\) or \(H(\Omega_{\mathrm{residual}})/H(\Omega_{\mathrm{max}})\) (residual shoe entropy over max) | \(S_{\mathrm{BH}}=A/4G\hbar\) on a game table |

### 5.2 Sign / polarity checklist (locked reading)

| Situation | \(H_c\) | Expected \(L\) effect |
|-----------|---------|------------------------|
| Many open results, high predictive uncertainty, active counting | high \(H_c\) | \(L_B\) high; \(L_E\) may be high if strategy is complex |
| Rapid learning: \(H_c\) drops fast over few steps | \(\Delta H_c < 0\) large | \(L_S = |\Delta H_c|\) **high** during the drop (flux), not low |
| Scrambling / irreversible overwrite (many \(d_i:0\to 1\)) | local \(H(Y)\) may fall | \(L_S^{\mathrm{decay}}\) **high** — loss is *work*, not free |
| Idle identity map, fully reduced, no observation | low activity | \(L\) low — **not** “stockpile of unused identity” as high load |
| After certainty reached (\(H_c=0\)) with no further ops | flat \(H_c\) | \(L_S\to 0\); \(L_E\to 0\) if no redexes; \(L_B\) may stay if residual unidentifiability of *which* \(f\) was used |

**Anti-pattern (explicitly rejected):**  
“Load = remaining unreduced term size as *potential identity still to compute*” as the *primary* story when that stockpile is idle. Idle complexity can enter \(L_E\) only if it is **active** work (live redexes / live strategy evaluation). Stockpile without flux is not high demand under the locked reading.

### 5.3 Relation to ACD-EW split load (do not collapse)

| ACD-EW (Euclidean dual toys) | M11 discrete |
|------------------------------|--------------|
| \(L_E \propto \mathbb{E}[(\nabla\hat\phi)^2]\) tracks \(G-1\) | \(L_E\) = redex/AST/ops — **different object** |
| \(L_S \propto |\Delta H_c|/\Delta t\) residual channel | \(L_S\) = \(|\Delta H_c|\) of **declared classical output** — same *role*, different \(H_c\) |
| \(L_B\) gradient saturation diagnostic | \(L_B\) = \(d_f\) / residual ensemble distinguishability |

**Rigor:** same **three-slot role structure** is **semantic / structural** across threads; numerical or formula identity is **not** claimed (**non-constructive**).

---

## 6. Decay vector & information export

### 6.1 IDEM decay vector (classical)

From IDEM drafts / [GLOSSARY](../GLOSSARY.md):

- \(d_i = 0\): input \(x_i\) recoverable from output (in the intended recoverability model).  
- \(d_i = 1\): input information **lost** to the observer of \(Y\) alone.  
- \(d_f \in [0,1]\): unidentifiability of \(f\) from observed I/O (Bayesian / static).

Example (foundations AND-gate intuition): \(Y=X_1\land X_2\) with fair bits — many inputs share \(Y=0\); recoverability fails for those preimages; local \(H(Y)\approx 0.811 < H(X_1,X_2)=2\).

### 6.2 Mapping to gravity-side language (candidate only)

| Classical | Gravity-side analogy | Rigor |
|-----------|----------------------|-------|
| \(d_i: 0\to 1\) (irreversible loss of input recoverability) | Local overwrite; exported distinguishability | **Structural (candidate)** — THEORY §3.1 |
| Exported entropy \(H(X)-H(Y)\) (for deterministic \(f\), under suitable conditions related to preimage structure) | Environment / “screen” register holding path information | **Structural** for finite classical systems; **semantic** for holographic screen |
| \(d_f\) high | Observer cannot name the channel law | **Analogical / structural soft** vs boundary entropy ratio |
| Infinite reduction paths / underivability | Inaccessible fine-grained history | **Analogical** (THEORY §3.1) |

### 6.3 Global conservation story (align foundations)

Foundations: globally, system + environment entropy conserved; locally, observers see reduced \(H(Y)\) because prior micro-details are irreversibly overwritten.

**M11 bookkeeping rule:**

1. Track **system** output entropy \(H_c = H(Y)\).  
2. Track **export ledger** \(H_{\mathrm{export}}\) (preimage multiplicity / environment bits / lost \(d_i\) information) so that for deterministic finite maps under uniform input,  
   \(H(X) = H(Y) + H(X\mid Y)\) (chain rule) remains the sanity check.  
3. Feed **rate of export** (or rate of \(\mathbf{d}\)-flips), not the static stock of lost bits alone, into \(L_S^{\mathrm{decay}}\).

**Rigor:** chain-rule accounting is **constructive** for finite classical maps. Holographic / Hawking language remains **semantic**.

---

## 7. Worked micro-example

Two micro-examples are sketched; **prefer (A) for Phase 1** if implementing pure accounting without a full shoe engine. (B) is the game-native path (ties M12).

### 7.A Irreversible AND-gate (one page)

**Setup.**  
- Inputs: \(X_1,X_2\) i.i.d. fair bits; \(H(X_1,X_2)=2\).  
- Channel step: single evaluation \(Y = X_1 \land X_2\).  
- IDEM-style decay (coarse): for output \(Y=1\), both inputs recoverable as \((1,1)\) \(\Rightarrow\) e.g. \(\mathbf{d}=(0,0)\); for \(Y=0\), inputs not uniquely recoverable \(\Rightarrow\) \(\mathbf{d}=(1,1)\) on that branch (or soft recoverability \(1-1/|\mathrm{preimage}|\)).

**Output distribution.**  
\(P(Y=1)=1/4\), \(P(Y=0)=3/4\),

\[
H_c = H(Y) = h_2(1/4) \approx 0.811\ \mathrm{bits}.
\]

**Local drop.** \(\Delta H = H(X)-H(Y) \approx 1.189\) bits accounted as \(H(X\mid Y)\) (export / preimage uncertainty), not destruction.

**Candidate load bookkeeping (one step, weights \(=1\)):**

| Term | Value (illustrative) | Rationale |
|------|----------------------|-----------|
| \(L_E\) | \(1\) (one gate op) or \(2\) (two inputs touched) | Active work this step |
| \(L_S\) | \(\|2 - 0.811\| \approx 1.189\) if comparing input joint entropy to output, **or** \(0\) if only multi-step \(\Delta H_c\) is allowed and this is a single-shot map | Prefer: define \(H_c^{\mathrm{in}}=H(X)\) only if the *channel output* of a prior id-map was \(X\); else set single-shot \(L_S := H(X\mid Y)\) as **export rate per evaluation** |
| \(L_B\) | \(d_f\): many Boolean maps share truth tables on sparse samples; for known AND, \(d_f\approx 0\). Ensemble: \(\langle \#\{x:d_i(x)=1\} \rangle / n\) high for AND | Distinguishability budget / lost recoverability mass |

**Locked reading check:** the evaluation is an **active irreversible overwrite** of input distinguishability → **high** \(L_S\) (flux of export) and nonzero \(L_E\), even though the **output** distribution is *more* predictable than the input. Load is not “how much identity is left inside the gate.”

**IDEM metadata (sketch).**  
Arity \(2\); result dim \(1\); decay \(\mathbf{d}\) branch-dependent; \(d_f \approx 0\) if the observer knows \(f=\mathrm{AND}\), higher if \(f\) is unknown among Boolean maps.

**Rigor:** \(H_c\) **constructive**; export via \(H(X\mid Y)\) **constructive**; load triple **structural bookkeeping**, not continuum \(L\).

---

### 7.B Blackjack: count update as channel step (pattern for M12)

**Setup (minimal).**  
- Shoe residual multiset \(\Omega_k\) after \(k\) draws; true next-card class \(C_{k+1}\).  
- Agent belief \(b_k\) (e.g. Hi-Lo running count + decks remaining).  
- Predictive channel: \(Y_k =\) predicted class distribution \(p(\cdot\mid b_k)\) or hard class \(\hat c(b_k)\).  
- **Classical \(H_c^{(k)} = H(C_{k+1}\mid b_k)\)** under true shoe measure (or cross-entropy / log-loss if using a scoring rule — if log-loss, label it \(H_c^{\mathrm{score}}\), not pure Shannon of a deterministic map).

**One step \(\Phi\):** observe card \(c_{k+1}\), update \(b_k \mapsto b_{k+1}\), optionally update strategy action.

**Bookkeeping:**

| Term | Proxy |
|------|--------|
| \(L_E\) | Cost of strategy: # count classes / table lookups / SUCC ops per draw (classical cost model in research/games notes) |
| \(L_S\) | \(\|H_c^{(k)}-H_c^{(k+1)}\|\) as info arrives (fast entropy drop late in shoe ⇒ high flux) |
| \(L_B\) | Residual shoe entropy \(H(\Omega_k)/H(\Omega_0)\), or \(d_f\) of “which counting system” from observed bet pattern |

**Honesty:**  
- Existing **blackjack belief dual** (lattice \(\phi\)) is **pattern-only** ACD-EW; its \(H_c\) is residual/edge, **not** this predictive \(H_c\).  
- Do **not** claim bankroll EV, gravity, or continuum \(G\) from either ledger.  
- M12 can deepen true game \(H_c\); M11 only needs the **slot map** above.

**Rigor:** predictive entropy under exact residual multiset is **constructive** in principle (combinatorial shoe); full multi-deck engine is engineering. Load map remains **structural**.

---

## 8. Rigor board

| Claim | Level | Status |
|-------|-------|--------|
| \(H_c\) = entropy of declared channel output | **Constructive** (definition) | Canonical foundations |
| Classical \(H_c\) generalizes to \(S_c = S(\Phi_g(\rho))\) | **Semantic** (stated) | Canonical; M10 for residual-toy vs von Neumann |
| Decay flips ↔ local information export | **Structural candidate** | Strong classical analogy; not holographic theorem |
| \(L_S^{\mathrm{disc}} \leftrightarrow \gamma\|dS_c/d\tau\|\) role | **Structural** | Best discrete–continuum role match |
| \(L_E^{\mathrm{disc}} \leftrightarrow\) energy-density term role | **Structural / analogical** | Needs chosen complexity measure |
| \(L_B^{\mathrm{disc}} \leftrightarrow\) boundary/Bekenstein ratio role | **Structural soft / analogical** | \(d_f\) / residual ensemble entropy as proxy |
| Discrete \(L^{\mathrm{disc}}\) **equals** continuum \(L(\rho,g)\) | **Not claimed** | Forbidden without continuum limit program |
| IDEM constructs continuum metric \(G\) | **Not claimed** | Explicit non-claim (PROGRESS §2.3.9) |
| Three-slot load form useful for discrete accounting | **Semantic design** | This note |
| Phase-1 pure accounting on AND-gate | **Constructive** | `simulations/classical/m11_and_gate_ledger.py` |
| Phase-2 multi-step Boolean / SKI / shoe ledgers | **Constructive** | `simulations/classical/m11_*_ledger.py` (Phase 2) |
| ACD-EW dual toys implement M11 | **False** | Different \(H_c\) object; dual is Euclidean warm-up only |

---

## 9. Non-claims

Do **not** assert from this design (or from Phase-1 accounting alone):

1. Master equation \(\Leftrightarrow\) continuum GfE (Bianconi).  
2. \(L \equiv G\), \(L^{\mathrm{disc}} \equiv L(\rho,g)\), or \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\).  
3. IDEM/decay **constructs** continuum \(L\) or \(G\) (PROGRESS non-claim §2.3.9).  
4. Newton / Einstein recovery from IDEM, AND-gate, or blackjack.  
5. Lattice denoising dual or blackjack-belief dual **is** gravity or **is** true game \(H_c\).  
6. Path J/M calibration constants \(\alpha,\beta,\gamma,\delta,\epsilon_0\) are fixed by discrete proxies.  
7. Decay vector components **are** Hawking radiation degrees of freedom.  
8. \(L\) is primarily remaining identity stockpile (idle unreduced size).  
9. Any single numerical “proof” that \(\gamma' L_S^{\mathrm{disc}}\) equals continuum entropy production.

**Allowed claim form after Phase 1:**  
“On model \(\mathcal{M}\), we define constructive \(H_c\) and a three-term discrete load ledger whose terms play the same *roles* as the master-equation load slots under the locked high-flux reading.”

---

## 10. Phased plan + success criteria

### Phase 0 — this note (**done**)

- Ontology, operational \(H_c\), three-term discrete \(L\), decay export story, non-claims, micro-example, open questions.

### Phase 1 — pure accounting on one discrete model (**done — AND-gate**)

**Implemented:** [`simulations/classical/m11_and_gate_ledger.py`](../simulations/classical/m11_and_gate_ledger.py)

| Criterion | Result |
|-----------|--------|
| S1 ontology | Fair bits + AND evaluation; comments match this note |
| S2 \(H_c=H(Y)\) | \(H(Y)=h_2(1/4)\approx 0.811278\) exact |
| S3 three load terms | \(L_E=1\), \(L_S=H(X\mid Y)\approx 1.188722\), \(L_B=\langle\) soft decay\(\rangle=0.5\) |
| S4 locked reading | high export ⇒ high \(L_S\) (asserted) |
| S5 chain rule | \(H(X)=H(Y)+H(X\mid Y)\) error \(<10^{-12}\) |
| S6 non-claims | printed in CLI / module docstring |
| S7 scope | under `simulations/classical/` only |

**Still available later:** richer game strategies (true M12); continuum contact (Phase 3).

### Phase 2 — multi-step / lambda / shoe (**done — classical ledgers**)

**Implemented under** [`simulations/classical/`](../simulations/classical/):

| Artifact | What |
|----------|------|
| [`m11_multistep_boolean_ledger.py`](../simulations/classical/m11_multistep_boolean_ledger.py) | id → AND → OR composition; high vs lower export; \(k_{\mathrm{eff}}\) diagnostic (\(\alpha'=0.1\)) |
| [`m11_tiny_lambda_ledger.py`](../simulations/classical/m11_tiny_lambda_ledger.py) | Fixed SKI ensemble; normal-order redex steps; \(L_E=\) mean redexes; \(L_S=\|\Delta H_c\|\) |
| [`m11_minimal_shoe_ledger.py`](../simulations/classical/m11_minimal_shoe_ledger.py) | Fixed-sequence 6R+6B residual multiset; predictive \(H_c\); \(L_B=H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)\) |

| Criterion | Result |
|-----------|--------|
| Multi-row Boolean ledger | AND export \(\approx 1.189\) > OR-step export; locked \(L_S\) ordering asserted |
| Load clock | \(k_{\mathrm{eff}}=\sum 1/(1+\alpha' L^{\mathrm{disc}})\) printed as **diagnostic only** |
| Tiny lambda | Exact \(H_c\) over finite term-shape classes; no continuum constants |
| Minimal shoe | Exact combinatorial \(H_c\); fixed seed; honesty: not EV / not dual residual |
| Non-claims | module docstrings + classical README |

**Not done in Phase 2 (deferred):** basic vs Hi-Lo strategy comparison; multi-deck shoe engine; continuum \(G\).  
Still **no** GfE metric, no ACD-EW scorecard churn for its own sake.

### Phase 3 — only later continuum contact

- Dictionary essay: which discrete limits could *motivate* continuum slots (feeds M10 / M5, not replaces them).  
- Still refuse \(L\equiv G\) and Einstein-from-IDEM.

### Success criteria for **next** implementation session (Phase 1)

| # | Criterion | Pass bar |
|---|-----------|----------|
| S1 | Declared microstate + channel step + output \(Y\) written in code comments matching this note | Unambiguous |
| S2 | \(H_c\) computed as **output** Shannon (exact preferred) | Matches foundations; AND-gate \(H(Y)\approx 0.811\) if that model chosen |
| S3 | All three \(L_E,L_S,L_B\) proxies logged with formulas from §5.1 | No continuum \(G,\epsilon_0\) |
| S4 | Locked reading respected in a unit check: high export / fast \(\| \Delta H_c \|\) ⇒ high \(L_S\), not low | Documented assert or printed case |
| S5 | Decay/export ledger: \(H(X)=H(Y)+H(X\mid Y)\) (or sequential chain rule) checked numerically | Relative error ~0 on finite model |
| S6 | README/docstring lists non-claims §9 | No gravity recovery language |
| S7 | No edits required to dual toy science; optional new path under `computational-models/` or `simulations/classical/` only if implementing | Scope control |

**Failure modes to avoid:** redefining \(H_c\) as AST size; setting \(L \propto\) remaining term size only; wiring continuum Newton calibration; claiming dual-toy 6/6 as M11 success.

---

## 11. Open questions

1. **Single-shot vs multi-step \(L_S\):** Is \(H(X\mid Y)\) an allowed single-evaluation proxy for entropy-production load, or must \(L_S\) always be a finite difference of the *same* output observable across steps?  
2. **Soft vs hard decay:** Prefer \(\{0,1\}\) recoverability or soft \(d_i = 1-1/|\mathrm{preimage}(y)|\)? Soft may track \(H(X\mid Y=y)\) better.  
3. **Is metadata in the channel?** Does emitting IDEM \(\mathrm{info}_f\) change \(H_c\) to \(H(Y,\mathrm{info})\), or is info observer-side instrumentation only?  
4. **Which complexity for \(L_E\)?** Redex count, AST size, wall-ops, or Kolmogorov-style proxies — which is stable across lambda vs games?  
5. **Product systems:** How to tensor two regions’ ledgers toward a future “local \(\rho\)” story without fake spacetime?  
6. **Load clock in discrete time:** Is \(\alpha'\) purely conventional until continuum matching, and should Phase 2 even introduce it?  
7. **Relation to M12:** Should true game log-loss be a *scoring rule* generalization of \(H_c\), or a separate \(H_c^{\mathrm{score}}\)?  
8. **Relation to M10:** When (if ever) should discrete \(H_c\) be compared to dual-toy residual \(H_c\) under a shared abstract “channel interface” without merging objects?  
9. **\(d_f\) estimation:** Bayesian I/O identification (existing \(d_f\) notes) vs static — which is default for \(L_B\)?  
10. **Nondeterministic reduction / mixed strategies:** How to define output measure when \(\Phi\) itself is random?

---

## 12. Links

| Resource | Role |
|----------|------|
| [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) | Canonical \(H_c\) / \(S_c\); AND-gate global conservation |
| [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) | Canonical \(L\), \(d\tau\), \(\Phi_g\) |
| [../THEORY.md](../THEORY.md) §3.1–3.2 | Correspondence tables this note refines |
| [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2.1, §4, §7.1.B | Locked \(L\) reading; M11 recommendation; non-claims |
| [../GLOSSARY.md](../GLOSSARY.md) | IDEM, decay, \(H_c\), \(L\) |
| [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) | M11 board status |
| [PACK_INDEX.md](PACK_INDEX.md) | Synthesis pack map |
| [m7-symbol-map.md](m7-symbol-map.md) | Continuum type-safety precedent (\(L\neq G\)) |
| [../simulations/bridging/DESIGN_blackjack_belief_dual.md](../simulations/bridging/DESIGN_blackjack_belief_dual.md) | Game *belief field* dual honesty (≠ true game \(H_c\)) |
| Root IDEM drafts (`Draft Report on IDEM…`, `Defining d_f…`, `Modeling Computational Entropy…`) | Historical IDEM metadata definitions |
| `research/games/black-jack/` | Classical strategy entropy / cost notes (M12 adjacent) |
| `computational-models/` | Intended home for classical microstructure code |

---

## 13. One-screen summary

```text
M11 DESIGN + Phase 1–2 (2026-07-15) — discrete bookkeeping only; no continuum claim

STATE:  lambda term / IDEM (y,d,d_f) / game belief  — NOT dual-toy spacetime φ
STEP:   reduce | evaluate f | observe+update strategy
H_c:    Shannon of declared OUTPUT only (foundations)
L:      L_E ~ active work (redex/AST/ops/stake)
        L_S ~ |ΔH_c| or decay-flip rate   (HIGH when flux high)
        L_B ~ d_f / residual distinguishability budget
READ:   high flux / open results / scrambling ⇒ HIGH L
        not “identity stockpile remaining”
DECAY:  d_i flips = export / irreversible overwrite (structural)
PHASE1: AND-gate ledger (H_c≈0.811, export≈1.189, L_disc≈2.689)
PHASE2: multi-step Boolean + SKI ensemble + minimal R/B shoe
NEXT:   M12 true game strategies; Phase 3 continuum contact (deferred)
NEVER:  L≡G, Einstein from IDEM, dual toy = gravity
```

---

*Update OPEN_MATH / PACK_INDEX / PROGRESS when M11 continuum contact begins (still deferred) or M12 deepens the shoe/game channel.*
