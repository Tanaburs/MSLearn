# --Create a list for a standard deck of cards-----
import random
suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
deck = []
deal = []

for suit in suits:
    for rank in ranks:
        deck.append(str(rank) + " of " + suit)
print(f"There are {len(deck)} cards in the deck.")

print("Dealing ...")
while len(deal) < 5:
    card = random.choice(deck)
    deck.remove(card)
    deal.append(card)
    # print(deal)

# print(deck)
# deal.append(deck.pop(random.choices(deck, k=5)))
#
# print(deal)

print(f"There are {len(deck)} cards in the deck")
print("Player has the following cards in their hand:")
print(deal)
