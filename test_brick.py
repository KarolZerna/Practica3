import unittest
from brick import Brick

class TestBrick(unittest.TestCase):
    def test_brickInit(self):
        self.assertEqual(Brick.brickInit(self),None)
    
    def test_drawBricks(self):
        self.assertEqual(Brick.drawBricks(self),None)


if __name__ == '__main__':
    unittest.main()