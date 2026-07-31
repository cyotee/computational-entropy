# PRD — Rebuild the load constants on a dimensionally-consistent footing

**Status:** Active PRD (written 2026-07-31) · Preliminary research
**Owner:** cyotee
**Motivation:** Stage 2 of the regime program ([REGIME_PROGRAM_dSc_decoupling.md](REGIME_PROGRAM_dSc_decoupling.md)) found that the master equation's calibration \(\alpha\beta=4\pi G/c^4\) is **dimensionally inconsistent** with dimensionless \(\alpha,\beta,L\), so the observable \(\alpha\gamma\) is not fixed by the theory. This PRD scopes the work to put the load \(L\) and its constants on a consistent footing — or to prove they cannot be, which is itself a result.
**Canonical target:** [../emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) · **Guardrails:** [../synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md)

---

## 1. End goal (one paragraph)

Produce a **dimensionally-consistent, physically-grounded reconstruction** of the load
\[
L(\rho,g)=\beta\frac{E[\rho]}{V\epsilon_0}+\gamma\Big|\frac{dS_c}{d\tau}\Big|_{\rm reg}+\delta\frac{S_{\rm boundary}}{S_{\rm BH}},\qquad d\tau=\frac{dt}{1+\alpha L},
\]
in which (i) every term is genuinely dimensionless, (ii) the Newtonian-limit calibration is written as a dimensionally valid condition, and (iii) the observable \(\alpha\gamma\) is **determined** (a number or a bounded expression), then fed back to the regime program's Stage 2/3. If no consistent assignment exists without abandoning locality or adding structure, deliver a **precise no-go** instead. Either outcome closes the Stage-2 blocker.

## 2. Background — the two problems Stage 2 exposed

1. **Dimensional inconsistency.** \(L\) is declared dimensionless (type safety), so \(\alpha,\beta,\delta\) are dimensionless and \(\gamma\) has units of **time** (to make \(\gamma\,|dS_c/d\tau|\) dimensionless). Then \(\alpha\beta\) is dimensionless while \(4\pi G/c^4\) is dimensionful — the calibration cannot hold literally.
2. **Local-vs-nonlocal tension (suspected, must be checked).** Gravitational time dilation tracks the **nonlocal** potential \(\Phi=-GM/r\) (Poisson-sourced), whereas \(\beta E/(V\epsilon_0)\) is a **local energy density** \(\rho_E/\rho_{\rm Pl}\). A local term cannot equal \(\Phi/c^2\) pointwise — this is the same reason the repo **withdrew** the pointwise \(\Phi\propto\rho\) identity and recovers Newton only via **Path J/M** (Clausius→Einstein→Poisson). So the load's role in producing time dilation must be reconciled with Path J/M, not assumed.

These are not the same bug: (1) is bookkeeping; (2) may be structural. Both must be resolved for a consistent \(L\).

## 3. Questions to answer (the core deliverables)

- **Q1 — Dimensional audit.** Assign units to every symbol (\(E,V,\epsilon_0,S_c,\tau,S_{\rm boundary},S_{\rm BH},\alpha,\beta,\gamma,\delta\)) and produce a table proving each term is dimensionless. Confirm \(\gamma\) is a time and identify the *only* observable combinations (\(\alpha\gamma\), \(\alpha\beta/\epsilon_0\), \(\alpha\delta\)).
- **Q2 — Valid calibration.** Replace \(\alpha\beta=4\pi G/c^4\) with a **dimensionally correct** Newtonian-matching condition. What quantity does \(\alpha L\) equal at weak field, and what does that fix? (Likely \(\alpha L \to \Phi/c^2\); but \(\Phi\) is nonlocal — see Q3.)
- **Q3 — Reconcile with Path J/M / locality.** Determine whether the energy term can source time dilation locally, or whether the load must be understood as a *diagnostic* co-moving with the Path J/M metric rather than *generating* it. State explicitly what the load term does and does not do, dimensionally and structurally.
- **Q4 — Fix \(\gamma\) (or bound it).** Using the framework's own invoked bounds — Margolus–Levitin (\(\tau_{\rm ML}=\pi\hbar/2E\)), Bekenstein (\(S\le 2\pi kRE/\hbar c\)), Landauer, Lloyd — derive \(\gamma\) as a physical time (candidate: \(\gamma\sim\hbar/E\), the ML time the regularization already uses), consistently with Q1–Q2. Compute \(\alpha\gamma\).
- **Q5 — Feed back to observability.** Plug the resulting \(\alpha\gamma\) into `regime_gamma_calibration.py` and state whether the dephasing clock effect is now (a) fixed and unmeasurable, (b) fixed and measurable, or (c) still irreducibly free.

