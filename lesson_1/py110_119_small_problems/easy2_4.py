# P:
# input: an unordered list with exactly one value occurring twice
# output: the duplicate value
# explicit:
# implicit: the input list will contain exclusively positive integers

# E: see below

# D:

# A:
# 1. definition statement for find_dup(lst) function
# 2. initialize new_list variable and assign it the value of []
# 3. for every integer in lst:
#     1. check if the integer is in new_list
#         1. if yes, return the integer
#         2. else, add the integer to the new_list

# C:
# def find_dup(lst):
#     new_list = []
    
#     for integer in lst:
#         if integer in new_list:
#             return integer
#         else:
#             new_list += [integer]

def find_dup(lst):
    for integer in lst:
        if lst.count(integer) == 2:
            return integer

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True
