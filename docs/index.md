# Computational Entropy

**Preliminary research.** Supporting constructions and numerical ledgers are real; **nothing here has GR-level certainty.**

The programme has **three tiers**. **Tier 1** (primary result) is computational entropy as a proposed mathematical object. **Tier 2** (secondary result, no gravity) is instruction persistence on a finite substrate. **Tier 3** (conjecture only) is the possible connection to gravity and a quantum layer.

## Tier 1 — Motivation: a Boltzmann–Shannon unification

The driving intent of this programme is a **Boltzmann–Shannon unification**: one notion of entropy that reads, on the same object, both as Shannon's uncertainty and as Boltzmann's \(k_B\ln W\) count of compatible microstates. The mathematical object proposed to serve it is **entropy defined on a channel's action on its input distribution**, rather than on a static distribution.

## Tier 1 — The core: channel-level entropy

**→ [Core: definition, theorems, new vs standard](core.md)** (start here)

For a channel \(p(y\mid x)\) acting on \(X\sim p_X\), the core quantities are the output entropy \(H_c=H(Y)\) and the **export** \(H(X\mid Y)\). They are linked for any channel by \(H(X)-H(Y)=H(X\mid Y)-H(Y\mid X)\). The core page also answers, candidly, **"Is this more than Shannon entropy?"**: not yet established, and it says what would have to be proved.

- **Paper A — Computational entropy (core):** output-distribution entropy, the export identity, Landauer coincidence for deterministic maps, and the path-dependent ledger (a convention). **No gravity claims.** → [read online](papers/paper-a.md) · [PDF](pdf/computational-entropy-paper-A.pdf){:download}
- **Paper C — The decay algebra (core):** the coupled export density is computed by a belief-transfer operator (proved in 1D and for general width; \(a=0.3007568\)), together with a constructive continuum entropy-production density \(\sigma(x)\) (witnessed). **No gravity claims.** → [read online](papers/paper-c.md) · [PDF](pdf/decay-algebra-paper-C.pdf){:download} · theorem notes [m11f](synthesis/m11f-theorem.md), [m11g](synthesis/m11g-theorem.md), [m11h](synthesis/m11h-2d.md), [m11i](synthesis/m11i-continuum.md)

## Tier 2 — Instruction persistence on a finite substrate

**→ [Tier 2: instruction persistence (research avenue)](tier2-instruction-persistence.md)**. The function-unidentifiability measure is reframed as a log-cardinality \(d_f^{\#}=\log_2\lvert[f]\rvert\) of the class of maps with the same output law. The page proves an exact composition rule \(d_f^{\#}=d_{g\circ f}^{\#}+R(g\mid f)\) and poses an open problem: the joint minimum of output capacity plus instruction persistence on a finite Toffoli register. No gravity.

**All PDFs on one page → [Downloads](downloads.md).**

## Tier 3 — Conjecture

> **Published as open conjecture resting on the core result (Tier 1), not as supported claims.**

- **Paper B — Emergent gravity (conjecture):** an information-theoretic *reformulation* of thermodynamic gravity. Channel + load is a Jacobson-shaped postulate; \(\alpha L=-\Phi/c^2\) on shell, and \(\alpha\beta=4\pi G/c^4\) is withdrawn (C17). Falsifiability verdict: **reformulation** ([analysis](papers/falsifiability.md)). → [read online](papers/paper-b.md) · [PDF](pdf/emergent-gravity-conjecture-paper-B.pdf){:download}
- **Integrated paper (conjecture):** the full manuscript, covering literature, the gravitational channel, load, master equation, and the quantum / von Neumann layer (AI-proposed scaffolding, not derived). → [read online](papers/paper-full.md) · [PDF](pdf/computational-entropy-integrated-paper.pdf){:download}

> **Honest boundary.** \(\sigma(x)\) is a **classical** entropy-production density, **not** the gravitational load term \(\gamma\lvert dS_c/d\tau\rvert\). Whether it *is* that term is a well-posed but open question, not a claim.

### Read the integrated paper (conjecture)

Every section of the manuscript is on this site:

1. **[Title & abstract](papers/chapters/00-front-matter.md)**  
2. **[§6. Channel, load & master equation](papers/chapters/06-channel-load-master-equation.md)** — includes the full **computational load** \(L(\rho,g)\) formula, load clock \(d\tau=dt/(1+\alpha L)\), and master equation  
3. Or open the **[full paper (single page)](papers/paper-full.md)** and use the right-hand table of contents  

**All chapters** appear under **Tier 3 — The integrated paper (conjecture)** in the left navigation (Introduction through References and appendices).

### Load equation (conjecture preview)

Dimensionless **computational load** (programme definition, conjecture; detail in [§6](papers/chapters/06-channel-load-master-equation.md)):

$$
L(\rho,g)
=
\beta \frac{E[\rho]}{V \epsilon_0}
+
\gamma \left| \frac{d S_c}{d\tau} \right|_{\mathrm{reg}}
+
\delta \frac{S_{\mathrm{boundary}}(\rho)}{S_{\mathrm{BH}}(A)}.
$$

Load clock and master equation:

$$
d\tau = \frac{dt}{1 + \alpha L(\rho,g)},
\qquad
\frac{d\rho}{dt}
=
\frac{1}{1 + \alpha L(\rho,g)}
\,\mathcal{L}_g\bigl[\rho;\, g_{\mu\nu}(\rho)\bigr].
$$

Canonical short form (same equations): [Channel, load, master equation](emergent-gravity/master-equation.md).

## Also on this site

| Link | Role |
|------|------|
| [Non-claims](non-claims.md) | What this program does *not* assert |
| [How to read](how-to-read.md) | Suggested paths for visitors |
| [Core (Tier 1)](core.md) | Definition, theorems, new vs standard |
| [Tier 2](tier2-instruction-persistence.md) | Instruction persistence (research avenue) |
| [Claims](synthesis/claims.md) · [Conclusions](synthesis/conclusions.md) | Frozen may-assert spine |
| [Final program report](papers/final-report.md) | In-repo freeze twin (with internal pointers) |
| [Source repository](https://github.com/cyotee/computational-entropy) | Code, ledgers, full research tree |

## Type safety (locked)

- **Load \(L\)** is a **dimensionless scalar** that clocks proper time.  
- **Structure metric \(G\)** is a **metric** (or edgewise cousin).  
- **\(L \neq G\)**. Discrete ledgers \(L^{\mathrm{disc}}\) are not continuum \(L\).
