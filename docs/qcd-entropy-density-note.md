# Tier 3 conjecture note: QCD entropy density and the joint-encoding view

**Tier:** 3 of 3, **conjecture only**. This is physics, so it sits under the Tier 3 quarantine. It makes no claim about QCD, about lattice methods, or about the lattice QCD sign problem.  
**Status:** 2026-11-26 · the finding was reported by a repo-reader agent and has **not yet been reproduced in-repo; source data needed**.

## 1. The reported finding

A repo-reader agent reported three things about the QCD entropy density \(s(T)\) across the crossover:

- the logarithmic slope \(d\ln s/d\ln T\) **peaks near 145 MeV**;
- there is **no knee**;
- **volume per nat**, \(1/s\), **falls** with \(T\).

**Provenance.**

- The repository does not contain this finding. A search of `master` and the working tree with `rg -i 'qcd|145 ?MeV|lattice'` finds no QCD analysis; the only matches are unrelated strings in notebooks.
- The reader's scratch notes sit outside the repository, on the agents' shared machine.
- Those notes name their inputs as HotQCD, arXiv:1407.6387 (tabulated EoS and its parametrization), and Wuppertal–Budapest, arXiv:1309.5258 (ancillary EoS data file). These citations are the reader's. The data files and the analysis script are not in this repository, and nothing here has been re-derived.

**The reader's printed numbers, quoted as reported:**

| Source (as cited by the reader) | Peak of \(d\ln s/d\ln T\) |
|---|---|
| HotQCD table | 6.95 at \(T=145\) MeV |
| HotQCD parametrization | 6.93 at \(T\approx147\) MeV |
| Wuppertal–Budapest data | 6.83 at \(T=135\) MeV |

- In the reader's HotQCD rows, \(s\) rises from 0.79 fm\(^{-3}\) at 130 MeV to 142.6 fm\(^{-3}\) at 400 MeV, so \(1/s\) falls monotonically.
- A smooth slope maximum rather than a kink is what one expects of a crossover. "No knee" is the reader's summary.

**Context.** The HotQCD paper's introduction places its results at zero net baryon number density. That regime is usually described as free of the sign problem, a Monte Carlo complex-action problem that arises at nonzero baryon chemical potential. So these data do not touch the sign problem, and a one-qubit toy cannot either.

## 2. How the joint-encoding view reframes it (conjecture)

In Cyotee's joint-encoding view, the relevant quantity is not raw volume per nat (\(1/s\)). It is the capacity left over after the output pays for its own instructions: capacity minus description cost, C_minus_K (see the [Joint Encoding Bound](thermal-channel-cost.md#7-joint-encoding-bound) section of the Tier 2 toy note).

On that reading:

- A falling \(1/s\) would not by itself say that "room per nat" shrinks in the relevant sense.
- What would matter is whether the self-description overhead grows faster or slower than the capacity ceiling as \(T\) rises.

**What the toy actually shows.** In the one-qubit toy, C_minus_K **falls** with \(T\), exactly where \(1/s\) falls. So the toy gives no support for expecting a quantity that rises with \(T\) while \(1/s\) falls.

**Open (not attempted).** Any QCD version would need:

- a definition of capacity and of description cost for a field-theory state;
- the reader's data committed to the repo, with provenance;
- a reproduction of the slope analysis.

Until then this note is a pointer, not a result.
