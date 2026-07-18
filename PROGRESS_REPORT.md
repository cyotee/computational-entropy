# Progress Report — Computational Entropy / Emergent Gravity / GfE Dual

**Date:** 2026-07-15 (updated D15: FINAL program report + conclusion freeze)  
**Purpose:** Bootstrap a **new session or agent context**. Read this document first; follow links only for depth.  
**Branch:** `master` (as of report writing; working tree may have uncommitted synthesis).  
**Stance:** All of this is **preliminary research**. Supporting constructions and evidence are real; nothing here has GR-level certainty.  
**Claims freeze:** [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · **Conclusions:** [synthesis/PROGRAM_CONCLUSIONS.md](synthesis/PROGRAM_CONCLUSIONS.md)  
**Post-freeze avenues:** [synthesis/OPEN_AVENUES.md](synthesis/OPEN_AVENUES.md) · **Integrated paper:** [papers/06-synthesis/PAPER.md](papers/06-synthesis/PAPER.md) · **FINAL freeze:** [papers/06-synthesis/FINAL.md](papers/06-synthesis/FINAL.md)

---

## 0. How to use this report in a new context

1. Read **§1–§4** (mission, settled claims, non-claims).  
2. Skim **§5** (what we built) and **§6** (file map).  
3. Use **§7–§8** (open board + **recommended next avenues**).  
4. **If starting a new research cycle:** [synthesis/OPEN_AVENUES.md](synthesis/OPEN_AVENUES.md) (buckets: concluded / new theory / experiment; missing theorems for O1–O5).  
5. For math detail: [synthesis/PACK_INDEX.md](synthesis/PACK_INDEX.md) → [synthesis/OPEN_MATH_DECISION_LOG.md](synthesis/OPEN_MATH_DECISION_LOG.md).  
6. For product/mission: [PRD.md](PRD.md) · [THEORY.md](THEORY.md) · FINAL report.

**Do not** restart heat-vs-PM residual dual from scratch unless the user asks for a paper-quality pure theorem without MC soft spots.

---

## 1. Mission (one paragraph)

Define **computational entropy** as entropy of a map/channel’s **output distribution**; develop a **gravitational channel** \(\Phi_g\) with **computational load** \(L\) and master equation that recovers gravity phenomenology in limits; **bridge** that framework to continuum **Gravity-from-Entropy (GfE)** (Bianconi et al.) via a staged workflow — without forcing premature symbolic identity of actions and master equations. Classical/lambda **IDEM** machinery is the intended long-term microstructure for the channel, still largely unconnected to gravity recoveries.

### Three-stage workflow (canonical mental model)

```text
STAGE 1 — Computational induction (OURS)
  ρ, Φ_g, S_c / H_c, load L, dτ = dt/(1+αL)
  IDEM / decay / games as discrete microstructure (aspirational)
        │
        ▼
STAGE 2 — Geometric imprint (BRIDGE)
  Structure-induced metric G  (or computational cousin)
  Type safety: L is a scalar; G is a metric — L ≠ G
        │
        ▼
STAGE 3 — Continuum entropic gravity (GfE MACRO)
  Relative entropy of metrics → modified Einstein, Λ_G, G-field
  Low coupling → EH / Newton via GR
```

---

## 2. What is settled (freeze these unless reopening with evidence)

### 2.1 Conceptual / claim hygiene

| Settled claim | Notes |
|---------------|--------|
| **ACD-EW exists** | Constructive **Euclidean** dual between GfE **warm-up** (induced \(G[\phi]\), PM flow) and observation channel + split load + load clock |
| **Toys support the dual pattern** | 1D, 2D, blackjack-belief: **6/6 SUPPORT** scorecards — pattern robust, not gravity confirmation |
| **PM > heat on edged structure is expected** | Structure-preserving dual reconstructor should beat isotropic heat; **not a theory problem** |
| **Residual dual is time-windowed (T1′)** | Ultra-short \(t\): heat can win residual (noise race). Intermediate: PM wins. Not “duality breaks” |
| **Unified pure residual window \(U_\star=[1.36,2.40]\)** | Under PCRH\(_b\) with \(\rho_b=0.42\); covers former hybrid \(I_\star\) + late pure window ([m1g](synthesis/m1g-unified-pure-window.md)) |
| **Load clock dual (M2) hybrid** | Load-PM ≈ mild time change of PM (\(\tau/t\sim 0.95\)); still beats heat on dual window |
| **Newton = Path J/M only** | Clausius → Einstein (Jacobson) → Poisson; \(\alpha\beta=4\pi G/c^4\) = on-shell **calibration**. Pointwise \(\Phi\propto\rho\Rightarrow\nabla^2\) **withdrawn** |
| **M6 WEAK PASS / FAIL identity** | Both frameworks → \(\nabla^2\Phi=4\pi G\rho_m\) via Einstein/GR; **not** framework equivalence |
| **Next-order structural FAIL** | GfE extras live in metric EOM (\(D_{\mu\nu},\Lambda_G\)); our \(\gamma_L,\delta_L\) live in load **clock** unless promoted |
| **\(L\) reading** | Prefer: demand from **scale/rate of possible channel outcomes** (energy + entropy production + boundary), not “stockpile of identity left to compute.” Active identity loss / scrambling → **higher** \(L\), not lower |

### 2.2 What “jump / heat / PM” means (for new agents)

| Term | Meaning in dual toys |
|------|----------------------|
| **Field \(\phi\)** | Scalar **test signal** on a flat lattice (like image brightness) — **not** spacetime geometry |
| **Jump** | Ground-truth **step edge** in that test signal — **test data**, not a gravity well |
| **Heat** | Isotropic diffusion denoiser (smears noise **and** edges) |
| **PM** | Edge-aware diffusion (GfE warm-up gradient flow); protects large gradients |
| **Why chase** | Only sharp, code-level handshake with Bianconi **warm-up**; not a model of smooth GR wells |

**Research-program status of heat/PM dual:** **Settled enough to stop as main open problem.** Further pure-proof polishing is optional paper depth, not crisis response.

### 2.3 Explicit non-claims (do not assert without new work)

1. Master equation \(\Leftrightarrow\) Bianconi continuum GfE.  
2. \(L \equiv G\), \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\), \(\alpha_L\beta_L \equiv \alpha_B/\beta_B\).  
3. T1 residual domination for all \(t\in(0,t_\star]\) (false; use T1′ / \(U_\star\)).  
4. Pure T1′ with **no** soft hypotheses (PCRH\(_b\) still ensemble-certified).  
5. Newton from pointwise \(\Phi\propto\rho\) Laplacian.  
6. Next-order \(\gamma_L,\delta_L\) equal GfE \(D_{\mu\nu},\Lambda_G\).  
7. Lattice denoising = empirical gravity.  
8. External GfE papers established on par with GR.  
9. IDEM/decay fully constructs continuum \(L\) or \(G\) (still open / deferred).

