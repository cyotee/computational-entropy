# Computational Entropy

**Preliminary research.** Supporting constructions and numerical ledgers are real; **nothing here has GR-level certainty.**

This site hosts the research program's papers plus short canonical reference pages.

## Papers & downloads

The program is split into a **solid core** and a **conjecture**:

- **Paper A — Computational entropy (solid core):** output-distribution entropy, the export identity, Landauer-exactness, and path-dependence. **No gravity claims.** → [read online](papers/paper-a.md) · [PDF](pdf/computational-entropy-paper-A.pdf){:download}
- **Paper B — Emergent gravity (conjecture):** an information-theoretic *reformulation* of thermodynamic gravity; channel + load as a Jacobson-shaped postulate. → [read online](papers/paper-b.md) · [PDF](pdf/emergent-gravity-conjecture-paper-B.pdf){:download}
- **Integrated paper** (full manuscript, literature + theory). → [read online](papers/paper-full.md) · [PDF](pdf/computational-entropy-integrated-paper.pdf){:download}

**All PDFs on one page → [Downloads](downloads.md).** Falsifiability verdict: **reformulation** ([analysis](papers/falsifiability.md)).

## Read the paper

Start with the manuscript (every section is on this site):

1. **[Title & abstract](papers/chapters/00-front-matter.md)**  
2. **[§6. Channel, load & master equation](papers/chapters/06-channel-load-master-equation.md)** — includes the full **computational load** \(L(\rho,g)\) formula, load clock \(d\tau=dt/(1+\alpha L)\), and master equation  
3. Or open the **[full paper (single page)](papers/paper-full.md)** and use the right-hand table of contents  

**All chapters** appear under **The paper** in the left navigation (Introduction through References and appendices).

## Load equation (preview)

Dimensionless **computational load** (program definition; detail in [§6](papers/chapters/06-channel-load-master-equation.md)):

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
| [Claims](synthesis/claims.md) · [Conclusions](synthesis/conclusions.md) | Frozen may-assert spine |
| [Final program report](papers/final-report.md) | In-repo freeze twin (with internal pointers) |
| [Source repository](https://github.com/cyotee/computational-entropy) | Code, ledgers, full research tree |

## Type safety (locked)

- **Load \(L\)** is a **dimensionless scalar** that clocks proper time.  
- **Structure metric \(G\)** is a **metric** (or edgewise cousin).  
- **\(L \neq G\)**. Discrete ledgers \(L^{\mathrm{disc}}\) are not continuum \(L\).
