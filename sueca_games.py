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

        self.odd = 0
        self.even = 0

        self.player_cards = {
            1: [],
            2: [],
            3: [],
            4: []
        }

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
        # --- Checking who played which card
        turn_orders = [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]
        current_turn = turn_orders[self.starting_player - 1]

        # # --- Adding to player_cards
        # # Append the cards to the player_cards dict
        # # In the order of the turn
        # # IE: Add the first card to player 1, then 2, then 3, then 4
        for i, player in enumerate(current_turn):
            self.player_cards[player].append(t.trick_cards[i])

        # --- Exceptions ---
        if t in self.tricks:
            raise CardAlreadyPlayed(f'Trick {t} has already been played')

        if self.gameTrump() in t.trick_cards and t.trick_winner( self.gameTrump().suit) != current_turn[0]:
            raise DealerDoesNotHoldTrumpCard('Player 2 did not hold the trump card')

        for i, player in enumerate(current_turn):
            # If the player is not the first player
            if i != 0 and t.trick_cards[0] in self.player_cards[player] and t.trick_cards[i] != t.trick_cards[0]:
                raise IllegalCardPlayed(f'Player {player} played an illegal card')

        self.tricks.append(t)

        # --- Calculating player points ---
        winning_player = (t.trick_winner(self.trump.suit) + self.starting_player - 1) % 4
        self.starting_player = winning_player

        # I could do points = t.points() to help performance slightly, but in my profiling the difference is negligible.
        self.even += t.points() if winning_player % 2 == 0 else 0
        self.odd += t.points() if winning_player % 2 != 0 else 0

    def cardsOf(self, p: int) -> list:
        """
        Returns a list of the cards held by player p.
        Exception ValueError if p is not a valid player.
        """
        # TODO Fix this
        if p not in range(1, 5):
            raise ValueError(f'{p} is not a valid player')

        return self.player_cards[p]

    def gameTricks(self) -> list:
        """
        Returns a list of the tricks played in the game.
        """
        return self.tricks
