# Simplifying IDEM Metadata in Lambda Calculus

## Introduction
The IDEM function metadata, used in a model blending Category Theory, Information Theory, and Vectorial Lambda Calculus, includes Arity, Result Dimensionality, AST Depth, AST Size, and a decay vector. This document explores simplifying it by embedding these members into the decay vector, reducing explicit fields while ensuring the metadata remains computable and useful for studying computational entropy and causal invariance.

## Current Metadata
- **Arity**: Number of input variables.
- **Result Dimensionality**: Size of the output tuple.
- **AST Depth**: Maximum depth of the Abstract Syntax Tree.
- **AST Size**: Number of nodes in the AST.
- **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \) is input recoverability (0 or 1) and \( d_f \) is function recovery probability (0 to 1).

## Simplification Proposal
### Embedding Arity
- **Why It Works**: Arity is the number of inputs, which equals the length of \( [d_1, \ldots, d_{n(f)}] \). For example, \( ([d_1, d_2], d_f) \) means Arity = 2.
- **Result**: No need for a separate Arity field; it’s inferred from the decay vector.

### Other Members
- **Result Dimensionality**: 
  - **Issue**: It’s about output size, not input recoverability. Example: \( f(x) = x \) (size 1) and \( f(x) = (x, x) \) (size 2) share the same decay vector \( ([0], d_f) \).
  - **Decision**: Keep it explicit.
- **AST Depth and Size**: 
  - **Issue**: These measure structural complexity, unrelated to recoverability. Example: \( \lambda x. x \) (Depth 1, Size 2) vs. \( \lambda x. (\lambda y. y) \, x \) (Depth 2, Size 5) with identical decay vectors.
  - **Decision**: Keep them explicit.

## Updated Metadata
- **Inferred**: Arity (from decay vector length).
- **Explicit**: 
  - Result Dimensionality
  - AST Depth
  - AST Size
  - Decay Vector \( ([d_1, \ldots, d_{n(f)}], d_f) \)

## Example
For \( \lambda x. \lambda y. x \):
- Decay Vector: \( ([0, 1], 0.5) \)
- Arity: 2 (inferred from \( [0, 1] \))
- Result Dimensionality: 1
- AST Depth: 2
- AST Size: 4

## Conclusion
Embedding Arity into the decay vector simplifies the metadata without loss of information, as it’s directly inferable. Result Dimensionality, AST Depth, and AST Size should stay explicit, as they provide unique insights the decay vector doesn’t cover. This approach keeps the metadata lean yet effective for your research.