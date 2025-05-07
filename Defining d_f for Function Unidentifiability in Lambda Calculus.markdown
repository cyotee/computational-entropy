# Defining d_f for Function Unidentifiability in Lambda Calculus

This report addresses your query about defining \( d_f \) in the decay vector for the IDEM function metadata. The decay vector, used in a model combining Category Theory, Information Theory, and Vectorial Lambda Calculus, captures input recoverability and function identity recovery. You proposed \( d_f \) as a measure of function unidentifiability, with recoverability summing to 1 across all required information. This response outlines a Bayesian inference approach to compute \( d_f \), using iterative input-output pairs to update confidence in the function's identity, and provides a Python implementation.

## Understanding d_f

\( d_f \) represents the uncertainty in identifying the function's identity. It starts high (near 1) when little is known and decreases as more input-output pairs confirm the function. The total recoverability, including inputs and the function, sums to 1 when all information is available.

### Bayesian Inference Approach

1. **Hypothesis Space**: Define possible functions, e.g., \( \mathcal{F} = \{f_1, f_2, \ldots, f_m\} \).
2. **Prior Probability**: Start with uniform priors, \( P(f_i) = \frac{1}{m} \).
3. **Likelihood**: For a pair \( (x, y, z) \), \( P(z | x, y, f_i) = 1 \) if \( f_i(x, y) = z \), else 0.
4. **Posterior Update**: Update with each pair:
   \[
   P(f_i | x, y, z) = \frac{P(z | x, y, f_i) P(f_i)}{\sum_j P(z | x, y, f_j) P(f_j)}
   \]
5. **Confidence Metric**: \( P_{\text{max}} = \max_i P(f_i | \text{data}) \).
6. **Unidentifiability**: \( d_f = 1 - P_{\text{max}} \).

### Iterative Updates

Each new pair refines \( P_{\text{max}} \), reducing \( d_f \). For indistinguishable functions, \( d_f \) approaches a limit (e.g., 0.5).

## Python Implementation

The following Python code demonstrates updating \( d_f \) with input-output pairs. The source is embedded directly within this Markdown file for your convenience:

```python
def update_posterior(functions, priors, x, y, z):
    posteriors = []
    total = 0
    for f, prior in zip(functions, priors):
        likelihood = 1 if f(x, y) == z else 0
        posterior = likelihood * prior
        posteriors.append(posterior)
        total += posterior
    if total == 0:
        return priors  # No update if all fail
    return [p / total for p in posteriors]

# Define example functions
f_sum = lambda x, y: x + y
f_prod = lambda x, y: x * y
functions = [f_sum, f_prod]

# Initial uniform priors
priors = [0.5, 0.5]

# Input-output pairs
pairs = [(2, 3, 5), (1, 1, 2)]

# Iterate over pairs
for x, y, z in pairs:
    priors = update_posterior(functions, priors, x, y, z)
    p_max = max(priors)
    d_f = 1 - p_max
    print(f"Pair ({x}, {y}, {z}): P_max = {p_max:.2f}, d_f = {d_f:.2f}")
```

**Sample Output**:
- Pair (2, 3, 5): \( P_{\text{max}} = 1.00 \), \( d_f = 0.00 \)
- Pair (1, 1, 2): Continues with updated confidence.

The code defines two simple functions (`f_sum` and `f_prod`), initializes uniform priors, and updates them with input-output pairs. The `update_posterior` function computes the Bayesian posterior, and \( d_f \) is derived as \( 1 - P_{\text{max}} \).

## Conclusion

Defining \( d_f \) as \( 1 - P_{\text{max}} \) using Bayesian inference aligns with your concept of recoverability summing to 1. It captures the iterative increase in confidence and asymptotic limits for indistinguishable functions, providing a robust measure of function unidentifiability for the decay vector. This implementation can be adapted to your specific function set and data.