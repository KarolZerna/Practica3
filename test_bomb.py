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
        self.gameArray = [[0 for x in range(80)] for y in range(40)]
        self.gameArray[0][0]=1


    def test_drawBomb(self):
        self.assertEqual(Bomb.drawBomb(self), None)

    def test_drawBomb_not_bimbo(self):
        self.assertFalse(Bomb.drawBomb(self.bimbo))

    def test_drawBomb_pos1(self):
        self.assertEqual(Bomb.drawBomb(self.bomPos[2]>1), None)

    def test_drawBomb_pos2(self):
        self.assertNotEqual(Bomb.drawBomb(self.bomPos[2]==-1), self.test_explosion)

    def test_drawExplosion(self):
        self.assertEqual(Bomb.drawExplosion(self, self.x, self.y), None)

    def test_check_post(self):
        self.assertEqual(Bomb.checkPos(self, self.x, self.y),1)

    def test_check_post_(self):
        self.assertNotEqual(self.gameArray=="X", -1)   

    def test_afterExplosion(self):
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)

    def test_explosion(self):
        self.assertEqual(Bomb.explosion(self), None)

    def test_explosion_after(self):
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)

    def test_explosion_check(self):
        self.assertTrue(Bomb.checkPos(self,self.x-1, self.y), 1)
        TestBomb.test_afterExplosion(self)


if __name__ == '__main__':
    unittest.main()