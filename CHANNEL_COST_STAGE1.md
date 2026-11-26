# Channel cost, Stage 1: an operational definition (proposal, untested)

**Tier:** 2 of 3 (channel-level research avenue). This file makes **no gravitational and no quantum-gravity claims**, and no claim about hadronic or QCD physics. Where it touches the simulations, those are **toy models** (proof-of-concept for the shape of a curve in a one- or two-qubit setting), as their own headers say.

**Status:** 2026-11-26 · **definitional stage only.** The definition below is a **proposal**. It is untested against the accounting question. No new simulation was run. The only computation was a tiny inline check of the closed forms in §5, listed in §5.4 and not committed. Stage 2 (the accounting test against the 58 failure points) is **not started**. It waits on review of this file.

**Scope of the question (Cyotee, 2026-11-26).** Define the channel cost as an operational quantity. The leading candidate is the von Neumann entropy of the channel's own mediating subsystem: the bath, or whatever degrees of freedom implement the map. It is computed directly from that subsystem's density matrix, independent of any input or output distribution. This file reviews the code to answer three questions: (1) is the internal state accessible; (2) what changes would expose it; (3) a precise definition.

**Short answer.**

- **(1)** No channel-internal state exists anywhere in the code or in any saved output. The scripts carry only Kraus operators; no bath state or Stinespring isometry is built for the GAD noise channel. But every channel in the runs is a fixed, deterministic function of \((g,p)\), so its environment state is **exactly reconstructable** from code plus parameters. Nothing is lost.
- **(2)** Exposing it needs one small helper module, about 60 to 100 lines, plus about 20 lines per script for an extra output column. There is no stochastic "per trial" channel to log.
- **(3)** The input-independent, dilation-independent version of the candidate is the **map entropy**: the entropy of the normalised Choi state, which equals the entropy exchange at the maximally mixed input. It is **proposed as primary**, with closed form (§5) for generalized amplitude damping (GAD):
\[
c_{\rm ch}(g,p) = H\!\Big(\tfrac{a+s}{2},\ \tfrac{a-s}{2},\ \tfrac{pg}{2},\ \tfrac{(1-p)g}{2}\Big),\qquad a = 1-\tfrac g2,\quad s=\sqrt{a^2-p(1-p)g^2}.
\]
- **Definitional consequence for Stage 2 (§8).** This quantity is bounded by 2 bits per qubit use and is exactly 0 at \(g=0\). Added to the original form, it **cannot** close the CE-6 deficits. Those deficits reach 3.076 bits, and at the 11 grid points with \(g=0\) they are 3.00 bits against a cost of 0. So the rescue reading of channel cost is ruled out by definition before Stage 2 runs. What Stage 2 can still test is narrower (§8).

The quantity proposed here is **standard, not new.** It is the *map entropy* of Roga, Fannes and Życzkowski (arXiv:1101.4105, Int. J. Quantum Inf. 9, 1031 (2011)), which is the entropy of the Jamiołkowski state. It is also Schumacher's *entropy exchange* (Phys. Rev. A 54, 2614 (1996)) evaluated at the maximally mixed input. What is proposed here is only the **choice** to use it as this programme's "channel cost", and the conventions.

---

## 1. Conventions (inherited from the code)

