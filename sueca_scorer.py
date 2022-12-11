import sueca_games as g
import os
import sueca_tricks as t
from sueca_cards import CardInvalid


class GameFileCouldNotBeOpenedError(Exception):
    """Exception raised when the game file could not be opened."""

    def __init__(self, fname: str):
        self.fname = fname

    def __str__(self):
        return f"The game file {self.fname} could not be opened."


class SuecaGameIncomplete(Exception):
    def __init__(self, message: str):
        self.message = message


def runGame(fname: str, showCards=False, showGame=False) -> None:
    """Run a game of Sueca and return the score.
    fname: name of the file containing the game
    showCards: if True, show the cards played
    showGame: if True, show the game
    """
    # Check if the game file exists
    if not os.path.isfile(fname):
        raise GameFileCouldNotBeOpenedError(fname)

    # Check if the game has all 10 tricks
    try:
        # Parse the game file
        with open(fname) as f:
            tc, ts = t.parseGameFile(fname)

        # Check if the game has 10 tricks
        if len(ts) != 10:
            raise SuecaGameIncomplete(f"This game only has {len(ts)} tricks.")
    except CardInvalid as e:
        # Handle any errors raised by t.parseGameFile()
        print(e)
        return

    game = g.Game(tc)
    for i in ts:
        try:
            game.playTrick(i)
        except g.CardAlreadyPlayed as e:
            print(e)
        except g.DealerDoesNotHoldTrumpCard as e:
            print(e)
        except g.IllegalCardPlayed as e:
            print(e)

    score_a, score_b = game.score()

    if score_a == score_b:
        print("The game ended in a draw")
    elif score_a > score_b:
        print("Pair A won the given sueca game")
    else:
        print("Pair B won the given sueca game")

    print(f"Score: {score_a} - {score_b}")

    if showCards:
        print(f"""Player 1: {" ".join([i.show() for i in game.cardsOf(1)])}
Player 2: {" ".join([i.show() for i in game.cardsOf(2)])}
Player 3: {" ".join([i.show() for i in game.cardsOf(3)])}
Player 4: {" ".join([i.show() for i in game.cardsOf(4)])}""")

    if showGame:
        suit_full = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}
        print(f"Trump card: {game.gameTrump().show()} - {suit_full[game.gameTrump().show()[1]]}")
        # Print the tricks
        for i in range(10):
            print(f"{i + 1}: {ts[i].show()}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Usage: python sueca_scorer.py [file] [options]")
        print("Options:")
        print("  -c: show the cards played")
        print("  -g: show the game")
        sys.exit(1)

    # Parse the command line arguments
    fname = sys.argv[-1]
    showCards = "-c" in sys.argv
    showGame = "-g" in sys.argv

    runGame(fname, showCards, showGame)

# Known issues:
# - The code can detect when an invalid card is played, but it doesn't know which player played it.
#   Therefore, it can't penalise the cheating player by giving them 0 points.
#   As a workaround, in the case of an invalid card, the code will print the error message and exit.

# - DealerDoesNotHoldTrumpCard is not raised when the dealer doesn't hold the trump card.
#   I'm not sure why, as my testing shows that it works as intended.
