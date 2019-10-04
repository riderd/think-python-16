import unittest
from mytime import *

class TestTime(unittest.TestCase):
    
    def setUp(self):
        self.t = Time()
        // should probably set up t2 as well
        
    def tearDown(self):
        del self.t
        # print("in tearDown")
        
    def test_time(self):
        self.assertEqual(0, self.t.hour)
        self.assertEqual(0, self.t.minute)
        self.assertEqual(0, self.t.second)
        
        self.t.hour = 11
        self.t.minute = 59
        self.t.second = 30
        self.assertEqual(11, self.t.hour)
        self.assertEqual(59, self.t.minute)
        self.assertEqual(30, self.t.second)
        
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
        increment_better(t1, 0)
        self.assertEqual("00:00:00", compose_time(t1))
        increment_better(t1, 30)
        self.assertEqual("00:00:30", compose_time(t1))
        increment_better(t1, 50)
        self.assertEqual("00:01:20", compose_time(t1))
        increment_better(t1, 175)
        self.assertEqual("00:02:135", compose_time(t1))
        
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
        increment(t1, 0)
        self.assertEqual("00:00:00", compose_time(t1))
        increment(t1, 30)
        self.assertEqual("00:00:30", compose_time(t1))
        increment(t1, 50)
        self.assertEqual("00:01:20", compose_time(t1))
        increment(t1, 175)
        self.assertEqual("00:04:15", compose_time(t1))
       
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        increment(t2, 290)
        self.assertEqual("12:04:20", compose_time(t2))
    
    def test_int_to_time(self):
        self.assertEqual("00:00:00", compose_time(int_to_time(0)))
        self.assertEqual("00:00:30", compose_time(int_to_time(30)))
        self.assertEqual("00:01:20", compose_time(int_to_time(80)))
        self.assertEqual("00:04:15", compose_time(int_to_time(255))) 
        
    def test_time_to_int(self):
        self.assertEqual(0, time_to_int(self.t))
        
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual((11 * 3600) + (59 * 60) + 30, time_to_int(t2))
      
    def test_add_time_base60(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(add_time_base60(t1, t1)))

        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual("23:59:00", compose_time(add_time_base60(t2, t2)))
        
        # test example from the book
        start = Time()
        start.hour = 9
        start.minute = 45
        start.second = 0
        duration = Time()
        duration.hour = 1
        duration.minute = 35
        duration.second = 0
        self.assertEqual("11:20:00", compose_time(add_time_base60(start, duration)))   
        
        t3 = Time()
        t3.hour = 23
        t3.minute = 30
        t3.second = 270
        self.assertEqual("47:09:00", compose_time(add_time_base60(t3, t3)))
        
    def test_increment_base60_pure(self):
        t1 = Time()
        self.assertEqual("00:00:00", compose_time(increment_base60_pure(t1, 0)))
        self.assertEqual("00:00:30", compose_time(increment_base60_pure(t1, 30)))
        self.assertEqual("00:01:20", compose_time(increment_base60_pure(t1, 80)))
        self.assertEqual("00:04:15", compose_time(increment_base60_pure(t1, 255)))
       
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertEqual("12:04:20", compose_time(increment_base60_pure(t2, 290)))
        
    def test_valid_time(self):
        t1 = Time()
        self.assertTrue(valid_time(t1))
        
        t2 = Time()
        t2.hour = 11
        t2.minute = 59
        t2.second = 30
        self.assertTrue(valid_time(t2))
        
        t2.minute = 60
        self.assertFalse(valid_time(t2))
        t2.minute = 61
        self.assertFalse(valid_time(t2))
        
        t2.minute = 59
        t2.second = 59
        self.assertTrue(valid_time(t2))
         
        t2.second = 60
        self.assertFalse(valid_time(t2))
        t2.second = 61
        self.assertFalse(valid_time(t2))
        
        t2.second = -1
        self.assertFalse(valid_time(t2))
        t2.second = 0
        self.assertTrue(valid_time(t2))
        
        t2.minute = -1
        self.assertFalse(valid_time(t2))
        t2.minute = -2
        self.assertFalse(valid_time(t2))
        
        t2 = Time()
        self.assertTrue(valid_time(t2))
        t2.hour = -1
        self.assertFalse(valid_time(t2))
        
if __name__ == '__main__':
    unittest.main()
    