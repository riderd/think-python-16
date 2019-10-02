import unittest
from ex1 import mul_time
from mytime import Time, compose_time

class TestEx1(unittest.TestCase):
    def test_mul_time(self):
        t = Time()
        self.assertEqual("00:00:00", compose_time(mul_time(t, 1)))
        self.assertEqual("00:00:00", compose_time(mul_time(t, 2)))        
        self.assertEqual("00:00:00", compose_time(mul_time(t, 841)))
        
        