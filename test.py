import unittest

import alarmexception
import board, person

class TestAlarmException(unittest.TestCase):
    def alarm_exception(self):
        pass

# class TestBoard(unittest.TestCase):
#     def test_game_board(self):
#         self.assertEqual(board.gameArray[0,0], 1)

class Person(unittest.TestCase):
     def TestCheckPost(self):
         self.assertEqual(person.checkPos(3,60),-1)
         self.assertEqual(person.checkPos(40,60),-1)
         self.assertEqual(person.checkPos(3,1),-1)
         self.assertEqual(person.checkPos(3,80),-1)
if __name__ == '__main__':
    unittest.main()