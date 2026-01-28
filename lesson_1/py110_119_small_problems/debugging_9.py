# Code problem:
# - This code raises an error because the iterable is mutated during
#   iteration, which is practice that creates unintended consequences and should
#   be avoided. 

data_set = {1, 2, 3, 4, 5}

odd_data_set = {item for item in data_set if item % 2 != 0}

print(odd_data_set)