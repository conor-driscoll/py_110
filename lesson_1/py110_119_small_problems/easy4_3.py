# P:
# input: two list arguments
# output: return the frozenset that is the intersection of the two lists

# E: see below

# D:

# A:
# def intersection(lst1, lst2):
#     1. return frozenset(lst1).intersection(frozenset(lst2))

# C:
def intersection(lst1, lst2):
    return frozenset(lst1).intersection(frozenset(lst2))

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True