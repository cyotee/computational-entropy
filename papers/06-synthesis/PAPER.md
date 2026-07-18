# Computational Entropy and Emergent Gravity: From Output Distributions to Load-Gated Geometry

**Authors:** cyotee doge
**Affiliation:** Independent
**Version:** Integrated research paper draft v1.0 (2026-07-15)  
**Status:** Standalone manuscript for review and publication decision  

**Abstract-level type safety.** Computational load $L$ is a dimensionless scalar demand; structure-induced metric quantities $G$ (GfE) and spacetime $g_{\mu\nu}$ are geometric. **$L \neq G$.** This work is preliminary research; nothing herein claims GR-level certainty or master-equation $\Leftrightarrow$ continuum Gravity-from-Entropy identity.

---

## Abstract

Computational entropy is defined as the entropy of a map or channel's **output** distribution: classical Shannon (or differential) $H_c$, and quantum/gravity von Neumann $S_c$. In this program, gravity is modeled as a CPTP channel $\Phi_g$ whose instantaneous demand is a dimensionless **load** $L$ that reparameterizes proper time via $$d\tau=dt/(1+\alpha L)$$. Newtonian Poisson is recovered only through **Path J/M** (Clausius on local horizons → Einstein → weak-field GR, with on-shell load-clock calibration $\alpha\beta=4\pi G/c^4$), not a withdrawn pointwise Laplacian identity. A constructive Euclidean dual (**ACD-EW**) links Bianconi's Gravity-from-Entropy **warm-up** (induced structure metric $G[\phi]$, Perona--Malik flow) to an observation channel with split load and load clock; residual dual of PM versus heat is **time-windowed** (T1′ / unified pure window $U_\star$), and joint toys serve as **pattern witnesses**, not continuum gravity confirmation. Weak-field contact with continuum GfE is a **WEAK PASS** on shared Poisson and a **FAIL** of framework identity (M6/M6b).

This document is an honest **program report**: it freezes settled claims, marks rigor labels (constructive / structural / semantic / calibration / external theorem), and states explicit non-claims. Classical IDEM/decay machinery is connected by a design dictionary plus constructive discrete ledgers (Phase 1 AND-gate; Phase 2 multi-step Boolean, tiny SKI, minimal shoe). Relationship witnesses (D13) include **path-dependent** cumulative export cost $\sum L_S$ under circuit composition (Direct $\sum L_S\approx 1.189$ vs Circuit $\approx 2.189$, same final $H(Z)$) and **Landauer contact** in which single-shot $L_S=H(X\mid Y)$ is the bit-count bounded by heat $Q\ge k_B T\ln 2\cdot H(X\mid Y)$. Discrete load $L^{\mathrm{disc}}$ is **not** continuum $L$; scalar $L$ is **not** metric $G$; the master equation is **not** continuum GfE.

**Keywords:** computational entropy; CPTP channel; computational load; thermodynamic gravity; Jacobson Clausius; Gravity from Entropy; Perona--Malik; action--channel duality; IDEM; Landauer principle; information export


## Contents
1. Introduction  
2. Related work and intellectual landscape  
3. Results (program conclusions)  
4. Foundations --- computational entropy  
5. Classical microstructure (IDEM, discrete load, Landauer, composition)  
6. Gravitational channel, load, and master equation  
7. Newtonian recovery (Path J/M)  
8. Euclidean dual (ACD-EW)  
9. Continuum GfE contact and applications  
10. Synthesis and open program  
11. Final conclusions  
Appendix A. Constructive witnesses  
Appendix B. Claims and non-claims  
Appendix C. Open mathematical avenues  
References  


---

## Non-claims banner

This report is **preliminary research**. Constructions and numerical ledgers are real; **nothing has GR-level certainty**. Do **not** read the body as asserting any of the following without new work:

1. Master equation $\Leftrightarrow$ Bianconi continuum Gravity-from-Entropy (GfE).  
2. $L \equiv G$, $S_c \equiv \operatorname{Tr} g\ln G^{-1}$, or continuum load coefficients identified with Bianconi's.  
3. Residual dual domination for all $t\in(0,t_\star]$ (use T1′ / $U_\star$ instead).  
4. Pure T1′ with no soft hypotheses (PCRH$_b$ remains ensemble-certified).  
5. Newton from pointwise $\Phi\propto\rho$ Laplacian (**withdrawn**).  
6. Next-order load terms $\gamma_L,\delta_L$ equal GfE extras $D_{\mu\nu},\Lambda_G$.  
7. Lattice denoising as empirical gravity.  
8. External GfE papers established on par with GR.  
9. IDEM/decay fully constructs continuum $L$ or metric $G$.

**Type safety (locked throughout):** load $L$ is a **dimensionless scalar**; structure-induced $G$ is a **metric** (or edgewise cousin). **$L \neq G$**. Discrete three-slot ledgers $L^{\mathrm{disc}}$ are **not** numerically equal to continuum $L(\rho,g)$. Entropy objects are tagged when ambiguous (M10: map $H_c$, $S_c$, $H_c^{\mathrm{toy}}$, $H_c^{\mathrm{game}}$, $H_c^{\mathrm{disc}}$).

---

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

# 2. Related work and intellectual landscape

## 2. Related work and intellectual landscape

The present program sits at a confluence of information theory, nonequilibrium thermodynamics, holographic gravity, continuum Gravity-from-Entropy (GfE) constructions, classical models of computation, and structure-preserving reconstruction. The literatures below are not treated as interchangeable under a single slogan of "entropy equals gravity." They supply distinct primary objects, dynamical laws, and standards of rigor. Our contribution is a channel-and-load formulation of computational entropy---classical $H_c$ as the entropy of a map's output law, quantum/gravity $S_c$ as the von Neumann entropy of a channel output---together with a dimensionless load $L$ that reparameterizes proper time, an explicit bridge posture toward continuum GfE, and a classical microstructure program (IDEM, decay, games) that is intended to ground, not to replace, continuum geometry. Throughout, peer constructions are cited as peers: continuum GfE and related thermodynamic recoveries are important targets and comparisons, not theorems of the present framework, and nothing in this section is claimed at the certainty of classical general relativity.

### 2.1 Information theory and irreversible computation

Shannon's mathematical theory of communication established entropy as a functional of a probability distribution over messages or channel outputs, and thereby fixed the modern language of uncertainty, rate, and coding (Shannon, 1948). In the textbook development of Cover and Thomas, the same viewpoint is refined into mutual information, conditional entropy, data-processing inequalities, and the systematic study of how maps act on distributions (Cover and Thomas, 2006). That orientation---entropy as a property of an **output law** induced by a process, rather than as an inventory of internal micro-instructions---is the information-theoretic backbone of computational entropy in the present sense. For a classical map $f$ taking input $X\sim p_X$ and producing $Y$, one studies $H(Y)$ (or differential entropy $h(Y)$ in continuous settings). Two maps that induce the same $p_Y$ are informationally equivalent for any prediction that depends only on the output law. This is deliberately closer to Shannon's output-centric bookkeeping than to algorithmic complexity as a measure of program length: Kolmogorov complexity and related notions quantify description length of individual strings, whereas computational entropy, as used here, quantifies the statistical pattern of a computation's possible results under a specified input measure.

Irreversible computation links that statistical picture to thermodynamics. Landauer's principle asserts that logically irreversible operations incur a minimum heat cost of order $k_B T\ln 2$ per bit of information erased (Landauer, 1961). In modern information-thermodynamic language, for an irreversible map with declared system output $Y$ and forgotten preimage information $H(X\mid Y)$, the average heat of erasure is bounded below by
$$
Q \ge k_B T\ln 2\cdot H(X\mid Y)
$$
(when Shannon entropy is measured in bits). The present program treats that contact carefully: export $H(X\mid Y)$ is a constructive finite-alphabet ledger quantity on deterministic maps; Landauer supplies the thermodynamic lower bound on heat associated with that export. The equality of scales is not a free derivation of Newton's constant, black-hole temperature, or continuum load from a gate alone.

Bennett's analyses of reversible computation and the thermodynamics of computation sharpened the complementary point: computation need not destroy information if one retains garbage bits and reverses the process; the thermodynamic cost is tied to **erasure and resetting**, not to computation as such (Bennett, 1973; Bennett, 1982). That distinction matters for gravitational narratives that equate "overwriting of microstates" with Landauer heat: the cost attaches to irreversible loss of distinguishability from the observer's declared system, not to every elementary step of a reversible unitary. Global fine-grained conservation with local apparent entropy reduction is the consistent reading: the chain rule $H(X)=H(Y)+H(X\mid Y)$ on deterministic maps is an identity, not a second-law violation.

Finally, computational complexity theory (time, space, circuit depth, interactive protocols) measures resources required to realize a map, whereas Shannon-style computational entropy measures the unpredictability of the map's **output distribution**. The two are related but not identical: a hard function can have low output entropy (e.g., a deterministic constant), and a simple function can concentrate or spread probability mass in nontrivial ways. The present framework uses resource language only where needed (load as demand, Margolus--Levitin-type rate limits in physical regimes) and keeps $H_c$/$S_c$ as entropy objects of outputs. Complexity enters gravity more directly in holographic complexity conjectures (Section 2.3); there the primary object is circuit cost or action, not Shannon entropy of a classical output alphabet.

### 2.2 Thermodynamic and entropic gravity

A central modern root of "gravity from thermodynamics" is Jacobson's derivation of the Einstein field equations as an equation of state (Jacobson, 1995). The argument requires that every local Rindler horizon satisfy the Clausius relation $\delta Q = T\,dS$, with entropy proportional to horizon area and $T$ the Unruh temperature. Variation of the heat flux across the horizon then implies the Einstein equation (up to a cosmological constant) as a thermodynamic identity, rather than as a fundamental dynamical postulate. In the present program, this result is imported as **Path J**: the Liouvillian generator of the gravitational channel is required to obey Clausius with $dS$ identified with a change in computational entropy $dS_c$ on local horizons. Path J is therefore an **external theorem plus modeling assumption**, not a re-proof of Jacobson's argument inside the channel formalism. Weak-field Newtonian Poisson then follows from standard linearization of Einstein gravity about Minkowski spacetime, not from a pointwise identification of gravitational potential with density.

Verlinde's entropic-force proposal interprets gravity as an emergent force associated with holographic information on screens, recovering Newtonian acceleration and, in extensions, relativistic structure from entropy gradients and equipartition of energy on screens (Verlinde, 2011; see also the earlier preprint discussion Verlinde, 2010). The narrative is powerful and widely discussed, but it remains more heuristic than Jacobson's Clausius derivation: the microstates of the screen, the precise entropy functional, and the status of the force law as fundamental versus effective have been debated extensively. In our comparison table (Section 2.7), Verlinde supplies an **entropic-force / holographic-screen** peer: the holographic boundary contribution to load is a computational analogue of screen information demand, not a second independent derivation of Poisson's equation.

Padmanabhan and collaborators have developed a related line in which spacetime dynamics is linked to holographic equipartition and the thermodynamic properties of horizons, often emphasizing the emergence of gravitational field equations from the balance of degrees of freedom on bulk and boundary (Padmanabhan, 2010). We cite this only as optional context within the broader thermodynamic-gravity family; the present recovery of Newton does not rely on a preferred equipartition postulate beyond what is already encoded in Path J and standard weak-field GR.

Underlying all horizon thermodynamics is the Bekenstein--Hawking area law: black-hole entropy is proportional to horizon area,
$$
S_{\mathrm{BH}} = \frac{A}{4G\hbar}
$$
(in units where $c=k_B=1$ as appropriate), establishing entropy as a geometric observable and area as an information capacity (Bekenstein, 1973; Hawking, 1975). That result is the fixed point of holographic bookkeeping in load: a boundary term compares screen entropy to $S_{\mathrm{BH}}$, and saturation of capacity is the natural strong-field / horizon regime of the same dimensionless demand that is small in the Newtonian weak field.

Nonequilibrium extensions go beyond equilibrium Clausius on stationary horizons. Kumar recovers the semiclassical Einstein equation from a generalized entropy $S_{\mathrm{gen}}$ and a nonequilibrium quantum expansion, without relying on entanglement-equilibrium assumptions of the Faulkner--Guica--Hartman--Myers type (Kumar, arXiv:2404.16912). That work is a valuable peer for the **Clausius / thermodynamic layer** of any master-equation story: it shows that semiclassical gravity can be organized around generalized entropy production rather than only equilibrium entanglement first law. We treat it as adjacent support for thermodynamic consistency conditions on channel generators, not as a derivation of our load functional or of continuum GfE.

### 2.3 Holography, complexity, and cosmic computation

Holographic duality and the Ryu--Takayanagi (RT) formula relate boundary entanglement entropy to the area of bulk minimal surfaces (Ryu and Takayanagi, 2006). Subsequent refinements (quantum extremal surfaces, islands) have produced a detailed account of the Page curve for evaporating black holes: early radiation entropy rises, then falls as interior degrees of freedom are correctly accounted for in the generalized entropy (Page, 1993; Almheiri et al., 2019, 2020, and related developments). In the present narrative, RT and Page-curve physics are **contextual peers**: they demonstrate that gravitational geometry and entropy bookkeeping are tightly coupled, and that "processed information" in quantum gravity is already measured by von Neumann-type entropies. They do not, by themselves, identify $S_c = S(\Phi_g(\rho))$ with RT area, nor do they construct continuum load $L$.

Susskind's complexity--geometry conjectures propose that bulk volumes or bulk actions track boundary quantum-circuit complexity---Complexity equals Volume (CV) and Complexity equals Action (CA) (Susskind, 2016; Brown et al., 2016). These conjectures elevate **computational cost** rather than Shannon entropy of a classical output alphabet as the dual of geometry. Our framework shares the broad slogan that gravity and computation are linked, but refuses free identification: $S_c$ is an output entropy, not circuit complexity; load $L$ is a scalar demand that clocks proper time, not a bulk volume functional. Where black-hole interiors exhibit late-time complexification, the program may offer a **semantic** reading in which sustained high-load overwriting tracks linear growth of effective complexity, but that reading is not a proof of CV/CA.

Lloyd's analysis of the ultimate physical limits of computation bounds the number of elementary operations and the number of registerable bits available to the observable universe, using energy, Margolus--Levitin-type speed limits, and holographic or gravitational degrees of freedom (Lloyd, 2002). Cosmic-capacity recoveries in emergent-gravity programs typically integrate such bounds over cosmic history. In our setting, capacity statements are **consistency targets** for a closed computational universe whose local demand is $L$, not independent postulates that replace Einstein gravity. They close the circle from microscopic information processing to cosmology without forcing identity between Lloyd's operation count and Bianconi's relative entropy of metrics.

### 2.4 Gravity from Entropy (Bianconi and follow-ons)

The continuum research line closest to the present program's Stage-3 target is Bianconi's Gravity from Entropy (GfE) and its immediate follow-ons. These works are **continuum peers**: variational or phenomenological field theories in which geometry and matter are co-determined by entropic or relative-entropic principles. They are not theorems of the channel-and-load framework, not established foundations on par with general relativity, and not claimed as derived from computational entropy $H_c$/$S_c$ or load $L$.

**Bianconi, Gravity from entropy (Phys. Rev. D 111, 066001, 2025; arXiv:2408.14391).** Bianconi proposes an entropic action built from the **quantum relative entropy** between the spacetime metric $g$, treated as a local quantum operator (effective density-matrix-like object), and a **matter-induced metric** $G$. Schematically, topological extensions package geometry and Dirac--Kähler matter so that
$$
\tilde G = \tilde g + \alpha \tilde M - \beta \tilde{\mathcal{R}},
$$
and the Lagrangian density takes the form of a relative (cross) entropy,
$$
\mathcal{L} = \operatorname{Tr}\,\tilde g\,\ln \tilde G^{-1},
$$
related to Araki-type relative entropy for operator algebras. An auxiliary **G-field** linearizes the variational problem, keeps the equations of motion second order (avoiding Ostrogradsky-type pathologies), and rewrites the theory as a dressed Einstein--Hilbert sector plus dressed matter. An **emergent cosmological term** $\Lambda_G$ depends only on the G-field,
$$
\Lambda_G = \frac{1}{2\beta}\operatorname{Tr}_F\bigl(\tilde{\mathcal{G}} - \tilde I - \ln\tilde{\mathcal{G}}\bigr) \ge 0,
$$
and is small when the G-field is near the identity. At low coupling the theory recovers Einstein--Hilbert gravity with vanishing $\Lambda$ together with the topological matter sector; the full equations are modified Einstein equations with dressed curvature, $\Lambda_G$, and additional G-field structures $D_{\mu\nu}$. A scalar warm-up with $G = g + \alpha M$ and $M_{\mu\nu}$ built from gradients of $\phi$ yields a logarithmic action that reduces to a massless Klein--Gordon kinetic term at weak coupling.

The semantic alignment with the present program is clear: geometry is not an independent absolute backdrop; it is co-determined with the information structure of matter; low "demand" recovers GR/Newton; high demand produces departures (emergent $\Lambda_G$, modified equations). The **structural** differences are equally clear and must not be erased. Bianconi's primary entropy object is relative entropy of **metrics-as-operators**; ours is computational entropy of a **channel output**. Bianconi's dynamics are Euler--Lagrange equations from an action; ours are a master equation with load-gated proper time $$d\tau=dt/(1+\alpha L)$$. Bianconi's auxiliary G-field is a metric dressing with second-derivative structures in the field equations; our $L$ is a **dimensionless scalar** demand. Type safety forbids writing $L \equiv G$ or $S_c \equiv \operatorname{Tr}\, g\ln G^{-1}$. Weak-field contact can be a shared Poisson end-state via Einstein/GR (a WEAK PASS of co-class with GR) while mechanism identity and next-order corrections fail (structural FAIL of framework equivalence). Those distinctions are program locks, not temporary pedantry.

