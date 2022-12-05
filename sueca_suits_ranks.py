def valid_suit(s: str) -> bool:
    """
    Returns whether the suit s is valid.
    """
    return s in {'C', 'D', 'H', 'S'}


def valid_rank(r):
    """
    Returns whether the rank r is valid in Sueca.

    Valid ranks in Sueca are:
    - '2'
    - '3'
    - '4'
    - '5'
    - '6'
    - 'Q' (Queen)
    - 'J' (Jack)
    - 'K' (King)
    - '7'
    - 'A' (Ace)
    """
    
    return r in {'2', '3', '4', '5', '6', 'Q', 'J', 'K', '7', 'A'}


def suit_full_name(s):
    """
    Returns the full name of the suit s.
    """
    suit_names = {
        'C': 'Clubs',
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades'
    }

    if s in suit_names:
        return suit_names[s]

    raise ValueError(f'Invalid suit symbol {s}')


def rank_points(r):
    """
    Returns the points associated with the rank r.

    In Sueca, the points associated with each rank are:
    Ace = 11
    7 = 10
    King = 4
    Jack = 3
    Queen = 2
    All other ranks = 0
    """

    points = {
        'A': 11,
        '7': 10,
        'K': 4,
        'J': 3,
        'Q': 2,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
    }
    if r in points:
        return points[r]
    raise ValueError(f'Invalid rank symbol {r}')


def rank_higher_than(r1, r2):
    """
    Returns whether the rank r1 is higher than the rank r2.
    """
    return rank_points(r1) > rank_points(r2)
