import sueca_suits_ranks as ssr


def parse_card(cs):
    """
    Parse a card string into a card object
    """
    if len(cs) != 2:
        raise ValueError(f"""CardInvalid: Card {cs} is not valid.
                        A card string representation must have 2 characters""")

    if not ssr.valid_rank(cs[0]):
        raise ValueError(f"""CardInvalid: Card {cs} is not valid.
                        Invalid suit symbol {cs[0]}""")

    if not ssr.valid_suit(cs[1]):
        raise ValueError(f"""CardInvalid: Card {cs} is not valid.
                            Invalid rank symbol {cs[1]}""")

    return Card(cs)


class Card:

    def __init__(self, cs: str):
        """
        Initializes the card with the card string cs.
        """
        self.rank = cs[0]
        self.suit = cs[1]

    def points(self):
        """
        Return the points associated with the current card self,
        which is linked to the points associated with the rank of the card.
        """
        return ssr.rank_points(self.rank)

    def higher_than(self, other, s, t):
        """
        Returns whether the card self card is higher than the other card,
        with respect to the lead suit s and trump suit t.
        """
        if self.suit == t:
            return ssr.rank_higher_than(self.rank, other.rank) if other.suit == t else True
        if other.suit == t:
            return False
        if self.suit == s:
            return ssr.rank_higher_than(self.rank, other.rank) if other.suit == s else True
        return self.suit == t

    def show(self):
        """
        Gives the string representation of the card.
        """
        return self.rank + self.suit
