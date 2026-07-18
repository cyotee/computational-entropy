# Weak-Field / Newtonian Comparison: Load Master Equation vs Bianconi GfE

**Status:** Synthesis comparison note (2026-07-14)  
**Scope:** Low-load / weak-field / low-coupling limits only — **not** full continuum equivalence  
**Parents:** [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) · [quantum/Newton.md](../quantum/Newton.md) · [papers/external/Bianconi_Gravity_from_entropy_NOTES.md](../papers/external/Bianconi_Gravity_from_entropy_NOTES.md) · [bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md) · [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) · [THEORY.md](../THEORY.md) §3.3  
**External primary:** G. Bianconi, *Gravity from entropy*, Phys. Rev. D **111**, 066001 (2025); arXiv:2408.14391  
**Local PDF:** [papers/external/Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf](../papers/external/Bianconi_Gravity_from_entropy_arXiv_2408.14391.pdf)

---

## 1. Purpose and honesty preamble

### Purpose

Compare, in the **weak / low-demand** regime:

| Side | Object of study |
|------|-----------------|
| **Ours** | Computational load \(L\) + master equation → documented Newtonian / Poisson recovery |
| **Bianconi GfE** | Low-coupling limit of the relative-entropy action → Einstein–Hilbert with zero \(\Lambda\); role of G-field and \(\Lambda_G\) |

The goal is a **dictionary of candidate correspondences** and a checklist for a future cross-framework test — not a derivation of either theory from the other.

### Honesty preamble

Both frameworks are **preliminary research programs**, not established physics on the footing of classical general relativity.

| Statement | Status |
|-----------|--------|
| GR weak field \(\Rightarrow\) Newton/Poisson | Standard, textbook |
| Our master equation \(\Rightarrow\) Newton via \(\alpha\beta = 4\pi G/c^4\) matching | **Internal recovery sketch** (repo-documented); constants fixed by matching, not derived from first principles independent of Newton |
| Bianconi entropic action \(\Rightarrow\) modified Einstein; low coupling \(\to\) EH with zero \(\Lambda\) | **Claim of the external paper** (arXiv:2408.14391); not independently re-derived here |
| Full Lorentzian GfE \(\Leftrightarrow\) gravitational master equation | **Not established** (see ACD-EW scope boundary) |
| Euclidean ACD-EW toy (PM \(\leftrightarrow\) observation channel + load) | **Constructive special case only** — does not substitute for weak-field continuum dictionary |

**Scope boundary (from ACD-EW):** Euclidean action–channel duality on a flat lattice is **not** continuum equivalence of Lorentzian GfE to the master equation. This note stays at the level of structural / semantic comparison of **limits**, not of full dynamics.

**Notation warning:** Bianconi’s coupling constants \(\alpha,\beta\) (matter / curvature weights in \(\tilde G\)) are **not** the same objects as our load weights \(\alpha,\beta\) in \(L\) and \(d\tau = dt/(1+\alpha L)\). Below we use subscripts when needed:

| Symbol set | Ours | Bianconi |
|------------|------|----------|
| Load scale / couplings | \(\alpha_L\), \(\beta_L\), \(\gamma_L\), \(\delta_L\) (when disambiguating); historically \(\alpha,\beta,\gamma,\delta\) in master equation | \(\alpha_B\), \(\beta_B\) in \(\tilde G = \tilde g + \alpha_B \tilde M - \beta_B \tilde{\mathcal{R}}\) |
| Geometry | \(g_{\mu\nu}(\rho)\), potential \(\Phi\) | Spacetime metric \(g\); matter-induced \(G\) (or \(\tilde G\)); G-field \(\tilde{\mathcal{G}}\) |
| Entropy object | \(S_c = S(\Phi_g(\rho))\) (output entropy of channel) | Relative entropy \(\operatorname{Tr}\, g\ln G^{-1}\) (metrics-as-operators) |

When quoting repo formulas that use bare \(\alpha,\beta\), we mean **our** load constants unless marked Bianconi.

---

## 2. Our side: load structure and Newton recovery

Canonical sources: [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md), [quantum/Newton.md](../quantum/Newton.md).

### 2.1 Load \(L\)

\[
L(\rho,g)
=
\beta\,\frac{E[\rho]}{V\epsilon_0}
+
\gamma\left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}}
+
\delta\frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)}.
\]

