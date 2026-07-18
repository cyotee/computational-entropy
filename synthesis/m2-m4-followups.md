# M2–M4 Follow-ups After M1 (Status)

**M-ids:** M2, M3, M4  
**Depends on:** [m1d-lemma-e-prime.md](m1d-lemma-e-prime.md) · [m2-t1-load.md](m2-t1-load.md) · [t1-residual-domination.md](t1-residual-domination.md)  
**Date:** 2026-07-14 (updated after M2 hybrid)

---

## M1 input used here

- Strict T1 on \((0,t_\star]\) has **short-time obstruction** (heat wins residual race).  
- **T1′** hybrid residual dual on \(I_\star\subset[1.2,1.67]\) (M1d).  
- Lemma **C′2♯** analytic persistence through \(T_{\mathrm{pers}}^\sharp\approx 1.67\).

---

## M2 — T1-load (load-gating vs heat)

**Statement:** For wall-clock \(t\in I_\star\), \(\mathbb{E} R_{\mathrm{load\text{-}PM}}(t)\le\mathbb{E} R_{\mathrm{heat}}(t)\).

**Status:** **Hybrid established** — see [m2-t1-load.md](m2-t1-load.md).  
Time-change lemma closed; residual comparison MC-certified on \(I_\star\) (\(\tau/t\approx 0.95\)). Pure deduction from T1′ + monotonicity still open.

**What it tells us:** Load clock preserves channel dual vs heat (master-equation form contact at toy level).

---

## M3 — Lyapunov (T2)

**Statement:** Exist \(\mathcal{L}_{\mathrm{ch}}(\hat\phi,\phi_\star)\) decreasing along PM on the C′ event, controlling edge energy.

**Status:** **Still deferred open.** Residual \(R\) is a candidate on intermediate \(t\) but fails as global Lyapunov for ultra-short \(t\).

**Rationale:** Short-time heat win shows \(R\) alone is not monotone-superior for all \(t>0\); need hybrid Lyapunov (noise energy + edge blur penalty).

---

## M4 — Load reparameterization theorem (T3)

**Statement:** Load-gating is a monotone time change preserving descent of \(\mathcal{L}_{\mathrm{ch}}\).

**Status:** **Structural half done** (M2-τ). Full theorem deferred until M3 picks \(\mathcal{L}_{\mathrm{ch}}\).

---

## Summary table

| ID | Status after M2 hybrid | Next action |
|----|------------------------|-------------|
| M2 | **Hybrid done** | Optional pure bridge from T1′ |
| M3 | Open / deferred | Design hybrid Lyapunov using T1′ window |
| M4 | Structural half open full | After M3 |

**Non-claim:** M3–M4 not proved; M2 is hybrid, not pure theorem.
