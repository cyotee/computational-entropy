# Transforming Probabilistic Decay Vectors in Lambda Calculus

## Introduction
The IDEM function, an extension of the identity function in lambda calculus, pairs a function’s output with metadata to analyze computational entropy and predict behavior without direct computation. The metadata includes Arity, Result Dimensionality, AST Depth, AST Size, and a Decay Vector, traditionally defined as \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \in \{0, 1\} \) indicates input recoverability, and \( d_f \in [0, 1] \) is the probability of not identifying the function. This report addresses the feasibility of performing lambda calculus operations to transform differently composed decay vectors—specifically those with probabilistic or combinatorial definitions based on result properties—into a standard form, as requested on May 08, 2025. It proposes a method to encode and manipulate decay vectors, ensuring computability and alignment with research goals.

## Background: IDEM Function and Decay Vector
The IDEM function is defined as:
\[
\text{Idem}_f = \lambda x_1. \lambda x_2. \ldots \lambda x_k. \text{pair} \, (f \, x_1 \, x_2 \, \ldots \, x_k) \, \text{info}_f
\]
where \( \text{info}_f \) includes:
- **Arity**: Number of input variables (\( k \)).
- **Result Dimensionality**: Size of the output tuple (e.g., 1 for scalar, 2 for pair).
- **AST Depth**: Maximum nesting level in the Abstract Syntax Tree (AST).
- **AST Size**: Total number of nodes in the AST.
- **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \) indicates whether input \( x_i \) is recoverable, and \( d_f \) is the probability of not identifying \( f \).

The query focuses on probabilistic IDEM expressions, where the decay vector may include probabilities (e.g., \( [0.25, 0.25] \)) or combinatorial properties (e.g., partitions, set memberships) to reflect the likelihood of identifying the function from a result set and partial inputs. The goal is to transform these “differently composed” decay vectors into a standard form, such as the binary \( d_i \) and scalar \( d_f \) format.

## Feasibility of Lambda Calculus Transformations
Lambda calculus is Turing-complete, enabling the expression of any computable function, including transformations of complex data structures like decay vectors. By encoding decay vectors as lambda terms, we can define functions to manipulate their components, converting probabilistic or combinatorial formats into a standard form. This is feasible because:
- **Data Encoding**: Lambda calculus supports encoding of lists, pairs, booleans, and numbers (e.g., Church numerals), sufficient for representing decay vectors.
- **Function Manipulation**: Lambda calculus allows defining operations to extract, transform, or normalize components, enabling conversion between formats.
- **Probabilistic Handling**: Probabilities can be approximated as rational numbers, encoded as pairs of integers, ensuring computability.

### Encoding Decay Vectors
To perform transformations, decay vectors must be represented as lambda terms:
- **Standard Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \in \{0, 1\} \) and \( d_f \in [0, 1] \).
  - **List of \( d_i \)**: Encoded as a Church-encoded list, where booleans are:
    - \( \text{true} = \lambda x. \lambda y. x \)
    - \( \text{false} = \lambda x. \lambda y. y \)
    - List: \( \text{nil} = \lambda f. \lambda x. x \), \( \text{cons} = \lambda h. \lambda t. \lambda f. \lambda x. f \, h \, (t \, f \, x) \).
    - Example: \( [0, 1] = \text{cons} \, \text{false} \, (\text{cons} \, \text{true} \, \text{nil}) \).
  - **\( d_f \)**: Approximated as a rational number (e.g., \( 0.5 = \frac{1}{2} \)), encoded as a pair:
    - Pair: \( \text{pair} = \lambda a. \lambda b. \lambda f. f \, a \, b \).
    - Example: \( 0.5 = \text{pair} \, 1 \, 2 \).
  - **Full Vector**: Encoded as a pair of the list and \( d_f \):
    - Example: \( ([0, 1], 0.5) = \text{pair} \, (\text{cons} \, \text{false} \, (\text{cons} \, \text{true} \, \text{nil})) \, (\text{pair} \, 1 \, 2) \).

- **Probabilistic Decay Vector**: \( ([p_1, \ldots, p_{n(f)}], d_f) \), where \( p_i \in [0, 1] \).
  - **List of \( p_i \)**: Each \( p_i \) is a rational number (e.g., \( 0.25 = \frac{1}{4} \)), encoded as a pair of Church numerals.
    - Example: \( [0.25, 0.25] = \text{cons} \, (\text{pair} \, 1 \, 4) \, (\text{cons} \, (\text{pair} \, 1 \, 4) \, \text{nil}) \).
  - **\( d_f \)**: As above, a rational number.
  - **Full Vector**: A pair of the list and \( d_f \).

- **Combinatorial Decay Vector**: \( ([p_1, \ldots, p_{n(f)}], d_f, \text{comb}) \), where \( \text{comb} \) includes properties like partitions, factors, or set memberships.
  - **\( \text{comb} \)**: Encoded as a tuple or list of properties:
    - Partitions: A Church numeral (e.g., 3 for 4 partitions).
    - Factors: A Church numeral (e.g., 2 for factors of 4).
    - Set Memberships: A list of booleans or symbols (e.g., \( [\text{natural}, \text{integer}] \)).
  - Example: \( ([0.25, 0.25], 0.5, [3, 2, [\text{natural}, \text{integer}]]) \) could be encoded as a nested pair structure.

### Transformation Functions
To transform a probabilistic or combinatorial decay vector into the standard form \( ([d_1, \ldots, d_{n(f)}], d_f) \), we define lambda calculus functions that:
- **Extract Components**: Use projections (\( \text{fst} \), \( \text{snd} \)) to access the list and \( d_f \).
- **Normalize Probabilities**: Convert \( p_i \) to binary \( d_i \) using a threshold (e.g., \( p_i > 0.5 \to d_i = 0 \), else \(