| Term | Content |
|------|---------|
| Energy-density | \(E[\rho]=\operatorname{Tr}(\rho H)\); \(\epsilon_0\) reference (Planck-scale) energy density |
| Entropy-production | Regularized \(\lvert dS_c/d\tau\rvert\) over a Margolus–Levitin window |
| Holographic boundary | Screen entropy over Bekenstein–Hawking capacity |

### 2.2 Proper-time reparameterization and master equation

\[
d\tau = \frac{dt}{1 + \alpha L(\rho,g)},
\qquad
\frac{d\rho}{dt}
=
\frac{1}{1+\alpha L(\rho,g)}\,
\mathcal{L}_g\bigl[\rho;\, g_{\mu\nu}(\rho)\bigr].
\]

\(\mathcal{L}_g\) is required to satisfy the Clausius relation \(\delta Q = T\, dS_c\) on local horizons (Jacobson 1995), so that Einstein-level thermodynamics is not an extra postulate once the generator is so constrained.

### 2.3 Low-load / weak-field / slow-motion regime

Assumptions (as stated in Newton recovery):

- \(\alpha L \ll 1\)
- Curvature small; velocities non-relativistic
- Entropy-production and holographic terms **subdominant** relative to the energy-density term

Dominant load:

\[
L(\rho,g)
\approx
\beta\frac{E[\rho]}{V\epsilon_0}
\approx
\beta\frac{\rho c^2}{\epsilon_0}
\]

(with \(\rho\) here the local mass-energy density — not the density operator; context distinguishes them).

### 2.4 Proper-time expansion and metric identification

\[
d\tau
\approx
\frac{dt}{1 + \alpha\beta\,\rho c^2/\epsilon_0}
\approx
dt\Bigl(1 - \alpha\beta\frac{\rho c^2}{\epsilon_0}\Bigr)
\quad(\alpha L \ll 1).
\]

Newtonian metric bookkeeping:

\[
\sqrt{-g_{00}} \approx 1 + \frac{\Phi}{c^2},\qquad \Phi \ll c^2.
\]

Repo identification (Newton.md):

\[
\frac{\Phi}{c^2}
\approx
-\,\alpha\beta\frac{\rho c^2}{\epsilon_0}.
\]

### 2.5 Poisson recovery (Path J/M — canonical as of 2026-07-14)

**Canonical writeup:** [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) · [quantum/Newton.md](../quantum/Newton.md) · audit [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md).

| Path | Content |
|------|---------|
| **J** | Clausius on \(\mathcal{L}_g\) → Einstein (Jacobson) → weak-field Poisson \(\nabla^2\Phi=4\pi G\rho_m\) |
| **M** | Match load clock \(d\tau/dt\) to \(1+\Phi/c^2\) **on shell** ⇒ calibration \(\alpha\beta=4\pi G/c^4\) |

**Withdrawn:** pointwise \(\Phi\propto\rho\) then \(\nabla^2\) “matching” (algebraically invalid).

**Interpretation:** higher mass-energy density raises \(L\), which slows proper time; that slowing is **calibrated** to the Newtonian \(\Phi\) already supplied by Einstein thermodynamics. No separate force law beyond Path J.

**Caveats:**

1. Constants \(\alpha,\beta,\epsilon_0\) are **fixed by matching**, not predicted independently of \(G\).  
2. Poisson is **inherited from GR/Jacobson**, not derived from load alone.  
3. Does not prove uniqueness or GfE equivalence (see M6/M6b).

### 2.6 Regime diagram (ours)

| Regime | Dominant \(L\) content | Documented recovery |
|--------|------------------------|---------------------|
| Low load, weak field, slow motion | Energy-density term | Newton / Poisson (this note) |
| Moderate curvature | Mixed + Clausius on \(\mathcal{L}_g\) | Toward Einstein-level thermodynamics (Jacobson route) |
| Horizons / high load | Boundary + entropy production | BH / time dilation / evaporation notes |
| Cosmological boundary growth | Boundary term dynamics | FLRW / inflation notes |

---

## 3. GfE side: low-coupling reduction and G-field

Sources: Bianconi arXiv:2408.14391 (abstract + §§II–III as extracted); [Bianconi_Gravity_from_entropy_NOTES.md](../papers/external/Bianconi_Gravity_from_entropy_NOTES.md); bridge note §2.

### 3.1 Objects and action (continuum GfE)

