import random
from deck import Stack


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
        tmp_stack = Stack("Spades")
        tmp_stack.shuffle()

        for card in tmp_stack.cards:
            spider.append(card)

    print(type(spider))
    random.shuffle(spider)

    for x in range(len(spider)):
        print(spider[x].str_val, ' of ', spider[x].suit, spider[x].global_id)

    exit()
