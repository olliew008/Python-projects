import random



print('Welcome to blackjack! You have £5000 to waste ;) ')
card_categories = ['H', 'D', 'C', 'S']
cards_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(card, category) for category in card_categories for card in cards_list]
global z


ra = random.choice(deck)
card, category = ra
print(ra)
print(card, category)
rb = list(ra)


def card_value():
    if card[0] in ['J','Q', 'k']:
        return 10
    elif card[0] == 'A':
      return 11
    else:
      return int(card[0])


def card_face():
    print('--------')
    print('-',card, category+'  -')
    print('-      -')
    print('--------')
card_face()


random.shuffle(deck)
dealer_hand = deck.pop()

print(dealer_hand)

