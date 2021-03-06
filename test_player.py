import unittest
# from person import * 
from board import *
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.playerPos = [1,1]
        self.score = 0
        self.lives = 3
        self.x = 3 #19
        self.y = 1 #5
    
    def test_drawPlayer(self):
        self.assertEqual(Player.drawPlayer(self, self.x, self.y), None)

    def test_checkPos_pos(self):
        self.assertEqual(Player.checkPos(self, self.x, self.y), 1)

    def test_checkEnemy(self):
        self.assertEqual(Player.checkEnemy(self, self.x, self.y), 1)

    def test_playerInit(self):
        self.assertEqual(Player.playerInit(self), None)

    def test_updateLife(self):
        self.assertEqual(Player.updateLife(self), None)

    def test_updateScore(self):
        self.assertEqual(Player.updateScore(self,4),None)

    def test_moveUp(self):
        self.assertEqual(Player.moveUp(self),None)

    def test_moveDown(self):
        self.assertEqual(Player.moveDown(self),None)

    def test_moveLeft(self):
        self.assertEqual(Player.moveLeft(self),None)

    def test_moveRight(self):
        self.assertEqual(Player.moveRight(self),None)

        
if __name__ == '__main__':
    unittest.main()