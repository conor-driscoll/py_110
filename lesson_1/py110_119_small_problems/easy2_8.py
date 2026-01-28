# P:
# input: one positive int argument
# output: list containing all the digits of the number as separate elements
# explicit:
# implicit:

# E: see below

# D:

# A:
# def digit_list(num):
# 1. return list comprehension/transformation in which num is converted to a
#    string, and its characters are iterated through, with each successive 
#    character converted to an integer and then added to the list as a separate
#    item.

# C:
def digit_list(num):
    return [int(char) for char in str(num)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
 
