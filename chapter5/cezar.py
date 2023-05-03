# DMOJ problem coci17c1p1

deck = [4, 4, 4, 4, 4, 4, 4, 4, 16, 4] # Cards left for each value (2, 3, 4, ... Ace)

cards = int(input())
hand = []

for _ in range(cards):
    hand.append(int(input()))

difference = 21 - sum(hand)

for i in range(len(hand)):
    deck[hand[i]-2] -= 1 # Decrement the amount of a card in deck by value
    # For example, if the first card in hand is 6, hand[0] = 6
    # deck[6-2] = 4, the current amount of 6's in deck currently
    # Should work as intended as hand[i] >= 2 always

greater_count = 0
# Find number of cards left in deck with a value greater than difference
for i in range(difference-1, len(deck)): 
    greater_count += deck[i]

less_count = 52 - len(hand) - greater_count # Rest of cards left in deck

if greater_count >= less_count:
    print("DOSTA")
else:
    print("VUCI")