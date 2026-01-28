# P:
# input: two list arguments
# output: return a set of elements unique to the first list
# explicit:
# implicit: 

# E: see below

# D:

# A:
# def unique_from_first(list1, list2):
#     1. intersect_lst = list1 & list2
#     2. return [num for num in list1 if num not in intersect_lst]

# C:
def unique_from_first(lst1, lst2):
    intersect_set = set(lst1) & set(lst2)
    return {num for num in lst1 if num not in intersect_set}


list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
