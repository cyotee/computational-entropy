# ACD-EW ↔ Continuum GfE / Master Equation: Dictionary and Honest Transfer List

**Status:** Synthesis note (2026-07-14) — preliminary research throughout  
**Scope:** What the Euclidean Action–Channel Duality (ACD-EW) *settles*, how its objects map into project language, and what may or may not carefully transfer toward continuum Gravity-from-Entropy (GfE) and our gravitational master equation.  
**Parents:** [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) · [bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md) · [THEORY.md](../THEORY.md) §3.3 · [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md)  
**Pack:** [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md)

This note is a **dictionary plus transfer checklist**, not a derivation. Bianconi GfE, our \(\Phi_g/S_c/L\) program, and the dual itself are all **research constructions**. None of them has the empirical standing of general relativity. Claim only what the toys and definitions support.

---

## 1. Settled ACD-EW claim (careful wording)

On **flat Euclidean 1D and 2D lattices**, with fixed observation models \(y=\phi_\star+\eta\) and reconstructors in the family \(\{\text{heat},\,\text{PM},\,\text{load-gated PM}\}\), Bianconi’s **GfE warm-up** — induced metric \(G=1+\alpha_G|\nabla\phi|^2\), action \(S_{\mathrm{GfE}}=-\sum\ln G\), gradient flow implemented as classical (Catte-regularized in 2D) **Perona–Malik** anisotropic diffusion — is **operationally dual** to an **observation channel** whose quality is scored by residual reconstruction entropy \(H_c\) (residual log-energy plus edge-location uncertainty) and whose **computational load** \(L_E+L_S\) both tracks induction intensity \(\mathbb{E}[G-1]\) and reparameterizes reconstructor time via \(dt/(1+\alpha_L L_{\mathrm{clock}})\). Duality means a **shared Stage-2 geometric imprint** \(G[\hat\phi]\): Stage-3 GfE/PM flow acts as a structure-preserving Stage-1 reconstructor that reduces residual relative to isotropic heat on jump-like structure, while Stage-1 load is a scalar summary of that imprint’s intensity plus entropy-change rate. This is a **constructive special case**, verified by joint toys at **6/6 SUPPORT** in 1D and 2D under fixed seeds and scorecards. It is **not** a proof that continuum Lorentzian GfE (modified Einstein equations with G-field and \(\Lambda_G\)) equals our gravitational master equation, nor a theorem for all fields, noise models, or continuum limits. A residual-domination theorem (T1) is only **sketched**; T2–T4 remain open.

---

## 2. Dictionary: warm-up objects ↔ project language

Objects below are those of the joint toys and of ACD-EW. “Project language” points to canonical definitions in foundations / emergent gravity; the toy uses **specializations** of those ideas.

