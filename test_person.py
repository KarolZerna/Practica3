import unittest
from person import Person

class TestPersonCheck(unittest.TestCase):
    def test_check_post_mayor(self):
        self.assertEqual(Person.checkPos(self, 3, 1), -1)

    def test_check_pos(self):
        self.assertEqual(Person.checkPos(self, 68, 70), -1)
    
        
if __name__ == '__main__':
    unittest.main()