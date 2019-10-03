from datetime import date
from ex2 import age, days_hours_minutes_seconds_till_next_birthday_from_today
import sys

try:
    birthday_str = input("Enter your birthday in format YYYY-MM-DD (e.g. 2000-06-15 for June 15, 2000): ")
    birthday = date.fromisoformat(birthday_str)
except:
    print("Please enter your birthday in the expected format YYYY-MM-DD")
    sys.exit(1)

print()
print("Today you are %d" % age(birthday))
print("You are %d days %d hours %d minutes %d seconds away from your next birthday" % days_hours_minutes_seconds_till_next_birthday_from_today(birthday))

