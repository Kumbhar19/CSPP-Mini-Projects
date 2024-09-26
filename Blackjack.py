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

def calculate_hand_value(hand):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    value = 0
    for card in hand:
        card_value = card[:-1]
        value += values[card_value]
    ace_in_hand = False
    for card in hand:
        if card[:-1] == 'A':
            ace_in_hand = True 
            break
    if ace_in_hand and value + 10 <= 21:
        value += 10
    return value


