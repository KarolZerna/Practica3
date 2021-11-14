import unittest
from unittest.case import expectedFailure
from board import Board

class TestBoard(unittest.TestCase):

     def test_gameBoard(self):
        gameArray = [[0 for x in range(80)] for y in range(40)]
        gameArray[0][0]=1
        expected = gameArray
        self.assertEqual(Board.gameBoard(self), expected)

        
if __name__ == '__main__':
    unittest.main()