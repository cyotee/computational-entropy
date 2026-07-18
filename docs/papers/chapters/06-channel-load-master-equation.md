# 6. Gravitational channel, computational load, and master equation

This section states the continuum **program definitions** of the gravitational channel $\Phi_g$, computational entropy $S_c$, dimensionless load $L$, load clock, and master equation (layer **M**). Formulas are the program's continuum definitions; we do not re-derive them at length here, and we do not claim symbolic identity of this layer with continuum Gravity-from-Entropy (GfE; layer **G**). Rigor for the dynamical law itself is **canonical/program**. The Clausius constraint on the generator is stated as setup for Path J (Part 4); the import of Jacobson's theorem is **external theorem + modeling assumption**, not re-proved here.

### 3.1 Gravitational channel $\Phi_g$ and computational entropy $S_c$

We model gravity as an effective **gravitational channel** $\Phi_g$: a completely positive, trace-preserving (CPTP) map acting on the density operator $\rho$ of local quantum microstates. In schematic form,


$$
\rho(\tau + \delta\tau)
=
\Phi_g\bigl[\rho(\tau);\, g_{\mu\nu}(\rho)\bigr],
$$


where the channel may depend on a geometry $g_{\mu\nu}$ that is itself determined (in the self-consistent picture) by the microstate content. The channel is the continuum object that evolves microstates while respecting universal information-processing bounds (Bekenstein capacity, Margolus--Levitin speed limit, Landauer erasure cost) as **program constraints**, not as theorems proved here.

The **computational entropy** realized by the channel at each step is the von Neumann entropy of the **output** state (Tag B in the program's entropy-object hygiene):


$$
S_c(\Phi_g;\rho)
=
S\bigl(\Phi_g(\rho)\bigr)
=
-\operatorname{Tr}\bigl(\Phi_g(\rho)\log_2\Phi_g(\rho)\bigr).
$$


This is the direct quantum/gravity counterpart of classical computational entropy $H_c(f;p_X)=H(Y)$ for $Y=f(X)$: entropy of the **realized output distribution**, independent of the internal mechanics of the map. Informational equivalence of channels that produce the same output entropy remains the foundational reading from Part 1; $\Phi_g$ is simply the channel whose output statistics we treat as the gravitational computational process.

### 3.2 Computational load $L$

Instantaneous information-processing **demand** is quantified by a dimensionless **computational load** $L(\rho,g)$. The canonical three-term formula is (Eq.\ (\ref{eq:load}) family below):


$$
L(\rho,g)
=
\beta \frac{E[\rho]}{V \epsilon_0}
+
\gamma \left| \frac{d S_c}{d\tau} \right|_{\mathrm{reg}}
+
\delta \frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)},
$$


where $E[\rho]=\operatorname{Tr}(\rho H)$ is local energy, $\epsilon_0$ is a reference (Planck-scale) energy density for dimensional bookkeeping, $\lvert dS_c/d\tau\rvert_{\mathrm{reg}}$ is a regularized rate of computational-entropy production (averaged over a short Margolus--Levitin window to avoid circularity with the load clock), $S_{\mathrm{boundary}}(\rho)$ is von Neumann entropy on a holographic screen of area $A$, and $S_{\mathrm{BH}}(A)=A/(4G\hbar)$ is the Bekenstein--Hawking entropy of that screen. The weights $\beta,\gamma,\delta$ and the reference $\epsilon_0$ are fixed, in the gravitational program, by matching conditions in the Newtonian weak-field limit and by saturation bookkeeping for the Bekenstein bound---not by free first-principles prediction of Newton's $G$ (see Part 4, Path M / C10).

**Semantic reading (C14).** Prefer reading $L$ as demand arising from the **scale and rate of possible channel outcomes**: energy-like work density, entropy-production / export flux, and boundary / distinguishability pressure against capacity. Active scrambling, high flux, and many open residual results imply **higher** $L$. The program **rejects** as primary story an "idle identity stockpile" reading in which load tracks unreduced complexity while the machine is idle. This reading is a **semantic / program convention** until continuum matching is complete; it is frozen at claim C14.

**Three-term roles and discrete microstructure (structural only).** Classical three-slot discrete ledgers $L^{\mathrm{disc}}=L_E^{\mathrm{disc}}+L_S^{\mathrm{disc}}+L_B^{\mathrm{disc}}$ (M11 Phase 1--2; continuum motivation in Appendix A) align with the continuum terms by **role**, not by numerical equality:

