# Procedural-share surface over noise and readout rank (Tier 2 toy)

**Tier:** 2 of 3. This is a **toy model and proof-of-concept for the shape of a curve (here, a surface)** in a two-qubit model.

- It is **not** evidence about hadronic or QCD physics.
- It makes no physical, quantum-foundational or thermodynamic claim.
- "Noise is the channel pre-paying for optionality" remains Cyotee's conjecture; nothing here tests it as physics.

**Status:** 2026-11-26 · computed. Follow-up to [Procedural share H(F|Y)](procedural-share.md) (CE-6/CE-7), fixing the contamination flag raised there: the candidate pool is now drawn before, and independently of, the channel.

**Script:** [`simulations/classical/procedural_share_surface.py`](https://github.com/cyotee/computational-entropy/blob/master/simulations/classical/procedural_share_surface.py) (pure numpy; imports `procedural_share.py` for the GAD Kraus operators and the \(p\leftrightarrow T\) convention; built-in self-checks; about 2 s, or about 8 s with `--robust 20`). Every number below is printed by

```
python simulations/classical/procedural_share_surface.py --robust 20      # T = 1 (default)
python simulations/classical/procedural_share_surface.py --T 0            # plain amplitude damping
python simulations/classical/procedural_share_surface.py --T inf
python simulations/classical/procedural_share_surface.py --encoding full  # degenerate control (§5)
```

Optional flags: `--seed`, `--pool` (default 50), `--ranks`, `--gammas`, `--gad P` (set the bath ground population directly), `--readout nested|random|both`, `--shots N` (finite-shot Monte Carlo), `--plot DIR` (PNG heatmaps, needs matplotlib; no images are committed).

## 1. Summary

- **Procedural share responds to readout rank in the predicted direction:** at every damping \(g<1\), \(H(F\mid Y)\) falls as the rank goes 2 → 16. At \(T=1\), \(g=0\) the drop is 0.271 bits; it shrinks with noise and vanishes at \(g=1\).
- **For the primary (nested) readout this is guaranteed by construction, not a test.** Rank \(r\) is a coarse-graining of rank \(2r\), so data processing forces \(H(F\mid Y)\) to be non-increasing in rank. The same argument forces it to be non-decreasing in \(g\) (§4).
- **Non-nested control (random entangled bases):** rank-monotonicity is not guaranteed there. It holds at every grid point for the default seed. Over 20 seeds it fails at 5 of 660 rank-doubling steps, by at most \(4.2\times10^{-4}\) bits. So it is a strong tendency, not a law.
- **The effect is small.** \(H(F\mid Y)\) never drops below 5.338 of \(\log_2 50 = 5.644\) bits. At most 0.306 bits (about 5%) of the candidate's identity is resolved, far above the floor \(\log_2 50-\log_2 r\).
- **Semantic share \(I(X;Y)\) is tiny** (at most 0.035 bits) because the receiver does not know which unitary scrambled the message. If \(f\) were known, it would be \(I(X;Y\mid F)\le 0.547\) bits.
- **Shape in noise:** \(H(F\mid Y)\) rises concavely in \(g\) at every rank (all second differences negative) and saturates at \(\log_2 50\) at \(g=1\). That endpoint is forced: at \(g=1\) the output state is independent of the input.
- **Shape in rank:** no diminishing returns. The nested steps are 0.034, 0.012 and 0.033 bits per doubling (mean over \(g\)); the random-basis steps grow (0.005, 0.012, 0.018).
- **Temperature barely matters:** across the \(T=0\), 1 and \(\infty\) runs, \(H(F\mid Y)\) differs by at most 0.022 bits at any grid point (0.019 for the random readout).
- **Bounds:** the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\) holds at 44/44 points, but it is a theorem in this joint law. The original \(I(X;Y)+H(F\mid Y)\le H(Y)\) holds at 0/44.

## 2. Model (fixed before any result was computed)

**Candidate pool, channel-independent.**

- 50 Haar-random two-qubit unitaries \(U_f\), drawn from `numpy.random.default_rng(2026)`. Each is the QR of a complex Ginibre matrix with the phase fix.
- The draw happens before any noise parameter is defined. The draw function takes only \((n,\text{seed})\).
- A SHA-256 hash of the pool (`114e410f9fcf4700…`) is taken right after the draw and re-checked after every grid point; the run aborts on any change.
- No candidate is filtered, added or reweighted by any channel quantity. The prior over \(F\) is uniform.

**Message and encoding.**

- One block is 2 channel uses. The same unknown \(U_f\) acts on both uses.
- Default encoding (`half`): each use carries one bit \(x\) on qubit A, and qubit B is a fixed reference \(\lvert 0\rangle\), so the input is \(\lvert x\,0\rangle\).
- \(X=(x_1,x_2)\) is uniform on 4 messages and independent of \(F\).

**Noise.**

