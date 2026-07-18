# Open Math Decision Log

**Status:** Living log (started 2026-07-14)  
**Purpose:** Track **serial** choices among open mathematical problems after the parallel synthesis pack. Experiments (1D/2D/blackjack dual toys) are largely done for the Euclidean layer; remaining work is proof, continuum contact, or new model classes.  
**Related:** [PACK_INDEX.md](PACK_INDEX.md) · [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) · [t1-residual-domination.md](t1-residual-domination.md) · [weak-field-gfe-vs-load.md](weak-field-gfe-vs-load.md)

---

## 0. Stance (read before prioritizing)

1. **Preliminary all the way down.** Our theory, Bianconi GfE, and ACD-EW are research constructions. Supporting evidence is real; “proven like GR” is not.
2. **Toys ≠ continuum equivalence.** 6/6 scorecards support a **Euclidean dual pattern**, not modified Einstein \(\Leftrightarrow\) master equation.
3. **Prefer falsifiable next steps** over more scorecards of the same dual.
4. **One serial math track at a time** when the same author/agent must hold proof details; experiments can still fork.

---

## 1. Open problem board

| ID | Problem | Primary doc | Status | Blocks / unblocks |
|----|---------|-------------|--------|-------------------|
| **M1** | **T1 residual domination** | [t1](t1-residual-domination.md) · [m1](m1-lemma-c-prime.md)–[m1g](m1g-unified-pure-window.md) | **Unified pure \(U_\star=[1.36,2.40]\)** (\(\rho_b=0.42\)); PCRH\(_b\) soft | Semi-analytic dual refined |
| **M2** | **T1-load** | [m2-t1-load.md](m2-t1-load.md) · [m2-m4-followups.md](m2-m4-followups.md) | **Hybrid done on \(I_\star\)**; pure open | Clock dual |
| **M3** | **T2 Lyapunov** | m2-m4-followups | **Deferred open** | Stronger dual |
| **M4** | **T3 load reparam** | m2-m4-followups | **Deferred open** | Toy master-equation form |
| **M5** | **T4 continuum warm-up** | [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) · [hygiene](m5-warmup-continuum-hygiene.md) · [m5b](m5b-smooth-action-limit.md) | **Citation + hygiene + smooth action sketch;** Γ open | Warm-up continuum contact |
| **M6** | **Weak-field plug-test** | [m6](m6-weak-field-plugtest.md) · [m6b](m6b-next-order-weak-field.md) · [m6c](m6c-bianconi-linearization.md) | **WEAK PASS** Poisson; structural next-order FAIL; **M6c** PDF linearization (\(\Lambda_G=O(\epsilon^2)\), \(D_{\mu\nu}\) present) | Gravity-facing cross-check |
| **M7** | **Symbol map** | [m7-symbol-map.md](m7-symbol-map.md) | **Done: candidates + non-maps** | Feeds M6 |
| **M8** | **Newton recovery audit + rewrite** | [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md) · [../emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) | **Done: gap N1 closed in writeup; Path J/M canonical** | Credibility for M6 |
| **M9** | Lorentzian / curvature-in-\(G\) lift | bridge + Bianconi | **Deferred** (D1) | Full GfE contact |
| **M10** | \(S_c\) vs residual \(H_c\) | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) · [m10-p1-object-comparison.md](m10-p1-object-comparison.md) | **Dictionary done; P1 hybrid non-identity done;** id theorem / P2+ open | Quantum channel |
| **M11** | IDEM / decay → \(H_c\), \(L^{\mathrm{disc}}\) (not continuum \(G\)) | [m11](m11-idem-to-load.md) · [m11c](m11c-continuum-motivation.md) | **P1–2 + coupled + continuum motivation** (D12); continuum \(G\) deferred | Microstructure |
| **M12** | True game log-loss channel | blackjack DESIGN | **Deferred** (D1); belief dual exists | Classical depth |

---

## 2. Decision log (chronological)

### 2026-07-14 — Pack complete; serial priority set

**Context:** Parallel agents delivered transfer dictionary, weak-field comparison, T1 standalone plan, blackjack-belief toy (6/6 pattern). Euclidean experimental dual is saturated for now.

**Decision D1 — Next math priority: M1 (T1 residual domination), then M6 (weak-field plug-test prep).**

