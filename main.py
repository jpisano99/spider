import random
import time
from deck import Stack, Pile, Deck, Card

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

    #
    # Create 10 piles (4 piles of 6 cards and 6 piles of 5 cards)
    #
    spider_piles = []
    for x in range(0, 4):
        spider_piles.append(Pile(spider_deck, 6))

    for x in range(0, 6):
        spider_piles.append(Pile(spider_deck, 5))

    print()
    print('Created ', len(spider_piles), ' piles')
    print ("Cards Remaining: ", len(spider_deck))
    print()

    return spider_deck, spider_piles


def find_match(matching_run, spider_piles):
    # Find the highest visible cards we can sequence
    print('Matching Search Run: ', matching_run)

    #
    # Find the first highest sequence on the board
    #
    # src_card_val = 0
    src_card = None
    # src_card_pile = None

    for pile_num, this_pile in enumerate(spider_piles):

        # Get the last Sequence in this pile
        print('\tPile number: ', pile_num, 'has this sequence to match', this_pile.sequences[len(this_pile.sequences)-1])
        seq_to_use_for_match = this_pile.sequences[len(this_pile.sequences)-1]

        # Get the card to use for this match attempt
        src_card = seq_to_use_for_match[0]

        print("\tSpecific card to use for match is " + src_card.str_val + ' of ', src_card.suit)

        exit()

        # this_card = this_pile.get_top_card()
        # # this_pile.reveal_pile()

        # print ("\tPile  ", this_pile.pile_id, ' has ', len(this_pile.cards), ' cards', '\t', this_card)
        # print("\tPile  ", this_pile.pile_id, ' has ', len(this_pile.sequences), ' sequences', '\t', this_card.str_val, ' of ', this_card.suit)

        if this_card.int_value > src_card_val:
            src_card_val = this_card.int_value
            src_card_pile = this_pile
            src_card = this_card

    #print ('\t\t High card', src_card)

    #
    # Find the next highest card and see if its a match
    #
    dest_card_val = 0
    dest_card = None
    dest_card_pile = None

    for pile_num, this_pile in enumerate(spider_piles):
        this_card = this_pile.get_top_card()

        if this_card.int_value >= src_card_val:
            continue
        elif this_card.int_value > dest_card_val:
            # This is now the potential dest card
            dest_card_val = this_card.int_value
            dest_card = this_card
            dest_card_pile = this_pile

    print()
    print('\tSource Card id ', src_card, ' in pile ', str(src_card_pile.pile_id))
    print('\tPotential Dest Card id ', dest_card, ' in pile ', str(dest_card_pile.pile_id))

    if dest_card_val + 1 == src_card_val:
        print('\tWe have a MATCH to Move')
        # card_move(src_card_pile, src_card, dest_card_pile, dest_card)
        do_again = True
    else:
        print('NO MATCH try again !')
        do_again = False

    # this_pile.reveal_pile()

    # Move Card to new pile
    # spider_piles

    print()
    return do_again


def show_piles(spider_piles):
    for this_pile in spider_piles:
        this_pile.reveal_pile()
        print()
    return


def card_move(src_card_pile, src_card, dest_card_pile, dest_card):
    tmp_card = dest_card_pile.remove_card(dest_card)
    src_card_pile.add_card(tmp_card)

    src_card_pile.reveal_pile()
    dest_card_pile.reveal_pile()

    print('removed ', tmp_card)
    return


if __name__ == '__main__':

    spider_deck, spider_piles = setup()

    show_piles(spider_piles)
    print(spider_piles[9].pile_id)
    print(spider_piles[9].cards)

    for x in range(0, 4):
        if find_match(x, spider_piles) is False:
            break

