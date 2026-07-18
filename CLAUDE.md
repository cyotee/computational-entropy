# CLAUDE.md — Agent bootstrap for computational-entropy

Research repository: **computational entropy** (\(H_c\)/\(S_c\)), **IDEM / lambda** models, **emergent gravity** (channel \(\Phi_g\), load \(L\), master equation), and a **bridge** to continuum Gravity-from-Entropy (Bianconi GfE).

**Stance:** Preliminary research. Prefer under-claiming. Nothing here has GR-level certainty.

---

## Read order (new session)

1. **[PROGRESS_REPORT.md](PROGRESS_REPORT.md)** — settled claims, non-claims, next avenues (prefer first)
2. **[synthesis/CURRENT_CLAIMS.md](synthesis/CURRENT_CLAIMS.md)** — frozen may-assert / non-claims
3. **[PRD.md](PRD.md)** — mission, agent rules
4. **[THEORY.md](THEORY.md)** — bridge architecture + correspondence tables
5. Task-specific: canonical defs → synthesis pack → code

| Task | Start here |
|------|------------|
| **Integrated research paper** | `papers/06-synthesis/PAPER.md` (standalone; literature + our theory) |
| **In-repo freeze / conclusions** | `papers/06-synthesis/FINAL.md` · `synthesis/PROGRAM_CONCLUSIONS.md` |
| **Post-freeze research avenues** | `synthesis/OPEN_AVENUES.md` (new theory vs experiment; O1–O5) |
| **M11 IDEM → load** | `m11-idem-to-load.md` · `m11c-continuum-motivation.md` · `simulations/classical/` |
| Entropy objects | `m10-sc-vs-toy-hc.md` · `m10-p1-object-comparison.md` |
| Warm-up continuum | `m5-warmup-continuum-hygiene.md` · `m5b-smooth-action-limit.md` |
| Claims hygiene | `CLAIM_GATE.md` · `check_claim_hygiene.py` |
| Open math board | `synthesis/OPEN_MATH_DECISION_LOG.md` (D1–D12) |
| Joint toy / dual (reference only) | `simulations/bridging/` — do not default-chase residual dual |
| Canonical definitions only | `foundations/computational-entropy/definition.md`, `emergent-gravity/master-equation.md` |
| GfE literature bridge | `synthesis/bridge-bianconi-relative-entropy.md`, `papers/external/` |
| Repo reorg | `PLAN.md` (canonicalize-first hybrid) |
| Notation | `GLOSSARY.md` |

Do **not** treat root `README.md` definition blocks as sole authority when marked historical; prefer `foundations/` and `emergent-gravity/`.

---

## Mission (one sentence)

Define computational entropy as entropy of a map/channel’s **output distribution**; develop gravitational channel \(\Phi_g\) + load \(L\) recovering gravity phenomenology in limits; bridge to continuum GfE **without** forcing premature symbolic identity of actions and master equations.

### Three-stage mental model

```text
STAGE 1 — Computational induction (ours)
  ρ, Φ_g, S_c / H_c, L, dτ = dt/(1+αL)
  IDEM / decay / games = discrete microstructure (M11 design + Phase 1 AND ledger started)
        │
        ▼
STAGE 2 — Geometric imprint (bridge)
  Structure-induced metric G  (or computational cousin)
  TYPE SAFETY: L is a dimensionless scalar; G is a metric — L ≠ G
        │
        ▼
STAGE 3 — Continuum GfE (macro target)
  Relative entropy of metrics → modified Einstein, Λ_G, G-field
```

### Three research threads

| Thread | Content | Entry points |
|--------|---------|--------------|
| Classical / lambda | IDEM, decay vectors, \(d_f\), combinatorics, games (Blackjack…) | `computational-models/`, `research/`, root IDEM `.markdown` |
| Emergent gravity | \(\Phi_g\), \(S_c\), \(L\), master eq, recoveries | `foundations/`, `emergent-gravity/`, `quantum/` |
| Bridge / synthesis | Mappings, ACD-EW dual, external GfE | `THEORY.md`, `synthesis/`, `simulations/bridging/` |

**Central gap:** Gravity work uses high-level \(H_c\)/\(S_c\) but not yet lambda/IDEM machinery. Cohesion goal: semantic → structural → constructive.

---

## Canonical sources (do not reinvent)

