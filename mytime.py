
class Time:
    """Represents the time of day
    
    attributes: hour, minute, second
    """
    
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0
    
def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))