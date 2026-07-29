# Delivery Plan — Reformulation Split & Two-Paper Spine

**Status:** Active plan (written 2026-07-29)
**Owner:** cyotee
**Stance:** Preliminary research. Prefer under-claiming. This plan operationalizes a review-driven restructuring; it does **not** reopen the heat/PM residual dual as a crisis.
**Companion docs:** [../PROGRESS_REPORT.md](../PROGRESS_REPORT.md) · [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md) · [../synthesis/OPEN_AVENUES.md](../synthesis/OPEN_AVENUES.md)

---

## End Goal (one sentence)

Restructure the program into a **publishable solid core** (Paper A: computational entropy + Landauer-exact export ledger) and an **honest conjecture** (Paper B: emergent gravity as an information-theoretic reformulation), with every canonical document consistent with that split and free of over-claims.

**Fixed stance (decided):** The program is an *information-theoretic reformulation of thermodynamic gravity*; "new theory" status is **contingent on a falsifiable departure from GR that is currently open**. Whatever the research supports — reformulation or new theory — is an acceptable outcome.

---

## Definition of Done (program-level)

The plan is DONE when **all** of the following hold:

- [x] **D-0** No canonical file over-claims relative to `synthesis/CURRENT_CLAIMS.md`; `check_claim_hygiene.py` passes green.
- [x] **D-1** `papers/DELIVERY_SCOPE.md` exists and fixes the may-assert / must-not-assert boundary for Paper A and Paper B.
- [x] **D-2** The one-page falsifiability analysis ("does `L` predict anything GR doesn't?") exists and its verdict is recorded. → `papers/FALSIFIABILITY_L_vs_GR.md`; **verdict: reformulation + flagged entropy-production candidate departure (term 2).**
- [x] **D-3** Paper A drafted: self-contained, theorem-level, **no gravity claim**, reproducible ledgers as appendices. → `papers/01-foundations/PAPER_A_computational_entropy.md`
- [ ] **D-4** Paper B drafted: emergent gravity stated explicitly as conjecture/reformulation, Path J/M honesty intact, falsifiability question central.
- [ ] **D-5** Meta-apparatus consolidated into one results ledger; ACD-EW dual thread marked closed (archived, not deleted, with user sign-off).
- [ ] **D-6** Bootstrap/living docs (`PROGRESS_REPORT.md`, `CURRENT_CLAIMS.md`, `THEORY.md`, `PACK_INDEX.md`, `CLAUDE.md` read-order) point at the new two-paper spine.

---

## Guiding principle

Split the program into a **solid core** (proven, publishable now) and a **conjecture** (honest, forward-looking); then make every canonical doc consistent with that split. Extract what is done, label what is open, prune the bookkeeping that has outgrown the results.

---

## Phases

Dependency order:

```
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 (Paper A) ──┐
                             └────► Phase 4 (Paper B) ──┴─► Phase 5 (prune)
```

### Phase 0 — Reconcile claims (fast, unblocks everything)

Mechanical, reversible, removes the one live inconsistency.

- [x] Soften the closing paragraph of `emergent-gravity/master-equation.md` ("recovers Newtonian gravity, Schwarzschild… inflation… unifies Jacobson, Verlinde, Susskind, Lloyd") to match `CURRENT_CLAIMS.md`: master equation is a **Jacobson-shaped postulate**; Newton via **Path J/M only**; everything else is aspiration, not recovery.
- [x] Add a one-line positioning banner to the canonical files + `PRD.md`: *"Reformulation unless/until a falsifiable departure from GR is constructed (open)."*
- [x] Re-run `.venv/bin/python simulations/classical/check_claim_hygiene.py` → OK.

**DoD:** D-0. Addresses review points #2 (framing), #3.

### Phase 1 — Define the two-paper split (scope contract)

Write `papers/DELIVERY_SCOPE.md` fixing what each paper may/may not assert **before** drafting either.

| | Paper A — "solid core" | Paper B — "conjecture" |
|---|---|---|
| Thesis | Computational entropy = output-distribution entropy; load/export ledger is Landauer-exact and path-dependent | Emergent gravity as information-theoretic reformulation; a **hypothesis**, not a recovery |
| Contains | `H_c`/`S_c` defn; `L_S = H(X\|Y)` = Landauer erased bits; `ΣL_S` path-dependence; invariant framing via `I(X;Y)` | Master equation as postulate; Path J/M honesty; falsifiability question; ACD-EW as analogy only |
| Rigor | Theorem-level, self-contained, **no gravity claim** | Explicitly labeled conjecture/open; cites Paper A |
| Status | Publishable now | Position paper / research programme |

- [x] `papers/DELIVERY_SCOPE.md` written and cross-linked.

**DoD:** D-1. Addresses your decision to segment; review point #1.

### Phase 2 — Gating falsifiability analysis (one page)

- [x] Write "Does `L` predict anything GR doesn't?" (short). → `FALSIFIABILITY_L_vs_GR.md`
- [x] Record verdict: **REFORMULATION**, with the entropy-production term (2) flagged as the single candidate departure (bucket B→C); term (1) reproduces GR by calibration, term (3) only bites near horizons.

**DoD:** D-2. Addresses review point #2; your decision #1 (either outcome acceptable).

### Phase 3 — Draft Paper A (the part that's done)

- [x] Extract from `foundations/computational-entropy/definition.md` + M11 ledgers.
- [x] Tighten the continuous case: lead with **mutual information / relative entropy** as the coordinate-invariant carrier of "information imparted"; keep differential entropy illustrative only (fixes the negative-`H_c` interpretation gap). → §6 + §1.1 caveat
- [x] Include executable ledgers (`m11_and_gate_ledger.py`, composition, Landauer) as reproducible appendices. → Appendix R

**DoD:** D-3. Addresses review point #6; your decision #3.

### Phase 4 — Draft Paper B (the conjecture)

- [ ] Master equation stated as Jacobson-shaped postulate; Newton = Path J/M with calibration honestly flagged.
- [ ] Fold in Phase 2's verdict as the central open question.
- [ ] Optional constructive seed (**O1**): single-slot (`L_S`) continuum-limit sketch, presented as "first step / open," not closed.

**DoD:** D-4. Addresses your decision #3 (conjecture paper); the "close O1's first step" suggestion.

### Phase 5 — Prune & consolidate (last, deliberately)

Only after A and B have mined the synthesis corpus.

- [ ] Collapse parallel numbering (M/D/P/O/W, tags A–E) into **one results ledger**: *proved / rigor-label / open*.
- [ ] Mark the ACD-EW / heat-vs-PM dual thread **closed** (Perona–Malik is prior art; gravity payoff is analogy). **Archive, do not delete — confirm with user before any bulk move** (per repo agent rule 7).
- [ ] Update `PROGRESS_REPORT.md`, `CURRENT_CLAIMS.md`, `THEORY.md`, `PACK_INDEX.md`, and `CLAUDE.md` read-order to point at the two-paper spine.

**DoD:** D-5, D-6. Addresses review points #4, #5.

---

## Non-goals (explicit)

- Not reopening the heat/PM residual dual as a crisis.
- Not asserting master equation ⇔ continuum GfE, `L ≡ G`, or IDEM → continuum `L`/`G` (frozen non-claims N1–N9 stand).
- Not deleting historical material; archive with sign-off only.

---

## Progress log

| Date | Phase | Entry |
|------|-------|-------|
| 2026-07-29 | — | Plan created from review dialogue; stance fixed as reformulation-contingent-on-falsifiability. |

*Update the checkboxes and this log as phases complete. The plan is DONE when all D-0…D-6 boxes are checked.*