| Concept | Canonical file |
|---------|----------------|
| Computational entropy \(H_c\) / \(S_c\) | `foundations/computational-entropy/definition.md` |
| \(\Phi_g\), load \(L\), master equation | `emergent-gravity/master-equation.md` |
| Newton recovery (Path J/M) | `emergent-gravity/recoveries/newtonian/README.md` |
| Formal Euclidean dual (ACD-EW) | `synthesis/action-channel-duality-euclidean.md` |
| Frozen claims sheet | `synthesis/CURRENT_CLAIMS.md` |
| M11 IDEM → \(H_c\) / \(L^{\mathrm{disc}}\) | `synthesis/m11-idem-to-load.md` |
| Synthesis pack map | `synthesis/PACK_INDEX.md` |
| Math decision board (M1–M12, D1–D9) | `synthesis/OPEN_MATH_DECISION_LOG.md` |
| Main paper draft | `quantum/Computational_Entropy_and_Emergent_Gravity.tex` |

**Single source of truth:** Link to canonical files; do **not** re-copy master equation / \(H_c\) definition into new docs.

---

## Notation (strict)

| Symbol | Meaning |
|--------|---------|
| \(H_c\) | Classical computational entropy (output Shannon / differential) |
| \(S_c\) | Quantum/gravity computational entropy (von Neumann of channel output) |
| \(\Phi_g\) | Gravitational CPTP channel |
| \(L\) | Computational load (dimensionless demand; clocks \(d\tau\)) |
| \(G\) | Matter- or structure-induced metric (GfE) — **not** Newton’s \(G\) in load formulas unless clear from context |
| GfE | Gravity from Entropy (Bianconi) |
| IDEM | Expanded identity + metadata (arity, decay vector, \(d_f\), AST metrics) |
| Decay vector | Which inputs are (ir)recoverable from output |
| PM | Perona–Malik anisotropic diffusion (GfE warm-up gradient-flow dual) |
| ACD-EW | Action–Channel Duality (Euclidean warm-up) |

Mark every mapping as **semantic / structural / constructive**. Never claim derivation of Bianconi’s action from \(L\) (or reverse) without an explicit map.

---

## Settled claims vs non-claims

### May treat as settled (research-program level)

- **ACD-EW** constructive Euclidean dual (GfE warm-up / PM ↔ observation channel + split load + load clock)
- Joint toys **6/6 SUPPORT** (1D, 2D, blackjack-belief *pattern only*) — dual **pattern**, not gravity confirmation
- Residual dual is **time-windowed (T1′)**, not all \(t\); unified pure window \(U_\star=[1.36,2.40]\) under soft PCRH\(_b\)
- Newton recovery = **Path J/M** only (Clausius → Einstein → Poisson); \(\alpha\beta=4\pi G/c^4\) is on-shell calibration
- **M6:** WEAK PASS shared Newtonian Poisson via GR; **FAIL** framework identity
- Heat/PM residual dual is **settled enough** — do not restart as main crisis unless user asks for paper-quality pure theorem

### Explicit non-claims (do not assert)

1. Master equation \(\Leftrightarrow\) full continuum GfE  
2. \(L \equiv G\), \(S_c \equiv \operatorname{Tr} g\ln G^{-1}\)  
3. T1 residual domination for all \(t\in(0,t_\star]\)  
4. Lattice denoising = empirical gravity  
5. IDEM/decay fully constructs continuum \(L\) or \(G\)  
6. Pointwise \(\Phi\propto\rho\Rightarrow\nabla^2\) Newton (withdrawn)

Full tables: `PROGRESS_REPORT.md` §2.

---

## Repository map

```text
PRD.md, PLAN.md, THEORY.md, GLOSSARY.md, PROGRESS_REPORT.md, README.md
foundations/computational-entropy/definition.md   # H_c / S_c canonical
emergent-gravity/master-equation.md               # Φ_g, L, master eq
emergent-gravity/recoveries/                      # Newton, BH, cosmology, …
synthesis/                                        # ACD-EW, M-series, bridge notes
  PACK_INDEX.md, OPEN_MATH_DECISION_LOG.md
simulations/bridging/                             # joint toys + T1 envelopes
papers/                                           # series skeleton + external/ GfE PDFs
quantum/                                          # legacy gravity writeups + main .tex
computational-models/, research/                  # lambda / IDEM / games
notebooks/, images/graphs/                        # older game entropy work
drafts/, archive/                                 # historical; prefer canonicals
src/python/                                       # misc scripts
```

**Reorg policy:** Hybrid *canonicalize-first* (`PLAN.md`). Skeleton exists; much content still in legacy paths. Mark superseded files; do not mass-delete without user confirmation.

---

## Commands

Project uses a local venv (`.venv`). Prefer it for all Python work.

