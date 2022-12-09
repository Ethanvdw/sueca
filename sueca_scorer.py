import sueca_games as g
import os
import sueca_tricks as t


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
    tc, ts = t.parseGameFile("game1.sueca")
    if len(ts) != 10:
        raise SuecaGameIncomplete(f"This game only has {len(ts)} tricks.")

    game = g.Game(tc)
    # fixer = 5
    for i in ts:
        game.playTrick(i)

    score_a, score_b = game.score()
    # score_a += fixer
    # score_b -= fixer
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
