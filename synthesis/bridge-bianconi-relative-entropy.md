# Bridge Note: Bianconi Relative Entropy ↔ Computational Entropy / \(\Phi_g\) / \(L\)

**Status:** Living synthesis note (2026-07-14)  
**Primary external source:** G. Bianconi, *Gravity from entropy*, Phys. Rev. D **111**, 066001 (2025); arXiv:2408.14391  
**Local PDF/notes:** [papers/external/](../papers/external/)  
**Parent docs:** [THEORY.md](../THEORY.md) §3.3 · [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)

---

## 1. Why this paper matters here

Bianconi derives continuum modified gravity from an **entropic action**: quantum relative entropy between the spacetime metric and a **matter-induced metric**. That is the same broad program as ours—geometry as information bookkeeping—cast as a **variational field theory** rather than a channel + load master equation. It is the strongest recent continuum peer to cite in the Jacobson–Verlinde–holography lineage, and a concrete target for a future continuum limit of our discrete computational models.

## 2. Bianconi in one page of substance

| Piece | Content |
|-------|---------|
| **Objects** | Metric \(g\) as local quantum operator (effective density matrix; invertible, not necessarily unit-trace). Matter-induced metric \(G\) (topologically: \(\tilde G = \tilde g + \alpha\tilde M - \beta\tilde{\mathcal{R}}\)). |
| **Action** | \(\mathcal{L} = \operatorname{Tr}\, g \ln G^{-1}\) (quantum relative / cross-entropy; Araki-related). |
| **Matter** | Dirac–Kähler bosons: 0-form ⊕ 1-form ⊕ 2-form; \(\tilde M\) from Hodge–Dirac structure; curvature enters so vacuum geometry is determined. |
| **G-field** | Auxiliary multipliers linearize the action → dressed Einstein–Hilbert + dressed matter; equations stay **second order**. |
| **Emergent \(\Lambda\)** | \(\Lambda_G = \frac{1}{2\beta}\operatorname{Tr}_F(\tilde{\mathcal{G}} - \tilde I - \ln\tilde{\mathcal{G}}) \ge 0\), depends **only** on the G-field; small near identity. |
| **Limits** | Low coupling → Einstein–Hilbert with zero \(\Lambda\); warm-up scalar recovers massless KG from relative entropy. |

## 3. Correspondence table (honest rigor)

| Level | Bianconi | Our framework | Status |
|-------|----------|---------------|--------|
| Semantic | Gravity from information/entropy mismatch of geometry vs matter | Gravity as computational channel \(\Phi_g\); \(S_c = S(\Phi_g(\rho))\); load \(L\) | **Aligned** |
| Semantic | Metric as effective density matrix / quantum operator | Local \(\rho\); von Neumann \(S_c\) | **Aligned** (operator vs state) |
| Structural | Relative entropy \(\operatorname{Tr} g\ln G^{-1}\) as dynamics | Master equation driven by \(L(E, \dot S_c, S_{\rm boundary})\) | **Candidate** — different entropy object |
| Structural | \(G = g + \alpha M - \beta\mathcal{R}\) | Energy term + entropy-production + holographic term in \(L\) | **Candidate** map of three contributions |
| Structural | G-field dresses \(g\); \(\Lambda_G > 0\) | Load reparameterizes \(d\tau\); cosmology / inflation recovery | **Analogical** |
| Constructive | Continuum from network precursor | Discrete lambda / IDEM / games → continuum \(\Phi_g\) | **Shared program**, not yet identified |

**What we share:** Geometry is not fundamental in isolation; it is co-determined with the information structure of matter. Low “demand” recovers GR/Newton; high demand produces strong-field / cosmological departures. Entropy (in the broad sense) is the currency.

**What we do not share yet:** Primary entropy is **relative entropy of metrics** (Bianconi) vs **output entropy of a computation** \(H_c\)/\(S_c\) (us). Dynamics are **EL from an action** vs **load-gated master equation**. Microscopic matter is **topological forms** vs **lambda/IDEM/decay vectors**.

## 4. Highest-value open mappings

1. **Relative entropy as continuum limit of \(H_c\).**  
   Interpret “realized geometry” vs “matter-channel output pattern” as two distributions (or operators). Ask whether \(\operatorname{Tr} g\ln G^{-1}\) can emerge from coarse-graining ensembles of reduction outcomes or channel outputs. Status: open; would raise the bridge from semantic to constructive.

2. **G-field vs load \(L\).**  
   - Hypothesis A: \(\tilde{\mathcal{G}}\) is a **metric dressing** (closer to \(g_{\mu\nu}(\rho)\) self-consistency than to \(L\)).  
   - Hypothesis B: \(\Lambda_G(\mathcal{G})\) tracks a **slow cosmological degree of freedom** related to boundary growth / inflation in our recoveries.  
   - Hypothesis C: second derivatives of \(\mathcal{G}\) in Bianconi’s \(D_{\mu\nu}\) parallel entropy-production stiffness in \(\gamma|dS_c/d\tau|_{\rm reg}\).  
   Prefer transparent comparison over forced equality.

3. **Three-term decomposition.**  
   Align \(\alpha\tilde M\) (matter kinetic/mass structure) with energy-density demand; curvature pieces with geometric self-consistency; holographic/boundary accounting with \(\delta S_{\rm boundary}/S_{\rm BH}\). Write explicit weak-field dictionaries before claiming derivation.

4. **Discrete bridge.**  
   Bianconi’s network precursor and our IDEM/games models are parallel discrete substrates. A shared toy (e.g. finite “screen + bulk cells” with relative-entropy action *and* a channel load) would validate both continuum stories.

## 5. Citation and use policy

- **Cite** Bianconi in papers under entropic / information-theoretic gravity (with Jacobson, Verlinde, holography, Lloyd).  
- **Do not** claim that our master equation is derived from her action (or vice versa) until a constructive map exists.  
- **Do** use her construction as: (i) continuum entropic-action target; (ii) existence proof that metric-as-operator + relative entropy yields second-order modified gravity with emergent \(\Lambda\); (iii) motivation for a future variational dual of \(\Phi_g, L\).

## 6. Next concrete steps

| Priority | Action | Status |
|----------|--------|--------|
| P0 | Keep this note + THEORY §3.3 in sync | Ongoing |
| P1 | Comparison in main `.tex` Unification (`Bianconi2025`) | Done |
| P2 | Euclidean joint toy (observation channel + PM + load) | **Done — 6/6 SUPPORT** |
| P3 | Formal ACD-EW duality note | **Done** — [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) |
| P4 | Theorem T1 residual domination / 2D lift | Open |
| P5 | Weak-field Newtonian dictionary vs continuum load | Open |
| P6 | Variational dual of full master equation | Open |

---

*Bridge note. Constructive Euclidean dual: see ACD-EW. Full continuum equivalence remains open.*
