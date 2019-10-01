import unittest
from mytime import Time

t = Time()

class TestTime(unittest.TestCase):
    
    def test_time(self):
        t = Time()
        self.assertEqual(0, t.hour)
        self.assertEqual(0, t.minute)
        self.assertEqual(0, t.second)
        
        t.hour = 11
        t.minute = 59
        t.second = 30
        self.assertEqual(11, t.hour)
        self.assertEqual(59, t.minute)
        self.assertEqual(30, t.second)
        
        

if __name__ == '__main__':
    unittest.main()
    