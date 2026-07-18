# Computational Entropy

**Preliminary research.** Supporting constructions and numerical ledgers are real; **nothing here has GR-level certainty.**

This site hosts the full integrated research paper **Computational Entropy and Emergent Gravity: From Output Distributions to Load-Gated Geometry**, plus short canonical reference pages.

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
