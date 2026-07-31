# simulations/regime/ — decoupling-regime witnesses

Experiments for the **regime program** ([papers/REGIME_PROGRAM_dSc_decoupling.md](../../papers/REGIME_PROGRAM_dSc_decoupling.md)):
does the load's entropy-production term \(\gamma\lvert dS_c/d\tau\rvert\) decouple
from stress-energy, or is it reabsorbable into the energy term (a reformulation)?

| Script | Stage | What it shows |
|--------|-------|---------------|
| `regime_decoupling_witness.py` | 1 | Open-qubit Lindblad model. **R1 pure dephasing:** \(E\) fixed, \(S_c\) rises, coupling \(\kappa=\lvert dE/dt\rvert/\lvert dS_c/dt\rvert\approx0\) → **decoupled**. **R2 amplitude damping:** \(\kappa\approx0.42\) → coupled control. **R3 two-qubit unitary:** global \(E\) fixed, subsystem \(S_c\) rises → coarse-graining anchor. |
| `regime_gamma_calibration.py` | 2 | \(\gamma\) has units of time; the master eq's \(\alpha\beta=4\pi G/c^4\) is dimensionally inconsistent ⇒ \(\alpha\gamma\) unfixed. Clock null-results bound \(\alpha\gamma\lesssim10^{-18}\,\)s; natural \(\gamma\) ⇒ unmeasurable, order-unity \(\alpha\)+microscopic \(\gamma\) ⇒ already excluded. |

**Result (Stage 1):** the entropy-production term is *not* reabsorbable into the
energy term for pure dephasing — a departure exists **in principle**.
**Result (Stage 2):** but for every natural parameter choice it is unmeasurable
(or already excluded) — **reformulation in practice**; the true gap is the
dimensional under-determination of the load constants.

**Non-claims:** structural weights \(\alpha=\beta=\gamma=1\) (uncalibrated); no
physical magnitude; \(S_c\) is a model channel entropy; **no gravity asserted.**
Stage 2 (calibrated \(\gamma\)-magnitude) and Stage 3 (precision clocks) remain open.

```bash
.venv/bin/python simulations/regime/regime_decoupling_witness.py
```
