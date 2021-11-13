import unittest

import alarmexception
import board, person

class TestAlarmException(unittest.TestCase):
    def alarm_exception(self):
        pass

class TestBoard(unittest.TestCase):
    gameArray = [[0 for x in range(80)] for y in range(40)]
    gameArray[0][0]=1

    def test_game_board(self):
        # gameArray[0][0]=1
        self.assertEqual(board.gameArray[2][37],"X")

class TestPerson(unittest.TestCase):
     def TestCheckPost(self):
         self.assertEqual(person.checkPos(3,60),-1)
         self.assertEqual(person.checkPos(40,60),-1)
         self.assertEqual(person.checkPos(3,1),-1)
         self.assertEqual(person.checkPos(3,80),-1)
         
if __name__ == '__main__':
    unittest.main()