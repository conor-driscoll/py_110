# P:
# input: one positive int argument
# output: sum of its digits
# explicit:
# implicit:

# E: see below

# D:

# A:
# def sum_digits(num):
#     running_total = 0
    
#     for char in str(num):
#         running_total += int(char)

#     return running_total

# C:
def sum_digits(num):
    running_total = 0
    
    for char in str(num):
        running_total += int(char)

    return running_total


print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True