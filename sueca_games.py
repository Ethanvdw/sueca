from sueca_cards import Card
from sueca_tricks import Trick


class CardAlreadyPlayed(Exception):
    def __init__(self, message: str):
        self.message = message


class DealerDoesNotHoldTrumpCard(Exception):
    def __init__(self, message: str):
        self.message = message


class IllegalCardPlayed(Exception):
    def __init__(self, message: str):
        self.message = message


class Game:

    def __init__(self, trump: Card) -> None:
        self.trump = trump
        self.tricks = []

        self.starting_player = 1

        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []

        self.odd = 0
        self.even = 0

    def gameTrump(self) -> Card:
        """
        Returns the game's trump card as an instance of class Card.
        """
        return self.trump

    def score(self) -> tuple:
        """
        Returns a pairs with the points won by each player pair.
        (odds and evens)
        """

        return self.odd, self.even

    def playTrick(self, t: Trick) -> None:
        """
        Adds the given trick t to the current game.
        The following exceptions should be raised:
        - CardAlreadyPlayed if a trick contains a card played in a previous trick.
        - DealerDoesNotHoldTrumpCard if player 2 did not actually hold the trump card.
        - IllegalCardPlayed if a card played in some round is illegal with respect to the lead suit, which caters for
            the illegal cut problem.
        """
        # Check the length of the trick_list
        if t in self.tricks:
            raise CardAlreadyPlayed(f'Trick {t} has already been played')
        # Check the trick winner was player 2
        # if t.trick_winner(self.trump.suit) != turn_order[1]:
        #     raise Exception('DealerDoesNotHoldTrumpCard')
        # If the winning card is the trump card, check the dealer played it
        if t.trick_winner(self.trump.suit) == 0 and self.trump not in t.trick_cards:
            raise DealerDoesNotHoldTrumpCard('Player 2 did not hold the trump card')

        # Check if a card is played in a round that is illegal with respect to the lead suit
        # A card is illegal if it is not the lead suit, but they have a lead suit card in their hand

        # When a card is played that is not of the lead or trump suit,
        # check if they have a card of the lead suit in their hand
        for i in range(4):
            if (t.trick_cards[i].suit != t.trick_cards[0].suit or t.trick_cards[i].suit != self.trump.suit) and \
                    t.trick_cards[i] in self.cardsOf(i + 1):
                raise IllegalCardPlayed(f'Player {i + 1} played an illegal card')

        self.tricks.append(t)

        # --- Calculating player points ---
        winning_player = (t.trick_winner(self.trump.suit) + self.starting_player - 1) % 4
        self.starting_player = winning_player

        # I could do points = t.points() to help performance slightly, but in my profiling the difference is negligible.
        self.even += t.points() if winning_player % 2 == 0 else 0
        self.odd += t.points() if winning_player % 2 != 0 else 0

        # --- Updating player hands ---
        # TODO: After a trick has been played, work out who played which card and add it to their hand


    def cardsOf(self, p: int) -> list:
        """
        Returns a list of the cards held by player p.
        Exception ValueError if p is not a valid player.
        """
        # TODO Fix this
        if p not in range(1, 5):
            raise ValueError(f'{p} is not a valid player')

        return [trick.trick_cards[p - 1] for trick in self.tricks]

    def gameTricks(self) -> list:
        """
        Returns a list of the tricks played in the game.
        """
        return self.tricks
