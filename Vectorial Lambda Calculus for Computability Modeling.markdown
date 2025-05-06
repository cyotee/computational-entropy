# Modeling Computability of Variables in Vectorial Lambda Calculus

This report explores how vectorial lambda calculus, a typed extension of lambda calculus that integrates linear-algebraic structures, can be applied to model the computability of variables when the function’s identity is potentially unknown, as exemplified by distinguishing between functions like `sqrt(x)` and `max(x,y)`. The user’s query focuses on using vectorial lambda calculus to represent the relationship between function identity, variable computability, and information decay, building on the idea that the number of input variables can help infer the function used. This approach is proposed as a way to measure computational entropy, extending beyond cryptographic applications to general computations. The report provides a detailed analysis, including theoretical foundations, practical examples, and a proposed model, drawing from recent sources and theoretical insights.

## Background: Lambda Calculus and Vectorial Extension

### Lambda Calculus Fundamentals
Lambda calculus, developed by Alonzo Church in the 1930s, is a formal system for expressing computation through function abstraction and application, serving as a foundation for functional programming ([Lambda Calculus - Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus)). It consists of:
- **Variables**: Placeholders (e.g., \(x\)).
- **Abstractions**: Function definitions, denoted \(\lambda x.M\), where \(x\) is the input and \(M\) is the body.
- **Applications**: Applying a function to an argument, written \((M N)\).

Computation proceeds via **β-reduction**, substituting arguments into functions. Lambda calculus is Turing-complete, capable of simulating any computation, but its untyped form lacks mechanisms to enforce specific properties like computational hardness, which is critical for cryptographic functions ([Lambda Calculus - Stanford]([invalid url, do not cite])).

