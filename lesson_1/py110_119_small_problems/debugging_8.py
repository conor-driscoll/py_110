# Code problem:
# - The issue is that a shallow copy was made, and then a nested list was
#   modified. Shallow copies don't copy nested objects, and instead, only contain
#   references to the original nested objects.


import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])