- Each use applies \(U_f\), then generalized amplitude damping \(\mathrm{GAD}(g,p)\) independently on each qubit.
- Conventions follow Nielsen & Chuang §8.3.5 and Khatri–Sharma–Wilde, with \(N=1-p\); the Kraus operators are the ones in [procedural-share §2](procedural-share.md).
- \(p\) is the bath ground-state population, \(p=1/(1+e^{-1/T})\) with \(\hbar\omega=k_B=1\). The default \(T=1\) gives \(p=0.7311\); \(T=0\) is plain amplitude damping.
- The grid is \(g\in\{0,0.1,\dots,1\}\).

**Readout: one joint projective measurement on the 16-dimensional two-use output.** Rank \(r\) is the number of outcomes; each projector has rank \(16/r\).

| Rank \(r\) | Nested (primary): Z-bits kept, order (A₁,B₁,A₂,B₂) | Channel uses read |
|---|---|---|
| 2 | A₁ | 1 |
| 4 | A₁ B₁ | 1 |
| 8 | A₁ B₁ A₂ | 2 |
| 16 | A₁ B₁ A₂ B₂ | 2 |

- *Nested readout:* rank \(r\) keeps the first \(\log_2 r\) bits, so it is an exact coarse-graining of rank \(2r\). Batching two uses is what lifts the readout past one use's 2 bits, as in the 16-symbol CE-7 run.
- *Random readout (control):* for each \(r\), an independent Haar basis of \(\mathbb C^{16}\) (seed \(2026+1000+r\), fixed before any noise), grouped into \(r\) blocks of \(16/r\) vectors. It is entangled across the two uses, and the bases for different ranks are **not** nested.

**Quantities.** All are computed exactly from the joint law \(P(f,x,y)=\tfrac1{50}\tfrac14\operatorname{Tr}[\Pi_y\,\rho_{f,x_1}\otimes\rho_{f,x_2}]\); no sampling is needed.

- Procedural share: \(H(F\mid Y)=\sum_y P(y)\,H(P(F\mid y))\), with \(P(f\mid y)\propto\sum_x P(f,x,y)\).
- Semantic share: \(I(X;Y)\), with \(F\) marginalized.
- Also reported: \(I(F;Y)\), \(I(X;Y\mid F)\), \(H(F\mid X,Y)\) and \(H(Y)\).
- The exact identity \(H(Y)=I(F;Y)+I(X;Y\mid F)+H(Y\mid X,F)\) is checked to \(4\times10^{-16}\).

## 3. The surface (GAD, \(T=1\), \(p=0.7311\), nested readout)