### Vectorial Lambda Calculus
The vectorial lambda calculus extends lambda calculus by incorporating linear-algebraic structures, allowing vectors and matrices to be encoded as terms ([The vectorial λ-calculus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0890540117300482)). Key features include:
- **Vectors**: Represented as linear combinations of basis terms (e.g., \(\sum_i v_i \cdot e_i\)).
- **Matrices**: Encoded as functions transforming vectors, typed to ensure linear-algebraic properties.
- **Type System**: Supports linear combinations of types, enabling static analysis of term reductions and properties like reversibility ([The Vectorial Lambda Calculus Revisited - arXiv](https://arxiv.org/abs/2007.03648)).

This system, originally designed for quantum computing, extends System F (a typed lambda calculus with polymorphism) by allowing terms and types to be superposed, making it suitable for modeling computations with vector-based inputs or keys.

### Cryptographic Context and Entropy
The user’s earlier discussions highlighted zero-knowledge proofs, where a secret key’s entropy ensures unpredictability while the proof guarantees validity. This duality—high entropy (unpredictability) and high certainty (validity)—suggests a general model for computational entropy, applicable to non-cryptographic functions like `sqrt(x)` and `max(x,y)`. The user proposes treating the function’s identity as a variable, with its computability tied to the number of input variables and the information needed to reverse the computation.

## User’s Example: `sqrt(x)` and `max(x,y)`

The user provides two functions, `sqrt(x)` and `max(x,y)`, to illustrate their model:
- **sqrt(x)**: Takes one input \(x \geq 0\) and returns \(\sqrt{x}\). It’s reversible if the result \(r\) is known: \(x = r^2\).
- **max(x,y)**: Takes two inputs \(x, y\) and returns \(\max(x, y)\). It’s not uniquely reversible, as the result \(r\) only implies \(x \leq r\), \(y \leq r\), with one of \(x\) or \(y\) equaling \(r\).

Both functions are reversible with all inputs known, but without them, reversing requires knowing the function’s identity. The user notes:
- Knowing the function informs the number of variables (1 for `sqrt`, 2 for `max`).
- If the function is unknown but the number of variables is known, you can infer the function:
  - One variable implies `sqrt(x)`.
  - Two variables imply `max(x,y)`.
- With one variable and the result, you can test `sqrt(x)` to confirm or rule it out, inferring `max(x,y)` if it fails (though `max` requires two variables, so additional data is needed).

This model treats the function’s identity as a variable, with computability tied to inferring the function and reversing the computation.

## Applying Vectorial Lambda Calculus

Vectorial lambda calculus can model this scenario by encoding the function’s identity and variables as terms, using its type system to distinguish functions by arity and represent computability constraints.

### Encoding Function Identity
To represent the unknown function identity (`sqrt` or `max`), we can use a tagged encoding or a vector-based selection mechanism:
- **Tagged Encoding**: Represent the computation as a pair \((t, f)\), where \(t\) is a tag indicating the function (`sqrt` or `max`), and \(f\) is the function term. In lambda calculus, pairs are encoded as Church pairs: \((a, b) = \lambda g. g a b\).
  - For `sqrt`: \(p_1 = \lambda g. g \text{true} f_1\), where \(f_1 = \lambda x. \sqrt{x}\).
  - For `max`: \(p_2 = \lambda g. g \text{false} f_2\), where \(f_2 = \lambda x. \lambda y. \max(x, y)\).
  - Tags use Church booleans: \(\text{true} = \lambda a. \lambda b. a\), \(\text{false} = \lambda a. \lambda b. b\).
- **Vector Encoding**: In vectorial lambda calculus, represent the function as a vector in a type space. Define a type \(F = [U, B]\), where:
  - \(U = \text{Real} \to \text{Real}\) for unary functions like `sqrt`.
  - \(B = \text{Real} \to \text{Real} \to \text{Real}\) for binary functions like `max`.
  - A term \(f\) of type \(F\) could be \([1 \cdot f_1, 0 \cdot f_2]\) for `sqrt` or \([0 \cdot f_1, 1 \cdot f_2]\) for `max`, selecting one function via a basis vector.

### Handling Arity and Computability
The number of variables (arity) is critical for inferring the function:
- **One Variable**: Implies a unary function (`sqrt`). Apply the term to one argument and check if the result matches. If it does, it’s `sqrt`; if not, it’s likely `max`, but `max` requires two variables, so the computation fails or needs more data.
- **Two Variables**: Implies a binary function (`max`). Apply the term to two arguments to compute the result.

In vectorial lambda calculus, the type system enforces arity:
- A term of type \(U\) expects one argument.
- A term of type \(B\) expects two arguments (curried).
- A term of type \(F = [U, B]\) is a linear combination, but application requires projecting to \(U\) or \(B\), which can be guided by the number of provided arguments.

### Reversibility and Information Decay
- **sqrt(x)**: Reversible with the result \(r\): \(x = r^2\). The function’s identity is computable with one variable and result, as `sqrt` is the only unary option.
- **max(x,y)**: Not uniquely reversible, as \(r = \max(x, y)\) implies \(x \leq r\), \(y \leq r\), with one equaling \(r\). Additional data (e.g., one variable’s value) is needed to compute the other.
- **Information Decay**: The user’s model treats the function’s identity as a variable. If unknown, it contributes to entropy (uncertainty). Knowing the number of variables reduces this entropy by identifying the function, enabling variable computation or probabilistic statements (e.g., for `max`, the unknown variable is \(\leq r\)).

### Vectorial Representation
To model this in vectorial lambda calculus:
- **Function Selection**: Use a vector \(\mathbf{v} = [v_1, v_2]\) where \(v_1 = 1, v_2 = 0\) selects `sqrt`, and \(v_1 = 0, v_2 = 1\) selects `max`. The term is:
  \[
  f = \lambda \mathbf{v}. \lambda \mathbf{a}. (v_1 \cdot f_1(\mathbf{a}_1) + v_2 \cdot f_2(\mathbf{a}_1, \mathbf{a}_2))
  \]
  where \(\mathbf{a}\) is a vector of arguments, \(\mathbf{a}_1\) is the first argument, and \(\mathbf{a}_2\) is the second (if needed).
- **Type System**: Define \(F = [U, B]\), ensuring \(f_1 : U\), \(f_2 : B\). The type system checks that \(\mathbf{v}\) selects a valid function and that \(\mathbf{a}\) provides enough arguments.
- **Computability**: If only one argument is provided, \(\mathbf{v} = [1, 0]\) (selecting `sqrt`) is inferred, as \(f_2\) requires two arguments. The result \(r\) allows computing \(x = r^2\). With two arguments, \(\mathbf{v} = [0, 1]\) is possible, and \(r\) constrains \(x, y \leq r\).

### Computational Entropy
The user’s model aligns with computational entropy:
- **Function Identity Entropy**: Initially high if the function is unknown (\(E = 2\) for `sqrt` or `max`)). Knowing the number of variables reduces \(E\) to 1.
- **Variable Computability Entropy**: For `sqrt`, low entropy as \(x\) is computable. For `max`, higher entropy due to ambiguity in \(x, y\).
- **Vector Role**: The vector \(\mathbf{v}\) encodes function identity, with its entropy tied to the number of possible functions. The result’s information content determines variable computability.

## Challenges and Limitations
- **Non-Linear Functions**: `sqrt(x)` and `max(x,y)` are non-linear, while vectorial lambda calculus is optimized for linear transformations. Encoding non-linear functions requires approximations or extensions beyond standard vectorial lambda calculus ([The vectorial λ-calculus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0890540117300482)).
- **Type System Complexity**: Managing types like \(F = [U, B]\) with different arities is non-trivial, requiring careful design to handle argument application.
- **Information Decay**: Quantifying decay as computability loss needs a formal entropy model, possibly integrating Shannon entropy for function and variable distributions.

## Table: Function Properties and Computability

| **Function** | **Arity** | **Reversibility** | **Entropy (Function Identity)** | **Entropy (Variables)** |
|--------------|-----------|-------------------|---------------------------------|-------------------------|
| `sqrt(x)`    | 1         | Reversible (\(x = r^2\)) | Low (inferred with 1 variable) | Low (unique \(x\))      |
| `max(x,y)`   | 2         | Not uniquely reversible | Low (inferred with 2 variables) | High (ambiguous \(x, y\)) |

## Conclusion
Vectorial lambda calculus can model the computability of variables when the function’s identity is unknown by encoding functions as vectors or typed terms, using the type system to distinguish arities. For `sqrt(x)` and `max(x,y)`, the number of variables infers the function, enabling variable computation or probabilistic statements. This approach supports a computational entropy model, quantifying information decay and function identity uncertainty, applicable beyond cryptography. While non-linear functions pose challenges, the framework’s flexibility makes it a promising tool for such analyses.

## Key Citations
- [Lambda Calculus - Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus)
- [The vectorial λ-calculus - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0890540117300482)
- [The Vectorial Lambda Calculus Revisited - arXiv](https://arxiv.org/abs/2007.03648)
- [Lambda Calculus and Intuitionistic Linear Logic](https://link.springer.com/article/10.1023/A:1005092630115)