from sueca_cards import Card, parseCard
from sueca_tricks import Trick
import sueca_suits_ranks as ssr


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
        turn_orders = {
            1: [1, 2, 3, 4],
            2: [2, 3, 4, 1],
            3: [3, 4, 1, 2],
            4: [4, 1, 2, 3]
        }
        current_turn = turn_orders[self.starting_player]
        # # --- Adding to player_cards
        # # Append the cards to the player_cards dict
        # # In the order of the turn
        # # IE: Add the first card to player 1, then 2, then 3, then 4
        for i in range(4):
            self.player_cards[current_turn[i]].append(t.trick_cards[i])



        # --- Exceptions ---
        # Check the length of the trick_list
        if t in self.tricks:
            raise CardAlreadyPlayed(f'Trick {t} has already been played')
        # Check the trick winner was player 2
        # TODO: this is currently broken. Reimplement with cards_of()
        # if t.trick_winner(self.trump.suit) == 0 and self.trump not in t.trick_cards:
        #     raise DealerDoesNotHoldTrumpCard('Player 2 did not hold the trump card')
        if self.gameTrump() in t.trick_cards and t.trick_winner(self.gameTrump().suit) != current_turn[0]:
            raise DealerDoesNotHoldTrumpCard('Player 2 did not hold the trump card')


        # Check if a card is played in a round that is illegal with respect to the lead suit
        # A card is illegal if it is not the lead suit but the player has a card of the lead suit in their hand
        # for i in range(4):
        #     if t.trick_cards[i].suit != t.trick_cards[0].suit and t.trick_cards[0].suit in [card.suit for card in self.player_cards[current_turn[i]]]:
        #         raise IllegalCardPlayed(f'Player {current_turn[i]} played an illegal card')
        # TODO: This doesn't work. I don't think I can fix it without changing the way I store the cards
        # I don't think I'll be able to fix this in time



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
