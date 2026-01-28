# P:
# input: one positive, negative, or 0 integer argument
# output: military time
# explicit: disregard Daylight Savings and other complications
# implicit: the number of minutes may exceed one day (24 hrs)

# E: see below

# D:

# A:
# def time_of_day(time_int):
#     1. if time_int < 0:
#         1. convert time_int to positive by adding it to 1440
#     2. hours = str(time_int // 60)
#     3. hours = hours if len(hours) == 2 else '0' + hours
#     4. minutes = str(time_int % 60)
#     5. minutes = minutes if len(minutes) == 2 else '0' + hours
#     4. return f'{hours}:{minutes}'

# C:
# def time_of_day(time_int):
#     while time_int < 0: 
#         time_int += 1440

#     time_int %= 1440

#     hours = str(time_int // 60)
#     hours = hours if len(hours) == 2 else '0' + hours
    
#     minutes = str(time_int % 60)
#     minutes = minutes if len(minutes) == 2 else '0' + minutes
    
#     return f'{hours}:{minutes}'

def time_of_day(time_int):
    while time_int < 0: 
        time_int += 1440

    time_int %= 1440

    hours = time_int // 60
    minutes = time_int % 60
    
    return f'{hours:02d}:{minutes:02d}'


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
