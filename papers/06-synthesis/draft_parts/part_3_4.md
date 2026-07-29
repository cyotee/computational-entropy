# Parts 3–4 — Gravitational channel, load, master equation; Newton recovery (Path J/M)

**Draft status:** Program paper prose (2026-07-15) · Parts 3–4 of `papers/06-synthesis/OUTLINE.md`  
**Stance:** Preliminary research. Prefer under-claiming. Nothing here has GR-level certainty.  
**Canonical sources:** [`emergent-gravity/master-equation.md`](../../../emergent-gravity/master-equation.md) · [`emergent-gravity/recoveries/newtonian/README.md`](../../../emergent-gravity/recoveries/newtonian/README.md)  
**Claims used:** C9, C10, C14 (freeze: [`synthesis/CURRENT_CLAIMS.md`](../../../synthesis/CURRENT_CLAIMS.md))  
**Type safety:** load \(L\) is a **dimensionless scalar**; structure-induced metric \(G\) (GfE) and spacetime metric \(g_{\mu\nu}\) are **metrics**. **\(L \neq G\)**.

---

## 3. Gravitational channel, computational load, and master equation

This section states the continuum **program definitions** of the gravitational channel \(\Phi_g\), computational entropy \(S_c\), dimensionless load \(L\), load clock, and master equation. Formulas are those of the repository canonical note; we do not re-derive them at length here, and we do not claim symbolic identity of this layer with continuum Gravity-from-Entropy (GfE). Rigor for the dynamical law itself is **canonical/program**. The Clausius constraint on the generator is stated as setup for Path J (Part 4); the import of Jacobson’s theorem is **external theorem + modeling assumption**, not an in-repo re-proof.

### 3.1 Gravitational channel \(\Phi_g\) and computational entropy \(S_c\)

We model gravity as an effective **gravitational channel** \(\Phi_g\): a completely positive, trace-preserving (CPTP) map acting on the density operator \(\rho\) of local quantum microstates. In schematic form,

\[
\rho(\tau + \delta\tau)
=
\Phi_g\bigl[\rho(\tau);\, g_{\mu\nu}(\rho)\bigr],
\]

where the channel may depend on a geometry \(g_{\mu\nu}\) that is itself determined (in the self-consistent picture) by the microstate content. The channel is the continuum object that evolves microstates while respecting universal information-processing bounds (Bekenstein capacity, Margolus–Levitin speed limit, Landauer erasure cost) as **program constraints**, not as theorems proved here.

The **computational entropy** realized by the channel at each step is the von Neumann entropy of the **output** state (Tag B in the program’s entropy-object hygiene):

\[
S_c(\Phi_g;\rho)
=
S\bigl(\Phi_g(\rho)\bigr)
=
-\operatorname{Tr}\bigl(\Phi_g(\rho)\log_2\Phi_g(\rho)\bigr).
\]

This is the direct quantum/gravity counterpart of classical computational entropy \(H_c(f;p_X)=H(Y)\) for \(Y=f(X)\): entropy of the **realized output distribution**, independent of the internal mechanics of the map. Informational equivalence of channels that produce the same output entropy remains the foundational reading from Part 1; \(\Phi_g\) is simply the channel whose output statistics we treat as the gravitational computational process.

### 3.2 Computational load \(L\)

Instantaneous information-processing **demand** is quantified by a dimensionless **computational load** \(L(\rho,g)\). The canonical three-term formula is ([`master-equation.md`](../../../emergent-gravity/master-equation.md)):

\[
L(\rho,g)
=
\beta \frac{E[\rho]}{V \epsilon_0}
+
\gamma \left| \frac{d S_c}{d\tau} \right|_{\mathrm{reg}}
+
\delta \frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)},
\]

