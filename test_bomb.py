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
        self.playerPos= []


    def test_drawBomb(self):
        pos = self.bomPos[2]
        self.assertEqual(Bomb.drawBomb(self), None)
        # self.assertGreater(Bomb.drawBomb(pos), self.x)
        self.assertIsNone(Bomb.drawBomb(self.bimbo))
        self.assertFalse(Bomb.drawBomb(self.bimbo))
        

    def test_drawExplosion(self):
        self.assertEqual(Bomb.drawExplosion(self, self.x, self.y), None)

    def test_check_post(self):
        self.assertEqual(Bomb.checkPos(self, 3, 1), 1)
        # self.assertEqual(Bomb.checkPos(self, [2*self.x+1], [4*self.y+1]), "X")


    def test_afterExplosion(self):
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)
        # self.assertTrue(Bomb.afterExplosion(self, self.playerPos[0], self.playerPos[1]))
        
        # self.assertEqual(Player.updateLife(self), None)
    

    def test_explosion(self):
        self.assertEqual(Bomb.explosion(self), None)
        self.assertEqual(Bomb.drawExplosion(self, self.x, self.y), None)
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)
        self.assertNotEqual(Bomb.checkPos(self, 3, 1), -1)

if __name__ == '__main__':
    unittest.main()