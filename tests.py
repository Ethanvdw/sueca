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
        self.assertFalse(ssr.rank_higher_than('6', '3'))
        self.assertTrue(ssr.rank_higher_than('K', 'Q'))
        self.assertFalse(ssr.rank_higher_than('3', '2'))
        self.assertFalse(ssr.rank_higher_than('J', '7'))
        self.assertFalse(ssr.rank_higher_than('4', '4'))
        self.assertRaises(ValueError, ssr.rank_higher_than, '8', '7')


class TestCard(unittest.TestCase):
    def test_card_show(self):
        self.assertEqual(c.parse_card('2C').show(), '2C')
        self.assertRaises(Exception, c.parse_card, '8C')
        self.assertRaises(Exception, c.parse_card, 'QSD')
        self.assertRaises(Exception, c.parse_card, '7Q')

    def test_card_points(self):
        self.assertEqual(c.parse_card('2C').points(), 0)
        self.assertEqual(c.parse_card('KS').points(), 4)
        self.assertRaises(Exception, c.parse_card, '9D')

    def test_card_higher_than(self):
        self.assertTrue(c.parse_card('KS').higher_than(c.parse_card('2C'), "S", "D"))
        self.assertTrue(c.parse_card('KS').higher_than(c.parse_card('JS'), "S", "D"))
        self.assertFalse(c.parse_card('KS').higher_than(c.parse_card('2D'), "S", "D"))
        self.assertFalse(c.parse_card('7S').higher_than(c.parse_card('2C'), "C", "D"))


class TestTrick(unittest.TestCase):
    def test_trick_show(self):
        self.assertEqual(t.parse_trick("AH 2D 5H 2H").show(), "AH 2D 5H 2H")
        self.assertRaises(Exception, t.parse_trick, "AH 2D 5H 8H")
        self.assertRaises(ValueError, t.parse_trick, "AS 2S 7S JS 5S")

    def test_trick_points(self):
        self.assertEqual(t.parse_trick("AH 2D 5H 2H").points(), 11)
        self.assertEqual(t.parse_trick("AS 2S 7S JS").points(), 24)

    def test_trick_winner(self):
        self.assertEqual(t.parse_trick("AH 2D 5H 2H").trick_winner("D"), 2)
        self.assertEqual(t.parse_trick("AS 2S 7S JS").trick_winner("D"), 1)
        self.assertEqual(t.parse_trick("5C 6S 6H JS").trick_winner("D"), 1)
        tc, ts = t.parse_game_file("game1.sueca")
        self.assertEqual(tc.show(), "7D")
        self.assertEqual(ts[0].show(), "AH 2D 5H 2H")
        self.assertEqual(ts[1].show(), "AC 3D 4C KC")
        self.assertEqual(ts[-1].show(), "5C 6S 6H JS")

    def test_parse_game(self):
        tc, ts = t.parse_game_file("game1.sueca")
        self.assertEqual(tc.show(), "7D")
        self.assertEqual(ts[0].show(), "AH 2D 5H 2H")
        self.assertEqual(ts[-1].show(), "5C 6S 6H JS")


class TestGame(unittest.TestCase):
    def test_game_trump(self):
        tc, ts = t.parse_game_file("game1.sueca")
        g1 = g.Game(tc)
        self.assertEqual(g1.game_trump().show(), "7D")

    def test_play_tricks(self):
        tc, ts = t.parse_game_file("game1.sueca")
        g1 = g.Game(tc)
        g1.play_trick(ts[0])
        # Use assertEqual to see if g1.score() outputs (0, 11)
        self.assertEqual(g1.score(), (0, 11))

if __name__ == '__main__':
    unittest.main()