where \(E[\rho]=\operatorname{Tr}(\rho H)\) is local energy, \(\epsilon_0\) is a reference (Planck-scale) energy density for dimensional bookkeeping, \(\lvert dS_c/d\tau\rvert_{\mathrm{reg}}\) is a regularized rate of computational-entropy production (averaged over a short Margolus–Levitin window to avoid circularity with the load clock), \(S_{\mathrm{boundary}}(\rho)\) is von Neumann entropy on a holographic screen of area \(A\), and \(S_{\mathrm{BH}}(A)=A/(4G\hbar)\) is the Bekenstein–Hawking entropy of that screen. The weights \(\beta,\gamma,\delta\) and the reference \(\epsilon_0\) are fixed, in the gravitational program, by matching conditions in the Newtonian weak-field limit and by saturation bookkeeping for the Bekenstein bound—not by free first-principles prediction of Newton’s \(G\) (see Part 4, Path M / C10).

**Semantic reading (C14).** Prefer reading \(L\) as demand arising from the **scale and rate of possible channel outcomes**: energy-like work density, entropy-production / export flux, and boundary / distinguishability pressure against capacity. Active scrambling, high flux, and many open residual results imply **higher** \(L\). The program **rejects** as primary story an “idle identity stockpile” reading in which load tracks unreduced complexity while the machine is idle. This reading is a **semantic / program convention** until continuum matching is complete; it is frozen at claim C14.

**Three-term roles and discrete microstructure (structural only).** Classical three-slot discrete ledgers \(L^{\mathrm{disc}}=L_E^{\mathrm{disc}}+L_S^{\mathrm{disc}}+L_B^{\mathrm{disc}}\) (M11 Phase 1–2; continuum motivation in [`m11c-continuum-motivation.md`](../../../synthesis/m11c-continuum-motivation.md)) align with the continuum terms by **role**, not by numerical equality:

| Continuum term | Role | Discrete role alignment |
|----------------|------|-------------------------|
| \(\beta E[\rho]/(V\epsilon_0)\) | Active **work** / energy-like density | Ops, redexes, evaluations (\(L_E^{\mathrm{disc}}\)) |
| \(\gamma\lvert dS_c/d\tau\rvert_{\mathrm{reg}}\) | **Export current** / entropy-rate flux | \(H(X\mid Y)\), \(\lvert\Delta H_c\rvert\), decay flips (\(L_S^{\mathrm{disc}}\)) |
| \(\delta S_{\mathrm{boundary}}/S_{\mathrm{BH}}\) | **Open budget** vs capacity | Residual recoverability, \(d_f\), residual ensemble entropy ratio (\(L_B^{\mathrm{disc}}\)) |

**Rigor label:** **structural** role alignment grounded in constructive discrete bookkeeping. We do **not** claim \(L^{\mathrm{disc}}=L(\rho,g)\), do **not** fit \(\alpha,\beta,\gamma,\delta,\epsilon_0\) from gates or shoes, and do **not** assert a hydrodynamic limit of IDEM maps to continuum load (non-claim: IDEM/decay does not fully construct continuum \(L\) or \(G\)).

A monist load (e.g.\ proportional to output entropy alone) fails the locked reading: irreversible maps can **lower** \(H_c\) while **raising** export and work demand. The three axes—how hard the machine is working, how fast possibility is being exported, and how much distinguishability budget remains open—are independently motivated by classical microstructure; continuum \(L\) inherits that **role split** at continuum language level only.

### 3.3 Load clock and master equation

Proper time is reparameterized by load:

\[
d\tau
=
\frac{dt}{1 + \alpha L(\rho,g)}.
\]

The product \(\alpha\beta\) that appears when the energy-density term dominates is fixed by on-shell Newtonian matching as a **calibration** (C10; detail in §4.3):

\[
\alpha\beta = \frac{4\pi G}{c^4}
\quad\text{(repo convention; matching, not free derivation of \(G\)).}
\]

The **master equation** governing laboratory-time evolution is

\[
\frac{d\rho}{dt}
=
\frac{1}{1 + \alpha L(\rho,g)}
\,\mathcal{L}_g\bigl[\rho;\, g_{\mu\nu}(\rho)\bigr],
\]

where \(\mathcal{L}_g\) is the Liouvillian generator of the channel \(\Phi_g\). High load slows the effective evolution rate in \(t\), unifying (at the level of bookkeeping) gravitational and kinematic forms of time dilation under a single dimensionless demand scalar.

