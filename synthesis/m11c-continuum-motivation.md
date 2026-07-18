# M11c — Continuum *Motivation* of Load Slots from Discrete Microstructure

**M-id:** M11c (Phase-3 dictionary essay; not continuum derivation)  
**Status:** **Design / theory note** — structural motivation of three continuum load *roles* from discrete Phase 1–2 evidence  
**Date:** 2026-07-15  
**Depends on:** [m11-idem-to-load.md](m11-idem-to-load.md) · [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) · [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) · [../THEORY.md](../THEORY.md) §3 · [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2.1 · [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md)  
**Evidence:** [`simulations/classical/`](../simulations/classical/) (Phase 1 AND-gate; Phase 2 multi-step Boolean, tiny SKI, minimal shoe)  
**Feeds:** optional `m11_coupled_regions_ledger.py` · paper Stage-1 microstructure prose · later true continuum contact (still deferred)  
**Related:** [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) · [m7-symbol-map.md](m7-symbol-map.md) (\(L\neq G\)) · [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md)

**Stance:** Preliminary research. Prefer under-claiming. This note motivates **why continuum \(L\) has three *roles*** from discrete bookkeeping that *works* — **not** a continuum limit theorem, **not** a fit of Newton constants, **not** Einstein-from-IDEM.

Every mapping is labeled **semantic / structural / constructive**. Prefer structural motivation over fake continuum limits.

---

## 1. Problem

Discrete load accounting is now **constructive** on small classical models ([m11](m11-idem-to-load.md) Phase 1–2):

\[
L^{\mathrm{disc}} = \beta' L_E^{\mathrm{disc}} + \gamma' L_S^{\mathrm{disc}} + \delta' L_B^{\mathrm{disc}},
\]

with \(\beta',\gamma',\delta'\) bookkeeping weights (default \(1\)), **not** continuum calibrations.

Continuum load in the master equation ([master-equation](../emergent-gravity/master-equation.md)) has the same *three-slot form*:

\[
L(\rho,g)
=
\beta \frac{E[\rho]}{V\epsilon_0}
+
\gamma \left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}}
+
\delta \frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)}.
\]

**Question this note answers (modestly):**  
Why *those* three roles — energy-like work, entropy-rate / export flux, boundary / capacity — as a **motivation** of the continuum template, given discrete microstructure, **without** claiming:

- numerical equality \(L^{\mathrm{disc}} = L(\rho,g)\),
- fitting \(\beta,\gamma,\delta,\alpha,\epsilon_0\) from gates or shoes,
- a proved hydrodynamic limit of IDEM → continuum fields.

**Out of scope:** Lorentzian GfE, Path J/M re-derivation, residual dual toys, continuum \(G\).

---

## 2. Locked \(L\) reading (reaffirmed)

From [PROGRESS_REPORT](../PROGRESS_REPORT.md) §2.1 / §4 and [CURRENT_CLAIMS](CURRENT_CLAIMS.md) C14:

| Prefer | Reject as primary story |
|--------|-------------------------|
| Demand from **scale/rate of possible channel outcomes** | “How much unreduced identity stockpile remains” |
| High **flux**, many **open results**, active **scrambling** ⇒ **high** \(L\) | Idle complexity as high load |
| Energy-like work + entropy production/export + boundary/distinguishability budget | Single monist “size of term” scalar |

**Polarity checklist (locked):**

| Situation | Expected load |
|-----------|----------------|
| High entropy flux / fast \(\lvert\Delta H_c\rvert\) | \(L_S\) **high** during the drop |
| Irreversible overwrite / decay flips \(d_i:0\to 1\) | \(L_S^{\mathrm{decay}}\) **high** (loss is work) |
| Many open residual world-lines / high \(d_f\) | \(L_B\) **high** |
| Active redexes / ops / strategy evaluation | \(L_E\) **high** |
| Idle identity, fully reduced, no observation | \(L\) **low** |