**Bianconi, Beyond holography (arXiv:2503.14048).** In a Euclidean warm-up setting, Bianconi identifies classical **Perona--Malik (PM) anisotropic diffusion** as the gradient flow of a GfE-type warm-up action between a support metric and an image- or structure-induced metric. This result is of exceptional operational value: it supplies a discrete/algorithmic dual of a relative-entropy geometric action that is already standard in image processing. The present program's Action--Channel Duality (Euclidean warm-up, ACD-EW) uses exactly that layer: structure-induced $G[\phi]$, PM flow as the GfE-side reconstructor, and an observation channel with residual/output entropy proxies and split load on the channel side. Honesty requires stating the scope: ACD-EW is a **constructive dual on the Euclidean warm-up layer**, not a derivation of Lorentzian modified Einstein equations, not empirical gravity from lattice denoising, and not continuum equivalence of the master equation with full GfE.

**Thattarampilly and Zheng, Inflation from entropy (arXiv:2509.23987).** Working within the GfE continuum setting, these authors study vacuum modified Friedmann equations and report inflationary regimes without a fundamental inflaton field, including a phantom branch and CMB-compatible $(r,n_s)$ under a slow-roll map in appropriate parameter regimes. The paper is a **cosmological recovery inside GfE**, useful as Stage-3 phenomenology in the peer literature. It is not a derivation of inflation from our load clock, and we do not import its parameter fits as theorems of the channel framework.

**Thattarampilly, Zheng, and Kakkat, spherically symmetric black holes and spontaneous emission (arXiv:2602.13694).** This follow-on constructs spherically symmetric black-hole solutions in GfE with Schwarzschild leading order plus higher-order corrections (including $O(r^{-4})$ structures), confronts observational bounds (e.g., S2/EHT-type constraints on coupling parameters), and discusses dynamical mass loss with an entropic-leakage contribution. Again, the work is a **GfE-internal black-hole recovery**, a peer for horizon and evaporation narratives, not a proof that Hawking radiation equals Landauer cost of $\Phi_g$ or that load saturation is identical to GfE leakage terms.

Collectively, the GfE lineage is the strongest recent continuum target for a staged bridge: computational induction (Stage 1) $\to$ geometric imprint (Stage 2) $\to$ continuum relative-entropy gravity (Stage 3). The bridge is only as strong as its maps. Semantic co-class is already meaningful; constructive Euclidean warm-up duality is available on a restricted layer; full continuum identity of actions, entropy objects, and master equations is **explicitly not claimed**.

### 2.5 Classical computation models and games

A long-standing gap in information-theoretic gravity is the missing microscopic computational substrate: continuum actions and holographic screens do not by themselves specify which classical reduction systems, decay patterns, or game-theoretic filtrations induce load-like demand. The present program's classical thread develops **IDEM** (expanded identity plus metadata)---arity, decay vectors marking which inputs are recoverable from outputs, function unidentifiability $d_f$, and AST-level metrics---as a microstructure program for entropy export and multi-step composition. Decay vectors formalize irreversibility at the level of preimage structure: components that flip under reduction encode which variables become underivable, linking logical irreversibility to the export term $H(X\mid Y)$ in finite ledgers. This is our contribution's **classical context**, not an external theorem: discrete three-slot load bookkeeping $L^{\mathrm{disc}}$ is design-and-ledger constructive on gates and small circuits; it is **not** continuum $L(\rho,g)$ and does not construct metric $G$.

Games enter as entropy-reducing or entropy-tracking computations under partial information. Predictive play induces conditional output laws $H(Y_k\mid\mathcal{F}_{k-1})$ with respect to a filtration of observed cards or moves; that game Shannon entropy is a legitimate $H_c$-family object for decision processes, but it must not be conflated with residual dual scores on lattice belief fields used only as pattern witnesses. The scientific point is modest: structured multi-agent or multi-step classical processes produce the same kind of output-law bookkeeping that computational entropy was defined to capture.

Adjacent external literature on **probabilistic $\lambda$-calculus**, quantitative semantics, and information-loss characterizations of reduction provides a mathematical neighborhood for stochastic computation and entropy change under evaluation, without automatically supplying gravity. We cite that neighborhood as **adjacent**, not as a completed embedding: probabilistic operational semantics and entropy of reduction paths are natural classical peers for IDEM/decay, but overclaiming a theorem-level map from $\lambda$-terms to Einstein equations would violate the program's under-claiming stance. The intended use is compositional discipline---how entropy and export behave under sequential and parallel combination of maps---before any continuum limit is attempted.

### 2.6 Anisotropic diffusion and observation channels

Perona and Malik introduced anisotropic diffusion as an edge-preserving alternative to isotropic heat flow in image processing (Perona and Malik, 1990). Conductivities that decrease with gradient magnitude smooth noise in flat regions while retaining edges; the resulting nonlinear PDEs and their regularizations (including Catté-type modifications) became standard tools for denoising and scale-space analysis. In Bianconi's Beyond holography program (Section 2.4), PM is reinterpreted as the gradient flow of a GfE warm-up relative-entropy action. That reinterpretation is the hinge between continuum entropic geometry and algorithmic reconstruction.

The present program treats **observation and denoising as computational channels**. A hidden structure $\phi_\star$ is observed through noise, $y=\phi_\star+\eta$; a reconstructor (heat, PM, or load-gated PM) produces $\hat\phi(t)$; residual energy and edge-location uncertainty supply specialized output-quality entropies; load tracks the intensity of structure-induced metric deformation and entropy-production rates and reparameterizes the reconstruction clock. This is a Euclidean laboratory for action--channel duality, not a claim that medical image denoising measures spacetime curvature. Lattice fields $\phi$ are test signals on a flat discrete manifold; "jumps" are edges in test data, not gravitational wells. The scientific yield is a constructive dual pattern and time-windowed residual comparisons, not empirical GR.

### 2.7 Positioning of the present work

The table below summarizes primary entropy objects, dynamics, microstructure, and Newtonian recovery across representative frameworks. Entries are deliberately coarse: they mark **what is being varied and what is being claimed**, not a full literature review of every variant.

| Framework | Primary entropy object | Dynamics | Microstructure | Newton recovery |
|-----------|------------------------|----------|----------------|-----------------|
| Jacobson (1995) | Horizon entropy $\propto$ area; Clausius $\delta Q=T\,dS$ | Einstein as equation of state from local Rindler thermodynamics | Quantum field / Unruh horizons (no classical gate model) | Weak-field GR $\Rightarrow$ Poisson (via Einstein) |
| Verlinde (2010/2011) | Holographic screen information / entropy gradients | Entropic force from screen equipartition and information density | Screen microstates (schematic) | Emergent $F=ma$ / Newtonian limit from entropy gradients |
| Bianconi GfE (2025+) | Relative entropy of metrics, $\operatorname{Tr}\,g\ln G^{-1}$ (Araki-related) | Variational EL / modified Einstein; G-field; $\Lambda_G$; PM as warm-up gradient flow | Topological / Dirac--Kähler matter; network precursors | Low coupling $\to$ EH $\to$ weak-field Poisson via GR |
| Kumar $S_{\mathrm{gen}}$ (arXiv:2404.16912) | Generalized entropy $S_{\mathrm{gen}}$ | Nonequilibrium thermodynamic recovery of semiclassical Einstein | Quantum expansion / QFT degrees of freedom | Semiclassical Einstein $\Rightarrow$ weak-field GR limits |
| Present work: $\Phi_g + L + H_c/S_c$ | Output Shannon $H_c$ / von Neumann $S_c$ of channel outputs; export $H(X\mid Y)$ classically | CPTP channel + load $L$; $$d\tau=dt/(1+\alpha L)$$; Clausius on $\mathcal{L}_g$ | IDEM / decay / games (discrete ledgers); Euclidean observation toys | **Path J/M only**: Clausius $\to$ Einstein (imported) $\to$ Poisson; $\alpha\beta=4\pi G/c^4$ on-shell calibration |

**What we share.** With Jacobson, we take thermodynamic consistency on local horizons as the bridge from information bookkeeping to Einstein gravity (imported, not re-proved). With Verlinde and holography, we accept that boundary information capacity and screen-like terms organize strong-field demand. With Bianconi GfE, we share the broad program that geometry is co-determined with matter's information structure, that low demand recovers Einstein/Newton, and that a Euclidean relative-entropy warm-up has an algorithmic dual in anisotropic diffusion. With Kumar, we share interest in nonequilibrium entropy production as a route to semiclassical gravitational equations. With classical information theory, we share output-centric entropy and Landauer contact for irreversible export.

**What we refuse to identify.** We refuse $L \equiv G$: load is a dimensionless scalar; $G$ is a metric (or edgewise cousin). We refuse $S_c \equiv \operatorname{Tr}\, g\ln G^{-1}$: computational entropy is an output entropy of a channel, not relative entropy of metric operators. We refuse master equation $\Leftrightarrow$ full continuum GfE action and EL system. We refuse residual dual of PM versus heat as continuum gravity confirmation, and lattice denoising as empirical gravity. We refuse free derivation of Newton's constant from load alone: Path M is on-shell calibration conditional on Path J. We refuse IDEM/decay as a completed construction of continuum $L$ or $G$. We refuse next-order load-clock coefficients as identical to GfE extras $D_{\mu\nu}$ and $\Lambda_G$ without a constructive map. External GfE papers remain peers in an active research program, not GR-level foundations.

In short, the intellectual landscape supplies thermodynamic gravity, holographic complexity, continuum relative-entropy actions, and classical irreversible computation as **resources and peers**. The present work contributes a single operational triad---output computational entropy, gravitational CPTP channel, and load-clocked master equation---plus a staged bridge posture that keeps Euclidean constructive duality where it is earned and continuum identity where it is not. We now develop the framework in detail.

# 3. Results (program conclusions)

**What "concluded" means here.** A **program conclusion** is a statement this research freeze may assert under an explicit rigor label (constructive finite model, hybrid-experimental toy, external theorem + modeling assumption, calibration, structural bookkeeping, or semantic program convention). It is **not** a claim of GR-level certainty, continuum derivation from IDEM, or symbolic identity of the master equation with Bianconi Gravity-from-Entropy (GfE). Positive conclusions **P1--P11** collect the spine; **refuted / withdrawn** items must not re-enter the narrative. Full claim inventory (C1--C14), dual claims A--D, and non-claims N1--N9 remain authoritative in Section 3 and Appendix B. The full program-conclusions spine (same numbering when present) lives in:

- **Section 3 and Appendix B** (canonical conclusions index; may be maintained in parallel with this draft)

### Positive conclusions P1--P11

Aligned with Section 3 and Appendix B. One-line forms; body sections carry full rigor.

| ID | Conclusion (one line) | Rigor | Pointer |
|----|------------------------|-------|---------|
| **P1** | Computational entropy is **output** entropy: classical $H_c(f;p_X):=H(Y)$; quantum/gravity $S_c(\Phi;\rho):=S(\Phi(\rho))$. | constructive (def.) | §1.1--1.2 |
| **P2** | Local entropy drop is **export**, not destruction: chain rule $H(X)=H(Y)+H(X\mid Y)$; AND export $\approx 1.189$. | constructive | §1.4, §2.4 · T1 |
| **P3** | Protocol R: $L_S^{\mathrm{disc}}:=H(X\mid Y)$ is the Landauer bit-count; $Q\ge k_B T\ln 2\cdot H(X\mid Y)$. | constructive + external Landauer | §2.8 · T4 · Appendix A.3 |
| **P4** | $\sum L_S$ is **path-dependent**: Direct $\approx 1.189$ vs Circuit $\approx 2.189$ at same final $H(Z)$. | constructive | §2.7 · T3 · Appendix A.2 |
| **P5** | Three load **axes** required: $L_E$ (work), $L_S$ (export flux), $L_B$ (capacity); monist $L\propto H_c^{\mathrm{disc}}$ fails on AND. | structural bookkeeping | §2.3, §2.9 · M11/M11c |
| **P6** | Continuum $L(\rho,g)$ is **role-motivated** by $L^{\mathrm{disc}}$, **not identified** with it; $L\neq G$. | structural motivation | §2.9--2.10, §3.2 · M11c |
| **P7** | Newton only via **Path J/M** (Clausius→Einstein→Poisson; $\alpha\beta=4\pi G/c^4$ calibration); pointwise Laplacian **withdrawn**. | external thm + assumption / calibration | §4 · C9--C10 |
| **P8** | ACD-EW Euclidean dual constructive; residual dual **time-windowed** $U_\star=[1.36,2.40]$ (PCRH$_b$ soft); toys **6/6** pattern only. | constructive + analytic + hybrid | §5 · C1--C5 · M1g |
| **P9** | Layer W: PM descends matched warm-up energy (M5c); residual dual stays Layer D --- not ME $\Leftrightarrow$ GfE. | external lit + constructive | §5.5 · M5c |
| **P10** | M6: **WEAK PASS** shared Poisson via Einstein/GR; **FAIL** framework identity (M6b next-order structural FAIL). | WEAK PASS / FAIL | §6 · C11--C13 |
| **P11** | **R4a:** next-order $\gamma_L,\delta_L$ vs $D_{\mu\nu},\Lambda_G$ is a **promotion no-go** without extra structure. | structural no-go | §6.4, §8 · m6d |

**Supporting freezes (CURRENT_CLAIMS):** C14 high-flux $L$ reading underwrites P5--P6; load-PM mild time-change dual (**C8**) sits under P8.

### Refuted / withdrawn (W1--W6)

| ID | Item | Status |
|----|------|--------|
| **W1** | Pointwise $\Phi\propto\rho\Rightarrow\nabla^2$ Newtonian Poisson | **Withdrawn** (invalid; Path J/M only) |
| **W2** | Residual dual for all $t\in(0,t_\star]$ (raw T1) | **False**; use T1′ / $U_\star$ |
| **W3** | $L\equiv G$ or $S_c\equiv\operatorname{Tr} g\ln G^{-1}$ | **Refused** (type safety / N2) |
| **W4** | Master equation $\Leftrightarrow$ continuum GfE | **Refused** (N1; M6 FAIL identity) |
| **W5** | IDEM/Phase 1--2 **constructs** continuum $L$ or $G$ | **Refused** (N9; P6 non-identity) |
| **W6** | Lattice denoising / dual toys = empirical gravity | **Non-claim** (N7; Layer D pattern only) |

Also frozen (not W-ids): pure T1′ with no soft hypotheses (N4); $\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G$ without promotion (N6 / P11); GfE as GR-peer foundation (N8); primary load as idle identity stockpile (rejected C14 reading).

**Pointer.** Full spine (P/W/O + external inputs): Section 3 and Appendix B. Claims freeze: Section 3 and Appendix B. Claim gate: Section 3 and Appendix B.

---

# 4. Foundations --- Computational entropy, equivalence, and conservation

## 1.1 Definition of computational entropy

The program's primary classical and quantum objects are standard information-theoretic entropies of **outputs**, not of internal algorithm complexity alone. The canonical source is Section 1.

**Premise.** Any map that transforms random inputs induces a marginal distribution on outputs. The predictability of that output law is an entropy. Computational entropy quantifies the statistical pattern of possible results of a computation, independent of the internal mechanics that produced it.

**General case.** For any map $f$ --- deterministic, stochastic, or quantum channel --- taking input $X\sim p_X$ and producing output $Y$, computational entropy is the entropy of the induced marginal $p_Y$:

- **Classical discrete** (Tag **A** when unambiguous; Tag **E** on finite M11 maps): Shannon entropy of the output mass function  
  
$$
  H_c(f; p_X) := H(Y) = -\sum_y p_Y(y)\,\log_2 p_Y(y).
  
$$


- **Classical continuous:** differential Shannon entropy of the output density  
  
$$
  H_c(f; p_X) := h(Y) = -\int f_Y(y)\,\log_2 f_Y(y)\,dy.
  
$$


- **Quantum / gravity channel** (Tag **B**): von Neumann entropy of the channel output  
  
$$
  S_c(\Phi;\rho_X) := S\bigl(\Phi(\rho_X)\bigr) = -\operatorname{Tr}\bigl(\Phi(\rho_X)\log_2\Phi(\rho_X)\bigr).
  
$$


In the gravity thread, the gravitational channel $\Phi_g$ acts on a local density operator $\rho$, and $S_c = S(\Phi_g(\rho))$ is the corresponding output entropy (canonical master-equation side: Eq.\ (\ref{eq:load}) family below). Classical $H_c$ and quantum $S_c$ share the **role** "entropy of what the channel emits," not a free symbolic identity of every repository object named $H_c$.

**Rigor:** definitions are **constructive** in the sense of standard Shannon/von Neumann theory on finite alphabets and density operators; the program's use of $S_c$ on $\Phi_g$ is framework-canonical, not a new information-theory theorem.

## 1.2 Informational equivalence of maps

**Key property.** Two or more different maps --- whether deterministic, probabilistic, or quantum --- are **informationally equivalent** if they induce output distributions with the same computational entropy. The internal mechanics (algorithm, intermediate randomness, or quantum circuit layout) do not enter the definition; only the final statistical pattern of possible outputs does.

This property is what makes computational entropy a unifying measure across classical gates, lambda reduction, games-as-maps, and CPTP channels: any probability-based prediction that depends only on $p_Y$ is shared by all maps with that $p_Y$.

## 1.3 Worked continuous example: $\sqrt{U}$ versus $\max(U_1,U_2)$

Consider two genuinely different functions on independent uniforms $U,U_1,U_2\sim\mathrm{Uniform}[0,1]$:

- Function 1: $Y_1=\sqrt{U}$ (square root of one uniform).  
- Function 2: $Y_2=\max(U_1,U_2)$ (maximum of two independent uniforms).

Both induce the **same** output PDF on $[0,1]$,


$$
f(y)=2y,
$$


and therefore the same differential computational entropy


$$
H_c(Y)=-\int_0^1 2y\log_2(2y)\,dy = -1+\frac{1}{2\ln 2}\approx -0.27865\ \mathrm{bits}.
$$


(The reflected map $Y_3=\min(U_1,U_2)$ is informationally equivalent under the substitution $z=1-y$.) Despite completely different internal operations, any prediction that depends only on the law of $Y$ --- e.g. $\mathbb{P}(Y>0.7)$, mean, variance --- is identical. This is the exact content of informational equivalence for continuous classical maps (Section 1.1).

