import random
import base64
import hashlib
from deck import Card, Deck, Stack


def get_card():
    my_suit = random.randrange(1, 5, 1)
    my_card = random.randrange(1, 14, 1)

    if my_suit == 1:
        my_suit = 'Spades'
    elif my_suit == 2:
        my_suit = 'Clubs'
    elif my_suit == 3:
        my_suit = 'Hearts'
    elif my_suit == 4:
        my_suit = 'Diamonds'

    if my_card == 1:
        my_card = 'Ace'
    elif my_card == 11:
        my_card = 'Jack'
    elif my_card == 12:
        my_card = 'Queen'
    elif my_card == 13:
        my_card = 'King'

    print(f'Card {my_card} of {my_suit}')


if __name__ == '__main__':
    #
    # my_deck = Deck()
    # print (my_deck)
    # for card in my_deck.cards[0:53]:
    #     print(card.str_val + ' of ' + card.suit)
    #
    # print('==================================')
    #
    # my_deck.shuffle()
    #
    # for card in my_deck.cards[0:53]:
    #     print(card.str_val + ' of ' + card.suit)

    print('==================================')

    my_stack = Stack('Hearts')
    for card in my_stack.cards[0:14]:
        print(card.str_val + ' of ' + card.suit)

    print()
    print (my_stack)
    print()

    my_stack.shuffle()
    print('==================================')

    for card in my_stack.cards[0:14]:
        print(card.str_val + ' of ' + card.suit)


    exit()





    # my_stack1 = Stack('Spades')
    # print (my_stack1)
    # my_stack2 = Stack('Diamonds')
    # my_stack3 = Stack('Clubs')
    # print (type(my_stack.cards), len(my_stack.cards))
    # print()

    for x in range(1, 14):
        print()
        print(my_stack.cards[x].id, my_stack.cards[x].global_id, my_stack.cards[x].str_val, my_stack.cards[x].suit_glyph)
        print(my_stack1.cards[x].id, my_stack1.cards[x].global_id, my_stack1.cards[x].str_val, my_stack1.cards[x].suit_glyph)
        print(my_stack2.cards[x].id, my_stack2.cards[x].global_id, my_stack2.cards[x].str_val, my_stack2.cards[x].suit_glyph)

    exit()


    message = "Python is fun"

    message_bytes = message.encode('utf-8')

    print(type(message_bytes))
    print(type(message))

    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')

    print(base64_message)
    print ('-----------------')

    message = "Python"

    message_bytes = message.encode('utf-8')

    print(type(message_bytes))
    print(type(message))

    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')

    print(base64_message)

    jim = '\xF0\x9F\x98\x81'
    jim_bytes = jim.encode('utf-8')

    print(jim)
    print(jim_bytes)
    print (jim_bytes.decode('utf-8'))
    print()



    #
    # jim = 'A'
    # print(bytes(ord('A'.encode('utf-8'))))

    exit()

    print (chr(128013))

    print(b'e')
    exit()

    spider = []

    jim = Card('Heart', 2, 'jim')
    print(jim)
    exit()

    # Create 8 Random Stacks
    for x in range(1, 9):
        spider.append(Stack('Spades'))

    # Create a single pack from the Stacks
    full_pack = []
    for x in spider:
        for card in x.cards:
            full_pack.append(card)

    print(full_pack)
    print(type(full_pack))
    print(len(full_pack))


    # Deal out 10 piles
    # 4 Piles of 6 and 6 Piles of 5
    # Total of 54 cards

    for x in range(1, 5):
        for y in range(1, 7):
            print(x, y)

    for x in range(1, 7):
        for y in range(1, 6):
            print(x, y)


    exit()
    game = {'pile1': [],
            'pile2': []
            }

    for idx, card in enumerate(full_pack):
        print (idx, card)


    exit()


    # Create a draw pile of 50 cards
    # 10 cards for 5 draws


    exit()

    my_card1 = Card("Clubs", "Ace", "random")
    my_card2 = Card("Hearts", "King", "random")

    print(my_card1)
    print(my_card2)
    print()


