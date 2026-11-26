# Computational Entropy: Output-Distribution Entropy and Landauer-Exact Export

> **Tier 1 paper (banner added 2026-11-26).** Paper A belongs to Tier 1, the programme's primary result: channel-level entropy ([CORE.md](https://github.com/cyotee/computational-entropy/blob/master/CORE.md)), the mathematical object proposed for a **Boltzmann–Shannon unification**. The non-classical line \(S_c\) in §1 is scaffolding from Tier 3 (conjecture). No theorem in this paper uses it. For which results here are standard and which are candidates for new, see [CORE.md §4](https://github.com/cyotee/computational-entropy/blob/master/CORE.md#4-genuinely-new-vs-standard).

**Paper A (solid core) — Draft**
**Status:** 2026-07-29 · Preliminary research · self-contained, no gravitational claims
**Scope contract:** [../DELIVERY_SCOPE.md](../DELIVERY_SCOPE.md) §1 (may assert A1–A6; must not assert gravity)
**Canonical definition:** [../../foundations/computational-entropy/definition.md](../../foundations/computational-entropy/definition.md)
**Reproducible artifacts:** `simulations/classical/m11_and_gate_ledger.py`, `m11_landauer_and_ledger.py`, `m11_composition_ledger.py`

---

## Abstract

We define **computational entropy** as the entropy of the *output distribution* induced by a map or channel on a random input, independent of the map's internal mechanics. Under this definition, maps that induce the same output distribution are informationally equivalent. We then give a clean thermodynamic account of the apparent local entropy reduction produced by an irreversible computation: for a deterministic map the drop is exactly the **export** \(H(X\mid Y)\) (the chain-rule remainder), which for a single evaluation coincides with the **Landauer** erased-bit count; for a stochastic channel the drop is \(H(X\mid Y)-H(Y\mid X)\). We show that the stage-wise export **ledger** is **path-dependent** — two circuits computing the same overall map can be charged different total export — and that this gap is an accounting quantity of the ledger convention, not a difference in minimum dissipated heat; and we identify the coordinate-invariant carrier of "information imparted" as mutual information / relative entropy, with differential entropy retained only as an illustrative (coordinate-dependent) special case. All quantitative claims are backed by short, exactly-reproducing reference computations. **No gravitational or continuum claims are made in this paper.**

---

## 1. Definition

Let \(f\) be any map — deterministic, stochastic, or a quantum channel — taking an input random variable \(X\sim p_X\) to an output \(Y\). The **computational entropy** of \(f\) on \(p_X\) is the entropy of the induced marginal output distribution \(p_Y\):


$$
H_c(f;p_X) := H(Y) = -\sum_y p_Y(y)\log_2 p_Y(y) \quad\text{(discrete)},
$$


$$
h_c(f;p_X) := h(Y) = -\int f_Y(y)\log_2 f_Y(y)\,dy \quad\text{(continuous)},
$$


$$
S_c(\Phi;\rho_X) := S(\Phi(\rho_X)) = -\operatorname{Tr}\!\big(\Phi(\rho_X)\log_2\Phi(\rho_X)\big) \quad\text{(quantum channel)}.
$$


The measure depends **only** on the statistical pattern of possible outputs — not on the algorithm, source of randomness, or gate structure that produced it.

### 1.1 Informational equivalence (A2)

**Proposition 1.** *If two maps \(f,g\) induce the same output law \(p_Y\), then \(H_c(f;p_X)=H_c(g;p_X)\), and every probability functional of the output (moments, tail probabilities, quantiles) agrees.*

*Example.* On \(U,U_1,U_2\sim\mathrm{Unif}[0,1]\), both \(Y_1=\sqrt U\) and \(Y_2=\max(U_1,U_2)\) have density \(f(y)=2y\) on \([0,1]\). Hence they are informationally equivalent, with


$$
h_c = -\int_0^1 2y\log_2(2y)\,dy = -1 + \frac{1}{2\ln 2} \approx -0.27865\ \text{bits}.
$$


(The reflected map \(\min(U_1,U_2)\) gives the same value by \(z=1-y\).)

**Caveat (recorded, A6).** The negative value here is a feature of *differential* entropy: \(h\) is **not** invariant under smooth reparameterization of \(y\) and can be negative. Differential entropy is therefore used **illustratively only**. The invariant statements below use discrete Shannon information and, in §5, mutual information.

---

## 2. Global conservation, local transfer

A computation can lower the entropy of the visible output below the entropy of its inputs. This is not a second-law violation; it is **local transfer with global conservation**.

**The AND gate.** Two fair bits \(X=(X_1,X_2)\), \(H(X)=2\) bits. Compute \(Y=X_1\wedge X_2\). Then


$$
H(Y)=h_2(\tfrac14)\approx 0.811278\ \text{bits}, \qquad H(X\mid Y)\approx 1.188722\ \text{bits},
$$