---

## 3. Work completed this arc (2026-07-13 → 2026-07-15)

### 3.1 Literature & bridge

- Integrated Bianconi *Gravity from entropy* (arXiv:2408.14391 / PRD 2025) and related papers (Beyond holography, Thattarampilly–Zheng, Kumar) under `papers/external/`.  
- Living bridge: [synthesis/bridge-bianconi-relative-entropy.md](synthesis/bridge-bianconi-relative-entropy.md).  
- Transfer / non-transfer dictionary: [synthesis/acd-ew-continuum-transfer.md](synthesis/acd-ew-continuum-transfer.md).  
- Formal dual: [synthesis/action-channel-duality-euclidean.md](synthesis/action-channel-duality-euclidean.md) (**ACD-EW**).

### 3.2 Experiments (Euclidean dual layer)

| Artifact | Outcome |
|----------|---------|
| 1D joint toy `_joint_toy_v2_core.py` | **6/6 SUPPORT** |
| 2D Catte PM toy | **6/6 SUPPORT** |
| Blackjack belief dual | **6/6 pattern only** (not real edge / GfE) |
| T1 MC envelopes | Short-\(t\) heat win; intermediate PM win; persistence strong |

**Interpretation:** Euclidean dual **pattern is saturated** for more scorecards of the same kind.