| Warm-up / ACD-EW object | Definition in the toys | Project language | Rigor of the match |
|-------------------------|------------------------|------------------|--------------------|
| \(\phi\), \(\phi_\star\), \(\hat\phi\) | Scalar field on a lattice; hidden truth; reconstructor state | Local “structure” / matter pattern whose gradients induce geometry; **not** yet a density operator \(\rho\) | Semantic / toy-level |
| Support metric \(g\equiv 1\) | Flat Euclidean edges (1D) or grid (2D) | Background / ambient geometry on which induction is measured | Structural (trivial warm-up of \(g\)) |
| Induced metric \(G=1+\alpha_G\|\nabla\phi\|^2\) | Edgewise (1D) or mean squared forward grads (2D) | Stage-2 **geometric imprint** of computational / matter structure; Bianconi warm-up second metric | **Structural** (definitional hinge of the dual) |
| \(S_{\mathrm{GfE}}=-\sum\ln G\) | Discrete warm-up action | Continuum GfE entropic action reduced to the scalar Euclidean warm-up; **not** \(\operatorname{Tr} g\ln G^{-1}\) with curvature | Structural / literature (Bianconi warm-up) |
| Perona–Malik (PM) flow | \(\rho=1/(1+(\|\nabla\phi\|/K)^2)\); div of flux; Catte regularization in 2D | Stage-3 dynamics of the warm-up action; used here as **observation channel** \(\mathcal{C}_t^{\mathrm{GfE}}\) | Structural (lit.) + constructive (toys) |
| Observation \(y=\phi_\star+\eta\) | Additive Gaussian noise | Input to a computational map / channel | Semantic specialization of a channel input |
| Residual \(R\), \(H_R\), \(H_{\mathrm{edge}}\) | MSE vs \(\phi_\star\); log residual proxy; soft edge-mass Shannon entropy | Quality / localization of **channel output** relative to hidden structure | Specialization of output-pattern entropy |
| **\(H_c=H_R+\lambda_e H_{\mathrm{edge}}\)** | Toy computational entropy of the reconstructor | Classical **computational entropy** \(H_c(f;p_X)=H(Y)\) specialized to residual/edge output quality — **not** Shannon entropy of a generic bit map, and **not** \(S_c=S(\Phi_g(\rho))\) | Constructive toy specialization of \(H_c\); quantum \(S_c\) not present |
| \(L_E\propto\mathbb{E}[(\nabla\hat\phi)^2]\) | Induction-intensity load | Scalar demand associated with Stage-2 deformation; tracks \(\mathbb{E}[G-1]\) | Constructive / near-definitional in the toy |
| \(L_S\propto\|\Delta H_c\|/\Delta t\) | Entropy-rate load | Analogue of entropy-production contribution in continuum load | Semantic + constructive (toy) |
| \(L_B\) | Edge-saturation term (not in clock in v2) | Capacity / boundary-like saturation; **not** identified with \(S_{\mathrm{boundary}}/S_{\mathrm{BH}}\) | Loose analogue only |
| \(L_{\mathrm{clock}}=L_E+L_S\) | Clock argument | Scalar summary of demand used for time reparameterization | Semantic + constructive |
| \(dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}})\) | Load-gated Euler step | Discrete analogue of master-equation factor \(d\tau=dt/(1+\alpha L)\) | Form match; **not** a derivation of continuum \(L(\rho,g)\) |
| Heat flow (control) | Isotropic diffusion | Non-structure-preserving baseline channel | Experimental control |
| Gravitational channel \(\Phi_g\) | **Absent** in toys | CPTP map on \(\rho\); \(S_c=S(\Phi_g(\rho))\) | Not instantiated in ACD-EW |
| Continuum load \(L(\rho,g)\) | **Absent** as three-term continuum formula | \(L=\beta E/(V\epsilon_0)+\gamma\|dS_c/d\tau\|_{\rm reg}+\delta S_{\mathrm{boundary}}/S_{\mathrm{BH}}\) | Only the **clock form** is mirrored |
| Full GfE \(G=\tilde g+\alpha\tilde M-\beta\tilde{\mathcal{R}}\), G-field, \(\Lambda_G\) | **Absent** | Continuum Stage-3 target (Bianconi full theory) | Open; warm-up only |

**Reading rule:** Shared object is Stage-2 \(G\). Shared *form* of dynamics is “entropic geometry drives a flow that can be read as a channel.” Shared *form* of load is a nonnegative scalar that slows internal time. Shared *identity* of entropy functionals, load components, or field equations is **not** claimed.

---

## 3. Transfer list — what may carefully carry upward

These items may be used, with the stated caveats, when discussing continuum GfE or the master equation as **programmatic targets**. Wording should remain conditional (“suggests,” “is consistent with,” “provides a discrete template for”), not equational.

1. **Three-stage workflow as a usable scaffold.**  
   Stage 1 (channel + load + clock) → Stage 2 (induced geometric imprint \(G\)) → Stage 3 (entropic action / flow on \((g,G)\)) is **non-vacuous** on Euclidean lattices. The same scaffolding is the intended story for continuum work. Transfer: workflow architecture, not field equations.

2. **Stage-2 \(G\) as the duality hinge.**  
   “Matter-/structure-induced metric” can be defined from reconstructor (or field) gradients, not only from a classical Lagrangian after the fact. Continuum GfE already uses an induced \(G\); ACD-EW shows an **operational** route to the same kind of object from a channel state \(\hat\phi\). Transfer: conceptual role of \(G\); the formula \(G=1+\alpha|\nabla\phi|^2\) is warm-up only.