## 1.4 Global conservation and local transfer: the AND-gate ledger

A common apparent paradox is that a computation can **reduce** local entropy (high-entropy random inputs → lower-entropy structured outputs), seemingly violating the second law. The framework resolves this by **global conservation with local transfer**: entropy is not destroyed; it is exported from the declared system output into environment / preimage registers that an observer of $Y$ alone does not hold.

### Classical irreversible AND (constructive)

Let $X=(X_1,X_2)$ be i.i.d. fair bits, so $H(X)=2$ bits. Let $Y=X_1\land X_2$. Then


$$
P(Y=1)=\tfrac14,\qquad P(Y=0)=\tfrac34,
$$


and the **declared system** computational entropy is the binary entropy of $Y$:


$$
H_c = H(Y) = h_2\bigl(\tfrac14\bigr)\approx 0.811278\ \mathrm{bits}.
$$


The "missing" mass relative to the input is **export**, not destruction:


$$
H(X\mid Y)\approx 1.188722\ \mathrm{bits},
$$


and the chain rule for a deterministic map is an identity,


$$
H(X)=H(Y)+H(X\mid Y),
$$


verified to machine precision ($<10^{-12}$) in the Phase 1 ledger (Appendix A.1). Rounding for exposition: **output $\approx 0.811$ bits**, **export $\approx 1.189$ bits**, total $2$.

Branch-wise, the export is concentrated on the ambiguous output:

| $Y$ | $P(Y)$ | Preimage size | $H(X\mid Y=y)$ |
|-------|----------|---------------|------------------|
| $1$ | $1/4$  | $1$         | $0$            |
| $0$ | $3/4$  | $3$         | $\log_2 3\approx 1.585$ |


$$
H(X\mid Y)=\tfrac34\log_2 3\approx 1.188722.
$$


**Program reading.** Local observers of $Y$ see an apparent reduction; globally, system + environment entropy is accounted by the chain rule. In the gravity narrative, $\Phi_g$ plays the analogous role of overwriting prior micro-details while exporting distinguishability; continuum load $L$ quantifies demand of that process (preview in later parts; definition in Eq.\ (\ref{eq:load}) family below). That narrative does **not** by itself prove Einstein equations or continuum GfE.

**Rigor:** finite classical chain-rule accounting is **constructive**; holographic / gravitational language for the environment register remains **semantic** until an explicit continuum map is built (explicitly not claimed here).

## 1.5 Three-stage mental model

The program is organized so that stages are not collapsed into symbolic identity of actions and master equations (see the staged workflow in Section 1.5):

```text
STAGE 1 --- Computational induction (this program report's discrete core)
  ρ, Φ_g, S_c / H_c, L, $$d\tau=dt/(1+\alpha L)$$
  IDEM / decay / games = discrete microstructure (M11 design + Phase 1--2 ledgers)
        |
        v
STAGE 2 --- Geometric imprint (bridge)
  Structure-induced metric G  (or computational cousin)
  TYPE SAFETY: L is a dimensionless scalar; G is a metric --- L ≠ G
        |
        v
STAGE 3 --- Continuum GfE (macro target)
  Relative entropy of metrics → modified Einstein, Λ_G, G-field
```

**Discipline.** Stage-1 constructive bookkeeping (AND ledgers, composition laws, Landauer contact) **motivates** Stage-2/3 language structurally; it does **not** construct continuum $L$ or $G$. Euclidean dual results (ACD-EW, residual T1′) live on a warm-up lattice and are **not** continuum gravitational equivalence. Continuum GfE contact is treated later as shared weak-field Poisson (**WEAK PASS**) without framework identity (**FAIL**).

## 1.6 Notation and type-safety table

| Symbol | Meaning | Type / hygiene |
|--------|---------|----------------|
| $H_c(f;p_X)$ | Classical computational entropy of map output | Scalar (bits); Tag **A** (foundations); Tag **E** on M11 finite maps |
| $S_c(\Phi;\rho)$ | Quantum/gravity computational entropy | Von Neumann of channel output; Tag **B** |
| $H_c^{\mathrm{toy}}$ | Dual-toy residual + edge score | Tag **C** --- **not** map $H(Y)$ |
| $H_c^{\mathrm{game}}$ | Predictive game Shannon given filtration | Tag **D** --- **not** belief-field dual residual |
| $H_c^{\mathrm{disc}}$ | Finite map / IDEM ledger $H(Y)$ | Tag **E** (M11) |
| $\Phi_g$ | Gravitational CPTP channel | Map on density operators |
| $L$ / $L(\rho,g)$ | Continuum **computational load** (demand) | **Dimensionless scalar**; clocks $d\tau$ |
| $L^{\mathrm{disc}}$ | Discrete three-slot load ledger | Scalar bookkeeping; $L^{\mathrm{disc}}\neq L(\rho,g)$ |
| $G$ | Structure-/matter-induced **metric** (GfE / ACD-EW) | Metric (or edgewise cousin); **$L\neq G$** |
| $G_{\mathrm{Newton}}$ | Newton's constant | Distinct from metric $G$; appear only in Path M calibration language |
| IDEM | Expanded identity + metadata | Result + arity, decay vector, $d_f$, AST metrics |
| $\mathbf{d}$ | Decay / recoverability flags | $\{0,1\}^n$ or soft $[0,1]^n$ |
| $d_f$ | Function unidentifiability | $[0,1]$ |
| GfE | Gravity from Entropy (Bianconi) | Continuum macro target; peer literature, not GR-peer foundation |
| ACD-EW | Action--Channel Duality (Euclidean warm-up) | Constructive dual on warm-up layer only |

**Locked type-safety rules.**

1. **$L$ is a dimensionless scalar.** **$G$ is a metric.** Never write $L\equiv G$.  
2. **$H_c$ / $S_c$ are entropies of declared outputs**, not internal AST size alone (AST size may enter **energy-like** load proxies).  
3. **$L^{\mathrm{disc}}\neq L(\rho,g)$** and discrete bookkeeping weights $\beta',\gamma',\delta'$ are not Newton-calibrated $\alpha\beta=4\pi G/c^4$.  
4. Dual-toy lattice field $\phi$ is a **test signal**, not spacetime geometry and not the M11 microstate of continuum $\rho$.

## 1.7 Entropy object tags (M10, brief)

Earlier drafts historically overloaded the token "$H_c$." M10 freezes five tags so that load rates $|\Delta H_c|$ cannot be mixed across layers (Section 1.7):

| Tag | Symbol | Object |
|-----|--------|--------|
| **A** | $H_c(f;p_X)$ | Classical **map** output Shannon / differential entropy (foundations) |
| **B** | $S_c(\Phi;\rho)$ | Von Neumann entropy of **channel** output $\Phi(\rho)$ |
| **C** | $H_c^{\mathrm{toy}}$ | Dual-toy residual + edge entropy (ACD-EW scorecards); supervised residual quality, not unsupervised $H(Y)$ alone |
| **D** | $H_c^{\mathrm{game}}$ | Predictive game Shannon $H(Y_k\mid\mathcal{F}_{k-1})$ |
| **E** | $H_c^{\mathrm{disc}}$ | Finite map / IDEM / M11 ledger $H(Y)$ |

**Non-identities (do not assert):** $H_c^{\mathrm{toy}}\not\equiv S_c$; $H_c^{\mathrm{disc}}\not\equiv S_c$; $H_c^{\mathrm{game}}\not\equiv H_c^{\mathrm{toy}}$; $H_c\not\equiv S_{\mathrm{GfE}}$. House style: bare $H_c$ only for Tag **A** when unambiguous; theory claims mixing layers must tag.

**Semantic preview of demand (C14).** Prefer reading continuum load $L$ as demand from the **scale and rate of channel outcomes** --- energy-like work, entropy flux / export, and boundary or distinguishability budget --- so that active scrambling and high export raise $L$. That reading is a **semantic** program convention until continuum matching exists; it is the same polarity that discrete ledgers enforce by construction in §2.

---

# 5. Classical microstructure --- IDEM, decay, and discrete load (M11 + D12--D13)

## 2.1 The central gap

This research program has long carried two substantial threads that barely touched:

| Thread | Machinery | Gap |
|--------|-----------|-----|
| **Classical / lambda** | IDEM (arity, AST metrics, decay vector, $d_f$), games as maps, combinatorial density | Did not feed gravity recoveries |
| **Emergent gravity** | $\Phi_g$, $S_c$, load $L$, master equation, Path J/M Newton | Used only high-level "output entropy" language |

**M11** addresses that gap by a **discrete accounting dictionary**


$$
\text{IDEM / game / lambda step}\;\longrightarrow\; H_c^{\mathrm{disc}}\ \text{and candidate terms in }L^{\mathrm{disc}},
$$


implemented as pure bookkeeping on finite classical models --- **without** inventing continuum metric $G$, rewriting the master equation, or claiming Einstein-from-gates (Appendix A). Continuum role motivation of the three load slots is a separate design essay (Appendix A): **structural**, not a continuum limit theorem.

## 2.2 IDEM and the decay vector (brief)

An **IDEM** (expanded identity) pairs a map result with metadata: arity, result dimension, decay vector $\mathbf{d}$, function unidentifiability $d_f$, and optional AST complexity metrics. In recoverability models:

- $d_i=0$: input $x_i$ is recoverable from the declared output under the model;  
- $d_i=1$: that input information is **lost** to an observer of $Y$ alone;  
- Soft variants use $d_i\in[0,1]$ (e.g. $1-1/|\mathrm{preimage}|$).

For fair-bit AND, output $Y=1$ has a unique preimage $(1,1)$, while $Y=0$ has three preimages; recoverability fails on the latter branch, matching the large conditional entropy $H(X\mid Y)$. Decay flips $0\to 1$ are the classical image of **irreversible overwrite**; M11 feeds the **rate** of export or soft decay into the entropy-rate load slot, not an idle "identity stockpile."

**Rigor:** IDEM ontology and decay semantics are **semantic/structural** classical design. Concrete finite Shannon numbers below are **constructive**. Mapping decay to holographic screen degrees of freedom remains **analogical**, not a theorem.

## 2.3 Operational $H_c^{\mathrm{disc}}$ and three-slot discrete load

**Operational rule.** Computational entropy on a discrete model is the Shannon entropy of the **declared public output**, not residual dual-toy scores, not internal AST size alone, and not blackjack bankroll EV.

Continuum load has three **roles** (energy-like density, entropy-rate / export, boundary/capacity). M11 defines matching **proxies** with bookkeeping weights $\beta',\gamma',\delta'$ (default $1$), **not** continuum calibrations:


$$
L^{\mathrm{disc}}
=
\beta' L_E^{\mathrm{disc}}
+
\gamma' L_S^{\mathrm{disc}}
+
\delta' L_B^{\mathrm{disc}}.
$$


| Continuum role (master eq) | Discrete proxy | Locked reading |
|----------------------------|----------------|----------------|
| Energy-like work | $L_E$: ops / redexes / active evaluations this step | Idle identity $\Rightarrow$ low $L_E$; active work $\Rightarrow$ high |
| Entropy-rate / export flux | $L_S$: $H(X\mid Y)$ single-shot, or $|\Delta H_c^{\mathrm{disc}}|$ multi-step, or soft decay-flip rate | High flux / overwrite $\Rightarrow$ **high** $L_S$ even when $H(Y)$ falls |
| Boundary / capacity | $L_B$: mean soft lost-recoverability mass; residual ensemble entropy ratio; open redex fraction | Open distinguishability budget $\Rightarrow$ high $L_B$ |

**Locked $L$ reading (C14).** Prefer demand from **scale and rate of possible channel outcomes**. Reject as primary story: "how much unreduced identity stockpile remains." High entropy flux, many open results, and active scrambling raise load; fully reduced idle maps have low load.

**Type safety.** The three discrete slots share **roles** with continuum $L(\rho,g)$. They do **not** equal continuum coefficients, Newton's $G$, or the structure metric $G$. Same three axes of demand; different mathematical objects.

## 2.4 Phase 1 --- AND-gate pure ledger (constructive)

Artifact: Appendix A.1.

| Quantity | Value (fair bits) | Role |
|----------|-------------------|------|
| $H(X)$ | $2$ bits | Input possibility mass |
| $H_c^{\mathrm{disc}}=H(Y)$ | $h_2(1/4)\approx 0.811278$ | Declared output entropy (Tag **E**) |
| Export $H(X\mid Y)$ | $\approx 1.188722$ | Preimage / environment ledger |
| $L_E^{\mathrm{disc}}$ | $1$ (one gate op) | Active work |
| $L_S^{\mathrm{disc}}$ | $:=H(X\mid Y)\approx 1.188722$ | Single-shot export flux |
| $L_B^{\mathrm{disc}}$ | $0.5$ (mean soft lost-recoverability mass) | Open distinguishability after map |
| $L^{\mathrm{disc}}$ (weights $1$) | $\approx 2.689$ | Sum of independent role proxies |

**Observation.** Output $H_c^{\mathrm{disc}}$ **drops** ($\approx 2\to 0.811$) while demand **rises**. Any monist load proportional to residual output entropy alone would report *low* demand precisely when irreversible overwrite is *expensive* --- opposite of the locked reading. Three independent axes appear simultaneously: work ($L_E$), export flux ($L_S$), and residual recoverability mass ($L_B$).

Chain rule residual on the ledger is $<10^{-12}$. **Rigor:** $H_c^{\mathrm{disc}}$ and export **constructive**; three-slot assignment **structural bookkeeping**, not continuum $L$ ($L^{\mathrm{disc}}\neq L(\rho,g)$).

## 2.5 Phase 2 --- multi-step Boolean, tiny SKI, minimal shoe (brief)

Phase-2 multi-step, SKI, and shoe ledgers are summarized in Appendix A.

**Multi-step Boolean.** An identity baseline on $(X_1,X_2,X_3)$ has $L_E=L_S=L_B=0$ (idle). An AND step spikes export ($L_S\approx 1.189$); a subsequent OR-type step has **lower** export than AND. Ordering is asserted under the locked reading: larger export $\Rightarrow$ larger $L_S$. An optional discrete load-clock diagnostic $k_{\mathrm{eff}}=\sum 1/(1+\alpha' L^{\mathrm{disc}})$ with conventional $\alpha'=0.1$ is printed only as bookkeeping --- **not** continuum proper time.

**Tiny SKI ensemble.** Fixed finite combinator terms under normal-order redex steps: $L_E=$ mean redex count pre-step; $L_S=|\Delta H_c^{\mathrm{disc}}|$ under reduction; $H_c^{\mathrm{disc}}$ drops as term-shape classes concentrate under reduction. Exact Shannon on a finite ensemble; no continuum constants.

**Minimal R/B shoe.** Fixed-sequence multiset (e.g. 6 red + 6 black residual shoe): predictive $H_c^{\mathrm{game}}$-adjacent combinatorial entropy of next color; $L_E=1$ per count-bucket update; $L_S=|\Delta H_c^{\mathrm{game}}|$ spikes when predictive entropy jumps; $L_B=H_{\mathrm{seq}}(\Omega_k)/H_{\mathrm{seq}}(\Omega_0)$ residual order-entropy ratio as capacity-like pressure. Honesty: **not** bankroll EV, **not** ACD-EW residual dual $H_c^{\mathrm{toy}}$, and not multi-deck strategy science (M12 deferred).

**Rigor:** Phase 2 ledgers are **constructive** finite accounting with **structural** continuum role alignment only.

## 2.6 Coupled regions (one paragraph)

A two-region product ledger (Appendix A) places independent fair-bit pairs on regions $A$ and $B$, runs local ANDs, then a coupling XOR "screen" that redistributes shared information. The experiment shows: global chain-rule conservation on the product alphabet; local high export $\Rightarrow$ high local $L_S$ while an idle baseline region stays low; coupling redistributes / screens information without magical destruction; optional per-region diagnostic $k_{\mathrm{eff}}$. Product regions are **not** spacetime patches, **not** continuum $\rho$, and **not** a derivation of local energy density fields. They make multi-site classical conservation **constructive** before any hydrodynamic aspiration (Section 2.9 / Appendix A §5--6).

## 2.7 Composition path dependence (D13 / Appendix A.2)

**Evidence:** Appendix A.2. Entropy object: Tag **E**. Stage-1 classical only.

**Two composition models (must not be conflated).**

| Model | Definition |
|-------|------------|
| **Pure cascade** | $Y=f(X)$, $Z=g(Y)$ --- next stage sees only $Y$ |
| **Circuit** | Later stages may still read residual input wires + intermediates |

Standard lemmas (finite classical):

- **Lemma A (chain rule):** $H(X)=H(Y)+H(X\mid Y)$ for deterministic $Y=f(X)$.  
- **Lemma B (export additivity on pure cascade):** $H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)$.  
- **Lemma C (DPI):** $H(g(Y))\le H(Y)$.  
- **Lemma D:** path $L_E$ is additive by counting ops.  
- **Lemma E (path dependence of cumulative $L_S$):** $\sum L_S$ is **not** a function of the final map alone.

**Explicit Direct vs Circuit witness (fair bits $X=(X_1,X_2)$).**

| Path | Stages | Final $Z$ | $H(Z)$ | $\sum L_S$ (stage exports) |
|------|--------|-------------|----------|------------------------------|
| **Direct $D$** | $Z=X_1\land X_2$ | AND law | $\approx 0.811278$ | $H(X\mid Z)\approx 1.188722$ |
| **Circuit $C$** | $Y=X_1$, then $Z=Y\land X_2$ (wire $X_2$ retained) | same AND law | $\approx 0.811278$ | $H(X\mid Y)+H(X\mid Z)=1+1.188722=2.188722$ |

Thus, in rounded form used for program citation:


$$
\sum L_S(D)\approx 1.189,\qquad
\sum L_S(C)\approx 2.189,\qquad
H(Z)\ \text{identical on both paths}.
$$


**Crucial distinction.**

```text
H(X|Z)           --- property of the final I/O pair (path-independent for fixed final map)
Σ_s L_S^(s)      --- property of the pipeline (path-dependent under circuit stages)
```

