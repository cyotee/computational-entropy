# Program Conclusions — Computational Entropy / Emergent Gravity / GfE Dual

**Status:** Frozen program conclusions (2026-07-15)  
**Stance:** Preliminary research only. Constructions and ledgers are real; **nothing has GR-level certainty**. Prefer under-claiming.  
**Role:** Intellectual closure spine for the research program (no new experiment). Dense inventory of what is concluded, refuted, and left open under stated axioms and external inputs.

**Authority / companions**

| Artifact | Path |
|----------|------|
| Program paper **FINAL** | [`papers/06-synthesis/FINAL.md`](../papers/06-synthesis/FINAL.md) |
| Working twin | [`papers/06-synthesis/DRAFT.md`](../papers/06-synthesis/DRAFT.md) |
| Claims freeze (C1–C14 / non-claims) | [`synthesis/CURRENT_CLAIMS.md`](CURRENT_CLAIMS.md) |
| Pre-merge claim gate | [`synthesis/CLAIM_GATE.md`](CLAIM_GATE.md) |
| Bootstrap / settled tables | [`PROGRESS_REPORT.md`](../PROGRESS_REPORT.md) §2 |

Type safety throughout: load \(L\) is a **dimensionless scalar**; structure-induced \(G\) is a **metric** (or edgewise cousin). **\(L \neq G\)**.

---

## 1. What “concluded” means here

**Concluded** = *program-level* under:

- stated definitions and type rules (`foundations/`, `emergent-gravity/master-equation.md`, CLAIM_GATE layers W/D/G/M);
- constructive finite-model ledgers and hybrid/analytic dual notes in-repo;
- **imported** external theorems and literature used as *inputs* (Shannon chain rule, Landauer, Jacobson Clausius→Einstein, weak-field GR, Bianconi warm-up / PM as continuum flow cite) — **not** re-proved as GR-level physics truth.

**Not claimed:** empirical gravity from lattice toys; peer status of GfE with GR; symbolic identity of master equation and continuum GfE action; free derivation of Newton’s \(G\) from bits alone; continuum hydrodynamic limit of IDEM.

Labels on every bridge: **semantic / structural / constructive** (or **calibration**, **external theorem + assumption**, **hybrid-experimental**). Fail closed against CLAIM_GATE when mixing layers or entropy-object tags (A–E).

---

## 2. Positive conclusions P1–P11