| Piece | Content |
|-------|---------|
| Geometry metric | \(g\) treated as local quantum operator / effective density matrix (invertible; not necessarily unit-trace) |
| Matter-induced metric | \(\tilde G = \tilde g + \alpha_B\tilde M - \beta_B\tilde{\mathcal{R}}\) (topological Dirac–Kähler bosons; curvature enters \(\tilde{\mathcal{R}}\)) |
| Entropic Lagrangian | \(\mathcal{L} = \operatorname{Tr}\, \tilde g\ln\tilde G^{-1} = -\operatorname{Tr}_F\ln(\tilde G\,\tilde g^{-1})\) |
| Action | \(\mathcal{S} = \ell_P^{-d}\int\sqrt{|-g|}\,\mathcal{L}\,d\mathbf{r}\) |

### 3.2 What “low coupling” means in GfE

Bianconi’s low-coupling statements (paper abstract and body; repo notes):

1. **Modified Einstein equations reduce to Einstein equations with zero cosmological constant** in the low-coupling regime.
2. **Warm-up (scalar only):** \(G = g + \alpha_B M\), \(M_{\mu\nu}=(\nabla_\mu\bar\phi)(\nabla_\nu\phi)\),
   \[
   \mathcal{L} = -\ln(1+\alpha_B|\nabla\phi|^2)
   \;\xrightarrow{\;\alpha_B|\nabla\phi|^2\ll 1\;}
   -\alpha_B|\nabla\phi|^2
   \]
   (massless Klein–Gordon). Vacuum does **not** fix \(g\) until curvature is included in the full theory.
3. With topological matter + curvature in \(\tilde G\), low energy / low curvature implies \(\tilde\Theta = \tilde G\tilde g^{-1}\) is a **small perturbation of the identity** (paper: \(\alpha_B\sim\alpha'\ell_P^4\), \(\beta_B\sim\beta'\ell_P^2\)).

**What weak field means there (careful):**

| Phrase | In GfE (as stated) | Not automatically the same as |
|--------|--------------------|-------------------------------|
| Low coupling | Small \(\alpha_B M\), \(\beta_B\mathcal{R}\) relative to \(g\); \(\tilde\Theta\simeq\tilde I\) | Our \(\alpha_L L\ll 1\) (different scalars) |
| Low coupling → EH, \(\Lambda=0\) | Einstein gravity without cosmological term | Explicit Poisson \(\nabla^2\Phi=4\pi G\rho\) derivation in the paper (not extracted as a dedicated Newton section in repo notes — **to verify against Bianconi PDF** if a linearized \(g_{00}\) calculation is given) |
| Warm-up weak gradient | KG Lagrangian | Gravitational Poisson sector |

So: GfE’s documented weak / low-coupling **gravitational** limit is **Einstein (zero \(\Lambda\))**, not a separately written Newtonian Poisson derivation in the materials we rely on. Newton then follows only if one **imports** the standard GR weak-field theorem. That chain is physically standard, but it is **not** the same logical path as our load \(\to\) \(d\tau\) \(\to\) \(\Phi\) sketch.

### 3.3 G-field, dressed EH, and \(\Lambda_G\)

Auxiliary G-field \(\tilde{\mathcal{G}}\) (and \(\tilde\Theta\)) linearizes the entropic action as Lagrangian multipliers. After elimination:

\[
\tilde{\mathcal{S}} = \beta_B\,\mathcal{S}_G + \alpha_B\,\mathcal{S}_M,
\qquad
\mathcal{L}_G = R_G - 2\Lambda_G,
\]

with

\[
\Lambda_G
=
\frac{1}{2\beta_B}
\operatorname{Tr}_F\bigl(\tilde{\mathcal{G}} - \tilde I - \ln\tilde{\mathcal{G}}\bigr)
\;\ge\; 0,
\]

depending **only** on the G-field. Near identity \(\tilde{\mathcal{G}}\simeq\tilde I+\tilde\epsilon\), \(\Lambda_G\) is small (leading piece quadratic in \(\tilde\epsilon\)).

Schematic modified Einstein equations (repo notes / paper Eq. form):

\[
R^G_{(\mu\nu)} - \tfrac12 g_{\mu\nu}\bigl(R_G - 2\Lambda_G\bigr) + D_{(\mu\nu)}
=
\kappa\, T_{(\mu\nu)},
\qquad
\kappa = \alpha_B/\beta_B,
\]

