# Simplifying IDEM Function Metadata with Embedded Decay Vector

## Introduction
This report examines the feasibility of embedding IDEM function metadata members—Arity, Result Dimensionality, AST Depth, and AST Size—into the decay vector to simplify metadata representation while preserving computability, reliability, and utility for research in computational entropy and causal invariance. The IDEM function, rooted in a model combining Category Theory, Information Theory, and Vectorial Lambda Calculus, encapsulates a function’s behavior and metadata. The decay vector currently captures input recoverability and function identity probability. We analyze each metadata member’s embeddability, considering their definitions, relationships to the decay vector, and trade-offs, including your hypothesis about embedding Result Dimensionality via probabilities.

## Context: IDEM Function and Decay Vector
The IDEM function pairs a function’s result with metadata:
- **Arity**: Number of input variables.
- **Result Dimensionality**: Size of the output tuple.
- **AST Depth**: Maximum nesting level in the Abstract Syntax Tree (AST).
- **AST Size**: Total number of nodes in the AST.
- **Decay Vector**: Represented as \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \in \{0, 1\} \) indicates input recoverability (0 if recoverable, 1 if not), and \( d_f \in [0, 1] \) is the probability of not recovering the function’s identity.

The goal is to reduce explicit metadata by embedding these members into the decay vector, ensuring the representation remains meaningful across reducible and irreducible computations.

## Feasibility and Trade-Offs of Embedding Metadata

### Arity
- **Why It’s Embeddable**: Arity is the number of inputs, directly reflected in the length of the decay vector’s input recoverability list. For example:
  - Decay vector \( [d_1, d_2] \) implies Arity = 2.
  - Decay vector \( [d_1] \) implies Arity = 1.
  Counting the elements in \( [d_1, \ldots, d_{n(f)}] \) gives Arity without additional data.
- **Method**: No explicit embedding needed; Arity is inferred from the vector’s structure.
- **Trade-Offs**:
  - **Pros**: Simplifies metadata with no added complexity or loss of information.
  - **Cons**: None. Arity is a syntactic property, computable from the function’s definition (e.g., lambda abstractions), and reliable across all computation types.
- **Conclusion**: Arity is readily embeddable with no trade-offs, making it an ideal candidate for implicit representation.

### Result Dimensionality
- **Why It’s Challenging**: Result Dimensionality (output tuple size) doesn’t naturally align with the decay vector’s focus on input recoverability. Functions with identical decay vectors can have different output sizes:
  - \( f(x) = x \): Result Dimensionality = 1, decay vector \( ([0], d_f) \).
  - \( f(x) = (x, x) \): Result Dimensionality = 2, decay vector \( ([0], d_f) \).
  The decay vector captures how inputs are preserved, not the output structure.
- **Embedding Methods**:
  1. **Append as a Scalar**: Add Result Dimensionality as a component, e.g., \( ([d_1, \ldots, d_{n(f)}], d_f, r) \), where \( r \) is the output size.
     - **Trade-Offs**:
       - **Pros**: Simple to compute (via output type or AST traversal) and preserves the exact value.
       - **Cons**: Expands the decay vector’s purpose beyond recoverability, potentially reducing its conceptual clarity.
  2. **Your Hypothesis—Discrete Probabilities**: Assign probabilities to each result tuple member based on their contribution to input recoverability, e.g., for \( f(x, y) = (x, y) \) with Result Dimensionality = 2, use \( [p_1, p_2] \) where \( p_1 = 0 \) (x recoverable) and \( p_2 = 0 \) (y recoverable), appended as \( ([d_1, d_2], d_f, [p_1, p_2]) \).
     - **Trade-Offs**:
       - **Pros**: Ties output structure to recoverability, potentially enriching analysis.
       - **Cons**: Complicates the decay vector with variable-length sub-vectors, risks redundancy (e.g., \( d_i \) and \( p_i \) overlap), and may obscure Result Dimensionality’s exact value if probabilities don’t directly indicate size.
- **Feasibility**: Both methods are computable, but the scalar approach is clearer and less disruptive to the decay vector’s design.
- **Conclusion**: Embedding is possible but introduces trade-offs in clarity and complexity. Keeping Result Dimensionality explicit avoids confusion and preserves its distinct role.

### AST Depth and AST Size
- **Why It’s Difficult**: AST Depth (nesting level) and AST Size (node count) reflect structural complexity, not recoverability. Functions with similar decay vectors can differ significantly in AST metrics:
  - \( \lambda x. x \): Depth = 1, Size = 2, decay vector \( ([0], d_f) \).
  - \( \lambda x. (\lambda y. y) \, x \): Depth = 2, Size = 5, decay vector \( ([0], d_f) \).
  These metrics don’t directly influence \( d_i \) or \( d_f \).
- **Embedding Methods**:
  1. **Separate Components**: Append both as \( ([d_1, \ldots, d_{n(f)}], d_f, \text{depth}, \text{size}) \).
     - **Trade-Offs**:
       - **Pros**: Retains exact values, computable via parsing tools.
       - **Cons**: Bloats the decay vector, diluting its focus on recoverability.
  2. **Complexity Score**: Combine into a single value, e.g., \( c = 0.5 \cdot \text{Depth} + 0.5 \cdot \text{Size} \) (normalized or weighted), appended as \( ([d_1, \ldots, d_{n(f)}], d_f, c) \).
     - **Trade-Offs**:
       - **Pros**: Reduces dimensionality, feasible with standard AST analysis.
       - **Cons**: Obscures individual contributions of Depth and Size, reducing interpretability (e.g., is \( c = 5 \) from deep nesting or many nodes?).
- **Feasibility**: Both are computable, but the complexity score balances simplicity and loss of detail.
- **Conclusion**: Embedding is feasible but sacrifices clarity. These metrics offer unique insights into code structure, better preserved as explicit fields.

## Proposed Metadata Representation
- **Embedded**: Arity (inferred from decay vector length).
- **Explicit**:
  - Result Dimensionality
  - AST Depth
  - AST Size
- **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \).

## Example
For \( \lambda x. \lambda y. x + y \):
- **Decay Vector**: \( ([1, 1], 0.1) \) (inputs not recoverable, 10% chance function identity not recovered).
- **Arity**: 2 (inferred).
- **Result Dimensionality**: 1.
- **AST Depth**: 2.
- **AST Size**: 5.

## Conclusion
- **Arity**: Embeddable with no trade-offs due to its direct mapping to decay vector length.
- **Result Dimensionality**: Embedding (scalar or probabilities) is possible but risks clarity; better kept explicit.
- **AST Depth and Size**: Embedding as a score or separate values is feasible but obscures distinct structural insights; explicit representation is preferable.
This approach balances simplicity and utility, ensuring metadata supports your research effectively.