| ID | Statement | Rigor | Primary source | DRAFT § |
|----|-----------|-------|----------------|---------|
| **P1** | Computational entropy is **output** entropy of a map/channel: classical \(H_c(f;p_X):=H(Y)\) (Shannon or differential); quantum/gravity \(S_c(\Phi;\rho):=S(\Phi(\rho))\). Mechanics of the map do not enter the definition (informational equivalence of equal-output-entropy maps). | **constructive** (def.) | [`foundations/computational-entropy/definition.md`](../foundations/computational-entropy/definition.md) | §1.1–1.2 |
| **P2** | Local entropy drop is accounted by **export**, not destruction: for finite classical maps the chain rule \(H(X)=H(Y)+H(X\mid Y)\) holds; AND-gate ledger gives \(H(Y)\approx 0.811\), export \(H(X\mid Y)\approx 1.189\), residual \(<10^{-12}\). | **constructive** | `simulations/classical/m11_and_gate_ledger.py` · M11 | §1.4, §2.4 |
| **P3** | Under Protocol R (reset residual input given \(Y\)), single-shot export equals Landauer bit-count: \(L_S^{\mathrm{disc}}:=H(X\mid Y)\) and \(Q_{\min}/(k_B T\ln 2)=H(X\mid Y)\). Inequality is external Landauer; identification of \(L_S\) with that object is structural contact — **not** Newton \(G\). | Shannon **constructive** + Landauer **external** + ID **structural** | [`m11e-landauer-export.md`](m11e-landauer-export.md) · `m11_landauer_and_ledger.py` | §2.8 |
| **P4** | Cumulative export \(\sum L_S\) is **path-dependent**: same final law \(H(Z)\), different circuit cost (Direct \(\sum L_S\approx 1.189\) vs Circuit \(\approx 2.189\) on fair-bit AND path vs multi-gate path). Load is not “final \(H_c\) alone.” | **constructive** | [`m11d-composition-laws.md`](m11d-composition-laws.md) · `m11_composition_ledger.py` | §2.7 |
| **P5** | Three **load axes** (roles) are required: work/energy-like \(L_E\), entropy flux/export \(L_S\), boundary/capacity \(L_B\). Monist \(L\propto H_c\) fails irreversible AND (output entropy low, export high). Continuum three-term \(L\) inherits the **same role split** only at language level. | **structural** (bookkeeping + motivation) | [`m11-idem-to-load.md`](m11-idem-to-load.md) · [`m11c-continuum-motivation.md`](m11c-continuum-motivation.md) · [`master-equation.md`](../emergent-gravity/master-equation.md) | §2.3, §2.9, §3.2 |
| **P6** | Continuum \(L(\rho,g)\) is **motivated** by discrete \(L^{\mathrm{disc}}\) role alignment (**m11c**); it is **not identified** with \(L^{\mathrm{disc}}\) and not obtained as a proved hydrodynamic limit of IDEM. | **structural motivation**; non-equality **explicit** | [`m11c-continuum-motivation.md`](m11c-continuum-motivation.md) | §2.9–2.10, §3.2, §7.3 |
| **P7** | Newtonian Poisson is recovered **only** via **Path J/M**: Clausius on \(\mathcal{L}_g\) → Einstein (Jacobson, imported) → weak-field \(\nabla^2\Phi=4\pi G\rho_m\); then on-shell load-clock match \(\alpha\beta=4\pi G/c^4\) (**calibration**, not free \(G\)). Pointwise Laplacian path **withdrawn** (W1). | Path J: **external thm + assumption**; Path M: **calibration** | [`emergent-gravity/recoveries/newtonian/README.md`](../emergent-gravity/recoveries/newtonian/README.md) · [`m8-newton-recovery-audit.md`](m8-newton-recovery-audit.md) | §4 |
| **P8** | Euclidean **ACD-EW** dual is constructive (warm-up \(G[\phi]\), PM ↔ observation channel + split load + clock). Residual dual PM vs heat is **time-windowed (T1′)**, not all \(t\); unified pure window \(U_\star=[1.36,2.40]\) under PCRH\(_b\) with \(\rho_b=0.42\) (**soft**). Joint toys **6/6 SUPPORT** = dual **pattern**, not continuum gravity. | constructive + analytic + hybrid-exp.; PCRH\(_b\) **soft** | [`action-channel-duality-euclidean.md`](action-channel-duality-euclidean.md) · [`m1g-unified-pure-window.md`](m1g-unified-pure-window.md) · [`t1-prime-hybrid-writeup.md`](t1-prime-hybrid-writeup.md) | §5 |
| **P9** | Layer **W**: continuum warm-up energy/action gradient flow is (classical) Perona–Malik (**external lit**); discrete joint-toy PM **descends** a matched edge energy (M5c witness). Residual dual stays Layer **D** — energy descent ≠ residual dual theorem; full \(\Gamma\)-limit open. | external lit + discrete **constructive** / hybrid | [`m5c-warmup-pm-gradient-flow.md`](m5c-warmup-pm-gradient-flow.md) · Bianconi “Beyond holography” | §5.5 |
| **P10** | **M6:** both master-equation framework and continuum GfE → \(\nabla^2\Phi=4\pi G\rho_m\) at leading weak field via Einstein/GR (**WEAK PASS**). Framework identity **FAIL** (mechanisms, symbol maps, next-order slots diverge). | **WEAK PASS** Poisson / **FAIL** identity | [`m6-weak-field-plugtest.md`](m6-weak-field-plugtest.md) · [`m6b-next-order-weak-field.md`](m6b-next-order-weak-field.md) | §6 |
| **P11** | **R4a / M6d:** next-order identification of GfE metric extras (\(D_{\mu\nu},\Lambda_G\)) with load-clock \(\gamma_L,\delta_L\) is a **structural no-go** without an extra **promotion** rule moving load corrections into the metric sector (or dual collapse). Present master equation does **not** supply that rule. | **structural** no-go | [`m6d-promotion-nogo.md`](m6d-promotion-nogo.md) | §6.4, §7.4 |

