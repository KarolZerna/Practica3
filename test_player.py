import unittest
from person import * 
from board import *
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.playerPos = [1,1]
        self.score = 0
        self.lives = 3
        self.x = 19
        self.y = 5

    def test_checkPos_pos(self):
        self.assertEqual(Player.checkPos(self, self.x, self.y), 1)

    def test_checkPos_neg(self):
        self.assertIsNot(Player.checkPos(self, self.x, self.y), -1)

        
if __name__ == '__main__':
    unittest.main()