This reading is **semantic / program convention** until continuum matching exists. Discrete ledgers **respect** it by construction ([m11](m11-idem-to-load.md) §5.2; classical README locked-reading asserts).

---

## 3. Three-slot motivation table

Canonical continuum terms from [master-equation](../emergent-gravity/master-equation.md). Discrete proxies and Phase evidence from [m11](m11-idem-to-load.md) §5 and `simulations/classical/`.

| Continuum slot | Role (motivation) | Discrete evidence (Phase 1–2) | Continuum role (master eq) | Rigor | What would make it **constructive** later |
|----------------|-------------------|------------------------------|----------------------------|-------|---------------------------------------------|
| **Energy-like** \(\beta E[\rho]/(V\epsilon_0)\) | Density of **active work** — ops / redexes / evaluations per volume·time, not idle stockpile | **AND:** \(L_E=1\) one gate op (`m11_and_gate_ledger.py`). **Multi-step Boolean:** \(L_E=\) active gate ops per step. **SKI:** \(L_E=\) mean redex count pre-step (`m11_tiny_lambda_ledger.py`). **Shoe:** \(L_E=1\) count-bucket update per draw. Idle id step: \(L_E=0\). | Local energy density scales information-processing *capacity demand* (Margolus–Levitin-facing) | **Structural** (complexity ↔ energy density analogy). **Not** constructive continuum match. | Specify a discrete complexity measure that converges (in a named topology) to continuum energy density of a field theory for \(\rho\); fix \(V,\epsilon_0\) by independent physics, not gate fit |
| **Entropy-rate** \(\gamma\lvert dS_c/d\tau\rvert_{\mathrm{reg}}\) | Local **export current** / \(\lvert dH_c/d\tau\rvert\) / decay-flip rate — flux of irreversibility | **AND:** \(L_S=H(X\mid Y)\approx 1.188722\) (export); \(H_c=H(Y)\approx 0.811278\); chain rule exact (`m11_and_gate_ledger.py`). **Boolean:** AND export \(\approx 1.189\) **>** OR-step export; locked assert larger export ⇒ larger \(L_S\). **SKI:** \(L_S=\lvert\Delta H_c\rvert\) under redex steps. **Shoe:** \(L_S=\lvert\Delta H_c\rvert\) spikes when predictive entropy jumps. | Regularized rate of computational-entropy production (clocked by \(\tau\)) | **Structural (strong candidate)** — best role match ([THEORY](../THEORY.md) §3.2). Export accounting **constructive** classically. Continuum rate **not** claimed equal. | Hydrodynamic / large-system limit of \(\lvert\Delta H_c/\Delta k\rvert\) → \(\lvert dS_c/d\tau\rvert_{\mathrm{reg}}\) for a declared family of channels; prove regularization window coincides with Margolus–Levitin window only if needed for gravity contact |
| **Boundary / capacity** \(\delta S_{\mathrm{boundary}}/S_{\mathrm{BH}}(A)\) | **Distinguishability budget** vs capacity — residual ensemble entropy, \(d_f\), open world-lines vs max register | **AND:** \(L_B=\) mean soft lost-recoverability mass \(=0.5\). **SKI:** \(L_B=\) fraction still open (has redex). **Shoe:** \(L_B=H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)\) residual order-entropy ratio — capacity-like pressure from remaining multiset possibilities. | Holographic / Bekenstein saturation pressure on screen area \(A\) | **Structural soft / analogical** — softest of the three. \(S_{\mathrm{BH}}\) language remains **semantic**. | Relate residual ensemble entropy ratio to a true area-law / screen entropy in a discrete geometry model; still refuse \(S_{\mathrm{BH}}=A/4G\hbar\) on a game table |

### 3.1 Role alignment (one screen)

```text
ACTIVE WORK     ──role──►  energy-like density in L
EXPORT / FLUX   ──role──►  |dS_c/dτ|_reg term in L
OPEN BUDGET     ──role──►  boundary / capacity ratio in L

Same three *axes of demand*; different mathematical objects.
Coefficients β,γ,δ vs β',γ',δ' are NOT identified.
```

