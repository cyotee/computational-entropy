# Current Claims (program-level freeze)

**Status:** Frozen 2026-07-15 · Preliminary research only  
**Purpose:** What we may assert vs must not assert  
**Authority:** [PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2 · dual [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) · Newton [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) · M6 [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) · ACD-EW [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md)

---

## 1. Stance

- All material is **preliminary research**. Constructions and evidence are real; **nothing has GR-level certainty**.
- Prefer **under-claiming**. Every bridge mapping is labeled **semantic / structural / constructive**.
- Type safety: load \(L\) is a **dimensionless scalar**; structure-induced \(G\) is a **metric** (or edgewise cousin). **\(L \neq G\)**.
- Three-stage model only: computational induction → geometric imprint → continuum GfE macro. Do **not** collapse stages into symbolic identity of master equation and GfE action.

---

## 2. Claims we may assert (with rigor label + pointer)

| # | Claim | Rigor | Pointer |
|---|--------|-------|---------|
| C1 | **ACD-EW exists:** constructive Euclidean dual between GfE **warm-up** (induced \(G[\phi]\), PM flow) and observation channel + split load + load clock | **constructive** (+ toys hybrid-experimental) | [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) |
| C2 | Joint toys **6/6 SUPPORT** (1D, 2D, blackjack-belief): dual **pattern** robust | **hybrid-experimental** | `simulations/bridging/`; blackjack = **pattern only** |
| C3 | PM > heat on edged structure is **expected** dual success, not a theory bug | **structural** | PROGRESS_REPORT §2.1–2.2 |
| C4 | Residual dual is **time-windowed (T1′)**, not all \(t\in(0,t_\star]\) | **analytic + hybrid-experimental** | [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) Claim A–C |
| C5 | Unified pure residual window \(U_\star=[1.36,2.40]\) under PCRH\(_b\) with \(\rho_b=0.42\) | **analytic** (majorant + identity) + **soft** PCRH\(_b\) (ensemble-certified) | [m1g-unified-pure-window.md](m1g-unified-pure-window.md) |
| C6 | Edge persistence: \(H^t\ge H_{\mathrm{floor}}=0.25>K\) on high-prob. event through \(T_{\mathrm{pers}}^\sharp\approx 1.67\) | **analytic** | Claim B / Lemma C′2♯ |
| C7 | Short-\(t\) heat win explained by noise race: \(\mathbb{E}(R_{\mathrm{heat}}-R_{\mathrm{PM}})=R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\); crossover \(\sim 1.2\) | **analytic identity** + **hybrid-experimental** | Claim C |
| C8 | Load-PM ≈ mild time change of PM (\(\tau/t\sim 0.95\text{–}0.98\)); residual dual vs heat on dual window | **hybrid-experimental** (time-change defn. constructive) | Claim D · [m2-t1-load.md](m2-t1-load.md) |
| C9 | Newton recovery = **Path J/M only** (Clausius → Einstein → Poisson; load-clock on-shell match) | Path J: **external theorem + assumption**; Path M: **calibration** | [newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) |
| C10 | \(\alpha\beta=4\pi G/c^4\) is **on-shell calibration**, not free derivation of \(G\) | **calibration** | Path M |
| C11 | M6: both frameworks → \(\nabla^2\Phi=4\pi G\rho_m\) via Einstein/GR at leading weak field | **WEAK PASS** (shared Poisson end) | [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) |
| C12 | M6: **not** framework equivalence; mechanisms and next-order structures diverge | **FAIL identity** | M6 §4 |
| C13 | Next-order: GfE extras in metric EOM (\(D_{\mu\nu},\Lambda_G\)); our \(\gamma_L,\delta_L\) live in load **clock** unless promoted — **structural FAIL** | **structural** | [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md) |
| C14 | Prefer reading \(L\) as demand from **scale/rate of channel outcomes** (energy + entropy flux + boundary); active scrambling → **higher** \(L\) | **semantic** (program convention) | PROGRESS_REPORT §2.1, §4 |

**Heat/PM residual dual program status:** settled enough to **stop as main open crisis**. Further pure-proof polishing is optional paper depth, not default work.

---

## 3. Explicit non-claims

Do **not** assert without new work (mirror PROGRESS_REPORT §2.3):

1. Master equation \(\Leftrightarrow\) Bianconi continuum GfE.  
2. \(L \equiv G\), \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\), \(\alpha_L\beta_L \equiv \alpha_B/\beta_B\).  
3. T1 residual domination for all \(t\in(0,t_\star]\) (false; use T1′ / \(U_\star\)).  
4. Pure T1′ with **no** soft hypotheses (PCRH\(_b\) still ensemble-certified).  
5. Newton from pointwise \(\Phi\propto\rho\) Laplacian (**withdrawn**).  
6. Next-order \(\gamma_L,\delta_L\) equal GfE \(D_{\mu\nu},\Lambda_G\).  
7. Lattice denoising = empirical gravity.  
8. External GfE papers established on par with GR.  
9. IDEM/decay fully constructs continuum \(L\) or \(G\) (open / deferred).

Also (dual write-up): no theorem-level multi-jump / 2D / continuum SPDE residual domination; toy \(H_c\) ≠ von Neumann \(S_c\) identity.

---

## 4. Newton recovery (Path J/M only)

Canonical: [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) · audit [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md)

| Path | Content | Rigor |
|------|---------|-------|
| **J** | Clausius on local horizons for \(\mathcal{L}_g\) → **Einstein** (Jacobson 1995, imported) → weak-field GR → \(\nabla^2\Phi=4\pi G\rho_m\) | **external theorem + modeling assumption** + standard GR |
| **M** | Load clock \(d\tau=dt/(1+\alpha L)\) matches Newtonian redshift **on shell** for calibrated family of solutions; repo convention \(\alpha\beta=4\pi G/c^4\) | **calibration** (conditional on Path J) |