and the chain rule \(H(X)=H(Y)+H(X\mid Y)\) holds exactly (reference computation: chain error \(<10^{-12}\)). The visible entropy drops from 2 to 0.811 bits; the missing \(1.189\) bits are the **export** \(H(X\mid Y)\) — the distinguishability between input preimages that the map discards.

---

## 3. The export identity (A3)

**Theorem 1 (export = chain-rule remainder).** *Let \(X\sim p_X\) and let \(Y\) be produced from \(X\) by any channel \(p(y\mid x)\) (a deterministic map \(Y=f(X)\) is the special case \(p(y\mid x)\in\{0,1\}\)). Then the change of visible entropy from input to output is*


$$
H(X) - H(Y) = H(X\mid Y) - H(Y\mid X).
$$


*If the map is deterministic, \(H(Y\mid X)=0\) and this reduces to*


$$
\underbrace{H(X)}_{\text{input}} - \underbrace{H(Y)}_{\text{output }H_c} = H(X\mid Y) =: \text{export}.
$$


*Proof.* Apply the chain rule to the joint law \(p_X(x)\,p(y\mid x)\) in both orders: \(H(X,Y)=H(X)+H(Y\mid X)=H(Y)+H(X\mid Y)\). Rearranging gives \(H(X)-H(Y)=H(X\mid Y)-H(Y\mid X)\). If \(Y=f(X)\), then \(H(Y\mid X)=0\) (equivalently \(H(X,Y)=H(X)\)), which gives the reduced form. \(\square\)

*Remark (stochastic channels).* For a stochastic channel the visible drop \(H(X)-H(Y)\) equals the export \(H(X\mid Y)\) minus the channel noise \(H(Y\mid X)\), and it can be negative. The export \(H(X\mid Y)\) remains well defined in both cases. *(Corrected 2026-11-26: the earlier statement asserted \(H(X)-H(Y)=H(X\mid Y)\) for any map; that holds only when \(H(Y\mid X)=0\).)*

Define the **single-shot export/load slot** \(L_S := H(X\mid Y)\). It is the information the environment must absorb for the computation to be realized irreversibly.

---

## 4. Landauer-exactness (A4)

**Theorem 2 (Landauer coincidence, deterministic maps).** *For a deterministic map \(Y=f(X)\), the single-shot export \(L_S=H(X\mid Y)\) equals the number of bits whose erasure Landauer's principle charges: the minimum dissipated heat to realize the irreversible map at temperature \(T\) is*


$$
Q \ \ge\ kT\ln 2 \cdot H(X\mid Y) \ =\ kT\ln 2 \cdot L_S .
$$


For the AND gate, \(L_S = 1.188722\) bits, so \(Q\ge 1.188722\,kT\ln 2\). This is not a coincidence of numerics: the erased distinguishability *is* the conditional entropy, so the export ledger and the Landauer bound are the same quantity written twice. (Reference: `m11_landauer_and_ledger.py`.)

*Stochastic channels.* The coincidence uses Theorem 1 in its deterministic form \(H(X)-H(Y)=H(X\mid Y)\). For a stochastic channel the standard generalized (Shannon-entropy) form of Landauer's bound charges the entropy drop of the information-bearing state, \(Q\ge kT\ln 2\cdot[H(X)-H(Y)] = kT\ln 2\cdot[H(X\mid Y)-H(Y\mid X)]\), so the export \(H(X\mid Y)\) is then an upper bound on the Landauer charge rather than equal to it.

---

## 5. Path-dependence of cumulative export (A5)

The *final* map's export \(H(X\mid Z)\) is path-independent (it depends only on the overall input–output relation). The **cumulative** export charged by the stage-wise ledger along a pipeline is **not**.

**Theorem 3 (path-dependence of the export ledger).** *Under the stage-wise ledger convention — each stage is charged \(L_S=H(\text{declared stage inputs}\mid\text{stage output})\) and a pipeline's cost is the sum of its stage charges — there exist two pipelines computing the same overall map, with equal final \(H_c\) and equal final export \(H(X\mid Z)\), whose cumulative ledger export \(\sum L_S\) differs. The difference is an export-accounting quantity of the ledger convention, not a difference in minimum dissipated heat.*

*Witness.* Compare a **direct** AND against a **circuit** that first publishes an intermediate wire then ANDs. Both realize the same final law (\(H_{\text{final}}=0.811278\), \(H(X\mid Z)=1.188722\)), yet


$$
\sum L_S^{\text{direct}} = 1.188722, \qquad \sum L_S^{\text{circuit}} = 2.188722, \qquad \text{gap} = 1.000000\ \text{bit},
$$


