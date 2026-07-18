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

The semantic alignment with the present program is clear: geometry is not an independent absolute backdrop; it is co-determined with the information structure of matter; low "demand" recovers GR/Newton; high demand produces departures (emergent $\Lambda_G$, modified equations). The **structural** differences are equally clear and must not be erased. Bianconi's primary entropy object is relative entropy of **metrics-as-operators**; ours is computational entropy of a **channel output**. Bianconi's dynamics are Euler--Lagrange equations from an action; ours are a master equation with load-gated proper time 

$$
d\tau=dt/(1+\alpha L)
$$

. Bianconi's auxiliary G-field is a metric dressing with second-derivative structures in the field equations; our $L$ is a **dimensionless scalar** demand. Type safety forbids writing $L \equiv G$ or $S_c \equiv \operatorname{Tr}\, g\ln G^{-1}$. Weak-field contact can be a shared Poisson end-state via Einstein/GR (a WEAK PASS of co-class with GR) while mechanism identity and next-order corrections fail (structural FAIL of framework equivalence). Those distinctions are program locks, not temporary pedantry.

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
| Present work: $\Phi_g + L + H_c/S_c$ | Output Shannon $H_c$ / von Neumann $S_c$ of channel outputs; export $H(X\mid Y)$ classically | CPTP channel + load $L$; 

$$
d\tau=dt/(1+\alpha L)
$$

; Clausius on $\mathcal{L}_g$ | IDEM / decay / games (discrete ledgers); Euclidean observation toys | **Path J/M only**: Clausius $\to$ Einstein (imported) $\to$ Poisson; $\alpha\beta=4\pi G/c^4$ on-shell calibration |

**What we share.** With Jacobson, we take thermodynamic consistency on local horizons as the bridge from information bookkeeping to Einstein gravity (imported, not re-proved). With Verlinde and holography, we accept that boundary information capacity and screen-like terms organize strong-field demand. With Bianconi GfE, we share the broad program that geometry is co-determined with matter's information structure, that low demand recovers Einstein/Newton, and that a Euclidean relative-entropy warm-up has an algorithmic dual in anisotropic diffusion. With Kumar, we share interest in nonequilibrium entropy production as a route to semiclassical gravitational equations. With classical information theory, we share output-centric entropy and Landauer contact for irreversible export.

**What we refuse to identify.** We refuse $L \equiv G$: load is a dimensionless scalar; $G$ is a metric (or edgewise cousin). We refuse $S_c \equiv \operatorname{Tr}\, g\ln G^{-1}$: computational entropy is an output entropy of a channel, not relative entropy of metric operators. We refuse master equation $\Leftrightarrow$ full continuum GfE action and EL system. We refuse residual dual of PM versus heat as continuum gravity confirmation, and lattice denoising as empirical gravity. We refuse free derivation of Newton's constant from load alone: Path M is on-shell calibration conditional on Path J. We refuse IDEM/decay as a completed construction of continuum $L$ or $G$. We refuse next-order load-clock coefficients as identical to GfE extras $D_{\mu\nu}$ and $\Lambda_G$ without a constructive map. External GfE papers remain peers in an active research program, not GR-level foundations.

In short, the intellectual landscape supplies thermodynamic gravity, holographic complexity, continuum relative-entropy actions, and classical irreversible computation as **resources and peers**. The present work contributes a single operational triad---output computational entropy, gravitational CPTP channel, and load-clocked master equation---plus a staged bridge posture that keeps Euclidean constructive duality where it is earned and continuum identity where it is not. We now develop the framework in detail.
