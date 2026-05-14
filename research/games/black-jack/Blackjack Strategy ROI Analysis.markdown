# Measuring Return on Investment for Blackjack Strategies

## Introduction
This report evaluates the **return on investment (ROI)** for three blackjack strategies—basic strategy, Hi-Lo, and Hi-Opt II—in a single-player game against a dealer using a single 52-card deck without reshuffling. The analysis abstracts betting budget and bet amounts, proposing the **combined cost** (a blend of counting classes and SUCC operations) as a proxy for bet size, which is “always paid” per draw. The ROI is calculated to assess whether this abstraction is reasonable, considering standard blackjack payouts (e.g., 3:2 for blackjack, 1:1 for wins). Two ROI metrics are provided: an **edge-based ROI** using expected edge and an **information-based ROI** using entropy reduction, both normalized by cumulative cost until the certainty threshold (entropy \( H \leq 1 \) bit). The report includes formal derivations and implications, formatted as a downloadable Markdown file ([Blackjack](https://en.wikipedia.org/wiki/Blackjack)).

## Blackjack Game Context
- **Setup**: Single player vs. dealer, standard rules (hit on soft 17, blackjack pays 3:2).
- **Deck**: 52 cards, no reshuffling.
- **Prediction**: Next card’s point value (1 for Ace, 2-9, 10 for tens and face cards).
- **Draws**: ~4-6 cards per hand, counted toward total draws (\( k \)).
- **Initial Probabilities**:
  - \( P(1) = 4/52 \approx 0.0769 \), ..., \( P(9) = 4/52 \approx 0.0769 \).
  - \( P(10) = 16/52 \approx 0.3077 \).
- **Initial Entropy**: \( H_0 \approx 3.0845 \) bits.

## Strategies Overview
### Basic Strategy
- **Description**: Fixed probabilities, no tracking.
- **Cost**:
  - Classes (\( C_{\text{basic}} \)): 1.
  - SUCCs (\( S_{\text{basic}} \)): 1.
- **Entropy**: Constant at ~3.08 bits until draw 51.

### Hi-Lo
- **Description**: Tracks running count (+1 for 2-6, -1 for 10-A, 0 for 7-9).
- **Cost**:
  - Classes (\( C_{\text{HiLo}} \)): 3.
  - SUCCs (\( S_{\text{HiLo}} \)): 1.7692.
- **Entropy**: Reaches \( H \leq 1 \) at draw ~40.

### Hi-Opt II
- **Description**: Tracks running count (+1 for 2-6, 7; +2 for 8-9; -1 for 10; -2 for A).
- **Cost**:
  - Classes (\( C_{\text{HiOpt}} \)): 5.
  - SUCCs (\( S_{\text{HiOpt}} \)): 1.7689.
- **Entropy**: Reaches \( H \leq 1 \) at draw ~38.

## Combined Cost Model
- **Per Draw**:
  \[
  \text{Combined Cost}_s = 0.5 \cdot C_s + 0.5 \cdot S_s
  \]
  - Basic: 1.
  - Hi-Lo: 2.3846.
  - Hi-Opt II: 3.3845.
- **Cumulative Cost** (until \( k_s \), where \( H_s(k) \leq 1 \)):
  \[
  \text{Cumulative Cost}_s = k_s \cdot \text{Combined Cost}_s
  \]
  - Basic: \( 51 \cdot 1 = 51 \).
  - Hi-Lo: \( 40 \cdot 2.3846 \approx 95.384 \).
  - Hi-Opt II: \( 38 \cdot 3.3845 \approx 128.611 \).

## ROI Metrics
### Edge-Based ROI
Uses expected edge as the return:
\[
\text{ROI}_s = \frac{\text{Edge}_s}{\text{Cumulative Cost}_s}
\]
- **Edges**:
  - Basic: 0.5% = 0.005.
  - Hi-Lo: 1.2% = 0.012.
  - Hi-Opt II: 1.3% = 0.013.

### Information-Based ROI
Uses cumulative entropy reduction (\( I_s \)) as the return:
\[
\text{ROI}_s = \frac{I_s}{\text{Cumulative Cost}_s}
\]
- **Estimates**:
  - Basic: \( k_{\text{basic}} = 51 \), \( I_{\text{basic}} \approx 0 \).
  - Hi-Lo: \( k_{\text{HiLo}} \approx 40 \), \( I_{\text{HiLo}} \approx 40 \).
  - Hi-Opt II: \( k_{\text{HiOpt}} \approx 38 \), \( I_{\text{HiOpt}} \approx 42 \).

### Calculations
- **Basic Strategy**:
  - Edge-Based ROI: \(\frac{0.005}{51} \approx 0.000098 \text{ (0.0098\%)}\).
  - Information-Based ROI: \(\frac{0}{51} = 0\).
- **Hi-Lo**:
  - Edge-Based ROI: \(\frac{0.012}{95.384} \approx 0.000126 \text{ (0.0126\%)}\).
  - Information-Based ROI: \(\frac{40}{95.384} \approx 0.4195\).
- **Hi-Opt II**:
  - Edge-Based ROI: \(\frac{0.013}{128.611} \approx 0.000101 \text{ (0.0101\%)}\).
  - Information-Based ROI: \(\frac{42}{128.611} \approx 0.3266\).

## Table: ROI Comparison

| **Strategy** | **Cumulative Cost** | **Edge (%)** | **Edge-Based ROI (%)** | **Entropy Reduction (\( I_s \))** | **Information-Based ROI** |
|--------------|---------------------|--------------|-----------------------|----------------------------------|---------------------------|
| Basic        | 51                  | 0.5          | 0.0098                | 0                                | 0                         |
| Hi-Lo        | 95.384              | 1.2          | 0.0126                | 40                               | 0.4195                    |
| Hi-Opt II    | 128.611             | 1.3          | 0.0101                | 42                               | 0.3266                    |

## Analysis
- **Reasonableness**: The information-based ROI is the most reasonable for abstracting monetary units, using entropy reduction as a return and cumulative cost as effort, aligning with the “always paid” concept. The edge-based ROI is less effective due to low values, requiring cost scaling for financial relevance.
- **Implications**:
  - **Hi-Lo**: Highest ROI (0.4195 information-based, 0.0126% edge-based), optimal for balancing predictive accuracy and effort.
  - **Hi-Opt II**: Strong predictions but lower ROI (0.3266, 0.0101%) due to higher cost, suitable for advanced players.
  - **Basic Strategy**: Zero ROI, minimal cost, no predictive benefit.

## Challenges and Limitations
- **Cost Scaling**: Combined cost as bet size needs scaling for financial ROI.
- **Payout Modeling**: Edge simplifies payouts, omitting hand-specific outcomes.
- **Sequence Variability**: Draw sequences affect costs and ROI.

## Conclusion
Using combined cost as a proxy for bet size is reasonable for abstracting ROI in a non-monetary sense, with the information-based ROI (\(\frac{I_s}{\text{Cumulative Cost}_s}\)) being the most effective, confirming Hi-Lo’s superiority (0.4195) over Hi-Opt II (0.3266) and basic strategy (0). This downloadable Markdown file provides a clear framework for evaluating blackjack strategy ROI ([Card Counting]([invalid url, do not cite])).