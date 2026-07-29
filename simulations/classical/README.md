# simulations/classical/

Discrete / classical computational models — pure accounting and multi-step load ledgers (M11).

Design: [`synthesis/m11-idem-to-load.md`](../../synthesis/m11-idem-to-load.md)

---

## M11 Phase 1 — AND-gate load ledger

| Path | Role |
|------|------|
| [`m11_and_gate_ledger.py`](m11_and_gate_ledger.py) | Exact \(H_c\), export \(H(X\mid Y)\), discrete \(L_E,L_S,L_B\) for fair-bit AND |

```bash
.venv/bin/python simulations/classical/m11_and_gate_ledger.py
```

**What it shows:** one irreversible gate evaluation drops output entropy to \(H(Y)\approx 0.811\) bits while **export** \(H(X\mid Y)\approx 1.189\) bits feeds **high** \(L_S\) (locked reading: flux/scrambling raises load).

---

## M11 Phase 2 — multi-step / lambda / shoe ledgers

| Path | Role |
|------|------|
| [`m11_multistep_boolean_ledger.py`](m11_multistep_boolean_ledger.py) | Composition id → AND → OR on fair bits; multi-row ledger + optional \(k_{\mathrm{eff}}\) clock diagnostic |
| [`m11_tiny_lambda_ledger.py`](m11_tiny_lambda_ledger.py) | Tiny SKI combinator ensemble; normal-order redex steps; \(H_c\) over term-shape classes |
| [`m11_minimal_shoe_ledger.py`](m11_minimal_shoe_ledger.py) | Minimal R/B residual multiset shoe (M12-adjacent); predictive \(H_c\) + order-entropy \(L_B\) |

```bash
.venv/bin/python simulations/classical/m11_multistep_boolean_ledger.py
.venv/bin/python simulations/classical/m11_tiny_lambda_ledger.py
.venv/bin/python simulations/classical/m11_minimal_shoe_ledger.py
# optional: all three back-to-back
.venv/bin/python simulations/classical/_run_m11_phase2.py
```

### Multi-step Boolean

- Steps: baseline id on \((X_1,X_2,X_3)\); \(A=X_1\land X_2\) (high export); \(B=A\lor X_3\) (lower export).
- Exact Shannon on finite supports; chain-rule checks; load clock \(k_{\mathrm{eff}}=\sum 1/(1+\alpha' L^{\mathrm{disc}})\) with \(\alpha'=0.1\) **diagnostic only** (not continuum \(\tau\)).
- Locked reading assert: larger \(H(X\mid Y)\) ⇒ larger \(L_S\).

### Tiny SKI lambda

- Fixed ensemble of closed SKI terms; one normal-order redex per step.
- \(H_c\) = Shannon of serialized term shape under the ensemble.
- \(L_E\) = mean redex count pre-step; \(L_S=|\Delta H_c|\); \(L_B\) = fraction still open (has redex).

### Minimal shoe (M12-adjacent)

- Fixed-sequence \(6\mathrm{R}+6\mathrm{B}\) multiset; after each draw, exact binary \(H_c\) of next class.
- \(L_E=1\) (count update); \(L_S=|\Delta H_c|\); \(L_B=H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)\).

---

## M11.3 — coupled-regions product ledger

| Path | Role |
|------|------|
| [`m11_coupled_regions_ledger.py`](m11_coupled_regions_ledger.py) | Two regions A/B with independent ANDs then shared export screen \(S=Y\oplus V\); regional + global conservation |

```bash
.venv/bin/python simulations/classical/m11_coupled_regions_ledger.py
```

**Model (exact finite Shannon on \(\{0,1\}^4\)):**

1. \(k=0\): idle priors — region A on \(X=(X_1,X_2)\), B on \(Z=(Z_1,Z_2)\), global \((X,Z)\); \(H=2,2,4\).
2. \(k=1\): independent local ANDs \(Y=X_1\land X_2\), \(V=Z_1\land Z_2\); per-region Phase-1 style \(H_c\), export \(H(X\mid Y)\), \(L_E,L_S,L_B\); global \((Y,V)\).
3. \(k=2\): couple via screen \(S=Y\oplus V\); declared outputs \(O_A=(Y,S)\), \(O_B=(V,S)\), \(O_G=(Y,V,S)\); plus screen-only diagnostic \(O=S\) (forget \(Y,V\) into environment).

**What it shows:**

