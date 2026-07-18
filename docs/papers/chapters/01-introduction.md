# 1. Introduction

Entropy, computation, and gravitation are usually treated as three separate intellectual economies: statistical mechanics tracks ensembles; computer science tracks algorithms and channels; general relativity tracks geometry. A recurring family of proposals suggests that these economies are not independent---that gravity, or at least some of its continuum phenomenology, can be read as a form of information bookkeeping. Thermodynamic derivations of Einstein's equation from local horizon Clausius relations [Jacobson, Phys. Rev. Lett. **75**, 1260 (1995)], holographic capacity bounds [Bekenstein; 't Hooft; Susskind], and more recent continuum *Gravity-from-Entropy* (GfE) constructions based on relative entropy of metrics [Bianconi, Phys. Rev. D **111**, 066001 (2025); arXiv:2408.14391] all treat spacetime dynamics as constrained by entropy balance rather than as a free geometric postulate. In parallel, classical information theory has long treated computation as a map from random inputs to output laws, with Shannon and von Neumann entropies measuring the unpredictability of those laws [Shannon; Cover and Thomas; Nielsen and Chuang]. Landauer's principle further ties irreversible information disposal to a physical heat cost [Landauer, IBM J. Res. Dev. **5**, 183 (1961)].

This paper starts from a deliberately simple premise: **computational entropy** should be the entropy of what a map or channel *emits*---the output distribution---rather than a measure of internal circuit size or algorithmic complexity alone. Once that premise is fixed, questions about gravity become questions about a *channel*: what is the output entropy of a gravitational process, what dimensionless demand ("load") does it impose, and how does that demand reparameterize proper time? The same premise forces classical microstructure---Boolean gates, composition of maps, decay of recoverable inputs, game-as-channel models---to speak the same bookkeeping language as continuum entropic gravity, even when the two layers are not yet identified by a hydrodynamic limit.

The motivation is therefore not a single slogan ("bits cause gravity") but a bookkeeping problem: local entropy can drop under irreversible maps; global conservation requires export; continuum theories encode demand in metrics, actions, and clocks; any honest bridge must track which object is scalar load, which is metric structure, which is output entropy, and which claims are constructive versus merely semantic. Under-claiming is intentional. Nothing in this program has general-relativity-level certainty; external GfE literature is treated as a peer research program, not as an established foundation on par with Einstein gravity.

## 1.1 The integration gap

Two research threads have run largely in parallel.

On the **classical / computational** side, one can define output Shannon entropy $H_c$ of finite maps, audit irreversible gates by the chain rule $H(X)=H(Y)+H(X\mid Y)$, and organize expanded identities (arity, decay vectors, AST metrics---"IDEM" microstructure) that describe *how* a computation forgets or retains inputs. Composition laws show that cumulative export cost can be **path-dependent**: the same final output law can be reached by circuits that pay different total export. Single-shot export $H(X\mid Y)$ contacts Landauer's bit-count under a reset protocol. These results are constructive on finite alphabets; they do not by themselves produce a spacetime metric.

On the **continuum entropic-gravity** side, GfE proposes an action based on relative entropy between the spacetime metric $g$ and a matter- or structure-induced metric $G$, yielding modified Einstein equations, a $G$-field dressing, and an emergent cosmological term $\Lambda_G$ [Bianconi, Phys. Rev. D **111**, 066001 (2025)]. Euclidean warm-up models identify anisotropic diffusion of Perona--Malik type with gradient flow of a simplified GfE energy [Bianconi, arXiv:2503.14048]. Applications within the GfE family recover inflationary cosmology without a dedicated inflaton [Thattarampilly and Zheng, arXiv:2509.23987] and spherically symmetric black-hole geometries with controlled corrections and evaporation-like mass loss [Thattarampilly, Zheng, and Kakkat, arXiv:2602.13694]. Adjacent work recovers semiclassical Einstein dynamics from nonequilibrium generalized entropy [Kumar, arXiv:2404.16912], supporting Clausius-type layers without entanglement-equilibrium assumptions.