### 3.4 Clausius constraint on \(\mathcal{L}_g\) (setup for Path J)

The generator \(\mathcal{L}_g\) is required to satisfy the Clausius relation

\[
\delta Q = T\, dS_c
\]

on every local horizon (Jacobson 1995). This is a **modeling assumption** of the framework: thermodynamic consistency of the channel generator on local Rindler horizons. We state it here as the continuum content that Path J will import; we do **not** re-prove Jacobson’s theorem in this paper. Under that assumption, Einstein dynamics become available as an equation of state of the underlying thermodynamics, and Newtonian Poisson follows by standard weak-field GR (Part 4).

Canonical master-equation prose sometimes says Einstein equations “emerge automatically” from the Clausius constraint. The honest program reading is: **if** \(\mathcal{L}_g\) is constrained by Clausius in Jacobson’s sense, **then** Einstein is imported as external continuum content of that constraint. That is Path J’s first half—not an independent derivation of Einstein from load alone.

### 3.5 Type safety: \(L\) scalar versus metric \(G\) / \(g_{\mu\nu}\)

Load \(L\) is a **dimensionless scalar** (or, locally, a scalar field of demand). It clocks proper time and modulates the rate of \(\rho\)-evolution. It is **not** a metric.

- Spacetime geometry in the master equation is written \(g_{\mu\nu}(\rho)\).  
- In continuum GfE, structure-induced metric objects are denoted \(G\) (matter- or structure-induced; Bianconi program).  
- **\(L \neq G\)** and **\(L \neq g_{\mu\nu}\)**. Identifying load with a metric, or writing “load metric” for continuum \(G\), is a type error and is an explicit non-claim of the program.

Self-consistency of the framework is circular at the level of ontology by design: microstates determine load and (via the Clausius/Einstein content of \(\mathcal{L}_g\)) geometry; geometry modulates \(\Phi_g\). That circularity does **not** license collapsing Stage-1 computational induction, Stage-2 geometric imprint, and Stage-3 continuum GfE into a single symbolic identity of master equation and Bianconi relative-entropy action. In particular:

**Non-claims at this layer.** We do **not** assert master equation \(\Leftrightarrow\) continuum GfE; \(L\equiv G\); \(S_c\equiv\operatorname{Tr} g\ln G^{-1}\); or \(\alpha_L\beta_L\equiv\alpha_B/\beta_B\).

---

## 4. Newton recovery — Path J/M only

### 4.1 Honesty preamble

Newtonian gravity is recovered as a **calibrated low-load regime** of the master-equation framework (**C9**), **not** by taking the Laplacian of a pointwise identification \(\Phi\propto\rho_m\).

| Claim piece | Status / rigor |
|-------------|----------------|
| Master equation + load definitions | Canonical (Part 3) |
| Clausius on \(\mathcal{L}_g\) \(\Rightarrow\) Einstein (Jacobson 1995) | **External theorem + modeling assumption** |
| Einstein weak field \(\Rightarrow\) \(\nabla^2\Phi=4\pi G\rho_m\) | Standard GR |
| Matching \(\alpha\beta=4\pi G/c^4\) so load clock agrees with Newtonian \(\Phi\) **on shell** | **Calibration** (Path M; **C10**) |
| Pointwise \(\Phi\propto\rho_m\Rightarrow\nabla^2\Phi\propto\nabla^2\rho_m\Rightarrow\) Poisson | **Invalid / withdrawn** |

**What is not claimed.** We do not derive Newton independently of Jacobson/Einstein input. We do not claim free derivation of Newton’s constant \(G\) from load bookkeeping alone. We do not claim that \(\gamma=\delta=0\) is proved—only that those contributions are modeled as subdominant in the leading weak-field regime.

Canonical recovery: [`emergent-gravity/recoveries/newtonian/README.md`](../../../emergent-gravity/recoveries/newtonian/README.md). Audit of the historical algebraic gap: [`synthesis/m8-newton-recovery-audit.md`](../../../synthesis/m8-newton-recovery-audit.md).

