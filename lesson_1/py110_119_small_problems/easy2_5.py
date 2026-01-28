# P:
# input: two lists
# output: new list, with all elements, in alternating sequence, from both lists
# explicit: both lists are non-empty, and have the same number of elements
# implicit: I'm going to assume that not mutating the argument lists is
#           preferable

# E: see below

# D: I'll work with shallow list copies, so as not to mutate the argument
#    lists

# A:
# 1. definition statement for interleave(lst1, lst2) function
# 2. shallow copy lst1 and assign it to copy_lst1
# 3. shallow copy lst2 and assign it to copy_lst2
# 4. initialize result_lst and it assign it the value of []
# 5. while len(copy_lst1) > 0:
#     1. pop off the element of copy_lst1 at index 0, and add it to result_lst
#     2. pop off the element of copy_lst1 at index 0, and add it to result_lst
# 6. return result_lst

# C:
# def interleave(lst1, lst2):
#     copy_lst1 = lst1[:]
#     copy_lst2 = lst2[:]
#     result_lst = []

#     while len(copy_lst1) > 0:
#         result_lst += [copy_lst1.pop(0), copy_lst2.pop(0)]

#     return result_lst


# Further exploration:

def interleave(lst1, lst2):
    result_lst = []

    for pair in zip(lst1, lst2):
        result_lst += pair

    return result_lst

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True