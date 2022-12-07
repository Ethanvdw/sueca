import sueca_games as g
import os
import sueca_tricks as t


def GameFileCouldNotBeOpenedError(Exception):
    """Exception raised when the game file could not be opened."""

    def __init__(self, fname):
        self.fname = fname

    def __str__(self):
        return f"The game file {self.fname} could not be opened."


def runGame(fname, showCards=False, showGame=False):
    """Run a game of Sueca and return the score.
    fname: name of the file containing the game
    showCards: if True, show the cards played
    showGame: if True, show the game
    """
    # Check if the game file exists
    if not os.path.isfile(fname):
        raise GameFileCouldNotBeOpenedError(fname)

    # Check if the game has all 10 tricks
    tc, ts = t.parse_game_file("game1.sueca")
    if len(ts) != 10:
        raise GameFileCouldNotBeOpenedError(fname)

    game = g.Game(tc)
    for i in ts:
        game.play_trick(i)

    score_a, score_b = game.score()
    winner = "A" if score_a > score_b else "B"
    print(f"Pair {winner} won the given sueca game")
    print(f"Score: {score_a} - {score_b}")

    if showCards:
        suit_full = {"C": "Clubs", "D": "Diamonds", "H": "Hearts", "S": "Spades"}

        print(
            f"""Trump card: {game.game_trump().show()} - {suit_full[game.game_trump().show()[1]]}
Player 1: {" ".join([i.show() for i in game.cards_of(1)])}
Player 2: {" ".join([i.show() for i in game.cards_of(2)])}
Player 3: {" ".join([i.show() for i in game.cards_of(3)])}
Player 4: {" ".join([i.show() for i in game.cards_of(4)])}""")
    if showGame:
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
    fname = sys.argv[1]
    showCards = "-c" in sys.argv
    showGame = "-g" in sys.argv

    runGame(fname, showCards, showGame)