**Rigor of the table as a whole:** **semantic design + structural role alignment** grounded in **constructive discrete ledgers**. Continuum formula identity: **not claimed**.

---

## 4. Why not one term?

A monist load (e.g. “\(L \propto\) remaining AST size” or “\(L \propto H_c\) alone”) fails the locked reading and the Phase evidence simultaneously.

### 4.1 Irreversible AND: three axes at once

From foundations ([definition](../foundations/computational-entropy/definition.md)) and Phase 1:

| Quantity | Value (fair bits) | Axis |
|----------|-------------------|------|
| \(H(X_1,X_2)\) | \(2\) bits | input possibility mass |
| \(H_c = H(Y)\) | \(\approx 0.811\) bits | **output** entropy (falls) |
| Export \(H(X\mid Y)\) | \(\approx 1.189\) bits | **flux / overwrite** (feeds \(L_S\)) |
| \(L_E\) | \(1\) (one op) | **work** (non-zero) |
| \(L_B\) | \(0.5\) soft recoverability mass | **open distinguishability** after map |
| \(L^{\mathrm{disc}}\) | \(\approx 2.689\) | sum of independent roles |

**Observation:** output \(H_c\) **drops** while demand **rises**. Any load \(\propto H_c\) alone would report *low* demand precisely when irreversible overwrite is *expensive* — opposite of the locked reading. Any load \(\propto\) “input size remaining” would miss that the expensive part is **export rate**, not idle joint support.

**Axes independence (this example):**

- \(L_E\): nonzero even if one rewrote \(L_S\) differently (still one gate evaluation).  
- \(L_S\): large export independent of counting “one op.”  
- \(L_B\): recoverability mass can stay positive after certainty of *which \(Y\)* while \(L_S\) for a *static* completed map would go to zero on subsequent idle steps.

### 4.2 Idle identity: low \(L\) without collapsing slots

Phase 2 multi-step Boolean begins with an **id** baseline on \((X_1,X_2,X_3)\): no gate work, no export, no recoverability loss → \(L_E=L_S=L_B=0\) (or zero-activity row). Later AND step spikes \(L_S\) and \(L_E\); OR step has **lower** export than AND (asserted ordering).

A single term cannot mark “idle” vs “scrambling evaluation” while also ranking AND > OR export and tracking residual capacity in other models.

### 4.3 Shoe: flux spikes vs capacity baseline

Minimal shoe (`m11_minimal_shoe_ledger.py`):

- \(L_E\) nearly constant (count update cost \(=1\)).  
- \(L_S = \lvert\Delta H_c\rvert\) **spikes** when predictive entropy jumps between draws.  
- \(L_B = H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)\) tracks residual multiset order-entropy ratio (capacity pressure), **smoothly** shrinking as the shoe depletes.

If only \(L_E\): misses information-arrival dynamics.  
If only \(L_S\): misses that near-certainty late shoe still has a different residual budget shape.  
If only \(L_B\): misses instantaneous flux of observation updates.

### 4.4 Conclusion (motivation, not theorem)

Three independent **axes of demand** appear in classical microstructure:

1. **How hard is the machine working?** (\(L_E\))  
2. **How fast is possibility being realized / exported?** (\(L_S\))  
3. **How much distinguishability budget remains open vs capacity?** (\(L_B\))

The continuum three-term \(L\) is the **same role split** at continuum language level ([THEORY](../THEORY.md) §3.2). That is **structural motivation**, not a uniqueness proof that no other split exists.

---

## 5. Local current picture (structural, non-constructive continuum)

### 5.1 Discrete lattice of maps (aspirational ontology)

Imagine a **graph / lattice of local maps** \(\{f_i\}\) (or local channels \(\Phi_i\)), each with its own ledger:

