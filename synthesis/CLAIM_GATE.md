# Claim Gate — pre-merge / pre-draft checklist

**Status:** Failure-mode infrastructure (Track A) · 2026-07-15  
**Authority:** [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) §2–§5 · [NONCLAIMS_FIXTURE.md](NONCLAIMS_FIXTURE.md)  
**Hygiene:** [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) · [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) · [m11-idem-to-load.md](m11-idem-to-load.md)  
**Post-freeze avenues:** [OPEN_AVENUES.md](OPEN_AVENUES.md) · [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md)  
**Stance:** Preliminary research. Prefer under-claiming. **Nothing has GR-level certainty.**

**Gate on open claims:** asserting O1–O5 closed without the missing theorem listed in OPEN_AVENUES → **FAIL**.

Run this gate **before** merging theory prose, paper sections, or claim-bearing docs. Agents: fail closed on any FAIL row.

---

## 0. Mandatory labels on every bridge claim

| Label | Required when |
|-------|----------------|
| **semantic / structural / constructive** | Any Stage-1 ↔ Stage-2 ↔ Stage-3 map |
| **Layer W / D / G / M** | Any result that could be misread as gravity (see §4) |
| **Entropy object tag** | Any use of \(H_c\) / \(S_c\) in theory claims (see §1) |

---

## 1. Entropy object tags (M10) — fail bare \(H_c\)

| Tag | Symbol | Object | FAIL if treated as |
|-----|--------|--------|--------------------|
| **A** | \(H_c\) / \(H_c(f;p_X)\) | Classical **map** output Shannon/differential | \(S_c\), toy residual, game EV |
| **B** | \(S_c(\Phi;\rho)\) | Von Neumann of **channel** output \(\Phi(\rho)\) | Toy \(H_c\), \(S_{\mathrm{GfE}}=-\sum\ln G\) |
| **C** | \(H_c^{\mathrm{toy}}\) | Dual residual + edge entropy (ACD-EW toys) | Canonical \(H(Y)\); continuum \(S_c\) |
| **D** | \(H_c^{\mathrm{game}}\) | Predictive Shannon \(H(Y_k\mid\mathcal{F}_{k-1})\) | Dual residual; strategy ROI |
| **E** | \(H_c^{\mathrm{disc}}\) | Finite map / IDEM / M11 ledger \(H(Y)\) | Continuum \(S_c\); dual residual |

**Gate:** Theory claims that write bare \(H_c\) without tag (or unambiguous Tag A context) → **FAIL**.  
**Gate:** \(H_c^{\mathrm{toy}}\equiv S_c\), \(H_c^{\mathrm{disc}}\equiv S_c\), \(H_c\equiv S_{\mathrm{GfE}}\) → **FAIL**.  
Details: [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md).

---

## 2. Type safety

| Rule | FAIL examples |
|------|----------------|
| \(L\) = **dimensionless scalar** demand; \(G\) = **metric** (or edgewise cousin) | \(L\equiv G\), “load metric,” load as continuum \(G_{\mu\nu}\) |
| \(L^{\mathrm{disc}}\) (M11 three-slot ledger) \(\neq\) continuum \(L(\rho,g)\) | AND/SKI/shoe ⇒ continuum load or Einstein |
| Continuum limit of \(G_i\) \(\neq\) limit of \(L_{\mathrm{clock}}\) | Mesh \(h\to0\) of dual toys ⇒ proper-time gravity |
| Clock form \(d\tau=dt/(1+\alpha L)\) is **on-shell / diagnostic** in toys | Free derivation of Newton \(G\) from \(\alpha,\beta\) alone |

---

## 3. Dual scope (ACD-EW only)

| May assert | Must not assert |
|------------|-----------------|
| Constructive **Euclidean** dual: warm-up \(G[\phi]\), PM, observation channel, split load, load clock | Dual = continuum gravity confirmation |
| Joint toys **6/6 SUPPORT** = dual **pattern** robust | Lattice denoising = empirical gravity |
| Residual dual **T1′ / \(U_\star\)** (windowed), not all \(t\) | T1 for all \(t\in(0,t_\star]\); pure T1′ with no soft PCRH\(_b\) |
| PM > heat on edged structure = expected dual success | Master equation \(\Leftrightarrow\) continuum GfE |

Full dual non-claims: CURRENT_CLAIMS §3, §6. Warm-up continuum honesty: [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md).

---

## 4. Layer labels W / D / G / M

| Layer | Code | Scope | Transfer up only with new map |
|-------|------|-------|-------------------------------|
| **W** | Warm-up | Euclidean GfE warm-up / \(G=1+\alpha|\nabla\phi|^2\) / PM | → G, M |
| **D** | Dual | ACD-EW observation dual + T1′ / toys | → G, M, gravity phenomenology |
| **G** | Full GfE | Continuum Bianconi relative-entropy action, \(\Lambda_G\), G-field | Identity with M without decision |
| **M** | Master eq | \(\Phi_g\), \(S_c\), continuum \(L\), \(d\tau=dt/(1+\alpha L)\) | Identity with G without decision |

