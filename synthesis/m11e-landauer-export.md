# M11e — Landauer / Thermodynamic Contact for Export and \(L_S\)

**M-id:** M11e  
**Status:** **Theory note + constructive finite ledger** — thermodynamic *contact* only  
**Date:** 2026-07-15  
**Depends on:** [m11-idem-to-load.md](m11-idem-to-load.md) §6 · [m11c-continuum-motivation.md](m11c-continuum-motivation.md) · [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) · [CLAIM_GATE.md](CLAIM_GATE.md)  
**Evidence:** [`simulations/classical/m11_landauer_and_ledger.py`](../simulations/classical/m11_landauer_and_ledger.py) · Phase 1 AND-gate ledger  
**Feeds:** paper Stage-1 export / Landauer sentence; honesty for \(L_S\) as flux object  

**Stance:** Preliminary research. Prefer under-claiming. This note relates discrete **export** \(H(X\mid Y)\) to the **standard Landauer lower bound** on average heat of erasure. It does **not** derive gravity, Newton \(G\), \(\hbar\), holography, or continuum \(L\).

Every map is labeled **semantic / structural / constructive**. Landauer itself is treated as an **external theorem** (information thermodynamics); the finite AND model is **constructive**.

---

## 1. Problem

M11 bookkeeping ([m11](m11-idem-to-load.md) §6) tracks:

1. System output entropy \(H_c = H(Y)\) (Tag **E** / classical map output).  
2. **Export** \(H_{\mathrm{export}} = H(X\mid Y)\) so the chain rule \(H(X)=H(Y)+H(X\mid Y)\) holds on finite deterministic maps.  
3. Single-shot \(L_S^{\mathrm{disc}} := H(X\mid Y)\) as **export flux** (locked high-flux reading).

Foundations already say the “missing” entropy of irreversible AND is transferred, not destroyed.  
**Question (this note):** In what precise sense does that export contact **thermodynamics**, and which M11 object does Landauer bound?

**Answer (modest):** On a standard bit-erasure / irreversible-map model, the average number of **erased bits** is \(H(X\mid Y)\) (for deterministic \(f\) under input measure \(p_X\)). Landauer’s principle then gives

\[
\boxed{
Q \;\ge\; k_B T \ln 2 \cdot H(X\mid Y)
}
\qquad\text{(Shannon in bits)},
\]

so in units of \(k_B T\ln 2\), the lower bound **equals** the export ledger quantity that M11 already uses as \(L_S^{\mathrm{disc}}\).

**Out of scope:** continuum \(L(\rho,g)\), black-hole temperature, Hawking-as-Landauer as a *theorem*, fitting \(k_B T\) to gravity scales.

---

## 2. Finite irreversible model (AND)

### 2.1 Setup (constructive)

| Object | Definition |
|--------|------------|
| Input | \(X=(X_1,X_2)\) i.i.d. fair bits; \(H(X)=2\) bits |
| Map | \(Y = f(X) = X_1 \land X_2\) (deterministic) |
| Declared system output | \(Y\) only (observer of the gate result) |
| \(H_c^{\mathrm{disc}}\) | \(H(Y)=h_2(1/4)\approx 0.811278\) bits |
| Export / preimage entropy | \(H(X\mid Y)\approx 1.188722\) bits |

**Chain rule (constructive identity):**

\[
H(X) = H(Y) + H(X\mid Y).
\]

For fair-bit AND: \(2 = H(Y) + H(X\mid Y)\). Numerically verified to machine precision in the sibling ledger.

### 2.2 Bit-erasure / reset-after-AND model

We fix an explicit **physical protocol** so “erased bits” is not ambiguous.

**Protocol R (reset after AND):**

1. Registers hold joint input \(X\) (2 classical bits of storage).  
2. Compute \(Y=f(X)\) into a result register (may share hardware).  
3. **Keep** only \(Y\) as the public system output.  
4. **Reset / thermalize** the input (and any work tape not counted in \(Y\)) to a fixed standard state, **conditional on** \(Y\) only — i.e. discard all residual distinguishability of preimages of \(Y\).

What is erased is not “2 bits every time,” but the **conditional** uncertainty of \(X\) given \(Y\):

\[
n_{\mathrm{erased}} \;:=\; H(X\mid Y)
\qquad\text{(average, in bits)}.
\]

