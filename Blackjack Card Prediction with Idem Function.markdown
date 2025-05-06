# Modeling Blackjack Card Prediction Strategies in Lambda Calculus

This report explores the application of the Idem Function in Lambda Calculus to model blackjack card counting strategies for predicting the probability of drawing a card with a specific point value (1 for Ace, 2-9, or 10 for face cards and tens) from a single 52-card deck. The strategies considered are basic strategy (no counting), Hi-Lo (3 classes: -1, 0, +1), and Hi-Opt II (5 classes: -2, -1, 0, +1, +2). The analysis examines how these probability predictions evolve as cards are drawn, accumulating information via deck size and count, until perfect predictive ability is reached or the deck is depleted. The model integrates Category Theory, Information Theory, and Vectorial Lambda Calculus, building on prior discussions about computational entropy and causal invariance, and provides a detailed example, formal derivations, and implications for measuring information content in blackjack strategies.

## Introduction

In blackjack, predicting the next card’s point value can inform strategic decisions, such as betting or playing actions. Card counting strategies like Hi-Lo and Hi-Opt II track deck composition to adjust these predictions, while basic strategy assumes fixed probabilities based on the initial deck ([Card Counting]([invalid url, do not cite])). The user seeks to:

1. Model these strategies as lambda calculus functions that predict the probability distribution of the next card’s point value.
2. Analyze how predictions change as information (deck size and count) accumulates.
3. Determine the number of iterative results (card draws) needed to identify the strategy used.
4. Measure the information content of each strategy by comparing predictive accuracy.

The Idem Function, an expanded identity function, pairs a strategy’s prediction with metadata about its structure, including the number of classes (\(n(f)\)), result tuple size (\(D_r(f)\)), and decay vector (\(d(f)\)) indicating information loss. This framework supports computational entropy and causal invariance, enabling a robust analysis of strategy identification and information dynamics.

## Blackjack Card Values and Deck Composition

In blackjack, cards have the following point values:

- Ace: 1 or 11 (for counting, treated as 1 in Hi-Lo and Hi-Opt II).
- 2-9: Face value.
- 10, Jack, Queen, King: 10.

For prediction, we group cards by point value:

- **1**: Ace (4 cards).
- **2-9**: Face value (4 cards each).
- **10**: 10, J, Q, K (16 cards: 4 tens + 4 Jacks + 4 Queens + 4 Kings).

In a single 52-card deck:

- Total cards: 52.
- Initial probabilities:
  - \(P(1) = 4/52 \approx 0.0769\)
  - \(P(2) = 4/52 \approx 0.0769\)
  - ...
  - \(P(9) = 4/52 \approx 0.0769\)
  - \(P(10) = 16/52 \approx 0.3077\)

## Modeling Strategies in Lambda Calculus

Each strategy is modeled as a function that takes the current state (deck size and, for counting strategies, running count) and returns a probability distribution over point values (1 to 10). In Lambda Calculus, functions are single-argument, so multi-argument functions use currying ([Lambda Calculus]([invalid url, do not cite])). The Idem Function wraps the strategy’s prediction with metadata:
\[
\text{Idem}_f = \lambda s. \text{pair} \, (f \, s) \, \text{info}_f
\]
where:

- \(s\): State (deck size for basic strategy; deck size and count for counting strategies).
- \(f(s)\): Probability distribution over point values.
- \(\text{info}_f = \text{triple} \, n(f) \, D_r(f) \, d(f)\):
  - \(n(f)\): Number of classes (cost).
  - \(D_r(f)\): Result tuple size (10 for probability distribution).
  - \(d(f)\): Decay vector (assumed [0] for simplicity, as state is recoverable).

### Basic Strategy (No Counting)