Paying for an intermediate publish/export that is later re-used in an irreversible gate **raises demand along the path**, even when the final output law is unchanged. Load is not "final $H_c^{\mathrm{disc}}$ alone." Soft-recoverability $L_B$ is likewise **not** freely additive under regional sums or stage sums without a fixed global coordinate convention (Lemma F counterexamples).

**Rigor:** Lemmas A--C and the Direct/Circuit numbers are **constructive**; continuum composition of $L(\rho,g)$ is **not claimed**.

## 2.8 Landauer contact for export and $L_S$ (D13 / Appendix A.3)

**Evidence:** Appendix A.3.

On the same finite AND model, fix an explicit **Protocol R** (reset after AND): compute $Y=f(X)$, keep only $Y$ as public system output, and thermalize residual input registers conditional on $Y$. The average number of erased bits is the export


$$
n_{\mathrm{erased}} := H(X\mid Y).
$$


**Landauer's principle** (external theorem; not re-proved here) then supplies the standard lower bound on average heat dissipated to a bath at temperature $T$:


$$
Q \;\ge\; k_B T \ln 2 \cdot H(X\mid Y)
\qquad\text{(Shannon in bits)}.
$$


In units of $k_B T\ln 2$, the bound **equals** the export ledger quantity. M11's single-shot entropy-rate slot is defined as that same object:


$$
L_S^{\mathrm{disc}} := H(X\mid Y)
\quad\Rightarrow\quad
Q \;\ge\; k_B T \ln 2 \cdot L_S^{\mathrm{disc}}
\quad\text{(single-shot AND / Protocol R)}.
$$


| Quantity | Fair-bit AND |
|----------|----------------|
| $H(Y)=H_c^{\mathrm{disc}}$ | $\approx 0.811278$ |
| Export $H(X\mid Y)$ | $\approx 1.188722$ |
| Landauer $Q_{\min}/(k_B T\ln 2)$ | $=H(X\mid Y)\approx 1.188722$ |
| $L_S^{\mathrm{disc}}$ | $=$ export by definition |

**Optional reversible dilation (Bennett-style, structural).** A reversible embedding can park preimage information in **garbage** $G$; public $H(Y)$ may match the irreversible case, but eventual erasure of $G$ still costs $\ge H(X\mid Y)$. Export does not vanish under reversible accounting; it is deferred until garbage reset.

**What this contact is and is not.**

| Allowed | Forbidden from Appendix A.3 alone |
|---------|---------------------------|
| Export $H(X\mid Y)$ is the average erased-bit count under Protocol R | Newton $G$ or Path J/M calibration from Landauer |
| $L_S^{\mathrm{disc}}$ is that information object | $\hbar$, holography, or $S_{\mathrm{BH}}=A/4G\hbar$ from AND heat |
| Thermodynamic bookkeeping contact only | Continuum $L_S$ density = GR/GfE heat flux |
| | $L\equiv G$ or $L^{\mathrm{disc}}\equiv L(\rho,g)$ |

**Rigor:** finite Shannon identities **constructive**; Landauer inequality **external theorem**; identification of $L_S$ with the Landauer bit-count **structural contact**. Conversion factor $k_B T\ln 2$ is standard thermodynamics, **not** fitted to gravity scales.

### Numbered Stage-1 theorems (finite classical)

The following are **finite classical** statements on declared I/O cuts (entropy Tag **E**). They are **constructive** on finite alphabets and ledgers unless labeled otherwise. They do **not** transfer to continuum $L(\rho,g)$, $\Phi_g$, Path J/M, dual residual $H_c^{\mathrm{toy}}$, or GfE without a new map. Sources: Appendix A.2, Appendix A.3; witnesses Appendix A.2, Appendix A.3, Appendix A.1.

**Theorem T1 (chain rule / export for deterministic maps).**  
Let $X$ be a finite-alphabet random variable and $Y=f(X)$ a deterministic map. Then

$$
H(X)=H(Y)+H(X\mid Y).
$$

**Reading:** $H(X\mid Y)$ is **export** (preimage / environment register), not destruction of information. Single-shot $L_S^{\mathrm{disc}}:=H(X\mid Y)$ is a structural export-flux proxy (M11).  
**Rigor:** **constructive** (Shannon chain rule; Phase 1 AND residual $<10^{-12}$).  
**Cite:** Appendix A.2 Lemma A · §1.4 · §2.4.

**Theorem T2 (Markov cascade export additivity).**  
Let $Y=f(X)$ and $Z=g(Y)$ be deterministic with pure cascade (second stage sees only $Y$). Then

$$
H(X\mid Z)=H(X\mid Y)+H(Y\mid Z).
$$

**Warning:** Circuit stages that re-read residual input wires need not obey this identity in the cascade form.  
**Rigor:** **constructive** (proof + ledger witness; e.g. AND then NOT).  
**Cite:** Appendix A.2 Lemma B · §2.7.

**Theorem T3 (path dependence of cumulative $\sum L_S$).**  
There exist finite models and two pipelines realizing the **same** final map $X\mapsto Z$ (same law, same $H(Z)$) such that cumulative stage export costs differ. Explicit fair-bit witness:

$$
\sum L_S(\mathrm{Direct})\approx 1.188722,\qquad
\sum L_S(\mathrm{Circuit})\approx 2.188722,\qquad
H(Z)\approx 0.811278\ \text{on both paths}
$$

(rounded **1.189** vs **2.189**). Thus $\sum L_S$ is **not** a function of the final map alone; final residual $H(X\mid Z)$ remains path-independent for fixed $(X,Z)$.  
**Rigor:** **constructive** (closed form + composition ledger).  
**See:** Theorem T3; Appendix A.2; Results P4.

**Theorem T4 (Landauer identification of $L_S$ under Protocol R).**  
On Protocol R for a finite deterministic map (compute $Y=f(X)$, keep public $Y$, thermalize residual input registers conditional on $Y$), the average erased-bit count is $H(X\mid Y)$. Landauer's principle (external) supplies

$$
Q\ge k_B T\ln 2\cdot H(X\mid Y).
$$

M11 single-shot $L_S^{\mathrm{disc}}:=H(X\mid Y)$ is that same information object, so $Q\ge k_B T\ln 2\cdot L_S^{\mathrm{disc}}$. On fair-bit AND, export $=$ Landauer bit-count $\approx 1.188722$.  
**Rigor:** finite Shannon **constructive**; Landauer inequality **external theorem**; $L_S$ identification **structural contact**. Not Newton, not continuum $L$, not $L\equiv G$.  
**See:** Theorem T4; Appendix A.3; Results P3.

**Proposition T5 ($L_B$ non-additivity witness).**  
Mean soft-recoverability $L_B$ is **not** freely additive under (i) regional sum vs joint mean on product systems, or (ii) sum of stage $L_B$ vs $L_B$ of a direct map. Explicit product witness: two independent AND regions with $L_B(A)=L_B(B)=0.5$ give sum $1.0$ but joint mean $L_B(G)=0.5$.  
**Rigor:** **constructive counterexamples** (not a uniqueness theorem for every possible $L_B$ formula).  
**See:** Proposition T5; Appendix A.2.

| ID | Statement | Rigor |
|----|-----------|-------|
| **T1** | $H(X)=H(Y)+H(X\mid Y)$ (deterministic) | constructive |
| **T2** | Pure-cascade export additivity $H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)$ | constructive |
| **T3** | $\sum L_S$ path-dependent (Direct $\approx 1.189$ vs Circuit $\approx 2.189$) | constructive |
| **T4** | $L_S=H(X\mid Y)$ Landauer bit-count under Protocol R | constructive + external |
| **T5** | Mean soft $L_B$ non-additive (product / stage witnesses) | constructive counterexamples |

**Non-claims for T1--T5.** Continuum composition of $L(\rho,g)$; Einstein from Boolean cascades; $\sum L_S$ as gravitational redshift; dual-toy residual $=$ gate export.

## 2.9 Why three load terms? (structural motivation)

Discrete evidence simultaneously requires three independent **axes of demand** (Section 2.9 / Appendix A):

1. **How hard is the machine working?** ($L_E$)  
2. **How fast is possibility being realized / exported?** ($L_S$)  
3. **How much distinguishability budget remains open versus capacity?** ($L_B$)

A monist load $L\propto H_c^{\mathrm{disc}}$ alone fails on irreversible AND (output entropy low, export high). A monist "remaining AST size" fails the locked reading when the stockpile is idle. Shoe dynamics separate nearly constant update cost ($L_E$), flux spikes ($L_S$), and smoothly shrinking residual multiset capacity ($L_B$). Continuum three-term $L$ is the **same role split** at continuum language level --- **structural motivation**, not uniqueness, and not a hydrodynamic limit of IDEM.

## 2.10 Section non-claims

Do **not** assert from M11 Phase 1--2, composition, Landauer contact, or coupled-region ledgers:

1. Master equation $\Leftrightarrow$ continuum GfE.  
2. $L\equiv G$, $L^{\mathrm{disc}}\equiv L(\rho,g)$, or $S_c\equiv\operatorname{Tr} g\ln G^{-1}$.  
3. IDEM/decay **constructs** continuum $L$ or metric $G$ (PROGRESS non-claim §2.3.9).  
4. Newton / Einstein recovery from gates, SKI terms, shoes, or Landauer heat.  
5. Lattice dual toys or blackjack-belief dual **are** gravity or **are** true game predictive $H_c^{\mathrm{game}}$.  
6. Path J/M calibration constants $\alpha,\beta,\gamma,\delta,\epsilon_0$ are fixed by discrete proxies.  
7. Decay vector components **are** Hawking radiation degrees of freedom.  
8. Primary load = idle remaining identity stockpile.  
9. Continuum composition laws of $L(\rho,g)$ or $\lvert dS_c/d\tau\rvert$ from finite Boolean cascades.  
10. Dual-toy residual $H_c^{\mathrm{toy}}$ equals gate export or Landauer bits.

**Allowed claim form (program-level).** On finite classical models $\mathcal{M}$, we define constructive $H_c^{\mathrm{disc}}$ and a three-term discrete load ledger whose terms play the same *roles* as master-equation load slots under the locked high-flux reading; cumulative stage export $\sum L_S$ is path-dependent under circuits even when final $H(Z)$ is fixed; and single-shot $L_S=H(X\mid Y)$ is the information object bounded by Landauer heat under Protocol R. Continuum gravity remains deferred.

---

## Source map for Parts 0--2

| Topic | Canonical / primary path |
|-------|--------------------------|
| $H_c$ / $S_c$ definitions | Section 1 |
| Claims freeze C1--C14, non-claims | Section 3 and Appendix B |
| M11 design + Phase 1--2 | Appendix A · Appendix A |
| Continuum role motivation | Appendix A |
| Composition / path $\sum L_S$ | Appendix A.2 |
| Landauer / $L_S$ | Appendix A.3 |
| Entropy tags A--E | Appendix A · Appendix A |
| Outline / product form | Appendix A |

---

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

# 7. Newton recovery --- Path J/M only

### 4.1 Honesty preamble

Newtonian gravity is recovered as a **calibrated low-load regime** of the master-equation framework (**C9**), **not** by taking the Laplacian of a pointwise identification $\Phi\propto\rho_m$.

| Claim piece | Status / rigor |
|-------------|----------------|
| Master equation + load definitions | Canonical (Part 3) |
| Clausius on $\mathcal{L}_g$ $\Rightarrow$ Einstein (Jacobson 1995) | **External theorem + modeling assumption** |
| Einstein weak field $\Rightarrow$ $\nabla^2\Phi=4\pi G\rho_m$ | Standard GR |
| Matching $\alpha\beta=4\pi G/c^4$ so load clock agrees with Newtonian $\Phi$ **on shell** | **Calibration** (Path M; **C10**) |
| Pointwise $\Phi\propto\rho_m\Rightarrow\nabla^2\Phi\propto\nabla^2\rho_m\Rightarrow$ Poisson | **Invalid / withdrawn** |

**What is not claimed.** We do not derive Newton independently of Jacobson/Einstein input. We do not claim free derivation of Newton's constant $G$ from load bookkeeping alone. We do not claim that $\gamma=\delta=0$ is proved---only that those contributions are modeled as subdominant in the leading weak-field regime.

Canonical recovery is Path J/M as stated in this section; the historical pointwise Laplacian route is withdrawn (Section 4.5).

### 4.2 Setup: low-load, weak-field, slow-motion assumptions

Under the master equation and load of Part 3, the Newtonian analysis uses:

| # | Assumption |
|---|------------|
| L1 | $\alpha L\ll 1$ |
| L2 | Curvature small; $v\ll c$ |
| L3 | Entropy-production and holographic terms **subdominant**: $\gamma,\delta$ contributions $\ll$ energy-density term (modeling assumption; not quantified) |
| L4 | $\mathcal{L}_g$ obeys $\delta Q=T\,dS_c$ on every local Rindler horizon (Jacobson consistency) |

Under L1--L3,


$$
L
\approx
\beta\frac{E[\rho]}{V\epsilon_0}
\approx
\beta\frac{\rho_m c^2}{\epsilon_0},
$$


where $\rho_m$ is classical mass density ($T_{00}\approx\rho_m c^2$).

### 4.3 Path J --- Clausius → Einstein → Poisson

Path J is the **derivation path for the Poisson equation**.

**Step J1 --- Thermodynamic consistency of the generator.**  
By L4, heat flux and computational-entropy change on local horizons satisfy $\delta Q=T\,dS_c$.

**Step J2 --- Jacobson's theorem (imported).**  
Jacobson (1995): the Clausius relation on local Rindler horizons, with entropy proportional to horizon area and Unruh temperature, implies the **Einstein field equations** as an equation of state of the underlying thermodynamics (up to a cosmological constant fixed by the vacuum). In this framework we **import** that theorem as the continuum content of L4. We do **not** re-prove Jacobson here. Rigor: **external theorem + modeling assumption**.

**Step J3 --- Weak-field GR → Poisson.**  
Linearize Einstein about Minkowski with a static, non-relativistic perfect fluid. Standard textbook result:


$$
\nabla^2\Phi = 4\pi G\,\rho_m,
\qquad
g_{00} \approx -\bigl(1+2\Phi/c^2\bigr),
\quad
\sqrt{-g_{00}}\approx 1+\Phi/c^2.
$$


**Conclusion of Path J.** Newtonian Poisson is available as the weak-field limit of the Einstein thermodynamics already built into $\mathcal{L}_g$ under L4. No Laplacian of $\rho_m$ is required. The nonlocal structure of $\Phi$ (inverse-square forces from compact sources) is inherited from GR, not invented by load algebra.

### 4.4 Path M --- Load-clock calibration (matching, not derivation)

Path J yields a metric with Newtonian potential $\Phi[\rho_m]$. Path M fixes how the **load reparameterization** tracks the same $\Phi$. Rigor: **calibration**, conditional on Path J (**C10**).

**Step M1 --- Proper-time expansion.** For $\alpha L\ll 1$,


$$
d\tau
=
\frac{dt}{1+\alpha L}
\approx
dt\bigl(1-\alpha L\bigr)
\approx
dt\Bigl(1-\alpha\beta\frac{\rho_m c^2}{\epsilon_0}\Bigr).
$$


**Step M2 --- Static weak-field clock.** For a static observer,


$$
\frac{d\tau}{dt}
=
\sqrt{-g_{00}}
\approx
1+\frac{\Phi}{c^2}.
$$


**Step M3 --- On-shell matching (not pointwise $\Phi\propto\rho_m$).**  
Do **not** identify $\Phi/c^2=-\alpha\beta\rho_m c^2/\epsilon_0$ as a **local algebraic law**. That identification would give $\Phi\propto\rho_m$ pointwise, which is not Newtonian gravity.

Instead: for solutions of Poisson with the same $\rho_m$, require the **leading linear response** of the load clock to agree with the Newtonian redshift **on shell**.

*Worked example (uniform ball).* For constant density $\rho_m$ in a ball of radius $R$, the interior potential is


$$
\Phi_{\mathrm{in}}(r)
=
-2\pi G\rho_m\Bigl(R^2-\frac{r^2}{3}\Bigr)
\quad(r\le R).
$$


At the center, $\Phi_{\mathrm{in}}(0)/c^2=-2\pi G\rho_m R^2/c^2$. The load expansion at the center gives $d\tau/dt-1\approx-\alpha\beta\rho_m c^2/\epsilon_0$. Matching order of magnitude for a characteristic scale $R\sim R_\star$ (or equating coefficients after fixing a reference geometry where $\Phi$ is proportional to $\rho_m R^2$) calibrates $\alpha\beta$ relative to $\epsilon_0$. The **standard product used in this program**


$$
\alpha\beta = \frac{4\pi G}{c^4}
$$


is the convention that absorbs $\epsilon_0$ and geometric scale into the definitions of $\beta$ and $\epsilon_0$ so that $\alpha\cdot\beta\cdot c^2/\epsilon_0$ reproduces $\lvert\Phi\rvert/c^2$ **for the calibrated family of solutions**, not for arbitrary pointwise $\rho_m$.

**Honest reading of $\alpha\beta=4\pi G/c^4$:** it is a **matching condition** between load bookkeeping and Newtonian $\Phi$, **conditional on Path J already supplying Poisson**. It is **not** a free derivation of $G$ from first principles independent of Newton/GR (**C10**).

**Step M4 --- What the load clock then means.** With Path J + M: geometry / $\Phi$ is fixed by Einstein thermodynamics (Jacobson) + weak field; $L\approx\beta\rho_m c^2/\epsilon_0$ raises demand where energy density is high; $$d\tau=dt/(1+\alpha L)$$ **tracks** the same slowing of clocks that GR encodes in $g_{00}$, once $\alpha\beta$ is calibrated; Newtonian force $\mathbf{F}=-m\nabla\Phi$ remains the effective description for slow massive probes---no extra force postulate beyond Path J's Einstein/Poisson content.

### 4.5 Withdrawn path (do not revive)

The following chain is **not** a valid recovery of Newtonian gravity (historical drafts; documented in M8; **withdrawn**):

