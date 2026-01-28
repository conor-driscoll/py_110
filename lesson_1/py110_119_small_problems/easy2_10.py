# P:
# input: one list of integers as an argument
# output: average of all the integers in the list, rounded to an integer
# explicit: list won't be empty and list integers will be positive
# implicit:

# E: see below

# D:

# A:

# C:
def average(lst):
    return int(sum(lst) / len(lst))


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
