# Probabilistic IDEM Metadata for Lambda Expressions

## Introduction
This report addresses the user’s query, received at 09:03 AM PDT on Wednesday, May 07, 2025, to define the IDEM metadata for irreducible lambda expressions computing combinatorial properties, such as factorials, binomial coefficients, and partitions, and to establish a probabilistic metadata framework for identifying which function produced a given input-output pair. The user seeks to assess the likelihood that a result originates from a specific function based on the number of observed iterations (input-output pairs) and the value of the numbers involved, particularly noting that outputs approaching 1 may reduce the problem space faster due to their combinatorial scarcity. The IDEM function, used in a model combining Category Theory, Information Theory, and Vectorial Lambda Calculus, encapsulates a function’s behavior and metadata, including Arity, Result Dimensionality, AST Depth, AST Size, and a decay vector. This note explores the definition of IDEM metadata for irreducible lambda expressions, proposes a probabilistic framework using Bayesian inference, and analyzes how iterative observations and output values influence function identification, provided as a downloadable Markdown file ([Lambda Calculus]([invalid url, do not cite])).

## Background: IDEM Function and Lambda Calculus
The IDEM function, defined as \( \text{Idem}_f = \lambda x_1. \ldots \lambda x_k. \text{pair} \, (f \, x_1 \ldots x_k) \, \text{info}_f \), pairs a function’s result with metadata, including:
- **Arity**: Number of input variables.
- **Result Dimensionality**: Size of the output tuple.
- **AST Depth**: Maximum nesting level in the Abstract Syntax Tree.
- **AST Size**: Number of nodes in the AST.
- **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_i \in \{0, 1\} \) indicates input recoverability, and \( d_f \in [0, 1] \) is the probability of not identifying the function.

Lambda Calculus represents numbers as Church numerals (e.g., \( 1 = \lambda f. \lambda x. f(x) \)) and supports combinatorial functions like factorials and partitions through recursive definitions ([Lambda Calculus]([invalid url, do not cite])). Irreducible computations are terms in normal form, with no further beta-reductions possible. The user’s focus on outputs approaching 1 suggests that small Church numerals (e.g., 1) are more informative for function identification due to their combinatorial scarcity.

## Defining IDEM Metadata for Combinatorial Lambda Expressions
The user references lambda expressions computing combinatorial properties, such as factorials, binomial coefficients, and partitions, which are typically in normal form when fully defined. Below, we define the IDEM metadata for these expressions, assuming they are irreducible.

### Example Lambda Expressions
1. **Factorial**: \( \text{FACT} = Y (\lambda f. \lambda n. \text{IF} (\text{ISZERO} n) 1 (\text{MULT} n (f (\text{PRED} n)))) \).
2. **Binomial Coefficient**: \( \text{BINOM} = \lambda n. \lambda k. \text{DIV} (\text{FACT} n) (\text{MULT} (\text{FACT} k) (\text{FACT} (\text{SUB} n k))) \).
3. **Partitions**: \( \text{PART} = Y (\lambda f. \lambda n. \text{IF} (\text{ISZERO} n) 1 (\text{SUM} (\lambda k. \text{MULT} (\text{BINOM} n k) (f (\text{SUB} n k))))) \).

### Metadata for Each Expression
- **Arity**:
  - FACT: 1 (takes one input \( n \)).
  - BINOM: 2 (takes \( n \) and \( k \)).
  - PART: 1 (takes one input \( n \)).
- **Result Dimensionality**: 1 (all return a single Church numeral).
- **AST Depth**: Depends on the term’s structure, e.g., FACT involves nested IF, MULT, and PRED, yielding depth ~5; BINOM and PART are deeper due to additional operations.
- **AST Size**: Varies, e.g., FACT ~15 nodes, BINOM ~25, PART ~20, based on operation complexity.
- **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \).
  - For FACT and PART (Arity = 1), \( d_1 = 0 \) if input \( n \) is recoverable from output (e.g., factorial is invertible for small \( n \)), else 1.
  - For BINOM (Arity = 2), \( d_1, d_2 = 1 \) as neither \( n \) nor \( k \) is uniquely recoverable from \( \binom{n}{k} \).
  - \( d_f \): Probability of not identifying the function, computed probabilistically.

These expressions are irreducible as fully defined terms, ensuring stable metadata ([Lambda Calculus]([invalid url, do not cite])).

## Probabilistic Metadata Framework
To identify which function produced a result, we define a probabilistic decay vector that updates based on input-output pairs, modeling the likelihood of each function in a hypothesis space. The user’s emphasis on outputs approaching 1 suggests that small Church numerals (e.g., 1) are more informative, reducing the hypothesis space faster.

