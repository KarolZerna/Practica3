import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):
    def test_draw_enemy(self):
        self.assertEqual(Enemy.drawEnemy(self),None)




if __name__ == '__main__':
    unittest.main()