# Information Density of Small Numbers in Function Identification

Your query suggests that smaller numbers like 1 might be "information dense" because there are fewer ways to compute them, while larger numbers have more possible combinations across various functions. This makes identifying functions, such as the successor function (SUCC), easier with small outputs like 1. Below, I’ll explain why this intuition holds, focusing on combinatorial routes and function identification, including in the context of Church numerals.

## Why 1 Is Information Dense

### Fewer Combinatorial Routes
Small numbers, especially 1, have limited ways to be produced by common operations:
- **Addition**: Only (0, 1) or (1, 0) sums to 1 with non-negative integers. If restricted to positive integers, it’s even more constrained.
- **Multiplication**: Only (1, 1) yields 1.
- **Other Functions**: Exponential functions (e.g., \(1^1\)), successor (SUCC: \(0 + 1\)), or identity-like operations also point to 1, but the options remain scarce.

In contrast, larger numbers have more possibilities:
- **For 5**:
  - **Addition**: (1, 4), (2, 3), (0, 5), etc.
  - **Multiplication**: (1, 5), (5, 1).
  - **Other Functions**: Exponentiation (e.g., \(5^1\)), factorials, or combinations increase the candidates.

The fewer routes to 1 mean that observing it as an output strongly narrows down the possible functions, making it highly informative.

### Function Identification
When identifying a function based on input-output pairs:
- **Small Output (e.g., 1)**: If you input 0 and get 1, the successor function (SUCC: \(n \to n+1\)) is an obvious candidate. Few other functions in a typical hypothesis set (e.g., basic arithmetic) produce 1 from 0.
- **Larger Output (e.g., 5)**: From input 4, 5 could come from SUCC, but also from \(n + 1\), \(n \times 1.25\), or other operations, requiring more data to disambiguate.

Thus, 1’s rarity across function outputs makes it a powerful clue, aligning with your idea of "information density."

## Church Numerals Context
In lambda calculus with Church numerals:
- **Numeral 1**: \( \lambda f. \lambda x. f(x) \) (applies \(f\) once).
- **Successor (SUCC)**: Takes a numeral \(n\) and returns \(n+1\). For \(0 = \lambda f. \lambda x. x\), SUCC yields 1 with one application step.
- **Beta-Reduction**: Applying SUCC to 0 and reducing it shows a single step, quickly confirming 1. Larger numerals (e.g., 2, 3) require more steps, adding complexity.

Seeing 1 as a result, especially with a minimal reduction, strongly suggests SUCC, as few other functions in this system produce such a tight "delta of 1" from the input.

## General Principle
- **Small Outputs**: Fewer functions map inputs to 1, reducing ambiguity and speeding up identification.
- **Large Outputs**: More functions (sums, products, etc.) can produce them, diluting the information per observation.

Your hypothesis is spot-on: 1’s information density stems from its combinatorial scarcity, making it a fast identifier of functions like SUCC, especially in constrained systems like Church numerals.