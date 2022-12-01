import sueca_suits_ranks as ssr


def parse_card(cs: str) -> object:
    """
    Parse a card string into a card object
    """
    if len(cs) != 2:
        raise ValueError(f"CardInvalid: Card {cs} is not valid. \n"
                        f"A card string representation must have 2 characters")

    if not ssr.valid_rank(cs[0]):
        raise ValueError(f"CardInvalid: Card {cs} is not valid. \n"
                        f"Invalid suit symbol {cs[0]}")

    if not ssr.valid_suit(cs[1]):
        raise ValueError(f"CardInvalid: Card {cs} is not valid. \n"
                        f"Invalid rank symbol {cs[1]}")

    return Card(cs)


class Card:
    rank = None
    suit = None

    def __init__(self, cs: str):
        """
        Initializes the card with the card string cs.
        """
        self.rank = cs[0]
        self.suit = cs[1]

    def points(self):
        """
        Return the points associated with the current card self, which is linked to the points associated with the rank of the card.
        """
        return ssr.rank_points(self.rank)

    def higher_than(self, other: object, s: str, t: str) -> bool:
        """
        Returns whether the card self card is higher than the other card, with respect to the lead suit s and trump suit t.
        """
        # This is a very verbose way of doing this. I want to find a more elegant way of doing this if time permits.
        # If trump cards are played
        if self.suit == t and other.suit != t:
            return True
        elif self.suit != t and other.suit == t:
            return False
        elif self.suit == t and other.suit == t:
            return ssr.rank_higher_than(self.rank, other.rank)

        # If lead cards are played
        elif self.suit == s and other.suit != s:
            return True
        elif self.suit != s and other.suit == s:
            return False
        elif self.suit == s and other.suit == s:
            return ssr.rank_higher_than(self.rank, other.rank)
        else:
            return False

    def show(self):
        """
        Gives the string representation of the card.
        """
        return self.rank + self.suit