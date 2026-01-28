# P: 
# input: one integer argument
# output: list w/ all integers between 1 and the argument (inclusive),
#         in ascending order
# explicit: integer argument will always be positive
# implicit:

# E: see below

# D:

# A:

# C:
def sequence(number):
    return list(range(1, number + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
     