| Order | Item | Why this order |
|-------|------|----------------|
| **1** | **M1** close Lemma C (edge persistence) then Lemma E | Highest leverage on dual’s *analytic* status; uses existing toy; no continuum ambiguity |
| **2** | **M8** verify/clean Newton Poisson recovery in-repo | Cheap credibility fix before M6 |
| **3** | **M7 + M6** weak-field dictionary → plug-test design (then calculation) | First gravity-facing cross-framework test; depends on honest low-coupling reading of Bianconi |
| **4** | **M2–M4** after M1 | Clock/Lyapunov once residual domination exists |
| **5** | **M5** as citation/continuum warm-up polish | Partly literature-backed; lower urgency |
| **Defer** | **M9–M12** | Larger scope; do not start until M1 or M6 produces a clear pass/fail |

**Rejected for now**

| Choice | Reason |
|--------|--------|
| More dual scorecards (new ICs only) | Diminishing returns; pattern already 6/6×3 |
| Claim continuum equivalence from toys | Epistemically false |
| Jump to full Lorentzian GfE derivation | Skips M6/M7; uncontrolled |
| Treat T1 as proved because scorecard passes | Scorecard is witness, not theorem (see t1 note) |

**Success criteria for the next session on M1**

- Written proof of Lemma C (or a weakened C′ with explicit \(T(\sigma,K,N)\)) **or** a documented obstruction.
- Updated lemma board in `t1-residual-domination.md`.
- If C closes: start Lemma E comparison inequality.

**Success criteria for the next session on M6 (after or parallel to M8)**

- Explicit list of Bianconi low-coupling → EH equations cited from PDF (page/eq).
- Side-by-side Poisson (or linearized \(g_{00}\)) expressions for both frameworks.
- Either a candidate constant map (M7) or a clear impossibility note.

---

### 2026-07-14 — D1 execution complete (parallel M1/M5/M8 + serial M7/M6 + F)

**Context:** Goal execute M-series per plan: parallel then serial; integrate cross-refs.

**Decision D2 — Record outcomes; freeze claims; next optional work is deepen T1′ proof or linearized GfE extras.**

| Track | Outcome |
|-------|---------|
| **M1** | Strict T1 on \((0,t_\star]\) **obstructed** (heat wins ultra-short residual). **C′** localization proved sketch + MC; persistence experimental. **T1′** window \([t_{\min},t_{\max}]\) with strong MC support. Artifact: `m1-lemma-c-prime.md`, `t1_mc_envelope.txt`. **Not theorem.** |
| **M5** | Continuum warm-up **citation bridge** complete; smooth FD consistency sketched; full T4 open. Artifact: `m5-warmup-continuum-t4.md`. |
| **M8** | Newton.md Laplacian step **algebraically wrong** if \(\Phi\propto\rho\) pointwise. Path **J/M** (Jacobson/Einstein + calibration) documented. Artifact: `m8-newton-recovery-audit.md`. |
| **M7** | Candidate maps + explicit non-maps; refuse \(\alpha_L\beta_L=\alpha_B/\beta_B\). Artifact: `m7-symbol-map.md`. |
| **M6** | **WEAK PASS** shared Poisson; **FAIL** mechanism identity / full equivalence. Artifact: `m6-weak-field-plugtest.md`. |
| **M2–M4** | Explicit **deferral** with rationale. Artifact: `m2-m4-followups.md`. |
| **M9–M12** | Remain **deferred** (D1). |

**Accepted next steps (optional, not required for D2 closure):** analytic close of C′2/E′; rewrite Newton.md along Path J; linearized GfE next-order modes.

**Rejected:** Claiming T1 proved; claiming GfE ⇔ master equation from weak PASS; implementing M9–M12 in this pass.

**Claim freezes (reaffirmed):** §5 still applies; add: do not cite ultra-short-time residual dual without T1′ window.

---

### 2026-07-14 — D3 parallel package: Newton rewrite + T1′ + next-order weak field

**Context:** User requested all three discrepancy-resolution suggestions in parallel (Newton Path J/M rewrite; solidify T1′/C′2; next-order GfE vs \(\gamma_L,\delta_L\)).