**Branch-wise view (same object):**

| \(Y\) | \(P(Y)\) | Preimage size | \(H(X\mid Y=y)\) |
|-------|----------|---------------|------------------|
| \(1\) | \(1/4\) | \(1\) \(\{(1,1)\}\) | \(0\) |
| \(0\) | \(3/4\) | \(3\) | \(\log_2 3 \approx 1.584963\) |

\[
H(X\mid Y)
=
\tfrac{3}{4}\log_2 3 + \tfrac{1}{4}\cdot 0
\approx 1.188722\ \mathrm{bits}.
\]

**Rigor:** definition of \(n_{\mathrm{erased}}\) on this finite model is **constructive** (Shannon calculus). Identifying the protocol with a laboratory heat bath is **semantic** application of Landauer (next section).

### 2.3 Alternative: pure irreversible map (same export)

If the channel is the stochastic map that *emits only* \(Y=f(X)\) and never stores \(X\), the information missing from \(Y\) relative to \(X\) is still \(H(X\mid Y)\) for deterministic \(f\). Protocol R makes the thermodynamic reading explicit (reset of a physical register); the **information object** is the same.

---

## 3. Landauer statement (external theorem)

**Landauer’s principle (standard form used here):**  
In a system in contact with a heat bath at temperature \(T\), **logically irreversible** erasure of information that reduces the Shannon entropy of a classical register by \(\Delta H\) bits requires average heat dissipation to the bath of at least

\[
Q \;\ge\; k_B T \ln 2 \cdot \Delta H
\qquad (\Delta H\text{ in bits}).
\]

Equivalently, if entropy is measured in nats, \(Q\ge k_B T\cdot \Delta H_{\mathrm{nats}}\).

**Status in this program:**

| Piece | Level |
|-------|--------|
| Finite-model \(H(X)\), \(H(Y)\), \(H(X\mid Y)\) | **Constructive** |
| Identification \(\Delta H = H(X\mid Y)\) for Protocol R | **Structural** (standard info-thermodynamics for deterministic \(f\)) |
| Inequality \(Q\ge k_B T\ln 2\cdot H(X\mid Y)\) | **External theorem** (Landauer / Bennett lineage) — **not** re-proved here |
| \(k_B T\ln 2\) conversion factor | **Standard conversion only** — **not** fitted to Newton \(G\), \(\hbar\), or continuum \(L\) |

**Units convention (locked for ledgers):**  
Report the Landauer lower bound in units of \(k_B T\ln 2\):

\[
\frac{Q_{\min}}{k_B T\ln 2}
=
H(X\mid Y)
\quad\text{(bits of erasure cost)}.
\]

So numerically, **bound \(=\) export** on the fair-bit AND model. No free parameters.

---

## 4. \(L_S\) is the information object Landauer bounds

From [m11](m11-idem-to-load.md) Phase 1 / §5–§6:

| M11 symbol | Fair-bit AND value | Role |
|------------|--------------------|------|
| \(H_c = H(Y)\) | \(\approx 0.811278\) | Output Shannon (Tag E) |
| Export \(H(X\mid Y)\) | \(\approx 1.188722\) | Preimage / environment ledger |
| \(L_S^{\mathrm{disc}}\) | \(:= H(X\mid Y)\) (single-shot) | Export-flux slot |

**Contact statement (allowed form):**

> *On Protocol R for a finite deterministic map, the average Landauer erasure cost (in units of \(k_B T\ln 2\)) equals the export \(H(X\mid Y)\). M11’s single-shot \(L_S^{\mathrm{disc}}\) is defined as that same information object — therefore \(L_S^{\mathrm{disc}}\) is the quantity that standard Landauer bounds from below as heat \(Q\ge (k_B T\ln 2)\,L_S^{\mathrm{disc}}\).*

**What this is not:**

- Not a claim that continuum \(\gamma|dS_c/d\tau|\) **equals** Landauer heat density.  
- Not a derivation of the master-equation coefficient \(\gamma\).  
- Not a claim that \(L^{\mathrm{disc}}\) is thermodynamic free energy.

**Type / tag hygiene ([CLAIM_GATE](CLAIM_GATE.md)):**