1. Postulate $d\tau/dt=1/(1+\alpha L)$ with $L=\beta\rho_m c^2/\epsilon_0$.  
2. Set $d\tau/dt=1+\Phi/c^2$.  
3. Conclude $\Phi=-\alpha\beta c^4\rho_m/\epsilon_0$ **pointwise**.  
4. Take $\nabla^2$ and "match" to $4\pi G\rho_m$.

**Why it fails.** Newtonian $\Phi$ is **nonlocal** ($\Phi=-G\int\rho_m/|x-x'|\,dV'$). Pointwise $\Phi\propto\rho_m$ does not produce inverse-square forces from compact sources. Algebraically,


$$
\nabla^2\Phi
=
-\,\alpha\beta\frac{c^4}{\epsilon_0}\,\nabla^2\rho_m
$$


is **not** Poisson unless $\nabla^2\rho_m\propto-\rho_m$.

> **Disallowed one-liner:** "Taking the Laplacian of $\Phi\propto\rho$ yields $\nabla^2\Phi=4\pi G\rho$."

> **Allowed one-liner:** In the low-load regime the energy-density term dominates $L$. With $\mathcal{L}_g$ constrained by the Clausius relation, the Einstein equation (Jacobson) and its weak-field Poisson limit are available; matching the load-induced proper-time factor to the Newtonian potential fixes $\alpha\beta=4\pi G/c^4$. Newtonian gravity is thus a **calibrated low-load regime** of the framework.

### 4.6 Recovery chain (allowed language)

```text
Clausius on L_g  --(Jacobson)--->  Einstein equation
                                      |
                                      v
                              weak field / slow motion
                                      |
                                      v
                              ∇²Φ = 4πG ρ_m     (Path J)
                                      |
                                      v
                    match load clock dτ/dt ≈ 1+Φ/c²
                    on shell  ⇒  αβ = 4πG/c⁴     (Path M)
```

**Role of coefficients at leading Newton.** $\epsilon_0$ is reference energy density making $L$ dimensionless (absorbed into $\beta$ bookkeeping under Path M). The product $\alpha\beta$ (with $\epsilon_0$) is fixed by Path M. Weights $\gamma$ and $\delta$ are **dropped** at leading Newton under L3; they re-enter next-order / nonequilibrium / near-horizon regimes and must not be silently equated with GfE extras $D_{\mu\nu},\Lambda_G$ (that identification is a **structural FAIL** at next order---Part 6 / M6b; not claimed here).

### 4.7 Other recoveries --- status only (deferred)

Black-hole horizons, cosmological expansion (including inflation narratives), Lloyd-type ultimate computational capacity, and unified accounts of gravitational and kinematic time dilation appear in historical and outline form under Appendix A and legacy Appendix A drafts. Those regimes are **not** presented here as settled at Path J/M rigor. High-load / horizon physics elevates the boundary term $\delta$; cosmology elevates boundary growth and expansion bookkeeping; capacity bounds touch Lloyd-type limits. Each requires the same honesty pass as Newton: explicit assumptions, external theorems labeled as such, calibration distinguished from free derivation, and no revival of withdrawn algebraic shortcuts. Until that pass is complete, the program's **settled** gravitational recovery claim remains **Path J/M Newtonian Poisson only** (**C9**, **C10**). Cross-framework weak-field contact with continuum GfE (shared Poisson via GR, **not** framework identity) is deferred to Part 6 (M6 WEAK PASS / FAIL).

---

## Claim inventory for Parts 3--4

| ID | Statement used | Where | Rigor |
|----|----------------|-------|-------|
| **C9** | Newton recovery = Path J/M only (Clausius → Einstein → Poisson; load-clock on-shell match) | §4 | Path J: external thm + assumption; Path M: calibration |
| **C10** | $\alpha\beta=4\pi G/c^4$ is on-shell calibration, not free derivation of $G$ | §3.3 preview; §4.4 | **calibration** |
| **C14** | Prefer $L$ as demand from scale/rate of channel outcomes (energy + entropy flux + boundary); active scrambling → higher $L$ | §3.2 | **semantic** (program convention) |

**Structural (not claim-ID frozen as C-number):** three-term continuum $L$ **roles** align with discrete $L_E,L_S,L_B$ (M11c)---**not** continuum equality.

**Explicit non-claims touched:** ME $\Leftrightarrow$ GfE; $L\equiv G$; free derivation of $G$; Newton from pointwise $\Phi\propto\rho$ Laplacian (**withdrawn**); IDEM/decay fully constructs continuum $L$ or $G$; other recoveries settled at Path J/M rigor.

---

## Sources (Parts 3--4)

| Role | Path |
|------|------|
| Outline Parts 3--4 | Appendix A |
| Canonical $\Phi_g$, $L$, master eq | Eq.\ (\ref{eq:load}) family below |
| Canonical Path J/M | Appendix A |
| M8 audit (withdrawn path) | Appendix A |
| Claims freeze C9--C10, C14 | Section 3 and Appendix B |
| Three-role structural motivation | Appendix A |
| Claim gate | Section 3 and Appendix B |

---

*External theorem (Path J): Jacobson (1995); see Bibliography.*

---

# 8. Euclidean dual ACD-EW --- T1′ / $U_\star$, claims A--D, toys as witnesses

### 5.1 Scope: Layers W and D only

This part concerns a **constructive Euclidean dual**, not continuum gravitational equivalence. Two layers must be kept distinct.

**Layer W (warm-up).** On a flat Euclidean support, Bianconi's Gravity-from-Entropy (GfE) program admits a scalar warm-up in which a structure-induced metric


$$
G[\phi] \;=\; 1 + \alpha_G\,(\nabla\phi)^2
$$


enters a relative-entropy / logarithmic action density $\mathcal{L}=-\ln G$ (edgewise on a lattice). In continuum language (external literature; not re-derived here), the $L^2$-gradient flow of the associated energy is classical Perona--Malik (PM) anisotropic diffusion; isotropic heat is the special case of unit conductivity. Discrete toys implement explicit-Euler PM (and a Catte-style lift in 2D) on a lattice field $\phi$. Layer W is about **action/energy and PM flow**, not about residual dual scorecards and not about Lorentzian GfE field equations.

**Layer D (dual).** Action--Channel Duality, Euclidean Warm-Up (**ACD-EW**) pairs that warm-up geometry with an **observation channel**: a hidden field $\phi_\star$ is observed as $y=\phi_\star+\eta$, reconstructed by heat, PM, or load-gated PM, scored by a residual/edge entropy proxy $H_c^{\mathrm{toy}}$, and summarized by a split scalar load that can reparameterize the reconstruction clock. Layer D is about **channel residual, load clock, and residual dual windows**. It does **not** automatically transfer to continuum GfE (**G**) or to the gravitational master equation (**M**).

**Type safety.** Load $L$ (and toy $L_{\mathrm{clock}}$) is a **dimensionless scalar** demand. Structure-induced $G$ is a **metric** (or edgewise cousin). **$L\neq G$**. Results proved or scorecarded only on W or D must not be cited as G or M theorems. In particular: lattice denoising is **not** empirical gravity; residual dual is **not** master-equation $\Leftrightarrow$ continuum GfE.

---

### 5.2 ACD-EW construction

**Support and state (1D primary toy).** Sites $i=0,\ldots,N-1$ (default $N=192$, spacing $h=1$); support metric $g_i\equiv 1$; scalar field $\phi\in\mathbb{R}^N$; edge gradients $(\nabla\phi)_i=\phi_{i+1}-\phi_i$.

**Stage 2 --- shared geometric object.** The induced edgewise metric $G_i[\phi]=1+\alpha_G(\nabla\phi)_i^2$ is simultaneously (i) the GfE warm-up second metric (Bianconi Stage 2--3 input) and (ii) the geometric imprint of local reconstructed structure in our workflow. Duality **hinges** on this shared Stage-2 object: both readings act on the same $G[\hat\phi]$.

**Stage 3 --- warm-up action and PM flow.** Edgewise warm-up density $\mathcal{L}_i^{\mathrm{GfE}}=-\ln G_i[\phi]$; total action $S_{\mathrm{GfE}}[\phi]=\sum_i\mathcal{L}_i^{\mathrm{GfE}}$. Dynamics on the GfE side are gradient flow implemented as Perona--Malik conductivity


$$
\rho_i \;=\; \frac{1}{1+\bigl((\nabla\phi)_i/K\bigr)^2},\qquad
\partial_t\phi \;=\; \operatorname{div}(\rho\,\nabla\phi),
$$


with $K$ of order the observation noise scale. External literature (Bianconi, *Beyond holography*) identifies continuum PM with the Euclidean GfE warm-up gradient flow; this program treats that identification as **literature structure for Layer W**, not as a re-proof of the continuum variational identity.

**Stage 1 --- observation channel.** Hidden structure $\phi_\star$; observation $y=\phi_\star+\eta$ with i.i.d. Gaussian noise $\eta\sim\mathcal{N}(0,\sigma^2 I)$ (default $\sigma=0.12$); reconstructor $\mathcal{C}_t:y\mapsto\hat\phi(t)$ given by heat, PM, or load-gated PM with $\hat\phi(0)=y$. Residual energy $R=\mathrm{mean}_i(\hat\phi_i-\phi_{\star,i})^2$; residual entropy proxy $H_R=\log(1+R/\sigma_{\mathrm{ref}}^2)$; edge-location entropy $H_{\mathrm{edge}}=-\sum_i p_i\log_2 p_i$ with $p\propto|\nabla\hat\phi|$. The dual **channel score** is


$$
H_c^{\mathrm{toy}}(\hat\phi\mid\phi_\star) \;=\; H_R + \lambda_e H_{\mathrm{edge}}
$$


(tag **C** in the M10 object dictionary). Lower $H_c^{\mathrm{toy}}$ means better reconstruction / more localized edge mass. This is a **supervised residual score**, not Shannon entropy of a generic map output and not von Neumann $S_c$.

**Stage 1 --- split load.** $L_E=c_E\mathbb{E}[(\nabla\hat\phi)^2]$ tracks induction intensity (and $\mathbb{E}[G-1]$); $L_S=c_S|\Delta H_c^{\mathrm{toy}}|/\Delta t$ tracks rate of channel-score change; $L_B$ is a capacity-like edge saturation not used in the v2 clock; $L_{\mathrm{clock}}=L_E+L_S$. Load-gated dynamics use the same PM vector field with $dt_{\mathrm{eff}}=dt/(1+\alpha_L L_{\mathrm{clock}})$, a discrete analogue of $$d\tau=dt/(1+\alpha L)$$.

**Duality statement (ACD-EW).** On this Euclidean special case: (A) $G[\hat\phi]$ is shared Stage 2; (B) PM is a structure-preserving reconstructor that reduces residual relative to isotropic heat on jump-like $\phi_\star$ with noise; (C) $L_E$ associates with induction intensity and load-gating slows mid-run evolution without erasing PM's residual/edge advantages; (D) dynamics admit dual language (maximize / flow $S_{\mathrm{GfE}}$ $\leftrightarrow$ run structure-preserving channel $\mathcal{C}^{\mathrm{GfE}}$). **Rigor for the existence of this dual construction: constructive** (definitions + implemented toys), with residual dual theorems hybrid/soft as in §5.3.

**What ACD-EW does not claim.** Equivalence of full Lorentzian GfE (curvature-in-$G$, G-field, $\Lambda_G$) to the gravitational master equation; numeric identity $H_c^{\mathrm{toy}}\equiv S_{\mathrm{GfE}}$ or $H_c^{\mathrm{toy}}\equiv S_c$; identity $L\equiv G$; continuum gravity confirmation from lattice denoising.

---

### 5.3 Claims A--D (T1′ residual dual)

Primary analytic setting (T1′ write-up): unit step $\phi_\star=\mathbf{1}_{i\ge N/2}$, $\sigma=0.12$, $K=0.15$, explicit Euler $dt=0.08$. Residual $R=N^{-1}\|\hat\phi-\phi_\star\|_2^2$. The residual dual is **time-windowed (T1′)**, not residual domination for all $t\in(0,t_\star]$ (**C4**).

#### Claim A --- Unified pure residual window $U_\star$ (**C5**)

On the unified pure window


$$
U_\star \;=\; [1.36,\,2.40]
$$


(grid times in $U_\star$), under a spectral majorant with burn-in conductivity $\rho_b=0.42$, Dirichlet-form linear theory, interface bound, and PCRH$_b$,


$$
\mathbb{E}\,R_{\mathrm{PM}}(t) \;\le\; \mathbb{E}\,R_{\mathrm{heat}}(t).
$$


PCRH$_b$ is an **ensemble residual majorant** (large-MC certificate): **soft**. The unified pure argument covers the former hybrid intermediate grid $I_\star$ and the former pure-late band $[2.0,2.4]$ in one window. The short-time crossover $t\approx 1.2$ remains **outside** $U_\star$.

**Rigor:** analytic majorant + identity machinery, with **soft** PCRH$_b$ input.

#### Claim B --- Edge persistence (**C6**)

With probability $\gtrsim 0.87$, initial true jump height $H^0\ge 0.80$. On that high-probability event, for all $t\le T_{\mathrm{pers}}^\sharp\approx 1.67$,


$$
H^t \;\ge\; H_{\mathrm{floor}}=0.25 \;>\; K
$$


(super-threshold freeze; Lemma C′2#).

**Rigor:** **analytic** (flux ODE bound + Gaussian concentration).

#### Claim C --- Short-$t$ heat win as noise race (**C7**)

For $t\lesssim 1.2$, heat can win residual because noise reduction dominates jump blur. This is **not** dual failure. The identity


$$
\mathbb{E}(R_{\mathrm{heat}}-R_{\mathrm{PM}}) \;=\; R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}
$$


holds to numerical precision; crossover when $R_{\mathrm{blur}}=\Delta_{\mathrm{noise}}$ near $t\sim 1.2$. Mechanism in brief: heat must blur the unit jump on scale $\sqrt{t}$ (deterministic residual $\Theta(\sqrt{t}/N)$); PM freezes the true edge and plateaus but freezes some noise gradients too (noise-race tax $\Delta_{\mathrm{noise}}$); residual dual holds when blur exceeds that tax.

**Rigor:** **analytic identity** + **hybrid-experimental** accounting.

#### Claim D --- Load-PM as mild time change (**C8**)

Load-PM is a monotone time change of pure PM: internal time $\tau(t)=\int_0^t(1+\alpha_L L_{\mathrm{clock}})^{-1}\,ds\le t$. Empirically $\tau/t\sim 0.95$--$0.98$ on the dual window. Residual dual of load-PM versus heat is supported experimentally on the same window (high Monte Carlo pathwise fractions on $I_\star$ / $U_\star$).

**Rigor:** time-change definition **constructive**; residual dual vs heat **hybrid-experimental**.

#### Soft spot: PCRH$_b$

PCRH$_b$ (with $\rho_b=0.42$) is **ensemble-certified** for the toy class. A full pathwise Dirichlet-form proof without certificate remains **open**. Do not assert pure T1′ with **no** soft hypotheses. Further pure-proof polishing is optional paper depth, not a main program crisis: the residual dual program is **settled enough** at T1′ / $U_\star$.

**Paste-ready citation sentence.** *In a 1D lattice observation model with a single noisy jump, PM residual domination over isotropic heat holds on an intermediate window $U_\star=[1.36,2.40]$ (T1′; PCRH$_b$, $\rho_b=0.42$), with analytic edge persistence and noise-versus-blur accounting; load reparameterization preserves the dual experimentally as a slower clock. This supports constructive Euclidean ACD-EW, not continuum gravitational equivalence.*

---

### 5.4 Joint toys as pattern witnesses (6/6 SUPPORT)

Beyond the residual-window analysis, joint toys implement the full ACD-EW special case (observation + split load + scorecard criteria E1--E7). Under fixed seeds and IC families:

| Toy | Role | Outcome |
|-----|------|---------|
| 1D joint toy | Noisy step / two-bumps / ramp; heat vs PM vs load-PM | **6/6 SUPPORT** |
| 2D joint toy | Catte-style PM lift on planar lattice | **6/6 SUPPORT** |
| Blackjack-belief dual | Game-motivated field $\phi$ (belief geometry) | **6/6 SUPPORT**, **pattern only** |

**Interpretation (C2--C3).** Six-of-six SUPPORT means the Euclidean dual **pattern** is robust under these IC classes: PM residual better than heat on primary edged ICs; edge retention; no staircase on weak-gradient ramps; $L_E$ tracks $\mathbb{E}[G-1]$; load-gating slows mid-run evolution. That PM outperforms heat on edged structure is **expected** dual success, not a theory bug. Blackjack-belief is **not** blackjack EV, strategy ROI, or predictive card-channel $H_c^{\mathrm{game}}$.

**Non-claims for toys.** Lattice denoising is not empirical gravity. Scorecard success does not lift residual dual to continuum SPDE residual domination, multi-jump theorem-level domination, or 2D theorem-level residual dual. Toys witness **Layer D pattern**, not Layer G/M equivalence.

**Rigor:** **hybrid-experimental** (**C2**); structural expectation of PM > heat on edges (**C3**).

---

### 5.5 M5c / M5b: warm-up continuum vs dual residual

Layer W continuum hygiene and Layer D residual dual must not be conflated.

