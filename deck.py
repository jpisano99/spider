import random
import hashlib
import json
#
# Definitions
# Stack - 13 cards from Ace to King of a any single suit
# Deck - 4 Stacks of each suit Total of 52 cards (Spades, Clubs, Hearts, Diamonds)
# Card - a single card of any suit and any value
#


class Card:
    # Create a single card object of a specific value and suit

    global_id = 0

    def __init__(self, suit: str, value: int):
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
        # serial_bytes = bytes(suit, 'utf-8') + bytes(str(value), 'utf-8') + bytes(str(self.global_id), 'utf-8')
        serial_bytes = bytes(suit, 'utf-8') + bytes(str(value), 'utf-8')
        hash_val = hashlib.md5(serial_bytes).hexdigest()

        self.hash_val = hash_val  # MD5
        self.global_id = self.global_id
        self.suit_glyph = glyph_dict[suit]
        self.suit = suit
        self.str_val = str_val
        self.int_value = value
        self.sequence = 0.0
        self.visible = False

        return

    def __repr__(self):
        _my_card = {}
        for a in dir(self):
            if a[:2] != "__":   # exclude any attribute with dunder __
                # print(a, ': \t', getattr(self, a))
                _my_card[a] = getattr(self, a)

        return json.dumps(_my_card)


class Stack:
    # Create a full suit cards (Ace to King) object of a specific suit

    def __init__(self, suit):
        self.cards = []

        for idx in range(1, 14):
            self.cards.append(Card(suit, idx))
        return

    def shuffle(self):
        random.shuffle(self.cards)
        return

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
        return

    def __repr__(self):
        rep = 'This is a deck of ' + str(len(self.cards)) + ' cards'
        return rep


class Pile:
    # A class for one of the 10 piles on the spider board

    global_pile_id = 0

    def __init__(self, spider_deck, num_of_cards):
        Pile.global_pile_id += 1

        self.pile_id = Pile.global_pile_id
        self.sequences = []
        self.cards = []

        x = 0
        for x in range(0, num_of_cards):
            self.cards.append(spider_deck.pop(x))

        # Make the last card visible and establish the initial sequence
        self.cards[x].visible = True
        self.cards[x].sequence = self.pile_id + .1
        self.sequences.append([self.cards[x]])

    def get_top_card(self):
        top_card = self.cards[-1]
        return top_card

    def reveal_pile(self):
        print('Pile id: ' +str(self.pile_id))
        for card in self.cards:
            print ('\t\t Card id: ', card.global_id, 'is:', '/', card.sequence, card.str_val, card.suit, card.visible)

        # for sequence in self.sequences:
        #     print('\t\t\tSequences: ', sequence)
        return

    def remove_card(self, card):
        removed_card = self.cards[-1]
        del self.cards[-1]
        return removed_card

    def add_card(self, card):
        self.cards.append(card)
        return



