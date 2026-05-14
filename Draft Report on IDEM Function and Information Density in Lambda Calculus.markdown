# Draft Report on IDEM Function and Information Density in Lambda Calculus

## Abstract
This draft report consolidates our research on the IDEM function, an extension of the identity function that pairs a function’s output with metadata capturing its structural and behavioral properties. This metadata—comprising Arity, Result Dimensionality, AST Depth, AST Size, and a Decay Vector—enables us to analyze computational entropy and predict function behavior without direct computation. We define the IDEM function, detail methods for deriving its metadata from lambda expressions, and demonstrate how the information density of values, rooted in their combinatorial properties, reveals a function’s predictability. Examples include irreducible functions (e.g., factorial), card counting in blackjack (drawing and playing scenarios), and encryption functions. This comprehensive first draft is intended for team review and feedback.

## 1. Introduction
The IDEM function enhances the traditional identity function by encapsulating both a function’s result and metadata that describes its properties. Formally, it is defined as:
\[
\text{Idem}_f = \lambda x_1. \lambda x_2. \ldots \lambda x_k. \text{pair} \, (f \, x_1 \, x_2 \, \ldots \, x_k) \, \text{info}_f
\]
where \( \text{info}_f \) includes:
- **Arity**: Number of input variables.
- **Result Dimensionality**: Size of the output tuple.
- **AST Depth**: Maximum nesting level in the Abstract Syntax Tree (AST).
- **AST Size**: Total number of nodes in the AST.
- **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \in \{0, 1\} \) indicates input recoverability, and \( d_f \in [0, 1] \) is the probability of not identifying the function.

This framework allows us to assess a function’s predictability by examining the information density of its outputs, derived from their combinatorial uniqueness. The report is organized as follows:
- **Section 2**: Defining the IDEM function.
- **Section 3**: Deriving metadata from lambda expressions.
- **Section 4**: Information density and predictability.
- **Section 5**: Examples across irreducible functions, blackjack, and encryption.
- **Section 6**: Conclusion and future work.

## 2. Defining the IDEM Function

The IDEM function extends the identity function \( \lambda x. x \) by pairing the result of a function \( f \) with metadata \( \text{info}_f \). This metadata quantifies structural and behavioral traits, enabling analysis without executing the function. For a function \( f \) with \( k \) inputs, the IDEM form is:
\[
\text{Idem}_f \, x_1 \, x_2 \, \ldots \, x_k = (f \, x_1 \, x_2 \, \ldots \, x_k, \text{info}_f)
\]
The metadata components are:
- **Arity**: The number of arguments \( k \).
- **Result Dimensionality**: The size or structure of the output (e.g., scalar, tuple).
- **AST Depth**: The deepest nesting level in the function’s AST.
- **AST Size**: The total node count in the AST.
- **Decay Vector**: A tuple capturing input recoverability (\( d_i \)) and function identifiability (\( d_f \)).

This definition roots our ability to predict behavior in the combinatorial properties encoded in \( \text{info}_f \).

## 3. Deriving Metadata from Lambda Expressions

### 3.1 Methodology
Metadata is extracted from a lambda expression’s structure and semantics:
- **Arity**: Count the outer \( \lambda \)-abstractions. For \( \lambda x. \lambda y. x \), arity is 2.
- **Result Dimensionality**: Analyze the output type or structure post-reduction.
- **AST Depth**: Compute the longest path in the AST from root to leaf.
- **AST Size**: Sum all nodes (variables, abstractions, applications) in the AST.
- **Decay Vector**:
  - \( d_i = 0 \) if input \( x_i \) is recoverable from the output; \( 1 \) otherwise.
  - \( d_f \) is estimated via Bayesian inference or static analysis, reflecting identifiability.

### 3.2 Process
1. Parse the lambda expression into an AST.
2. Traverse the AST to compute depth and size.
3. Analyze the reduction behavior to assess recoverability and output structure.
4. Synthesize the metadata into \( \text{info}_f \).

This process is systematic and applicable to any lambda term.

## 4. Information Density and Predictability

### 4.1 Information Density
Information density quantifies how unique or informative a value is, based on its combinatorial representations:
- **High Density**: Values with few representations (e.g., primes, unique factorials) are less predictable and carry more information.
- **Low Density**: Values with many representations (e.g., 2 as a natural, integer, or rational) are more predictable due to ambiguity.