**M5b (smooth action limit --- conditional lemma).** Under hypotheses H1--H4 (fixed $C^3$ periodic field, point sampling, fixed $\alpha>0$, mesh $h\to 0$), the mesh-weighted discrete Euclidean warm-up action $S_h[\phi|_{\mathrm{grid}}]=h\sum_i -\ln\bigl(1+\alpha(D_h\phi)_i^2\bigr)$ approximates the continuum integral $S[\phi]=\int -\ln\bigl(1+\alpha|\phi'|^2\bigr)\,dx$ with error at most $C(\alpha,\|\phi'\|_\infty,\|\phi''\|_\infty,\|\phi'''\|_\infty)\,h$; the argument is Taylor consistency of forward differences, global Lipschitz continuity of $z\mapsto -\ln(1+\alpha z^2)$, and a standard Riemann-sum estimate (see Appendix A.5). This is a **conditional smooth lemma** (Layer **W** action consistency), **not** Γ-convergence, not a BV/jump theorem, not residual dual continuum, and not Lorentzian GfE or master-equation contact.

**M5c (PM energy descent, Layer W).** Continuum literature identifies PM with the gradient flow of the Euclidean warm-up energy/action (matched coupling $\alpha=1/K^2$ equates energy descent with action ascent up to a positive factor). On the discrete side, joint-toy explicit-Euler PM is consistent with **discrete gradient descent** of an edge energy whose conductivity matches the toy flux (under stated hypotheses; not a full scheme-convergence theorem). Optional numerical witnesses check energy descent along PM trajectories.

**Relationship to residual dual.** M5c lives on **Layer W**: action/energy and PM flux. Residual dual $H_c^{\mathrm{toy}}$ and T1′ / $U_\star$ live on **Layer D**. Discrete energy descent of the warm-up does **not** identify residual dual with continuum relative entropy of metrics, nor with von Neumann $S_c$. Continuum PM well-posedness / Catte regularization as $h\to 0$ and full T4 (Γ-limit + BV + residual dual continuum) remain **open**. The dual residual program and the warm-up continuum program are **siblings under ACD-EW**, not the same theorem.

---

### 5.6 M10 P1: non-identity of entropy objects

ACD-EW uses $H_c^{\mathrm{toy}}$ (tag **C**). Foundations computational entropy $H_c(f;p_X)=H(Y)$ is map-output Shannon (tag **A**). Gravity uses $S_c(\Phi;\rho)=S(\Phi(\rho))$ (tag **B**). These must not be silently identified.

**M10 P1** (hybrid-experimental) measures both $H_c^{\mathrm{toy}}$ and ensemble Shannon $H(Z)$ of coarsened reconstructor observables $Z(\hat\phi)$ (binary edge-location cut; 8-bin argmax of $|\nabla\hat\phi|$) on the standard 1D dual at times in / near $U_\star$. On that grid, MC means of $H_c^{\mathrm{toy}}$ sit near **$\sim 1.1$--$1.3$**, while ensemble $H(Z_{\mathrm{bin}})$ and $H(Z_8)$ are **$\approx 0$** (or at most $\mathcal{O}(0.1)$ on one heat row): residual dual quality and unsupervised coarsened Shannon of declared edge location are **not the same measured object**.

Structural reasons (definitional, no MC needed): $H_c^{\mathrm{toy}}$ is a **per-sample supervised score** using oracle $\phi_\star$ via residual $R$; $H(Z)$ is **across-sample Shannon** of a declared coarse alphabet without residual supervision. Aggregation, edge role (soft within-field entropy vs hard argmax location), and units differ. Residual dual ($R_{\mathrm{PM}}<R_{\mathrm{heat}}$) can hold while $H(Z)\approx 0$.

**Non-claims.** Not $S_c$; not continuum GfE; not $H_c^{\mathrm{toy}}\equiv H(Y)$ for the full field $\hat\phi\in\mathbb{R}^N$; not a proof that no other $Z$ ever co-moves. House style: tag $H_c^{\mathrm{toy}}$ on dual residual; reserve bare $H_c$ for unambiguous Tag A; never write $H_c^{\mathrm{toy}}=S_c$.

---

### 5.7 Claim inventory for Part 5

| ID | One-line | Rigor |
|----|----------|-------|
| **C1** | ACD-EW constructive Euclidean dual (warm-up $G[\phi]$, PM, observation channel, split load, load clock) | constructive (+ toys hybrid) |
| **C2** | Joint toys 6/6 SUPPORT: dual **pattern** robust | hybrid-experimental |
| **C3** | PM > heat on edged structure is expected dual success | structural |
| **C4** | Residual dual is time-windowed T1′, not all $t\in(0,t_\star]$ | analytic + hybrid |
| **C5** | $U_\star=[1.36,2.40]$, $\rho_b=0.42$, PCRH$_b$ soft | analytic + soft |
| **C6** | Edge persistence $H_{\mathrm{floor}}=0.25>K$ through $T_{\mathrm{pers}}^\sharp\approx 1.67$ | analytic |
| **C7** | Short-$t$ noise race; identity $R_{\mathrm{blur}}-\Delta_{\mathrm{noise}}$; crossover $\sim 1.2$ | analytic identity + hybrid |
| **C8** | Load-PM mild time change; residual dual vs heat on window | hybrid-experimental |

---

# 9. Continuum GfE contact --- M6 WEAK PASS / FAIL; M6b structural FAIL

### 6.1 Shared weak-field problem

Parts 3--4 recover Newtonian Poisson on **our** side (layer **M**) via **Path J/M** only (Clausius → Einstein → weak-field GR; load-clock on-shell calibration $\alpha\beta=4\pi G/c^4$). Continuum Bianconi GfE (layer **G**) is a **different** upper theory: relative entropy of metrics, low-coupling Einstein--Hilbert limit, and modified equations with $\Lambda_G$, $D_{\mu\nu}$, dressed $R^G$ away from strict low coupling. M6 asks only whether the two frameworks agree on a **shared weak-field problem**, not whether they are the same theory. Layers **W** / **D** dual success does not transfer automatically to **G** or **M**.

**Shared problem (static weak field).** Background Minkowski plus static Newtonian potential $\Phi\ll c^2$; classical mass density $\rho_m(\mathbf{x})$ (perfect fluid at rest, $T_{00}\approx\rho_m c^2$). Ask for the **leading** equation determining $\Phi$.

**Side A --- ours (Path J/M).** Assume $\mathcal{L}_g$ satisfies Clausius on local horizons so that the Einstein equation holds (Jacobson 1995 imported), or take Einstein as the thermodynamic fixed point of the channel generator. Weak-field GR yields $\nabla^2\Phi=4\pi G\rho_m$. Load $L\approx\beta_L\rho_m c^2/\epsilon_0$ calibrates the proper-time factor to the same $\Phi$ via on-shell matching $\alpha_L\beta_L=4\pi G/c^4$ (**Path M calibration**), not via the withdrawn pointwise Laplacian identity $\Phi\propto\rho\Rightarrow\nabla^2\Phi\propto\nabla^2\rho$.

**Side B --- Bianconi GfE (documented low coupling).** At low coupling the entropic action reduces to Einstein--Hilbert with zero cosmological constant (external paper claim). Standard GR weak-field linearization on that EH theory again yields $\nabla^2\Phi=4\pi G\rho_m$. Newton here is **via GR**, not via a load clock. Away from strict low coupling, modified equations involve $\Lambda_G(\tilde{\mathcal{G}})$, dressed $R^G$, and $D_{\mu\nu}$.

---

### 6.2 WEAK PASS at Poisson order (**C11**)

| Item | Ours (Path J/M) | GfE low coupling |
|------|-----------------|------------------|
| Leading PDE for $\Phi$ | $\nabla^2\Phi=4\pi G\rho_m$ | $\nabla^2\Phi=4\pi G\rho_m$ |
| Mechanism | Clausius/Einstein + load calibration | Relative-entropy action → EH → GR linearization |
| Extra fields at leading Newton | None if $\gamma_L,\delta_L$ dropped | None if $\tilde{\mathcal{G}}=\tilde I$, $\Lambda_G=0$ |

**Outcome:** **WEAK PASS** --- same leading Poisson equation. Equations agree at this order. The agreement is **real** and **expected** if both frameworks embed Einstein gravity at low demand. It is **supporting circumstantial evidence** that they sit in the same phenomenological class as GR --- **not** evidence that load dynamics equal Bianconi's relative-entropy Euler--Lagrange equations.

**Honesty limits.** WEAK PASS does **not** upgrade either theory to GR-level certainty. Path J still depends on Jacobson/Einstein input; Poisson is not free from GR. We did **not** solve Bianconi's field equations numerically.

---

### 6.3 FAIL of framework identity (**C12**)

| Criterion | Outcome |
|-----------|---------|
| Same leading Poisson $\nabla^2\Phi=4\pi G\rho_m$ | **WEAK PASS** |
| Same upper derivation mechanism | **FAIL** |
| Identifiable $(\alpha_L,\beta_L)=(\alpha_B,\beta_B)$ | **FAIL / refused** (M7) |
| Continuum GfE $\Leftrightarrow$ master equation | **FAIL** --- do not claim |

**Mechanisms differ.** Ours: Clausius constraint on a channel generator, Einstein as fixed point, load as scalar demand clock. GfE: relative entropy of metrics as primary action, low-coupling EH, then GR. Shared Poisson is shared **GR linearization**, not shared primary entropy object.

**Constant refusal.** Do **not** assert $\alpha_L\beta_L=\alpha_B/\beta_B$ (or $\alpha_L\beta_L\equiv\alpha_B/\beta_B$). The product $\alpha_L\beta_L$ is an **on-shell calibration** of our load clock to Newtonian redshift (Path M). The ratio $\alpha_B/\beta_B$ is a **coupling constant in Bianconi's field equations** (schematic $\kappa=\alpha_B/\beta_B$). Different roles; identification is refused without a new OPEN_MATH decision and an explicit continuum map. Also refuse $L\equiv G$ and $S_c\equiv\operatorname{Tr} g\ln G^{-1}$.

---

### 6.4 M6b: next-order structural FAIL (**C13**)

Leading Poisson does not discriminate mechanisms. Discrimination lives at **next order**.

**Our next-order candidates.** Full load


$$
L \;=\; \beta_L\frac{\rho_m c^2}{\epsilon_0} + \gamma_L\left|\frac{dS_c}{d\tau}\right|_{\mathrm{reg}} + \delta_L\frac{S_{\mathrm{boundary}}}{S_{\mathrm{BH}}},
$$


with clock expansion $d\tau/dt=1/(1+\alpha_L L)=1-\alpha_L L+\alpha_L^2 L^2-\cdots$. In a static weak field, $\gamma_L L_S$ vanishes in strict equilibrium and $\delta_L L_\partial$ is a screen term; nonlinear $\alpha_L^2 L_E^2$ is PPN-like bookkeeping only if carefully mapped. Crucially: under Path J the **metric** is primarily Einstein-sourced. Default reading of $\gamma_L,\delta_L$ is **additive scalar corrections to the clock**, not automatic modifications of $\nabla^2\Phi=4\pi G\rho_m$, unless a dynamical rule promotes $L_S,L_\partial$ into effective stress.

**GfE next-order candidates.** Schematic modified sector: $R^G_{(\mu\nu)}-\frac12 g_{\mu\nu}(R_G-2\Lambda_G)+D_{(\mu\nu)}=\kappa T_{(\mu\nu)}$ with $\Lambda_G\ge 0$ from the G-field functional and $D_{\mu\nu}$ from G-field derivatives. Linearized deformations of Poisson may involve Yukawa/scalar modes, effective $G_N$ renormalization, or emergent cosmological terms --- **structurally inside the metric field equations**.

**Primary structural conclusion.** Next-order extras **do not match as the same object class**:

| Ours (next order) | GfE (next order) | Label |
|-------------------|------------------|-------|
| $\gamma_L\|dS_c/d\tau\|$ in load **clock** | $D_{\mu\nu}$ in metric EOM | type mismatch unless a map is built |
| $\delta_L S_{\partial}/S_{\mathrm{BH}}$ screen ratio | not primary as holographic screen term in GfE action | does not map cleanly |
| load reparam only (no new Poisson source by default) | $\Lambda_G$, $D_{\mu\nu}$ **do** enter metric EOM | **structural divergence** |
| no intrinsic $\Lambda$ from load at low order | $\Lambda_G\ge 0$ from G-field alone | **structural divergence** |

**Outcome:** **structural FAIL** of next-order match (**C13**). Coefficient-level PPN / Yukawa comparison is **not established** (needs explicit Bianconi linearization). Do **not** assert $\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G$.

---

### 6.5 Interpretation: co-class via GR, not shared primary entropy

M6's honest reading is **co-class membership** with general relativity at low demand, not framework identity:

1. Both sides can recover $\nabla^2\Phi=4\pi G\rho_m$ because both (under stated assumptions) sit on the Einstein/GR weak-field track at leading order.
2. Upper mechanisms differ: channel + load clock versus relative entropy of metrics.
3. Next-order structures live in different slots: **clock factors** versus **metric EOM extras**.
4. Therefore Poisson agreement is **not** evidence that continuum load dynamics equal Bianconi EL equations, and **not** evidence that master equation $\Leftrightarrow$ continuum GfE.

**Where the interesting dual remains.** The constructive dual that is **settled enough** in this program is **ACD-EW on Layers W and D** (Part 5): shared Stage-2 $G[\phi]$, PM as reconstructor, residual dual T1′ / $U_\star$, load as mild time change. That dual is a **different mathematical layer** from M6's Lorentzian weak-field plug-test. Euclidean residual dual does **not** lift automatically to Poisson agreement; Poisson agreement does **not** lift residual dual to continuum gravity. Stage-1 / Stage-2 / Stage-3 of the program mental model must not be collapsed into symbolic identity of master equation and GfE action.

**Non-claims (M6 block).** No numerical solution of Bianconi field equations; no derivation of $\alpha_L\beta_L$ from $\alpha_B,\beta_B$; no master equation $\Leftrightarrow$ GfE; no next-order $\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G$; WEAK PASS does not confer GR-level certainty; Path J still imports Jacobson/Einstein.

---

### 6.6 Claim inventory for Part 6

| ID | One-line | Rigor |
|----|----------|-------|
| **C11** | M6: both frameworks → $\nabla^2\Phi=4\pi G\rho_m$ via Einstein/GR at leading weak field | **WEAK PASS** |
| **C12** | M6: not framework equivalence; mechanisms diverge; refuse $(\alpha_L,\beta_L)=(\alpha_B,\beta_B)$ | **FAIL identity** |
| **C13** | M6b: GfE extras in metric EOM; $\gamma_L,\delta_L$ in load clock unless promoted | **structural FAIL** |

---

## Sources (Parts 5--6)

| Role | Path |
|------|------|
| Claims freeze C1--C8, C11--C13 | Section 3 and Appendix B |
| Claim gate / layers W D G M | Section 3 and Appendix B |
| ACD-EW formal dual | Appendix A |
| T1′ claims A--D | Appendix A |
| $U_\star$, $\rho_b$, PCRH$_b$ | Appendix A |
| Load M2 / Claim D | Appendix A |
| M5b smooth action | Appendix A.5 |
| M5c PM / Layer W | Appendix A.4 |
| M10 P1 non-identity | Appendix A.6 |
| M6 plug-test | Appendix A |
| M6b next-order | Appendix A |
| Joint toys / envelopes | Appendix A.8 |
| R4a promotion no-go | Appendix A.7 |
| Program conclusions spine | Section 3 and Appendix B |

---

# 9.5 Continuum GfE applications as recovery targets

Continuum Gravity-from-Entropy (GfE) is not only a variational proposal; it has begun to generate **sectoral applications**---cosmological expansion and spherically symmetric black holes---that any entropic-gravity program must eventually face as recovery targets. This section treats those applications as **external literature**: they set benchmarks for what a mature continuum theory should explain, and they clarify what our channel--load program has *not* yet established at the honesty standard used for Newtonian Path J/M. We under-claim throughout. Shared weak-field Poisson (Section 7) does not automatically transfer inflationary or strong-field GfE results into load-clock theorems.

## 6B.1 Why applications matter as recovery targets

A continuum entropic theory earns credibility in layers. First comes an action or dynamical law and a controlled low-demand limit that recovers Einstein gravity and Newtonian Poisson. Second come **phenomenological sectors**: early-universe expansion, black-hole exteriors and evaporation, and observational bounds on extra parameters. Bianconi's foundational GfE construction supplies the first layer: relative entropy between the spacetime metric $g$ and a matter- or geometry-induced metric $G$ yields modified Einstein equations, a $G$-field dressing of the Einstein--Hilbert sector, and an emergent cosmological contribution $\Lambda_G$ [Bianconi, Phys. Rev. D **111**, 066001 (2025); arXiv:2408.14391]. The Euclidean warm-up further links a simplified GfE energy to Perona--Malik anisotropic diffusion [Bianconi, arXiv:2503.14048]---the continuum template for our constructive dual (Section 6), not a substitute for Lorentzian phenomenology.

Application papers in the GfE family address the second layer. They do **not** become theorems of the $\Phi_g$/$L$ master equation by citation alone. Their scientific role for this program is:

1. **Target specification.** What geometries, expansion histories, and evaporation laws should a peer continuum theory produce?
2. **Honesty calibration.** Do our historical recovery sketches meet the same explicit-input standard as Path J/M (external theorem + modeling assumption + calibration), or do they remain narrative?
3. **Non-transfer discipline.** Euclidean dual toys and residual dual windows must not be misread as inflation or black-hole evidence [cf. transfer limits discussed with ACD-EW].

## 6B.2 External claims: inflation from entropy

Thattarampilly and Zheng study vacuum cosmology within GfE and report that modified Friedmann dynamics admit an **inflationary phase without a dedicated inflaton field** [Thattarampilly and Zheng, arXiv:2509.23987]. In their analysis, the GfE structure supplies effective stress-energy contributions that can drive accelerated expansion; a phantom-like branch appears among dynamical regimes; and under a slow-roll map, predictions for the tensor-to-scalar ratio $r$ and spectral index $n_s$ can sit in CMB-compatible windows for suitable parameter choices.

For our purposes, the precise field content of their equations is less important than the **recovery target** they define:

- Early-universe accelerated expansion as a **regime of the continuum entropic equations**, not an extra scalar inserted by hand.
- Contact with CMB observables under controlled approximations.
- Dependence on GfE-specific structures ($G$-field / relative-entropy couplings) that have no automatic counterpart in a scalar load $L$.

We record these as **claims of the external GfE cosmology literature**, not as results derived from computational entropy $H_c$/$S_c$ or from the load clock $$d\tau=dt/(1+\alpha L)$$. In particular, ACD-EW residual dual windows and lattice reconstruction scores do **not** imply GfE inflation or CMB windows.

## 6B.3 External claims: spherically symmetric black holes

Thattarampilly, Zheng, and Kakkat analyze static and dynamical spherical geometries in GfE [Thattarampilly, Zheng, and Kakkat, arXiv:2602.13694]. Reported structure includes:

- Recovery of the **Schwarzschild** exterior as a controlled limit, with **higher-order corrections** of schematic order $O(r^{-4})$ (and related multipole/radial falloffs as derived in that work).
- Observational/constraint discussion using strong-field probes (e.g. S2 stellar orbits and Event Horizon Telescope-type bounds) to restrict GfE coupling parameters such as $\beta$.
- A dynamical sector with **Hawking-like mass loss**, including a term scaling as $\dot M\propto M^{-2}$, together with a constant **entropic leakage** contribution of the schematic form $-\beta/24$ in their mass-loss balance (notation as in the source paper).

Again, these statements are **external GfE black-hole phenomenology**. They define continuum strong-field targets: asymptotic flatness with controlled corrections; horizon thermodynamics compatible with evaporation-like loss; parameter bounds from observations. They do **not** establish that load-gated Perona--Malik dynamics on a lattice is a black-hole model, nor that discrete export $L_S$ equals entropic leakage $-\beta/24$.

Themes that *may* later enter an analogy checklist---horizon entropy, mass loss, information export---remain at **semantic** contact until a constructive map exists between channel load and GfE metric equations.

## 6B.4 Adjacent support: nonequilibrium $S_{\mathrm{gen}}$ and the Clausius layer

Kumar recovers semiclassical Einstein dynamics from a nonequilibrium thermodynamic argument based on generalized entropy $S_{\mathrm{gen}}$ and quantum expansion $\Theta$, without relying on entanglement-equilibrium hypotheses [Kumar, arXiv:2404.16912]. Relative to our program, this literature is best read as **support for a Clausius-type layer**---the idea that $\delta Q=T\,dS$ (or a carefully stated nonequilibrium cousin) can underwrite gravitational field equations---rather than as a proof of GfE, ACD-EW, or load-channel equivalence.

Path J of our Newtonian recovery already **imports** Jacobson's equilibrium Clausius→Einstein theorem as an external input [Jacobson, Phys. Rev. Lett. **75**, 1260 (1995)]. Kumar's route is adjacent motivation that thermodynamic/entropy-balance arguments need not be confined to a single equilibrium packaging. We do **not** assert $S_{\mathrm{gen}}\equiv S_c$, $S_{\mathrm{gen}}\equiv H_c$, or that Kumar derives Bianconi's relative-entropy action.

## 6B.5 Our recovery program: honest status

Historical drafts in the broader computational-entropy / load-channel narrative describe Schwarzschild geometry, horizon thermodynamics, FLRW expansion, and inflation-like boundary growth as "regimes of the master equation." At the rigor standard enforced for Newton, those drafts are **not** Path J/M recoveries. Specifically:

| What Path J/M requires | Status for BH / cosmology in *our* program |
|------------------------|-----------------------------------------------|
| Explicit external theorem or derivation chain | Newton: Jacobson + weak-field GR. BH/cosmo: not rebuilt at that standard |
| Clear modeling assumptions (what $\mathcal{L}_g$ must satisfy) | Stated for Clausius-on-horizons setup; not closed for full dynamical BH evaporation or inflationary matching |
| On-shell calibration honesty ($\alpha\beta=4\pi G/c^4$ class) | Path M for Newton only; no peer calibration for $r,n_s$ or $\dot M$ laws |
| Separation from withdrawn shortcuts | Pointwise Laplacian withdrawn for Newton; analogous algebraic shortcuts for BH/cosmo not re-validated |

**What would be needed for peer recovery** (program checklist, not a claim of completion):

1. **Cosmology.** A controlled continuum limit or effective FLRW reduction of the load-clocked channel (or an explicit embedding into Einstein + load corrections) producing accelerated expansion; a dictionary between boundary/capacity load $L_B$ (or related terms) and any $\Lambda$-like contribution; slow-roll or equivalent map to $(n_s,r)$ *only after* the dynamical equations are fixed; comparison---not automatic identification---with GfE inflation [arXiv:2509.23987].
2. **Black holes.** Horizon Clausius or nonequilibrium entropy balance sufficient to fix exterior geometry at Schwarzschild order; systematic $1/r$ expansion of corrections with parameter map to observational bounds; dynamical mass-loss law derived from channel/load or from promoted metric equations, not postulated by analogy to $-\beta/24$; clear type-safe distinction between scalar load contributions and metric-sector leakage.
3. **Shared infrastructure.** Either a promotion rule moving load corrections into the metric Euler--Lagrange sector (currently a structural no-go without extra structure; Section 7) or a proof that load-clock phenomenology can reproduce GfE application observables *without* that promotion---an open theoretical problem, not a dual-toy exercise.

Until those items exist, the correct public statement is: **Newton is the only recovery frozen at Path J/M honesty; BH and cosmology remain deferred targets informed by external GfE applications.**

## 6B.6 Shared endpoints versus shared mechanisms

Both continuum GfE and the load-channel framework aim at regimes that look like general relativity when demand is low. Section 7 records a **WEAK PASS**: leading weak-field Poisson $\nabla^2\Phi=4\pi G\rho_m$ on both sides, each via Einstein/GR (GfE through low-coupling reduction; ours through Path J/M). That agreement is **expected** if both embed GR; it is **not** evidence that load dynamics equal Bianconi's relative-entropy field equations, nor that GfE inflation/BH results transfer.

Beyond leading Newton, endpoints diverge in packaging: GfE places corrections in metric equations ($D_{\mu\nu}$, $\Lambda_G$, $G$-field); we place leading non-Einstein demand in a **scalar clock** unless an extra promotion is introduced. Application-level observables (inflationary windows, $O(r^{-4})$ exteriors, $\dot M$ laws) therefore remain **GfE-literature status** until reconstructed under our axioms.

## 6B.7 Summary table

| Phenomenon | GfE literature status (external) | Our program status | Shared Newton/GR endpoint? |
|------------|----------------------------------|--------------------|----------------------------|
| Leading weak-field Poisson $\nabla^2\Phi=4\pi G\rho_m$ | Low-coupling GfE $\to$ Einstein/GR [Bianconi, PRD **111**, 066001 (2025)] | Path J/M only; calibration $\alpha\beta=4\pi G/c^4$; pointwise path withdrawn | **Yes (WEAK PASS)** --- via GR on both sides; **not** framework identity |
| Vacuum / early-universe inflation without inflaton | Reported in GfE cosmology [Thattarampilly & Zheng, arXiv:2509.23987]; CMB window under slow-roll map | Historical narrative only; **not** Path J/M rigor; no peer $(n_s,r)$ derivation from $L$ | **Not established** as shared; GR inflation is a different standard story |
| FLRW expansion / effective $\Lambda$ | $\Lambda_G$ and modified Friedmann structure in GfE family | Load boundary/capacity terms **semantic** cosmology sketch; no frozen reduction | Possible **analogical** co-class with GR+$\Lambda$ only after maps exist |
| Schwarzschild exterior | Recovered with $O(r^{-4})$-class corrections [Thattarampilly et al., arXiv:2602.13694] | Historical sketches; **not** rebuilt at Path J/M honesty | Schwarzschild limit is GR; **corrections not shared** |
| BH mass loss / evaporation-like law | $\dot M\propto M^{-2}$ plus constant entropic leakage $\sim-\beta/24$ (external) | Not derived from $\Phi_g$/$L$; no identification with discrete $L_S$ | **No** --- not a shared frozen result |
| Observational bounds on extra couplings | S2/EHT-type constraints discussed in GfE BH paper | No peer parameter fit for load coefficients | **No** |
| Clausius / $\delta Q=T\,dS$ layer | Implicit in GfE thermodynamic reading; adjacent nonequilibrium $S_{\mathrm{gen}}$ route [Kumar, arXiv:2404.16912] | Path J **imports** Jacobson; Kumar as **support**, not identity $S_{\mathrm{gen}}\equiv S_c$ | Shared **methodology class** (thermodynamic gravity), not shared theorem |
| Euclidean warm-up / PM flow | PM as GfE warm-up gradient flow [Bianconi, arXiv:2503.14048] | ACD-EW constructive dual + time-windowed residual dual (Section 6) | Shared **warm-up layer** only; not Lorentzian applications |

## 6B.8 Takeaway

GfE application papers set the right **continuum ambition**: inflationary cosmology and corrected black holes with observational handles. They remain third-party results inside an active research program. Our frozen spine recovers Newtonian Poisson under explicit external inputs and calibrations; it constructs a Euclidean dual to the GfE warm-up; and it **refuses** symbolic identity of master equation and continuum GfE. Elevating black-hole and cosmological recoveries to peer status requires new continuum theory---effective reductions, promotion or alternative packaging of corrections, and calibrated observables---not additional lattice dual scorecards. Until then, Thattarampilly--Zheng and related works are **targets on the far side of the bridge**, not theorems on our near side.

# 10. Synthesis and open program

### 7.1 Program map (Stages 1--3)

The program is organized as a **three-stage** workflow. Stages are not interchangeable layers of one identity theorem; each has its own objects, rigor labels, and transfer rules.

```text
STAGE 1 --- Computational induction (ours)
  ρ, Φ_g, S_c / H_c, load L, $$d\tau=dt/(1+\alpha L)$$
  IDEM / decay / discrete maps = microstructure design + ledgers
        |
        v
STAGE 2 --- Geometric imprint (bridge)
  Structure-induced metric G  (or computational cousin)
  Type safety: L is a scalar; G is a metric --- L ≠ G
        |
        v
STAGE 3 --- Continuum GfE (macro target)
  Relative entropy of metrics → modified Einstein, Λ_G, G-field
  Low coupling → EH / Newton via GR (co-class contact, not framework identity)
```

| Stage | What is settled enough for a program report | What remains open |
|-------|---------------------------------------------|-------------------|
| **1** | Output-entropy definitions; master-equation form; Path J/M Newton; M11 discrete $H_c^{\mathrm{disc}}$ and three-slot $L^{\mathrm{disc}}$; D13 composition / Landauer relationships | Continuum $L$ limit from IDEM; full $S_c$ identity path; multi-region lattice export currents |
| **2** | ACD-EW Euclidean dual (constructive + toys as pattern witnesses); transfer dictionary with explicit non-maps | Lorentzian lift; continuum SPDE residual dual; promotion of load into metric sector |
| **3** | Shared weak-field Poisson (M6 WEAK PASS via GR); next-order structural FAIL (M6b) | Full GfE linearization / PPN; symbolic identity of actions and master equations (**refused** unless a new map is built) |

**Layer tags (CLAIM_GATE).** Layer **W** (warm-up / PM energy), **D** (Euclidean dual + T1′), **G** (full continuum GfE), **M** (master equation). Results proved only on W or D must not be cited as G or M theorems. M6 Poisson agreement is **GR-layer contact**, not W/D success and not G⇔M.

### 7.2 What is frozen (inventory)

The following are **program-level freezes**. They may be asserted with the rigor labels of CURRENT_CLAIMS.md; they are not GR-level theorems.

#### Dual residual program (closed as main crisis)

Heat-vs-PM residual dual work is **settled enough to stop as the default open problem**. Settled content includes:

- **C1--C8:** ACD-EW constructive Euclidean dual; joint toys **6/6 SUPPORT** as dual *pattern* (not continuum gravity); PM > heat on edges expected; residual dual **time-windowed (T1′)**; unified pure window $U_\star=[1.36,2.40]$ under PCRH$_b$ ($\rho_b=0.42$); edge persistence and short-$t$ noise race; load-PM as mild time change dual (hybrid).
- Soft spot retained honestly: PCRH$_b$ remains **ensemble-certified**; full pathwise Dirichlet-form proof is optional paper depth, not crisis response.
- **Decision D9 / dual close:** do not restart residual dual scorecards as main science track.

#### Path J/M Newton and calibration

- **C9--C10:** Newtonian Poisson only via **Path J** (Clausius → import Jacobson → Einstein → weak-field GR) and **Path M** (on-shell load-clock match; $\alpha\beta=4\pi G/c^4$ calibration). Pointwise $\Phi\propto\rho\Rightarrow\nabla^2$ is **withdrawn**.

#### M6 / M6b continuum contact

- **C11--C13:** Leading shared $\nabla^2\Phi=4\pi G\rho_m$ is a **WEAK PASS** (both via Einstein/GR). Framework identity **FAIL**. Next-order: GfE extras ($D_{\mu\nu}$, $\Lambda_G$) live in **metric EOM**; our $\gamma_L,\delta_L$ live in the load **clock** unless promoted --- **structural FAIL**. Optional promotion analysis: m6d-promotion-nogo.md (R4a).

#### M11 microstructure and D13 relationships

| Freeze | Content | Rigor |
|--------|---------|--------|
| **M11 design** | IDEM → operational $H_c^{\mathrm{disc}}$; three-slot $L^{\mathrm{disc}}=L_E^{\mathrm{disc}}+L_S^{\mathrm{disc}}+L_B^{\mathrm{disc}}$ aligned to continuum *roles* only | design + structural role map |
| **Phase 1--2** | AND ledger; multi-step Boolean; tiny SKI; minimal R/B shoe; coupled regions | constructive discrete accounting |
| **C14** | $L$ = demand from scale/rate of channel outcomes; scrambling ⇒ higher $L$ | semantic (program convention) |
| **D13 / R1** | Composition: Markov export; path-dependent $\sum L_S$ (same final $H_c^{\mathrm{disc}}$, different circuit cost) | constructive Stage-1 |
| **D13 / R2** | Landauer: single-shot $L_S=H(X\mid Y)$ (bit units) bounds erasure heat | constructive Stage-1 |
| **D13 / R3a** | Layer W: discrete PM descends matched warm-up energy; residual dual stays Layer D | constructive warm-up, not ME⇔GfE |

**Decision board status (D9--D13):** dual freeze; claim gate + object hygiene (M5/M10); M11 Phase 1--2 + continuum *motivation* (not continuum derivation); relationships R1--R3a as validation spine. These decisions **close residual dual as crisis** without claiming continuum gravity equivalence.

### 7.3 What remains open

| Track | Status | Comment |
|-------|--------|---------|
| **M9** Lorentzian / curvature-in-$G$ lift | Deferred | High cost; requires clear M6/M7 posture (already FAIL identity) |
| **M5 full $\Gamma$-limit** | Open | Hygiene + smooth $O(h)$ sketch exist; Γ-convergence **not** claimed |
| **M10 $S_c$ identity path** | Open beyond P1 | Dictionary + hybrid **non-identity** of $H_c^{\mathrm{toy}}$ vs coarsened objects; no $H_c^{\mathrm{toy}}\equiv S_c$ |
| **Continuum $L$ limit from IDEM** | Open / deferred | Discrete ledgers ≠ continuum $L(\rho,g)$; non-claim N9 |
| **M3--M4** Lyapunov / pure reparam | Deferred | After identity score if needed |
| **M12** true game channel $H_c^{\mathrm{game}}$ | Deferred | Belief dual is ACD-EW pattern only, not EV/ROI |
| **Optional PCRH$_b$ harden** | Optional | Pure math note depth only |

### 7.4 Status of this freeze (post-D15)

**This program report is frozen as final draft v1.0.** Positive conclusions P1--P11, withdrawn W1--W6, Stage-1 theorems T1--T5, M6/R4a no-gos, and non-claims N1--N9 are the closure package (see Results and §8; spine in Section 3 and Appendix B).

**Optional future cycles only (not required for this freeze):**

1. Pure PCRH$_b$ for dual SI (dual already program-closed).  
2. Multi-region lattice / continuum $L^{\mathrm{disc}}$ limit (opens O1 --- new cycle).  
3. Editorial LaTeX extraction of this report.

### 7.5 Deprioritize

| Deprioritized | Why |
|---------------|-----|
| More dual scorecards (new ICs only) | Pattern already 6/6×3; diminishing returns |
| Residual dual "crisis" restart | Program closed at T1′ / $U_\star$ honesty |
| Equating $\alpha_L\beta_L$ with Bianconi $\alpha_B/\beta_B$ | M7 refusal; different roles |
| Continuum $L$ or $G$ fits from AND Phase 1--2 | Non-claim N9; roles ≠ equalities |
| Equating $H_c^{\mathrm{toy}}$ with $S_c$ or $S_{\mathrm{GfE}}$ | M10 non-identity |

### 7.6 Open-board snapshot (M1--M12)

| ID | Status | Priority note |
|----|--------|----------------|
| **M1** residual dual | Program-level settled ($U_\star$) | Do not default-chase |
| **M2** load dual | Hybrid done | Optional pure |
| **M3--M4** Lyapunov / reparam | Deferred | After identity score if needed |
| **M5** warm-up continuum | Hygiene + smooth sketch; $\Gamma$ open | Program-report cite |
| **M6--M8** gravity contact | Done as analysis | Optional PPN; optional R4a |
| **M9** Lorentzian GfE lift | Deferred | High cost |
| **M10** $S_c$ vs $H_c^{\mathrm{toy}}$ | Dictionary + P1 non-identity | Identity path open |
| **M11** IDEM → $H_c^{\mathrm{disc}}$ / $L^{\mathrm{disc}}$ | P1--2 + coupled + motivation | Optional multi-region lattice |
| **M12** true game $H_c^{\mathrm{game}}$ | Deferred | Classical depth |

---

# 11. Final conclusions

### 8.1 Thesis restated (under-claimed)

This report freezes a **program**, not a derivation of Einstein from bits alone.

**Under-claimed thesis.** Computational entropy is the entropy of a map or channel's **output** distribution (classical $H_c$, quantum/gravity $S_c$). Gravity is modeled as a CPTP channel $\Phi_g$ whose instantaneous demand is a dimensionless **load** $L$ that reparameterizes proper time via $$d\tau=dt/(1+\alpha L)$$. Newtonian Poisson is recovered only via **Path J/M** (Clausius → Einstein → weak-field GR, then on-shell load-clock calibration $\alpha\beta=4\pi G/c^4$), not a withdrawn pointwise Laplacian identity. A **constructive Euclidean dual (ACD-EW)** links Bianconi's GfE **warm-up** (induced $G[\phi]$, Perona--Malik flow) to an observation channel with split load and load clock; residual dual of PM vs heat is **time-windowed (T1′ / $U_\star$)**, with joint toys as **pattern witnesses**, not continuum gravity. Weak-field contact with continuum GfE is a **WEAK PASS** on shared Poisson and a **FAIL** of framework identity (M6/M6b), reinforced by a next-order **promotion no-go** (R4a). Classical IDEM/decay machinery is connected by a **design dictionary** plus **constructive discrete ledgers** (Phase 1--2; T1--T5 composition and Landauer theorems) for $H_c^{\mathrm{disc}}$ and three-slot $L^{\mathrm{disc}}$ --- **not** a continuum derivation of $L$ or metric $G$.

Nothing in this conclusion upgrades the stance above preliminary research. Type safety remains locked: **$L\neq G$** and $L^{\mathrm{disc}}\neq L(\rho,g)$. Master equation $\Leftrightarrow$ continuum GfE is **not** asserted.

### 8.2 Positive conclusions P1--P11 (summary)

Full statements and sources: front **Results** section and Section 3 and Appendix B.

| ID | One-line freeze |
|----|-----------------|
| **P1** | Output entropy: $H_c=H(Y)$, $S_c=S(\Phi(\rho))$. |
| **P2** | Export chain rule; local drop is export (AND $\approx 1.189$). |
| **P3** | Landauer: Protocol R identifies $L_S=H(X\mid Y)$ with erasure bit-count. |
| **P4** | Path-dependent $\sum L_S$ (Direct $\approx 1.189$ vs Circuit $\approx 2.189$). |
| **P5** | Three load axes $L_E,L_S,L_B$; monist $L\propto H_c^{\mathrm{disc}}$ fails. |
| **P6** | Continuum $L$ **motivated**, not equal to $L^{\mathrm{disc}}$; $L\neq G$. |
| **P7** | Newton = Path J/M only; pointwise Laplacian **withdrawn**. |
| **P8** | ACD-EW dual + time-windowed residual $U_\star$; toys pattern only. |
| **P9** | PM warm-up energy descent (Layer W); residual dual stays Layer D. |
| **P10** | M6 WEAK PASS Poisson / FAIL framework identity. |
| **P11** | R4a: promotion no-go for next-order slot identity. |

**Finite Stage-1 theorems (constructive):** T1 chain rule; T2 cascade export additivity; T3 path-dependent $\sum L_S$; T4 Landauer/$L_S$ under Protocol R; T5 $L_B$ non-additivity --- §2 (Numbered Stage-1 theorems).

**Claims inventory C1--C14** (dual A--D detail, calibration honesty, M6 WEAK PASS/FAIL) remains the operational freeze sheet: Section 3 and Appendix B. Dual residual program: **settled enough to stop as main open crisis**.

### 8.3 Full non-claims N1--N9

Do **not** assert without new work (mirror banner + CURRENT_CLAIMS §3):

| ID | Non-claim |
|----|-----------|
| **N1** | Master equation $\Leftrightarrow$ Bianconi continuum GfE. |
| **N2** | $L \equiv G$, $S_c \equiv \operatorname{Tr} g\ln G^{-1}$, $\alpha_L\beta_L \equiv \alpha_B/\beta_B$. |
| **N3** | T1 residual domination for all $t\in(0,t_\star]$ (false; use T1′ / $U_\star$). |
| **N4** | Pure T1′ with **no** soft hypotheses (PCRH$_b$ still ensemble-certified). |
| **N5** | Newton from pointwise $\Phi\propto\rho$ Laplacian (**withdrawn**). |
| **N6** | Next-order $\gamma_L,\delta_L$ equal GfE $D_{\mu\nu},\Lambda_G$. |
| **N7** | Lattice denoising = empirical gravity. |
| **N8** | External GfE papers established on par with GR. |
| **N9** | IDEM/decay fully constructs continuum $L$ or $G$ (open / deferred). |

**Also (dual / M10 / M11 / M6 honesty):**

- No theorem-level multi-jump / 2D / continuum SPDE residual domination.  
- Toy residual $H_c^{\mathrm{toy}}$ $\neq$ von Neumann $S_c$ identity.  
- M11 discrete accounting $\neq$ continuum derivation; no Einstein from AND / SKI / shoe ledgers.  
- WEAK PASS does not upgrade either theory to GR-level certainty; Path J still imports Jacobson/Einstein.  
- Shared Poisson is co-class contact with GR at low demand, not evidence that load dynamics equal relative-entropy EL equations.  
- Refuted spine **W1--W6**: pointwise Newton path; raw T1-all-$t$; $L\equiv G$; ME $\Leftrightarrow$ GfE; IDEM constructs continuum $L$/$G$; lattice = empirical gravity.

### 8.4 R4a --- promotion no-go (one paragraph)

**R4a / M6d** (Appendix A.7) strengthens the next-order **FAIL** without reopening dual residual work or claiming GfE is wrong. At leading weak field both frameworks can share $\nabla^2\Phi=4\pi G\rho_m$ via Einstein/GR (**WEAK PASS**). At next order the extras live in **different slots**: GfE's $\Lambda_G$, $D_{\mu\nu}$, dressed curvature sit in **metric field equations**; our $\gamma_L|dS_c/d\tau|$, $\delta_L S_{\partial}/S_{\mathrm{BH}}$, and nonlinear $\alpha_L L$ sit in the **load clock** $$d\tau=dt/(1+\alpha L)$$ and do not automatically rewrite Poisson. Identifying those structures as the *same* correction requires an extra **promotion rule** (e.g. load into effective stress, load into metric ansatz, collapse of GfE extras to pure reparameterization, or a shared continuum action) that the **present** master equation does not supply. Coefficient retuning alone is a type error (scalar clock $\neq$ tensor EOM). Therefore framework equivalence at next order is **structurally blocked** inside the current formulation --- this is **P11**, reaffirms **N1/N2/N6**, and is **not** a PPN calculation or a refutation of Bianconi GfE.

### 8.5 What is not concluded without experiment (or heavy new theory)

The following remain **open** (PROGRAM_CONCLUSIONS O1--O5). They are not hidden failures of the freeze.

**Full roadmap:** Appendix C --- what **"needs new theory"** means (missing theorems/constructions, **not** "wrong program"); missing theorem statements for each O-item; experiment bucket (only after sharp predictions); suggested next-cycle priority (default **O1**).

| Open | Needs (bucket) |
|------|----------------|
| Continuum / hydrodynamic $L^{\mathrm{disc}}\to L(\rho,g)$ or IDEM $\to G$ | **New theory:** scale-separation / limit theorem (not more AND scorecards) |
| M5 full warm-up $\Gamma$-limit / BV / residual dual continuum | **New theory:** heavy analysis; smooth $O(h)$ sketch is not Γ |
| Constructive continuum $S_c$ dynamics beyond M10 dictionary | **New theory:** positive channel construction; no $H_c^{\mathrm{toy}}\equiv S_c$ |
| Lorentzian / curvature-in-$G$ GfE lift | **New theory** (high cost); optional experiment only after a prediction |
| Pathwise PCRH$_b$; true game $H_c^{\mathrm{game}}$; BH/cosmology at Path J/M honesty | **New theory** (optional dual SI / recoveries) |

**Not open as crisis:** heat/PM residual dual as default main track (closed at T1′ / $U_\star$ honesty).

**Without laboratory or astronomical experiment,** this program does **not** conclude empirical gravity, measured $\alpha\beta$, or observational discrimination of load-clock vs GfE next-order corrections. Constructive "experiments" in this program are **finite ledgers and lattice dual toys** --- constructive/hybrid witnesses under stated models, not gravity detections.

### 8.6 Data availability (optional)

Numerical ledgers and dual-toy protocols used as constructive witnesses are archived with the authors' research code. They are **not** required to read the argument: essential numbers appear in the text and Appendix A. A public repository URL may be added upon submission.


### 8.7 Scope of this document

This report is self-contained: definitions, theorems, numerical witnesses, and non-claims appear in the main text and Appendices A--C. A separate research code archive may be cited upon submission for reproducibility; it is not required to follow the logical argument.

### 8.8 Closing: claim freeze closes the program cycle

Under its own axioms and the external inputs listed in PROGRAM_CONCLUSIONS (Shannon, Landauer, Jacobson, weak-field GR, Bianconi warm-up literature), the program may assert: **output-entropy** foundations; **export** accounting and **Landauer** contact for single-shot $L_S$; multi-axial, **path-dependent** discrete demand that only **motivates** continuum load; a load-gated channel with **Path J/M** Newton; a constructive **Euclidean warm-up dual** with **windowed** residual honesty; and weak-field **co-class** contact with continuum GfE that **fails** as theory identity, with next-order identity **blocked** without promotion. Continuum construction of $L$ or $G$ from IDEM, Lorentzian GfE lift, full $\Gamma$-limits, and master-equation $\Leftrightarrow$ GfE remain **open or refused**, not hidden gaps.

**This draft freezes those conclusions under CLAIM_GATE.** The research cycle for claim establishment is closed at the present rigor levels: further default work is **paper polish and optional pure-depth notes**, not reopening residual dual as crisis, not equating $L$ with $G$, and not asserting ME $\Leftrightarrow$ GfE without a new constructive map.

---


# Appendix A. Constructive witnesses (self-contained summaries)

This appendix replaces repository file pointers. Numerical values below are fixed by finite classical probability (or fixed dual-toy protocols) and can be regenerated from the associated open-source research repository if desired; the **paper does not depend on hyperlinks**.

## A.1 Irreversible AND ledger

Fair bits $X=(X_1,X_2)$, $Y=X_1\land X_2$:
$H(X)=2$, $H(Y)=h_2(1/4)\approx 0.811278$, $H(X\mid Y)\approx 1.188722$,
$L_E=1$, $L_S=H(X\mid Y)$, soft $L_B=0.5$, $L^{\mathrm{disc}}\approx 2.689$.
Chain rule residual $<10^{-12}$.

## A.2 Composition / path dependence

Same final AND law $H(Z)\approx 0.811278$ and same residual export $H(X\mid Z)\approx 1.188722$, but cumulative stage cost differs:
- Direct AND: $\sum L_S \approx 1.188722$, $\sum L_E=1$
- Circuit (publish wire then AND): $\sum L_S \approx 2.188722$, $\sum L_E=2$
Markov cascade $Y=\mathrm{AND}$, $Z=\mathrm{NOT}(Y)$: $H(X\mid Z)=H(X\mid Y)+H(Y\mid Z)$ exactly.

## A.3 Landauer contact (Protocol R)

After AND, keep $Y$, reset residual input conditional on $Y$. Landauer (external) gives
$Q \ge k_B T\ln 2 \cdot H(X\mid Y)$. In units of $k_B T\ln 2$, $Q_{\min}/(k_B T\ln 2)=H(X\mid Y)=L_S$ for this single-shot assignment. Reversible dilation parks the same entropy as garbage until erased.

## A.4 Discrete PM energy descent (Layer W)

On the 1D noisy-step dual protocol, explicit-Euler Perona--Malik with matched edge energy $E_h$ is non-increasing along the trajectory; with matched coupling, $E_h=-(K^2/2)S_{\mathrm{matched}}$. This is Layer W (warm-up energy), not residual dual (Layer D).

## A.5 Smooth warm-up action (conditional)

Under $C^3$ periodic $\phi$, fixed $\alpha>0$, mesh $h\to 0$,
$S_h=h\sum_i -\ln(1+\alpha(D_h\phi)_i^2)$ approximates $\int -\ln(1+\alpha|\phi'|^2)\,dx$ at rate $O(h)$ (Taylor + Lipschitz + Riemann sum). Not $\Gamma$-convergence; not BV/jumps.

## A.6 Entropy-object non-identity (dual toys)

On dual times in $U_\star$, MC-mean residual dual score $H_c^{\mathrm{toy}}\sim 1.1$--$1.3$ while ensemble Shannon $H(Z)$ of coarsened edge location is $\approx 0$. Objects are not identical.

## A.7 Next-order promotion no-go (summary)

GfE next-order extras ($D_{\mu\nu}$, $\Lambda_G$) live in metric EOM; load $\gamma_L,\delta_L$ live in the clock $$d\tau=dt/(1+\alpha L)$$. Identifying them requires an extra promotion rule not supplied by the present master equation (structural no-go, not a PPN calculation).

## A.8 Euclidean dual toys (pattern witnesses)

1D/2D joint toys and a game-motivated belief dual report 6/6 SUPPORT scorecards for a Euclidean dual **pattern** (PM vs heat, load co-motion, etc.). These are **not** continuum gravity detections. Residual dual of PM vs heat is time-windowed on $U_\star=[1.36,2.40]$ under soft ensemble hypotheses (PCRH$_b$, $\rho_b=0.42$).

---

# Appendix B. Claim and non-claim checklist (standalone)

**May assert (program-level):** P1--P11 as in Results (output entropy; export; Landauer contact; path-dependent $\sum L_S$; three load roles; continuum $L$ motivated not identified; Path J/M Newton; Euclidean dual $U_\star$; warm-up PM descent; M6 WEAK PASS/FAIL identity; promotion no-go).

**Must not assert:** master equation $\Leftrightarrow$ continuum GfE; $L\equiv G$; residual dual for all $t\in(0,t_\star]$; pure T1$'$ with no soft hypotheses; Newton from pointwise $\Phi\propto\rho$; $\gamma_L,\delta_L=D_{\mu\nu},\Lambda_G$ without promotion; lattice denoising = empirical gravity; GfE literature as GR-peer foundation; IDEM constructs continuum $L$ or $G$.

---

# Appendix C. Open mathematical avenues (not claimed settled)

| ID | Missing work (theory) | Not fixed by |
|----|----------------------|--------------|
| O1 | Scale limit $L^{\mathrm{disc}}\to L(\rho,g)$ (or obstruction) | More dual scorecards |
| O2 | $\Gamma$-limit / BV continuum warm-up | Smooth $O(h)$ sketch alone |
| O3 | Positive continuum $S_c$ construction | Equating dual residual scores by fiat |
| O4 | Lorentzian GfE lift / true continuum dual | Euclidean toys alone |
| O5 | Optional pure PCRH$_b$; true game channels; honest BH/cosmo recoveries | Dual IC farming |

Experiment (GPS, cosmology, lab) only after a sharp continuum prediction exists.

---

*End of standalone program report v1.0.*

---

# References

1. C. E. Shannon, "A mathematical theory of communication," *Bell Syst. Tech. J.* **27**, 379 (1948).
2. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006).
3. R. Landauer, "Irreversibility and heat generation in the computing process," *IBM J. Res. Dev.* **5**, 183 (1961).
4. C. H. Bennett, "The thermodynamics of computation---a review," *Int. J. Theor. Phys.* **21**, 905 (1982).
5. T. Jacobson, "Thermodynamics of spacetime: The Einstein equation of state," *Phys. Rev. Lett.* **75**, 1260 (1995); arXiv:gr-qc/9504004.
6. E. P. Verlinde, "On the origin of gravity and the laws of Newton," *JHEP* **04**, 029 (2011); arXiv:1001.0785.
7. T. Padmanabhan, "Thermodynamical aspects of gravity: New insights," *Rep. Prog. Phys.* **73**, 046901 (2010); arXiv:0911.5004.
8. J. D. Bekenstein, "Black holes and entropy," *Phys. Rev. D* **7**, 2333 (1973).
9. S. W. Hawking, "Particle creation by black holes," *Commun. Math. Phys.* **43**, 199 (1975).
10. S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from AdS/CFT," *Phys. Rev. Lett.* **96**, 181602 (2006); arXiv:hep-th/0603001.
11. A. Almheiri *et al.*, "The entropy of Hawking radiation," *Rev. Mod. Phys.* **93**, 035002 (2021); arXiv:2006.06872.
12. L. Susskind, "Computational complexity and black hole horizons," *Fortsch. Phys.* **64**, 24 (2016); arXiv:1402.5674.
13. A. R. Brown *et al.*, "Complexity equals action," *Phys. Rev. Lett.* **116**, 191301 (2016); arXiv:1509.07876.
14. S. Lloyd, "Ultimate physical limits to computation," *Nature* **406**, 1047 (2000); arXiv:quant-ph/9908043.
15. G. Bianconi, "Gravity from entropy," *Phys. Rev. D* **111**, 066001 (2025); arXiv:2408.14391.
16. G. Bianconi, "Beyond holography: the entropic quantum gravity foundations of anisotropic diffusion," arXiv:2503.14048 (2025).
17. U. Thattarampilly and Y. Zheng, "Inflation from entropy," arXiv:2509.23987 (2025).
18. U. Thattarampilly, Y. Zheng, and V. Kakkat, "Spherically symmetric black holes in Gravity from Entropy and spontaneous emission," arXiv:2602.13694 (2026).
19. N. Kumar, "Recovering semiclassical Einstein's equation using generalized entropy," arXiv:2404.16912 (2024).
20. P. Perona and J. Malik, "Scale-space and edge detection using anisotropic diffusion," *IEEE Trans. Pattern Anal. Mach. Intell.* **12**, 629 (1990).
21. M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, 2000).
22. N. Margolus and L. B. Levitin, "The maximum speed of dynamical evolution," *Physica D* **120**, 188 (1998); arXiv:quant-ph/9710043.
23. J. Maldacena, "The large $N$ limit of superconformal field theories and supergravity," *Adv. Theor. Math. Phys.* **2**, 231 (1998); arXiv:hep-th/9711200.

**Literature roles in this paper.** [1--4]: computational entropy and Landauer contact. [5--9]: thermodynamic/entropic gravity and black-hole entropy. [10--14]: holography, complexity, and computational bounds. [15--18]: Gravity-from-Entropy continuum theory and applications. [19]: nonequilibrium Clausius/semiclassical Einstein support. [20]: anisotropic diffusion dual laboratory. [21--23]: quantum channels, speed limits, AdS/CFT context.
