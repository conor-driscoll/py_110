# P:
# input: list of numbers argument
# output: returns sum of sums of each leading subsequence of input list
# explicit: assume that list contains >= 1 number
# implicit:

# E: see below

# D:

# A:
# def sum_of_sums(lst):
#     1. list comprehension which creates a list of leading subsequences and
#        assign the variable master_lst to it
#     2. return sum of a nested list comprehension which converts master_lst into one
#        list w/out nesting

# C:
def sum_of_sums(lst):
    master_lst = [lst[:end] for end in range(1, len(lst) + 1)]

    return sum([num for subseq in master_lst 
                    for num in subseq])


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True