# Computational Entropy (Canonical Definition)

**Status:** Canonical source of truth (extracted 2026-06-22).

This file is the single authoritative version of the core definition. All other documents (including papers and the main `.tex`) should reference this file rather than duplicating the content.

---

# Computational Entropy

This project collects research into a computational property we are naming Computational Entropy.

## Premise

Entropy can be measured as a lack of order, or more appropriately, the predictability of a state.
Shannon Entropy calculates exactly this for a signal being transmitted over a channel.
But in that case, the inputs are expected to be non-random, or they are ignored. It does not measure the effect of a computation on random inputs.

Any function (or map) that transforms inputs will result in a probabilistic distribution of outputs.
This means that for any set of random inputs, there is a matching set of non-random outputs.
Meaning the predictability has been altered. And that implies that the entropy has been reduced.
Meaning information was imparted by the function on the inputs to produce the outputs.

This project aims to define and quantify how computing a function imparts this implicit information as a means of entropy transfer.
We will term this measure of entropy transfer as Computational Entropy.

## Definition

Computational entropy is an information-theoretic measure that depends solely on the statistical pattern of the output distribution produced by a computation, independent of its internal mechanics or algorithm.

## General Case (All Types of Functions)

For any map $  f  $ — deterministic, probabilistic (stochastic), or quantum channel — that takes an input random variable $  X  $ (with distribution $  p_X  $) and produces an output random variable $  Y  $, the computational entropy is the entropy of the induced marginal output distribution $  p_Y  $:

- Classical discrete case: Shannon entropy of the output probability mass function


$$
H_c(f; p_X) := H(Y) = -\sum_y p_Y(y) \log_2 p_Y(y)
$$


- Classical continuous case: Differential Shannon entropy of the output probability density function


$$
H_c(f; p_X) := h(Y) = -\int f_Y(y) \log_2 f_Y(y) \, dy
$$


- Quantum case: Von Neumann entropy of the output state of a quantum channel


$$
S_c(\Phi; \rho_X) := S(\rho_Y) = -\operatorname{Tr}\bigl(\Phi(\rho_X) \log_2 \Phi(\rho_X)\bigr)
$$


## Key Property

Two (or more) different maps — whether deterministic, probabilistic, or quantum — are informationally equivalent if they induce output distributions with the same computational entropy.
The internal mechanics (algorithm, randomness, or quantum operations) do not matter; only the final statistical pattern of possible outputs does.

## Classical Examples (Demonstrating the General Definition)

### Deterministic functions with identical outputs

Consider two genuinely different functions on uniform random variables $  U, U_1, U_2 \sim \text{Uniform}[0,1]  $:

- Function 1: $  Y_1 = \sqrt{U}  $ (square root of one uniform)
- Function 2: $  Y_2 = \max(U_1, U_2)  $ (maximum of two independent uniforms)

Both have the identical output PDF on [0,1]:


$$
f(y) = 2y
$$


The computational entropy is the differential Shannon entropy:


$$
H_c(Y) = -\int_0^1 2y \log_2 (2y) \, dy = -1 + \frac{1}{2 \ln 2} \approx -0.27865 \text{ bits}.
$$


Explicit derivation (for both functions):


$$
\log_2(2y) = 1 + \log_2 y
$$


$$
H_c = -\int_0^1 2y(1 + \log_2 y) \, dy = -1 - \int_0^1 2y \log_2 y \, dy.
$$


The integral $  \int_0^1 2y \log_2 y \, dy = -1/(2 \ln 2)  $, so


$$
H_c = -1 + \frac{1}{2 \ln 2} \approx -0.27865 \text{ bits}.
$$


(The same result holds for the reflected case $  Y_3 = \min(U_1, U_2)  $ because differential entropy is invariant under the substitution $  z = 1 - y  $.)

Thus, despite completely different internal operations, all three functions are informationally equivalent: any probability-based prediction (e.g., $  P(Y > 0.7)  $, expected value, variance) is identical for all three.
This is the exact property that makes computational entropy a powerful unifying measure.

### Probabilistic (stochastic) extension

A stochastic map that outputs according to a conditional probability distribution $  p(Y|X)  $ still has a well-defined marginal output distribution $  p_Y  $.
Its computational entropy is simply the Shannon (or differential) entropy of that marginal.
Different stochastic mechanisms that produce the same $  p_Y  $ are informationally equivalent.

### Quantum Generalization

When the computation is a quantum channel $  \Phi  $ acting on an input density operator $  \rho_X  $, we use von Neumann entropy of the output state.

This is the direct quantum analogue: it reduces exactly to differential Shannon entropy in the semiclassical limit and is the standard measure of output uncertainty in quantum information theory.
It is already used in gravitational physics (Ryu–Takayanagi formula, Page curve) to quantify processed information.

This definition is therefore fully general — it applies uniformly to deterministic classical functions, probabilistic classical maps, and quantum channels — while remaining grounded in standard information theory.
It provides the rigorous classical foundation for our gravitational channel $  \Phi_g  $ and the subsequent master equation.

## Global Conservation and Local Entropy Transfer

A common apparent paradox is that a computation can reduce local entropy (turning high-entropy random inputs into lower-entropy structured outputs), seemingly violating the second law.
Our framework resolves this cleanly through global conservation with local transfer.

### Classical Example (Irreversible AND Gate)

Two independent fair bits $  X_1, X_2  $: total input entropy $  H(X_1, X_2) = 2  $ bits.

Computation: $  Y = X_1 \land X_2  $.

Output entropy: $  H(Y) \approx 0.811  $ bits (apparent local reduction).

The “missing” entropy (~1.189 bits) is accounted for by the irreversible loss of distinguishability between input paths.
Globally, total entropy (system + environment) remains exactly 2 bits — it is conserved.
The computation did not create or destroy information; it transferred it from the system to the environment.

## In Our Framework

The gravitational channel $  \Phi_g  $ performs the same process on quantum microstates.
Each step overwrites prior information, exporting entropy to the environment (or holographic screen) while realizing a lower-entropy output pattern locally.

The computational load $  L  $ quantifies this demand and enforces proper-time slowing when needed.
Globally, total fine-grained entropy is conserved (unitary or CPTP evolution); locally, observers see an apparent reduction because fine-grained prior details are lost.

This realizes the original intuition: entropy is constant globally across time, with directed local transfer from future potential (high-entropy input possibilities) to past reality (lower-entropy realized outputs).
The master equation and load parameter $  L  $ make this transfer explicit and quantifiable.

This classical grounding (Shannon/differential entropy of the output) carries over unchanged to the quantum case, where von Neumann entropy of the output state of the gravitational channel plays the analogous role.
The definition is therefore both rigorous and consistent across classical and quantum regimes.