### 3.3 Analytic dual program (M1 series)

| ID | Result |
|----|--------|
| M1 / C′ | Strict Lemma C fails; weakened C′ localization |
| T1′ | Residual dual on \([t_{\min},t_{\max}]\); not \((0,t_\star]\) |
| M1b–M1d | C′2, \(\Delta_{\mathrm{noise}}=R_{\mathrm{blur}}\) race, hybrid E′ |
| M1e–M1f | Spectral freeze-tax; pure window with \(\rho_{\mathrm{eff}}\approx 0.30\) from \(t=2\) |
| **M1g** | **Unified pure \(U_\star=[1.36,2.40]\)** with \(\rho_b=0.42\) (PCRH\(_b\) soft) |
| M2 | Load-PM hybrid dual vs heat |

### 3.4 Gravity-facing program (M6–M8)

| ID | Result |
|----|--------|
| M8 | Newton.md algebraic gap documented |
| Path J/M rewrite | Canonical: [emergent-gravity/recoveries/newtonian/README.md](emergent-gravity/recoveries/newtonian/README.md) · [quantum/Newton.md](quantum/Newton.md) |
| M7 | Symbol map; refuse numerical \(\alpha_L=\alpha_B\) |
| M6 | WEAK PASS Poisson; FAIL identity |
| M6b/M6c | Next-order structural FAIL; Bianconi PDF Eqs. 60–68 linearization sketch |

### 3.5 Decisions (D1–D8)

See [synthesis/OPEN_MATH_DECISION_LOG.md](synthesis/OPEN_MATH_DECISION_LOG.md).  
**Latest:** D8 — unified pure residual window \(U_\star\); dual residual program no longer the default open crisis.

---

## 4. Conceptual clarifications locked in conversation

1. **Jump** = test-data edge in scalar field \(\phi\), not spacetime kink, not “jump in information throughput.”  
2. **Heat / PM** = two denoising algorithms (isotropic vs edge-aware); thermal language is analogy.  
3. **PM > heat** on edged structure = **expected dual success**, not a bug.  
4. **Time windows** = when residual favors PM, and how we **prove** it — not duality turning on/off as a framework.  
5. **Load \(L\)** ≈ demand from **possibility space / energy / entropy flux**, not remaining identity stockpile; active decoherence/scrambling → **higher** \(L\).  
6. **Further residual dual chasing** = diminishing returns unless paper theorem without MC.

---

## 5. Key file map (start here)

### Bootstrap

| File | Use |
|------|-----|
| **This report** | New-context orientation |
| [PRD.md](PRD.md) | Mission + staged workflow |
| [THEORY.md](THEORY.md) | Thread map + GfE correspondence |
| [synthesis/PACK_INDEX.md](synthesis/PACK_INDEX.md) | Full synthesis pack |
| [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) | Frozen settled / non-claims |
| [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) | M11 design + Phase 1 status |
| [synthesis/OPEN_MATH_DECISION_LOG.md](synthesis/OPEN_MATH_DECISION_LOG.md) | M1–M12 board + D1–D9 |

### Dual (settled layer)

| File | Use |
|------|-----|
| [synthesis/action-channel-duality-euclidean.md](synthesis/action-channel-duality-euclidean.md) | ACD-EW formal dual |
| [synthesis/acd-ew-continuum-transfer.md](synthesis/acd-ew-continuum-transfer.md) | What may/may not transfer |
| [synthesis/t1-prime-hybrid-writeup.md](synthesis/t1-prime-hybrid-writeup.md) | Paste-ready dual claims |
| [synthesis/m1g-unified-pure-window.md](synthesis/m1g-unified-pure-window.md) | \(U_\star\) pure residual dual |
| [synthesis/m2-t1-load.md](synthesis/m2-t1-load.md) | Load clock dual |
| `simulations/bridging/_joint_toy_v2_core.py` | 1D toy + CLI |
| `simulations/bridging/test_t1_unified_pure.py` | \(U_\star\) witness |

### Gravity / GfE contact

