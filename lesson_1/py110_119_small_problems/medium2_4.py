# * P:
#     * input: integer representing a year as arg
#     * output: return int representing number of Friday the 13ths in that year
#     * explicit: 
#         * year will be > 1752 (first year of modern Gregorian calendar)
#         * this calendar will be in use for the foreseeable future
#     * from my own research: New Year's day in 1753 was a Monday
# * E: see below
# * D & A:
# * def friday_the_13ths(year):
#     * calculate the number of days from Monday, 1/1/1753 to the last day of
#       (year - 1)
#     * determine the day of the week of the 1st day of the year in question
#     * use a nested comprehension to create a dict with all the days of the year
#       in question recorded, w/ two-element lists as values (date, day of the
#       week)
#     * return the number of values containing both 13 and Friday
# * C:
REMAINDER_DAY = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    0: 'Sunday',
}


NEXT_DAY = {
    'Sunday':    'Monday',
    'Monday':    'Tuesday',
    'Tuesday':   'Wednesday',
    'Wednesday': 'Thursday',
    'Thursday':  'Friday',
    'Friday':    'Saturday',
    'Saturday':  'Sunday',
}



def is_leap_year(input_year):
    return (input_year % 4 == 0 and 
            (input_year % 100 != 0 or input_year % 400 == 0))


def friday_the_13ths(input_year):
    YEAR_ZERO = 1753 # First full year of modern Gregorian calendar
    
    days_until_input_year = 0
    for year in range(YEAR_ZERO, input_year):
        if is_leap_year(year):
            days_until_input_year += 366
        else:    
            days_until_input_year += 365
    
    jan1_input_year_key = (days_until_input_year + 1) % 7
    jan1_day = REMAINDER_DAY[jan1_input_year_key]
    leap_year = is_leap_year(input_year)
    dates_by_month_plus_1 = (32, 30 if leap_year else 29, 32, 31, 32, 31, 32,
                            32, 31, 32, 31, 32)
    
    friday_the_13th_counter = 0
    current_day = jan1_day
    for month in dates_by_month_plus_1:
        for date in range(1, month):
            if current_day == 'Friday' and date == 13:
                friday_the_13th_counter += 1
            current_day = NEXT_DAY[current_day]
    
    return friday_the_13th_counter



print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True