the extra bit being the ledger's stage-1 charge for publishing \(Y=X_1\): the convention charges \(H(X\mid Y)=H(X_2\mid X_1)=1\) bit there although \(X_2\) is still held on a wire and is read by the stage-2 AND. No information is erased at stage 1 (the stage leaves \((Y,X_2)=(X_1,X_2)\) on wires, from which \(X\) is recoverable), so Theorem 2 assigns it no heat; on both paths the only erasure is the overall map \((X_1,X_2)\mapsto Z\), and the minimum dissipated heat is the same, \(Q\ge kT\ln 2\cdot H(X\mid Z)=1.188722\,kT\ln 2\). The 1-bit gap is therefore an export-accounting quantity (the ledger's convention), not a thermodynamic heat difference. (Reference: `m11_composition_ledger.py`; composition also verifies \(H(X\mid Y)+H(Y\mid Z)=H(X\mid Z)\) exactly and the data-processing inequality.) The active-work slot is likewise extensive (\(\sum L_E\): direct 1, circuit 2), and a soft-recoverability slot \(L_B\) is non-additive across independent regions.

**Interpretation.** The ledger charges export where information is *declared public* at a stage boundary, not merely by the abstract final function, so its cumulative total depends on how a computation is factored into stages even when the answer is unchanged — a discrete, exact statement that "the way you compute matters" *to the export ledger*. It is not a claim that refactoring changes the thermodynamic cost: by Theorem 2, heat is bounded by what is actually erased, which in the witness is the same on both paths. *(Corrected 2026-11-26: an earlier wording read the 1-bit gap as irreversibility "charged where information is made public / overwritten", i.e. as a physical cost; it is a ledger-counting effect.)*

---

## 6. The invariant carrier of "information imparted" (A6)

The motivating slogan — a computation makes outputs *less random*, hence *imparts information* — is made precise not by differential entropy (§1.1 caveat) but by **mutual information / relative entropy**, which are invariant under invertible reparameterization:


$$
I(X;Y) = H(Y) - H(Y\mid X) = D_{\mathrm{KL}}\!\big(p_{XY}\,\|\,p_X p_Y\big).
$$


For a deterministic \(f\), \(I(X;Y)=H(Y)=H_c\); the output entropy *is* the imparted information. For stochastic maps the two separate, and \(I(X;Y)\) is the correct invariant quantity. Paper A therefore states its physical (Landauer) and structural (path-dependence) results in terms of \(H(\cdot\mid\cdot)\) and \(I(\cdot;\cdot)\), and treats differential entropy as a non-invariant illustration only.

---

## 7. What this paper does not claim

Per [../DELIVERY_SCOPE.md](../DELIVERY_SCOPE.md) §1′: no gravitational channel, load-as-time-dilation, master equation, or Gravity-from-Entropy content; no identification of toy \(H_c\) with the von Neumann entropy of any physical channel; no claim that differential entropy is itself invariant; no derivation of thermodynamics beyond the Landauer bound it instantiates.

## 8. Continuation

The export identity (Thm 1) and its path-dependence (Thm 3) are the seed of a follow-on classical paper. **Paper C — *The Decay Algebra: From Export Ledgers to a Continuum Entropy-Production Density*** ([../02-computational-models/PAPER_C_decay_algebra.md](../02-computational-models/PAPER_C_decay_algebra.md)) shows that a *coupled* lattice of local maps has a well-defined export **density**, computes it with a belief-transfer operator (proved for 1D and general window widths), and takes a hydrodynamic limit to a continuum density field \(\sigma(x)\). Paper C is also classical and makes no gravitational claim.

---

## Appendix R — Reproducibility

All numeric claims reproduce exactly (rational arithmetic on finite models):

```bash
.venv/bin/python simulations/classical/m11_and_gate_ledger.py     # H(Y)=0.811278, export=1.188722, chain err <1e-12
.venv/bin/python simulations/classical/m11_landauer_and_ledger.py # L_S = H(X|Y) = Landauer erased bits
.venv/bin/python simulations/classical/m11_composition_ledger.py  # path-dep: ΣL_S 1.188722 vs 2.188722, gap 1.000000
```

| Quantity | Value | Source |
|----------|-------|--------|
| \(H(X)\) | 2 bits | AND ledger |
| \(H_c=H(Y)\) | 0.811278 bits | AND ledger |
| export \(H(X\mid Y)\) | 1.188722 bits | AND ledger |
| chain error | \(<10^{-12}\) | AND ledger |
| \(\sum L_S\) direct / circuit | 1.188722 / 2.188722 | composition ledger |
| path-dependence gap (ledger convention; not a heat difference) | 1.000000 bit | composition ledger |
| differential \(h_c\) of \(2y\) | \(-0.27865\) bits | §1.1 (illustrative) |

---

## Changelog

| Date | Entry |
|------|-------|
| 2026-07-29 | Initial draft: Def + Prop 1, Thm 1 (export), Thm 2 (Landauer), Thm 3 (path-dep), invariant framing, reproducibility. |
| 2026-11-26 | Thm 1 restated for any channel (\(H(X)-H(Y)=H(X\mid Y)-H(Y\mid X)\); deterministic case unchanged) with two-sided chain-rule proof; Thm 2 scoped to deterministic maps plus stochastic note; Thm 3 reworded so the 1-bit gap is a ledger-convention (export-accounting) quantity, not a heat difference. No numbers changed. |