**Decision D3 — Execute N1/N2/N3 in parallel; freeze upgraded claims; leave sharpened C′2 and Bianconi linearization open.**

| Track | Outcome |
|-------|---------|
| **N1 Newton rewrite** | Canonical [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) + [quantum/Newton.md](../quantum/Newton.md) along **Path J/M**. Invalid Laplacian chain **withdrawn**. \(\alpha\beta=4\pi G/c^4\) = on-shell matching only. |
| **N2 T1′ / C′2** | [m1b-t1-prime-c2-bound.md](m1b-t1-prime-c2-bound.md): analytic crude \(T_{\mathrm{pers}}\approx 0.76\); experimental T1′ window **\([1.6,6.4]\)**; E′ inequality explicit; **full T1′ theorem still open** (need sharpened persistence so analytic \(t_{\max}\ge t_{\min}\), plus \(\Delta_{\mathrm{noise}}\)). |
| **N3 next-order weak field** | [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md): GfE extras live in **metric EOM** (\(\Lambda_G,D_{\mu\nu},R^G\)); our \(\gamma_L,\delta_L\) live in **load clock** unless promoted. **Structural FAIL** as same next-order object class. PPN/Yukawa coefficients **not** computed. |
| **N4 integration** | PACK_INDEX, this log, m1/m6/m8/t1/weak-field cross-refs updated. |

**Accepted next steps (optional after D3):**

1. Sharpen C′2 constants (comparison / cancellation) so \(T_{\mathrm{pers}}\gtrsim t_{\min}\).  
2. Lattice estimate of \(\Delta_{\mathrm{noise}}(t)\) for analytic \(t_{\min}\).  
3. Explicit Bianconi linearization (W1) for coefficient-level M6b.  
4. M2–M4 only after T1′ theorem or clear stop.

**Rejected:** Claiming T1′ proved; equating \(\gamma_L\) with \(D_{\mu\nu}\); restoring \(\Phi\propto\rho\) Laplacian recovery; M9–M12.

**Claim freezes (additions):**

6. Do **not** claim Newton recovery from pointwise \(\Phi\propto\rho\).  
7. Do **not** claim next-order load corrections equal GfE G-field corrections.  
8. Do **not** cite analytic \(T_{\mathrm{pers}}\approx 0.76\) as the experimental residual window (MC window is larger).

---

### 2026-07-14 — D4 parallel package: C′2♯ + \(\Delta_{\mathrm{noise}}\) + Bianconi linearization

**Context:** User again requested parallel work on the post-D3 open suggestions.

**Decision D4 — Close empty-window block on T1′; freeze PDF-anchored GfE linear structure; leave full E′ and PPN open.**

| Track | Outcome |
|-------|---------|
| **C′2♯** | [m1c](m1c-c2-sharp-delta-noise.md): C′1b \(H^0\ge 0.80\) + floor \(0.25\) ⇒ \(T_{\mathrm{pers}}^\sharp\approx 1.67\ge t_{\min}\approx 1.2\). Analytic T1′ window **nonempty**. |
| **\(\Delta_{\mathrm{noise}}\)** | Lattice split: \(R_h-R_{\mathrm{PM}}=R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\) holds numerically; crossover at \(t\approx 1.2\) when blur overtakes noise-race gap. Witness: `t1_delta_noise_envelope.txt`, `test_t1_delta_noise.py`. \(c_D\approx 0.30\text{–}0.32\). |
| **Bianconi W1** | [m6c](m6c-bianconi-linearization.md): PDF Eqs. (45),(60),(64),(66)–(68). Leading Poisson PASS. \(\Lambda_G=O(\epsilon^2)\) (no linear CC). \(D_{\mu\nu},R^G-R\) are linear next-order structures; still **≠** load-clock \(\gamma_L,\delta_L\). No PPN numbers. |

**Accepted next (optional):** close E′ with constants on \([1.2,1.67]\); martingale C′2 for longer analytic \(t_{\max}\); full PPN reduction of GfE (large).

**Rejected:** Claiming T1′ theorem; equating \(D_{\mu\nu}\) with \(\gamma_L\); quoting GfE PPN from this pass.

**Claim freezes (additions):**

9. Do **not** claim full T1′ theorem from nonempty analytic window alone (E′ still open).  
10. Do **not** claim linear-order \(\Lambda_G\) correction to Poisson (it is \(O(\epsilon^2)\)).