3. **Structure-preserving flow as a computational channel.**  
   Gradient flow of an entropic geometric action can reduce reconstruction residual relative to isotropic diffusion while retaining edges. That supports reading Stage-3 dynamics as Stage-1 computation on the same \(G\). Transfer: *channel reading of geometric flow* as a research principle; residual domination remains toy-supported + T1 sketch, not a continuum theorem.

4. **Load as induction intensity plus entropy rate.**  
   Splitting \(L_E\) (geometry induction) and \(L_S\) (rate of \(H_c\) change) is compatible with PM and with a load-gated clock. This is a **template** for comparing to continuum \(L\)’s energy and \(\|dS_c/d\tau\|\) terms. Transfer: multi-component demand; coefficients and continuum identification remain open.

5. **Clock factor form \(1/(1+\alpha L)\).**  
   Discrete load-gating slows mid-run evolution without erasing PM’s residual/edge advantages on the tested ICs. Transfer: **formal analogy** to \(d\tau=dt/(1+\alpha L)\) in the master equation; not a derivation of proper time from relative entropy of metrics.

6. **1D → 2D Euclidean robustness.**  
   The dual is not an artifact of one dimension: `_joint_toy_2d.py` also scores 6/6 with Catte PM. Transfer: mild support for continuum/image-processing links in *Beyond holography* and for T4 (continuum limit of the **warm-up**), still inside Euclidean ACD-EW.

7. **Citation and experimental posture.**  
   Joint toys + ACD-EW may be cited as **constructive Euclidean evidence** that load/\(H_c\) interface cleanly with GfE warm-up geometry. Bianconi full theory and Thattarampilly–Zheng recoveries remain **external continuum targets**, not outputs of our toys.

8. **Programmatic next maps (still open, but well-posed).**  
   From ACD-EW §6 and the bridge note: lift \(G\) toward topological \(\tilde G=\tilde g+\alpha\tilde M-\beta\tilde{\mathcal{R}}\); relate residual \(H_c\) to von Neumann \(S_c\); relate \(L_{\mathrm{clock}}\) to three-term \(L(\rho,g)\); compare weak-field / cosmology recoveries to GfE modified Einstein only after those maps exist.

---

## 4. Non-transfer list — what we must not claim

Do **not** carry the following upward in papers, talks, or theory docs without new constructive work.

1. **Full Bianconi modified Einstein \(\Leftrightarrow\) our master equation.**  
   Not established. Different primary entropy objects (relative entropy of metrics vs output entropy of a channel), different dynamics (variational EL vs load-gated Liouvillian), different matter microstructure.

2. **Identity of functionals.**  
   Not \(H_c\equiv S_{\mathrm{GfE}}\), not \(H_c\equiv S_c\), not \(L\equiv G\), not \(L_{\mathrm{clock}}\equiv L(\rho,g)\), not \(L_B\equiv S_{\mathrm{boundary}}/S_{\mathrm{BH}}\).

3. **Derivation of continuum GfE action from computational load (or vice versa).**  
   ACD-EW does not derive \(\mathcal{L}=\operatorname{Tr} g\ln G^{-1}\), the G-field, or \(\Lambda_G\) from \(L\). The joint toy starts from the **warm-up** Lagrangian already.

4. **Lorentzian, curvature-coupled, or quantum-\(\rho\) content.**  
   Toys are flat Euclidean scalar fields with classical noise. No horizons, no CPTP \(\Phi_g\), no Dirac–Kähler forms, no network-to-continuum limit of the full theory.

5. **Theorem-level residual domination for all \(\phi_\star\).**  
   Scorecards are constructive verification on fixed IC families and parameters. T1 is a **proof outline** (§10 of ACD-EW), not a finished proposition. T2–T4 are open.

6. **Empirical gravity claims.**  
   Edge denoising on a lattice is not evidence for Newtonian recovery, Schwarzschild geometry, inflation, or black-hole evaporation. Those recoveries, on either side of the literature, need their own arguments.

7. **Equivalence of external GfE phenomenology papers to our recoveries.**  
   Thattarampilly–Zheng inflation/BH results are continuum **GfE** applications. They do not automatically become results of the \(\Phi_g/L\) master equation.

