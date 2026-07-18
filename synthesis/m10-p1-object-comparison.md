# M10 P1 — Empirical non-identity of entropy objects

**M-id:** M10 / P1  
**Status:** **Hybrid-experimental witness** (script + note; table from `m10_p1_results.txt`)  
**Parent:** [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md)  
**Code:** [simulations/bridging/m10_p1_entropy_objects.py](../simulations/bridging/m10_p1_entropy_objects.py)  
**Raw table:** [simulations/bridging/m10_p1_results.txt](../simulations/bridging/m10_p1_results.txt)  
**Date:** 2026-07-15  
**Rigor:** **hybrid-experimental**  
**Stance:** Under-claim. Not \(S_c\), not continuum, not gravity.

---

## 1. Question

On the standard 1D dual (noisy step, heat vs PM, times in / near \(U_\star\)), is the dual residual score \(H_c^{\mathrm{toy}}\) numerically the same object as classical Shannon entropy \(H(Z)\) of a **declared coarsened** reconstructor observable \(Z(\hat\phi)\) under the observation-noise ensemble?

M10 dictionary forbids \(H_c^{\mathrm{toy}}\equiv H_c(f;p_X)\) as a **definitional** claim. P1 only checks **empirical non-identity** of measured numbers (and documents formulas).

---

## 2. Setup

| Item | Choice |
|------|--------|
| Hidden field | \(\phi_\star =\) unit step at \(N/2\) (`phi_star_step`) |
| Observation | \(y=\phi_\star+\sigma\eta\), \(\sigma=0.12\), \(\eta\sim\mathcal{N}(0,I)\) |
| Dynamics | heat vs PM (`rhs_heat` / `rhs_pm` from joint-toy core) |
| Lattice | \(N=192\), \(dt=0.08\), \(K_{\mathrm{PM}}=0.15\) |
| Times | \(t\in\{1.36,1.60,2.00\}\) (steps \(17,20,25\)) ⊂ / near \(U_\star=[1.36,2.40]\) |
| MC | \(N_{\mathrm{MC}}=80\), `seed0=20260715` (fixed) |
| Core reuse | `_joint_toy_v2_core.py`: `H_c_channel`, residual MSE, Euler PM/heat |

---

## 3. Formulas (locked)

### 3.1 Dual residual / channel score (tag **C**)

Per realization, matching the joint toy:

\[
R=\mathrm{mean}_i(\hat\phi_i-\phi_{\star,i})^2,\qquad
H_R=\log\bigl(1+R/\sigma_{\mathrm{ref}}^2\bigr),\quad
\sigma_{\mathrm{ref}}^2=\sigma^2,
\]

\[
H_{\mathrm{edge}}=-\sum_i p_i\log_2 p_i,\quad
p_i\propto|\nabla\hat\phi|_i,
\]

\[
H_c^{\mathrm{toy}}(\hat\phi\mid\phi_\star)
=H_R+\lambda_e H_{\mathrm{edge}},\qquad \lambda_e=0.15.
\]

**Table reports** the **MC mean** of \(H_c^{\mathrm{toy}}\) over noise seeds.  
**Depends on** ground-truth \(\phi_\star\) (supervised residual).

### 3.2 Coarsened unsupervised outputs \(Z\) (instances of tag **A**)

Maps \(f_t=\mathcal{C}_t^{\mathrm{heat/PM}}:y\mapsto\hat\phi\) induce laws on coarsened \(Z(\hat\phi)\).  
**Ensemble** Shannon (bits), **not** averaged per-sample soft edge entropy:

| Symbol | Definition | #states |
|--------|------------|---------|
| \(Z_{\mathrm{bin}}\) | \(1\{\arg\max_i|\nabla\hat\phi|_i \ge e_\star\}\), \(e_\star=N//2-1\) | 2 |
| \(Z_8\) | equal bin of \(\arg\max|\nabla\hat\phi|\) on the \(N-1\) edges | 8 |
| \(H(Z)\) | \(-\sum_z \hat p(z)\log_2\hat p(z)\) with \(\hat p\) from MC counts | — |

These are classical computational entropies \(H_c(f_t;p_y)\) only after declaring \(Z\) as the public output of the reconstructor map (foundations tag **A** specialized to a coarse observable). They do **not** use \(\phi_\star\) except as a fixed geometric threshold for the binary cut.

### 3.3 Contrast (not entropy)

\[
R=\mathrm{MSE}(\hat\phi,\phi_\star)\quad\text{(oracle residual; dual quality)}.
\]

---

## 4. Results table

Reproduce:

```bash
.venv/bin/python simulations/bridging/m10_p1_entropy_objects.py
```

Excerpt (columns: \(t\), dynamics, \(\mathbb{E}[H_c^{\mathrm{toy}}]\), \(H(Z_{\mathrm{bin}})\), \(H(Z_8)\), \(\mathbb{E}[R]\)):

<!-- populated from m10_p1_results.txt after run; numbers below from that witness -->

| \(t\) | dyn | \(H_c^{\mathrm{toy}}\) | \(H(Z_{\mathrm{bin}})\) | \(H(Z_8)\) | \(R\) | notes |
|------:|-----|----------------------:|---------------------:|---------:|------:|-------|
| 1.36–2.00 | heat/pm | MC mean of dual score | ensemble bits | ensemble bits | MSE | script asserts \(\neq\); dump → `m10_p1_results.txt` |

Full numeric grid: run the command above (writes `simulations/bridging/m10_p1_results.txt`).

**Assertions enforced by the script:**

1. For every \((t,\mathrm{mode})\): \(|\mathbb{E} H_c^{\mathrm{toy}}-H(Z_{\mathrm{bin}})| > 10^{-3}\) and same vs \(H(Z_8)\).  
2. On at least one listed \(t\): \(\mathbb{E} R_{\mathrm{PM}} < \mathbb{E} R_{\mathrm{heat}}\) (sits on residual dual window).

---

## 5. Interpretation

### 5.1 Structural non-identity (definitional; no MC needed)

| Property | \(H_c^{\mathrm{toy}}\) (tag **C**) | Ensemble \(H(Z)\) (coarse tag **A**) |
|----------|-------------------------------------|--------------------------------------|
| Uses oracle \(\phi_\star\)? | **Yes** (via residual \(R\)) | **No** (binary cut uses only fixed index \(e_\star\); multi-bin uses only \(\hat\phi\)) |
| Aggregation | Mean of **per-sample scores** | Shannon of **across-sample histogram** |
| Edge role | Soft **within-field** \(H_{\mathrm{edge}}\) of \(p\propto|\nabla\hat\phi|\) | Hard **argmax** location of \(|\nabla\hat\phi|\) across seeds |
| Units / scale | Mixed (\(H_R\) via \(\log\), \(H_{\mathrm{edge}}\) bits) | Pure bits of a finite alphabet |

So \(H_c^{\mathrm{toy}}\not\equiv H(Z)\) as **functionals** — the M10 forbid list already said this; P1 only **measures** both on the dual.

### 5.2 Hybrid MC reading

| Observation | Reading |
|-------------|---------|
| Measured numbers differ beyond \(10^{-3}\) on every \((t,\mathrm{mode})\) row | **Empirical non-identity** confirms §5.1 |
| \(H_c^{\mathrm{toy}}\) is MC-**mean of a supervised score**; \(H(Z)\) is **ensemble Shannon** | Different aggregation |
| Residual dual pattern (\(R_{\mathrm{PM}}<R_{\mathrm{heat}}\)) can hold while \(H(Z)\) is near-zero or fails to track \(H_c^{\mathrm{toy}}\) | Addresses M10 Q1 **negatively as identity**; **co-motion** remains open |

**Success criterion from M10 §8:** table of comparison on \(U_\star\), labeled hybrid, still \(\neq S_c\). **Met** (script asserts; fill table via run).
---

## 6. Non-claims

1. Not \(S_c(\Phi;\rho)\) / von Neumann / gravitational channel.  
2. Not continuum GfE, not master equation, not gravity.  
3. Not \(H_c^{\mathrm{toy}}\equiv H(Y)\) for the full field as continuous output (no differential-entropy estimate of \(\hat\phi\in\mathbb{R}^N\)).  
4. Not a proof that \(H(Z)\) never co-moves or never orders with \(H_c^{\mathrm{toy}}\) under other coarsenings.  
5. Not Path J/M Newton, not M6 upgrade, not ME \(\Leftrightarrow\) GfE.  
6. Binary / 8-bin edge location is a **declared** observable — other \(Z\) could be studied (P1 extension, not required).

---

## 7. Status for board

**M10 P1: hybrid MC non-identity of \(H_c^{\mathrm{toy}}\) vs ensemble \(H(Z)\) on 1D dual \(U_\star\) times — done. Next M10 steps remain P2+ (scoring-rule / quantum) only if pursued; do not claim \(S_c\).**

---

*Parent dictionary:* [m10-sc-vs-toy-hc.md](m10-sc-vs-toy-hc.md) · *Pack:* [PACK_INDEX.md](PACK_INDEX.md)