We use Shannon entropy, \( I = -\log(p) \), where \( p \) is the probability of a specific representation, to measure this density.

### 4.2 Predictability Hypothesis
A function’s predictability correlates with the information density of its outputs. High-density outputs (unique, rare) suggest low predictability without computation, while low-density outputs (common, ambiguous) allow behavior inference from patterns.

### 4.3 Using IDEM
The IDEM metadata, particularly the Decay Vector and output structure, reflects this density. By analyzing \( \text{info}_f \), we predict behavior without computing \( f \).

## 5. Examples

### 5.1 Irreducible Function: Factorial
Consider the factorial function in lambda calculus:
\[
\text{FACT} = Y (\lambda f. \lambda n. \text{IF} (\text{ISZERO} n) 1 (\text{MULT} n (f (\text{PRED} n))))
\]
- **Metadata**:
  - Arity: 1
  - Result Dimensionality: 1 (scalar)
  - AST Depth: ~5
  - AST Size: ~15
  - Decay Vector: \( ([0], 0) \) for small \( n \) (invertible, identifiable)
- **Output Examples**: \( 1, 2, 6, 24 \)
- **Analysis**: Outputs are unique (high density). The Decay Vector \( [0] \) indicates recoverability (e.g., \( 6 \to 3! \)), and \( d_f = 0 \) confirms identifiability. Predictability is low without computation due to output uniqueness.

### 5.2 Card Counting in Blackjack: Drawing Cards
In blackjack, drawing cards affects deck composition. Model a counter as:
\[
\text{COUNT} = \lambda \text{card}. \text{UPDATE} \, \text{count} \, (\text{VALUE} \, \text{card})
\]
- **Metadata**:
  - Arity: 1
  - Result Dimensionality: 1 (running count)
  - AST Depth: ~3
  - AST Size: ~10
  - Decay Vector: \( ([1], 0.5) \) (card not recoverable, count partially identifiable)
- **Output Examples**: Hi-Lo counts (e.g., +1 for 2-6, -1 for 10-A)
- **Analysis**: Counts have moderate density (many sequences yield the same count). The Decay Vector \( [1] \) shows card loss, but patterns (low density) allow betting strategy predictions without recomputing deck state.

### 5.3 Card Counting in Blackjack: Playing Scenarios
For a play decision (hit/stand):
\[
\text{DECIDE} = \lambda \text{hand}. \lambda \text{dealer}. \text{IF} (\text{COUNT} > 0) \, \text{HIT} \, \text{STAND}
\]
- **Metadata**:
  - Arity: 2
  - Result Dimensionality: 1 (decision)
  - AST Depth: ~4
  - AST Size: ~12
  - Decay Vector: \( ([1, 1], 0.3) \) (inputs obscured, decision identifiable)
- **Output Examples**: “hit” or “stand”
- **Analysis**: Binary outputs have low density (highly predictable from count trends). The Decay Vector suggests input loss, but \( d_f = 0.3 \) indicates recognizable patterns, enabling strategy prediction.

### 5.4 Encryption Function
For a simple encryption \( f(\text{key}, \text{plaintext}) = \text{ciphertext} \):
\[
\text{ENCRYPT} = \lambda k. \lambda p. \text{XOR} \, k \, p
\]
- **Metadata**:
  - Arity: 2
  - Result Dimensionality: 1
  - AST Depth: ~3
  - AST Size: ~8
  - Decay Vector: \( ([1, 1], 1) \) (neither input recoverable, function obscured)
- **Output Examples**: Random-like ciphertexts
- **Analysis**: Ciphertexts have high density (unique per input pair). The Decay Vector \( [1, 1], 1 \) reflects total unpredictability without keys, aligning with encryption goals. Behavior is unpredictable without computation.

## 6. Conclusion and Future Work
The IDEM function, with its metadata, offers a powerful lens for analyzing function behavior through information density and combinatorics. From factorials to blackjack and encryption, we predict predictability without direct computation. Future work will refine metadata derivation and expand applications to complex systems.

## References
- [Lambda Calculus - Wikipedia](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Combinatorics - Wikipedia](https://en.wikipedia.org/wiki/Combinatorics)
- [Bayesian Inference - Wikipedia](https://en.wikipedia.org/wiki/Bayesian_inference)
- [Abstract Syntax Tree - Wikipedia](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- [Church Encoding - Wikipedia](https://en.wikipedia.org/wiki/Church_encoding)