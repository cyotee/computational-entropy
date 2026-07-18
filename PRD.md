# PRD.md — Computational Entropy & Emergent Gravity

**Status:** Living product/research definition (written 2026-07-14; **Euclidean dual freeze 2026-07-15+**)  
**Purpose:** Reliable context bootstrap for a new agent or session. Read this first, then follow links for depth.  
**Audience:** Agents and collaborators continuing theory, papers, or the joint toy simulation.  
**Progress snapshot:** **[PROGRESS_REPORT.md](PROGRESS_REPORT.md)** — full settled/open board + recommended next avenues (prefer for new contexts).  
**Claims freeze:** [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · **M11 track:** [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md)

---

## 1. One-sentence mission

Define **computational entropy** as the entropy of a map/channel’s **output distribution**, develop a **gravitational quantum channel** \(\Phi_g\) with **computational load** \(L\) that recovers known gravity phenomenology, and **bridge** that framework to continuum **Gravity-from-Entropy (GfE)** theories (Bianconi et al.) via an explicit staged workflow—not by forcing premature symbolic identity.

---

## 2. What we are working on (current focus)

### 2.1 Primary research program (always true)

| Thread | Content | Canonical entry points |
|--------|---------|------------------------|
| **Classical / lambda** | IDEM functions, decay vectors, \(d_f\), combinatorics, games (Blackjack, etc.) as entropy-reducing computations | `computational-models/`, `research/`, root IDEM markdowns |
| **Emergent gravity** | Channel \(\Phi_g\), \(S_c = S(\Phi_g(\rho))\), load \(L\), master equation, recoveries (Newton, BH, cosmology, Lloyd, …) | `foundations/computational-entropy/definition.md`, `emergent-gravity/master-equation.md`, `quantum/*.tex` |
| **Bridge / synthesis** | Explicit mappings between threads; external GfE literature; discrete joint toys | `THEORY.md`, `synthesis/`, `simulations/bridging/` |

**Central gap (from PLAN.md / THEORY.md):** Gravity work uses high-level \(H_c\)/\(S_c\) but not yet lambda/IDEM machinery. Goal is cohesion at semantic → structural → constructive levels.

### 2.2 Active integration track (2026-07-15+)

Integrate **Bianconi Gravity from Entropy (GfE)** and follow-on papers as a **continuum Stage-3 target**, with our \(\Phi_g / S_c / L\) as **Stage-1 operational induction**, without claiming full equivalence until maps are constructive.

**Euclidean dual (ACD-EW) — program-level settled (freeze 2026-07-15+):**  
The heat/PM residual dual, joint toys (1D / 2D / blackjack-belief **pattern**), and time-windowed residual story (T1′ / \(U_\star\)) are **settled enough at research-program level**. Do **not** default-chase more dual scorecards or residual majorants unless writing a paper-quality pure theorem. Paste-ready claims: [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · [synthesis/t1-prime-hybrid-writeup.md](synthesis/t1-prime-hybrid-writeup.md). Formal dual: [synthesis/action-channel-duality-euclidean.md](synthesis/action-channel-duality-euclidean.md).

**Primary tracks now (not more dual scorecards):**

| Priority | Track | Entry |
|----------|--------|--------|
| **1** | **M11 IDEM → load** — connect classical decay / recoverability to \(L\) or \(H_c\) (attacks central gap) | [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) |
| **2** | **Continuum hygiene (M5 / M10)** — warm-up continuum bridge; toy \(H_c\) vs von Neumann \(S_c\) | [synthesis/m5-warmup-continuum-t4.md](synthesis/m5-warmup-continuum-t4.md), OPEN_MATH |
| **3** | **Paper outline / claim freeze** — foundations → channel → master eq → ACD-EW → Path J/M → M6 | [PLAN.md](PLAN.md), [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) |

See [PROGRESS_REPORT.md](PROGRESS_REPORT.md) §7. All preliminary — not GR-level certainty.

**Workflow model under test:**

```text
STAGE 1 — Computational induction (OUR framework)
  ρ, Φ_g, S_c (or H_c), load L, dτ = dt/(1+αL)
  IDEM / decay vectors / games as discrete microstructure
        │
        ▼  (define / induce geometric imprint)
STAGE 2 — Geometric encoding (BRIDGE)
  Matter/geometry-induced metric G
  (or computational cousin G_c[ρ,g,Φ_g])
        │
        ▼  (relative entropy action)
STAGE 3 — Entropic gravity law (GfE MACRO)
  Action ~ Tr g ln G^{-1} → modified Einstein, Λ_G, G-field
  Recoveries: inflation, spherical BHs, etc.
```

**Key clarification (type safety):**

- Load \(L\) is a **dimensionless scalar** (demand / clock rate).
- Bianconi’s \(G\) is a **metric operator**.
- Therefore **\(L \neq G\)**. Honest slogan:  
  **\(L\) and \(S_c\) describe the process that induces structure; \(G\) is the geometric imprint; GfE is the continuum law of the pair \((g,G)\).**

### 2.3 Settled dual layer + engineering artifacts (reference, not active chase)

**Joint toy v2** (Euclidean warm-up; **pattern saturated** — re-run for regression only, not as default science work):

| Path | Role |
|------|------|
| `simulations/bridging/gfe_load_joint_toy.ipynb` | Runnable experiment (v2) |
| `simulations/bridging/_joint_toy_v2_core.py` | Shared core + CLI |
| `simulations/bridging/DESIGN_gfe_load_joint_toy.md` | Design + interpretation |
| `simulations/bridging/gfe_load_joint_toy_scorecard_v2.txt` | Latest scorecard text |
| `synthesis/bridge-bianconi-relative-entropy.md` | Living bridge note |
| `papers/external/` | GfE + related PDFs |

**Scorecard (2026-07-14, deterministic seeds): 6/6 SUPPORT → PROMISING** (1D; also 2D + blackjack-belief pattern).  
**Related synthesis:**
- **[synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md)** — frozen settled / non-claims sheet  
- **[synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md)** — primary M11 design track  
- **[synthesis/PACK_INDEX.md](synthesis/PACK_INDEX.md)** — pack map + reading paths  
- **[synthesis/OPEN_MATH_DECISION_LOG.md](synthesis/OPEN_MATH_DECISION_LOG.md)** — M1–M12 board; residual dual **program-level settled** (do not default-chase)  
- [synthesis/acd-ew-continuum-transfer.md](synthesis/acd-ew-continuum-transfer.md) — transfer / non-transfer dictionary  
- [synthesis/m1g-unified-pure-window.md](synthesis/m1g-unified-pure-window.md) · [m5-warmup-continuum-t4.md](synthesis/m5-warmup-continuum-t4.md) · [m8-newton-recovery-audit.md](synthesis/m8-newton-recovery-audit.md) · [m7-symbol-map.md](synthesis/m7-symbol-map.md) · [m6-weak-field-plugtest.md](synthesis/m6-weak-field-plugtest.md) · [m2-m4-followups.md](synthesis/m2-m4-followups.md)  
- [simulations/bridging/blackjack_belief_dual.py](simulations/bridging/blackjack_belief_dual.py) — game-motivated IC (6/6 dual pattern only)  

**Honesty lock:** M6 = WEAK PASS shared Newtonian Poisson via Einstein/GR; **not** GfE ⇔ master equation. Residual dual = **time-windowed (T1′)** with \(U_\star=[1.36,2.40]\) under soft PCRH\(_b\) — **not** domination for all \(t\). Do not claim continuum equivalence or GR-level certainty.

---

## 3. Core definitions (do not reinvent)

### 3.1 Computational entropy

Canonical: `foundations/computational-entropy/definition.md`

- Classical: \(H_c(f;p_X) = H(Y)\) or differential \(h(Y)\) of **output** distribution only.
- Quantum: \(S_c(\Phi;\rho_X) = S(\Phi(\rho_X))\) (von Neumann).
- **Key property:** maps with the same output entropy are **informationally equivalent** (e.g. \(\sqrt{U}\) vs \(\max(U_1,U_2)\)).
- Global conservation + local transfer (AND-gate example).

### 3.2 Master equation and load

Canonical: `emergent-gravity/master-equation.md`

\[
L(\rho,g) = \beta\frac{E[\rho]}{V\epsilon_0} + \gamma\left|\frac{dS_c}{d\tau}\right|_{\rm reg} + \delta\frac{S_{\rm boundary}}{S_{\rm BH}(A)}
\]

\[
\frac{d\rho}{dt} = \frac{1}{1+\alpha L}\,\mathcal{L}_g[\rho; g_{\mu\nu}(\rho)],
\qquad
d\tau = \frac{dt}{1+\alpha L}
\]

Newtonian matching: \(\alpha\beta = 4\pi G/c^4\).  
\(\mathcal{L}_g\) obeys Clausius \(\delta Q = T\,dS_c\) on local horizons.

### 3.3 External: Gravity from Entropy (GfE)

Primary: Bianconi, *Gravity from entropy*, Phys. Rev. D **111**, 066001 (2025); arXiv:2408.14391  
PDF: `papers/external/Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf`

- Metric as local quantum operator; action = quantum relative entropy between spacetime metric \(g\) and matter/geometry-induced metric \(G\).
- G-field → dressed Einstein–Hilbert + emergent \(\Lambda_G \ge 0\); low coupling → GR.
- Warm-up: \(\mathcal{L} = -\ln(1+\alpha|\nabla\phi|^2)\); gradient flow dual to Perona–Malik (*Beyond holography*, arXiv:2503.14048).

**Other external papers in `papers/external/`:**

| File | Role |
|------|------|
| `Bianconi_Beyond_holography_arXiv_2503.14048.pdf` | PM = GfE gradient flow; template for discrete toy |
| `Thattarampilly_Zheng_Inflation_from_entropy_arXiv_2509.23987.pdf` | GfE vacuum inflation, phantom branch, CMB window |
| `Thattarampilly_Zheng_Spherically_symmetric_BH_arXiv_2602.13694.pdf` | Schwarzschild + \(r^{-4}\) corrections; Hawking-like \(\dot M\); entropic leakage |
| `Kumar_Recovering_semiclassical_Einstein_arXiv_2404.16912.pdf` | \(S_{\rm gen}\) + nonequilibrium route to semiclassical Einstein (supports Clausius layer) |

Bibliography entry in main tex: `\bibitem{Bianconi2025}` in `quantum/Computational_Entropy_and_Emergent_Gravity.tex`.

---

## 4. Repository map (navigation)

```
PRD.md, PLAN.md, THEORY.md, GLOSSARY.md, README.md
foundations/computational-entropy/definition.md   ← H_c / S_c canonical
emergent-gravity/master-equation.md               ← Φ_g, L, master eq canonical
synthesis/bridge-bianconi-relative-entropy.md     ← GfE ↔ us bridge
papers/                                           ← our series skeleton + external/
  external/README.md
simulations/bridging/                             ← joint toy
quantum/                                          ← legacy gravity writeups + main .tex
computational-models/, research/, drafts/, archive/
notebooks/                                        ← older game entropy notebooks
```

**Living docs priority for agents:** `PRD.md` (this) → `THEORY.md` → `PLAN.md` → canonical foundations/master-equation → bridge note → joint toy design.

**Do not** treat root `README.md` definition block as sole source if it is marked historical; prefer `foundations/`.

---

## 5. Joint toy — what it is (v2)

### 5.1 Setup (1D Euclidean warm-up, P0–P2)

- Lattice of \(N\) sites; **hidden** \(\phi_\star\); **observation** \(y=\phi_\star+\eta\); reconstructor \(\hat\phi(t)\) starts at \(y\).
- **Induced metric:** \(G = 1 + \alpha_G(\nabla\hat\phi)^2\); **GfE action** \(S_{\mathrm{GfE}}=-\sum\ln G\).
- **P0 dynamics:** classical PM \(\rho=1/(1+(\nabla\phi/K)^2)\) with \(K\sim\) noise scale (not large-\(\alpha\) staircasing).
- **Dynamics compared:** heat (control) · PM/GfE · load-gated PM with \(dt/(1+\alpha_L(L_E+L_S))\).
- **P1 channel \(H_c\):** residual log-energy vs \(\phi_\star\) + edge-location posterior entropy (not histogram of \(\hat\phi\)).
- **P2 load split:** \(L_E\) (induction), \(L_S\) (entropy rate), \(L_B\) (edge saturation); clock uses \(L_E+L_S\).

ICs: `noisy_step`, `noisy_two_bumps`, `noisy_ramp`, `clean_step` (fixed seeds 101–104).

### 5.2 Scorecard v2 criteria

1. PM residual better than heat (step impro>0.05; bumps impro>0)  
2. PM edge retention > heat×1.15 on step ICs  
3. Ramp stability (PM max-grad ratio < 2.5)  
4. \(\mathrm{corr}(L_E,\mathbb{E}[G-1])>0.85\) on all PM runs  
5. Load-gating slows mid-run \(L_2\) change vs pure PM  
6. Residual co-motion on `noisy_step` (PM better final + monotone ≥ heat)

**Latest automated result (2026-07-14): 6/6 SUPPORT → PROMISING.**

### 5.3 How to interpret results

| Finding | Status | Meaning |
|---------|--------|---------|
| PM residual ≪ heat on `noisy_step` | **Supported** | Observation channel improves under GfE/PM vs heat |
| Edges retained under PM; ramps not staircased | **Supported** | P0 success; structure-preserving denoising |
| \(L_E\) tracks \(\mathbb{E}[G-1]\) | **Supported** | Load intensity = induction intensity of \(G\) |
| Load-gating slows evolution | **Supported** | Stage-1 clock / time-dilation analogue |
| Full continuum duality / Bianconi Lorentzian action derived | **Not claimed** | Toy is Euclidean warm-up only |
| Action–Channel Duality (ACD-EW) + residual dual | **Program-level settled** | Writeup + 2D + T1′ / \(U_\star\); optional pure PCRH\(_b\) only for paper depth |

**Run (regression / witnesses only):** `.venv/bin/python simulations/bridging/_joint_toy_v2_core.py`  
**Notebook kernel:** Python (computational-entropy) / `.venv`.

---

## 6. Experimentation roadmap (after v2 PROMISING)

| Priority | Work | Status |
|----------|------|--------|
| **P0** Soft PM / \(K\)-scale | Done | Ramp stable |
| **P1** Observation-channel \(H_c\) | Done | Residual dual works on step |
| **P2** Split load + clock | Done | \(L_E\) + load-gating support |
| **P3** Scorecard v2 | Done | 6/6 SUPPORT |
| **Next A** | Write `synthesis/action-channel-duality-euclidean.md` | **Done** |
| **Next B** | 2D lift; residual dual (T1′ / \(U_\star\)) | **2D done (6/6)**; residual dual **program closed** (optional paper pure theorem only) |
| **Next C** | Optional game belief field as \(\phi\) | Pattern toy done (`blackjack_belief_dual.py`); true game \(H_c\) = M12 deferred |
| **Primary now** | **M11 IDEM→load**; continuum hygiene (M5/M10); claim freeze / paper outline | Active — see §2.2 |
| **Not yet** | Continuum limit to full GfE / master equation equivalence | Open research; non-claim |

**Do not:** over-claim full gravity equivalence; churn parameters only to keep 6/6; default-chase heat/PM residual dual.

---

## 7. What is already done (session state as of 2026-07-15 dual freeze)

- [x] Repo familiarization; canonical defs and PLAN/THEORY structure understood  
- [x] Bianconi GfE PDF + notes under `papers/external/`  
- [x] Additional papers: Beyond holography; Inflation from entropy; Spherical BHs; Kumar semiclassical Einstein  
- [x] `THEORY.md` §3.3 correspondence table + open questions  
- [x] Bridge note `synthesis/bridge-bianconi-relative-entropy.md`  
- [x] Bibitem + short unification subsection in main `.tex` (`Bianconi2025`)  
- [x] Joint toy notebook + DESIGN  
- [x] `ipykernel` / kernel `Python (computational-entropy)` registered for Jupyter  
- [x] P0–P2 toy refinements → scorecard **6/6 SUPPORT (PROMISING)**  
- [x] Formal Action–Channel Duality writeup (Euclidean warm-up): `synthesis/action-channel-duality-euclidean.md`  
- [x] 2D joint toy lift (`_joint_toy_2d.py`, 6/6 SUPPORT)  
- [x] Dual residual program: T1′ time-windowed; unified pure \(U_\star\); M1–M2 hybrid — **program-level closed** (optional PCRH\(_b\) harden for paper only)  
- [x] Dual writeup paste path: `synthesis/t1-prime-hybrid-writeup.md`  
- [x] **M11** design + Phase 1–2 ledgers ([synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md), `simulations/classical/`)  
- [x] Claims freeze sheet ([synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md))  
- [x] Continuum hygiene dictionaries (M5/M10)  
- [x] Paper outline ([papers/06-synthesis/OUTLINE.md](papers/06-synthesis/OUTLINE.md))  
- [x] CLAIM_GATE + non-claims fixture + hygiene checker  
- [x] M11c continuum motivation + coupled-regions ledger  
- [x] M10 P1 \(H_c^{\mathrm{toy}}\neq H(Z)\); M5b smooth action sketch  
- [x] **R1** composition laws + path-dependent \(\sum L_S\) ([m11d](synthesis/m11d-composition-laws.md))  
- [x] **R2** Landauer ↔ export ([m11e](synthesis/m11e-landauer-export.md))  
- [x] **R3a** warm-up/PM energy descent ([m5c](synthesis/m5c-warmup-pm-gradient-flow.md))  
- [x] **FINAL program report v1.0** ([papers/06-synthesis/FINAL.md](papers/06-synthesis/FINAL.md))  
- [x] **PROGRAM_CONCLUSIONS** P1–P11 ([synthesis/PROGRAM_CONCLUSIONS.md](synthesis/PROGRAM_CONCLUSIONS.md))  
- [x] **R4a** promotion no-go ([m6d](synthesis/m6d-promotion-nogo.md))  
- [x] **M5b** lemma polish  
- [ ] Optional LaTeX / figures (editorial)  
- [ ] Optional new science cycle (O1–O5)
- [ ] Paper outline (foundations → models → channel → master eq → ACD-EW → Path J/M → M6)  
- [ ] Bulk migration of legacy files into new tree (skeleton exists; content still largely legacy paths)

---

## 8. Agent instructions (how to continue safely)

1. **Read order:** [PROGRESS_REPORT.md](PROGRESS_REPORT.md) → this PRD → `THEORY.md` → relevant canonical file → only then edit.  
2. **Single source of truth:** do not re-copy master equation / \(H_c\) definition into new files; link to `foundations/` and `emergent-gravity/`.  
3. **Rigor honesty:** mark mappings as semantic / structural / constructive; never claim derivation of Bianconi’s action from \(L\) (or vice versa) without a map.  
4. **Notation:** \(H_c\) classical, \(S_c\) quantum/gravity; \(L\) load scalar; \(G\) induced metric (GfE) — **\(L \neq G\)**.  
5. **Kernel for notebooks:** prefer project `.venv` / kernel name **Python (computational-entropy)**.  
6. **Risky git/shared actions:** confirm with user before force-push, mass delete of archive content, etc.  
7. **Dual layer:** treat ACD-EW / residual dual as **settled**; re-run toys for regression only. Default new science = **M11 / continuum hygiene / paper**, not more residual dual.  
8. **If refining the toy (rare):** re-run scorecard; update this PRD §5.2–5.3 and DESIGN file with new numbers — do not churn params only to keep 6/6.

---

## 9. Open questions (theory)

From `THEORY.md` / PLAN, still open (dual toys **saturated** — central gap remains **IDEM ↔ gravity**):

- Representation of \(\rho\) via lambda terms: constructive or motivational only? (**M11** touches this)  
- Are the three terms in \(L\) derived or motivated from computational models? (**M11** primary)  
- Can Bianconi relative entropy of metrics emerge as continuum limit of computational relative entropy between “realized geometry” and matter-channel output patterns? (M5 / transfer dictionary)  
- Is the G-field closer to metric dressing, coarse-grained \(L\), or a new macro DOF? (**\(L \neq G\)** type safety)  
- One major synthesis paper vs short monograph?  
- Optional paper-only: pure residual dual without MC soft spots (PCRH\(_b\)) — **not** the default open crisis

---

## 10. Glossary (minimal)

| Term | Meaning |
|------|---------|
| \(H_c\) | Classical computational entropy (output Shannon/differential entropy) |
| \(S_c\) | Quantum/gravity computational entropy (von Neumann of channel output) |
| \(\Phi_g\) | Gravitational CPTP channel |
| \(L\) | Computational load (dimensionless demand; clocks \(d\tau\)) |
| GfE | Gravity from Entropy (Bianconi) |
| \(G\) / \(G_c\) | Matter- or computation-induced metric (**not** \(L\)) |
| IDEM | Expanded identity with metadata (arity, decay vector, \(d_f\), AST metrics) |
| Decay vector | Which inputs are (ir)recoverable from output |
| PM | Perona–Malik anisotropic diffusion (GfE warm-up dual) |
| ACD-EW | Action–Channel Duality (Euclidean warm-up) — program-level settled |

Full living glossary: `GLOSSARY.md`.

---

## 11. Suggested first tasks for a new agent

**Default:** prefer **M11 / claims freeze / paper outline** over residual dual. Do **not** restart heat-vs-PM residual unless the user asks for a paper-quality pure theorem.

| Request type | Start here |
|--------------|------------|
| **M11 IDEM → load (preferred)** | [synthesis/m11-idem-to-load.md](synthesis/m11-idem-to-load.md) + `THEORY.md` central gap + load terms §3.2 |
| **Claims freeze / hygiene** | [synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md) · [PROGRESS_REPORT.md](PROGRESS_REPORT.md) §2 |
| **Paper outline** | `PLAN.md` series; settled dual + Path J/M + M6 WEAK PASS / FAIL identity |
| **Continuum hygiene (M5 / M10)** | [synthesis/acd-ew-continuum-transfer.md](synthesis/acd-ew-continuum-transfer.md) · [m5-warmup-continuum-t4.md](synthesis/m5-warmup-continuum-t4.md) |
| **Open math board** | [synthesis/OPEN_MATH_DECISION_LOG.md](synthesis/OPEN_MATH_DECISION_LOG.md) (M11 high value; M1 residual **settled** — do not default-chase) |
| **Duality / pack (reference)** | [synthesis/PACK_INDEX.md](synthesis/PACK_INDEX.md) then ACD-EW + transfer dictionary |
| **Re-run joint toy (regression)** | `simulations/bridging/` core + notebook; scorecard should stay PROMISING |
| **Theory / GfE bridge** | `THEORY.md` §3.3 + `synthesis/bridge-bianconi-relative-entropy.md` |
| **Papers / citations** | `papers/external/README.md` + main `.tex` unification section |
| **Canonical defs only** | `foundations/.../definition.md`, `emergent-gravity/master-equation.md` |
| **Repo reorg** | `PLAN.md` hybrid canonicalize-first strategy |

---

*This document replaces any prior PRD.md. Update it when the joint-toy scorecard, workflow status, or primary research focus changes.*
