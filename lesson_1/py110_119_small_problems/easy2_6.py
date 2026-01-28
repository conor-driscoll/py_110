# P:
# input: list of positive integers
# output: 3 decimal pt string value for the multiplicative avg of list elements
# explicit:
# implicit:

# E: see below

# D:

# A:
# 1. definition statement for multiplicative_average(lst) function
# 2. initialize cum_value variable and assign it a value of 1
# 3. for each integer:
#     1. multiply integer by cum_value, and reassign it this new value
# 4. divide cum_value by len(lst), inside of an f-string, formatted w/3
#    decimal rounding, and return string

# C:
def multiplicative_average(lst):
    cum_value = 1
    for integer in lst:
        cum_value *= integer

    return f"{cum_value / len(lst):.3f}"


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")