| Local field (discrete) | Meaning | Continuum aspiration (named, **not proved**) |
|------------------------|---------|-----------------------------------------------|
| Work density \(w_i\) | ops / redexes at site \(i\) per step | \(\mapsto\) energy-like density \(\sim E[\rho]/V\) |
| Export current \(j_i^{\mathrm{exp}}\) | \(H(X_i\mid Y_i)\) or \(\lvert\Delta H_c\rvert\) or \(\lVert\Delta\mathbf{d}\rVert_1\) per step | \(\mapsto\) entropy-production rate \(\lvert dS_c/d\tau\rvert\) |
| Residual open set \(b_i\) | \(d_f\), soft recoverability, residual ensemble entropy vs max | \(\mapsto\) boundary / capacity ratio |

**Global conservation (classical, constructive when finite):**  
For each local deterministic map under suitable input measure, chain rule

\[
H(X_i) = H(Y_i) + H(X_i\mid Y_i)
\]

holds ([definition](../foundations/computational-entropy/definition.md); Phase 1 assert error \(<10^{-12}\)). Exported mass lives in an environment / preimage register, not in \(H(Y_i)\).

**Local load (structural):**

\[
L_i^{\mathrm{disc}} \sim \beta' w_i + \gamma' j_i^{\mathrm{exp}} + \delta' b_i.
\]

### 5.2 Continuum density fields — labeled **aspirational / non-constructive**

| Step | Status |
|------|--------|
| Discrete multi-site ledger with per-site \(w,j,b\) | **Structural design**; optional next implementation (coupled regions) |
| Continuum fields \(w(x), j^{\mathrm{exp}}(x), b(x)\) | **Semantic / structural aspiration** |
| Identification with \(E[\rho](x)\), \(\lvert dS_c/d\tau\rvert(x)\), \(S_{\mathrm{boundary}}/S_{\mathrm{BH}}\) | **Not claimed** |
| Hydrodynamic limit of IDEM lattice → master-equation continuum | **Open / deferred** (PROGRESS non-claim §2.3.9) |

**Honesty sentence (paste-ready):**

> *Discrete three-slot ledgers motivate continuum load as three density-like demand axes (work, export current, open capacity). We do not claim a continuum limit of IDEM maps to \(L(\rho,g)\) or to Einstein dynamics.*

Type safety remains: even after a continuum limit of **load densities**, the result is still a **scalar field** (or integrated scalar), **not** the structure-induced metric \(G\) ([CURRENT_CLAIMS](CURRENT_CLAIMS.md); [m7](m7-symbol-map.md)).

---

## 6. Coupled regions (preview) — success criteria for a sibling ledger

**Intent:** Make local vs global accounting **constructive** on a two-region classical product, without spacetime geometry.

**Proposed artifact (sibling may implement):**  
`simulations/classical/m11_coupled_regions_ledger.py`

### 6.1 Minimal design sketch

| Element | Spec |
|---------|------|
| Regions | \(A\), \(B\) with local inputs \(X_A, X_B\) (finite alphabets) |
| Local maps | \(Y_A = f_A(X_A)\) and/or \(Y_B = f_B(X_B)\); optional **coupled** map \(Y_{AB}=f_{AB}(X_A,X_B)\) on one step |
| Environment | Explicit export registers \(E_A, E_B\) holding preimage / discarded path info |
| Local \(H_c\) | \(H(Y_A)\), \(H(Y_B)\) (or joint \(H(Y_A,Y_B)\) if declared joint output) |
| Local load | \(L_A^{\mathrm{disc}}\), \(L_B^{\mathrm{disc}}\) each with three slots |
| Global | Joint input entropy \(H(X_A,X_B)\); joint output; total export |

### 6.2 What the ledger **should** show

1. **Global conservation (constructive):**  
   \(H(X_A,X_B) = H(Y_{\mathrm{sys}}) + H_{\mathrm{export,total}}\) (chain rule / I-diagram identity on the finite model), with relative error \(\sim 0\).

2. **Local \(H_c\) can drop while global fine-grained entropy is conserved** — foundations story made multi-site.