---

### 2026-07-14 — D5 Lemma E′ hybrid close

**Context:** Proceed on recommended next step: close E′ on analytic T1′ window.

**Decision D5 — Record hybrid T1′ residual comparison; freeze pure-theorem language; last pure gap is freeze-tax spectral bound.**

| Track | Outcome |
|-------|---------|
| **E′0** | Identity \(R_h-R_{\mathrm{PM}}=R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\) (analytic) |
| **E′a** | Exact lattice \(R_{\mathrm{blur}}(t)\) table; \(c_D\approx 0.30\) |
| **E′b** | Interface \(\le 2\mu^2/N\), \(\mu=0.09t\) — \(\ll\) blur on window |
| **E′c** | Pure Neumann+interface **insufficient** (freeze tax dominates); \(\Delta_{\mathrm{noise}}\) **MC-certified** \(\le R_{\mathrm{blur}}\) on \(I_\star=\{1.36,1.44,1.52,1.60\}\) with margin \(\ge 4.5\cdot 10^{-4}\) |
| **E′d** | Edge height on \(\mathcal{E}\): PM \(\ge 0.25\); MC ratio \(\sim 4\) at \(t=1.6\) |
| **Witness** | `t1_eprime_envelope.txt`, `test_t1_eprime.py` (asserts pass) |

**Hybrid claim allowed:** residual domination on discrete times \(I_\star\subset[1.2,1.67]\) for toy Euler scheme.  
**Still disallowed:** pure T1′ theorem with no numerical input; T1 on \((0,t_\star]\).

**Accepted next (optional):** spectral bound on PM freeze tax (pure E′c); martingale C′2 for longer \(t_{\max}\); M2 load conjecture.

**Rejected:** Claiming Neumann comparison alone proves E′; reopening raw T1.

**Claim freezes (additions):**

11. Do **not** cite hybrid T1′ as a fully analytic theorem.  
12. Do **not** claim \(R_{\mathrm{PM}}\le R_{\mathrm{Neu}}+R_{\mathrm{interface}}\) with the thin interface majorant alone (empirically false).

---

### 2026-07-14 — D6 write-up + pure E′c majorant + M2 hybrid

**Context:** User requested all three post-E′ recommendations in parallel.

**Decision D6 — Land paper write-up, conditional pure freeze-tax majorant, and M2 hybrid; freeze Hρ as remaining pure gap.**

| Track | Outcome |
|-------|---------|
| **Write-up** | [t1-prime-hybrid-writeup.md](t1-prime-hybrid-writeup.md) + updated paste-ready claims in [acd-ew-continuum-transfer.md](acd-ew-continuum-transfer.md) |
| **Pure E′c** | [m1e-freeze-tax-spectral.md](m1e-freeze-tax-spectral.md): \(\Delta_{\mathrm{maj}}^{\mathrm{typ}}=R_n(\rho_{\mathrm{typ}}t)-R_n(t)+R_{\mathrm{int}}\) with \(\rho_{\mathrm{typ}}\approx 0.439\); **passes \(I_\star\) under Hρ**; Hρ not proved |
| **M2** | [m2-t1-load.md](m2-t1-load.md): load beats heat on \(I_\star\) (frac \(\ge 0.74\) at 1.36, \(\ge 0.97\) at 1.60); \(\tau/t\approx 0.95\); slightly worse than pure PM |

**Accepted next (optional):** prove Hρ; M3 hybrid Lyapunov; paper draft from write-up.

**Rejected:** Claiming unconditional pure T1′; claiming load improves residual vs pure PM.

**Claim freezes (additions):**

13. Do **not** drop the Hρ label when citing the spectral freeze-tax majorant as a pure proof.  
14. Do **not** claim load-PM residual superior to pure PM.

---

### 2026-07-15 — D7 pure Hρ / E′c proof implementation

**Context:** User asked to implement the suggested Hρ proof.

**Decision D7 — Land pure residual dual on \([2.0,2.4]\); keep \(I_\star\) hybrid; record L8-tail as the remaining soft lemma.**