| Item | Convention | Where fixed |
|---|---|---|
| Logs | base 2; every entropy in **bits**. \(H(\cdot)\) is Shannon entropy and \(S(\rho)=-\operatorname{Tr}\rho\log_2\rho\) is von Neumann entropy. | `procedural_share.H`, `joint_encoding_bound.vn_entropy` |
| Units | \(\hbar\omega = k_B = 1\) | all thermal scripts |
| GAD Kraus | \(A_0=\sqrt p\begin{pmatrix}1&0\\0&\sqrt{1-g}\end{pmatrix}\), \(A_1=\sqrt p\begin{pmatrix}0&\sqrt g\\0&0\end{pmatrix}\), \(A_2=\sqrt{1-p}\begin{pmatrix}\sqrt{1-g}&0\\0&1\end{pmatrix}\), \(A_3=\sqrt{1-p}\begin{pmatrix}0&0\\\sqrt g&0\end{pmatrix}\). Nielsen & Chuang §8.3.5; Khatri, Sharma & Wilde, arXiv:1903.07747, with \(N = 1-p\). | `procedural_share.gad_kraus` (lines 95–100) |
| Temperature | \(p\) = bath ground-state population \(=1/(1+e^{-1/T})\), so \(p\in[1/2,1]\Leftrightarrow T\ge 0\). \(p=1\) is plain amplitude damping (AD) at \(T=0\); \(p=1/2\) is \(T=\infty\). | `procedural_share.p_of_T` |
| CE-4 temperature (different!) | \(\gamma = 1/(e^{\beta\omega}+1)\) on **plain AD**. Here \(T\) is tied to the damping strength itself, not to a bath population, and that file labels it a toy parametrisation. | `thermal_channel_cost.py` header |
| Noise structure | per qubit, independently: two qubits per use, two uses per block (CE-9 to CE-12), so a block applies \(\mathrm{GAD}^{\otimes 4}\); single qubit, single use in the CE-6 one-bit run | `procedural_share_surface.two_qubit_gad_kraus` |
| Candidate map | \(U_f\) acts **before** the noise: \(\rho\mapsto (\mathrm{GAD}\otimes\mathrm{GAD})(U_f\rho U_f^\dagger)\) | `output_states` (CE-9), `out_states` (CE-10, CE-12) |
| Dephasing (CE-12) | per qubit, \(\{\sqrt{1-g/2}\,I,\ \sqrt{g/2}\,Z\}\) | `procedural_share_mlpool.kraus` |

**Symbol clash to avoid.** \(S_c(\Phi;\rho) := S(\Phi(\rho))\) already denotes the computational entropy of the channel **output** (GLOSSARY tag B; README notes it is scaffolding). The channel cost below is a **different object** and gets a different symbol, \(c_{\rm ch}\). It must not be identified with \(S_c\).

---

## 2. Question (1): is the channel's internal state accessible or reconstructable?

### 2.1 What the code builds

| Script | Channel objects built | Dilation / bath / environment | Written to disk |
|---|---|---|---|
| `thermal_channel_cost.py` (CE-4) | Kraus lists: AD, phase damping, depolarizing, bit flip, unitaries, resets, measurement | none | nothing (stdout only) |
| `joint_encoding_bound.py` (CE-5) | AD Kraus; Holevo quantities via `vn_entropy` of **outputs** | **one**: `stinespring_circuit_check` builds a 3-CNOT + 2-Ry system+ancilla unitary for **plain AD only** (\(p=1\)), ancilla in \(|0\rangle\). It uses that unitary only to check the system marginal (max error printed); the ancilla state is traced out and never returned. | nothing |
| `procedural_share.py` (CE-6/7) | `gad_kraus(g,p)` (4 Kraus); candidates reduced to laws \((q_0,q_1)\) | `_random_cptp` dilates the **pool B candidates** (random 2-qubit unitary on system \(\otimes |0\rangle\)), keeping only the 2 Kraus operators. This is a candidate, not the noise channel. No GAD dilation; \(p\) enters only as Kraus weights, and **no bath state is ever formed.** | nothing |
| `procedural_share_surface.py` (CE-9) | `two_qubit_gad_kraus` (16 Kraus, Kronecker pairs); output states \(\rho_{f,i}\) held in memory | none | optional PNG heatmaps (`--plot`) only |
| `procedural_share_informed.py` (CE-10) | same 16 Kraus; output states; Holevo of inputs | none | nothing |
| `procedural_share_structured.py` (CE-11) | same; structured pools | none | nothing |
| `procedural_share_mlpool.py` (CE-12, `ff7972f`) | `kraus("gad"/"dephasing", g, p)`; `out_states`; `ce6_overlap` recomputes the CE-6 one-bit run | none | nothing |

### 2.2 Saved run outputs

- **In the repo:** the only saved outputs for these runs are the tables in `docs/thermal-channel-cost.md`, `docs/procedural-share*.md`. Those are printed summary numbers: shares, pass counts, deficit ranges. No density matrix, Kraus set or per-point environment quantity is saved. (The `.txt` files under `simulations/bridging/` belong to unrelated earlier tracks.)
- **On the working box, outside the repo:** the stdout logs of the CE-12 run, e.g. `run_default.txt` and `run_eps02.txt`. They hold the same summary tables, including the CE-6 deficit range at the 58 failures (min / median / max = 0.047 / 1.455 / 3.076 bits). They give no per-point deficits and no channel-internal state.

