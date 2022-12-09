def valid_suit(s: str) -> bool:
    """
    Returns whether the suit s is valid.
    """
    return s in {'C', 'D', 'H', 'S'}


def valid_rank(r: str) -> bool:
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


def suit_full_name(s: str) -> str:
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


def rank_points(r: str) -> int:
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


def rank_higher_than(r1: str, r2: str) -> bool:
    """
    Returns whether the rank r1 is higher than the rank r2.
    """
    # Lowest rank is 2
    # Highest rank is Ace
    rank_order = ['2', '3', '4', '5', '6', 'Q', 'J', 'K', '7', 'A']

    try:
        return rank_order.index(r1) > rank_order.index(r2)
    except ValueError as e:
        # Find which rank is invalid
        if r1 not in rank_order:
            raise ValueError(f'Invalid rank symbol {r1}') from e
        else:
            raise ValueError(f'Invalid rank symbol {r2}') from e