with dressed Ricci \(R^G\) and second-derivative G-field terms \(D_{\mu\nu}\). Equations remain **second order** in metric and G-field.

**Low-coupling reduction again:** when couplings are small / G-field near identity in the appropriate sense, action \(\to\) Einstein–Hilbert with **zero** \(\Lambda\), plus (topological) matter — as stated by Bianconi.

### 3.4 Regime diagram (GfE)

| Regime | GfE content | Outcome (per paper) |
|--------|-------------|---------------------|
| Low coupling, small curvature/matter deformation | \(\tilde G\simeq\tilde g\); \(\tilde{\mathcal{G}}\simeq\tilde I\) | EH, \(\Lambda=0\) |
| G-field near but not identity | Small \(\Lambda_G>0\) | Dressed EH + tiny emergent CC |
| Finite coupling / strong dressing | \(R^G\), \(D_{\mu\nu}\), \(\Lambda_G\) active | Modified second-order gravity |
| Scalar warm-up only | No curvature in \(G\) | KG at weak gradient; \(g\) undetermined in vacuum |

---

## 4. Correspondence table

Rigor labels: **semantic** (shared story) · **structural** (parallel decomposition / roles) · **candidate** (plausible map, unproven) · **analogical** (loose parallel) · **does not map** (type mismatch or conflict) · **constructive (toy only)** (ACD-EW Euclidean).

### 4.1 Shared regime story (semantic)

| Theme | Ours | GfE | Label |
|-------|------|-----|-------|
| Geometry co-determined with matter/info structure | \(g_{\mu\nu}(\rho)\); channel \(\Phi_g\) | Relative entropy of \(g\) vs matter-induced \(G\) | Semantic |
| Low demand recovers classical gravity | Low load \(\to\) Newton (repo sketch) | Low coupling \(\to\) EH, \(\Lambda=0\) | Semantic (shared *direction*; different terminal object) |
| High demand \(\to\) departures | Horizons, inflation, high-\(L\) regimes | Modified Einstein, \(\Lambda_G\), \(D_{\mu\nu}\) | Semantic / analogical |
| Entropy as currency | \(S_c\) of channel output | Relative entropy of metrics-as-operators | Semantic **family**, different primary object |

### 4.2 Symbols that *might* map

| Bianconi | Ours | Why a map is tempting | Label | Caution |
|----------|------|----------------------|-------|---------|
| Low coupling \(\alpha_B M,\beta_B\mathcal{R}\) small | \(\alpha_L L\ll 1\) | Both are “small deformation / small demand” expansions | Structural / candidate | Different dimensionless scalars; no proven common continuum limit |
| Matter piece \(\alpha_B\tilde M\) | Energy-density term \(\beta_L E/(V\epsilon_0)\) | Matter/energy drives geometric response | Structural candidate | \(\tilde M\) is form-kinetic structure; \(E[\rho]\) is Hamiltonian expectation |
| Curvature piece \(\beta_B\tilde{\mathcal{R}}\) | Geometric self-consistency of \(g_{\mu\nu}(\rho)\) + Clausius on \(\mathcal{L}_g\) | Geometry feeds back into the entropic bookkeeping | Candidate | Ours packages feedback in channel + load, not as \(-\beta\mathcal{R}\) inside a second metric |
| Induced metric \(G\) (Stage 2) | Geometric imprint of structure / \(g_{\mu\nu}(\rho)\) bookkeeping | Shared Stage-2 *role* in ACD-EW toy | Structural (toy constructive for Euclidean \(G[\phi]\)); continuum candidate | \(G\) is a metric operator; \(L\) is a scalar — **\(L\not\equiv G\)** |
| \(\kappa=\alpha_B/\beta_B\) | Newton matching \(\alpha_L\beta_L=4\pi G/c^4\) (and related \(\kappa_{\mathrm{E}}=8\pi G/c^4\)) | Both fix strength of matter–geometry coupling by calibration/structure of action | Analogical / candidate | Different equations being normalized; do not equate \(\alpha_B/\beta_B\) with \(\alpha_L\beta_L\) numerically without a map |
| \(\Lambda_G(\tilde{\mathcal{G}})\ge 0\) small near identity | Cosmological / inflationary recovery via load & boundary growth | Both produce small positive “dark energy–like” effects from information geometry | Analogical | Ours: dynamics of \(L\) and screens; GfE: algebraic functional of G-field only |
| G-field \(\tilde{\mathcal{G}}\) dresses EH | Load reparameterizes \(d\tau\); \(g_{\mu\nu}(\rho)\) self-consistency | Both “dress” pure vacuum geometry with extra structure | Analogical (three open hypotheses in bridge note) | Prefer **not** identifying \(\tilde{\mathcal{G}}\equiv L\) |
| Warm-up \(G=1+\alpha_G(\nabla\phi)^2\), PM flow | Observation channel \(H_c\), split load, load clock | ACD-EW | **Constructive (Euclidean toy)** | Explicitly not Lorentzian weak-field Newton |