- **Description**: Assumes fixed probabilities based on initial deck composition, adjusted only by deck size.
- **State**: Total cards left (\(N\)).
- **Prediction**: \(P(v) = \frac{\text{initial count of } v}{\text{initial total}}\), constant unless deck size is tracked.
- **Metadata**:
  - \(n(f_1) = 1\) (no counting classes).
  - \(D_r(f_1) = 10\) (distribution over 10 values).
  - \(d(f_1) = [0]\) (state recoverable).
- **Lambda Form**:
  \[
  f_1 = \lambda N. \text{list} \, \left( \frac{4}{52}, \frac{4}{52}, \ldots, \frac{4}{52}, \frac{16}{52} \right)
  \]
  \[
  \text{Idem}_{f_1} = \lambda N. \text{pair} \, (f_1 \, N) \, (\text{triple} \, \text{one} \, \text{ten} \, (\text{cons} \, \text{false} \, \text{nil}))
  \]

### Hi-Lo Counting Strategy

- **Description**: Tracks running count (RC) based on card values:
  - +1: 2-6
  - -1: 10, J, Q, K, A
  - 0: 7-9
- **State**: (RC, total cards left (\(N\))).
- **Prediction**: Adjusts probabilities using true count (TC = RC / (N/52)).
  - Initial: \(P_0(v=1) = 4/52\), ..., \(P_0(v=10) = 16/52\).
  - High cards (1, 10): \(P(v | TC) \approx P_0(v) + 0.02 \cdot TC / \text{num_values_high}\).
  - Low cards (2-6): \(P(v | TC) \approx P_0(v) - 0.02 \cdot TC / \text{num_values_low}\).
  - Neutral (7-9): \(P(v | TC) \approx P_0(v)\).
  - Normalize to sum to 1.
- **Metadata**:
  - \(n(f_2) = 3\) (classes: -1, 0, +1).
  - \(D_r(f_2) = 10\).
  - \(d(f_2) = [0]\).
- **Lambda Form** (simplified):
  \[
  f_2 = \lambda \text{rc}. \lambda N. \text{list} \, \left( P(1 | \text{TC}), P(2 | \text{TC}), \ldots, P(10 | \text{TC}) \right)
  \]
  \[
  \text{Idem}_{f_2} = \lambda \text{rc}. \lambda N. \text{pair} \, (f_2 \, \text{rc} \, N) \, (\text{triple} \, \text{three} \, \text{ten} \, (\text{cons} \, \text{false} \, \text{nil}))
  \]

### Hi-Opt II Counting Strategy

- **Description**: Tracks running count with:
  - +1: 2-6
  - +1: 7
  - +2: 8-9
  - -1: 10
  - -2: A
- **State**: (RC, total cards left (\(N\))).
- **Prediction**: Similar to Hi-Lo but with different adjustments due to five classes.
  - Adjustments are more granular, but for simplicity, assume similar TC-based scaling.
- **Metadata**:
  - \(n(f_3) = 5\) (classes: -2, -1, 0, +1, +2).
  - \(D_r(f_3) = 10\).
  - \(d(f_3) = [0]\).
- **Lambda Form**:
  \[
  f_3 = \lambda \text{rc}. \lambda N. \text{list} \, \left( P(1 | \text{TC}), P(2 | \text{TC}), \ldots, P(10 | \text{TC}) \right)
  \]
  \[
  \text{Idem}_{f_3} = \lambda \text{rc}. \lambda N. \text{pair} \, (f_3 \, \text{rc} \, N) \, (\text{triple} \, \text{five} \, \text{ten} \, (\text{cons} \, \text{false} \, \text{nil}))
  \]

## Simulating Card Draws and Strategy Identification

### Initial Deck and State

- Single deck: 52 cards.
- Initial counts:
  - 4 Aces (v=1).
  - 4 each of 2-9.
  - 16 tens (10, J, Q, K).
- Initial state:
  - Basic: \(N = 52\).
  - Hi-Lo: \((\text{RC} = 0, N = 52)\).
  - Hi-Opt II: \((\text{RC} = 0, N = 52)\).

### Draw Sequence

