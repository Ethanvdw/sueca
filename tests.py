import card

def test_higher_than():
    '''
    Tests card.higher_than
    '''
    # Let the lead suit be Clubs and the trump suit be Spades
    lead_suit = 'C'
    trump_suit = 'S'

    # 1. Two trump cards. The higher rank wins.
    assert Card('AS').higher_than(Card('KS'), lead_suit, trump_suit) == True
    assert Card('KS').higher_than(Card('AS'), lead_suit, trump_suit) == False

    # 2. Two lead cards. The higher rank wins.
    assert Card('AC').higher_than(Card('KC'), lead_suit, trump_suit) == True
    assert Card('KC').higher_than(Card('AC'), lead_suit, trump_suit) == False

    # 3. One trump and one lead card. The trump wins.
    assert Card('AS').higher_than(Card('KC'), lead_suit, trump_suit) == True
    assert Card('KC').higher_than(Card('AS'), lead_suit, trump_suit) == False

    # 4. One trump and one non-trump card. The trump wins.
    assert Card('AS').higher_than(Card('KD'), lead_suit, trump_suit) == True
    assert Card('KD').higher_than(Card('AS'), lead_suit, trump_suit) == False

    # 5. One lead and one non-lead card. The lead wins.
    assert Card('AC').higher_than(Card('KD'), lead_suit, trump_suit) == True
    assert Card('KD').higher_than(Card('AC'), lead_suit, trump_suit) == False

    # 6. Two non-trump, non-lead cards. No card wins.
    assert Card('AD').higher_than(Card('KD'), lead_suit, trump_suit) == False
    assert Card('KD').higher_than(Card('AD'), lead_suit, trump_suit) == False

test_higher_than()