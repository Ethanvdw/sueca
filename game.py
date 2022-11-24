from card import *


class Game:

    def __init__(self):
        pass

    def game_trump(self):
        """
        Returns the game's trump card as in instance of class Card.
        """

    def score(self):
        """
        Returns a tuple with the points won by each pair in the current game.
        """
        pass

    def play_trick(self, t):
        """
        Adds the given trick t (an instance of class Trick) to the current game.
        The following exceptions may be raised:
        - CardAlreadyPlayed if a trick contains a card played in a previous round of the game.
        - DealerDoesNotHoldTrumpCard if player 2 (the dealer) did not actually hold the game's trump card.
        - IllegalCardPlayed if a card played in some round is illegal with respect to the lead suit, which caters for
          the illegal cuts problem.
        """
        pass

    def cards_of(self, p):
        """
        Returns a list of card instances held by player p (an integer between 1 and 4) in the current game.
        Exception "ValueError" should be raised if the given player number is not valid.
        """
        pass

    def game_tricks(self):
        pass