**Open hypotheses for G-field vs load** (from bridge note; unchanged):

| Hypothesis | Content | Status |
|------------|---------|--------|
| A | \(\tilde{\mathcal{G}}\) is metric **dressing** — closer to \(g_{\mu\nu}(\rho)\) consistency than to scalar \(L\) | Open |
| B | \(\Lambda_G(\mathcal{G})\) tracks a slow cosmological DOF related to our boundary / inflation recovery | Open |
| C | \(D_{\mu\nu}\) (second derivatives of \(\mathcal{G}\)) parallels entropy-production stiffness \(\gamma_L|dS_c/d\tau|_{\mathrm{reg}}\) | Open |

### 4.3 Symbols / objects that do **not** map (or map poorly)

| Pair | Why not |
|------|---------|
| \(S_c = S(\Phi_g(\rho))\) vs \(\operatorname{Tr}\, g\ln G^{-1}\) | Output entropy of a CPTP channel vs relative entropy of **metrics as operators**. Same broad “information” language; different domain and codomain. |
| \(L\) (dimensionless scalar) vs \(G\) or \(\tilde{\mathcal{G}}\) (metric / operator fields) | Type mismatch. At most: functionals of \(G-\,g\) can *source* a scalar load (as in ACD-EW \(L_E\sim\mathbb{E}[G-1]\)). |
| Master equation \(\partial_t\rho \propto \mathcal{L}_g/(1+\alpha L)\) vs EL equations from \(\delta\mathcal{S}=0\) | Dynamical law class differs (channel/ODE vs variational field equations). |
| Dirac–Kähler topological bosons vs lambda/IDEM/decay-vector matter | Microscopic matter models not identified. |
| Our \(\alpha_L,\beta_L\) vs Bianconi \(\alpha_B,\beta_B\) | Homonymous couplings; different actions. |
| Euclidean PM conductivity \(\rho_i=1/(1+(\nabla\phi/K)^2)\) vs Newtonian \(d\tau=dt/(1+\alpha L)\) | Structural rhyme in “\(1/(1+\cdot)\)” only; different physics. |
| ACD-EW residual \(H_c\) vs continuum \(S_c\) or Araki relative entropy | Toy specialization of output-pattern entropy; not a continuum proof. |

### 4.4 Side-by-side limit chain

| Step | Ours (documented) | GfE (documented) |
|------|--------------------|-------------------|
| 1. Small parameter | \(\alpha L\ll 1\) | \(\alpha_B M\), \(\beta_B\mathcal{R}\) small; \(\tilde\Theta\simeq\tilde I\) |
| 2. Truncation | \(L\approx\beta\rho c^2/\epsilon_0\); drop \(\gamma,\delta\) terms | Expand \(\ln G\) / relative entropy; recover EH (and KG in warm-up) |
| 3. Geometric reading | \(d\tau/dt \leftrightarrow 1+\Phi/c^2\) | Metric \(g\) satisfies Einstein (zero \(\Lambda\)); G-field near identity \(\Rightarrow\) tiny \(\Lambda_G\) only when retained |
| 4. Force law / Poisson | Path J Poisson + Path M \(\alpha\beta=4\pi G/c^4\) match | **Via GR weak field** (standard), not a separate load clock |
| 5. Status | Internal recovery note | External continuum field theory claim |

**Bottom line of the table:** both sides say *low demand \(\Rightarrow\) classical gravity*, but:

- Ours ends the chain at **Newton/Poisson** via a **load clock**.
- GfE ends the documented chain at **Einstein–Hilbert (\(\Lambda=0\))** via a **relative-entropy action** (and G-field dressing away from that limit).

Equating the two chains requires an extra theorem (continuum limit + weak-field dictionary) that is **not** claimed here.

