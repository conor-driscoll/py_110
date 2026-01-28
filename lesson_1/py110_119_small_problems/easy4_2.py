# P:
# input: two list arguments
# output: convert lists to sets and return union of the sets
# explicit:
# implicit:

# E: below

# D:

# A:
# def merge_sets(lst1, lst2):
#     1. add the lists together, convert the resulting concatenated list to a 
#        set, and return the result

# C:
def merge_sets(lst1, lst2):
    return set(lst1 + lst2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True