from unittest import TestCase
from Game import Game


class TestGame(TestCase):
    def test_opponent(self):
        game = Game()
        self.assertEqual(game.opponent(game.max_player), game.min_player)
        self.assertEqual(game.opponent(game.min_player), game.max_player)