- Chain rules: \(H(X)=H(Y)+H(X\mid Y)\), \(H(X,Z)=H(Y,V)+H(X,Z\mid Y,V)\), exports add across independent regions.
- Locked reading: local high export \(\Rightarrow\) high local \(L_S\) on each AND.
- After coupling, \((Y,S)\leftrightarrow(Y,V)\) (each region learns the other AND via \(S\)); local input export unchanged; global bookkeeping intact.
- Screen-only row: \(H(X,Z)=H(S)+H(X,Z\mid S)\) — information redistributed to environment, not destroyed.
- Optional per-region discrete load clock \(k_{\mathrm{eff}}\) (diagnostic only).

**What it does not show:** continuum \(L\), \(L\equiv G\), gravity, dual-toy residual \(H_c\), or product regions as spacetime / continuum \(\rho\).

---

## M11d — composition laws for \(H_c^{\mathrm{disc}}\) / \(L^{\mathrm{disc}}\)

| Path | Role |
|------|------|
| [`m11_composition_ledger.py`](m11_composition_ledger.py) | Finite Shannon: pure-cascade export additivity, circuit path-dependent \(\sum L_S\), \(L_E\) sum, DPI, \(L_B\) non-additivity |
| Design | [`synthesis/m11d-composition-laws.md`](../../synthesis/m11d-composition-laws.md) |

```bash
.venv/bin/python simulations/classical/m11_composition_ledger.py
```

**What it shows:**

- **Lemma B (pure cascade):** \(Y=X_1\land X_2\), \(Z=\mathrm{NOT}(Y)\) \(\Rightarrow\) \(H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)\) exact; DPI \(H(Z)\le H(Y)\).
- **Path dependence (circuit):** Direct AND vs publish \(Y=X_1\) then \(Z=Y\land X_2\) — same final \(H(Z)\approx 0.811\) and same \(H(X\mid Z)\approx 1.189\), but \(\sum L_S\) is \(\approx 1.189\) vs \(\approx 2.189\).
- **\(L_E\):** sequential ops add (\(1\) vs \(2\)).
- **\(L_B\) non-additivity:** two independent ANDs give \(L_B(A)+L_B(B)=1\neq 0.5=L_B(\mathrm{global\ mean})\).

**What it does not show:** continuum \(L\), \(L\equiv G\), gravity, dual-toy residual \(H_c\), or composition laws of continuum load.

---

## M11e — Landauer contact for export / \(L_S\)

| Path | Role |
|------|------|
| [`m11_landauer_and_ledger.py`](m11_landauer_and_ledger.py) | Fair-bit AND: \(H(X)\), \(H(Y)\), export \(H(X\mid Y)\), Landauer bound in units of \(k_B T\ln 2\) |
| Design | [`synthesis/m11e-landauer-export.md`](../../synthesis/m11e-landauer-export.md) |

```bash
.venv/bin/python simulations/classical/m11_landauer_and_ledger.py
```

**What it shows:**

- Protocol R (reset after AND): erased bits \(:= H(X\mid Y)\approx 1.188722\); Landauer \(Q\ge k_B T\ln 2\cdot H(X\mid Y)\); in units of \(k_B T\ln 2\), bound \(=\) export \(= L_S\).
- Protocol V (reversible dilation with garbage \(G=X\)): \(H(Y,G)=H(X)\); garbage entropy \(H(G\mid Y)=H(X\mid Y)\) parks export until \(G\) is erased — same cost when paid.
- Chain rule \(H(X)=H(Y)+H(X\mid Y)\) exact; \(k_B T\ln 2\) is standard conversion only (not gravity-fitted).

**What it does not show:** Newton \(G\), \(\hbar\), holographic area, \(L\equiv G\), ME \(\Leftrightarrow\) GfE, continuum \(L\).

---

## Non-claims (all scripts)

Do **not** assert from these ledgers:

- continuum \(L(\rho,g)\) equality, \(L\equiv G\), Einstein/Newton recovery
- GfE identity or master-equation \(\Leftrightarrow\) continuum GfE
- ACD-EW dual-toy residual \(H_c\) (lattice \(\phi\)) as classical strategy / gate \(H_c\)
- blackjack EV / strategy ROI / bankroll (shoe script is **not** EV)
- discrete \(k_{\mathrm{eff}}\) as continuum proper time
- coupled classical regions as spacetime patches or continuum \(\rho\)
- Landauer contact \(\Rightarrow\) Newton \(G\), \(\hbar\), holographic area, or continuum \(L\) identity (M11e is thermodynamic bookkeeping only)
- composition laws of continuum load / \(L^{\mathrm{disc}}=L(\rho,g)\) (M11d is finite classical only)

**Allowed claim form:** constructive \(H_c\) + three-term discrete load ledger with the same *roles* as master-equation load slots under the locked high-flux reading; optional Landauer bound on export \(H(X\mid Y)\) via standard \(k_B T\ln 2\); finite composition/export path-dependence (Tag E) without continuum transfer.
