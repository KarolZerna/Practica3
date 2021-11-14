import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):
    def test_draw_enemy(self):
        self.assertEqual(Enemy.drawEnemy(self),None)
    def test_updateNum(self):
        self.assertEqual(Enemy.updateNum(self,4),None)
    def test_checkPos(self):
        self.assertEqual(Enemy.checkPos(self,4,3),1)
    
    def test_killPlayer(self):
        self.assertEqual(Enemy.killPlayer(self,4,1),None)
    def test_enNum(self):
        self.assertEqual(Enemy.enNum(self),5)


if __name__ == '__main__':
    unittest.main()