- Entropy object: Tag **E** (\(H_c^{\mathrm{disc}}=H(Y)\)); export is conditional Shannon \(H(X\mid Y)\), not \(S_c\), not toy residual.  
- \(L_S^{\mathrm{disc}}\) remains a **dimensionless** bookkeeping scalar (bits of flux); Landauer multiplies by \(k_B T\ln 2\) only when converting to heat.  
- Still \(L\neq G\); still \(L^{\mathrm{disc}}\neq L(\rho,g)\).

### 4.1 Locked reading reaffirmed

Output \(H_c\) **drops** (\(\approx 2\to 0.811\)) while export / Landauer cost is **large** (\(\approx 1.189\)). Demand tracks **irreversible overwrite cost**, not residual output entropy — same locked high-flux reading as M11 / M11c.

---

## 5. Optional reversible dilation (garbage accounting)

**Protocol V (reversible embedding):**  
Extend the map to an invertible (or injective) dilation on a larger register, e.g.

\[
R:\ (X_1,X_2,0)\;\mapsto\; (Y,\, G),\qquad
Y=X_1\land X_2,\quad G=\text{garbage bits enough to recover }X.
\]

Concrete choice used in the ledger: store \(Y\) and full input copy as garbage \(G=X\) (wasteful but exact), or a minimal garbage that separates preimages. Then:

| Quantity | Irreversible (Protocol R) | Reversible dilation (keep garbage) |
|----------|---------------------------|-------------------------------------|
| Public \(H(Y)\) | \(\approx 0.811\) | same if only \(Y\) is “result” |
| Joint \(H(Y,G)\) | n/a (input discarded) | \(= H(X) = 2\) if \(R\) is bijective on support |
| Erasure cost now | \(H(X\mid Y)\) | **0** until garbage is erased |
| If later erase \(G\) | — | cost \(\ge H(G\mid Y)=H(X\mid Y)\) |

**Lesson (Bennett-style, structural):** logical irreversibility can be deferred into **garbage**. The **export** does not vanish; it is parked in \(G\). Landauer cost appears when garbage is reset. In irreversible Protocol R, export is paid immediately; in Protocol V, \(L_S\)-like flux is postponed until garbage erasure — still the **same** \(H(X\mid Y)\) object.

**Rigor:** reversible accounting on the finite alphabet is **constructive**; equivalence of total eventual heat to irreversible cost is **standard structural** (Bennett), not a new theorem of this repo.

---

## 6. Numeric fair-bit AND (ledger summary)

From [`m11_landauer_and_ledger.py`](../simulations/classical/m11_landauer_and_ledger.py):

| Quantity | Value (bits / bit-units) |
|----------|---------------------------|
| \(H(X)\) | \(2\) |
| \(H(Y)=H_c\) | \(h_2(1/4)\approx 0.811278\) |
| Export \(H(X\mid Y)\) | \(\approx 1.188722\) |
| Landauer \(Q_{\min}/(k_B T\ln 2)\) | \(= H(X\mid Y)\approx 1.188722\) |
| \(L_S^{\mathrm{disc}}\) | \(=\) export (by definition) |
| Chain-rule residual | \(<10^{-12}\) |
| Reversible: \(H(Y,G)-H(Y)\) (garbage entropy) | \(= H(X\mid Y)\) when \(G\) completes \(X\) |

**Main inequality (paper-ready):**

\[
Q \;\ge\; k_B T \ln 2 \cdot H(X\mid Y)
\quad\text{with}\quad
H(X\mid Y)=L_S^{\mathrm{disc}}\ \text{(single-shot AND protocol)}.
\]

---

## 7. Rigor board

| Claim | Level | Status |
|-------|-------|--------|
| \(H(X)=H(Y)+H(X\mid Y)\) on fair-bit AND | **Constructive** | Ledger assert |
| \(n_{\mathrm{erased}}:=H(X\mid Y)\) for Protocol R | **Constructive definition** | This note |
| \(Q\ge k_B T\ln 2\cdot n_{\mathrm{erased}}\) | **External theorem** (Landauer) | Cited, not re-proved |
| \(L_S^{\mathrm{disc}}=H(X\mid Y)\) is the Landauer bit-count | **Structural contact** | Same object, two names |
| Continuum \(L_S\) density = local heat flux | **Not claimed** | — |
| \(k_B T\ln 2\) fixed by gravity / \(\hbar\) | **Not claimed** | Conversion only |
| Garbage dilation preserves export until erase | **Constructive** (finite) + **structural** (Bennett) | Ledger optional rows |