The gap is not a shortage of either language; it is the lack of an **integrated** program that (i) freezes honest definitions of computational entropy, (ii) states a gravitational channel and load-clock dynamics, (iii) recovers Newtonian Poisson only under explicitly labeled external inputs and calibrations, (iv) constructs a Euclidean dual to the GfE *warm-up* without promoting lattice denoising to empirical gravity, and (v) measures continuum contact by weak-field agreement *and* structural non-equivalence rather than by forced symbolic identity of actions. Many narratives jump from "entropy appears in both stories" to "the stories are the same." This paper refuses that jump.

## 1.2 Contributions

This paper reports a frozen research program. Contributions, with rigor labels, are:

- **Definitions of computational entropy.** Classical $H_c(f;p_X):=H(Y)$ (Shannon or differential entropy of the output of a map $f$ under input law $p_X$); quantum/gravity $S_c(\Phi;\rho):=S(\Phi(\rho))$ (von Neumann entropy of a channel output). Informational equivalence: maps that induce the same output entropy are interchangeable for any prediction depending only on that output law. **Rigor:** constructive (standard information theory).

- **Gravitational channel, load, and master equation.** Gravity is modeled as a CPTP channel $\Phi_g$ with dimensionless computational load $L$ and load clock
  \[
  d\tau=\frac{dt}{1+\alpha L},
  \]
  so that the master dynamics reparameterize a Liouvillian by demand. Continuum $L$ is multi-axial (energy-like, entropy-flux, boundary/capacity roles), motivated by---but **not identified with**---discrete three-slot ledgers $L^{\mathrm{disc}}$. **Rigor:** framework-canonical definitions; continuum role match is structural motivation only.

- **Newtonian recovery only via Path J/M.** Path **J** imports Jacobson's Clausius→Einstein argument on local horizons for the gravitational sector, then standard weak-field GR to Poisson $\nabla^2\Phi=4\pi G\rho_m$. Path **M** matches the load clock on shell to Newtonian redshift for a calibrated solution family, with the convention $\alpha\beta=4\pi G/c^4$ as **calibration**, not a free derivation of Newton's constant from bits alone. A pointwise Laplacian path $\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho$ is **withdrawn**. **Rigor:** external theorem + modeling assumption (J); calibration (M).

- **Discrete load: path dependence and Landauer contact.** Cumulative export $\sum L_S$ is path-dependent under circuit composition at fixed final output entropy. Single-shot $L_S^{\mathrm{disc}}:=H(X\mid Y)$ is the Landauer bit-count under a residual-reset protocol ($Q\ge k_B T\ln 2\cdot H(X\mid Y)$). Monist $L\propto H_c$ fails on irreversible gates with low output entropy and high export. **Rigor:** constructive finite ledgers + external Landauer inequality.

- **Action--Channel Duality, Euclidean warm-up (ACD-EW).** A constructive dual between Bianconi's GfE warm-up (induced structure metric $G[\phi]$, Perona--Malik flow) and an observation channel with split load and load clock. Residual dual of edge-aware reconstruction versus isotropic heat is **time-windowed** (T1′), with a unified pure residual window $U_\star=[1.36,2.40]$ under a soft ensemble conductivity hypothesis $\mathrm{PCRH}_b$ ($\rho_b=0.42$). Joint lattice toys score full support on fixed dual scorecards as **pattern witnesses**, not continuum gravity confirmation. **Rigor:** constructive dual + analytic/hybrid residual claims; $\mathrm{PCRH}_b$ soft.

- **Weak-field GfE contact (M6): WEAK PASS / FAIL.** Both the load-channel framework (via Path J/M) and continuum GfE (via low-coupling Einstein/GR) yield the same leading Poisson equation---a **WEAK PASS** on shared Newtonian endpoint. Framework identity **FAILS**: primary entropy objects, Euler--Lagrange structure, and next-order correction slots diverge. Identifying load-clock corrections $(\gamma_L,\delta_L)$ with GfE metric extras $(D_{\mu\nu},\Lambda_G)$ is a **structural promotion no-go** without an extra rule moving load into the metric sector. **Rigor:** analysis under stated embeddings; not a new continuum derivation.

