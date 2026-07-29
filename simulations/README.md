# simulations/

Executable models, notebooks, and code that demonstrate concepts.

Structure:
- classical/       ← Discrete \(H_c\) / load accounting (M11), games, IDEM examples
- gravity-toy/     ← Simple models of the master equation, load, or time dilation
- bridging/        ← Euclidean dual toys (GfE warm-up ↔ channel/load) — **program-level settled**

## Classical (primary science track after D9)

- **[classical/m11_and_gate_ledger.py](classical/m11_and_gate_ledger.py)** — M11 Phase 1 pure AND-gate ledger
- **[classical/README.md](classical/README.md)** — how to run + honesty limits
- Design: [synthesis/m11-idem-to-load.md](../synthesis/m11-idem-to-load.md)

```bash
.venv/bin/python simulations/classical/m11_and_gate_ledger.py
```

## Bridging (reference / dual layer)

- **[bridging/](bridging/)** — 1D/2D/blackjack dual toys (6/6 SUPPORT pattern)
- See [bridging/README.md](bridging/README.md); claims: [synthesis/CURRENT_CLAIMS.md](../synthesis/CURRENT_CLAIMS.md)

All code here should support claims made in THEORY.md / CURRENT_CLAIMS without overclaiming continuum gravity.