| Result | Detail |
|--------|--------|
| **Artifact** | [m1f-hrho-pure-proof.md](m1f-hrho-pure-proof.md) · `test_t1_pure_hrho.py` (pass) |
| **\(\rho_\star\)** | Full-field energy-weighted \(\rho_{\mathrm{eff}}(2\sigma^2)\approx 0.299\) |
| **Pure window** | \(t\ge 2.0\): \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{maj}}(\rho_\star)\); residual dual MC frac \(=1\) at \(t=2.0\) |
| **Why not \(I_\star\) pure** | \(\rho_\star\approx 0.30\) majorant too loose before \(t=2\); needs \(\rho\gtrsim 0.41\) or burn-in bootstrap |
| **L1–L7** | Spectral heat, Dirichlet-form linear majorant, Gaussian \(\rho_{\mathrm{eff}}\), residual↓, interface/blur, martingale persistence |
| **L8-PCRH** | Proved structure + toy certificate \(\rho_{\mathrm{ew}}(t)\ge\rho_\star\) and \(R_{\mathrm{PM}}^{\mathrm{noise}}\le R_n^{(\rho_\star)}\) |

**Accepted next:** burn-in bootstrap for \(\rho_b\ge 0.41\) to purify \(I_\star\); or paper write-up including pure \([2.0,2.4]\) window.

**Rejected:** Claiming pure dual on all of \(I_\star\) from \(\rho_{\mathrm{eff}}=0.30\) alone.

---

### 2026-07-15 — D8 unified pure window \(U_\star\)

**Context:** User requested pursuit of a single pure residual dual window covering early dual times.

**Decision D8 — Land \(U_\star=[1.36,2.40]\) with \(\rho_b=0.42\); absorb hybrid \(I_\star\) and M1f late pure into one claim.**

| Item | Outcome |
|------|---------|
| **Artifact** | [m1g-unified-pure-window.md](m1g-unified-pure-window.md) · `test_t1_unified_pure.py` |
| **\(\rho_b\)** | 0.42 (burn-in; \(>\rho_{\mathrm{eff}}(0)\approx 0.30\)) |
| **U1** | \(R_{\mathrm{blur}}\ge\Delta_{\mathrm{maj}}^{(0.42)}\) on \(U_\star\) — **exact** |
| **U2 PCRH\(_b\)** | \(\mathbb{E}R_{\mathrm{PM}}^{\mathrm{noise}}\le R_n^{(0.42)}\) on \(U_\star\) — **MC margin \(\ge 0.0003\)** + burn-in \(\rho_{\mathrm{ew}}\) structure |
| **Not pure** | \(t=1.20\) (maj margin negative; dual ~55%) |
| **Big win** | One pure window from start of \(I_\star\) through late times |

**Accepted next:** Harden PCRH\(_b\) (remove MC certificate); paper draft with \(U_\star\).

**Rejected:** Claiming pure dual at \(t=1.20\); pathwise \(\rho\ge 0.42\) from \(t=0\).

---

### 2026-07-15 — D9 dual freeze + M11 open + Phase 1 AND ledger

**Context:** Euclidean residual dual closed at research-program level (D8). User directed parallel claim freeze + M11 design, then sequential Phase 1.

**Decision D9 — Freeze dual as default-closed; primary science track = M11 IDEM→\(H_c\)/\(L^{\mathrm{disc}}\); land Phase 1 pure accounting.**

| Track | Outcome |
|-------|---------|
| **Claim freeze** | [CURRENT_CLAIMS.md](CURRENT_CLAIMS.md); PRD/THEORY retargeted; dual not main crisis |
| **M11 design** | [m11-idem-to-load.md](m11-idem-to-load.md): ontology, \(H_c\), three-slot \(L^{\mathrm{disc}}\), locked flux reading, non-claims |
| **M11 Phase 1** | `simulations/classical/m11_and_gate_ledger.py`: \(H(Y)\approx 0.811\), export \(H(X\mid Y)\approx 1.189\), \(L_E+L_S+L_B\), chain rule exact |
| **M1 residual** | Remains program-level settled; optional paper harden only |

**Accepted next steps:**

1. Optional M11 Phase 2 multi-step / tiny lambda / minimal shoe (M12-adjacent).  
2. Paper outline using CURRENT_CLAIMS + ACD-EW + Path J/M + M6 + M11 design.  
3. Continuum hygiene M5/M10 only without overclaim.  

