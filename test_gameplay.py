import unittest
import time
from gameplay import Gameplay
from unittest import mock


class TestGamePlay(unittest.TestCase):

    def setUp(self):
        self.cur_time = time.time()
        # self.run_time = time.time() - self.cur_time

    def test_init(self):
        self.assertNotEqual(Gameplay.__init__(self.cur_time), time.time())


    def test_printboard(self):
        self.assertGreater(Gameplay.printboard(time.time() - self.cur_time), 1)
        for x in range(1, 39):
            with self.subTest(x = x):
                # self.assertEqual(1 // x, 0)
                self.assertNotEqual(Gameplay.__init__(self.cur_time), time.time())

    def test_printboard_return(self):
        self.assertEqual(Gameplay.printboard(self), None)


if __name__ == '__main__':
    unittest.main()