**H(F|Y) [nested, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.609 | 5.486 | 5.453 | 5.338 |
| 0.1 | 5.616 | 5.529 | 5.502 | 5.419 |
| 0.2 | 5.622 | 5.561 | 5.539 | 5.480 |
| 0.3 | 5.627 | 5.585 | 5.568 | 5.527 |
| 0.4 | 5.631 | 5.603 | 5.591 | 5.563 |
| 0.5 | 5.635 | 5.617 | 5.608 | 5.590 |
| 0.6 | 5.638 | 5.627 | 5.621 | 5.611 |
| 0.7 | 5.640 | 5.635 | 5.631 | 5.626 |
| 0.8 | 5.642 | 5.640 | 5.638 | 5.636 |
| 0.9 | 5.643 | 5.643 | 5.642 | 5.642 |
| 1.0 | 5.644 | 5.644 | 5.644 | 5.644 |

**I(X;Y) [nested, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.000 | 0.001 | 0.014 | 0.035 |
| 0.1 | 0.000 | 0.001 | 0.009 | 0.021 |
| 0.2 | 0.000 | 0.001 | 0.006 | 0.013 |
| 0.3 | 0.000 | 0.000 | 0.004 | 0.007 |
| 0.4 | 0.000 | 0.000 | 0.002 | 0.004 |
| 0.5 | 0.000 | 0.000 | 0.001 | 0.002 |
| 0.6 | 0.000 | 0.000 | 0.000 | 0.001 |
| 0.7 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.8 | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.9 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1.0 | 0.000 | 0.000 | 0.000 | 0.000 |

**I(F;Y) [nested, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 0.035 | 0.158 | 0.191 | 0.306 |
| 0.1 | 0.028 | 0.115 | 0.142 | 0.225 |
| 0.2 | 0.022 | 0.083 | 0.105 | 0.163 |
| 0.3 | 0.017 | 0.059 | 0.076 | 0.117 |
| 0.4 | 0.013 | 0.041 | 0.053 | 0.081 |
| 0.5 | 0.009 | 0.027 | 0.036 | 0.053 |
| 0.6 | 0.006 | 0.017 | 0.022 | 0.033 |
| 0.7 | 0.003 | 0.009 | 0.013 | 0.018 |
| 0.8 | 0.002 | 0.004 | 0.006 | 0.008 |
| 0.9 | 0.000 | 0.001 | 0.001 | 0.002 |
| 1.0 | 0.000 | 0.000 | 0.000 | 0.000 |

For comparison, \(I(X;Y\mid F)\) (the semantic share if the receiver knew \(f\)) is 0.547 bits at \(g=0\), \(r=16\), and \(H(F\mid X,Y)\) (the procedural share if the receiver knew \(x\)) is 4.826 bits there; the script prints both full tables.

**Random-basis control** (same pool, same \(T\)):

**H(F|Y) [random, T=1]**

| \(g\) | r=2 | r=4 | r=8 | r=16 |
|---|---|---|---|---|
| 0.0 | 5.635 | 5.620 | 5.581 | 5.528 |
| 0.1 | 5.637 | 5.626 | 5.597 | 5.558 |
| 0.2 | 5.639 | 5.630 | 5.609 | 5.579 |
| 0.3 | 5.640 | 5.633 | 5.618 | 5.595 |
| 0.4 | 5.641 | 5.636 | 5.624 | 5.607 |
| 0.5 | 5.642 | 5.638 | 5.630 | 5.617 |
| 0.6 | 5.642 | 5.639 | 5.634 | 5.624 |
| 0.7 | 5.643 | 5.641 | 5.637 | 5.630 |
| 0.8 | 5.643 | 5.642 | 5.640 | 5.635 |
| 0.9 | 5.644 | 5.643 | 5.642 | 5.640 |
| 1.0 | 5.644 | 5.644 | 5.644 | 5.644 |

## 4. Does resolution lower the procedural share? Honest status

**Nested readout: yes at every \(g<1\), and guaranteed.**

- Rank-\(r\) outcomes are a deterministic function of rank-\(2r\) outcomes. By data processing, \(I(F;Y_r)\le I(F;Y_{2r})\), so \(H(F\mid Y)\) cannot increase with rank.
- The observed monotonicity therefore confirms the code, **not the conjecture**.
- The same holds along \(g\). GAD at fixed \(p\) composes as a semigroup in \(1-g\) (checked in the self-checks), and it maps diagonals to diagonals. So the Z-readout at larger \(g\) is a classical garbling of the Z-readout at smaller \(g\), and \(H(F\mid Y)\) cannot decrease with noise.

**Random readout: not guaranteed, observed with rare exceptions.**

- Different ranks use unrelated bases, so data processing says nothing.
- For seed 2026, \(H(F\mid Y)\) is non-increasing in rank and non-decreasing in \(g\) at all 44 points.
- Over seeds 1–20 (`--robust 20`), rank-doubling increases occur at 5 of 660 steps, the largest by \(4.16\times10^{-4}\) bits. No \(g\)-step decreases occur.
- This is the only part of the rank result that could have failed. It mostly did not, but the exceptions show it is a tendency, not a law.

**Magnitude.** The rank effect is real but small:

- Nested readout at \(g=0\): 5.609 → 5.338 bits.
- Random readout at \(g=0\): 5.635 → 5.528 bits.
- At \(g=0.5\) the nested drop is only 0.045 bits.

The ceiling on what can be learned is set less by rank than by the model: two uses, an unknown message, and a scrambling unitary. The floor \(\log_2 50-\log_2 r\) (1.64 bits at \(r=16\)) is nowhere near attained.

**Finite shots** (`--shots 4`, Monte Carlo): with 4 i.i.d. blocks, the nested \(g=0\), \(r=16\) share falls to about 4.6 bits. Repetition narrows the posterior much faster than rank does in this toy.

## 5. Degenerate encoding (a structural fact worth recording)

With `--encoding full` (all four basis states per use, so \(X\) is uniform on 16 messages), the \(X\)-averaged input is \(I/4\). Since \(U(I/4)U^\dagger=I/4\) for every unitary, \(P(y\mid f)\) is the same for all \(f\). As a result:

- \(I(F;Y)=0\) and \(H(F\mid Y)=\log_2 50\) exactly, at every \(g\) and every rank.
- The posterior never narrows unless the receiver also knows \(X\), via \(H(F\mid X,Y)\).

This is why the default uses a fixed reference qubit. The choice is a modelling convention, stated up front, not a tuning to get a result.

## 6. Accounting bounds

| Bound | Pass rate (nested and random, \(T=0,1,\infty\)) | Status |
|---|---|---|
| \(I(X;Y)+I(F;Y)\le H(Y)\) (corrected, CE-6/7) | 44/44 at each setting | Theorem here: \(X\perp F\) gives \(I(X;Y)\le I(X;Y\mid F)\), and the identity in §2 then implies it. A code check, not a finding. |
| \(I(X;Y)+H(F\mid Y)\le H(Y)\) (original) | 0/44 at each setting | Fails everywhere. \(H(F\mid Y)\ge 5.3\) bits, while \(H(Y)\le 4\). |

## 7. Status and non-claims

- This is a toy proof-of-concept for the shape of a surface. It is **not evidence about hadronic or QCD physics** and makes no physical claim.
- The headline monotonicity in rank and in noise is **guaranteed by data processing** for the primary readout. Only the random-basis control is a non-trivial check, and it shows rare small exceptions.
- Modelling choices: 2 channel uses, the `half` encoding, Z-basis or random-basis readout, a uniform prior over a 50-member Haar pool, and the same GAD on both qubits. Correlated inputs across uses, adaptive measurements and other pools were not explored.