| Continuum term | Role | Discrete role alignment |
|----------------|------|-------------------------|
| $\beta E[\rho]/(V\epsilon_0)$ | Active **work** / energy-like density | Ops, redexes, evaluations ($L_E^{\mathrm{disc}}$) |
| $\gamma\lvert dS_c/d\tau\rvert_{\mathrm{reg}}$ | **Export current** / entropy-rate flux | $H(X\mid Y)$, $\lvert\Delta H_c^{\mathrm{disc}}\rvert$, decay flips ($L_S^{\mathrm{disc}}$) |
| $\delta S_{\mathrm{boundary}}/S_{\mathrm{BH}}$ | **Open budget** vs capacity | Residual recoverability, $d_f$, residual ensemble entropy ratio ($L_B^{\mathrm{disc}}$) |

**Rigor label:** **structural** role alignment grounded in constructive discrete bookkeeping. We do **not** claim $L^{\mathrm{disc}}=L(\rho,g)$, do **not** fit $\alpha,\beta,\gamma,\delta,\epsilon_0$ from gates or shoes, and do **not** assert a hydrodynamic limit of IDEM maps to continuum load (non-claim: IDEM/decay does not fully construct continuum $L$ or $G$).

A monist load (e.g.\ proportional to output entropy alone) fails the locked reading: irreversible maps can **lower** $H_c^{\mathrm{disc}}$ while **raising** export and work demand. The three axes---how hard the machine is working, how fast possibility is being exported, and how much distinguishability budget remains open---are independently motivated by classical microstructure; continuum $L$ inherits that **role split** at continuum language level only ($L^{\mathrm{disc}}\neq L(\rho,g)$).

### 3.3 Load clock and master equation

Proper time is reparameterized by load:


$$
d\tau
=
\frac{dt}{1 + \alpha L(\rho,g)}.
$$


The product $\alpha\beta$ that appears when the energy-density term dominates is fixed by on-shell Newtonian matching as a **calibration** (C10; detail in §4.3):


$$
\alpha\beta = \frac{4\pi G}{c^4}
\quad\text{(matching convention; not free derivation of $G$).}
$$


The **master equation** governing laboratory-time evolution is


$$
\frac{d\rho}{dt}
=
\frac{1}{1 + \alpha L(\rho,g)}
\,\mathcal{L}_g\bigl[\rho;\, g_{\mu\nu}(\rho)\bigr],
$$


where $\mathcal{L}_g$ is the Liouvillian generator of the channel $\Phi_g$. High load slows the effective evolution rate in $t$, unifying (at the level of bookkeeping) gravitational and kinematic forms of time dilation under a single dimensionless demand scalar.

### 3.4 Clausius constraint on $\mathcal{L}_g$ (setup for Path J)

The generator $\mathcal{L}_g$ is required to satisfy the Clausius relation


$$
\delta Q = T\, dS_c
$$


on every local horizon (Jacobson 1995). This is a **modeling assumption** of the framework: thermodynamic consistency of the channel generator on local Rindler horizons. We state it here as the continuum content that Path J will import; we do **not** re-prove Jacobson's theorem in this program report. Under that assumption, Einstein dynamics become available as an equation of state of the underlying thermodynamics, and Newtonian Poisson follows by standard weak-field GR (Part 4).

Canonical master-equation prose sometimes says Einstein equations "emerge automatically" from the Clausius constraint. The honest program reading is: **if** $\mathcal{L}_g$ is constrained by Clausius in Jacobson's sense, **then** Einstein is imported as external continuum content of that constraint. That is Path J's first half---not an independent derivation of Einstein from bits or from load alone.

### 3.5 Type safety: $L$ scalar versus metric $G$ / $g_{\mu\nu}$

Load $L$ is a **dimensionless scalar** (or, locally, a scalar field of demand). It clocks proper time and modulates the rate of $\rho$-evolution. It is **not** a metric.

- Spacetime geometry in the master equation is written $g_{\mu\nu}(\rho)$.  
- In continuum GfE, structure-induced metric objects are denoted $G$ (matter- or structure-induced; Bianconi program).  
- **$L \neq G$** and **$L \neq g_{\mu\nu}$**. Identifying load with a metric, or writing "load metric" for continuum $G$, is a type error and is an explicit non-claim of the program.

Self-consistency of the framework is circular at the level of ontology by design: microstates determine load and (via the Clausius/Einstein content of $\mathcal{L}_g$) geometry; geometry modulates $\Phi_g$. That circularity does **not** license collapsing Stage-1 computational induction, Stage-2 geometric imprint, and Stage-3 continuum GfE into a single symbolic identity of master equation and Bianconi relative-entropy action. In particular:

**Non-claims at this layer.** We do **not** assert master equation $\Leftrightarrow$ continuum GfE; $L\equiv G$; $S_c\equiv\operatorname{Tr} g\ln G^{-1}$; or $\alpha_L\beta_L\equiv\alpha_B/\beta_B$.

---
