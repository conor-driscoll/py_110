# P:
# input: list of ints
# output: return a list w/ only the first value, where values occur successively
#         in the original list
# explicit:
# implicit: assuming that mutation of the argument list isn't desired

# E: see below

# D:

# A:
# def unique_sequence(lst):
#     1. initialize a previous_value variable and assign it the value of None
#     2. initialize a new_lst variable and assign it the value of []
#     3. for num in lst:
#         1. if num != previous_value:
#             2. new_lst.append(num)
#         2. previous_value = num
#     4. return new_lst

# C:
def unique_sequence(lst):
    previous_value = None
    new_lst = []
    
    for num in lst:
        if num != previous_value:
            new_lst.append(num)
        previous_value = num
    
    return new_lst


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True