**Rejected:** Restarting heat/PM residual dual as default; claiming continuum \(L\) or \(G\) from AND-gate; \(L\equiv G\).

**Success criteria met for Phase 1:** S1–S7 in m11 note (exact \(H_c\), three load terms, locked reading, chain rule, non-claims).

---

### 2026-07-14 — D10 continuum hygiene M5 / M10

**Context:** User requested advance of continuum hygiene tracks M5 and M10 without overclaim (no new sims, no Γ-proof).

**Decision D10 — Freeze object/transfer dictionaries; leave identification and Γ-limits open.**

| Track | Outcome |
|-------|---------|
| **M10** | [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md): tags A–E for classical \(H_c\), \(S_c\), toy residual \(H_c^{\mathrm{toy}}\), game \(H_c^{\mathrm{game}}\), M11 \(H_c^{\mathrm{disc}}\); collision table; allow/forbid; program path P0–P4 only |
| **M5** | [m5-warmup-continuum-hygiene.md](m5-warmup-continuum-hygiene.md): warm-up continuum definition; lit-backed vs open; transfer checklist; abstract allow/forbid; points at T4 parent without rewriting history |
| **Parent header** | [m5-warmup-continuum-t4.md](m5-warmup-continuum-t4.md) links hygiene note |

**Accepted next (optional, one each if pursued):** M10 P1 coarsened \(H(Z)\) comparison; M5 smooth-only \(O(h)\) action lemma.

**Rejected:** \(H_c^{\mathrm{toy}}\equiv S_c\); Γ-convergence claimed; master equation \(\Leftrightarrow\) GfE from hygiene notes; new dual simulations.

---

### 2026-07-15 — D11 parallel triple: M11 Phase 2 + paper outline + continuum hygiene

**Context:** User asked to run all three post-D9 avenues in parallel (subagents): M11 Phase 2 classical ledgers; paper outline; continuum hygiene (M5/M10 already landed as D10 mid-flight).

**Decision D11 — Record parallel completion of D9 next-steps; freeze program as ready for first paper draft or M11 Phase 3.**

| Track | Outcome |
|-------|---------|
| **M11 Phase 2** | Multi-step Boolean, tiny SKI, minimal R/B shoe ledgers under `simulations/classical/`; all run exit 0; locked \(L_S\) reading |
| **Paper outline** | [`papers/06-synthesis/OUTLINE.md`](../papers/06-synthesis/OUTLINE.md) — single long program paper; parts 0–8; C1–C14 map; non-claims appendix |
| **M5/M10** | Already D10 dictionaries; reaffirmed as hygiene-complete (Γ / id still open) |

**Numeric witnesses (Phase 2):**

- Boolean: AND \(H_c\approx 0.811\), export \(\approx 1.189\); OR \(H_c\approx 0.954\), lower export \(\approx 0.857\)
- SKI: \(H_c(0)=4\), \(H_c(1)\approx 3.156\), \(L_S(1)\approx 0.844\)
- Shoe: \(H_c(0)=1\); max \(L_S=1\) at last informative draw; mean \(L_{\mathrm{disc}}\approx 1.51\)

**Accepted next steps (pick one):**

1. **First prose draft** of paper following OUTLINE (Parts 1→3→4→5→6→2→7).  
2. **M11 Phase 3** optional: load-clock comparison across strategies / multi-deck shoe (still no gravity).  
3. Optional M10 P1 coarsened \(H(Z)\) or M5 smooth \(O(h)\) lemma (paper depth only).  

**Rejected:** Residual dual restart; continuum \(L\)/\(G\) from Phase 2; \(L\equiv G\); claiming OUTLINE is a finished paper.

---

### 2026-07-15 — D12 deepen theory + failure-mode infrastructure

**Context:** User requested parallel advance of (A) failure-mode guardrails and (B) theory depth per post-D11 plan: CLAIM_GATE, M11c continuum motivation, coupled-regions ledger, M10 P1, M5b smooth lemma.

**Decision D12 — Lock claim gate + deepen structural continuum motivation; freeze object non-identity and smooth warm-up action sketch.**

