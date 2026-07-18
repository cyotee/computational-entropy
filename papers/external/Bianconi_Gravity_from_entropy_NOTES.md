# Notes: Bianconi — Gravity from entropy

**Citation:** Ginestra Bianconi, *Gravity from entropy*, arXiv:2408.14391v7; Phys. Rev. D **111**, 066001 (2025).  
**PDF:** [Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf](Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf)  
**Added:** 2026-07-13

## One-line summary

Gravity is derived from an **entropic action**: the **quantum relative entropy** between the spacetime metric \(g\) (treated as a local quantum operator / effective density matrix) and a **matter-induced metric** \(G\), yielding modified Einstein equations that reduce to GR at low coupling, with an auxiliary **G-field** producing a dressed Einstein–Hilbert action and an **emergent small positive cosmological constant**.

## Core construction

1. **Metric as quantum operator.** At each point of Lorentzian spacetime, rank-2 metric tensors are treated as invertible quantum operators (not necessarily unit-trace density matrices). Eigenvalues are defined in a Lorentz-invariant way via \(\hat{G}_{\mu\sigma} g^{\sigma\nu} V_\nu = \lambda V_\mu\). Remarkably, eigenvalues of \(g_{\mu\nu}\) are all \(1\), so the von Neumann-like entropy of \(g\) itself vanishes.

2. **Two metrics.**
   - Geometry metric: \(g\) (and topological extension \(\tilde{g}\) over 0-, 1-, and 2-forms).
   - Matter-induced metric: \(\tilde{G} = \tilde{g} + \alpha \tilde{M} - \beta \tilde{\mathcal{R}}\), where \(\tilde{M}\) comes from Dirac–Kähler (topological) bosons and \(\tilde{\mathcal{R}}\) packages Ricci scalar/tensor and Riemann contributions.

3. **Entropic action.** Lagrangian is the quantum relative entropy (cross-entropy) between \(\tilde{g}\) and \(\tilde{G}\):
   \[
   \mathcal{L} = \operatorname{Tr} \tilde{g}\, \ln \tilde{G}^{-1} = -\operatorname{Tr}_F \ln(\tilde{G}\,\tilde{g}^{-1}).
   \]
   Action: \(\mathcal{S} = \ell_P^{-d} \int \sqrt{|-g|}\,\mathcal{L}\, d\mathbf{r}\). Related to **Araki relative entropy** for von Neumann algebras.

4. **G-field.** Auxiliary fields \(\tilde{\mathcal{G}}\) (G-field) and \(\tilde{\Theta}\) enforce \(\tilde{G}\,\tilde{g}^{-1} = \tilde{\Theta}\) as Lagrangian multipliers, linearizing the action and avoiding Ostrogradsky-type higher-derivative pathologies. Equations remain **second order** in the metric and G-field.

5. **Dressed EH + emergent Λ.** After eliminating auxiliaries, the action splits as \(\tilde{\mathcal{S}} = \beta \mathcal{S}_G + \alpha \mathcal{S}_M\) with
   \[
   \mathcal{L}_G = R_G - 2\Lambda_G,\qquad
   \Lambda_G = \frac{1}{2\beta}\operatorname{Tr}_F\bigl(\tilde{\mathcal{G}} - \tilde{I} - \ln\tilde{\mathcal{G}}\bigr)
   \]
   non-negative and **depending only on the G-field**. Low-coupling limit recovers Einstein–Hilbert with zero Λ plus standard (topological) matter.

6. **Modified Einstein equations** (schematic):
   \[
   R^G_{(\mu\nu)} - \tfrac12 g_{\mu\nu} R_G - 2\Lambda_G + D_{(\mu\nu)} = \kappa T_{(\mu\nu)},
   \]
   with dressed Ricci \(R^G\), G-field second-derivative terms \(D_{\mu\nu}\), and \(\kappa = \alpha/\beta\).

## Warm-up (scalar) limit

For complex scalar \(\phi\) with \(G = g + \alpha M\), \(M_{\mu\nu} = (\nabla_\mu\bar\phi)(\nabla_\nu\phi)\):
\[
\mathcal{L} = -\ln(1+\alpha|\nabla\phi|^2) \to -\alpha|\nabla\phi|^2
\]
at weak coupling (massless Klein–Gordon). Vacuum does **not** fix \(g\) until curvature terms are included in the full theory.

## Relation to this project

See discussion in the session summary / THEORY.md updates. High-level alignment:

| Bianconi (2025) | This repo (computational entropy / emergent gravity) |
|-----------------|------------------------------------------------------|
| Gravity from entropic / information action | Gravity as computational channel \(\Phi_g\) with computational entropy \(S_c\) |
| Metric as effective density matrix / quantum operator | Local microstate \(\rho\) evolved by CPTP channel; \(S_c = S(\Phi_g(\rho))\) |
| Relative entropy \(D(g\|G_{\text{matter}})\) as dynamics | Local entropy transfer + global conservation; load \(L\) from information demand |
| Matter-induced metric \(G\) couples matter ↔ geometry | Matter/energy density + entropy production + boundary terms in \(L\) |
| G-field dresses EH; emergent \(\Lambda_G > 0\) | Load reparameterizes proper time; cosmological recovery including inflation |
| Low coupling → Einstein | Low load → Newtonian / GR weak-field recoveries |
| Araki / von Neumann algebra framing | Quantum \(S_c\) (von Neumann) as quantum case of \(H_c\) |
| Discrete network precursor [Bianconi 2024] | Discrete lambda/IDEM/games models as microscopic substrate |

### Differences / caution

- Bianconi is a **variational continuum field theory** (action → EL equations). Ours is currently a **master equation / channel** picture with computational load, not yet a relative-entropy action principle.
- Bianconi’s “entropy” is relative entropy of **metrics-as-operators**, not explicitly the entropy of an **output distribution of a computation** (\(H_c\) / \(S_c\)).
- The G-field is a new auxiliary in Bianconi; mapping it to our \(L\), boundary term, or holographic screen is non-trivial and open.
- Dirac–Kähler topological bosons ≠ lambda/IDEM decay vectors, but both encode structured “matter as forms/terms” that induce information loss or metric deformation.

### Suggested follow-ups for this repo

1. ~~Add Bianconi to external citations in the main `.tex` and in `THEORY.md` correspondence tables~~ — done 2026-07-14 (`\bibitem{Bianconi2025}`, THEORY §3.3).
2. Living bridge note: [synthesis/bridge-bianconi-relative-entropy.md](../../synthesis/bridge-bianconi-relative-entropy.md).
3. Explore whether \(\mathcal{L} = \operatorname{Tr} g\ln G^{-1}\) can be motivated as a continuum limit of computational relative entropy between “realized geometry” and “matter-channel output pattern.”
4. Compare \(\Lambda_G(\mathcal{G})\) with cosmological recovery and holographic boundary term \(\delta S_{\rm boundary}/S_{\rm BH}\) in our load \(L\).
5. Note discrete network precursor as potential bridge to lambda/combinatorial models.