---

## 5. What a future “plug values across” test would require

**Not claimed done.** The bridge note lists this as open item P5 (“Weak-field Newtonian dictionary vs continuum load”).

A serious cross-test would need at least:

| # | Requirement | Why |
|---|-------------|-----|
| T1 | **Shared background spacetime** | e.g. Minkowski + static weak \(g_{00}\), or FLRW linearization — same ansatz on both sides |
| T2 | **Common matter sector** | Either port Dirac–Kähler / scalar warm-up into a channel language, or restrict GfE to a density \(\rho\) with stress tensor \(T_{\mu\nu}\) matching our \(E[\rho]\) |
| T3 | **Linearized GfE equations** | Expand Bianconi Eqs. (modified Einstein + G-field EOM) to \(\mathcal{O}(\Phi/c^2)\); extract effective Poisson or Yukawa-like equation for \(\Phi\). **To verify against Bianconi PDF / follow-on solutions literature** (e.g. Thattarampilly–Zheng papers as continuum solution targets) |
| T4 | **Linearized master-equation sector** | Same background: expand \(d\tau=dt/(1+\alpha L)\), \(L\approx\beta\rho c^2/\epsilon_0\), and \(\mathcal{L}_g\)’s Clausius content to obtain \(\Phi[\rho]\) without *assuming* the final Poisson form |
| T5 | **Parameter map** | Explicit functions: \((\alpha_L,\beta_L,\epsilon_0,\ldots)\leftrightarrow(\alpha_B,\beta_B,\ell_P,\kappa,\ldots)\) such that numerical coefficients of \(\nabla^2\Phi-\,4\pi G\rho\) match (or quantify mismatch) |
| T6 | **G-field freeze-out test** | Set \(\tilde{\mathcal{G}}=\tilde I\) (or integrate out at quadratic order in \(\tilde\epsilon\)); check whether residual \(\Lambda_G\) and \(D_{\mu\nu}\) vanish fast enough to leave pure Newton on solar-system scales |
| T7 | **Load from \(G-g\)** | Construct \(L = L[G-g,\dot S_c,\ldots]\) continuum functional whose low-load expansion reproduces T4; compare to ACD-EW \(L_E\sim\mathbb{E}[G-1]\) as a discrete prototype |
| T8 | **Pass/fail metrics** | Coefficient of Poisson source; PPN \(\gamma,\beta\) if available; presence/absence of extra scalar from G-field; sign of effective \(\Lambda\) |

Until T1–T5 exist on paper (even as a calculation note), “plugging in \(G\) and \(c\)” across frameworks is **not** a defined experiment.

---

## 6. Open calculations / next math steps

Prioritized for the weak-field thread (complements bridge note P4–P6 and THEORY open questions):

| Priority | Calculation | Output |
|----------|-------------|--------|
| **W1** | Write linearized Bianconi equations about Minkowski with static perfect-fluid \(T_{\mu\nu}\); **verify against PDF** every coefficient | Effective equation for \(\Phi\) (and any G-field scalar modes) |
| **W2** | Re-derive our Poisson sketch with explicit \(\epsilon_0\) bookkeeping and a stated identification principle (horizon Clausius vs local \(d\tau\)) | Cleaner internal theorem-level Newton note |
| **W3** | Three-term weak-field dictionary: \(\alpha_B\tilde M\leftrightarrow\beta_L E/\epsilon_0\); curvature \(\leftrightarrow\) which of \(\gamma_L,\delta_L\) or \(g(\rho)\); boundary \(\leftrightarrow\) holographic term | Structural table upgraded from “candidate” only if equations match |
| **W4** | Expand \(\Lambda_G(\tilde I+\tilde\epsilon)\) to quadratic order; compare magnitude to observed \(\Lambda\) / to our inflation recovery scales | Quantitative analogical test for Hypothesis B |
| **W5** | Continuum limit of ACD-EW \(L_E\) as \(h\to 0\); relate to Bianconi warm-up \(G=1+\alpha_G(\nabla\phi)^2\) (T4 in ACD-EW) | Partial constructive path, still Euclidean |
| **W6** | Variational dual of master equation (action whose EL reproduce load-gated channel in a continuum limit) | Would raise bridge from structural to constructive on dynamics class |
| **W7** | Solar-system / PPN constraints on G-field fluctuations vs load corrections beyond Newton | Phenomenology gate for both modified sectors |

