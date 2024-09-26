import random
def create_deck():
    suits = ['♠', '♣', '♥', '♦']
    values = ['2', '3', '4', '5', '6' , '7', '8', '9', 'J', 'Q', 'K', 'A']
    deck = []
    for value in values:
        for suit in suits:
            deck.append(value + suit)
    return deck

def deal_initial_cards(deck):
    player_hand = []
    dealer_hand = []
    for i in range(2):
        random_index = random.randint(0, len(deck) -1)
        player_hand.append(deck.pop(random_index))
        random_index = random.randint(0, len(deck) -1)
        dealer_hand.append(deck.pop(random_index))
    return player_hand, dealer_hand