---

## 8. Explicit non-claims

Do **not** assert from this note or its ledger:

1. **Newton \(G\)** or Path J/M calibration from Landauer or AND export.  
2. **\(\hbar\)**, Planck units, or Bekenstein bound from gate thermodynamics.  
3. **Holographic area** / \(S_{\mathrm{BH}}=A/(4G\hbar)\) as the AND environment.  
4. **\(L\equiv G\)** or \(L^{\mathrm{disc}}\equiv L(\rho,g)\).  
5. **Master equation \(\Leftrightarrow\) continuum GfE**.  
6. Continuum identity of \(L_S\) with heat production rate in GR/GfE.  
7. Hawking radiation **proved** as Landauer cost of \(\Phi_g\) (semantic program language elsewhere remains non-theorem).  
8. Numerical fit of \(T\) or \(k_B\) to any gravity scale.  
9. Dual-toy residual \(H_c\) equals gate export or Landauer bits.

**Allowed claim form:**

> *For finite deterministic maps under Protocol R, export \(H(X\mid Y)\) is the average erased-bit count; Landauer supplies \(Q\ge k_B T\ln 2\cdot H(X\mid Y)\). M11 single-shot \(L_S\) is that export object. Contact is thermodynamic bookkeeping only.*

---

## 9. Conclusion (one paragraph for paper)

Irreversible classical maps such as fair-bit AND reduce local output entropy \(H_c=H(Y)\) while conserving total information via the chain rule \(H(X)=H(Y)+H(X\mid Y)\). Interpreting the residual \(H(X\mid Y)\) as the average number of bits erased when the input register is reset after the result is stored, standard Landauer thermodynamics bounds the average heat by \(Q\ge k_B T\ln 2\cdot H(X\mid Y)\). In units of \(k_B T\ln 2\), that lower bound equals the M11 export ledger entry already used as the single-shot load slot \(L_S^{\mathrm{disc}}\). Thus \(L_S\) is the information-theoretic object that Landauer converts into a minimal heat cost; the conversion factor is the usual \(k_B T\ln 2\), not a gravity-fitted constant. This is constructive on finite models and external-theorem contact only: it does not identify discrete load with continuum \(L\), metric \(G\), or Einstein dynamics.

---

## 10. Links

| Resource | Role |
|----------|------|
| [m11-idem-to-load.md](m11-idem-to-load.md) §6–§7.A | Export ledger; AND micro-example; \(L_S\) definition |
| [m11c-continuum-motivation.md](m11c-continuum-motivation.md) | Why export is a load *role* |
| [../foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) | Global conservation + AND intuition |
| [CLAIM_GATE.md](CLAIM_GATE.md) | Entropy tags; \(L\neq G\); M11 accounting only |
| [../simulations/classical/m11_landauer_and_ledger.py](../simulations/classical/m11_landauer_and_ledger.py) | Numeric asserts |
| [../simulations/classical/m11_and_gate_ledger.py](../simulations/classical/m11_and_gate_ledger.py) | Phase 1 three-slot ledger |
| [../simulations/classical/README.md](../simulations/classical/README.md) | Classical commands |

---

## 11. One-screen summary

```text
M11e — Landauer contact for export / L_S (2026-07-15)
        thermodynamic contact only; no gravity fit

MODEL:   fair bits X; Y = X1 ∧ X2; Protocol R: keep Y, reset input
EXPORT:  H(X|Y) ≈ 1.188722 bits  (= preimage entropy)
CHAIN:   H(X) = H(Y) + H(X|Y)     constructive

LANDAUER (external):  Q ≥ kT ln 2 · H(X|Y)
UNITS:   Q_min / (kT ln 2) = H(X|Y) = L_S  (single-shot)

DILATION: reversible R parks export in garbage G;
          erase G later → same H(X|Y) cost

NEVER:   Newton G, ħ, area law, L≡G, ME⇔GfE, continuum L identity
PAPER:   L_S is the bit-count Landauer multiplies by kT ln 2
```

---

*Do not promote this note to continuum thermodynamics or Hawking theorem. Update classical README / PACK_INDEX when the ledger lands.*
