import unittest
import time
from gameplay import Gameplay
from unittest import mock

from board import *
from brick import *
from person import *
from player import *
from enemy import *
from bomb import *
bo = Board()
br = Brick()
pl = Player()
en = Enemy()
bom = Bomb()


class TestGamePlay(unittest.TestCase):

    def setUp(self):
        self.gameArray = bo.gameBoard()
		# self.br = br.drawBricks()
		# self.pl = pl.updatePlayer()
        self.cur_time = time.time()
        self.run_time = self.cur_time
	    # self.run_time = time.time() - self.cur_time

    def test_init(self):
        self.assertNotEqual(Gameplay.__init__(self.cur_time), time.time())


    def test_printboard(self):
        # self.assertNotEqual(self.run_time, time.time()-self.cur_time)
        pass

if __name__ == '__main__':
    unittest.main()