**Gate:** Results proved/shown only on W or D must not be cited as G or M theorems.  
**Gate:** M6 Poisson agreement is **GR-layer contact**, not W/D success and not G⇔M.

---

## 5. Newton, M6, M11, constants

| Topic | PASS only if | FAIL if |
|-------|--------------|---------|
| **Newton** | **Path J/M only** (Clausius → Einstein → Poisson; \(\alpha\beta=4\pi G/c^4\) on-shell calibration) | Pointwise \(\Phi\propto\rho\Rightarrow\nabla^2\) Poisson (**withdrawn**) |
| **M6** | WEAK PASS shared \(\nabla^2\Phi=4\pi G\rho_m\) via Einstein/GR | Framework identity; same mechanism; next-order match |
| **M6b** | Structural FAIL: GfE EOM extras vs load-clock \(\gamma_L,\delta_L\) | \(\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G\) |
| **M11** | Discrete \(H_c^{\mathrm{disc}}\), \(L^{\mathrm{disc}}\) **accounting** | Continuum \(L\)/\(G\) from IDEM; Einstein from AND/SKI/shoe |
| **Constants** | Separate \(\alpha_L,\beta_L\) vs \(\alpha_B,\beta_B\); refuse identification | \(\alpha_L\beta_L=\alpha_B/\beta_B\) without new OPEN_MATH decision |

---

## 6. Pass/fail mental table (agents)

| # | Check | Pass | Fail |
|---|--------|------|------|
| G1 | Entropy symbols tagged A–E / \(S_c\) | Explicit tag or unambiguous Tag A | Bare \(H_c\) in theory claim; silent cross-object ID |
| G2 | \(L\neq G\); \(L^{\mathrm{disc}}\neq L(\rho,g)\) | Type-safe wording | \(L\equiv G\); ledger = continuum load |
| G3 | Dual = Euclidean pattern only | ACD-EW / W+D language | Dual proves gravity / ME⇔GfE |
| G4 | Residual dual windowed | T1′ / \(U_\star\); soft PCRH\(_b\) named | All-\(t\) T1; pure with no soft hyp. |
| G5 | Newton Path J/M only | J + M calibration honesty | Withdrawn Laplacian identity |
| G6 | M6 WEAK PASS ≠ identity | Shared Poisson + FAIL identity | “Same theory” / mechanism match |
| G7 | M11 accounting only | Discrete ledger claims | Einstein / continuum \(G\) from gates |
| G8 | Constant refusal | No \(\alpha_L\beta_L=\alpha_B/\beta_B\) | Forced constant identification |
| G9 | Layer W/D/G/M labeled | Layer stated on gravity-facing claims | Warm-up result sold as full GfE |
| G10 | Non-claims list intact | Aligns CURRENT_CLAIMS §3 | Asserts any frozen non-claim |

**Merge rule:** any single FAIL → do not merge claim-bearing text; fix wording or open a decision in [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md).

---

## 7. Explicit non-claims (mirror CURRENT_CLAIMS §3)

Do **not** assert without new work:

1. Master equation \(\Leftrightarrow\) Bianconi continuum GfE.  
2. \(L\equiv G\), \(S_c\equiv\operatorname{Tr} g\ln G^{-1}\), \(\alpha_L\beta_L\equiv\alpha_B/\beta_B\).  
3. T1 residual domination for all \(t\in(0,t_\star]\) (use T1′ / \(U_\star\)).  
4. Pure T1′ with **no** soft hypotheses (PCRH\(_b\) ensemble-certified).  
5. Newton from pointwise \(\Phi\propto\rho\) Laplacian (**withdrawn**).  
6. Next-order \(\gamma_L,\delta_L\) equal GfE \(D_{\mu\nu},\Lambda_G\).  
7. Lattice denoising = empirical gravity.  
8. External GfE papers established on par with GR.  
9. IDEM/decay fully constructs continuum \(L\) or \(G\).

Also: no theorem-level multi-jump / 2D / continuum SPDE residual domination; toy \(H_c\neq\) von Neumann \(S_c\) identity.

Canonical list + optional grep: [NONCLAIMS_FIXTURE.md](NONCLAIMS_FIXTURE.md) · `simulations/classical/check_claim_hygiene.py`.

---

## 8. Quick links

| Role | Path |
|------|------|
| Frozen may-assert / non-claims | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md) |
| Non-claims fixture | [NONCLAIMS_FIXTURE.md](NONCLAIMS_FIXTURE.md) |
| Entropy object map | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) |
| Warm-up continuum hygiene | [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md) |
| M11 discrete load | [m11-idem-to-load.md](m11-idem-to-load.md) |
| Notation | [../GLOSSARY.md](../GLOSSARY.md) |
| Paper outline non-claims banner | [../papers/06-synthesis/OUTLINE.md](../papers/06-synthesis/OUTLINE.md) |
| Program non-claims | [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) §2.3 |

---

*Update when CURRENT_CLAIMS §3, M10 tags, or layer codes change. Do not invent physics here — gates only.*
