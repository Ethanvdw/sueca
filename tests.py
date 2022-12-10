import unittest
import sueca_suits_ranks as ssr
import sueca_cards as c
import sueca_tricks as t
import sueca_games as g


# Uses examples from https://now.ntu.ac.uk/d2l/le/content/891619/viewContent/9837391/View


class TestSuecaSuitsRanks(unittest.TestCase):
    def test_valid_suite(self):
        self.assertTrue(ssr.valid_suit('C'))
        self.assertTrue(ssr.valid_suit('S'))
        self.assertFalse(ssr.valid_suit('P'))

    def test_valid_rank(self):
        self.assertTrue(ssr.valid_rank('3'))
        self.assertTrue(ssr.valid_rank('7'))
        self.assertFalse(ssr.valid_rank('8'))

    def test_rank_points(self):
        self.assertEqual(ssr.rank_points('A'), 11)
        self.assertEqual(ssr.rank_points('7'), 10)
        self.assertEqual(ssr.rank_points('5'), 0)
        self.assertRaises(ValueError, ssr.rank_points, '9')

    def test_rank_higher_than(self):
        self.assertTrue(ssr.rank_higher_than('6', '3'))
        self.assertTrue(ssr.rank_higher_than('K', 'Q'))
        self.assertFalse(ssr.rank_higher_than('2', '3'))
        self.assertTrue(ssr.rank_higher_than('3', '2'))
        self.assertFalse(ssr.rank_higher_than('J', '7'))
        self.assertFalse(ssr.rank_higher_than('4', '4'))
        self.assertRaises(ValueError, ssr.rank_higher_than, '8', '7')


class TestCard(unittest.TestCase):
    def test_card_show(self):
        self.assertEqual(c.parseCard('2C').show(), '2C')
        self.assertRaises(Exception, c.parseCard, '8C')
        self.assertRaises(Exception, c.parseCard, 'QSD')
        self.assertRaises(Exception, c.parseCard, '7Q')
        self.assertRaises(Exception, c.parseCard, '8S')

    def test_card_points(self):
        self.assertEqual(c.parseCard('2C').points(), 0)
        self.assertEqual(c.parseCard('KS').points(), 4)
        self.assertRaises(Exception, c.parseCard, '9D')

    def test_card_higher_than(self):
        self.assertTrue(c.parseCard('KS').higher_than(c.parseCard('2C'), "S", "D"))
        self.assertTrue(c.parseCard('KS').higher_than(c.parseCard('JS'), "S", "D"))
        self.assertTrue(c.parseCard('6S').higher_than(c.parseCard('5S'), "S", "H"))
        self.assertFalse(c.parseCard('KS').higher_than(c.parseCard('2D'), "S", "D"))
        self.assertFalse(c.parseCard('7S').higher_than(c.parseCard('2C'), "C", "D"))


class TestTrick(unittest.TestCase):
    def test_trick_show(self):
        self.assertEqual(t.parseTrick("AH 2D 5H 2H").show(), "AH 2D 5H 2H")
        self.assertRaises(Exception, t.parseTrick, "AH 2D 5H 8H")
        self.assertRaises(ValueError, t.parseTrick, "AS 2S 7S JS 5S")

    def test_trick_points(self):
        self.assertEqual(t.parseTrick("AH 2D 5H 2H").points(), 11)
        self.assertEqual(t.parseTrick("AS 2S 7S JS").points(), 24)
        ts = t.parseGameFile("game1.sueca")[1]
        correct_scores = [11, 15, 11, 13, 13, 20, 10, 14, 10, 3]
        for position, i in enumerate(ts):
            self.assertEqual(i.points(), correct_scores[position])

    def test_trick_winner(self):
        self.assertEqual(t.parseTrick("AH 2D 5H 2H").trick_winner("D"), 2)
        self.assertEqual(t.parseTrick("AS 2S 7S JS").trick_winner("D"), 1)
        self.assertEqual(t.parseTrick("5C 6S 6H JS").trick_winner("D"), 1)
        self.assertEqual(t.parseTrick("5C 6S 6H JS").trick_winner("S"), 4)
        self.assertEqual(t.parseTrick("5C 6S 6H JS").trick_winner("H"), 3)
        self.assertEqual(t.parseTrick("5C 6S 6H JS").trick_winner("C"), 1)
        self.assertEqual(t.parseTrick("5C 6S 6H JS").trick_winner("C"), 1)
        tc, ts = t.parseGameFile("game1.sueca")
        self.assertEqual(tc.show(), "7D")
        self.assertEqual(ts[0].show(), "AH 2D 5H 2H")
        self.assertEqual(ts[1].show(), "AC 3D 4C KC")
        self.assertEqual(ts[-1].show(), "5C 6S 6H JS")
        self.assertEqual(t.parseTrick("QS KS 7S 6S").trick_winner("C"), 3)

    def test_parse_game(self):
        tc, ts = t.parseGameFile("game1.sueca")
        self.assertEqual(tc.show(), "7D")
        self.assertEqual(ts[0].show(), "AH 2D 5H 2H")
        self.assertEqual(ts[-1].show(), "5C 6S 6H JS")


class TestGame(unittest.TestCase):
    def test_game_trump(self):
        tc, ts = t.parseGameFile("game1.sueca")
        g1 = g.Game(tc)
        self.assertEqual(g1.gameTrump().show(), "7D")

    def test_play_tricks(self):
        tc, ts = t.parseGameFile("game1.sueca")
        g1 = g.Game(tc)
        g1.playTrick(ts[0])
        # Use assertEqual to see if g1.score() outputs (0, 11)
        self.assertEqual(g1.score(), (0, 11))

    def test_cards_of(self):
        tc, ts = t.parseGameFile("game1.sueca")
        g1 = g.Game(tc)
        for i in ts:
            g1.playTrick(i)
        self.assertEqual(g1.cardsOf(1)[0].show(), "AH")
        self.assertEqual(g1.cardsOf(2)[0].show(), "2D")
        self.assertEqual(g1.cardsOf(1)[-1].show(), "5C")
        self.assertEqual(g1.cardsOf(2)[-1].show(), "6S")
        self.assertRaises(ValueError, g1.cardsOf, 5)

    def test_score(self):
        tc, ts = t.parseGameFile("game1.sueca")
        g1 = g.Game(tc)
        # self.assertEqual(g1.score(), (0, 0))
        g1.playTrick(ts[0])
        # self.assertEqual(g1.score(), (0, 11))
        g1.playTrick(ts[1])
        #
        # self.assertEqual(g1.score(), (15, 11))

        for t1 in ts[2:]:
            g1.playTrick(t1)
        self.assertEqual(g1.gameTricks()[-1].show(), "5C 6S 6H JS")
        print("Pause")
        self.assertEqual(g1.score(), (76, 44))


if __name__ == '__main__':
    unittest.main()