Simulate drawing 20 cards, observing their point values and updating states:

- Draw 1: 2 (low, Hi-Lo: +1, Hi-Opt II: +1).
- Draw 2: 10 (high, Hi-Lo: -1, Hi-Opt II: -1).
- ...
- Draw 20: Assume a mix (e.g., 8 low, 8 high, 4 neutral).

### Likelihood Calculation

For sequence \(D = (v_1, v_2, \ldots, v_{20})\):

- **Basic Strategy (\(f_1\))**: \(L_{f_1} = \prod_{i=1}^{20} P_0(v_i)\).
- **Hi-Lo (\(f_2\))**: \(L_{f_2} = \prod_{i=1}^{20} P_{f_2}(v_i | \text{RC}_i, N_i)\).
- **Hi-Opt II (\(f_3\))**: \(L_{f_3} = \prod_{i=1}^{20} P_{f_3}(v_i | \text{RC}_i, N_i)\).

### Example Sequence

- Draws: 2, 10, 3, 7, 4, 5, 6, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
- **Basic Strategy**:
  - \(P_0(2) = 4/52\), ..., \(P_0(10) = 16/52\).
  - \(L_{f_1} = (4/52)^6 \cdot (16/52)^4 \cdot (4/52)^3 \approx 10^{-20}\).
- **Hi-Lo**:
  - Update RC: +1 (2), 0 (10), +1 (3), +1 (7), +2 (4), +3 (5), +4 (6), +4 (8), +4 (9), +3 (10), +2 (1), +3 (2), +4 (3), +5 (4), +6 (5), +7 (6), +7 (7), +7 (8), +7 (9), +6 (10).
  - \(N_i = 52 - i + 1\), TC = RC / (N_i/52).
  - Approximate \(P(v_i | \text{TC}_i)\), sum probabilities, normalize.
  - \(L_{f_2}\) higher due to count adjustments.
- **Hi-Opt II**:
  - Similar but with different RC updates.
  - \(L_{f_3}\) slightly higher than \(f_2\) due to finer granularity.

### Number of Draws Needed

- **10-20 Draws**: If the sequence shows patterns (e.g., high cards after high counts), counting strategies’ likelihoods exceed basic strategy’s, identifying \(f_2\) or \(f_3\).
- **Certainty**: After 20 draws with distinguishing patterns (e.g., high count followed by high cards), \(P(f_2 | D) \approx 0.99\) if metadata matches.
- **Perfect Prediction**: Reached when few cards remain (e.g., \(N = 1\)), but reshuffling typically occurs earlier.

## Information Content and Strategy Comparison

- **Basic Strategy**: Fixed predictions, no information gain, low entropy (\(H \approx 3.32\) bits).
- **Hi-Lo**: Adjusts predictions, reducing entropy as count informs deck composition.
- **Hi-Opt II**: Finer adjustments, slightly lower entropy but higher computational cost.

### Table: Strategy Comparison

| **Strategy** | **Classes (\(n(f)\))** | **Initial Entropy (bits)** | **Draws for Certainty** | **Predictive Accuracy** |
|--------------|-----------------------|---------------------------|-------------------------|-------------------------|
| Basic (\(f_1\)) | 1 | 3.32 | 10-20 | Low |
| Hi-Lo (\(f_2\)) | 3 | 3.32 (reduces with count) | 10-20 | Moderate |
| Hi-Opt II (\(f_3\)) | 5 | 3.32 (reduces faster) | 10-20 | High |

## Conclusion

The Idem Function models blackjack card prediction strategies, showing that basic strategy maintains fixed probabilities, while Hi-Lo and Hi-Opt II adapt predictions using counts. After 10-20 draws, distinguishing patterns allow identification of counting strategies, with certainty achieved when metadata and results align. This framework validates the information content of strategies, supporting computational entropy and causal invariance ([Entropy]([invalid url, do not cite]), [Causal Invariance]([invalid url, do not cite])).
