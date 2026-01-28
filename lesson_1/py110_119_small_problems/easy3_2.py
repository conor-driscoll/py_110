# P:
# input: military time string
# output: one integer between 0 and 1439, inclusive
# explicit: disregard Daylight Savings and other complications
# implicit:

# E: see below

# D:

# A:

# C:

MIN_PER_HR = 60
HRS_PER_DAY = 24
MIN_PER_DAY = 1440


def after_midnight(time_24hr):
    hours = int(time_24hr[:2]) % HRS_PER_DAY
    minutes = int(time_24hr[3:])

    return (hours * MIN_PER_HR) + minutes


def before_midnight(time_24hr):
    min_past_12am = after_midnight(time_24hr)
    
    return (MIN_PER_DAY - min_past_12am if min_past_12am != 0
            else min_past_12am)


print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True