### 2.3 What is reconstructable

- **Exactly reconstructable from code plus parameters, which is everything needed.** Each noise channel is a fixed CPTP map determined by \((g,p)\) (or \(g\) for dephasing): `gad_kraus` is closed form, with no randomness. Every quantity in the runs is computed **exactly** from probabilities, not sampled; the only exception is the optional finite-shot check `--shots` in CE-9. So for any grid point, candidate \(f\) and input, the environment state is a deterministic function of \((g,p,f,\text{input})\). The pools are seeded and hashed: CE-6 uses seeds 11 and 23, CE-9 to CE-11 use `default_rng(seed)` with a SHA-256 pool hash, and CE-12 uses `default_rng([s, 12])`. So the inputs are reproducible too.
- **Not reconstructable at all, and not needed:** nothing. There is no hidden stochastic channel realisation. "The channel's internal state at each trial" has **no referent** beyond (environment state as a function of \((g,p)\) and the input). The physical bath state is **not determined by the code**, because the code never commits to a physical dilation (§4).

---

## 3. Question (3), first part: the input-dependence problem

The leading candidate wants an entropy "independent of any input or output distribution". Taken literally, that fails for the environment **after** the interaction. For a Stinespring isometry \(V:\mathcal H_A\to\mathcal H_B\otimes\mathcal H_E\), \(\Phi(\rho)=\operatorname{Tr}_E V\rho V^\dagger\), the environment ends in
\[
\Phi^c(\rho) = \operatorname{Tr}_B V\rho V^\dagger,\qquad [\Phi^c(\rho)]_{kl} = \operatorname{Tr}\big(K_k\,\rho\,K_l^\dagger\big)\ \text{ for } V=\textstyle\sum_k K_k\otimes|k\rangle_E .
\]
\(\Phi^c\) is the **complementary channel**, and \(S(\Phi^c(\rho))\) depends on \(\rho\). Input independence therefore holds only for particular choices. Three are on the table.

| | Candidate | Formula | Input-independent? | Dilation-independent? | For GAD |
|---|---|---|---|---|---|
| **(A)** | entropy of the bath **before** interaction | \(S(\tau_E)\) | yes | **no** | \(h_2(p)\) for the thermal-qubit dilation; \(0\) for the purified (minimal) dilation |
| **(B)** | **map entropy** = entropy exchange at the maximally mixed input | \(S^{\rm map}(\Phi)=S\big(J(\Phi)/d\big)=S\big(\Phi^c(I/d)\big)\) | yes, **by convention** (canonical input \(I/d\)) | **yes** | closed form, §5 |
| **(C)** | min or max output entropy of \(\Phi^c\) | \(\min_\psi S(\Phi^c(\psi))\), \(\max_\rho S(\Phi^c(\rho))\) | yes, by optimisation | yes | no simple closed form; numeric |

Here \(J(\Phi) = (\mathrm{id}\otimes\Phi)(|\Omega\rangle\langle\Omega|)\) with unnormalised \(|\Omega\rangle=\sum_i|ii\rangle\), so \(J/d\) is the Choi state with the maximally entangled input. The equality \(S(J/d)=S(\Phi^c(I/d))\) holds because the joint state of reference, output and environment is pure.

### 3.1 Dilation non-uniqueness (stated explicitly)

- **For a given input, the environment entropy does not depend on the dilation**, provided the environment starts pure. Any two isometric dilations differ by a partial isometry on \(E\), so \(S(\Phi^c(\rho))\) is the same for all of them and equals the entropy exchange \(S_e(\rho,\Phi)\). That makes (B) and (C) properties of \(\Phi\) alone.
- **The bath's initial-state entropy (A) does depend on the dilation.** GAD has two standard realisations:
  - a qubit bath in the thermal state \(\tau_p=\mathrm{diag}(p,1-p)\), coupled by the excitation-preserving partial swap of strength \(g\) (§5.3), gives \(S(\tau_E)=h_2(p)\);
  - the same bath **purified** (a two-qubit environment, which is a minimal Stinespring dilation, because GAD has Kraus rank 4 for \(0<g\), \(1/2\le p<1\)) gives \(S(\tau_E)=0\).

  Both realise the same \(\Phi\). (A) is therefore a property of a **physical model**, not of the channel. It also behaves badly as a cost: in the thermal dilation it is \(h_2(p)>0\) at \(g=0\), where the channel is the identity, and it does not depend on \(g\) at all. (A) is kept only as a model-level alternate.