## 1.3 Roadmap

Section 2 develops foundations: $H_c$ and $S_c$, informational equivalence, global conservation with local export (including the irreversible AND ledger), and the three-stage mental model---computational induction, geometric imprint, continuum GfE macro---without collapsing stages.

Section 3 treats classical microstructure: IDEM/decay ontology as design language; discrete three-slot load $L^{\mathrm{disc}}$; composition and path dependence; Landauer contact; honesty limits on continuum identification.

Section 4 states the gravitational channel $\Phi_g$, multi-term load $L$, load clock, and master equation, with type safety and the semantic reading of demand as scale/rate of possible channel outcomes (high flux and scrambling raise $L$).

Section 5 presents Path J/M Newtonian recovery, the withdrawn pointwise path, and the status of other recoveries (black holes, cosmology, capacity) as **not** yet at Path J/M honesty.

Section 6 develops ACD-EW, residual dual claims on $U_\star$, joint toys as pattern witnesses, and warm-up energy descent versus residual dual (distinct layers).

Section 6B (integrated literature) surveys continuum GfE applications---inflation and spherical black holes---as **external recovery targets**, relates them honestly to our deferred recoveries, and positions nonequilibrium generalized-entropy routes as support for a Clausius-type layer rather than as identity theorems.

Section 7 analyzes weak-field contact with continuum GfE: WEAK PASS on Poisson, FAIL of framework identity, next-order structural FAIL, and the promotion no-go.

Section 8 synthesizes open items (continuum limit of discrete load, full warm-up $\Gamma$-limits, Lorentzian dual, pure dual hypotheses), restates non-claims, and freezes the program conclusion spine.

Appendices collect notation and type-safety tables, claim checklists (settled vs non-claims), reproduction notes for finite ledgers and dual toys, and bibliography stubs for external GfE and thermodynamic-gravity literature.

## 1.4 Explicit non-claims

Readers should not import any of the following as theorems of this paper without new work:

1. The master equation is **not** equivalent to continuum Bianconi GfE (symbolic, dynamical, or "same equations in disguise").
2. Load $L$ is **not** the structure-induced metric $G$; $S_c$ is **not** identified with $\operatorname{Tr} g\ln G^{-1}$; continuum load coefficients are **not** numerically identified with Bianconi's coupling parameters.
3. Residual dual domination of Perona--Malik over heat does **not** hold for all short times $t\in(0,t_\star]$; the correct statement is time-windowed (T1′ / $U_\star$).
4. Pure residual dual statements still depend on a **soft** ensemble hypothesis ($\mathrm{PCRH}_b$); we do not claim a pathwise Dirichlet-form proof without certificate.
5. Newtonian gravity is **not** recovered from a pointwise $\Phi\propto\rho$ Laplacian identity (that path is withdrawn).
6. Next-order load-clock terms are **not** identified with GfE metric extras without an explicit promotion structure.
7. Lattice denoising and dual toys are **not** empirical gravity.
8. External GfE papers are **not** asserted as established on par with general relativity.
9. IDEM/decay microstructure and finite ledgers do **not** construct continuum $L$ or metric $G$.

**Type safety (locked throughout).** Computational load $L$ is a **dimensionless scalar** demand that reparameterizes a clock. Structure-induced $G$ in GfE (or its edgewise warm-up cousin) is a **metric** (or metric-like field). These live in different mathematical categories: **$L\neq G$**. Discrete three-slot ledgers $L^{\mathrm{disc}}$ motivate continuum roles but are not numerically equal to continuum $L(\rho,g)$. When multiple entropy objects appear (map Shannon $H_c$, channel von Neumann $S_c$, toy residual scores, game-channel entropy), they are not freely equated.

**Stance.** The constructions and ledgers reported here are real; the dual pattern is robust under stated hypotheses; the weak-field co-class with GR is informative. None of this is a claim of completed physics. The paper's purpose is an honest integration of parallel threads under explicit labels---constructive, structural, semantic, calibration, external theorem + assumption, hybrid-experimental---so that future work can add missing theorems without rewriting the spine.
