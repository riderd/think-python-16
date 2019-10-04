import unittest
from ex2 import *
from datetime import date, timedelta

class TestEx1(unittest.TestCase):
    def test_current_day(self):
        # Note this test will fail if it's not Friday. I haven't come up with a good way
        # to test this. Maybe there's another way to calculate the day of the week.
        # Best way is to probably make another method that gets the day of the week from a date
        # and that can be tested well with different dates and then the current_day() method
        # is really simple and could be tested 
        self.assertEqual("Friday", current_day())

    def test_age_asof_date(self):
        # June 15, 2000
        birthday = date(2000, 6, 15)
        
        self.assertEqual(0, age_asof_date(birthday, date(2000, 6, 15)))    
        # Is -1 right for an answer?    
        self.assertEqual(-1, age_asof_date(birthday, date(2000, 6, 14)))
        
        self.assertEqual(-1, age_asof_date(birthday, date(1999, 6, 15)))
        
        self.assertEqual(0, age_asof_date(birthday, date(2001, 6, 14)))        
        self.assertEqual(1, age_asof_date(birthday, date(2001, 6, 15)))  
        
        self.assertEqual(1, age_asof_date(birthday, date(2002, 6, 14)))        
        self.assertEqual(2, age_asof_date(birthday, date(2002, 6, 15)))
        self.assertEqual(2, age_asof_date(birthday, date(2002, 6, 16)))
        
        self.assertEqual(19, age_asof_date(birthday, date(2019, 10, 3)))
        self.assertEqual(19, age_asof_date(birthday, date(2019, 10, 20)))
        
    def test_age(self):
          # June 15, 2000
          birthday = date(2000, 6, 15)
          
          # this won't always be right but will be right when I present this Oct 4, 2019
          self.assertEqual(19, age(birthday))    
          
    def test_delta_to_days_hours_minutes_seconds(self):
        delta = timedelta(days=4, hours=15, minutes=16, seconds = 12)
        self.assertEqual((4, 15, 16, 12), delta_to_days_hours_minutes_seconds(delta))
        
        delta2 = timedelta(seconds = delta.total_seconds())
        self.assertEqual((4, 15, 16, 12), delta_to_days_hours_minutes_seconds(delta2))
        
    def test_days_hours_minutes_seconds_till_next_birthday(self):
        birthday = date(2000, 6, 15)
        dt = datetime(2019, 10, 3, hour = 15, minute = 29, second = 30)
        self.assertEqual((255, 8, 30, 30), days_hours_minutes_seconds_till_next_birthday(birthday, dt))
        
        # Should this be 0,0,0,0. Right now, it's accounting for a leap day in 2020
        dt = datetime(2019, 6, 15, hour = 15, minute = 29, second = 30)
        self.assertEqual((365, 8, 30, 30), days_hours_minutes_seconds_till_next_birthday(birthday, dt))
        
        # Should this be 0,0,0,0. Right now, it's accounting for no leap day in 2021
        dt = datetime(2020, 6, 15, hour = 15, minute = 29, second = 30) 
        self.assertEqual((364, 8, 30, 30), days_hours_minutes_seconds_till_next_birthday(birthday, dt))
        
        # here's a test that come up during the presentation that was wrong
        birthday = date(1992, 10, 10)
        dt = datetime(2019, 10, 4, hour = 14, minute = 58, second = 30)
        print(days_hours_minutes_seconds_till_next_birthday(birthday, dt))

if __name__ == '__main__':
    unittest.main()
        
        
    