---

## 7. Explicit non-claims

This note does **not** claim:

1. That the master equation is derived from Bianconi’s relative-entropy action (or vice versa).
2. That \(L \equiv \tilde{\mathcal{G}}\), \(L \equiv G\), \(S_c \equiv \operatorname{Tr}\, g\ln G^{-1}\), or \(\alpha_L\beta_L \equiv \alpha_B/\beta_B\).
3. That low-load Newton recovery and low-coupling EH recovery have been shown to be **the same limit of one theory**.
4. That ACD-EW (Euclidean PM dual) implies weak-field Lorentzian equivalence.
5. That either framework replaces or supersedes classical GR as established physics.
6. That Bianconi’s paper contains a dedicated Newtonian Poisson derivation identical to ours — **not verified as such**; low coupling \(\to\) Einstein is the documented statement; Newton would be via standard GR linearization.
7. That dark-matter / dark-energy phenomenology of the G-field equals our cosmological load recovery.
8. That “plug in \(G,c\)” numerical cross-validation has been performed (see §5).
9. ~~Completeness of the intermediate Laplacian algebra~~ — **withdrawn**; Path J/M is the recovery (see §2.5 rewrite).

---

## 8. One-page summary table

| Question | Answer in this note |
|----------|---------------------|
| Do both recover “ordinary gravity” at low demand? | **Yes, directionally** — ours: Newton sketch; GfE: EH with \(\Lambda=0\) |
| Same mechanism? | **No claim** — load clock vs relative-entropy action + G-field |
| Best current bridge? | Semantic + structural candidates; Euclidean ACD-EW constructive toy; full continuum open |
| Next concrete math? | Linearized GfE Poisson sector (W1) + cleaned internal Newton derivation (W2) + parameter map (T5) |
| Cite Bianconi how? | Continuum entropic-gravity peer; low-coupling EH existence proof in that framework; **not** as already dual to \(\Phi_g,L\) |

---

## References (repo-local)

| Resource | Role |
|----------|------|
| [emergent-gravity/master-equation.md](../emergent-gravity/master-equation.md) | Canonical \(L\), \(d\tau\), master equation |
| [quantum/Newton.md](../quantum/Newton.md) | Newtonian recovery sketch |
| [papers/external/Bianconi_Gravity_from_entropy_NOTES.md](../papers/external/Bianconi_Gravity_from_entropy_NOTES.md) | GfE digest |
| [bridge-bianconi-relative-entropy.md](bridge-bianconi-relative-entropy.md) | Full-bridge correspondence + open mappings |
| [action-channel-duality-euclidean.md](action-channel-duality-euclidean.md) | Scope boundary: Euclidean dual \(\neq\) continuum equivalence |
| [THEORY.md](../THEORY.md) §3.3 | Project-level continuum bridge status |
| Bianconi, arXiv:2408.14391 / PRD **111**, 066001 (2025) | Primary external GfE source |

---

## 9. Follow-on execution (2026-07-14)

| M-id | Artifact | Outcome |
|------|----------|---------|
| M8 | [m8-newton-recovery-audit.md](m8-newton-recovery-audit.md) | Algebraic gap N1; Path J/M |
| M8+ | [emergent-gravity/recoveries/newtonian/README.md](../emergent-gravity/recoveries/newtonian/README.md) · [quantum/Newton.md](../quantum/Newton.md) | **Path J/M rewrite landed** |
| M7 | [m7-symbol-map.md](m7-symbol-map.md) | Candidates + non-maps |
| M6 | [m6-weak-field-plugtest.md](m6-weak-field-plugtest.md) | **WEAK PASS** shared Poisson; **FAIL** identity |
| M6b | [m6b-next-order-weak-field.md](m6b-next-order-weak-field.md) | Next-order: GfE EOM extras vs load-clock \(\gamma_L,\delta_L\) — **structural FAIL** |
| M6c | [m6c-bianconi-linearization.md](m6c-bianconi-linearization.md) | PDF linearization W1: Poisson PASS; \(\Lambda_G=O(\epsilon^2)\); \(D_{\mu\nu}\) linear structure |

*Comparison note. Preliminary frameworks only. Pack: [PACK_INDEX.md](PACK_INDEX.md) · [OPEN_MATH_DECISION_LOG.md](OPEN_MATH_DECISION_LOG.md).*
