# Design: Blackjack / Game Belief-Field Dual (ACD-EW extension)

**Status:** Preliminary experiment (2026-07-14)  
**CLI:** [blackjack_belief_dual.py](blackjack_belief_dual.py)  
**Scorecard:** [blackjack_belief_dual_scorecard.txt](blackjack_belief_dual_scorecard.txt)  
**Math core (reused):** [_joint_toy_v2_core.py](_joint_toy_v2_core.py)  
**Theory scope:** [synthesis/action-channel-duality-euclidean.md](../../synthesis/action-channel-duality-euclidean.md) — **Euclidean warm-up only**  
**PRD pointer:** optional game belief field as \(\phi\) (Next C / pending)

---

## 1. What this is (and is not)

| Is | Is not |
|----|--------|
| Same **Action–Channel Duality (Euclidean warm-up)** pattern as the joint toy | A full blackjack engine or multi-deck shoe sim |
| A **game-motivated IC** for \(\phi\): belief / true-count / edge strength | A proof of player edge or optimal strategy |
| Residual + edge + load-clock scorecard on that IC | A derivation of continuum GfE or Lorentzian gravity |
| Bridge from classical **computational-entropy games** thread to ACD-EW | A claim that card counting “is” gravitational load |

**Tone:** exploratory constructive check — *does the dual still read sensibly when \(\phi\) is labeled as a belief field?*

---

## 2. What \(\phi\) means

On a 1D lattice of \(N=192\) bins:

- **Index \(i\)** (comment-level only): deck **penetration** or successive **info bins** as cards are seen. Low \(i\) = early shoe; high \(i\) = deep penetration. The continuum equation does not encode shoe composition — only the dual’s Euclidean 1D structure.
- **\(\phi(i)\)**: scalar **belief / count-strength / edge-strength** at that bin (normalized \(\sim[0,1]\) in the ICs).
- **\(\phi_\star\)**: idealized **true** edge profile (hidden structure the channel should recover).
- **\(y\)**: **noisy observation** of that profile — imperfect count, sampling noise, or coarse belief (not a full Hi-Lo running-count path).

### True structures used

| IC name | Shape | Game flavor |
|---------|--------|-------------|
| `noisy_high_count` | Step at mid-lattice | High-count region appears only past a threshold |
| `noisy_two_windows` | Two bumps | Two favorable windows in a shoe |
| `noisy_edge_ramp` | Smooth tanh ramp | Gradual accumulation of count info |
| `clean_high_count` | Clean step | Edge retention without observation noise |

Dynamics and \(H_c\) are **identical** to joint toy v2 (import from `_joint_toy_v2_core`).

---

## 3. What \(H_c\) is

Same operational channel entropy as joint toy v2:

\[
H_c(\hat\phi;\phi_\star)
  = H_R + \lambda_e H_{\mathrm{edge}},
\]

- \(R = \mathrm{mean}((\hat\phi-\phi_\star)^2)\), \(H_R=\log(1+R/\sigma^2_{\mathrm{ref}})\) — residual vs **true** edge profile.
- \(H_{\mathrm{edge}} = -\sum p\log_2 p\), \(p\propto|\nabla\hat\phi|\) — how “spread” the reconstructed edge locations are.
- Lower \(H_c\) = better reconstructor (less residual, less smeared edge mass).

**Interpretation in game language:** \(H_c\) is **not** “Shannon entropy of the next card” from the research/games blackjack notes. It is the **channel residual + edge posterior** of the dual toy, applied to a field that *looks like* count/edge strength. Classical game \(H_c\) (output entropy of strategy maps) remains a **separate** microstructure thread; this experiment only asks whether that field can sit in the **same dual pattern**.

---

## 4. Dynamics and load clock

| Mode | Role |
|------|------|
| `heat` | Control: blur everything, including the high-count jump |
| `pm` | Structure-preserving reconstructor (Perona–Malik) |
| `load_pm` | PM with \(dt/(1+\alpha_L(L_E+L_S))\) |

Load split (unchanged):

- \(L_E \propto \mathbb{E}[(\nabla\hat\phi)^2]\) — induction intensity; tracks \(\mathbb{E}[G-1]\)
- \(L_S \propto |\Delta H_c|/\Delta t\) — rate of channel improvement
- \(L_B\) — gradient saturation (diagnostic; not in clock)
- Clock uses \(L_E+L_S\) only

Induced metric / GfE warm-up action: \(G=1+\alpha_G(\nabla\phi)^2\), \(S_{\mathrm{GfE}}=-\sum\ln G\).

---

## 5. What “success” means

Success is **scorecard SUPPORT on the dual criteria**, not EV at the table:

1. **Residual impro:** PM ends with lower residual vs \(\phi_\star\) than heat on primary (+ secondary) ICs.  
2. **Edge retention:** PM keeps the high-count jump sharper than heat.  
3. **Ramp stability:** gradual edge ramp does not staircase under PM.  
4. **\(L_E\leftrightarrow G\):** load intensity tracks induced metric (near-definitional plumbing).  
5. **Load slows:** load-gated PM changes less by mid-run than pure PM.  
6. **Co-motion:** residual improves under PM with good monotonicity on primary IC.

**Verdict bands:** ≥5 PROMISING · 3–4 MIXED · ≤2 WEAK — same as joint toy; MIXED is acceptable and should be reported honestly.

---

## 6. Link to games thread and ACD-EW

```text
research/games/black-jack/     classical computational entropy of strategies
        │                      (counts, predictive accuracy, ROI notes)
        ▼
   belief / edge field φ       (this scaffold: 1D proxy, not full engine)
        │
        ▼
   ACD-EW joint dual           heat vs PM + H_c residual + L_E/L_S clock
        │
        ▼
synthesis/action-channel-duality-euclidean.md
   Euclidean warm-up only — not Lorentzian GfE
```

**Claim wording (careful):**  
“The same Euclidean Action–Channel Duality pattern used on image-like \(\phi\) can be run on a **game-motivated belief/count-strength field**, with residual and edge criteria that are meaningful under that labeling.”

**Does *not* claim:** counting systems equal gravity; \(L\) equals bankroll risk; IDEM/lambda microstructure is embedded; continuum GfE.

---

## 7. How to run

```bash
.venv/bin/python simulations/bridging/blackjack_belief_dual.py
# writes simulations/bridging/blackjack_belief_dual_scorecard.txt
```

Fixed RNG seeds **201–204** (deterministic). Imports dynamics from `_joint_toy_v2_core` so numbers stay comparable to joint toy v2 when ICs match geometrically.

---

## 8. Honesty about limits

1. **No shoe:** no 52-card multiset, no Hi-Lo integer running count, no betting schedule.  
2. **\(\phi_\star\) is hand-designed** (step/ramp/bumps), not fitted from casino data.  
3. **\(H_c\) here ≠ game predictive log-loss** in the blackjack analysis markdowns.  
4. **Scorecard can be MIXED** and still be a useful documentation of scope.  
5. **Scope remains ACD-EW:** 1D flat Euclidean dual toy — same ceiling as joint toy / 2D image lift.

---

## 9. Map to three-stage workflow

```text
y, φ_star (belief)  →  H_c, L_E/L_S/L_B, load clock     STAGE 1
                    →  G = 1 + α_G (∇φ̂)²                STAGE 2
                    →  S_GfE, PM flow                   STAGE 3
```

Hypothesis under test: Stage-1 channel quantities remain operational summaries of Stage 2–3 structure when the IC is **labeled** as a game belief field. Result lives in the scorecard file after each run.
