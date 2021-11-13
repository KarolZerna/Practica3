import unittest
from bomb import Bomb

class TestBomb(unittest.TestCase):
    def test_check_post(self):
         self.assertEqual(Bomb.checkPos(self, 3, 1), 1)
    

if __name__ == '__main__':
    unittest.main()