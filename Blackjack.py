import random
def create_deck():
    suits = ['♠', '♣', '♥', '♦']
    values = ['2', '3', '4', '5', '6' , '7', '8', '9', 'J', 'Q', 'K', 'A']
    deck = []
    for value in values:
        for suit in suits:
            deck.append(value + suit)
    return deck
# deck = create_deck
# print(create_deck())