### 4.2 Setup: low-load, weak-field, slow-motion assumptions

Under the master equation and load of Part 3, the Newtonian analysis uses:

| # | Assumption |
|---|------------|
| L1 | \(\alpha L\ll 1\) |
| L2 | Curvature small; \(v\ll c\) |
| L3 | Entropy-production and holographic terms **subdominant**: \(\gamma,\delta\) contributions \(\ll\) energy-density term (modeling assumption; not quantified) |
| L4 | \(\mathcal{L}_g\) obeys \(\delta Q=T\,dS_c\) on every local Rindler horizon (Jacobson consistency) |

Under L1–L3,

\[
L
\approx
\beta\frac{E[\rho]}{V\epsilon_0}
\approx
\beta\frac{\rho_m c^2}{\epsilon_0},
\]

where \(\rho_m\) is classical mass density (\(T_{00}\approx\rho_m c^2\)).

### 4.3 Path J — Clausius → Einstein → Poisson

Path J is the **derivation path for the Poisson equation**.

**Step J1 — Thermodynamic consistency of the generator.**  
By L4, heat flux and computational-entropy change on local horizons satisfy \(\delta Q=T\,dS_c\).

**Step J2 — Jacobson’s theorem (imported).**  
Jacobson (1995): the Clausius relation on local Rindler horizons, with entropy proportional to horizon area and Unruh temperature, implies the **Einstein field equations** as an equation of state of the underlying thermodynamics (up to a cosmological constant fixed by the vacuum). In this framework we **import** that theorem as the continuum content of L4. We do **not** re-prove Jacobson here. Rigor: **external theorem + modeling assumption**.

**Step J3 — Weak-field GR → Poisson.**  
Linearize Einstein about Minkowski with a static, non-relativistic perfect fluid. Standard textbook result:

\[
\nabla^2\Phi = 4\pi G\,\rho_m,
\qquad
g_{00} \approx -\bigl(1+2\Phi/c^2\bigr),
\quad
\sqrt{-g_{00}}\approx 1+\Phi/c^2.
\]

**Conclusion of Path J.** Newtonian Poisson is available as the weak-field limit of the Einstein thermodynamics already built into \(\mathcal{L}_g\) under L4. No Laplacian of \(\rho_m\) is required. The nonlocal structure of \(\Phi\) (inverse-square forces from compact sources) is inherited from GR, not invented by load algebra.

### 4.4 Path M — Load-clock calibration (matching, not derivation)

Path J yields a metric with Newtonian potential \(\Phi[\rho_m]\). Path M fixes how the **load reparameterization** tracks the same \(\Phi\). Rigor: **calibration**, conditional on Path J (**C10**).

**Step M1 — Proper-time expansion.** For \(\alpha L\ll 1\),

\[
d\tau
=
\frac{dt}{1+\alpha L}
\approx
dt\bigl(1-\alpha L\bigr)
\approx
dt\Bigl(1-\alpha\beta\frac{\rho_m c^2}{\epsilon_0}\Bigr).
\]

**Step M2 — Static weak-field clock.** For a static observer,

\[
\frac{d\tau}{dt}
=
\sqrt{-g_{00}}
\approx
1+\frac{\Phi}{c^2}.
\]

**Step M3 — On-shell matching (not pointwise \(\Phi\propto\rho_m\)).**  
Do **not** identify \(\Phi/c^2=-\alpha\beta\rho_m c^2/\epsilon_0\) as a **local algebraic law**. That identification would give \(\Phi\propto\rho_m\) pointwise, which is not Newtonian gravity.

Instead: for solutions of Poisson with the same \(\rho_m\), require the **leading linear response** of the load clock to agree with the Newtonian redshift **on shell**.

*Worked example (uniform ball).* For constant density \(\rho_m\) in a ball of radius \(R\), the interior potential is

\[
\Phi_{\mathrm{in}}(r)
=
-2\pi G\rho_m\Bigl(R^2-\frac{r^2}{3}\Bigr)
\quad(r\le R).
\]

