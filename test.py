import time
# import tty 

import unittest
from unittest.case import expectedFailure
from unittest import mock

from gameplay import Gameplay
from board import Board
from bomb import Bomb
from enemy import Enemy
from player import Player
from alarmexception import AlarmException
from person import Person
from brick import Brick


class TestAlarmException(unittest.TestCase):
     def test_alarmexception(self):
        self.assertRaises(Exception)


class TestBoard(unittest.TestCase):

     def test_gameBoard(self):
        gameArray = [[0 for x in range(80)] for y in range(40)]
        gameArray[0][0]=1
        expected = gameArray
        self.assertEqual(Board.gameBoard(self), None)

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

    def test_drawBomb_in_range(self):
        self.assertIn(Bomb.drawBomb(self.y), self.gameArray[0][0])

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
        self.assertIsNone(Bomb.explosion(self), None)

    def test_explosion_after(self):
        self.assertEqual(Bomb.afterExplosion(self, self.x, self.y), None)

    def test_explosion_check(self):
        self.assertTrue(Bomb.checkPos(self,self.x-1, self.y), 1)
        TestBomb.test_afterExplosion(self)




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
    def test_update_pos(self):
        self.assertEqual(Enemy.updatePos(self),None)
    def test_enemy_init(self):
        self.assertEqual(Enemy.enemyInit(self),None)
    def test_checkPos_conditional(self):
        self.assertTrue(Enemy.checkPos(self,0,0),-1)


class TestGamePlay(unittest.TestCase):

    def setUp(self):
        self.cur_time = time.time()
        # self.run_time = time.time() - self.cur_time

    def test_init(self):
        self.assertNotEqual(Gameplay.__init__(self.cur_time), time.time())


    def test_printboard(self):
        self.assertGreater(Gameplay.printboard(time.time() - self.cur_time), 1)

    def test_printboard_return(self):
        self.assertEqual(Gameplay.printboard(self), None)

class TestPersonCheck(unittest.TestCase):
    def test_check_post_mayor(self):
        self.assertEqual(Person.checkPos(self, 3, 1), -1)

    def test_check_pos(self):
        self.assertEqual(Person.checkPos(self, 68, 70), -1)
    
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

    # def test_checkPos_neg(self):
    #     self.assertEqual(Player.checkPos(self, self.x, self.y), -1)

    def test_moveUp(self):
        self.assertEqual(Player.moveUp(self),None)

    def test_moveDown(self):
        self.assertEqual(Player.moveDown(self),None)

    def test_moveLeft(self):
        self.assertEqual(Player.moveLeft(self),None)

    def test_moveRight(self):
        self.assertEqual(Player.moveRight(self),None)

    def test_checkEnemy(self):
        self.assertEqual(Player.checkEnemy(self, self.x, self.y), 1)

    def test_playerInit(self):
        self.assertEqual(Player.playerInit(self), None)

    def test_updateLife(self):
        self.assertEqual(Player.updateLife(self), None)

    def test_updateScore(self):
        self.assertEqual(Player.updateScore(self,4),None)


class TestBrick(unittest.TestCase):
    def test_brickInit(self):
        self.assertEqual(Brick.brickInit(self),None)
    
    def test_drawBricks(self):
        self.assertEqual(Brick.drawBricks(self),None)


if __name__ == '__main__':
    unittest.main()