# Synthesis Pack Index (ACD-EW / GfE bridge)

**Status:** Living index (2026-07-14; dual freeze + M11 Phase 1–2 + D11: 2026-07-15)  
**Purpose:** One place to open the parallel synthesis pack and see what each file settles, what it refuses, and what to read next.  
**New context bootstrap:** **[../PROGRESS_REPORT.md](../PROGRESS_REPORT.md)** — settled claims, non-claims, file map, recommended next avenues.  
**Claims freeze sheet:** **[CURRENT_CLAIMS.md](CURRENT_CLAIMS.md)**  
**Paper outline:** **[../papers/06-synthesis/OUTLINE.md](../papers/06-synthesis/OUTLINE.md)**  
**Stance:** All of this is **preliminary research**. External GfE literature and our dual are supporting constructions — **not** established physics on the order of general relativity. Prefer under-claiming.  
**Dual residual program:** Settled at research-program level (\(U_\star\)); optional paper hardening only.  
**Classical track:** **[m11-idem-to-load.md](m11-idem-to-load.md)** + Phase 1–2 ledgers under `simulations/classical/`.

---

## 1. Pack map

```text
                    ┌─────────────────────────────────────┐
                    │  ACD-EW formal dual (1D/2D/game toys) │
                    │  action-channel-duality-euclidean.md  │
                    └──────────────────┬──────────────────┘
                                       │
          ┌────────────────────────────┼────────────────────────────┐
          ▼                            ▼                            ▼
 acd-ew-continuum-transfer.md   t1-residual-domination.md   weak-field-gfe-vs-load.md
 (dictionary + transfer)        (analytic T1 program)       (continuum Newton/EH gap)
          │                            │                            │
          └────────────────────────────┼────────────────────────────┘
                                       ▼
                         OPEN_MATH_DECISION_LOG.md
                         (what to do next, serially)
```

