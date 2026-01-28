# P:
# input: two integer arguments, a list element count and a sequence starting
#        integer, respectively
# output: list than begins at the starting integer, and continues by multiples
#         of the starting integer, until the required element count has been 
#         reached
# explicit: 
#           - count >= 0
#           - starting # == any integer
#           - count == 0 should produce an empty list
# implicit:

# E: see below

# D:

# A:
# def sequence(count, start):
#     1. initialize result_list and assign it a value of []
#     2. for integer in range(1, count + 1):
#         1. result_list += [start * integer]
#     3. return result_list

# C:
# def sequence(count, start):
#     result_list = []
    
#     for integer in range(1, count + 1): 
#         result_list += [start * integer]
    
#     return result_list

def sequence(count, start):
    return [start * num for num in range(1, count + 1)]


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True