At the center, \(\Phi_{\mathrm{in}}(0)/c^2=-2\pi G\rho_m R^2/c^2\). The load expansion at the center gives \(d\tau/dt-1\approx-\alpha\beta\rho_m c^2/\epsilon_0\). Matching order of magnitude for a characteristic scale \(R\sim R_\star\) (or equating coefficients after fixing a reference geometry where \(\Phi\) is proportional to \(\rho_m R^2\)) calibrates \(\alpha\beta\) relative to \(\epsilon_0\). The **repo-standard product**

\[
\alpha\beta = \frac{4\pi G}{c^4}
\]

is the convention that absorbs \(\epsilon_0\) and geometric scale into the definitions of \(\beta\) and \(\epsilon_0\) so that \(\alpha\cdot\beta\cdot c^2/\epsilon_0\) reproduces \(\lvert\Phi\rvert/c^2\) **for the calibrated family of solutions**, not for arbitrary pointwise \(\rho_m\).

**Honest reading of \(\alpha\beta=4\pi G/c^4\):** it is a **matching condition** between load bookkeeping and Newtonian \(\Phi\), **conditional on Path J already supplying Poisson**. It is **not** a free derivation of \(G\) from first principles independent of Newton/GR (**C10**).

**Step M4 — What the load clock then means.** With Path J + M: geometry / \(\Phi\) is fixed by Einstein thermodynamics (Jacobson) + weak field; \(L\approx\beta\rho_m c^2/\epsilon_0\) raises demand where energy density is high; \(d\tau=dt/(1+\alpha L)\) **tracks** the same slowing of clocks that GR encodes in \(g_{00}\), once \(\alpha\beta\) is calibrated; Newtonian force \(\mathbf{F}=-m\nabla\Phi\) remains the effective description for slow massive probes—no extra force postulate beyond Path J’s Einstein/Poisson content.

### 4.5 Withdrawn path (do not revive)

The following chain is **not** a valid recovery of Newtonian gravity (historical drafts; documented in M8; **withdrawn**):

1. Postulate \(d\tau/dt=1/(1+\alpha L)\) with \(L=\beta\rho_m c^2/\epsilon_0\).  
2. Set \(d\tau/dt=1+\Phi/c^2\).  
3. Conclude \(\Phi=-\alpha\beta c^4\rho_m/\epsilon_0\) **pointwise**.  
4. Take \(\nabla^2\) and “match” to \(4\pi G\rho_m\).

**Why it fails.** Newtonian \(\Phi\) is **nonlocal** (\(\Phi=-G\int\rho_m/|x-x'|\,dV'\)). Pointwise \(\Phi\propto\rho_m\) does not produce inverse-square forces from compact sources. Algebraically,

\[
\nabla^2\Phi
=
-\,\alpha\beta\frac{c^4}{\epsilon_0}\,\nabla^2\rho_m
\]

is **not** Poisson unless \(\nabla^2\rho_m\propto-\rho_m\).

> **Disallowed one-liner:** “Taking the Laplacian of \(\Phi\propto\rho\) yields \(\nabla^2\Phi=4\pi G\rho\).”

> **Allowed one-liner:** In the low-load regime the energy-density term dominates \(L\). With \(\mathcal{L}_g\) constrained by the Clausius relation, the Einstein equation (Jacobson) and its weak-field Poisson limit are available; matching the load-induced proper-time factor to the Newtonian potential fixes \(\alpha\beta=4\pi G/c^4\). Newtonian gravity is thus a **calibrated low-load regime** of the framework.

### 4.6 Recovery chain (allowed language)

```text
Clausius on L_g  ──(Jacobson)──►  Einstein equation
                                      │
                                      ▼
                              weak field / slow motion
                                      │
                                      ▼
                              ∇²Φ = 4πG ρ_m     (Path J)
                                      │
                                      ▼
                    match load clock dτ/dt ≈ 1+Φ/c²
                    on shell  ⇒  αβ = 4πG/c⁴     (Path M)
```

