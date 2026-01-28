# P:
#     input: two list arguments
#     output: function returns a set (union of the two list values)
#     explicit: 
#         - two arguments will always both be lists
#     implicit:

# E: see below

# D:

# A:
# def union(list1, list2):
#     add both lists together to create combined_list
#     create a set out of combined_list
#     return set

# C:
def union(list1, list2):
    return set(list1 + list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True