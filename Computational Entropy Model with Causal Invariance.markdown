# Modeling Computational Entropy with Causal Invariance

This report explores the feasibility of defining a model that integrates Category Theory, Information Theory, and Vectorial Lambda Calculus to describe the relationship between causal invariance, consistent entropy, and computational reversibility, particularly in the context of functions like `sqrt(x)` and `max(x,y)` and their potential to exhibit emergent cryptographic properties. The user posits that entropy across variables, including the function’s identity, should be consistent (not necessarily constant), with reversibility depending on whether sufficient entropy exists to derive unknown variables. Cryptographic functions, requiring specific variables (e.g., keys) for reversal, contrast with functions that are reversible with partial information. The report provides a comprehensive framework, formalizing the model, applying it to the user’s examples, and addressing its implications for computational entropy and emergent cryptographic behavior.

## Background: Key Concepts

### Causal Invariance
Causal invariance, within the interventionist account of causality, refers to the stability of causal relationships across different contexts or interventions ([Measuring Causal Invariance Formally](https://www.mdpi.com/1099-4300/23/6/690)). In computations, this translates to the idea that the causal relationships between inputs and outputs remain consistent regardless of the order of operations, provided the final result is the same. For example, in a commutative operation like addition (\(a + b = b + a\)), the causal link between inputs and output is invariant to order.

### Consistent Entropy
The user suggests that entropy across variables, including the function’s identity, should be consistent, meaning the total information content is preserved but can shift between components (e.g., from function identity to variables). Unlike constant entropy, which implies a fixed total, consistent entropy allows for gains or losses based on available information. In Information Theory, entropy measures uncertainty, calculated as \(H(X) = -\sum p(x_i) \log_2 p(x_i)\) for a random variable \(X\) ([Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29)).

### Reversibility and Cryptography
A function is **inherently reversible** if knowing some variables allows derivation of others, assuming the function’s identity is known. For example, `sqrt(x)` is reversible given the result \(r\), as \(x = r^2\). A function is **not inherently reversible** if, even with the function’s identity and some variables, others remain underdetermined, as in cryptographic functions requiring a key ([One-Way Function](https://en.wikipedia.org/wiki/One-Way_Function)). The user proposes that a set like \([sqrt, max]\) can be emergently cryptographic if insufficient variables are known, preventing function identification.

### Vectorial Lambda Calculus
Vectorial lambda calculus extends lambda calculus with linear-algebraic structures, encoding vectors and matrices as terms ([The vectorial λ-calculus](https://www.sciencedirect.com/science/article/abs/pii/S0890540115000497)). Functions like `sqrt(x)` or `max(x,y)` can be represented as vectors in a function space, with types distinguishing their arity (unary vs. binary). This framework supports modeling function identity and variable computability, crucial for the user’s model.

## User’s Example: `sqrt(x)` and `max(x,y)`

The user provides two functions to illustrate their model:
- **sqrt(x)**: Unary function, reversible with result \(r\): \(x = r^2\). Requires one input.
- **max(x,y)**: Binary function, not uniquely reversible, as \(r = \max(x, y)\) implies \(x \leq r\), \(y \leq r\), with one equaling \(r\). Requires two inputs.

Key observations:
- Both produce non-negative real outputs, but their input requirements differ.
- Reversibility depends on knowing the function and sufficient variables.
- If only the result is known, distinguishing between `sqrt(x)` and `max(x,y)` is impossible without knowing the number of variables, creating high uncertainty akin to cryptographic systems.

## Proposed Model

### Framework Overview
The model combines:
- **Category Theory**: Models computations as morphisms between objects (e.g., inputs to outputs), ensuring causal invariance through stable morphism compositions.
- **Information Theory**: Quantifies entropy across function identity, variables, and hidden components, ensuring consistent entropy.
- **Vectorial Lambda Calculus**: Encodes functions and variables as vectors, enabling linear-algebraic operations to model transformations and reversibility.

### Encoding in Vectorial Lambda Calculus
- **Function Space**: Define a type \(F = [U, B]\), where:
  - \(U = \text{Real} \to \text{Real}\): Unary functions (e.g., `sqrt(x)`).
  - \(B = \text{Real} \to \text{Real} \to \text{Real}\): Binary functions (e.g., `max(x,y)`).
- **Function Identity**: Represent as a vector \(\mathbf{f} = [f_U, f_B]\):
  - `sqrt(x)`: \(\mathbf{f} = [1, 0]\).
  - `max(x,y)`: \(\mathbf{f} = [0, 1]\).
- **Variables**: Inputs as vectors \(\mathbf{v}\), with dimensionality matching the function’s arity (1 for `sqrt`, 2 for `max`).
- **Computation**: A term \(f = \lambda \mathbf{f}. \lambda \mathbf{v}. (f_U \cdot f_1(\mathbf{v}_1) + f_B \cdot f_2(\mathbf{v}_1, \mathbf{v}_2))\), where \(f_1\) is `sqrt`, \(f_2\) is `max`, and \(\mathbf{v}_i\) are input components.

### Entropy Calculation
- **Function Identity Entropy (\(H_F\))**:
  - Initially, with two functions, \(H_F = -\sum_{i=1}^2 p(f_i) \log_2 p(f_i)\). If \(p(\text{sqrt}) = p(\text{max}) = 0.5\), then:
    \[
    H_F = -(0.5 \log_2 0.5 + 0.5 \log_2 0.5) = 1 \text{ bit}
    \]
  - With one input variable, infer `sqrt(x)`, so \(H_F = 0\). With two, infer `max(x,y)`, so \(H_F = 0\).
- **Variable Entropy (\(H_V\))**:
  - For `sqrt(x)`, given \(r\), \(x = r^2\), so \(H_V = 0\).
  - For `max(x,y)`, given \(r\), \(x \leq r\), \(y \leq r\), with one equaling \(r\). Assuming a uniform distribution over possible \((x, y)\), entropy is higher, e.g., \(H_V \approx \log_2 r\) for continuous inputs up to \(r\).
- **Total Entropy**: Consistent across components:
  \[
  H_{\text{total}} = H_F + H_V + H_{\text{hidden}}
  \]
  - \(H_{\text{hidden}}\): Entropy of undecayed variables (e.g., keys in cryptographic functions).
  - For \([sqrt, max]\) with only the result, \(H_F = 1\), \(H_V\) depends on the function, and \(H_{\text{hidden}} = 0\) unless secrets are involved.

### Causal Invariance
- **Category Theory**: Computations are morphisms in a category \(\mathcal{C}\), with objects as variable states and morphisms as functions. Causal invariance is ensured by stable morphisms under composition, meaning \(f \circ g = g \circ f\) for commutative operations.
- **Application**: For `sqrt(x)`, the morphism \(x \to \sqrt{x}\) is invariant because \((\sqrt{x})^2 = x\). For `max(x,y)`, the morphism \((x, y) \to \max(x, y)\) is invariant under input permutation, as \(\max(x, y) = \max(y, x)\).

### Emergent Cryptographic Properties
- **With Insufficient Variables**: If only the result \(r\) is known, \(H_F = 1\) (cannot distinguish `sqrt` from `max`)), and \(H_V\) is high (cannot compute inputs without knowing arity). This high entropy mimics cryptographic functions, where reversal is infeasible without a key.
- **With Sufficient Variables**: Knowing one input for `sqrt` or two for `max` reduces \(H_F\) and \(H_V\), making reversal possible, unlike cryptographic functions where a key is always required.

## Practical Example
- **Scenario**: Result \(r = 4\).
  - **If `sqrt(x)`**: \(x = 4^2 = 16\), fully reversible (\(H_V = 0\)).
  - **If `max(x,y)`**: \(x \leq 4\), \(y \leq 4\), one equaling 4. Entropy \(H_V > 0\) due to multiple \((x, y)\).
  - **Unknown Function**: \(H_F = 1\), as both functions are possible. Without variable count, reversal is impossible, resembling cryptographic irreversibility.
- **Inference**: With one input, test `sqrt(x)`; if it matches, \(H_F = 0\). If not, infer `max(x,y)`, but need another input, maintaining high entropy.

## Implications for Computational Entropy
- **Consistent Entropy**: The model ensures entropy is consistent by tracking \(H_F\), \(H_V\), and \(H_{\text{hidden}}\). Gains in certainty (e.g., identifying `sqrt`) reduce \(H_F\), balanced by losses elsewhere (e.g., variable uncertainty in `max`).
- **Cryptographic Functions**: Require high \(H_{\text{hidden}}\) (e.g., key entropy), ensuring irreversibility without the key, even with function identity known.
- **General Computations**: Functions like \([sqrt, max]\) show emergent cryptographic behavior when information is limited, highlighting the model’s versatility.

## Challenges and Future Work
- **Non-Linear Functions**: `sqrt(x)` and `max(x,y)` are non-linear, challenging vectorial lambda calculus’s linear framework. Extensions to handle non-linear transformations are needed.
- **Formalizing Entropy**: Quantifying \(H_V\) for continuous variables requires differential entropy, complicating calculations.
- **Emergent Cryptography**: Proving that \([sqrt, max]\) is cryptographically secure requires analyzing the entropy threshold for irreversibility.

## Table: Entropy Components for `sqrt(x)` and `max(x,y)`

| **Component**         | **sqrt(x)**                     | **max(x,y)**                    |
|-----------------------|---------------------------------|---------------------------------|
| **Function Entropy (\(H_F\))** | 0 (with 1 input)               | 0 (with 2 inputs)              |
| **Variable Entropy (\(H_V\))** | 0 (given \(r\), \(x = r^2\))   | >0 (given \(r\), \(x, y \leq r\)) |
| **Hidden Entropy (\(H_{\text{hidden}}\))** | 0 (no secrets)                | 0 (no secrets)                 |
| **Reversibility**     | Inherent (full info)           | Not inherent (needs both inputs) |

## Conclusion
The proposed model successfully integrates Category Theory, Information Theory, and Vectorial Lambda Calculus to describe causal invariance and consistent entropy in computations. It captures the emergent cryptographic properties of functions like \([sqrt, max]\) when insufficient variables are known, showing high entropy akin to cryptographic systems. By encoding function identity and variables as vectors, ensuring stable morphisms, and measuring entropy, the model provides a robust framework for analyzing computational reversibility and entropy, with applications in both theoretical and practical domains.

## Key Citations
- [Entropy (information theory) - Wikipedia](https://en.wikipedia.org/wiki/Entropy_%28information_theory%29)
- [Lambda Calculus - Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Measuring Causal Invariance Formally - MDPI](https://www.mdpi.com/1099-4300/23/6/690)
- [One-Way Function - Wikipedia](https://en.wikipedia.org/wiki/One-Way_Function)
- [The vectorial λ-calculus - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0890540115000497)