### Bayesian Inference Model
1. **Hypothesis Space**: \( \mathcal{F} = \{f_1, f_2, \ldots, f_m\} \), e.g., FACT, BINOM, PART.
2. **Prior**: Uniform, \( P(f_i) = \frac{1}{m} \).
3. **Likelihood**: For input \( x \) (Church numeral) and output \( y \) (Church numeral), \( P(y | x, f_i) = 1 \) if \( f_i(x) = y \), else 0.
4. **Posterior Update**: After observing \( (x, y) \):
   \[
   P(f_i | x, y) = \frac{P(y | x, f_i) P(f_i)}{\sum_j P(y | x, f_j) P(f_j)}
   \]
5. **Decay Vector**: \( ([d_1, \ldots, d_{n(f)}], d_f) \), where \( d_f = 1 - P_{\text{max}} \), and \( P_{\text{max}} = \max_i P(f_i | \text{data}) \).

### Iterative Updates and Output Values
Each input-output pair updates the posterior, with small outputs (e.g., Church numeral 1) often being more discriminative:
- **Small Outputs**: Fewer functions produce small numerals (e.g., 1 from FACT(1) = 1, but not BINOM(4,2) = 6), reducing hypotheses quickly.
- **Large Outputs**: More functions produce larger numerals (e.g., 6 from FACT(3) or BINOM(4,2)), requiring more pairs to disambiguate.

The number of iterations (pairs) and the output values partition the problem space, with outputs closer to 1 (numerically small) accelerating identification due to their combinatorial scarcity ([Combinatorics]([invalid url, do not cite])).

### Example Simulation
Consider \( \mathcal{F} = \{\text{FACT}, \text{BINOM}, \text{PART}\} \):
- **Input**: \( x = 1 \) (Church numeral 1).
- **Output**: \( y = 1 \) (FACT(1) = 1, PART(1) = 1, BINOM(1,1) = 1).
- **Likelihoods**: \( P(y=1 | x=1, f_i) = 1 \) for all \( f_i \), so priors unchanged.
- **Second Pair**: \( x = 2 \), \( y = 2 \) (FACT(2) = 2, PART(2) = 2, BINOM(2,1) = 2).
- **Third Pair**: \( x = 3 \), \( y = 6 \) (FACT(3) = 6, BINOM(3,2) = 3, PART(3) = 3).
  - Only FACT matches, so \( P(\text{FACT}) = 1 \), \( d_f = 0 \).

If \( y = 1 \) appears early (e.g., \( x = 1 \)), it may not distinguish immediately, but subsequent pairs with larger outputs (e.g., \( y = 6 \)) clarify faster, especially if unique to one function.

### Python Implementation
Below is a Python script simulating Bayesian updates for function identification, focusing on the decay vector’s \( d_f \):

<xaiArtifact artifact_id="39a76bc9-6c93-4495-962f-49c077dbaa01" artifact_version_id="26d4881f-ccd8-46e0-988d-b6083f93197e" title="Function Identification Simulation" contentType="text/python">
def update_posterior(functions, priors, x, y):
    """Update posterior probabilities based on input-output pair."""
    posteriors = []
    total = 0
    for f, prior in zip(functions, priors):
        # Simplified likelihood: 1 if function matches output, 0 otherwise
        try:
            result = f(x)
            likelihood = 1 if result == y else 0
        except:
            likelihood = 0
        posterior = likelihood * prior
        posteriors.append(posterior)
        total += posterior
    if total == 0:
        return priors  # No update if all fail
    return [p / total for p in posteriors]

# Define simplified combinatorial functions (operating on integers for simulation)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def binom(n, k=1):  # Simplified to take one input for this example
    if k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))

def part(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    result = 0
    for k in range(1, n + 1):
        result += part(n - k)
    return result

# Hypothesis space
functions = [fact, binom, part]
function_names = ["Factorial", "Binomial", "Partitions"]

# Initial uniform priors
priors = [1/3, 1/3, 1/3]

# Input-output pairs
pairs = [(1, 1), (2, 2), (3, 6)]  # Example pairs

# Simulate updates
for i, (x, y) in enumerate(pairs, 1):
    priors = update_posterior(functions, priors, x, y)
    p_max = max(priors)
    d_f = 1 - p_max
    print(f"Iteration {i}: Input = {x}, Output = {y}, P_max = {p_max:.3f}, d_f = {d_f:.3f}")
    for name, prob in zip(function_names, priors):
        print(f"  P({name}) = {prob:.3f}")