import sueca_cards as c


def parse_trick(cs: str) -> object:
    """
    Takes a trick string and returns a trick object
    A trick object is a list of card objects
    """
    # Split the string into a list of card strings
    cards = cs.split(' ')
    if len(cards) != 4:
        raise ValueError(f"TrickInvalid: Trick {cs} is not valid. \n"
                         f"A trick string representation must have 4 cards")
    # Parse each card string into a card object
    parsed_cards = [c.parse_card(i) for i in cards]
    return Trick(parsed_cards)


# Takes a file name string, and returns a trump card and a list of trick objects


def parse_game_file(file_name):
    # Open the file
    with open(file_name, 'r') as f:
        # The trick string is the first line of the file
        trick = f.readline().strip()
        # The cards are the rest of the lines
        cards = [line.strip() for line in f.readlines()]
    # Return the trump as a card object, and the tricks as a list of trick objects
    return c.parse_card(trick), [parse_trick(i) for i in cards]


class Trick:

    """
    A trick contains 4 cards and a trump card.
    """

    def __init__(self, cs: list):
        """
        Initializes the trick with the trick string cs.
        """
        self.trick_cards = cs

    def points(self):
        """
        Gives the points associated with the trick.
        """
        # This is calculated by summing the points of each card in the trick.
        return sum(card.points() for card in self.trick_cards)

    def trick_winner(self, trump):
        # Compares all the cards using the higher_than method of the card class.
        # To find the winner, we need to find the card that is higher than all the other cards.
        # We can do this by comparing each card to all the other cards.

        # The lead suit is the suit of the first card in the trick.
        lead_card = self.trick_cards[0]

        # The winner is the highest value card in the trick.
        winner = self.trick_cards[0]
        for card in self.trick_cards:
            if card.higher_than(winner, lead_card, trump):
                winner = card

        # Return index of the winner
        return self.trick_cards.index(winner) + 1

    def show(self):
        """
        Gives the string representation of the trick.
        """
        return ' '.join([card.show() for card in self.trick_cards])