| File | Role | Settles | Does **not** settle |
|------|------|---------|---------------------|
| [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) | Formal **ACD-EW** dual | Constructive Euclidean dual; scorecards | Full GfE \(\Leftrightarrow\) master equation |
| [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) | Transfer / non-transfer dictionary | Claim hygiene | Continuum derivation |
| [weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md) | Pre-M6/M8 comparison sketch | Semantic/structural candidates | Plug-test (see M6) |
| [t1-residual-domination.md](t1-residual-domination.md) | T1 proposition + lemma board | Proof program | Full theorem |
| [m1-lemma-c-prime.md](m1-lemma-c-prime.md) | **M1** C′ + T1′ window + MC | Short-\(t\) obstruction; C′; T1′ envelope | Full T1′ theorem |
| [m1b-t1-prime-c2-bound.md](m1b-t1-prime-c2-bound.md) | **M1b** analytic C′2 + T1′ limits | Crude \(T_{\mathrm{pers}}\); pinned MC window | — |
| [m1c-c2-sharp-delta-noise.md](m1c-c2-sharp-delta-noise.md) | **M1c** C′2♯ + \(\Delta_{\mathrm{noise}}\) | Analytic \(t_{\max}\ge t_{\min}\); blur/noise split | — |
| [m1d-lemma-e-prime.md](m1d-lemma-e-prime.md) | **M1d** Lemma E′ residual comparison | Hybrid T1′ on \(I_\star\); E′a/b/d closed | — |
| [m1e-freeze-tax-spectral.md](m1e-freeze-tax-spectral.md) | **M1e** spectral freeze-tax majorant | Majorant under Hρ / \(\rho_{\mathrm{typ}}\) | — |
| [m1f-hrho-pure-proof.md](m1f-hrho-pure-proof.md) | **M1f** pure Hρ (\(\rho_{\mathrm{eff}}\approx 0.30\)) | Pure dual on \([2.0,2.4]\) | — |
| [m1g-unified-pure-window.md](m1g-unified-pure-window.md) | **M1g** unified pure window | **\(U_\star=[1.36,2.40]\)** with \(\rho_b=0.42\) | Pathwise PCRH\(_b\) without MC |
| [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) | **Paper-ready** hybrid dual write-up | Paste-ready claims A–D | Continuum equivalence |
| [m2-t1-load.md](m2-t1-load.md) | **M2** T1-load | Hybrid load vs heat on \(I_\star\) | Pure time-change bridge |
| [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) | **M5** warm-up continuum bridge (T4) | Citation/consistency sketch | Γ-convergence theorem |
| [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) | **M5** continuum warm-up hygiene | Lit vs open; abstract checklist; transfer | — |
| [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) | **M10** \(S_c\) vs toy/classical \(H_c\) | Object map + collision table | \(H_c^{\mathrm{toy}}\equiv S_c\) identity |
| [m10-p1-object-comparison.md](m10-p1-object-comparison.md) | **M10 P1** \(H_c^{\mathrm{toy}}\) vs \(H(Z)\) | Hybrid MC non-identity on \(U_\star\) | Not \(S_c\); not co-motion theorem |
| [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md) | **M8** Newton audit | Gap N1; Path J/M | — |
| [../emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) | **N1 rewrite** Path J/M recovery | Canonical Newton recovery | First-principles \(G\) |
| [m7-symbol-map.md](m7-symbol-map.md) | **M7** symbol map | Candidates + non-maps | Numerical \(\alpha_L=\alpha_B\) |
| [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) | **M6** plug-test | **WEAK PASS** Poisson; FAIL identity | Framework equivalence |
| [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md) | **M6b** next-order GfE vs \(\gamma_L,\delta_L\) | Structural mismatch (EOM vs clock) | PPN coefficients |
| [m6c-bianconi-linearization.md](m6c-bianconi-linearization.md) | **M6c** Bianconi linearization W1 | PDF Eqs. 60–68; Poisson PASS; \(\Lambda_G=O(\epsilon^2)\) | Full PPN numbers |
| [m2-m4-followups.md](m2-m4-followups.md) | **M2–M4** after M1 | Explicit deferral | Proofs of M2–M4 |
| [bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md) | Original Bianconi bridge | Lineage | Constructive dual |
| [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) | **Program-level claims freeze** | Settled C1–C14 + non-claims | Continuum equivalence |
| [m11-idem-to-load.md](m11-idem-to-load.md) | **M11** IDEM/decay → \(H_c\), \(L^{\mathrm{disc}}\) | Design + Phase 1–2 ledgers | Continuum \(L\) or \(G\) from IDEM |
| [m11c-continuum-motivation.md](m11c-continuum-motivation.md) | **M11c** three-slot continuum *motivation* | Roles not equalities; flux reading | Continuum derivation |
| [m11d-composition-laws.md](m11d-composition-laws.md) | **R1** composition / path dependence | \(\sum L_S\) path-dep; \(L_B\) non-additive | Continuum composition |
| [m11e-landauer-export.md](m11e-landauer-export.md) | **R2** Landauer ↔ export/\(L_S\) | \(Q\ge kT\ln2\cdot H(X\mid Y)\) | Gravity / \(G\) |
| [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) | **R3a** warm-up ↔ PM GD | Discrete \(E_h\) descent; Layer W | Lorentzian GfE / ME |
| [CLAIM_GATE.md](CLAIM_GATE.md) | Pre-draft claim checklist | Failure-mode gates G1–G10 | — |
| [NONCLAIMS_FIXTURE.md](NONCLAIMS_FIXTURE.md) | Canonical N1–N9 | Frozen non-claims | — |
| [m10-p1-object-comparison.md](m10-p1-object-comparison.md) | **M10 P1** \(H_c^{\mathrm{toy}}\) vs \(H(Z)\) | Empirical non-identity | \(S_c\) identity |
| [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md) | **M5b** smooth action \(O(h)\) | Sketch lemma | Γ-convergence |
| [../papers/06-synthesis/OUTLINE.md](../papers/06-synthesis/OUTLINE.md) | **Paper outline** | Drafting map; claim→section | — |
| [../papers/06-synthesis/FINAL.md](../papers/06-synthesis/FINAL.md) | **FINAL program report v1.0** (~14k words) | Claim-freeze conclusions package | GR-level physics |
| [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md) | **P1–P11 · W1–W6 · O1–O5** | Frozen spine | — |
| [OPEN_AVENUES.md](OPEN_AVENUES.md) | **Post-freeze roadmap** | New theory vs experiment; missing theorems O1–O5 | — |
| [m6d-promotion-nogo.md](m6d-promotion-nogo.md) | **R4a** next-order promotion no-go | Structural impossibility without promotion | PPN numbers |
| [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) | Decisions M1–M12 | D1–D12 outcomes | — |

---

## 2. Experiment pack (joint toys)

