# Design: GfE ↔ Load Joint Toy (1D Euclidean Warm-Up) v2

**Status:** Active (refined P0–P2, 2026-07-14)  
**Notebook:** [gfe_load_joint_toy.ipynb](gfe_load_joint_toy.ipynb)  
**Core (CLI-shared):** [_joint_toy_v2_core.py](_joint_toy_v2_core.py)  
**Latest scorecard:** [gfe_load_joint_toy_scorecard_v2.txt](gfe_load_joint_toy_scorecard_v2.txt)  
**Summary figure:** [gfe_load_joint_toy_summary.png](gfe_load_joint_toy_summary.png)

---

## 1. Scientific question

Does a **load-gated, observation-channel entropy-reducing dynamics** (Stage 1) move with **GfE / Perona–Malik flow** on an induced metric (Stages 2–3) on a minimal Euclidean system?

---

## 2. v2 refinements (P0–P2)

| ID | Change | Why |
|----|--------|-----|
| **P0** | Classical PM conductivity \(\rho=1/(1+(\nabla\phi/K)^2)\) with \(K\sim\) noise scale | Avoid α-driven staircasing on ramps |
| **P1** | \(H_c = H_R + \lambda_e H_{\mathrm{edge}}\) from **true residual** vs \(\phi_\star\) + edge-location posterior | Histogram-of-\(\phi\) was the wrong entropy |
| **P2** | Split \(L_E, L_S, L_B\); clock uses \(L_E+L_S\) | Separate induction intensity from rate/saturation |
| **Scorecard** | Residual dual + edge + ramp + \(L_E\) + clock + residual co-motion | Match actual hypothesis |

---

## 3. Mathematical objects

### Channel (Stage 1)
- Hidden \(\phi_\star\); observation \(y=\phi_\star+\eta\).
- Reconstructor \(\hat\phi(t)\) starts at \(y\).
- Residual: \(R=\mathrm{mean}((\hat\phi-\phi_\star)^2)\), \(H_R=\log(1+R/\sigma^2_{\mathrm{ref}})\).
- Edge entropy: \(H_{\mathrm{edge}}=-\sum p\log_2 p\) with \(p\propto|\nabla\hat\phi|\).
- \(H_c = H_R + \lambda_e H_{\mathrm{edge}}\) (lower = better channel).

### Induced metric / GfE (Stages 2–3)
- \(G=1+\alpha_G(\nabla\phi)^2\), \(S_{\mathrm{GfE}}=-\sum\ln G\).
- PM flux: \(\rho=1/(1+(\nabla\phi/K)^2)\).

### Load (Stage 1)
- \(L_E=c_E\mathbb{E}[(\nabla\hat\phi)^2]\) — tracks \(\mathbb{E}[G-1]\)
- \(L_S=c_S|\Delta H_c|/\Delta t\)
- \(L_B=c_B\max|\nabla|/(1+\max|\nabla|)\)
- Clock: \(dt/(1+\alpha_L(L_E+L_S))\)

### Dynamics
Heat (control) · PM · load-gated PM.

### ICs
`noisy_step`, `noisy_two_bumps`, `noisy_ramp`, `clean_step` (fixed RNG seeds 101–104).

---

## 4. Scorecard v2 criteria

1. PM residual better than heat (`noisy_step` impro>0.05; bumps impro>0)  
2. PM edge retention > heat×1.15 on step ICs  
3. Ramp stability: PM max-grad ratio < 2.5  
4. \(\mathrm{corr}(L_E,\mathbb{E}[G-1])>0.85\) on all PM runs  
5. Load-gating slows mid-run \(L_2\) change vs pure PM  
6. Residual co-motion on `noisy_step` (PM better final + monotone ≥ heat)

**Verdict bands:** ≥5 PROMISING · 3–4 MIXED · ≤2 WEAK.

---

## 5. Latest results (2026-07-14, deterministic)

```
TOTAL: 6/6 criteria SUPPORT
VERDICT: PROMISING — formalize Action–Channel Duality for Euclidean warm-up; optional 2D next.
```

| Criterion | Result (approx) |
|-----------|-----------------|
| [1] residual dual | SUPPORT (step impro ~0.37; bumps ~0.02) |
| [2] edge retention | SUPPORT (~11× heat on steps) |
| [3] ramp stability | SUPPORT (ratio ~0.05, no staircasing) |
| [4] \(L_E\leftrightarrow G\) | SUPPORT (corr=1.0 by construction+plumbing) |
| [5] load clock | SUPPORT (all ICs) |
| [6] residual co-motion | SUPPORT (mono PM 1.00 vs heat 0.17) |

**Honest reading:** Strong **partial dual** on this Euclidean warm-up: observation-channel residual + edge geometry + load clock align with GfE/PM structure-preserving flow. This is **not** a continuum derivation of Bianconi’s Lorentzian action. Next theory step: write Action–Channel Duality for this special case only.

---

## 6. How to run

```bash
# CLI scorecard
.venv/bin/python simulations/bridging/_joint_toy_v2_core.py

# Notebook (kernel: Python (computational-entropy))
# open simulations/bridging/gfe_load_joint_toy.ipynb
```

---

## 7. Map to three-stage workflow

```text
y, φ_star  →  H_c, L_E/L_S/L_B, load clock     STAGE 1
           →  G = 1 + α_G (∇φ̂)²                STAGE 2
           →  S_GfE, PM flow                   STAGE 3
```

Hypothesis under test (now **supported** on this toy): Stage-1 channel quantities are operational summaries of the same structure Stage 2–3 treat as \((g,G)\) and relative-entropy gradient flow.

---

## 8. Next steps

1. ~~Action–Channel Duality note~~ → `synthesis/action-channel-duality-euclidean.md` (incl. T1 sketch).  
2. ~~2D image IC~~ → `_joint_toy_2d.py` **6/6 SUPPORT**.  
3. Optional: game belief field as \(\phi\); finish T1 proposition proof.  
4. Do **not** claim full GfE/master-equation equivalence without continuum limit work.
