class Game():
    trump = None
    tricks = []
    odd_team = 0
    even_team = 0

    def __init__(self, trump):
        self.trump = trump

    def game_trump(self):
        """
        Returns the game's trump card as an instance of class Card.
        """
        return self.trump

    def score(self):
        """
        Returns a pairs o pair with the points won by each player pair.
        (odds and evens)
        """
        for trick in self.tricks:
            if trick.trick_winner(self.trump.suit) % 2 == 0:
                self.even_team += trick.points()
            else:
                self.odd_team += trick.points()
        return self.odd_team, self.even_team

    def play_trick(self, t):
        """
        Adds the given trick t to the current game.
        The following exceptions should be raised:
        - CardAlreadyPlayed if a trick contains a card played in a previous trick.
        - DealerDoesNotHoldTrumpCard if player 2 did not actually hold the trump card.
        - IllegalCardPlayed if a card played in some round is illegal with respect to the lead suit, which caters for
            the illegal cuts problem.
        """

        if t in self.tricks:
            raise Exception('CardAlreadyPlayed')
        if t.trick_winner(self.trump.suit) != 2:
            raise Exception('DealerDoesNotHoldTrumpCard')
        # Check if a card is played in a round that is illegal with respect to the lead suit
        # A card is illegal if it is not the lead suit, but they have a lead suit card in their hand
        # TODO - Implement this
        # When a card is played that is not of the lead or trump suit, check if they have a card of the lead suit in their hand
        # If they do, raise an exception
        # We can use the cards_of method to get the cards of a player
        for i in range(0, 4):
            if t.trick_cards[i].suit != t.trick_cards[0].suit or t.trick_cards[i].suit != self.trump.suit:
                if t.trick_cards[i] in self.cards_of(i + 1):
                    raise Exception('IllegalCardPlayed')
        self.tricks.append(t)

    def cards_of(self, p):
        """
        Returns a list of the cards held by player p.
        Exception ValueError if p is not a valid player.
        """
        if p not in range(1, 5):
            raise ValueError(f'{p} is not a valid player')
        return [card for card in self.tricks if card.player == p]

    def game_tricks(self):
        """
        Returns a list of the tricks played in the game.
        """
        return self.tricks
