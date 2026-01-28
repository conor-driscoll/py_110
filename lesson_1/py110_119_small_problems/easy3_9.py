# P:
# input: list argument
# output: list argument w/ elements reversed in place (original list should be
#         mutated and returned)
# explicit: can't use list.reverse method or a reverse slice ([::-1])
# implicit:

# E: see below

# D:

# A:

# C:

from copy import copy as shallow_copy

def reverse_list(lst):
    
    lst_copy = shallow_copy(lst)
    
    for i in range(len(lst)):
        lst[i] = lst_copy.pop()
    
    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True