- A related model-level quantity is the bath entropy **change** \(S(\tau_E')-S(\tau_E)\) in the thermal dilation. It is input-dependent, can be negative, and is likewise dilation-dependent. It is not proposed here.

### 3.2 Recommendation

- **Primary: (B), map entropy.** It is a channel-only quantity (dilation-invariant), input-independent with a stated canonical input, closed form for GAD, additive (§6) and invariant under the candidate unitary (§4). It reads directly as the leading candidate: the entropy of the mediating subsystem's density matrix \(\Phi^c(I/d)\). The price is the convention that the probe is the maximally mixed state (equivalently, half of a maximally entangled pair). That is a choice, and it is stated.
- **Alternate (B′): entropy exchange at the run's actual average input**, \(S(\Phi^c(\bar\rho))\). It is operationally closer to a given run but input-dependent.
  - In the CE-6 one-bit run with the uniform input, \(\bar\rho=I/2\), so (B′) coincides with (B).
  - With the Blahut–Arimoto input it does not.
  - For the CE-9 half encoding, \(\bar\rho_{\rm use}=\tfrac I2\otimes|0\rangle\langle0|\) before \(U_f\). By the identity in §4 that is \(f\)-dependent, \(S_e(\bar\rho, \Phi\circ\mathcal U_f)=S_e(U_f\bar\rho U_f^\dagger,\Phi)\), and it is **not** the noise-only value.
- **Alternate (C): minimum output entropy of \(\Phi^c\)**, which equals the minimum output entropy of \(\Phi\) because \(S(\Phi(\psi))=S(\Phi^c(\psi))\) for pure \(\psi\). It needs an optimisation and has no simple GAD closed form; at \(g=0.5\), \(p=0.5\) the minimiser is not \(|0\rangle\) (§5.4). It is 0 for plain AD at every \(g\), since \(|0\rangle\) is a fixed pure state. That makes it insensitive to damping strength at \(T=0\), which argues against it as a cost. The max-entropy variant needs an optimisation over mixed inputs. Neither is proposed as primary.

---

## 4. Which map is "the channel"?

- **Recommendation: the noise channel alone.** That means \(\mathcal N=\mathrm{GAD}_{g,p}\) per qubit use, so \(\mathrm{GAD}_{g,p}^{\otimes 4}\) per CE-9 to CE-12 block and \(\mathrm{GAD}_{g,p}\) for CE-6. The readout and the candidate \(U_f\) are excluded.
- **For (B) the choice does not matter** whenever the candidate is unitary. This is checked, not guessed. Using \((I\otimes U)|\Omega\rangle=(U^{T}\otimes I)|\Omega\rangle\),
\[
J(\mathcal N\circ\mathcal U)=(U^{T}\otimes I)\,J(\mathcal N)\,(U^{T}\otimes I)^\dagger,\qquad J(\mathcal U\circ\mathcal N)=(I\otimes U)\,J(\mathcal N)\,(I\otimes U)^\dagger,
\]
  so both are unitarily equivalent to \(J(\mathcal N)\) and
\[
S^{\rm map}(\mathcal N\circ\mathcal U_f)=S^{\rm map}(\mathcal U_f\circ\mathcal N)=S^{\rm map}(\mathcal N)\quad\text{for every } f.
\]
  This was checked numerically on the 16-Kraus two-qubit GAD with a random \(4\times4\) unitary (§5.4). Consequences:
  - including \(U_f\) is harmless but carries **no information about \(f\)**: the channel cost cannot distinguish pool members;
  - for an input-dependent choice such as (B′) the two choices **do** differ, because \(S_e(\rho,\mathcal N\circ\mathcal U)=S_e(U\rho U^\dagger,\mathcal N)\). This is one more reason to prefer (B).
- **Non-unitary candidates.** CE-6 pool A includes resets, dephasing and measurement, and pool B has random CPTP maps. Each has its own map entropy. A "full-map" cost for those candidates would be candidate-dependent, and it is not the noise channel's cost. It is listed as an open choice, not proposed.
- **The readout** (nested-\(Z\) or random-basis projective measurement) is excluded. It is the observer's coarse-graining, and in this convention a rank-\(r\) readout is not part of the channel. So the proposed cost is **rank-independent** by construction. Its own map entropy as a quantum-to-classical map is 1 bit per measured qubit for a complete \(Z\) dephasing. That would be a separate readout cost if wanted.

---

## 5. Closed forms for GAD (and dephasing)

### 5.1 Environment state and spectrum at \(I/2\)

With the Kraus set of §1 and \(\rho=I/2\), \(W_{kl}=\tfrac12\operatorname{Tr}(A_l^\dagger A_k)\). The only nonzero cross term is between \(A_0\) and \(A_2\), giving
\[
W=\frac12\begin{pmatrix} p(2-g) & 0 & 2\sqrt{p(1-p)(1-g)} & 0\\ 0 & pg & 0 & 0\\ 2\sqrt{p(1-p)(1-g)} & 0 & (1-p)(2-g) & 0\\ 0&0&0&(1-p)g\end{pmatrix}.
\]
The \(\{A_0,A_2\}\) block has trace \(a=1-g/2\) and determinant \(p(1-p)g^2/4\). Hence the spectrum is
\[
\operatorname{spec} W=\Big\{\tfrac{a+s}{2},\ \tfrac{a-s}{2},\ \tfrac{pg}{2},\ \tfrac{(1-p)g}{2}\Big\},\qquad s=\sqrt{a^2-p(1-p)g^2},
\]
and the proposed channel cost per qubit use is
\[
\boxed{\,c_{\rm ch}(g,p) := S^{\rm map}(\mathrm{GAD}_{g,p}) = H\big(\operatorname{spec}W\big)\ \text{bits}\,}\qquad (0\le c_{\rm ch}\le 2).
\]

### 5.2 Limits and dependence

- **\(g=0\):** spectrum \(\{1,0,0,0\}\), so \(c_{\rm ch}=0\) at every \(p\), i.e. at every temperature. The identity channel costs nothing, unlike candidate (A).
- **\(p=1\) (plain AD, \(T=0\)):** spectrum \(\{1-g/2,\ g/2\}\), so \(c_{\rm ch}=h_2(g/2)\). This is the textbook AD entropy exchange at \(I/2\), and it reaches 1 bit at \(g=1\).
- **\(g=1\):** spectrum \(\{p/2,(1-p)/2,p/2,(1-p)/2\}\), so \(c_{\rm ch}=1+h_2(p)\). That is 1 bit at \(T=0\) and the maximum 2 bits \(=\log_2 d^2\) only at \(g=1\), \(T=\infty\). There the channel is the completely depolarizing map onto \(I/2\).
- **Temperature:** at fixed \(g>0\), \(c_{\rm ch}\) rises monotonically as \(p\) falls from 1 to \(1/2\) (\(T\) from 0 to \(\infty\)). It also rises monotonically in \(g\) at fixed \(p\). Both monotonicities were checked on grids (§5.4), not proved.
- **Example, \(T=1\) (\(p=0.7311\)):** \(c_{\rm ch}=1.137\) bits at \(g=0.5\) and \(1.840\) bits at \(g=1\).
- **Dephasing (CE-12):** \(\{\sqrt{1-g/2}\,I,\sqrt{g/2}\,Z\}\) gives \(c_{\rm ch}=h_2(g/2)\) per qubit, which is 1 bit at full dephasing.

### 5.3 Physical thermal dilation, used only for candidate (A)

On system \(\otimes\) bath in the basis \(|s\,b\rangle\), take
\[
U_g = |00\rangle\langle00|+|11\rangle\langle11| + \sqrt{1-g}\,\big(|01\rangle\langle01|+|10\rangle\langle10|\big) + \sqrt g\,\big(|10\rangle\langle01|-|01\rangle\langle10|\big),
\]
with the bath in \(\tau_p=\mathrm{diag}(p,1-p)\). Then \(\operatorname{Tr}_{\rm bath}U_g(\rho\otimes\tau_p)U_g^\dagger=\mathrm{GAD}_{g,p}(\rho)\) with exactly the code's Kraus set (checked, §5.4). Purifying \(\tau_p\) gives a two-qubit pure environment, which is a minimal Stinespring dilation. In that picture the post-interaction state of the two-qubit environment at input \(I/2\) has entropy \(c_{\rm ch}(g,p)\).

### 5.4 Inline sanity check (the only computation done)

This was a throwaway numpy script, not committed and not a simulation run. It imported `procedural_share.gad_kraus` and `procedural_share_surface.two_qubit_gad_kraus`.

| Check | Result |
|---|---|
| Closed form vs numeric \(S(J/2)\) vs numeric \(S(\Phi^c(I/2))\), on an \(11\times11\) grid in \((g,p)\) | max abs difference \(1.6\times10^{-15}\) |
| Limits: \(g=1\) gives \(1+h_2(p)\) at \(p=0.75\) and \(p=0.5\), and \(=1\) at \(p=1\); AD at \(g=0.4\) gives \(h_2(0.2)=0.7219\) | exact match |
| Partial-swap thermal dilation (§5.3) vs `gad_kraus` on random pure inputs at \((g,p) = (0.3,0.7), (0.9,0.55), (0.5,1)\) | max error \(2.2\times10^{-16}\) |
| \(S^{\rm map}\) of the two-qubit map \(\mathcal N\), \(\mathcal N\circ\mathcal U\), \(\mathcal U\circ\mathcal N\) (random \(U\)), and \(2\,c_{\rm ch}\), at \(g=0.37\), \(T=1\) | all \(1.826796\) |
| Dephasing at \(g=0.5\) vs \(h_2(0.25)\) | \(0.811278\) both |
| Monotone in \(g\) (\(p=0.7\), 101 points) and decreasing in \(p\) (\(g=0.6\), 51 points) | true |
| Min output entropy (C), pure real inputs, 181-point grid | \((g,p)=(0.5,1)\): 0; \((0.5,0.7)\): 0.527 vs 0.610 at \(|0\rangle\); \((1,0.7)\): 0.881 at \(|0\rangle\); \((0.5,0.5)\): 0.601 vs 0.811 at \(|0\rangle\). The minimiser is generally not \(|0\rangle\), so there is no simple closed form. |

---

## 6. Additivity, and the relation to CE-4 Landauer pricing

- **Additivity (theorem).** \(J(\Phi_1\otimes\Phi_2)\) is \(J(\Phi_1)\otimes J(\Phi_2)\) up to a reordering of factors, so \(S^{\rm map}(\Phi_1\otimes\Phi_2)=S^{\rm map}(\Phi_1)+S^{\rm map}(\Phi_2)\). Roga, Fannes and Życzkowski prove this for all Rényi orders. With per-qubit noise:
  - a CE-9 to CE-12 block costs \(4\,c_{\rm ch}(g,p)\), at most 8 bits;
  - one use (two qubits) costs \(2\,c_{\rm ch}\), checked in §5.4;
  - a CE-6 one-bit point costs \(c_{\rm ch}(g,p)\), at most 2 bits.
- **The cost is rank-independent and pool-independent** (§4). It depends only on \((g,p)\) and on the number of qubit uses.
- **Bits, not energy.** The proposed cost is an entropy in bits. A priced version can be defined **as a convention**, \(\tilde c_{\rm ch}:=c_{\rm ch}\,k_BT\ln2\), with \(T\) the GAD bath temperature \(1/\ln(p/(1-p))\). It is not claimed to equal any heat or work. It inherits two oddities:
  - it is 0 at \(T=0\) although \(c_{\rm ch}(g,1)=h_2(g/2)>0\);
  - it diverges at \(T=\infty\).

  So it should be kept separate from the bit-valued quantity.
- **Not the same object as CE-4's price.** CE-4 priced \(d^{\#}_\varepsilon\,k_BT\ln2\). There \(d^{\#}_\varepsilon=\log_2|C_\varepsilon|\) counts **candidate maps** within an \(\varepsilon\)-ball of the target's output law, so it depends on the pool and on \(\varepsilon\). It also uses a different temperature map (\(\gamma=1/(e^{\beta\omega}+1)\) on plain AD, not \(p\)). By contrast \(c_{\rm ch}\) depends on the channel alone.
  - **What they share:** both are in bits before pricing, and both can be multiplied by \(k_BT\ln2\) by convention.
  - **How they would be related:** only through a stated inequality or comparison at matched \((g,T)\). None is proposed or claimed. **They are not claimed to be equal or proportional.**

---

## 7. Question (2): modifications needed to expose the channel subsystem's density matrix

There is no per-trial stochastic channel: every run is an exact computation over a grid. "At each trial" therefore means each (grid point, candidate \(f\), input) triple. Proposed changes (scope only, **not implemented**):

1. **New helper module** `simulations/classical/channel_cost.py` (about 60–100 lines, pure numpy, importing `procedural_share`). It would contain:
   - `stinespring(kraus)`: the isometry \(V=\sum_k K_k\otimes|k\rangle_E\) (\(2\to 2\times4\) for GAD; \(4\to4\times16\) for the two-qubit map);
   - `gad_thermal_dilation(g, p)`: the partial swap \(U_g\) plus \(\tau_p\) of §5.3, with an optional purification, for candidate (A) and the bath picture;
   - `env_state(kraus, rho)`: \(W_{kl}=\operatorname{Tr}(K_k\rho K_l^\dagger)\), which is \(\Phi^c(\rho)\);
   - `map_entropy(kraus, d)`: \(S(J/d)\);
   - `gad_map_entropy(g, p)`: the closed form of §5.1.
2. **Self-checks** in that module, the same as §5.4:
   - closed form = Choi = \(\Phi^c(I/2)\);
   - the dilation reproduces `gad_kraus`;
   - unitary invariance;
   - additivity over `two_qubit_gad_kraus`;
   - the \(g=0\) and \(g=1\) limits.
3. **Hooks (about 20 lines per script, additive columns only, no change to existing numbers):**
   - **CE-6 / CE-12 one-bit run:** in `procedural_share_mlpool.ce6_overlap` (line 313), which loops over \((g,p)\) and calls `ps.gad_law`, add \(c_{\rm ch}(g,p)\) and the per-point deficit \(H(F\mid Y)-H(Y\mid X)\) to the per-point record. This is the Stage 2 hook. CE-12 currently prints only min / median / max of the deficit.
   - **CE-9 to CE-12 surfaces:** at the point where output states are formed, add an optional environment-state output \(W_{f,m}=\Phi^c(U_f\psi_m\psi_m^\dagger U_f^\dagger)\) (16×16 per qubit-pair use) for (B′). The places are `procedural_share_surface.output_states` (line 149), `procedural_share_informed.out_states` (line 201) and `procedural_share_mlpool.out_states` (line 204); `procedural_share_structured` reuses the informed path. For (B) a single number \(4\,c_{\rm ch}(g,p)\) per grid point suffices, because it is input- and \(f\)-independent.
   - **Optional `--dump-env PATH`** writing an `.npz` of \((g,p)\) to \(c_{\rm ch}\), and optionally the \(W_{f,m}\). Nothing is required on disk, since everything is exactly recomputable.
4. **Total scope:** roughly 150–200 lines across one new module and three or four small hooks, plus a doc section. No existing output changes.

---

## 8. Stage 2 plan (described only; **not run**) and the bound-size check

**The 58 failure points.** These come from CE-6 ([docs/procedural-share.md](docs/procedural-share.md) §4): the one-bit run, variant (a), pool A, \(\varepsilon=0.05\), uniform or capacity input, on the \(21\times11\) \((g,p)\) grid. It has 72 defined points, and the original form \(I(X;Y)+H(F\mid Y)\le H(Y)\), i.e. \(H(F\mid Y)\le H(Y\mid X)\), fails at 58. CE-12 reproduced this exactly. Deficits \(D:=H(F\mid Y)-H(Y\mid X)\) at the failures range over 0.047 / 1.455 / 3.076 bits (min / median / max).

**Planned test.** Take the cost-augmented original form
\[
H(F\mid Y)\ \le\ H(Y\mid X)+c_{\rm ch}(g,p)\qquad\Longleftrightarrow\qquad D(g,p)\le c_{\rm ch}(g,p).
\]
At each of the 58 points, compute \(D\) and \(c_{\rm ch}\) via the hooks of §7. Report the count of points where it holds, and the residual \(D-c_{\rm ch}\).

**Falsifiable criterion.** The channel-cost reading "the missing term is the channel's own entropy" is **ruled out** for this toy if \(D>c_{\rm ch}\) at any of the 58 points. It survives only if \(D\le c_{\rm ch}\) at all 58. The same test applies with (B′), the entropy exchange at the actual average input. That is identical to (B) for the uniform input and differs for the capacity input.

**Bound-size check (a definitional consequence, decided before Stage 2).**

- **Cap.** \(c_{\rm ch}\le\log_2 d^2=2\) bits for a qubit channel, and the same cap holds for (B′) and (C), since all are entropies on an environment of dimension at most 4. The maximum deficit is \(3.076>2\), so the planned test **cannot pass at all 58 points, for any \((g,p)\)**.
- **The \(g=0\) row.** There GAD is the identity at every \(p\), so \(c_{\rm ch}=0\). The published slice table (procedural-share.md §3) shows \(|C|=8\), \(H(F\mid Y)=3.00\) and \(H(Y\mid X)=0\), so \(D=3.00\) bits at each of the 11 \(p\) values of the grid. These are among the 58, because the class is nonempty and the original form fails. At those points the cost-augmented form demands \(H(F\mid Y)=0\), which is false.
- **Structural reason (consistent with CE-12).** CE-12 showed \(H(F\mid Y)\ge\log_2|C|-H(Y)\), which grows with the class size, while every correction term capped by \(H(X)\) or \(H(Y)\) is bounded. \(c_{\rm ch}\) is not capped by \(H(X)\) or \(H(Y)\), but it is capped by \(2\log_2 d\) and is **independent of the pool**. So the same argument applies to it: enlarging the pool or \(\varepsilon\) raises \(D\) at fixed \(c_{\rm ch}\). No channel-only term can track a pool-size-driven deficit.
- **Relation to the paper plan.** [PAPER_PLAN.md](PAPER_PLAN.md) §4 demotes the overlap-first repair and says to revisit it only if a channel-cost definition supplies a term that grows with the pool. The proposed \(c_{\rm ch}\) does not grow with the pool, so it does **not** meet that revisit condition. Channel cost remains parallel research and is not a dependency of the paper.
- **Verdict by definition:** under (B), (B′) or (C), channel cost **cannot rescue the original identity** on the CE-6 failures. This is a consequence of the definition and of already-published numbers, not a Stage 2 result.

**What Stage 2 could still usefully measure (if reviewed and approved).**

- (i) How many of the 58 have \(D\le c_{\rm ch}\), i.e. the size of the residual. That gives the exact count of points with \(D>2\); at least the 11 \(g=0\) points have \(D=3.00>c_{\rm ch}=0\).
- (ii) Whether \(c_{\rm ch}\) is useful as a **separate ledger entry** next to the corrected bound \(I(X;Y)+I(F;Y)\le H(Y)\). An example is comparing \(c_{\rm ch}\) with \(H(Y\mid X)\) along the grid. That is a comparison, not a rescue, and no relation between them is claimed here.
- (iii) Whether the model-level (A) adds anything once (B) is in hand.

None of this is run.

**Pool source for Stage 2 (CE-15, added after review request t21u).** The Stage 2 candidate pool is now ML-derived by default. `procedural_share_mlpool.ce6_overlap(pool_source="ml")` uses pool A with its 20 Haar members replaced by 20 Margolus–Levitin one-bit laws, drawn from the saved pool `simulations/classical/data/ce15_ml_pool.json`. `pool_source="A"` reproduces the 58. On the ML-derived pool the original form fails at 38 of 81 defined points, with deficits up to 2.933 bits. The cap argument above is unchanged. Details are in [docs/procedural-share-mlpool.md](docs/procedural-share-mlpool.md) §9. No channel cost is computed.

---

## 9. Labels and non-claims

- **Proposal, untested.** "Channel cost := map entropy of the noise channel" is a **definition proposed for review**. It is not a result. Its only established properties are standard theorems: dilation invariance, additivity and unitary invariance, plus the closed form and limits verified in §5.4.
- **Not new.** The map entropy and the entropy exchange are standard: Roga–Fannes–Życzkowski 2011; Schumacher 1996; Nielsen & Chuang ch. 12. Only their adoption as this programme's channel cost is proposed.
- **Not \(S_c\).** \(c_{\rm ch}\) is not the computational entropy \(S_c=S(\Phi(\rho))\), and the two are not identified.
- **Not a heat.** The priced form \(c_{\rm ch}k_BT\ln2\) is a convention, as in CE-4. No equality with CE-4's \(d^{\#}_\varepsilon k_BT\ln2\) or with any thermodynamic quantity is claimed.
- **Toy scope.** Every simulation referenced is a one- or two-qubit toy (proof-of-concept for curve shapes). It is not evidence about hadronic or QCD physics.
- **Stage 2 not started.** The accounting test waits on review of this file.
