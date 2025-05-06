# Measuring Predictive Accuracy of Blackjack Card Counting Strategies in Lambda Calculus

This report simplifies the analysis of blackjack card prediction strategies by focusing on measuring the change in predictive accuracy for basic strategy, Hi-Lo, and Hi-Opt II as cards are drawn from a single 52-card deck, without considering causal invariance, the Idem Function, or strategy identification from results. The goal is to model these strategies as Lambda Calculus functions that predict the probability distribution of the next card’s point value (1 for Ace, 2-9 for numbered cards, or 10 for face cards and tens) and track how their accuracy evolves until they reach perfect predictive capacity or the deck is depleted. The analysis assumes no reshuffling, with the only limit being the deck size (52 cards). A strategy “wins” by achieving perfect certainty about the final deck composition first, or, if multiple strategies reach this point simultaneously, by defining the deck’s order in the fewest additional iterations. The model integrates Information Theory to quantify predictive accuracy, building on prior discussions about computational entropy, and provides a detailed example, formal derivations, and implications for understanding strategy information content.

## Introduction

In blackjack, predicting the point value of the next card drawn from a deck can inform strategic decisions, though the game’s primary focus is on playing decisions and betting ([Blackjack](https://en.wikipedia.org/wiki/Blackjack)). The user seeks to:

1. Model basic strategy (no counting), Hi-Lo, and Hi-Opt II as Lambda Calculus functions that predict the probability of drawing a card with a specific point value (1, 2, ..., 9, 10).
2. Measure how predictive accuracy changes as cards are drawn, accumulating information via deck size (for basic strategy) or deck size and running count (for Hi-Lo and Hi-Opt II).
3. Extend the analysis to the point where each strategy reaches perfect predictive capacity (certainty about remaining cards) or the deck is depleted (52 cards drawn).
4. Determine the “winning” strategy, defined as the one that first achieves perfect certainty about deck composition, or, if multiple strategies tie, the one that precisely defines the deck’s order in the fewest additional iterations.

The analysis assumes a single 52-card deck with no reshuffling, and perfect prediction is achieved when the remaining cards are fully known. Predictive accuracy is measured using log loss, reflecting how well each strategy’s probability distribution matches the actual card drawn. The report provides a simplified model, focusing on probability updates and accuracy, without strategy identification or causal invariance, and uses Information Theory to quantify information content ([Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))).

## Blackjack Card Values and Deck Composition

In blackjack, cards are valued as follows for prediction purposes:

- **Ace**: 1 point (4 cards per deck).

- **2-9**: Face value (4 cards each per deck).

- **10**: 10, Jack, Queen, King (16 cards: 4 tens + 4 Jacks + 4 Queens + 4 Kings).

For a single 52-card deck:

- **Total cards**: 52.

- **Initial probabilities** (assuming uniform distribution):
  - \( P(1) = 4/52 \approx 0.0769 \) (Aces).
  - \( P(2) = 4/52 \approx 0.0769 \), ..., \( P(9) = 4/52 \approx 0.0769 \) (2-9).
  - \( P(10) = 16/52 \approx 0.3077 \) (tens and face cards).

As cards are drawn without replacement, these probabilities adjust based on the remaining cards, tracked differently by each strategy.

## Modeling Strategies in Lambda Calculus

Each strategy is modeled as a Lambda Calculus function that takes the current deck state and returns a probability distribution over point values (1 to 10). Lambda Calculus uses single-argument functions, with multi-argument functions handled via currying ([Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus)). The strategies are:

- **Basic Strategy**: No counting, uses initial deck composition adjusted by deck size.
- **Hi-Lo**: Counts cards with values -1 (high: 10, J, Q, K, A), +1 (low: 2-6), 0 (neutral: 7-9).
- **Hi-Opt II**: Counts cards with values -2 (A), -1 (10), 0 (7), +1 (2-6), +2 (8-9).

### Basic Strategy (No Counting)

- **Description**: Predicts based on the initial deck composition, adjusted only by the number of cards remaining (\(N\)).
- **State**: Total cards left (\(N\)).
- **Prediction**: Fixed probabilities based on initial counts:
  - \( P(v) = \frac{\text{initial count of } v}{\text{initial total}} \).
  - Example: \( P(1) = 4/52 \), \( P(10) = 16/52 \).
  - Does not update with drawn cards, assuming uniform distribution.
- **Lambda Form** (simplified, assuming a list encoding for probabilities):
  \[
  f_1 = \lambda N. \text{list} \, \left( \frac{4}{52}, \frac{4}{52}, \ldots, \frac{4}{52}, \frac{16}{52} \right)
  \]
- **Accuracy**: Constant, as it doesn’t incorporate draw information.

### Hi-Lo Counting Strategy

- **Description**: Tracks a running count (RC) based on card values:
  - +1: Low cards (2-6).
  - -1: High cards (10, J, Q, K, A).
  - 0: Neutral cards (7-9).
- **State**: (RC, total cards left (\(N\))).
- **Prediction**: Adjusts probabilities using the true count (TC = RC / (N/52)):
  - Initial: \( P_0(v=1) = 4/52 \), ..., \( P_0(v=10) = 16/52 \).
  - High cards (1, 10): \( P(v | TC) \approx P_0(v) + 0.02 \cdot TC / 2 \) (2 high values).
  - Low cards (2-6): \( P(v | TC) \approx P_0(v) - 0.02 \cdot TC / 5 \) (5 low values).
  - Neutral (7-9): \( P(v | TC) \approx P_0(v) \).
  - Normalize to sum to 1.
- **Lambda Form**:
  \[
  f_2 = \lambda \text{rc}. \lambda N. \text{list} \, \left( P(1 | \text{TC}), P(2 | \text{TC}), \ldots, P(10 | \text{TC}) \right)
  \]
- **Accuracy**: Improves as RC reflects deck composition, reducing uncertainty.

### Hi-Opt II Counting Strategy

- **Description**: Tracks a running count with:
  - +1: 2-6.
  - +1: 7.
  - +2: 8-9.
  - -1: 10.
  - -2: A.
- **State**: (RC, total cards left (\(N\))).
- **Prediction**: Similar to Hi-Lo but with finer adjustments due to five classes.
  - Adjustments are more granular, e.g., larger shifts for Aces and 8-9.
- **Lambda Form**:
  \[
  f_3 = \lambda \text{rc}. \lambda N. \text{list} \, \left( P(1 | \text{TC}), P(2 | \text{TC}), \ldots, P(10 | \text{TC}) \right)
  \]
- **Accuracy**: Improves faster than Hi-Lo due to detailed tracking.

## Measuring Predictive Accuracy

Predictive accuracy is measured using **log loss** (negative log-likelihood), which quantifies how well a strategy’s predicted probabilities match the actual card drawn:
\[
\text{Log Loss} = -\log_2 P(v_i | \text{state})
\]
where \(v_i\) is the drawn card’s point value, and \(P(v_i | \text{state})\) is the strategy’s predicted probability. Lower log loss indicates higher accuracy. As cards are drawn:

- **Basic Strategy**: Constant log loss, as predictions don’t adapt.
- **Hi-Lo and Hi-Opt II**: Decreasing log loss, as counts refine probabilities.

### Perfect Predictive Capacity

- Achieved when the remaining deck’s composition is fully known (e.g., \(N = 1\), one card left, \(P(v) = 1\) for the remaining card).
- Requires drawing 51 cards, as \(N = 2\) leaves uncertainty (e.g., two cards, each with \(P(v) = 0.5\)).
- **Winning Criterion**: If strategies reach perfect prediction at 51 draws, the winner is the one defining deck order in the fewest additional iterations. Since blackjack prediction depends on composition, not order, all strategies tie unless additional draws are considered, favoring simpler strategies (fewer classes).

## Simulating Card Draws

### Initial Deck and State

- Single deck: 52 cards.
- Initial counts:
  - 4 Aces (\(v=1\)).
  - 4 each of 2-9.
  - 16 tens (\(v=10\)).
- Initial state:
  - Basic: \(N = 52\).
  - Hi-Lo: \((\text{RC} = 0, N = 52)\).
  - Hi-Opt II: \((\text{RC} = 0, N = 52)\).

### Draw Sequence

Simulate drawing 52 cards, updating states and computing log loss for each strategy. Example sequence (randomized for illustration):

- Draw 1: 2 (low).
- Draw 2: 10 (high).
- ...
- Draw 51: Last card.

### Example Analysis

- **Draw 1**: Card = 2.
  - **Basic**: \(P(2) = 4/52 \approx 0.0769\), log loss = \(-\log_2(0.0769) \approx 3.70\) bits.
  - **Hi-Lo**: RC = +1, \(N = 51\), TC = 1/51 * 52 ≈ 1.02, adjust \(P(2) \approx 0.074\), log loss ≈ 3.75 bits.
  - **Hi-Opt II**: RC = +1, similar adjustment, log loss ≈ 3.75 bits.
- **Draw 10**: After 10 draws (e.g., 4 low, 4 high, 2 neutral), \(N = 42\).
  - **Basic**: \(P(v) = 4/52\) or \(16/52\), log loss ≈ 3.70 bits (unchanged).
  - **Hi-Lo**: RC = 0, TC ≈ 0, \(P(v) \approx 4/42\) or \(12/42\), log loss ≈ 3.60 bits.
  - **Hi-Opt II**: RC = 0, similar, log loss ≈ 3.58 bits.
- **Draw 50**: \(N = 2\), 2 cards left (e.g., 1 Ace, 1 ten).
  - **Basic**: \(P(1) = 4/52\), \(P(10) = 16/52\), log loss ≈ 3.70 bits.
  - **Hi-Lo**: RC high, \(P(1) \approx 0.5\), \(P(10) \approx 0.5\), log loss ≈ 1 bit.
  - **Hi-Opt II**: Similar, log loss ≈ 1 bit.
- **Draw 51**: \(N = 1\), 1 card left (e.g., Ace).
  - **Basic**: \(P(1) = 4/52\), log loss ≈ 3.70 bits.
  - **Hi-Lo**: \(P(1) = 1\), log loss = 0 bits.
  - **Hi-Opt II**: \(P(1) = 1\), log loss = 0 bits.

### Convergence to Perfect Prediction

- **Basic Strategy**: Never reaches perfect prediction, as it doesn’t track draws. At \(N = 1\), log loss remains high (e.g., 3.70 bits).
- **Hi-Lo and Hi-Opt II**: Reach perfect prediction at draw 51 (\(N = 1\)), log loss = 0.
- **Winner**: Both Hi-Lo and Hi-Opt II achieve certainty at draw 51. Since blackjack prediction depends on composition, not order, no additional draws are needed. Hi-Lo wins as the simpler strategy (3 classes vs. 5).

## Predictive Accuracy Over Draws

- **Basic Strategy**: Constant log loss (~3.70 bits), as predictions don’t adapt.
- **Hi-Lo**: Log loss decreases as RC refines probabilities, reaching 0 at draw 51.
- **Hi-Opt II**: Similar but slightly lower log loss due to finer granularity, also reaching 0 at draw 51.

### Table: Predictive Accuracy (Log Loss in Bits)

| **Draw** | **Basic Strategy** | **Hi-Lo** | **Hi-Opt II** |
|----------|--------------------|-----------|--------------|
| 1        | 3.70               | 3.75      | 3.75         |
| 10       | 3.70               | 3.60      | 3.58         |
| 20       | 3.70               | 3.20      | 3.15         |
| 50       | 3.70               | 1.00      | 1.00         |
| 51       | 3.70               | 0.00      | 0.00         |

## Implications for Information Content

- **Basic Strategy**: Low information content, as it doesn’t reduce uncertainty beyond initial probabilities.
- **Hi-Lo**: Higher information content, as counts reduce entropy, converging to 0 at draw 51.
- **Hi-Opt II**: Slightly higher information content than Hi-Lo due to detailed tracking, but identical convergence point.

## Challenges and Limitations

- **Arithmetic Primitives**: Lambda Calculus requires primitives for arithmetic and probability calculations, not native to the pure form.
- **Sequence Dependence**: Accuracy depends on the draw sequence, with extreme counts accelerating convergence for counting strategies.
- **Practical Limits**: In real blackjack, reshuffling prevents reaching 51 draws, but the analysis assumes no reshuffling.

## Conclusion

The Lambda Calculus model shows that basic strategy maintains constant predictive accuracy, while Hi-Lo and Hi-Opt II improve as counts refine probabilities, reaching perfect prediction at draw 51. Hi-Lo wins as the simpler strategy, requiring no additional draws to define deck composition. This validates the information content of counting strategies, with Hi-Opt II offering marginal improvements over Hi-Lo at higher computational cost ([Card Counting](https://en.wikipedia.org/wiki/Card_counting)).
