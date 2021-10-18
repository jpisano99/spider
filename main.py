import random
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

    spider = []

    # Create 8 Random Stacks
    for x in range(1, 9):
        spider.append(Stack('Spades'))

    print(spider)
    print(len(spider))

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

    game = {'pile1' : []}

    for stack in range(1, 11):
        print ('pile', x)

    exit()


    # Create a draw pile of 50 cards
    # 10 cards for 5 draws


    exit()

    my_card1 = Card("Clubs", "Ace", "random")
    my_card2 = Card("Hearts", "King", "random")

    print(my_card1)
    print(my_card2)
    print()


