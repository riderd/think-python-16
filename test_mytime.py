import unittest
from mytime import *

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
        
    def test_compose_time(self):
        t = Time()
        self.assertEqual("00:00:00", compose_time(t))
        t.hour = 11
        t.minute = 59
        t.second = 30
        self.assertEqual("11:59:30", compose_time(t))
        
    def test_is_after(self):
        t1 = Time()
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertTrue(is_after(t2, t1))
        self.assertFalse(is_after(t1, t2))
        self.assertFalse(is_after(t1, t1))
        self.assertFalse(is_after(t2, t2))
        t3 = Time()
        t3.hour = 11
        t3.minute = 59
        t3.second = 31
        self.assertTrue(is_after(t3, t2))
        self.assertFalse(is_after(t2, t3))
        
    def test_add_time_simple(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(add_time_simple(t1, t1)))

        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual("22:118:60", compose_time(add_time_simple(t2, t2)))
        
        # test example from the book
        start = Time()
        start.hour = 9
        start.minute = 45
        start.second = 0
        duration = Time()
        duration.hour = 1
        duration.minute = 35
        duration.second = 0
        self.assertEqual("10:80:00", compose_time(add_time_simple(start, duration)))
        
    def test_add_time_better(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(add_time_better(t1, t1)))

        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual("23:59:00", compose_time(add_time_better(t2, t2)))
   
        # test example from the book
        start = Time()
        start.hour = 9
        start.minute = 45
        start.second = 0
        duration = Time()
        duration.hour = 1
        duration.minute = 35
        duration.second = 0
        self.assertEqual("11:20:00", compose_time(add_time_better(start, duration)))

    def test_increment_better(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(increment_better(t1, 0)))
        self.assertEqual("00:00:30", compose_time(increment_better(t1, 30)))
        self.assertEqual("00:01:20", compose_time(increment_better(t1, 80)))
        self.assertEqual("00:01:195", compose_time(increment_better(t1, 255)))
        
    def test_add_time(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(add_time(t1, t1)))

        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual("23:59:00", compose_time(add_time(t2, t2)))
        
        # test example from the book
        start = Time()
        start.hour = 9
        start.minute = 45
        start.second = 0
        duration = Time()
        duration.hour = 1
        duration.minute = 35
        duration.second = 0
        self.assertEqual("11:20:00", compose_time(add_time(start, duration)))   
        
        t3 = Time()
        t3.hour = 23
        t3.minute = 30
        t3.second = 270
        self.assertEqual("47:09:00", compose_time(add_time(t3, t3)))
        
    def test_increment(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(increment(t1, 0)))
        self.assertEqual("00:00:30", compose_time(increment(t1, 30)))
        self.assertEqual("00:01:20", compose_time(increment(t1, 80)))
        self.assertEqual("00:04:15", compose_time(increment(t1, 255))) 
       
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual("12:04:20", compose_time(increment(t2, 290)))
    
    def test_int_to_time(self):
        self.assertEqual("00:00:00", compose_time(int_to_time(0)))
        self.assertEqual("00:00:30", compose_time(int_to_time(30)))
        self.assertEqual("00:01:20", compose_time(int_to_time(80)))
        self.assertEqual("00:04:15", compose_time(int_to_time(255))) 
        
    def test_time_to_int(self):
        t1 = Time()
        self.assertEqual(0, time_to_int(t1))
        
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual((11 * 3600) + (59 * 60) + 30, time_to_int(t2))
        
if __name__ == '__main__':
    unittest.main()
    