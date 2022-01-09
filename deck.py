import random
import hashlib
#
# Definitions
# Stack - 13 cards from Ace to King of a any single suit
# Deck - 4 Stacks of each suit (Spades, Clubs, Hearts, Diamonds)
# Card - a single card of any suit and any value
#


class Card:
    # Create a single card object of a specific value and suit

    global_id = 0

    def __init__(self, suit, value):
        # Create a globally unique ID for this card
        Card.global_id += 1

        # Dicts for unicode card symbols and string names
        glyph_dict = {'Spades': '\u2660', 'Clubs': '\u2663', 'Hearts': '\u2665', 'Diamonds': '\u2666'}
        value_dict = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}

        # Create a string name for this card value
        str_val = str(value)
        if value == 1 or value >= 11:
            str_val = value_dict[value]

        # Create an MD5 Hash value
        serial_bytes = bytes(suit, 'utf-8') + bytes(str(value), 'utf-8') + bytes(str(self.global_id), 'utf-8')
        hash_val = hashlib.md5(serial_bytes).hexdigest()

        self.id = hash_val  # MD5
        self.global_id = self.global_id
        self.suit_glyph = glyph_dict[suit]
        self.suit = suit
        self.str_val = str_val
        self.int_value = value
        self.visible = False

        # print('global id', Card.global_id, str_val + ' of ' + suit)

    def __repr__(self):
        rep = 'Your Card is a ' + str(self.str_val) + \
              ' of ' + self.suit + ' ' + self.suit_glyph + \
              ' with a md5 hash of ' + str(self.id)
        return rep


class Stack:
    # Create a full suit cards (Ace to King) object of a specific suit

    def __init__(self, suit):
        self.cards = []

        for idx in range(1, 14):
            self.cards.append(Card(suit, idx))

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        rep = 'This is a stack of ' + str(self.cards[1].suit)

        return rep


class Deck:
    # Create a full deck of standard cards

    def __init__(self):
        self.cards = []

        suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

        for suit in suits:
            for idx in range(1, 14):
                self.cards.append(Card(suit, idx))

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        rep = 'This is a deck of ' + str(len(self.cards)) + ' cards'
        return rep


class Pile:

    def __init__(self, spider_deck, num_of_cards):
        self.pile = []

        for x in range(0, num_of_cards):
            self.pile.append(spider_deck.pop(x))

        # Make the last card visible
        self.pile[x].visible = True

        # for card in self.pile:
        #     print(card.global_id, card.suit, card.str_val, card.visible)
        # print()
        #
        # print()
        # print('Deck now has ', len(spider_deck))