**Role of coefficients at leading Newton.** \(\epsilon_0\) is reference energy density making \(L\) dimensionless (absorbed into \(\beta\) bookkeeping under Path M). The product \(\alpha\beta\) (with \(\epsilon_0\)) is fixed by Path M. Weights \(\gamma\) and \(\delta\) are **dropped** at leading Newton under L3; they re-enter next-order / nonequilibrium / near-horizon regimes and must not be silently equated with GfE extras \(D_{\mu\nu},\Lambda_G\) (that identification is a **structural FAIL** at next order—Part 6 / M6b; not claimed here).

### 4.7 Other recoveries — status only (deferred)

Black-hole horizons, cosmological expansion (including inflation narratives), Lloyd-type ultimate computational capacity, and unified accounts of gravitational and kinematic time dilation appear in historical and outline form under `emergent-gravity/recoveries/` and legacy `quantum/` drafts. Those regimes are **not** presented here as settled at Path J/M rigor. High-load / horizon physics elevates the boundary term \(\delta\); cosmology elevates boundary growth and expansion bookkeeping; capacity bounds touch Lloyd-type limits. Each requires the same honesty pass as Newton: explicit assumptions, external theorems labeled as such, calibration distinguished from free derivation, and no revival of withdrawn algebraic shortcuts. Until that pass is complete, the program’s **settled** gravitational recovery claim remains **Path J/M Newtonian Poisson only** (**C9**, **C10**). Cross-framework weak-field contact with continuum GfE (shared Poisson via GR, **not** framework identity) is deferred to Part 6 (M6 WEAK PASS / FAIL).

---

## Claim inventory for Parts 3–4

| ID | Statement used | Where | Rigor |
|----|----------------|-------|-------|
| **C9** | Newton recovery = Path J/M only (Clausius → Einstein → Poisson; load-clock on-shell match) | §4 | Path J: external thm + assumption; Path M: calibration |
| **C10** | \(\alpha\beta=4\pi G/c^4\) is on-shell calibration, not free derivation of \(G\) | §3.3 preview; §4.4 | **calibration** |
| **C14** | Prefer \(L\) as demand from scale/rate of channel outcomes (energy + entropy flux + boundary); active scrambling → higher \(L\) | §3.2 | **semantic** (program convention) |

**Structural (not claim-ID frozen as C-number):** three-term continuum \(L\) **roles** align with discrete \(L_E,L_S,L_B\) (M11c)—**not** continuum equality.

**Explicit non-claims touched:** ME \(\Leftrightarrow\) GfE; \(L\equiv G\); free derivation of \(G\); Newton from pointwise \(\Phi\propto\rho\) Laplacian (**withdrawn**); IDEM/decay fully constructs continuum \(L\) or \(G\); other recoveries settled at Path J/M rigor.

---

## Sources (absolute paths)

| Role | Path |
|------|------|
| Outline Parts 3–4 | `/Users/cyotee/Development/github-cyotee/computational-entropy/papers/06-synthesis/OUTLINE.md` |
| Canonical \(\Phi_g\), \(L\), master eq | `/Users/cyotee/Development/github-cyotee/computational-entropy/emergent-gravity/master-equation.md` |
| Canonical Path J/M | `/Users/cyotee/Development/github-cyotee/computational-entropy/emergent-gravity/recoveries/newtonian/README.md` |
| M8 audit (withdrawn path) | `/Users/cyotee/Development/github-cyotee/computational-entropy/synthesis/m8-newton-recovery-audit.md` |
| Claims freeze C9–C10, C14 | `/Users/cyotee/Development/github-cyotee/computational-entropy/synthesis/CURRENT_CLAIMS.md` |
| Three-role structural motivation | `/Users/cyotee/Development/github-cyotee/computational-entropy/synthesis/m11c-continuum-motivation.md` |
| Claim gate | `/Users/cyotee/Development/github-cyotee/computational-entropy/synthesis/CLAIM_GATE.md` |

---

*Jacobson, T. (1995). Thermodynamics of spacetime: The Einstein equation of state. Phys. Rev. Lett. **75**, 1260.*