8. **Established status.**  
   Do not present ACD-EW, Bianconi GfE, or our master equation as settled physics on par with GR. All three are **preliminary theoretical programs** with partial internal consistency and external literature alignment.

---

## 5. Status of external references (supporting literature)

All items below are **third-party supporting literature** for the continuum side of the program. They motivate targets and templates; they are not theorems of this repository, and they are themselves active research, not established theory in the GR sense.

| Reference | Local path | Role relative to ACD-EW / continuum | What we may say | What we must not say |
|-----------|------------|-------------------------------------|-----------------|----------------------|
| Bianconi, *Gravity from entropy*, PRD **111**, 066001 (2025); arXiv:2408.14391 | `papers/external/Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf` (+ `Bianconi_Gravity_from_entropy_NOTES.md`) | Foundational continuum GfE action; Stage-3 **macro target** | Cite as continuum entropic-action peer; relative entropy of metrics; G-field; emergent \(\Lambda_G\) | That we derived it from \(L\); that it equals the master equation |
| Bianconi, *Beyond holography*, arXiv:2503.14048 | `papers/external/Bianconi_Beyond_holography_arXiv_2503.14048.pdf` | PM = gradient flow of Euclidean GfE **warm-up**; direct template for joint toys | Cite as justification that PM implements warm-up GfE flow; image/algorithmic dual | That PM on a lattice proves Lorentzian modified Einstein equations |
| Thattarampilly & Zheng, *Inflation from entropy*, arXiv:2509.23987 | `papers/external/Thattarampilly_Zheng_Inflation_from_entropy_arXiv_2509.23987.pdf` | Cosmology / inflation **within GfE** | Cite as continuum recovery target for GfE vacuum cosmology; comparison candidate for our inflation recovery **after** a map | That ACD-EW or our toys imply GfE inflation or CMB windows |
| Thattarampilly, Zheng & Kakkat, spherical BHs in GfE, arXiv:2602.13694 | `papers/external/Thattarampilly_Zheng_Spherically_symmetric_BH_arXiv_2602.13694.pdf` | BH sector **within GfE** (Schwarzschild + corrections; mass-loss sketch) | Cite as GfE strong-field target; analogy checklist for horizon/entropy leakage themes | That load-gated PM is a black-hole model |
| Kumar, *Recovering semiclassical Einstein…*, arXiv:2404.16912 | `papers/external/Kumar_Recovering_semiclassical_Einstein_arXiv_2404.16912.pdf` | Adjacent Clausius / \(S_{\mathrm{gen}}\) route to semiclassical Einstein | Cite as support for thermodynamic / \(\delta Q=T\,dS\) layer of the master equation program | That Kumar proves GfE or ACD-EW; that \(S_{\mathrm{gen}}\equiv H_c\) |

**Index:** [papers/external/README.md](../papers/external/README.md). Living continuum comparison (beyond the warm-up): [bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md).

---

## 6. Paste-ready “we have / we have not” (for papers)

Use or adapt the following bullets. Prefer this tone over stronger language.

### We have

- A **constructive Euclidean dual (ACD-EW)** on 1D and 2D flat lattices in which Bianconi’s GfE **warm-up** (induced metric \(G=1+\alpha|\nabla\phi|^2\), action \(S_{\mathrm{GfE}}=-\sum\ln G\), Perona–Malik gradient flow) is operationally dual to an observation channel with residual/edge computational entropy \(H_c\) and a split load \(L_E+L_S\) that tracks \(\mathbb{E}[G-1]\) and reparameterizes reconstructor time.
- **Joint numerical evidence** at 6/6 SUPPORT under fixed scorecards for both 1D (`simulations/bridging/_joint_toy_v2_core.py`) and 2D (`simulations/bridging/_joint_toy_2d.py`): PM residual and edge retention superior to heat on primary structured ICs; ramp stability; \(L_E\)–\((G-1)\) tracking; load-gating slows mid-run evolution.
- A **unified pure T1′ residual dual** on \(U_\star=[1.36,2.40]\): analytic edge persistence, identity \(R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}\), spectral freeze-tax majorant with burn-in conductivity \(\rho_b=0.42\) (PCRH\(_b\)). See `m1g-unified-pure-window.md`, `t1-prime-hybrid-writeup.md`.
- **Load-clock dual (M2 hybrid):** load-gated PM beats heat on \(I_\star\) as a mild time change (\(\tau/t\approx 0.95\)) of pure PM (`m2-t1-load.md`).
- A **formal conjecture writeup** with definitions and rigor taxonomy: `synthesis/action-channel-duality-euclidean.md`.
- A clear **shared object** story: Stage-2 \(G[\hat\phi]\) is the hinge between channel/load language and GfE warm-up language.
- **Supporting continuum literature** (Bianconi GfE and *Beyond holography*; Thattarampilly–Zheng; Kumar) as external targets, archived under `papers/external/`.
- An **honest three-stage workflow** consistent from toys to the intended continuum program.