**Supporting frozen claims (CURRENT_CLAIMS C1–C14)** map into P7–P10 and dual subclaims of P8; C14 (semantic high-flux \(L\) reading) underwrites P5–P6 polarity. Dual program status: **settled enough to stop as main open crisis** (optional PCRH\(_b\) pure proof = paper depth only).

---

## 3. Refuted / withdrawn W1–W6

Do **not** revive. Each is either invalid algebra, false on evidence, or an explicit program non-claim.

| ID | Statement (refuted / withdrawn) | Why | DRAFT / freeze |
|----|----------------------------------|-----|----------------|
| **W1** | Pointwise \(\Phi\propto\rho_m\Rightarrow\nabla^2\Phi\propto\nabla^2\rho_m\Rightarrow\) Newtonian Poisson | Nonlocal \(\Phi\); \(\nabla^2\rho_m\not\propto-\rho_m\) in general. **Withdrawn** recovery path. | §4.5; N5; M8 |
| **W2** | Residual dual (PM residual \(\le\) heat residual) for **all** \(t\in(0,t_\star]\) | False: short-\(t\) heat can win (noise race); use **T1′** / \(U_\star\). | §5.3; N3; C4–C5, C7 |
| **W3** | \(L\equiv G\) (or \(S_c\equiv\operatorname{Tr} g\ln G^{-1}\), \(\alpha_L\beta_L\equiv\alpha_B/\beta_B\)) | Type error (scalar vs metric); M7 refuse numerical map. | §3.5; N2; C12 |
| **W4** | Master equation \(\Leftrightarrow\) continuum Bianconi GfE (symbolic or dynamical identity) | M6 FAIL identity; different primary entropy / EL structure. | §6; N1; C12 |
| **W5** | IDEM/decay (or Phase 1–2 ledgers) **construct** continuum \(L(\rho,g)\) or metric \(G\) | Discrete bookkeeping ≠ continuum limit; N9 deferred. | §2.10, §7.3; P6 non-identity |
| **W6** | Lattice denoising / dual toys = **empirical gravity** | Layer D pattern witnesses only; \(\phi\) is test signal, not spacetime. | §5.4; N7 |

**Also frozen non-claims (not re-listed as W-ids):** pure T1′ with no soft hypotheses (N4); \(\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G\) without promotion (N6 / covered by P11); GfE literature as GR-peer foundation (N8).

---

## 4. Open O1–O5

These need **new theory** (missing theorems/constructions), **experiment** (after predictions), or both — not re-assertable from current freeze.

| ID | Open item | Why still open | Bucket |
|----|-----------|----------------|--------|
| **O1** | Continuum / hydrodynamic limit: \(L^{\mathrm{disc}}\to L(\rho,g)\) or IDEM \(\to\) continuum fields / \(G\) | No scale-separation theorem; m11c is motivation only | **New theory** |
| **O2** | M5 full warm-up continuum (\(\Gamma\)-limit, BV, residual dual continuum T4) | Smooth \(O(h)\) sketch only; Γ not claimed | **New theory** |
| **O3** | Positive continuum \(S_c\) path; no \(H_c^{\mathrm{toy}}\equiv S_c\) | Non-identity settled; positive construction open | **New theory** |
| **O4** | M9 Lorentzian / full continuum dual beyond Euclidean warm-up | High cost; M6 already FAIL identity at weak field | **New theory** (then optional experiment) |
| **O5** | Pure PCRH\(_b\); true game \(H_c^{\mathrm{game}}\); BH/cosmo recoveries at Path J/M honesty | Soft dual SI; belief dual ≠ EV; recoveries deferred | **New theory** (optional) |

