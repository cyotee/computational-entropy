# Shannon Entropy in Games 63 and Submarine: Iterative Uncertainty Reduction

## Introduction

Shannon Entropy, a cornerstone of information theory introduced by Claude Shannon in his seminal 1948 paper, quantifies the uncertainty or information content of a random variable, measured in bits as \( H(X) = -\sum_i P(x_i) \log_2 P(x_i) \), where \( P(x_i) \) is the probability of outcome \( x_i \) ([Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))). In games and decision-making processes, entropy measures the uncertainty about an unknown state, and iterative actions (e.g., queries or guesses) reduce this uncertainty by providing information. The user requests an expansion of the Weighing Problem analysis to include the Shannon Entropy examples of the games "63" and "Submarine," interpreted as scenarios where iterative computations reduce uncertainty, modeled in Lambda Calculus to align with prior discussions on computational entropy.

The games "63" and "Submarine" are not explicitly documented as standard Shannon Entropy examples in the provided sources, but they can be reasonably interpreted based on context. "63" likely refers to a guessing game with 63 possible outcomes, where iterative yes/no questions identify the correct outcome, similar to Twenty Questions or the Weighing Problem. "Submarine" resembles a search game, akin to Battleship, where a hidden object (e.g., a submarine) is located in a grid through queries that narrow down possible locations ([Battleship (game)](https://en.wikipedia.org/wiki/Battleship_%28game%29)). This document models these games in Lambda Calculus, calculates their Shannon Entropy at each iterative step, and relates the process to information gain, providing a rigorous analysis for readers with backgrounds in information theory, computational theory, and thermodynamics, formatted in KaTeX-compatible LaTeX for Markdown rendering in VS Code’s Markdown+Math extension.

## Modeling Games with Lambda Calculus

### Game 63: Guessing Among 63 Possibilities
The "63" game is interpreted as a guessing game where one item must be identified among 63 equally likely possibilities (e.g., a number from 1 to 63). The initial entropy, assuming uniform probability, is:

\[ H(X) = \log_2 63 \approx 5.977 \, \text{bits} \]

Each yes/no question ideally halves the possibilities, providing 1 bit of information and reducing entropy by approximately 1 bit. After \( k \) questions, the number of remaining possibilities is \( \lceil 63 / 2^k \rceil \), and entropy is:

\[ H_k = \log_2 \lceil 63 / 2^k \rceil \]

After 6 questions, \( \lceil 63 / 2^6 \rceil = \lceil 63 / 64 \rceil = 1 \), reducing entropy to \( \log_2 1 = 0 \), identifying the item.

In Lambda Calculus, model the state as a list of 63 possibilities, with each question as a function application that filters the list. Define:

\[ M = \lambda \text{state}.\lambda \text{query}.\text{filter}(\text{state}, \text{query}) \]

- **Initial State**: \(\text{state}_0 = \text{list of } \{1, 2, \ldots, 63\}\).
- **Query**: \(\text{query}_1 = \lambda s.\text{partition}(s, s \leq 31)\), splitting into \( \{1, \ldots, 31\} \) (31 items) or \( \{32, \ldots, 63\} \) (32 items).
- **Entropy**: \( H(\text{state}_0) = \log_2 63 \approx 5.977 \), \( H(\text{state}_1) = \log_2 32 = 5 \) or \( \log_2 31 \approx 4.954 \).

Each reduction step filters the state, reducing entropy until a single item remains.

### Submarine: Search in a Grid
The "Submarine" game is interpreted as a search game similar to Battleship, where a submarine is hidden in one cell of a 10x10 grid (100 cells). Initial entropy is:

\[ H(X) = \log_2 100 \approx 6.644 \, \text{bits} \]

Queries divide the grid, e.g., asking if the submarine is in the left half (50 cells). Each yes/no query provides up to 1 bit, reducing entropy to:

\[ H_k = \log_2 \lceil 100 / 2^k \rceil \]

After 7 queries, \( \lceil 100 / 2^7 \rceil = 1 \), entropy is 0. In Lambda Calculus:

\[ M = \lambda \text{state}.\lambda \text{query}.\text{filter}(\text{state}, \text{query}) \]

- **Initial State**: \(\text{state}_0 = \text{list of } \{(1,1), \ldots, (10,10)\}\).
- **Query**: \(\text{query}_1 = \lambda s.\text{partition}(s, \text{column} \leq 5)\), splitting into left (50 cells) or right half.
- **Entropy**: \( H(\text{state}_0) = \log_2 100 \approx 6.644 \), \( H(\text{state}_1) = \log_2 50 \approx 5.644 \).

### Information Gain
Each query’s information gain is:

\[ I = H_{\text{before}} - H_{\text{after}} \]

For "63," a query reducing from 63 to 32 possibilities yields \( I \approx \log_2 63 - \log_2 32 \approx 0.977 \) bits. For "Submarine," from 100 to 50, \( I \approx 1 \) bit. Optimal strategies maximize \( I \), minimizing steps to zero entropy.

## Computational Entropy and Shannon Entropy

In both games, iterative computations (queries) reduce entropy by partitioning the state space, directly relating to Shannon Entropy’s measure of uncertainty reduction. Lambda Calculus models these as function applications, with entropy calculated as the logarithm of remaining possibilities or via probability distributions over reduction paths, providing a formal computational framework.

---

# Shannon Entropy in Games 63 and Submarine: A Comprehensive Analysis

## Introduction

Shannon Entropy, introduced by Claude Shannon in his 1948 paper "A Mathematical Theory of Communication," quantifies the uncertainty or information content of a random variable, defined as \( H(X) = -\sum_i P(x_i) \log_2 P(x_i) \), where \( P(x_i) \) is the probability of outcome \( x_i \) ([Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))). In games and decision-making scenarios, entropy measures the uncertainty about an unknown state, and iterative actions, such as queries or guesses, reduce this uncertainty by providing information. The Weighing Problem, a classic example, involves identifying a defective item among a set using a balance scale, with each weighing reducing entropy through information gain ([Balance puzzle](https://en.wikipedia.org/wiki/Balance_puzzle)). The user requests an expansion of this analysis to include the Shannon Entropy examples of the games "63" and "Submarine," interpreted as scenarios where iterative computations reduce uncertainty, modeled in Lambda Calculus to align with prior discussions on computational entropy.

The games "63" and "Submarine" are not explicitly documented as standard Shannon Entropy examples in the provided sources, but they can be reasonably interpreted based on context. "63" is likely a guessing game with 63 possible outcomes, where iterative yes/no questions identify the correct outcome, similar to Twenty Questions or the Weighing Problem. "Submarine" resembles a search game, akin to Battleship, where a hidden object (e.g., a submarine) is located in a grid through queries that narrow down possible locations ([Battleship (game)](https://en.wikipedia.org/wiki/Battleship_%28game%29)). This document models these games in Lambda Calculus, calculates their Shannon Entropy at each iterative step, and relates the process to information gain, providing a rigorous analysis for readers with backgrounds in information theory, computational theory, and thermodynamics, formatted in KaTeX-compatible LaTeX for Markdown rendering in VS Code’s Markdown+Math extension.

## Shannon Entropy in Games

Shannon Entropy measures the average uncertainty in a random variable’s outcomes. For a discrete set of \( n \) equally likely outcomes, entropy is:

\[ H(X) = \log_2 n \]

In games, each iterative action (e.g., a question or query) partitions the outcome space, reducing entropy by the information gained, defined as:

\[ I = H_{\text{before}} - H_{\text{after}} \]

where \( H_{\text{after}} = \sum_i P_i \log_2 |S_i| \), with \( P_i \) as the probability of outcome \( i \) and \( |S_i| \) as the size of the resulting subset. Optimal strategies maximize \( I \), minimizing the steps to reach zero entropy (certainty).

### Game 63: Guessing Among 63 Possibilities

The "63" game is interpreted as a guessing game where one item must be identified among 63 equally likely possibilities (e.g., a number from 1 to 63). The initial entropy is:

\[ H(X) = \log_2 63 \approx 5.977 \, \text{bits} \]

Each yes/no question ideally halves the possibilities, providing approximately 1 bit of information. After \( k \) questions, the number of remaining possibilities is \( \lceil 63 / 2^k \rceil \), and entropy is:

\[ H_k = \log_2 \lceil 63 / 2^k \rceil \]

For example:
- After 1 question (e.g., “Is it ≤ 31?”), possibilities reduce to 31 or 32: \( H_1 \approx \log_2 32 = 5 \) or \( \log_2 31 \approx 4.954 \, \text{bits} \).
- After 6 questions, \( \lceil 63 / 2^6 \rceil = 1 \), so \( H_6 = 0 \).

The information gained per question is:

\[ I = H_{k-1} - H_k \]

For the first question, \( I \approx 5.977 - 5 \approx 0.977 \, \text{bits} \) (if 32 possibilities remain).

In Lambda Calculus, model the state as a list of 63 possibilities, with each question as a function application:

\[ M = \lambda \text{state}.\lambda \text{query}.\text{filter}(\text{state}, \text{query}) \]

- **Initial State**: \(\text{state}_0 = \text{list of } \{1, 2, \ldots, 63\}\).
- **Query**: \(\text{query}_1 = \lambda s.\text{partition}(s, s \leq 31)\), yielding \(\text{state}_1\) with 31 or 32 items.
- **Entropy**: \( H(\text{state}_0) = \log_2 63 \approx 5.977 \), \( H(\text{state}_1) \approx 5 \).

Each reduction filters the state, reducing entropy until one item remains. If reversing to retrieve the input without queries triggers an infinite reduction path (e.g., via \(\lambda x.\Omega\)), the input’s entropy is preserved, as in prior discussions.

### Submarine: Search in a Grid

The "Submarine" game is interpreted as a search game similar to Battleship, where a submarine is hidden in one cell of a 10x10 grid (100 cells). Initial entropy is:

\[ H(X) = \log_2 100 \approx 6.644 \, \text{bits} \]

Each yes/no query divides the grid, e.g., “Is it in the left half (columns 1–5)?” reduces possibilities to 50 cells:

\[ H_1 = \log_2 50 \approx 5.644 \, \text{bits} \]

Information gained:

\[ I = 6.644 - 5.644 = 1 \, \text{bit} \]

After 7 queries, \( \lceil 100 / 2^7 \rceil = 1 \), so \( H_7 = 0 \). An optimal strategy might use queries that split possibilities unevenly but maximize expected information gain, akin to the Weighing Problem’s three-outcome queries.

In Lambda Calculus:

\[ M = \lambda \text{state}.\lambda \text{query}.\text{filter}(\text{state}, \text{query}) \]

- **Initial State**: \(\text{state}_0 = \text{list of } \{(1,1), \ldots, (10,10)\}\).
- **Query**: \(\text{query}_1 = \lambda s.\text{partition}(s, \text{column} \leq 5)\), yielding \(\text{state}_1\) with 50 cells.
- **Entropy**: \( H(\text{state}_0) = \log_2 100 \approx 6.644 \), \( H(\text{state}_1) \approx 5.644 \).

Reversing without queries could trigger divergence, preserving the submarine’s location entropy.

### Comparison with Weighing Problem

The Weighing Problem with 12 coins (24 scenarios) has initial entropy \( \log_2 24 \approx 4.585 \, \text{bits} \). Each three-outcome weighing provides up to \( \log_2 3 \approx 1.585 \, \text{bits} \), reducing entropy to zero in three steps. Similarly, "63" and "Submarine" involve iterative queries reducing entropy, but "63" uses binary queries (1 bit each), and "Submarine" may use binary or multi-outcome queries, depending on the strategy.

| Game              | Initial Possibilities | Initial Entropy (bits) | Query Type | Steps to Zero Entropy |
|-------------------|-----------------------|------------------------|------------|-----------------------|
| Weighing (12 coins) | 24                    | 4.585                  | 3-outcome  | 3                     |
| 63                | 63                    | 5.977                  | Yes/No     | ~6                    |
| Submarine (10x10) | 100                   | 6.644                  | Yes/No     | ~7                    |

## Relating to Shannon Entropy

Shannon Entropy quantifies uncertainty reduction in these games. Each query partitions the outcome space, with the expected entropy after a query given by:

\[ H_{\text{after}} = \sum_i P_i \log_2 |S_i| \]

Information gain is the reduction in entropy, directly relating to Shannon’s framework. Lambda Calculus models these partitions as function applications, with entropy calculated as \( \log_2 |S_i| \) or via probability distributions over reduction paths, providing a computational perspective on information gain.

## Challenges and Considerations

- **Game Identification**: The lack of direct references to "63" and "Submarine" as standard Shannon Entropy examples requires interpretive assumptions, potentially misaligning with the user’s intent.
- **Query Optimization**: Optimal strategies maximize information gain, which may involve non-binary queries in "Submarine," complicating entropy calculations.
- **Lambda Calculus Modeling**: Finite reductions suffice for these games, but infinite paths could model underivability of initial states, as in prior discussions.
- **Probability Assumptions**: Uniform probabilities simplify calculations but may not reflect real-world strategies.

## Conclusion

The games "63" and "Submarine" illustrate Shannon Entropy’s application to iterative uncertainty reduction, modeled in Lambda Calculus as state-filtering reductions. "63" involves identifying one of 63 outcomes through yes/no questions, reducing entropy from 5.977 bits to zero in about 6 steps. "Submarine," akin to Battleship, locates a hidden object in a 10x10 grid, reducing entropy from 6.644 bits to zero in about 7 steps. These examples highlight how each computational step provides information, aligning with Shannon Entropy’s measure of uncertainty reduction, offering insights into decision-making and search strategies.

## Key Citations

- [Entropy in Information Theory](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Balance Puzzle](https://en.wikipedia.org/wiki/Balance_puzzle)
- [Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus)
- [Church-Turing Thesis](https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis)
- [Zero-Knowledge Proof](https://en.wikipedia.org/wiki/Zero-knowledge_proof)
- [Reversible Computing](https://en.wikipedia.org/wiki/Reversible_computing)
- [Landauer’s Principle](https://en.wikipedia.org/wiki/Landauer%27s_principle)
- [Data Compression](https://en.wikipedia.org/wiki/Data_compression)
- [Battleship Game](https://en.wikipedia.org/wiki/Battleship_%28game%29)
- [How Claude Shannon’s Entropy Quantifies Information](https://www.quantamagazine.org/how-claude-shannons-concept-of-entropy-quantifies-information-20220906/)
- [Shannon Entropy, Information Gain, and Picking Balls](https://medium.com/udacity/shannon-entropy-information-gain-and-picking-balls-from-buckets-5810d35d54b4)
- [Refining the Estimated Entropy of English](https://mattmahoney.net/dc/entropy1.html)
- [Shannon’s Entropy/Guessing Game](https://www.reddit.com/r/AskComputerScience/comments/lc8jha/shannons_entropyguessing_game/)
- [Fifty Years of Shannon Information Theory](https://pmc.ncbi.nlm.nih.gov/articles/PMC8863911/)
- [Shannon Entropy Overview](https://www.sciencedirect.com/topics/engineering/shannon-entropy)
- [Humans Outperform Machines at Bilingual Shannon Game](https://www.mdpi.com/1099-4300/19/1/15)
- [Maximum Entropy: Entropy Games](http://maximum-entropy-blog.blogspot.com/2013/10/entropy-games.html)
- [Shannon Entropy Problem](https://www.physicsforums.com/threads/shannon-entropy-problem.377090/)
- [Shannon Game for Language Entropy](https://github.com/lianghuang3/shannon_game)
- [Shannon Game Python Project](https://github.com/VickiShaw94/shannon-game)
- [Shannon Game Lecture](https://www.youtube.com/watch?v=0shft1gokac)
- [Extensions of Shannon Entropy](https://arxiv.org/abs/1909.08193)
- [Shannon Entropy Experiment](https://mathweb.ucsd.edu/~crypto/java/ENTROPY/)
- [Backgammon Is Life: Entropy](https://jeffrey-spencer.medium.com/backgammon-is-life-entropy-fe6daa145b96)
- [Mathematics Behind Battleship](https://blogs.glowscotland.org.uk/glowblogs/njoldfieldeportfolio1/2015/12/01/mathematics-behind-battleship/)
- [An Analysis of Battleship](https://medium.com/%40divijgarg04/a-painful-analysis-of-battleship-ea5a462f0d15)
- [Shannon Entropy Calculator](https://www.omnicalculator.com/statistics/shannon-entropy)
- [Shannon Entropy in Quantum Computing](https://www.reddit.com/r/QuantumComputing/comments/q697oq/confusions_about_shannon_entropy/)
- [Shannon Entropy of a Fair Dice](https://math.stackexchange.com/questions/2916887/shannon-entropy-of-a-fair-dice)
- [Information Theory Series: Entropy](https://rendazhang.medium.com/information-theory-series-1-entropy-and-shannon-entropy-a20a2101108e)
- [Entropy for Data Science](https://www.youtube.com/watch?v=YtebGVx-Fxw)
- [Information Theory](https://en.wikipedia.org/wiki/Information_theory)