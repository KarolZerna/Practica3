import unittest
from getchunix import GetchUnix
import tty 

class TestGetchUnix(unittest.TestCase):

     def test_init(self):
        self.assertTrue(self, tty)
        
if __name__ == '__main__':
    unittest.main()