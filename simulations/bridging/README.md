# simulations/bridging/

Experiments that connect computational entropy / load with continuum entropic-gravity ideas (especially Bianconi GfE).

## Joint toy v2: GfE warm-up ↔ observation-channel load

| Path | Description |
|------|-------------|
| [gfe_load_joint_toy.ipynb](gfe_load_joint_toy.ipynb) | Jupyter notebook (P0–P2 refined) |
| [_joint_toy_v2_core.py](_joint_toy_v2_core.py) | Shared core + CLI scorecard |
| [DESIGN_gfe_load_joint_toy.md](DESIGN_gfe_load_joint_toy.md) | Design + interpretation |
| [gfe_load_joint_toy_scorecard_v2.txt](gfe_load_joint_toy_scorecard_v2.txt) | Latest automated scorecard |
| [gfe_load_joint_toy_summary.png](gfe_load_joint_toy_summary.png) | Summary figure (`noisy_step`) |

**Latest 1D result (2026-07-14): 6/6 SUPPORT — PROMISING** (Euclidean warm-up dual).

```bash
.venv/bin/python simulations/bridging/_joint_toy_v2_core.py
.venv/bin/python simulations/bridging/_joint_toy_2d.py   # 2D lift
.venv/bin/python simulations/bridging/m10_p1_entropy_objects.py  # M10 P1 H_c^toy vs H(Z)
```

| 2D paths | Role |
|----------|------|
| [_joint_toy_2d.py](_joint_toy_2d.py) | 2D image dual CLI |
| [gfe_load_joint_toy_2d_scorecard.txt](gfe_load_joint_toy_2d_scorecard.txt) | 2D scorecard (when run) |
| [gfe_load_joint_toy_2d_summary.png](gfe_load_joint_toy_2d_summary.png) | 2D summary figure |

| Game-motivated | Role |
|----------------|------|
| [blackjack_belief_dual.py](blackjack_belief_dual.py) | Belief / count-strength \(\phi\) dual CLI |
| [DESIGN_blackjack_belief_dual.md](DESIGN_blackjack_belief_dual.md) | Design + honesty limits |
| [blackjack_belief_dual_scorecard.txt](blackjack_belief_dual_scorecard.txt) | **6/6 SUPPORT** (dual pattern only — not blackjack EV) |

**Theory:** [synthesis/action-channel-duality-euclidean.md](../../synthesis/action-channel-duality-euclidean.md) · [acd-ew-continuum-transfer.md](../../synthesis/acd-ew-continuum-transfer.md) · [t1-residual-domination.md](../../synthesis/t1-residual-domination.md) · [weak-field-gfe-vs-load.md](../../synthesis/weak-field-gfe-vs-load.md)

Kernel for notebook: **Python (computational-entropy)** / project `.venv`.

See [PRD.md](../../PRD.md).
