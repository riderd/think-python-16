import unittest
from ex1 import mul_time, average_time_per_mile
from mytime import Time, compose_time

class TestEx1(unittest.TestCase):
    def test_mul_time(self):
        t = Time()
        self.assertEqual("00:00:00", compose_time(mul_time(t, 1)))
        self.assertEqual("00:00:00", compose_time(mul_time(t, 2)))        
        self.assertEqual("00:00:00", compose_time(mul_time(t, 841)))
        
    def test_average_time_per_mile(self):
        t = Time()
        t.hour = 3
        t.minute = 2
        t.second = 0
        self.assertEqual("00:07:00", compose_time(average_time_per_mile(t, 26)))
        
        t.minute = 0
        self.assertEqual("00:06:55", compose_time(average_time_per_mile(t, 26)))
        
        self.assertEqual("00:06:52", compose_time(average_time_per_mile(t, 26.2)))
        
        t.hour = 0
        t.minute = 48
        t.second = 30
        self.assertEqual("00:09:42", compose_time(average_time_per_mile(t, 5)))
        
        # rounds down to the second - not to closest
        t.second = 34
        self.assertEqual("00:09:42", compose_time(average_time_per_mile(t, 5)))
        
        t.second = 35
        self.assertEqual("00:09:43", compose_time(average_time_per_mile(t, 5)))
        
        
if __name__ == '__main__':
    unittest.main()
        
        