## 4. Tasks / phases

```
P1  Dimensional audit (Q1)                         -> units table + observable combinations
P2  Valid Newtonian calibration (Q2)               -> corrected matching condition
P3  Locality reconciliation (Q3)                   -> load: generator vs diagnostic; Path J/M tie
P4  gamma from bounds (Q4)                          -> gamma expression, alpha*gamma value
P5  Observability feedback (Q5)                     -> update Stage-2 witness + verdict
P6  Canonical update + honesty pass                -> master-equation.md, falsifiability, ledgers
```

## 5. Deliverables

- **A canonical dimensional note** — either a new `emergent-gravity/load-dimensional-analysis.md` or a revision of `master-equation.md`, containing the units table (Q1), the corrected calibration (Q2), the locality statement (Q3), and the \(\gamma\) result (Q4).
- **Updated `simulations/regime/regime_gamma_calibration.py`** using the derived \(\alpha\gamma\) (Q5), with the verdict recomputed.
- **Updated living docs:** `master-equation.md` (constants section), `FALSIFIABILITY_L_vs_GR.md` (caveat 2), `REGIME_PROGRAM` (Stage 2/3), `RESULTS_LEDGER`/`OPEN_AVENUES` O-5, `CURRENT_CLAIMS` (add/adjust the calibration claim).
- **If no-go:** a precise statement of *why* the constants cannot be consistently fixed (e.g., locality + dimensionlessness + Newtonian matching are mutually incompatible without new structure), logged as a withdrawn/impossible claim.

## 6. Definition of Done

- [ ] **D-1** Units table proves every load term dimensionless; observable combinations identified (Q1).
- [ ] **D-2** \(\alpha\beta=4\pi G/c^4\) replaced by a dimensionally valid condition, or shown impossible (Q2).
- [ ] **D-3** Explicit statement of whether the load *generates* or merely *diagnoses* time dilation, reconciled with Path J/M and the withdrawn pointwise identity (Q3).
- [ ] **D-4** \(\gamma\) derived as a physical time from ML/Bekenstein/Lloyd, or shown irreducibly free; \(\alpha\gamma\) computed/bounded (Q4).
- [ ] **D-5** Stage-2 witness updated with the derived \(\alpha\gamma\); observability verdict recomputed (Q5).
- [ ] **D-6** Canonical + living docs updated; `check_claim_hygiene.py` green; no term left dimensionally undefined.
- [ ] **D-7** If a no-go, it is stated precisely and added to the non-claims/withdrawn record.

## 7. Non-goals & guardrails

- **Do not** fabricate numerical constants to force a measurable prediction. If \(\alpha\gamma\) stays free or Planck-suppressed, report that.
- **Do not** revive the withdrawn pointwise \(\Phi\propto\rho\) Newton identity (N5); any locality claim must respect Path J/M.
- **Do not** assert a departure from GR; the default verdict remains reformulation.
- Preserve all frozen non-claims; label every result (dimensional / derived / calibration / no-go).
- A **negative result is a valid deliverable** — a clean no-go is as valuable as a consistent completion.

## 8. Risks

- **Most likely outcome:** the load's energy term cannot both be a local density *and* reproduce nonlocal gravitational dilation, so the honest resolution is "\(L\) is a diagnostic co-moving with the Path J/M metric, not its generator," and \(\gamma\) is fixed only up to the ML time — i.e. reformulation, now on firm dimensional ground. This is a **clarifying** result, not a failure.
- **Deeper risk:** making \(L\) consistent may require new structure (promoting load terms into the field equations — the R4a "promotion" theme), which changes the theory rather than repairing it. If so, document it as such and stop; do not silently redefine the master equation.

## 9. Changelog

| Date | Entry |
|------|-------|
| 2026-07-31 | PRD created: rebuild load constants dimensionally (Q1–Q5), reconcile with Path J/M/locality, fix or bound \(\alpha\gamma\); no-go is an acceptable deliverable. |
