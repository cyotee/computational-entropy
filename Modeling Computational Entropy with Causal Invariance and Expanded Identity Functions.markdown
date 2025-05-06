# Modeling Computational Entropy with Causal Invariance and Expanded Identity Functions

This report investigates the feasibility of defining an expanded identity function to represent the number of variables, result tuple size, and a decay vector capturing how variable information decays into the result’s information content, within a model combining Category Theory, Information Theory, and Vectorial Lambda Calculus. The model aims to support the analogy between a function’s identity and a cryptographic key, enabling reversibility when sufficient information is known, and to connect this to causal invariance by demonstrating that results from emergently cryptographic function sets are invariant to their causal origins. The analysis focuses on functions like `sqrt(x)` and `max(x,y)`, which exhibit emergent cryptographic behavior when variable information is limited, and provides a formal framework, practical examples, and implications for computational entropy.

## Introduction

Causal invariance, within the interventionist account of causality, refers to the stability of causal relationships across different contexts or interventions ([Measuring Causal Invariance Formally](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8228138/)). In computational contexts, this translates to consistent input-output transformations regardless of operation order, provided the final result is the same. Information Theory quantifies uncertainty through Shannon entropy, \( H(X) = -\sum p(x_i) \log_2 p(x_i) \), which can measure the unpredictability of computational variables, including function identity ([Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))). Vectorial Lambda Calculus extends lambda calculus with linear-algebraic structures, enabling vector-based representations of functions and variables ([The vectorial λ-calculus](https://www.sciencedirect.com/science/article/pii/S0890540115000497)). Category Theory provides a framework for modeling computations as morphisms, ensuring structural consistency ([Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus)).

The user proposes an expanded identity function that encapsulates:
- **Number of Variables**: The input arity (e.g., 1 for `sqrt(x)`, 2 for `max(x,y)`).
- **Result Tuple Size**: The dimensionality of the output (e.g., 1D for both functions).
- **Decay Vector**: How variable information transforms into the result’s information content.

This function aims to ensure the result’s information content meets or exceeds that of derivable variables, supporting the analogy between function identity and a cryptographic key. The model connects to causal invariance by showing that emergently cryptographic function sets, like `[sqrt, max]`, produce results invariant to their specific causal paths when information is limited.

## Theoretical Framework

### Causal Invariance in Computations
Causal invariance ensures that the causal relationships between inputs and outputs remain stable across different computational paths or contexts. In multiway systems, causal invariance means isomorphic causal graphs regardless of the evolutionary path ([Causal Invariance](https://mathworld.wolfram.com/CausalInvariance.html)). For computations, this implies that the function’s effect on inputs is consistent, whether applied in different orders or with varying initial conditions, as long as the output is the same.

### Consistent Entropy
Entropy is consistent across variables, including function identity, meaning the total information content is preserved but can shift between components. A function is inherently reversible if sufficient entropy in known variables allows derivation of unknowns. Cryptographic functions, like zero-knowledge proofs, are irreversible without a key, even with function identity known, due to high entropy in hidden variables ([One-Way Function](https://en.wikipedia.org/wiki/One-way_function)).

### Expanded Identity Function
The expanded identity function is defined as:
- **Variable Count (\(N_v\))**: Number of input variables.
- **Result Tuple Size (\(D_r\))**: Dimensionality of the output.
- **Decay Vector (\(\mathbf{d}\))**: A vector \(\mathbf{d} = [d_1, d_2, \ldots, d_{N_v}]\), where \(d_i \in [0, 1]\) represents the fraction of variable \(i\)’s information retained in the result. If \(d_i = 0\), the variable is fully decayed (derivable); if \(d_i = 1\), it’s fully hidden.

The information content of the result, \(H_R\), must satisfy:
\[
H_R \geq \max_i \{ H(V_i) \mid d_i = 0 \}
\]
where \(H(V_i)\) is the entropy of variable \(i\), ensuring derivable variables are recoverable.

### Vectorial Lambda Calculus
Functions are encoded as vectors in a type space \(F = [U, B]\), where \(U = \text{Real} \to \text{Real}\) (unary) and \(B = \text{Real} \to \text{Real} \to \text{Real}\) (binary). The function identity is a vector \(\mathbf{f} = [f_U, f_B]\), selecting `sqrt` or `max`. Computations are terms like:
\[
f = \lambda \mathbf{f}. \lambda \mathbf{v}. (f_U \cdot f_1(\mathbf{v}_1) + f_B \cdot f_2(\mathbf{v}_1, \mathbf{v}_2))
\]
The type system enforces arity, aiding inference of function identity ([The vectorial λ-calculus](https://www.sciencedirect.com/science/article/pii/S0890540115000497)).

### Category Theory
Computations are morphisms in a category \(\mathcal{C}\), with objects as variable states and morphisms as functions. Causal invariance is ensured by stable compositions, e.g., \(f \circ g = g \circ f\) for commutative operations, maintaining consistent relationships ([Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus)).

## Application to `sqrt(x)` and `max(x,y)`

### Function Properties
- **sqrt(x)**: Unary, reversible (\(x = r^2\)). Entropy \(H_V = 0\) given result \(r\).
- **max(x,y)**: Binary, not uniquely reversible (\(x \leq r, y \leq r\)). Entropy \(H_V > 0\).
- **Unknown Identity**: With only result \(r\), \(H_F = 1\) bit (two functions). Variable count inference reduces \(H_F\).

### Emergent Cryptographic Behavior
With only result \(r = 4\):
- **sqrt(x)**: \(x = 16\), \(H_V = 0\).
- **max(x,y)**: \(x \leq 4, y \leq 4\), \(H_V \approx \log_2 4 = 2\) bits (assuming uniform distribution).
- **Unknown Function**: \(H_F = 1\), total entropy high, resembling cryptographic irreversibility.

With one input, `sqrt(x)` is inferred, reducing entropy. For `max(x,y)`, two inputs are needed, maintaining higher entropy.

### Causal Invariance
The set `[sqrt, max]` is emergently cryptographic when variable information is limited, as the result is invariant to the specific function used. This invariance reflects stable causal relationships, as the output’s information content is consistent across the set’s causal paths.

## Formal Model

### Entropy Components
- **Function Identity Entropy (\(H_F\))**:
  \[
  H_F = -\sum_{i=1}^k p(f_i) \log_2 p(f_i)
  \]
  For \(k = 2\), \(H_F = 1\) bit initially, reducing to 0 with variable count.
- **Variable Entropy (\(H_V\))**:
  \[
  H_V = -\sum_{\mathbf{v}} p(\mathbf{v} | r) \log_2 p(\mathbf{v} | r)
  \]
  Depends on function and known variables.
- **Hidden Entropy (\(H_{\text{hidden}}\))**: For cryptographic functions, entropy of keys or undecayed variables.
- **Total Entropy**:
  \[
  H_{\text{total}} = H_F + H_V + H_{\text{hidden}}
  \]

### Decay Vector
The decay vector \(\mathbf{d}\) quantifies information retention:
- For `sqrt(x)`, \(\mathbf{d} = [0]\), as \(x\) is derivable.
- For `max(x,y)`, \(\mathbf{d} = [d_1, d_2]\), where \(d_i \approx 1\) if inputs are underdetermined.
- In cryptographic functions, \(\mathbf{d}\) includes high values for keys.

### Reversibility
A function is reversible if:
\[
H_R + H_{\text{known}} \geq \sum_{i: d_i = 0} H(V_i)
\]
Cryptographic functions have high \(H_{\text{hidden}}\), preventing reversal without keys.

## Implications
This model supports the analogy between function identity and cryptographic keys, as both control reversibility. It extends to computational entropy by quantifying information decay and stability, applicable to diverse systems. The connection to causal invariance highlights how emergent cryptographic sets maintain invariant results, enhancing robustness in computational design.

## Challenges
- **Non-Linear Functions**: Vectorial Lambda Calculus is linear-focused, requiring extensions for `sqrt` and `max`.
- **Entropy Quantification**: Continuous variables complicate \(H_V\) calculations.
- **Cryptographic Security**: Emergent properties may not meet formal security standards.

## Table: Entropy Analysis for `[sqrt, max]`

| **Scenario**               | **Function Entropy (\(H_F\))** | **Variable Entropy (\(H_V\))** | **Hidden Entropy (\(H_{\text{hidden}}\))** | **Reversibility** |
|----------------------------|-------------------------------|-------------------------------|------------------------------------------|-------------------|
| Result only (\(r = 4\))    | 1 bit                        | High (\(\approx 2\) bits for `max`) | 0                                        | Not reversible    |
| One input (`sqrt`)         | 0                            | 0                             | 0                                        | Reversible        |
| Two inputs (`max`)         | 0                            | >0                            | 0                                        | Partially reversible |

## Key Citations
- [Causal invariance as a tacit aspiration](https://www.sciencedirect.com/science/article/pii/S0010028521000554)
- [Measuring Causal Invariance Formally](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8228138/)
- [An Invariant Cost Model for the Lambda Calculus](https://arxiv.org/abs/cs/0511045)
- [Information-Theoretic Approximation to Causal Models](https://arxiv.org/abs/2007.15047)
- [Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- [One-Way Function](https://en.wikipedia.org/wiki/One-way_function)
- [The vectorial λ-calculus](https://www.sciencedirect.com/science/article/pii/S0890540115000497)