3. **Local \(L\) tracks local demand:**  
   - Idle region: low \(L\).  
   - Active irreversible region: high \(L_S\) (export) + nonzero \(L_E\).  
   - Region with large residual ambiguity: high \(L_B\).

4. **Coupling effect (qualitative):**  
   When \(f_{AB}\) correlates regions, local export and joint \(H_c\) differ from the product of independent maps — ledger rows should expose the difference without continuum language.

5. **Locked reading:** high local flux ⇒ high local \(L_S\), not “remaining local identity stockpile.”

### 6.3 Success criteria (pass bar)

| # | Criterion | Pass bar |
|---|-----------|----------|
| C1 | Two regions + declared outputs + export registers in code comments matching this note | Unambiguous |
| C2 | Exact (or exact-on-support) Shannon; chain-rule global conservation checked | Error \(\lesssim 10^{-12}\) on finite model |
| C3 | Per-region \(L_E,L_S,L_B\) logged; formulas from [m11](m11-idem-to-load.md) §5.1 | No continuum \(G,\epsilon_0,G_{\mathrm{Newton}}\) |
| C4 | At least one scenario: region \(A\) irreversible (AND-like), region \(B\) idle id | \(L_A \gg L_B\) with asserted ordering |
| C5 | At least one coupled vs product comparison printed | Numerical difference documented |
| C6 | Module docstring lists non-claims §7 of this note | No gravity recovery language |
| C7 | Lives under `simulations/classical/` only | Scope control |

**Failure modes:** redefining \(H_c\) as “correlation strength”; claiming two-region product **is** spacetime; wiring \(\alpha\beta=4\pi G/c^4\).

**Rigor if implemented:** **constructive** multi-site classical accounting; continuum density interpretation still **structural aspiration** (§5).

---

## 7. Explicit non-claims

Do **not** assert from this motivation note (or from Phase 1–2 + future coupled ledgers alone):

1. **Master equation \(\Leftrightarrow\) continuum GfE** (Bianconi).  
2. **\(L \equiv G\)**, \(L^{\mathrm{disc}} \equiv L(\rho,g)\), or \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\).  
3. **\(\alpha\beta = 4\pi G/c^4\)** (or any Path M calibration) **from discrete** gates, SKI, shoes, or region products — Path M remains **on-shell continuum calibration** ([CURRENT_CLAIMS](CURRENT_CLAIMS.md) C10).  
4. **Einstein / Newton recovery from IDEM** or classical ledgers (Newton remains Path J/M only).  
5. **IDEM/decay constructs continuum \(L\) or \(G\)** (PROGRESS non-claim §2.3.9 — still open/deferred).  
6. Continuum density fields of §5 are **proved** hydrodynamic limits.  
7. Uniqueness of the three-term split among all possible demand functionals.  
8. Dual-toy residual \(H_c\) (lattice \(\phi\)) equals classical gate/strategy \(H_c\).  
9. \(S_{\mathrm{BH}}=A/(4G\hbar)\) applies to a Boolean or shoe register.

**Allowed claim form:**

> *Classical three-slot load ledgers under the locked high-flux reading provide **structural motivation** for the continuum master-equation load’s three roles (work, entropy-rate, boundary/capacity). Continuum equality and gravitational recovery are not claimed.*

---

## 8. Open questions

