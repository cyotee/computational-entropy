# AGENTS.md

Guidance for automated agents (and humans) editing this repository. See also [CLAUDE.md](CLAUDE.md) and [synthesis/CLAIM_GATE.md](synthesis/CLAIM_GATE.md).

## Known Pitfalls

### 1. Equal entropy is not informational equivalence (the `min(U1,U2)` drift)

**What happened.** [foundations/computational-entropy/definition.md](foundations/computational-entropy/definition.md) (Classical Examples, formerly ~L78–80) claimed that \(\sqrt{U}\), \(\max(U_1,U_2)\) and \(\min(U_1,U_2)\) are all informationally equivalent, with identical \(P(Y>0.7)\), mean and variance. That was false. \(\sqrt{U}\) and \(\max(U_1,U_2)\) share the density \(2y\) on \([0,1]\) (mean \(2/3\), \(P(Y>0.7)=0.51\)), but \(\min(U_1,U_2)\) has density \(2(1-y)\) (mean \(1/3\), \(P(Y>0.7)=0.09\)). The variance happens to coincide (\(1/18\) for all three), but the distribution, mean and tail probability differ. The reflection \(z=1-y\) preserves differential entropy, not the law. The same error had spread to the synthesis paper sources and their `docs/` mirrors, along with a weaker "same computational entropy ⇒ equivalent" definition that contradicted Paper A, Proposition 1.

**Rule.** When comparing maps for informational equivalence, verify the **full output distribution** (density / law \(p_Y\); for channels, the output state), not just the entropy or a few summary statistics. Equal law implies equal entropy, but equal entropy does not imply equal law. A reflection like \(\min\) vs \(\max\) keeps the entropy and changes the distribution.

**Checklist.**

- [ ] Any claim that two or more maps are (informationally) equivalent explicitly cites their shared output law (e.g. "both have density \(2y\) on \([0,1]\)").
- [ ] Any listed shared statistic (mean, variance, tail probability) has been computed for **every** map named, not inferred from equal entropy.
- [ ] Edits to the canonical definition are mirrored in the copies (synthesis paper sources, `quantum/Computational_Entropy.md`) and in `docs/` via `scripts/sync_site_docs.py`.