| File | Use |
|------|-----|
| [emergent-gravity/master-equation.md](emergent-gravity/master-equation.md) | Canonical \(L\), \(d\tau\), \(\mathcal{L}_g\) |
| [emergent-gravity/recoveries/newtonian/README.md](emergent-gravity/recoveries/newtonian/README.md) | Path J/M Newton |
| [synthesis/m6-weak-field-plugtest.md](synthesis/m6-weak-field-plugtest.md) | WEAK PASS / FAIL |
| [synthesis/m6c-bianconi-linearization.md](synthesis/m6c-bianconi-linearization.md) | PDF-anchored next order |
| [papers/external/](papers/external/) | Bianconi + follow-ons |

### Classical / IDEM (M11 started)

| Path | Use |
|------|-----|
| [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) | Design dictionary IDEM → \(H_c\), \(L^{\mathrm{disc}}\) |
| `simulations/classical/` | Phase 1–2 ledgers (AND, multi-step, SKI, shoe) |
| [papers/06-synthesis/OUTLINE.md](papers/06-synthesis/OUTLINE.md) | Paper outline (drafting map) |
| [synthesis/m10-sc-vs-toy-hc.md](synthesis/m10-sc-vs-toy-hc.md) | Entropy object map (tags A–E) |
| [synthesis/m5-warmup-continuum-hygiene.md](synthesis/m5-warmup-continuum-hygiene.md) | Warm-up continuum honesty |
| `computational-models/`, root IDEM markdowns | Identity, decay vectors, games |
| THEORY.md “central gap” | Gravity still not continuum-connected to IDEM; discrete slots now exist |

---

## 6. Open math board (snapshot)

| ID | Status | Priority note |
|----|--------|----------------|
| **M1** residual dual | **Program-level settled** (\(U_\star\)); optional harden PCRH\(_b\) | Do not default-chase |
| **M2** load dual | Hybrid done | Optional pure |
| **M3–M4** Lyapunov / reparam | Deferred | After identity score if needed |
| **M5** warm-up continuum | Hygiene + [m5b smooth sketch](synthesis/m5b-smooth-action-limit.md); Γ open | Paper cite |
| **M6–M8** gravity contact | Done as analysis | Optional PPN / solar-system |
| **M9** Lorentzian GfE lift | Deferred | High cost |
| **M10** \(S_c\) vs toy \(H_c\) | Dictionary + **P1 non-identity** ([p1](synthesis/m10-p1-object-comparison.md)) | \(S_c\) path still open |
| **M11** IDEM → \(H_c\) / \(L^{\mathrm{disc}}\) | **P1–2 + coupled + m11c motivation** (D12) | Optional lattice of gates |
| **M12** true game \(H_c\) | Deferred | Classical depth (M11 slots ready) |

---

## 7. Recommendations — avenues to pursue next

### 7.1 Status after D13 (2026-07-15)

**Done this arc (D9–D13):** dual freeze, CLAIM_GATE, M11 microstructure, M10/M5 hygiene, **plus relationships:**

| Relationship | Artifact | External theory |
|--------------|----------|-----------------|
| Composition / path-dep load | [m11d](synthesis/m11d-composition-laws.md) · `m11_composition_ledger.py` | Shannon / DPI / chain rule |
| Landauer ↔ export \(L_S\) | [m11e](synthesis/m11e-landauer-export.md) · `m11_landauer_and_ledger.py` | Landauer bound |
| Warm-up ↔ PM energy descent | [m5c](synthesis/m5c-warmup-pm-gradient-flow.md) · `m5c_pm_energy_descent.py` | Bianconi warm-up / PM PDE |

**Key new conclusions (D13):**  
(1) \(\sum L_S\) is **path-dependent** (same final \(H_c\), circuit pays +1 bit vs direct AND).  
(2) Single-shot \(L_S = H(X\mid Y)\) is exactly the bit count in \(Q\ge kT\ln2\cdot H(X\mid Y)\).  
(3) Layer W: discrete PM **descends** matched warm-up energy; residual dual stays Layer D.

### 7.2 Default recommendation (post-D15)

**Program claim-freeze cycle is closed.**

