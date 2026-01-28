# P:
# input: two arguments - two lists of integers of the same length
# output: new list where each element is the product of the corresponding
#         elements from the two lists
# explicit:
# implicit:

# E: see above

# D:

# A:
# def multiply_items(lst1, lst2):
#     1. create list comprehension which uses the zip function to create an
#        iterator of tuples of corresponding elements, unpacks them, and
#        multiplies them

# C:
def multiply_items(lst1, lst2):
    return [int1 * int2 for int1, int2 in zip(lst1, lst2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True