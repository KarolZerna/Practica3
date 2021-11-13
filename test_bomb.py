import unittest
from bomb import Bomb
from enemy import Enemy
from player import Player

class TestBomb(unittest.TestCase):

    def setUp(self):
        self.bomPos = [0,0,-1] 
        self.bombThrown = 0
        self.bimbo=[]
        self.pl = Player()
        self.en = Enemy()
        self.x = 3 #19
        self.y = 1 #5


    def test_drawBomb(self):
        self.assertEqual(Bomb.drawBomb(self), None)
        

    def test_drawExplosion(self):
        self.assertEqual(Bomb.drawExplosion(self, self.x, self.y), None)

    def test_check_post(self):
         self.assertEqual(Bomb.checkPos(self, 3, 1), 1)


    def test_afterExplosion(self):
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)
        # self.assertEqual(Player.updateLife(self), None)
    

    def test_explosion(self):
        self.assertEqual(Bomb.explosion(self), None)
        self.assertEqual(Bomb.drawExplosion(self, self.x, self.y), None)
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)
        self.assertEqual(Bomb.checkPos(self, 3, 1), -1)

if __name__ == '__main__':
    unittest.main()