| Artifact | Path |
|----------|------|
| **Integrated paper (publish review)** | [papers/06-synthesis/PAPER.md](papers/06-synthesis/PAPER.md) (~22k words; literature + theory) |
| **In-repo FINAL freeze** | [papers/06-synthesis/FINAL.md](papers/06-synthesis/FINAL.md) |
| **Conclusions spine** | [synthesis/PROGRAM_CONCLUSIONS.md](synthesis/PROGRAM_CONCLUSIONS.md) |
| Companions | m6d (R4a), m5b lemma, CLAIM_GATE |

Optional only: LaTeX/figures; **or** a new research cycle per [OPEN_AVENUES.md](synthesis/OPEN_AVENUES.md) (default priority: O1 continuum \(L_S\) density).

### 7.3 Deprioritize

Dual scorecards; continuum \(L\) fits; residual dual crisis; equating \(H_c^{\mathrm{toy}}\) with \(S_{\mathrm{GfE}}\) or \(S_c\).

### 7.4 Next session

**Primary:** read FINAL + PROGRAM_CONCLUSIONS.  
**New science:** follow [OPEN_AVENUES.md](synthesis/OPEN_AVENUES.md) (missing theorems for O1–O5; “new theory” ≠ wrong program).

---

## 8. Reproduction commands (dual witnesses)

```bash
# Claim hygiene
.venv/bin/python simulations/classical/check_claim_hygiene.py

# D13 relationship witnesses
.venv/bin/python simulations/classical/m11_composition_ledger.py
.venv/bin/python simulations/classical/m11_landauer_and_ledger.py
.venv/bin/python simulations/bridging/m5c_pm_energy_descent.py

# M11 microstructure (reference)
.venv/bin/python simulations/classical/_run_m11_phase2.py
.venv/bin/python simulations/classical/m11_coupled_regions_ledger.py
```

---

## 9. One-page summary for agents

```text
PROJECT: Computational entropy + emergent gravity + bridge to Bianconi GfE
STANCE:  Preliminary research only

SETTLED:
  - Euclidean ACD-EW dual (toys 6/6; PM vs heat expected; time-windowed residual)
  - U_star pure residual dual [1.36,2.40] under PCRH_b (rho_b=0.42)
  - Newton Path J/M (not Phi ∝ rho Laplacian)
  - M6: same Poisson WEAK PASS; not theory identity; next-order structural FAIL
  - L = demand / possibility-space flux, not identity stockpile

NOT SETTLED:
  - Continuum GfE ⇔ master equation
  - IDEM constructs continuum L or G
  - Full pure residual dual with zero soft hypotheses
  - Lorentzian lift, PPN, H_c^toy = S_c identity
  - Γ-convergence of warm-up lattice action

SETTLED (D13 add):
  - Load path-dependent (ΣL_S); L_B non-additive
  - L_S/export = Landauer erased bits (AND protocol)
  - Layer W: PM discrete energy descent (warm-up)

DEFAULT NEXT:
  Freeze closed — read FINAL.md + PROGRAM_CONCLUSIONS.md
  New cycle: synthesis/OPEN_AVENUES.md (O1–O5 missing theorems)

KEY PATHS:
  papers/06-synthesis/FINAL.md
  synthesis/PROGRAM_CONCLUSIONS.md
  synthesis/OPEN_AVENUES.md
  synthesis/CLAIM_GATE.md, CURRENT_CLAIMS.md
```

---

## 10. Report metadata

| Field | Value |
|-------|--------|
| Written | 2026-07-15 |
| Updated | 2026-07-15 (D15) |
| Covers decisions | D1–D15 |
| Dual program status | **Closed** |
| Paper | **FINAL v1.0** (`papers/06-synthesis/FINAL.md`) |
| Recommended posture | **Under-claim; freeze complete** |

### Changelog

| Date | Entry |
|------|--------|
| 2026-07-15 | D8–D14 dual freeze through first DRAFT + R1–R4a |
| 2026-07-15 | **D15:** PROGRAM_CONCLUSIONS; FINAL.md; M5b lemma polish; conclusion freeze |
| 2026-07-15 | **OPEN_AVENUES.md:** concluded vs new theory vs experiment; missing theorems for O1–O5 |

*Append further changelog only if a new cycle (D16+) reopens the program.*
