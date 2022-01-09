import random
from deck import Stack, Pile


def setup():
    # Build a Spider Solitaire Deck of 8 stacks (104 cards)
    spider_deck = []

    # Create 8 well shuffled Stacks
    for x in range(1, 9):
        # Create and Shuffle this one stack
        tmp_stack = Stack("Spades")
        tmp_stack.shuffle()
        for card in tmp_stack.cards:
            spider_deck.append(card)

    # Shuffle entire deck
    random.shuffle(spider_deck)

    # for x in range(len(spider_deck)):
    #     print(spider_deck[x].str_val, ' of ', spider_deck[x].suit, spider_deck[x].global_id)
    print()
    print ('This deck has '+ str(len(spider_deck)) + ' cards')

    # Create 10 piles (4 piles of 6 cards and 6 piles of 5 cards)
    spider_field = []
    for x in range(0, 4):
        spider_field.append(Pile(spider_deck, 6))

    for x in range(0, 6):
        spider_field.append(Pile(spider_deck, 5))

    print()
    print('Created ', len(spider_field), ' piles')
    print ("Cards Remaining: ", len(spider_deck))

    return


if __name__ == '__main__':
    setup()