```bash
# Activate / use project Python
.venv/bin/python ...

# Claim hygiene
.venv/bin/python simulations/classical/check_claim_hygiene.py

# D13 relationship witnesses
.venv/bin/python simulations/classical/m11_composition_ledger.py
.venv/bin/python simulations/classical/m11_landauer_and_ledger.py
.venv/bin/python simulations/bridging/m5c_pm_energy_descent.py
```

**Jupyter kernel:** `Python (computational-entropy)` → project `.venv`.  
Notebook: `simulations/bridging/gfe_load_joint_toy.ipynb`.

**Main paper (LaTeX):** `quantum/Computational_Entropy_and_Emergent_Gravity.tex` (build with local TeX toolchain if available).

No root `package.json` / `Cargo.toml` — this is markdown + Python research, not a product app.

---

## Joint toy (what agents need)

| Path | Role |
|------|------|
| `_joint_toy_v2_core.py` | 1D core + CLI |
| `_joint_toy_2d.py` | 2D Catte PM lift |
| `blackjack_belief_dual.py` | Game-motivated \(\phi\) (pattern only) |
| `DESIGN_gfe_load_joint_toy.md` | Design + honesty limits |
| `gfe_load_joint_toy_scorecard_v2.txt` | Latest 1D scorecard |

**Setup (1D):** hidden \(\phi_\star\); observation \(y=\phi_\star+\eta\); \(G=1+\alpha_G(\nabla\hat\phi)^2\); dynamics heat vs PM vs load-gated PM; channel \(H_c\) = residual log-energy + edge-location entropy; load split \(L_E,L_S,L_B\); clock uses \(L_E+L_S\).

**Interpretation rule:** 6/6 SUPPORT means Euclidean dual **pattern** is robust — not continuum gravity confirmation. Do not churn parameters only to keep 6/6 without new science.

---

## Agent rules

1. **Bootstrap** via PROGRESS_REPORT → PRD → THEORY before large edits.  
2. **Canonicalize:** link foundations/master-equation; no duplicate core formulas.  
3. **Rigor honesty:** semantic / structural / constructive labels on every bridge claim.  
4. **Type safety:** \(L\) scalar ≠ metric \(G\).  
5. **Do not** restart heat-vs-PM residual dual from scratch unless asked.  
6. **Update living docs** when status changes: PRD scorecard sections, PROGRESS_REPORT, THEORY progress log, DESIGN files, PACK_INDEX / OPEN_MATH as needed.  
7. **Archive carefully:** confirm before mass-moving or deleting `drafts/`, `archive/`, root historical `.markdown`.  
8. **Risky git actions** (force-push, hard reset, bulk delete): confirm with user first.

---

## Recommended next avenues (unless user directs otherwise)

From PROGRESS_REPORT §7 / **D15**:

1. **Read** `papers/06-synthesis/FINAL.md` + `synthesis/PROGRAM_CONCLUSIONS.md`  
2. **New cycle:** `synthesis/OPEN_AVENUES.md` — “new theory” = missing theorems/constructions, not “wrong program”; default O1  
3. Optional LaTeX/figures only  

**Done (D9–D15):** full program freeze — FINAL report, P1–P11 conclusions, R1–R4a, claim gate.  
**Do not** default-chase heat/PM residual dual.

---

## Gotchas

- Root and `quantum/` files often **duplicate** definitions; many marked **Historical / superseded**.  
- `field φ` in toys is a **test signal on a flat lattice**, not spacetime geometry; “jump” = step edge in test data, not a gravity well.  
- Blackjack dual scorecard is **pattern only** — not blackjack EV / strategy ROI.  
- External PDFs in `papers/external/` are **peers in a research program**, not established foundations.  
- Newton: use Path J/M; do not revive withdrawn pointwise Laplacian identity.  
- Working tree may mix uncommitted synthesis with committed skeleton — check `git status` before large reorgs.

---

## Key external literature (local)

| Paper | Path |
|-------|------|
| Bianconi, Gravity from entropy (PRD 2025) | `papers/external/Bianconi_Gravity_from_entropy_*` |
| Bianconi, Beyond holography (PM = GfE flow) | `papers/external/Bianconi_Beyond_holography_*` |
| Thattarampilly–Zheng (inflation / spherical BH) | `papers/external/Thattarampilly_*` |
| Kumar (semiclassical Einstein via \(S_{\rm gen}\)) | `papers/external/Kumar_*` |

Notes: `papers/external/Bianconi_Gravity_from_entropy_NOTES.md`, `papers/external/README.md`.

---

*Update this file when bootstrap order, canonical paths, settled claims, or standard commands change.*
