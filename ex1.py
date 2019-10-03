from mytime import *

def mul_time(t, multiplier):
    return int_to_time(time_to_int(t) * multiplier)
    
# note this will round the time down to second and not to the closest second
def average_time_per_mile(finishing_time, distance_in_miles):
    return mul_time(finishing_time, 1.0/distance_in_miles)
