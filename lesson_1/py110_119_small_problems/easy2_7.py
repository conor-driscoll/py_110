# P:
# input: two list arguments
# output: new list containing the products of same-index list pairs
# explicit: both argument lists have the same number of elements
# implicit: list arguments contain only positive integers

# E: see below

# D:

# A:
# 1. definition statement for multiply_list(lst1, lst2) function
# 2. intialize empty new_list
# 3. for lst1_int, lst2_int in zip(lst1, lst2):
#     1. new_list += [lst1_int * lst2_int]
# 4. return new_lst

# C:
def multiply_list(lst1, lst2):
    new_lst = []

    for lst1_int, lst2_int in zip(lst1, lst2):
        new_lst += [lst1_int * lst2_int]
    
    return new_lst


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
