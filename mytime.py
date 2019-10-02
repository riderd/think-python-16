
class Time:
    """Represents the time of day
    
    attributes: hour, minute, second
    """
    
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
    
def compose_time(t):
    return '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)
    
def print_time(t):
    print(compose_time(t))
    
def is_after(t1, t2):
    return t1.hour > t2.hour or t1.minute > t2.minute or t1.second > t2.second
    
def add_time_simple(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum
    
def add_time_better(t1, t2):
    sum = add_time_simple(t1, t2)
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
        
    if sum.minute >= 60:
       sum.minute -= 60
       sum.hour += 1
       
    return sum
    
def increment_better(t, seconds):
    seconds_time = Time()
    seconds_time.second = seconds
    sum = add_time_better(t, seconds_time)
    t.hour = sum.hour
    t.minute = sum.minute
    t.second = sum.second
    
def add_time(t1, t2):
    sum = add_time_simple(t1, t2)
    (add_minutes, seconds_remaining) = divmod(sum.second, 60)
    sum.minute += add_minutes
    sum.second = seconds_remaining
    (add_hours, minutes_remaining) = divmod(sum.minute, 60)
    sum.hour += add_hours
    sum.minute = minutes_remaining
    return sum
    
def increment(t, seconds):
    seconds_time = Time()
    seconds_time.second = seconds
    sum = add_time(t, seconds_time)
    t.hour = sum.hour
    t.minute = sum.minute
    t.second = sum.second
    
def int_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
    
def time_to_int(t):
    minutes = t.hour * 60 + t.minute
    return minutes * 60 + t.second
    
def add_time_base60(t1, t2):
    return int_to_time(time_to_int(t1) + time_to_int(t2))
    
def increment_base60_pure(t1, seconds):
    return int_to_time(time_to_int(t1) + seconds)

def valid_time(t):
    if (t.hour < 0 or t.minute < 0 or t.second < 0 or t.minute >= 60 or t.second >= 60):
        return False
    return True
    