**Withdrawn:** pointwise \(\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho\Rightarrow\) Poisson. Invalid; do not revive.

**Not claimed:** derivation of Newton independent of Jacobson/Einstein input; free derivation of \(G\) from load alone.

---

## 5. GfE contact (M6 WEAK PASS / FAIL)

| Criterion | Outcome |
|-----------|---------|
| Same leading Poisson \(\nabla^2\Phi=4\pi G\rho_m\) | **WEAK PASS** (both via Einstein/GR) |
| Same upper derivation mechanism | **FAIL** |
| Identifiable \((\alpha_L,\beta_L)=(\alpha_B,\beta_B)\) | **FAIL / refused** (M7) |
| Next-order corrections match | **structural FAIL** (M6b): GfE metric EOM extras vs load-clock \(\gamma_L,\delta_L\) |
| Continuum GfE \(\Leftrightarrow\) master equation | **FAIL** — do not claim |

**Interpretation:** Poisson agreement is **expected** if both embed Einstein at low demand — circumstantial co-class with GR, **not** evidence that load dynamics = Bianconi relative-entropy EL equations. Interesting dual remains **ACD-EW Euclidean warm-up** (different mathematical layer).

---

## 6. Dual residual (T1′ / \(U_\star\)) — summary of A–D

Source: [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) · [m1g-unified-pure-window.md](m1g-unified-pure-window.md)

| Claim | Statement | Rigor |
|-------|-----------|-------|
| **A** | \(\mathbb{E}\,R_{\mathrm{PM}}(t)\le\mathbb{E}\,R_{\mathrm{heat}}(t)\) on unified pure window \(U_\star=[1.36,2.40]\) (grid times in \(U_\star\)); \(\rho_b=0.42\); PCRH\(_b\) soft | pure majorant + **soft** ensemble majorant |
| **B** | Edge height persistence on high-prob. event (\(H^0\ge 0.80\) w.p. \(\gtrsim 0.87\)) → \(H^t\ge 0.25>K\) for \(t\le T_{\mathrm{pers}}^\sharp\approx 1.67\) | **analytic** |
| **C** | Ultra-short \(t\lesssim 1.2\): heat can win residual (noise race); not dual failure; exact identity \(R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\) | **explained** |
| **D** | Load-PM: \(\tau(t)=\int_0^t(1+\alpha_L L_{\mathrm{clock}})^{-1}ds\le t\); residual dual vs heat on window | **hybrid / experimental** |

**Soft spot (do not hide):** PCRH\(_b\) is large-MC-certified for the toy class; full pathwise Dirichlet-form proof without certificate remains open.

**Citation sentence (paste-ready):**  
*In a 1D lattice observation model with a single noisy jump, PM residual domination over isotropic heat holds on an intermediate window \(U_\star=[1.36,2.40]\) (T1′; PCRH\(_b\), \(\rho_b=0.42\)), with analytic edge persistence and noise-versus-blur accounting; load reparameterization preserves the dual experimentally as a slower clock. This supports constructive Euclidean ACD-EW, not continuum gravitational equivalence.*

---

## 7. Active next track

**Default:** freeze dual claims; **do not** restart heat/PM residual dual as main crisis.

| Priority | Track | Notes |
|----------|-------|--------|
| 1 | **FINAL frozen** | [FINAL.md](../papers/06-synthesis/FINAL.md) · [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md) |
| 2 | **New cycle (if any)** | [OPEN_AVENUES.md](OPEN_AVENUES.md) — O1–O5; “new theory” = missing math |
| 3 | **Relationships (done)** | [m11d](m11d-composition-laws.md) · [m11e](m11e-landauer-export.md) · [m5c](m5c-warmup-pm-gradient-flow.md) |
| — | **Deprioritize** | Dual scorecards; continuum \(L\) fit; residual crisis |

Full avenue list: [PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §7.

---

## 8. Key paths

| Role | Path |
|------|------|
| Bootstrap / settled tables | [PROGRESS_REPORT.md](../PROGRESS_REPORT.md) |
| This freeze sheet | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) |
| Dual claims A–D | [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) |
| \(U_\star\), \(\rho_b=0.42\), PCRH\(_b\) | [m1g-unified-pure-window.md](m1g-unified-pure-window.md) |
| ACD-EW formal dual | [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) |
| Transfer limits | [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) |
| Path J/M Newton | [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) |
| M6 WEAK PASS / FAIL | [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) |
| M6b next-order structural FAIL | [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md) |
| Canonical \(H_c\)/\(S_c\) | [foundations/computational-entropy/definition.md](../foundations/computational-entropy/definition.md) |
| Canonical \(\Phi_g\), \(L\), master eq | [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) |
| Math board M1–M12 | [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md) · [PACK_INDEX.md](PACK_INDEX.md) |
| M11 design + Phase 1–2 | [m11-idem-to-load.md](m11-idem-to-load.md) · `simulations/classical/` |
| Paper outline | [../papers/06-synthesis/OUTLINE.md](../papers/06-synthesis/OUTLINE.md) |
| M10 / M5 hygiene | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) · [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) |
| Dual witnesses | `simulations/bridging/test_t1_unified_pure.py`, `_joint_toy_v2_core.py` |

---

*Update this file when settled claims, \(U_\star\), M6/M11 status, or non-claims change. Do not expand into full proofs — link sources.*