### We have not

- Established equivalence between **full Lorentzian GfE** and our **gravitational master equation**.
- Derived Bianconi’s continuum action from computational load \(L\), or the reverse.
- Identified toy \(H_c\) with von Neumann \(S_c\), or toy \(L_{\mathrm{clock}}\) with continuum \(L(\rho,g)\).
- A **pure unconditional** residual-domination theorem (Hρ / freeze-tax spectral bound still a hypothesis; raw T1 on \((0,t_\star]\) is false).
- Embedded lambda/IDEM, quantum channels, Lorentzian signature, or horizons into the joint toys.
- Empirical tests of gravity; lattice denoising is not a gravity experiment.
- A claim that GfE phenomenology papers are results of our framework.

---

## 7. Pointers

| Resource | Path | Use |
|----------|------|-----|
| **Formal dual (ACD-EW)** | [synthesis/action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) | Definitions, conjecture (A)–(D), scorecard criteria, rigor table, T1 sketch §10, 2D status §11 |
| **Continuum bridge (full GfE)** | [synthesis/bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md) | Semantic/structural maps to \(\Phi_g,S_c,L\); open mappings; citation policy |
| **Master equation (canonical)** | [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) | \(\Phi_g\), \(S_c\), \(L(\rho,g)\), \(d\tau\), \(\partial_\tau\rho=\mathcal{L}_g\rho\) |
| **Theory correspondence** | [THEORY.md](../THEORY.md) §3.3 | High-level GfE ↔ us table; ACD-EW pointer |
| **1D joint toy core** | [simulations/bridging/_joint_toy_v2_core.py](../simulations/bridging/_joint_toy_v2_core.py) | CLI scorecard; shared dynamics |
| **2D joint toy** | [simulations/bridging/_joint_toy_2d.py](../simulations/bridging/_joint_toy_2d.py) | Image-lattice lift; Catte PM |
| **Design / scorecard notes** | [simulations/bridging/DESIGN_gfe_load_joint_toy.md](../simulations/bridging/DESIGN_gfe_load_joint_toy.md), [simulations/bridging/README.md](../simulations/bridging/README.md) | P0–P2 refinements; run commands |
| **External PDFs + index** | [papers/external/](../papers/external/), [papers/external/README.md](../papers/external/README.md) | Bianconi (×2), Thattarampilly–Zheng (×2), Kumar |
| **Bianconi reading notes** | [papers/external/Bianconi_Gravity_from_entropy_NOTES.md](../papers/external/Bianconi_Gravity_from_entropy_NOTES.md) | Condensed continuum construction |

**Reproduction (toys):**

```bash
.venv/bin/python simulations/bridging/_joint_toy_v2_core.py
.venv/bin/python simulations/bridging/_joint_toy_2d.py
```

---

## 8. One-line discipline for future writing

> **ACD-EW settles a constructive Euclidean dual between GfE warm-up geometry and an observation channel with load clock; it does not settle continuum GfE \(\Leftrightarrow\) master equation. Treat Bianconi, Thattarampilly–Zheng, Kumar, our theory, and this dual as preliminary research that share a family resemblance—not as established equivalence.**

---

*Document control: written 2026-07-14 as the dictionary + honest transfer list companion to ACD-EW. Update when T1–T4, continuum maps, or joint-toy scope change.*