| Track | Outcome |
|-------|---------|
| **A Claim gate** | [CLAIM_GATE.md](CLAIM_GATE.md) · [NONCLAIMS_FIXTURE.md](NONCLAIMS_FIXTURE.md) · `check_claim_hygiene.py` · GLOSSARY tags A–E, layers W/D/G/M |
| **B1 M11c** | [m11c-continuum-motivation.md](m11c-continuum-motivation.md): three demand axes; roles not equalities; locked flux reading |
| **B1.3 Coupled** | `simulations/classical/m11_coupled_regions_ledger.py`: two AND regions + XOR screen; conservation; high export ⇒ high \(L_S\); G\* screen-only higher export |
| **B2 M10 P1** | [m10-p1-object-comparison.md](m10-p1-object-comparison.md) · `m10_p1_entropy_objects.py`: \(H_c^{\mathrm{toy}}\sim 1.1\)–\(1.3\) vs \(H(Z)\approx 0\) on \(U_\star\) — **non-identity** |
| **B3 M5b** | [m5b-smooth-action-limit.md](m5b-smooth-action-limit.md): smooth \(C^3\) action Riemann \(O(h)\) sketch; **not** Γ |

**Accepted next:**

1. Paper draft using OUTLINE + CLAIM_GATE on every section.  
2. Optional: multi-region lattice of gates (export currents); M10 correlation study (non-identity already enough).  
3. Optional: promote M5b sketch to fully written lemma with explicit constants.

**Rejected:** Continuum \(L\) from discrete fits; \(H_c^{\mathrm{toy}}\equiv S_c\); Γ-convergence; residual dual restart; Einstein-from-coupled-regions.

---

### 2026-07-15 — D13 relationships: composition + Landauer + warm-up/PM

**Context:** User asked for theory advance via new conclusions and validation against existing theories. Parallel R1/R2/R3a.

**Decision D13 — Record three constructive relationships; freeze as Stage-1 / Layer-W advances.**

| Track | Outcome |
|-------|---------|
| **R1 Composition** | [m11d-composition-laws.md](m11d-composition-laws.md) · `m11_composition_ledger.py`: Markov export additivity; DPI; **path-dependent** \(\sum L_S\) (same \(H(Z)\), gap \(1\) bit); \(L_E\) additive; \(L_B\) non-additive |
| **R2 Landauer** | [m11e-landauer-export.md](m11e-landauer-export.md) · `m11_landauer_and_ledger.py`: \(Q\ge k_BT\ln 2\cdot H(X\mid Y)\); single-shot \(L_S=H(X\mid Y)\) in bit units; reversible garbage parks export |
| **R3a Warm-up/PM** | [m5c-warmup-pm-gradient-flow.md](m5c-warmup-pm-gradient-flow.md) · `m5c_pm_energy_descent.py`: PM = discrete GD of matched energy \(E_h\); \(E=-(K^2/2)S\); Layer D residual dual not continuum relative entropy |

**New conclusions (allowed form):**

1. Discrete load is **path-dependent** and not a function of final \(H_c\) alone.  
2. Export / \(L_S\) is the object **Landauer bounds** in a standard AND-erasure protocol.  
3. Layer W: joint-toy PM is **energy descent** for the warm-up energy matched to PM conductivity; external continuum PM = GfE warm-up flow (cited).

**Rejected:** Continuum \(L\) from composition; gravity from Landauer; ME⇔GfE from PM descent; \(H_c^{\mathrm{toy}}\equiv S_{\mathrm{GfE}}\).

**Accepted next:** Paper draft with R1–R3 paragraphs; optional R4a no-go promotion dictionary; optional multi-region lattice.

---

### 2026-07-15 — D14 first program paper draft + R4a no-go

**Context:** User directed proceed with paper draft under CLAIM_GATE (default post-D13).

**Decision D14 — Land first complete program draft; freeze R4a next-order no-go as companion.**

| Track | Outcome |
|-------|---------|
| **Paper draft** | [`papers/06-synthesis/DRAFT.md`](../papers/06-synthesis/DRAFT.md) (~12k words): Parts 0–8 |
| **R4a** | [m6d-promotion-nogo.md](m6d-promotion-nogo.md): next-order identity needs promotion of clock terms into metric EOM |
| **Gate** | Written under CLAIM_GATE / CURRENT_CLAIMS |

