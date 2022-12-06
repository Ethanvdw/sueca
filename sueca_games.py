class Game:
    player_order = {
        1: [1, 2, 3, 4],
        2: [2, 3, 4, 1],
        3: [3, 4, 1, 3],
        4: [4, 1, 2, 3]
    }

    def __init__(self, trump):
        self.trump = trump
        self.tricks = []

    def game_trump(self):
        """
        Returns the game's trump card as an instance of class Card.
        """
        return self.trump

    def score(self):
        """
        Returns a pairs with the points won by each player pair.
        (odds and evens)
        """

        odd = 0
        even = 0
        for trick in self.tricks:
            turn_order = self.player_order.get(1)
            if trick is not self.tricks[0]:
                turn_order = self.player_order.get(self.tricks[-1].trick_winner(self.trump.suit))

            winner = turn_order.index(trick.trick_winner(self.trump.suit))

            # If the winner is odd, add the points to the odd score
            if winner % 2 == 0:
                odd += trick.points()
            else:
                even += trick.points()

        return odd, even






    def playTrick(self, t):
        """
        Adds the given trick t to the current game.
        The following exceptions should be raised:
        - CardAlreadyPlayed if a trick contains a card played in a previous trick.
        - DealerDoesNotHoldTrumpCard if player 2 did not actually hold the trump card.
        - IllegalCardPlayed if a card played in some round is illegal with respect to the lead suit, which caters for
            the illegal cut problem.
        """
        # Check the length of the trick_list
        if len(self.tricks) == 0:
            turn_order = self.player_order[1]
        else:
            turn_order = self.player_order[self.tricks[-1].trick_winner(self.trump.suit)]

        if t in self.tricks:
            raise Exception('CardAlreadyPlayed')
        # Check the trick winner was player 2
        # if t.trick_winner(self.trump.suit) != turn_order[1]:
        #     raise Exception('DealerDoesNotHoldTrumpCard')
        # If the winning card is the trump card, check the dealer played it
        if t.trick_winner(self.trump.suit) == 0 and turn_order[0] != 2:
            raise Exception('DealerDoesNotHoldTrumpCard')

        # Check if a card is played in a round that is illegal with respect to the lead suit
        # A card is illegal if it is not the lead suit, but they have a lead suit card in their hand

        # When a card is played that is not of the lead or trump suit,
        # check if they have a card of the lead suit in their hand
        for i in range(4):
            if (t.trick_cards[i].suit != t.trick_cards[0].suit or t.trick_cards[i].suit != self.trump.suit) and \
                    t.trick_cards[i] in self.cards_of(i + 1):
                raise Exception('IllegalCardPlayed')
        self.tricks.append(t)

    def cards_of(self, p):
        """
        Returns a list of the cards held by player p.
        Exception ValueError if p is not a valid player.
        """
        if p not in range(1, 5):
            raise ValueError(f'{p} is not a valid player')

        return [trick.trick_cards[p - 1] for trick in self.tricks]

    def game_tricks(self):
        """
        Returns a list of the tricks played in the game.
        """
        return self.tricks
