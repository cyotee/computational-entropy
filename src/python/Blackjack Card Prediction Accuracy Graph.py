import numpy as np
import matplotlib.pyplot as plt

# Initial counts for card point values
initial_counts = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}
total_cards = sum(initial_counts.values())  # 52

# Initial probabilities
P0 = {v: count / total_cards for v, count in initial_counts.items()}

# Function to compute entropy
def entropy(p):
    return -sum([p_v * np.log2(p_v) if p_v > 0 else 0 for p_v in p.values()])

# Simulate deck
deck = []
for v in range(1, 11):
    deck.extend([v] * initial_counts[v])
np.random.shuffle(deck)

# Initialize strategies
RC_HiLo = 0
RC_HiOpt = 0
H_basic = []
H_HiLo = []
H_HiOpt = []

# Simulate draws
for k in range(52):
    N_current = 52 - k
    
    # Basic strategy: always uses initial probabilities
    P_basic = P0.copy()
    H_basic.append(entropy(P_basic))
    
    # Hi-Lo: adjust probabilities based on true count
    if N_current > 0:
        TC_HiLo = RC_HiLo / (N_current / 52)
        adjustment = 0.02 * TC_HiLo
        P_HiLo = {v: max(0, min(1, P0[v] + adjustment if v in [1, 10] else P0[v] - adjustment / 5 if v in [2, 3, 4, 5, 6] else P0[v])) for v in range(1, 11)}
        total = sum(P_HiLo.values())
        P_HiLo = {v: p / total if total > 0 else 0 for v, p in P_HiLo.items()}
        H_HiLo.append(entropy(P_HiLo))
    else:
        H_HiLo.append(0)
    
    # Hi-Opt II: adjust probabilities with different weights
    if N_current > 0:
        TC_HiOpt = RC_HiOpt / (N_current / 52)
        P_HiOpt = {v: max(0, min(1, P0[v] - 0.06 * TC_HiOpt if v == 1 else P0[v] - 0.03 * TC_HiOpt if v == 10 else P0[v] + 0.03 * TC_HiOpt if v in [2, 3, 4, 5, 6, 7] else P0[v] + 0.06 * TC_HiOpt if v in [8, 9] else P0[v])) for v in range(1, 11)}
        total = sum(P_HiOpt.values())
        P_HiOpt = {v: p / total if total > 0 else 0 for v, p in P_HiOpt.items()}
        H_HiOpt.append(entropy(P_HiOpt))
    else:
        H_HiOpt.append(0)
    
    # Draw the next card
    if k < 51:
        next_card = deck[k]
        # Update RC_HiLo
        if next_card in [2, 3, 4, 5, 6]:
            RC_HiLo += 1
        elif next_card in [1, 10]:
            RC_HiLo -= 1
        # Update RC_HiOpt
        if next_card in [2, 3, 4, 5, 6, 7]:
            RC_HiOpt += 1
        elif next_card in [8, 9]:
            RC_HiOpt += 2
        elif next_card == 10:
            RC_HiOpt -= 1
        elif next_card == 1:
            RC_HiOpt -= 2
    else:
        # At k=51, no more draws
        H_basic.append(0)  # Assume perfect prediction at N=1
        H_HiLo.append(0)
        H_HiOpt.append(0)
        break

# Plot
plt.figure(figsize=(10, 6))
plt.plot(range(52), H_basic, label='Basic Strategy', color='blue')
plt.plot(range(52), H_HiLo, label='Hi-Lo', color='green')
plt.plot(range(52), H_HiOpt, label='Hi-Opt II', color='red')
plt.xlabel('Number of Draws')
plt.ylabel('Entropy (bits)')
plt.title('Change in Predictive Certainty Over Draws')
plt.legend()
plt.grid(True)
plt.savefig('blackjack_prediction_certainty.png')