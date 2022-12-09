import sueca_cards as c


def parseTrick(cs: str) -> 'Trick':
    """
    Takes a trick string and returns a trick object
    A trick object is a list of card objects
    """
    # Split the string into a list of card strings
    cards = cs.split(' ')
    if len(cards) != 4:
        raise ValueError(f"TrickInvalid:Trick {cs} is not valid. \n"
                         f"A trick string representation must have 4 cards")
    # Parse each card string into a card object
    parsed_cards = [c.parseCard(i) for i in cards]
    return Trick(parsed_cards)


# Takes a file name string, and returns a trump card and a list of trick objects

def parseGameFile(file_name : str) -> 'tuple':
    # Open the file
    with open(file_name, 'r') as f:
        # The trick string is the first line of the file
        trick = f.readline().strip()
        # The cards are the rest of the lines
        cards = [line.strip() for line in f.readlines()]
    # Return the trump as a card object, and the tricks as a list of trick objects
    return c.parseCard(trick), [parseTrick(i) for i in cards]


class Trick:
    """
    A trick contains 4 cards and a trump card.
    """

    def __init__(self, cs: list) -> None:
        """
        Initializes the trick with the trick string cs.
        """
        self.trick_cards = cs

    def points(self) -> int:
        """
        Gives the points associated with the trick.
        """
        # This is calculated by summing the points of each card in the trick.
        return sum(card.points() for card in self.trick_cards)

    def trick_winner(self, trump: str) -> int:
        """
        Computes the winner of the trick, given the trump card.
        """
        # By default, the first card is the winner
        winner = self.trick_cards[0]
        # Iterate over the rest of the cards
        for card in self.trick_cards[1:]:
            # If the card is higher than the current winner, it becomes the new winner
            if card.higher_than(winner, self.trick_cards[0].suit, trump):
                winner = card
        # Return the winner
        return self.trick_cards.index(winner) + 1

    def show(self) -> str:
        """
        Gives the string representation of the trick.
        """
        return ' '.join([card.show() for card in self.trick_cards])
