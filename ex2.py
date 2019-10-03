from datetime import *

def day_from_date(d):
    weekday_to_str = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday",
    }
    return weekday_to_str[d.weekday()]
    
def current_day():
    return day_from_date(date.today())
    
def print_current_day():
    print(current_day())

def age_asof_date(birthday, d):
    years_age = d.year - birthday.year
    if d.month > birthday.month:
        return years_age
    if (d.month < birthday.month):
        return years_age - 1
    if (d.day < birthday.day):
        return years_age - 1
    return years_age

def age(birthday):
    return age_asof_date(birthday, date.today())    
    
def delta_to_days_hours_minutes_seconds(delta):
    days = delta.days
    hours, remaining_seconds_after_hours = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remaining_seconds_after_hours, 60)
    return (days, hours, minutes, seconds)
    
def days_hours_minutes_seconds_till_next_birthday(birthday, dt):
    dt_year_birthday = datetime(dt.year, birthday.month, birthday.day)
    # should I be returning a (0, 0, 0, 0) if it's the same day?
    if (dt_year_birthday > dt):
        return delta_to_days_hours_minutes_seconds(dt - dt_year_birthday)
    dt_next_year_birthday = datetime(dt_year_birthday.year + 1, dt_year_birthday.month, dt_year_birthday.day)
    return delta_to_days_hours_minutes_seconds(dt_next_year_birthday - dt)
    
def days_hours_minutes_seconds_till_next_birthday_from_today(birthday):
    return days_hours_minutes_seconds_till_next_birthday(birthday, datetime.today())
    
def __double_day__(first_birthday, second_birthday):
    return second_birthday + (second_birthday - first_birthday)
    
def find_double_day(birthday1, birthday2):
    if (birthday1 > birthday2):
        return __double_day(birthday2, birthday1)
    return __double_day(birthday1, birthday2)