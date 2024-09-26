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

def display_hands(player_hand, dealer_hand, reveal_dealer_card=False):
    player_value = calculate_hand_value(player_hand)
    player_hand_str = "Player's hand: " + ', '.join(dealer_hand)+ "(total: " + str(player_value) + ")"
    print(player_hand_str)
    if reveal_dealer_card:
        dealer_value = calculate_hand_value(dealer_hand)
        dealer_hand_str = "Dealer's hand: " + ', '.join(dealer_hand)+ "(total: " + str(dealer_value) + ")"
        print(dealer_hand_str)
    else:
        dealer_hand_str = "Dealer's hand: " + dealer_hand[0] + ", [hidden]"
        print(dealer_hand_str)

def player_turn(deck, player_hand):
    while True:
        choice = input("Would you like to (H)it or (S)tand? ").upper()
        if choice == 'H':   
            player_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
            print("Player hits and receives: " + player_hand[-1])
            display_hands(player_hand, [], True)
            if calculate_hand_value(player_hand) > 21:
                print("Player busts!")
                return True
            elif choice == 'S':
                print("Player stands.")
                return False


