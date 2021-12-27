import random
import base64
import hashlib
#
# Definitions
# Stack - 13 cards from Ace to King of a any single suit
# Deck - 4 Stacks of each suit (Spades, Clubs, Hearts, Diamonds)
# Card - a single card of any suit and any value
#


class Card:

    _id = 0

    def __init__(self, suit, value, card_type='random'):
        suit_dict = {1: 'Spades', 2: 'Clubs', 3: 'Hearts', 4: 'Diamonds'}
        value_dict = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        Card._id = Card._id + 1

        d=hashlib.md5(b"hello worlds").digest()
        d=base64.b64encode(d)
        print(d)
        exit()


        if card_type == 'random':
            self.id = Card._id,
            self.card_type = card_type
            self.suit = random.randrange(1, 5, 1)
            self.value = random.randrange(1, 14, 1)

            self.suit = suit_dict.get(self.suit)
            self.value = value_dict.get(self.value, str(self.value))
        else:
            self.id = Card._id
            self.suit = suit
            self.value = value
            self.card_type = card_type

    def __repr__(self):
        rep = 'Your Card is # ' + str(self.id) + ' is ' + self.value + ' of ' + self.suit
        return rep


class Stack:

    def __init__(self, suit):
        value_dict = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}

        card_values = [*range(1, 14)]
        random.shuffle(card_values)

        self.cards = []
        for idx in card_values:
            self.cards.append([value_dict.get(idx, str(idx)), suit])

    def __repr__(self):
        rep = str(self.cards)
        return rep


class Deck(Card):
    num_of_cards = 52

    # def __init__(self, card_type):
    #     print(card_type)

    def shuffle(self):
        pass
