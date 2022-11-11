import sueca_suits_ranks as ssr
from card import *

def parse_trick(cs: str) -> object:
    '''
    Takes a trick string and returns a trick object.
    '''
    # A trick is represented in the format "AH 2D 5H 2H"
    # We need to check that the trick string is valid, and if it is not, raise an exception.
    # Check if there are 4 cards in the trick
    # Split the trick string into a list of cards
    cards = cs.split()
    print(cards)
    raise Exception("TrickInvalid")
    # return Trick(cards[0], cards[1], cards[2], cards[3])

# Takes a file name string, and returns a trump card and a list of trick objects
def parse_game_file(fname: str) -> tuple:
    # Open the file
    with open(fname, 'r') as f:
        # The trick string is the first line of the file
        trick = f.readline().strip()
        # The cards are the rest of the lines
        cards = [line.strip() for line in f.readlines()]
    # Return the trump as a card object, and the trick as a trick object
    return parse_card(trick), parse_trick(cards)


class Trick:
    '''
    A trick contains 4 cards and a trump card.
    '''
    trump = None
    trick_cards = None
    def __init__(self, trump:str, cs: str):
        '''
        Initializes the trick with the trick string cs.
        '''
        self.trump = parse_card(trump)
        self.trick_cards = [parse_card(c) for c in cs.split()]

    def points(self):
        '''
        Gives the points associated with the trick.
        '''
        # This is calculated by summing the points of each card in the trick.
        return sum([c.points() for c in self.trick_cards])


    def trick_winner(self):
        # Compares all the cards using the higher_than method of the card class.
        # To find the winner, we need to find the card that is higher than all the other cards.
        # We can do this by comparing each card to all the other cards.
        
        # The lead suit is the suit of the first card in the trick.
        lead_suit = self.trick_cards[0].card_suit
        trump_suit = self.trump.card_suit

        # The winner is the highest value card in the trick.
        # TODO: THIS DOES NOT HANDLE TIES.
        winner = self.trick_cards[0]
        for card in self.trick_cards:
            if card.higher_than(winner, lead_suit, trump_suit):
                winner = card

        # Return index of the winner
        return self.trick_cards.index(winner)+1

    def show(self):
        '''
        Gives the string representation of the trick.
        '''
        return ''.join([c.show() for c in self.trick_cards])


# t1 = Trick("3D", "AH 2D 5H 2H")
# print(t1.trick_winner())
'''
TODO: Move to a dedicated test file.
def test_tricks():
    assert Trick("7D", "AH 2D 5H 2H").trick_winner() == 2
    assert Trick("7D", "AC 3D 4C KC").trick_winner() == 2
    assert Trick("7D", "AS 2S 4S 3S").trick_winner() == 1
    assert Trick("7D", "AD 4H QD 6D").trick_winner() == 1
    assert Trick("7D", "4D 7S 3H JD").trick_winner() == 4
test_tricks()
'''