| Path | What it is | Latest scorecard |
|------|------------|------------------|
| `simulations/bridging/_joint_toy_v2_core.py` | 1D observation channel dual | **6/6 SUPPORT** |
| `simulations/bridging/gfe_load_joint_toy.ipynb` | 1D notebook | same core |
| `simulations/bridging/_joint_toy_2d.py` | 2D image dual (Catte PM) | **6/6 SUPPORT** |
| `simulations/bridging/blackjack_belief_dual.py` | Game-motivated belief / count \(\phi\) | **6/6 SUPPORT** (pattern only) |
| `simulations/bridging/DESIGN_*.md` | Designs + honesty limits | — |
| `simulations/classical/m11_and_gate_ledger.py` | **M11 Phase 1** AND-gate \(H_c\) + \(L^{\mathrm{disc}}\) | Exact chain rule; not gravity |
| `simulations/classical/m11_multistep_boolean_ledger.py` | **M11 Phase 2** multi-step Boolean | AND high export; OR lower |
| `simulations/classical/m11_tiny_lambda_ledger.py` | **M11 Phase 2** tiny SKI ensemble | \(H_c\) drop under redex steps |
| `simulations/classical/m11_minimal_shoe_ledger.py` | **M11 Phase 2 / M12-adj** R/B shoe | Predictive \(H_c\); not EV |
| `simulations/classical/_run_m11_phase2.py` | Run all Phase 2 ledgers | exit 0 verified |
| `simulations/classical/m11_coupled_regions_ledger.py` | **M11.3** two regions + XOR screen | Conservation + locked \(L_S\) |
| `simulations/classical/check_claim_hygiene.py` | Claim hygiene checker | N1–N9 + banners |
| `simulations/bridging/m10_p1_entropy_objects.py` | **M10 P1** object comparison | \(H_c^{\mathrm{toy}}\neq H(Z)\) |
| `simulations/classical/m11_composition_ledger.py` | **R1** composition / path-dep | \(\sum L_S\) gap \(1\) bit |
| `simulations/classical/m11_landauer_and_ledger.py` | **R2** Landauer AND | export \(=Q_{\min}/(kT\ln2)\) |
| `simulations/bridging/m5c_pm_energy_descent.py` | **R3a** PM energy descent | \(E_h\) non-increasing |

**Interpretation:** Repeated PROMISING scorecards mean the **Euclidean dual pattern is robust across ICs**, not that gravity is confirmed.

---

## 3. External literature (supporting, preliminary)

| Paper | Local | Use in pack |
|-------|-------|-------------|
| Bianconi, *Gravity from entropy* (PRD 2025) | `papers/external/Bianconi_Gravity_from_entropy_*` | Continuum GfE action, \(G\), G-field, \(\Lambda_G\) |
| Bianconi, *Beyond holography* (arXiv:2503.14048) | `papers/external/Bianconi_Beyond_holography_*` | PM = GfE warm-up gradient flow |
| Thattarampilly–Zheng inflation / BHs | `papers/external/Thattarampilly_*` | Continuum recovery *targets* only |
| Kumar, semiclassical Einstein via \(S_{\mathrm{gen}}\) | `papers/external/Kumar_*` | Nonequilibrium Clausius lineage |

Treat as **peers in a research program**, not as settled foundations.

---

## 4. Suggested reading paths

| Goal | Order |
|------|--------|
| **Claims hygiene** (what we may say) | This index → [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) → ACD-EW formal dual |
| **Analytic dual** | ACD-EW §10 → [t1-residual-domination.md](t1-residual-domination.md) → OPEN_MATH log |
| **Continuum gravity gap** | [weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md) → newtonian recovery Path J/M → M6/M6b → OPEN_MATH log |
| **Analytic T1′ depth** | [t1-residual-domination.md](t1-residual-domination.md) → [m1](m1-lemma-c-prime.md) → [m1b](m1b-t1-prime-c2-bound.md) |
| **Classical thread touch** | [m11-idem-to-load.md](m11-idem-to-load.md) → AND ledger → DESIGN_blackjack_belief_dual (pattern only) |
| **Claims freeze** | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) → PROGRESS_REPORT §2 |
| **Paper drafting** | [OUTLINE.md](../papers/06-synthesis/OUTLINE.md) → CURRENT_CLAIMS → section source files |
| **New agent bootstrap** | [PRD.md](../PRD.md) → [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) → this index |

---

## 5. One-sentence pack summary

We have a **constructive Euclidean dual** (toys + ACD-EW) between GfE warm-up geometry/flow and channel/load bookkeeping; we have **dictionaries and open proof programs** toward continuum contact; we have **not** established full GfE gravity as equivalent to our master equation, nor upgraded any of this to the epistemic status of relativity.

---

*Update this index when new synthesis notes or scorecards land. Decisions on open math live in [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md).*