**Not open as crisis:** heat/PM residual dual as main board item (program-closed at T1′ / \(U_\star\) honesty).

### Full avenue map (required reading for next cycle)

**→ [OPEN_AVENUES.md](OPEN_AVENUES.md)** — what “new theory” means; missing theorem statements for O1–O5; experiment bucket; priority order for a new research cycle.

---

## 5. External theories used as inputs

| Input | Role in program | Where used |
|-------|-----------------|------------|
| **Shannon entropy / chain rule / DPI** | Definition of \(H_c\); export identity; composition lemmas | P1–P4; M11d |
| **Landauer principle** | Lower bound \(Q\ge k_B T\ln 2\cdot H(X\mid Y)\) under Protocol R | P3; M11e |
| **Jacobson (1995) Clausius → Einstein** | Path J continuum content of \(\delta Q=T\,dS_c\) on local horizons | P7 |
| **GR weak-field / Poisson** | \(\nabla^2\Phi=4\pi G\rho_m\) from Einstein linearization | P7, P10 |
| **Bianconi GfE + warm-up lit** (relative entropy of metrics; PM as GfE Euclidean flow / “Beyond holography”) | Macro target Stage 3; Layer W continuum flow cite; M6 co-class comparison | P8–P11; ACD-EW |

These are **dependencies**, not outputs of the program. Imported theorems keep their external rigor; program conclusions inherit that dependence (e.g. Path J is not “Einstein from bits alone”).

---

## 6. One-paragraph program conclusion

Under its own axioms and the external inputs above, the computational-entropy program concludes that **output entropy** (\(H_c\)/\(S_c\)) is the right primitive for map/channel bookkeeping; that **local entropy drops export** via the chain rule and contact **Landauer** on single-shot \(L_S=H(X\mid Y)\); that **demand** is multi-axial (work / export flux / capacity), path-dependent under composition, and only **motivates**—does not identify—continuum load \(L\); that Newtonian Poisson is a **calibrated low-load regime** of a load-clocked channel only through **Path J/M** (Jacobson→Einstein→Poisson + \(\alpha\beta=4\pi G/c^4\)), never the withdrawn pointwise Laplacian; that a **constructive Euclidean dual (ACD-EW)** to Bianconi’s warm-up exists with **time-windowed** residual dual \(U_\star\) under soft PCRH\(_b\); and that continuum GfE contact is at most a **WEAK PASS** on shared weak-field Poisson via GR, with **FAIL** of framework identity and a **structural no-go** on next-order slot identity without promotion. Continuum construction of \(L\) or \(G\) from IDEM, Lorentzian GfE lift, and full warm-up \(\Gamma\)-limits remain **open**. This freezes the program’s intellectual spine without claiming GR-level physics truth.

---

## 7. Maintenance

- **Do not** expand this file into full proofs — link primary sources.  
- When a P/W/O status changes, update here **and** [`CURRENT_CLAIMS.md`](CURRENT_CLAIMS.md), [`PROGRESS_REPORT.md`](../PROGRESS_REPORT.md) §2, and the DRAFT non-claims banner under [`CLAIM_GATE.md`](CLAIM_GATE.md).  
- Default: treat [`FINAL.md`](../papers/06-synthesis/FINAL.md) as frozen; plan **new cycles** via [`OPEN_AVENUES.md`](OPEN_AVENUES.md).  
- Do not reopen dual residual crisis or invent continuum limits without the missing theorems listed there.

---

*Frozen 2026-07-15. Intellectual closure artifact for the computational-entropy research program. Open-avenue detail lives in OPEN_AVENUES.md.*