1. **Single-shot export vs multi-step \(\Delta H_c\):** Keep both as legitimate \(L_S\) proxies under different channel definitions, or force a single convention before continuum contact?  
2. **Soft vs hard decay for \(L_B\) / \(L_S^{\mathrm{decay}}\):** Soft \(d_i=1-1/\lvert\mathrm{preimage}\rvert\) tracks \(H(X\mid Y=y)\) better — default?  
3. **Independent axes formalization:** Can one exhibit a discrete family where \((L_E,L_S,L_B)\) are linearly independent as functionals (motivates three terms more sharply than examples)?  
4. **Product systems / locality:** What is the right tensor / cut for two-region load so that \(L_{AB}\) is not double-counting export? (Coupled ledger should stress-test.)  
5. **Load clock:** Is discrete \(k_{\mathrm{eff}}=\sum 1/(1+\alpha' L^{\mathrm{disc}})\) only diagnostic forever, or can \(\alpha'\) be fixed by a *non-gravitational* capacity bound first?  
6. **When does continuum contact start?** Prefer: after multi-site conservation is constructive + paper prose uses role language only — not before fake \(\epsilon_0\).  
7. **Relation to ACD-EW split load:** Same three *roles* across threads ([m11](m11-idem-to-load.md) §5.3) — keep permanently non-identified objects, or seek an abstract “channel interface” (M10) without merging?  
8. **Boundary term hardness:** Is residual ensemble entropy ratio enough forever, or must \(L_B\) eventually touch a genuine area-law model to stay honest vs \(S_{\mathrm{BH}}\)?

---

## 9. Single recommended next math step

**Implement / specify the two-region ledger (§6) at constructive classical level** (`m11_coupled_regions_ledger.py` or equivalent design freeze), with global chain-rule conservation and local three-slot \(L\), **before** any continuum field limit language in proofs.

**Why this step (not a continuum Γ-limit, not Newton fitting):**

- Closes the largest *honest* gap between single-map Phase 1–2 and the “local \(\rho\) / local \(L\)” story the master equation assumes.  
- Stress-tests axis independence and export bookkeeping under coupling.  
- Stays inside Stage-1 computational induction — no \(L\equiv G\), no Path M abuse.  
- Feeds paper prose with multi-site microstructure without overclaiming continuum.

Optional parallel (paper only): paste role-alignment §3 into Stage-1 exposition with rigor labels.

---

## 10. Links

| Resource | Role |
|----------|------|
| [m11-idem-to-load.md](m11-idem-to-load.md) | Discrete dictionary Phase 0–2; proxies; non-claims |
| [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) | Canonical \(H_c\); AND-gate global conservation |
| [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) | Canonical three-term \(L\), \(d\tau\), \(\Phi_g\) |
| [../THEORY.md](../THEORY.md) §3.1–3.2 | Correspondence tables refined here |
| [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2.1, §4 | Locked \(L\) reading |
| [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) | C14 load reading; non-claims 1–2, 9–10 |
| [../simulations/classical/README.md](../simulations/classical/README.md) | Phase 1–2 commands + honesty |
| [m7-symbol-map.md](m7-symbol-map.md) | Type safety \(L\neq G\) |
| [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) | Entropy object hygiene (tag E = discrete M11 \(H_c\)) |

---

## 11. One-screen summary

```text
M11c — continuum MOTIVATION of load slots (2026-07-15)
        structural roles only; no continuum limit claim

PROBLEM:  discrete L^disc works; continuum L has 3 terms — why those roles?
READ:     high flux / open results / scrambling ⇒ HIGH L
          not identity stockpile

SLOTS:    L_E  work density     ← redexes/ops (SKI, gates)
          L_S  export current   ← H(X|Y), |ΔH_c|, decay flips
          L_B  capacity budget  ← soft d, residual H_seq ratio, d_f

WHY 3:    AND: H_c↓ but export↑ + work>0 + recoverability open
          idle id: L≈0; shoe: L_S spikes ≠ L_B shrink ≠ L_E flat

LOCAL:    lattice of maps → (w, j_exp, b) densities — ASPIRATIONAL
COUPLED:  next constructive step = two-region ledger + chain rule

NEVER:    L≡G; αβ=4πG/c^4 from discrete; Einstein from IDEM; ME⇔GfE
NEXT:     m11_coupled_regions_ledger.py success criteria (§6)
```

---

*Update [PACK_INDEX](PACK_INDEX.md) / OPEN_MATH / m11 parent when coupled-region ledger lands or continuum contact begins. Do not promote this note to “continuum derivation.”*