**Accepted next:** Human edit pass; optional LaTeX; optional multi-region lattice.

**Rejected:** Residual dual restart; treating DRAFT as GR-level final theory.

---

### 2026-07-15 — D15 conclusion freeze + FINAL program report

**Context:** User requested execution of all conclusion-freeze suggestions and a final paper draft.

**Decision D15 — Freeze program conclusions; land FINAL report v1.0.**

| Track | Outcome |
|-------|---------|
| **PROGRAM_CONCLUSIONS** | [`PROGRAM_CONCLUSIONS.md`](PROGRAM_CONCLUSIONS.md): P1–P11, W1–W6, O1–O5 |
| **FINAL paper** | [`papers/06-synthesis/FINAL.md`](../papers/06-synthesis/FINAL.md) (~14k words): Results + T1–T5 + §8 conclusions + Bibliography |
| **M5b polish** | Conditional lemma form with H1–H4 + paste-ready corollary |
| **R4a** | Already in draft; surfaced in Results P11 and §8.4 |
| **Voice pass** | Terminology / layer / path hygiene on body |

**Program cycle status:** **Closed at claim freeze** (no experimental data required).

**Accepted next (optional only):** LaTeX/figures; pure PCRH\(_b\); new cycle on O1–O5.

**Rejected:** Residual dual restart; overclaiming GR certainty.

---

### Template for future entries

```text
### YYYY-MM-DD — Title
**Context:** …
**Decision Dn — …**
**Rationale:** …
**Accepted next steps:** …
**Rejected:** …
**Success criteria:** …
**Owner / agent:** …
```

---

## 3. Dependency graph (math only)

```text
M1 (T1 residual)
 ├── M2 (T1-load)
 ├── M3 (Lyapunov)   [soft]
 └── M4 (load reparam) [soft]

M8 (Newton cleanup) ──► M7 (symbol map) ──► M6 (weak-field plug-test)

M5 (warm-up continuum)  [independent; literature assist]

M9 (Lorentzian lift)  [after M6 clarity]
M10 (S_c vs H_c)      [after M1 or channel redesign]
M11 (IDEM → H_c / L_disc)  [Phase 1–2 done — D9/D11]
M12 (true game channel) [shoe ledger exists; full EV deferred]
Paper outline           [papers/06-synthesis/OUTLINE.md — D11]
```

---

## 4. Recommendation snapshot (as of 2026-07-15, post-D15)

| If you want… | Do this next |
|--------------|--------------|
| **Default** | Read [FINAL.md](../papers/06-synthesis/FINAL.md) + [PROGRAM_CONCLUSIONS.md](PROGRAM_CONCLUSIONS.md) |
| Publish packaging | LaTeX / figures (editorial) |
| New science cycle | O1 continuum limit; M9 Lorentzian; pure PCRH\(_b\) |
| Stop | Program freeze closed D15 |

**Default recommendation:** **program cycle closed** — use FINAL as the conclusion package. New science: [OPEN_AVENUES.md](OPEN_AVENUES.md).

---

## 5. Claim freezes (until a log entry reopens them)

Do **not** state in papers or abstracts, without a new decision entry:

1. Master equation derived from / equivalent to Bianconi GfE.  
2. T1 / T1′ residual domination is a **pure** theorem (hybrid on \(I_\star\) is OK if labeled).  
3. Weak-field constants matched across frameworks.  
4. Blackjack dual proves game entropy = GfE or implies edge.  
5. External GfE papers are established on par with GR.  
6. Newtonian Poisson from pointwise \(\Phi\propto\rho\) Laplacian (withdrawn).  
7. Next-order \(\gamma_L,\delta_L\) equal GfE \(\Lambda_G,D_{\mu\nu}\) (structural mismatch).  
8. Ultra-short-time residual dual without T1′ window \([t_{\min},t_{\max}]\).  
9. \(R_{\mathrm{PM}}\le R_{\mathrm{Neu}}+R_{\mathrm{interface}}\) with thin interface majorant alone.

Allowed (per transfer dictionary + D3): constructive Euclidean dual; Path J/M calibrated Newton; experimental T1′ window; preliminary supporting literature; open continuum program.

---

*Append new dated sections; do not rewrite history — strike decisions only by a later entry that supersedes them.*
