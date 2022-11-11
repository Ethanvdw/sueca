import sueca_suits_ranks as ssr

def parse_card(cs: str) -> object:
    '''
    Parse a card string into a card object
    '''
    if ssr.valid_rank(cs[0]) and ssr.valid_suit(cs[1]):
        return Card(cs)
    raise Exception("CardInvalid")


class Card:

    card_rank = None
    card_suit = None

    def __init__(self, cs: str):
        '''
        Initializes the card with the card string cs.
        '''
        self.card_rank = cs[0]
        self.card_suit = cs[1]



    def points(self):
        '''
        Return the points associated with the current card self, which is linked to the points associated with the rank of the card.
        '''
        return ssr.rank_points(self.card_rank)


    def higher_than(self, other: object, s: str, t: str) -> bool:
        '''
        Returns whether the card self card is higher than the other card, with respect to the lead suit s and trump suit t.        
        '''
        # This is a very verbose way of doing this. I want to find a more elegant way of doing this if time permits.
        # If trump cards are played
        if self.card_suit == t and other.card_suit != t:
            return True
        elif self.card_suit != t and other.card_suit == t:
            return False
        elif self.card_suit == t and other.card_suit == t:
            return ssr.rank_higher_than(self.card_rank, other.card_rank)
        
        # If lead cards are played
        elif self.card_suit == s and other.card_suit != s:
            return True
        elif self.card_suit != s and other.card_suit == s:
            return False
        elif self.card_suit == s and other.card_suit == s:
            return ssr.rank_higher_than(self.card_rank, other.card_rank)
        else:
            return False

    def show(self):
        '''
        Gives the string representation of the card.
        '''
        return self.card_rank + self.card_suit


'''
TODO: Move this to a dedicated test file

def higher_than_tester():
    # In this test, the trump suit is 'C' and the lead suit is 'D'
    
    # Card 1 is a trump card, card 2 is not
    assert parse_card('AC').higher_than(parse_card('AH'), 'D', 'C') == True
    # Card 2 is a trump card, card 1 is not
    assert parse_card('AH').higher_than(parse_card('AC'), 'D', 'C') == False
    # Both cards are trump cards, but card 1 is a more valuable card
    assert parse_card('AC').higher_than(parse_card('7C'), 'D', 'C') == True
    # Both cards are trump cards, but card 1 is a less valuable card
    assert parse_card('7C').higher_than(parse_card('AC'), 'D', 'C') == False

    # Card 1 is a lead card, card 2 is not
    assert parse_card('AD').higher_than(parse_card('AH'), 'D', 'C') == True
    # Card 2 is a lead card, card 1 is not
    assert parse_card('AH').higher_than(parse_card('AD'), 'D', 'C') == False

    # Both cards are lead cards, but card 1 is a more valuable card
    assert parse_card('AD').higher_than(parse_card('7D'), 'D', 'C') == True
    # Both cards are lead cards, but card 1 is a less valuable card
    assert parse_card('7D').higher_than(parse_card('AD'), 'D', 'C') == False

    # Neither card is a trump card nor a lead card
    assert parse_card('AH').higher_than(parse_card('AD'), 'D', 'C') == False

higher_than_tester()
'''