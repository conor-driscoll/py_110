# P:
# input: one list
# output: one nested list, containing two lists. the 1st list should contain
#         the 1st half of the original list (including the middle element in
#         cases in which the original list has an odd number of elements) and
#         the 2nd list should contain the 2nd 1/2 of the original list
# explicit:
# implicit: -element order should be maintained
#           -if the original list is empty, the function should return a nested
#            list with 2 empty lists
#           -if the original list has only one element, the 1st sub-list will
#            have the 1st element and the 2nd sub-list will be empty

# E: see below

# D:

# A:
# 1. definition statement for halvsies(input_list)
# 2. item_count = len(input_list)
# 3. if item_count % 2 = 1:
#     1. first_list = input_list[:int((item_count + 1) / 2)]
#     2. second_list = input_list[int((item_count + 1) / 2):]
#    else:
#     1. first_list = input_list[:int(item_count / 2)]
#     2. second_list = input_list[int(item_count / 2):]
# 4. return [first_list, second_list]

# C:
def halvsies(input_list):
    item_count = len(input_list)
    
    if item_count % 2 == 1:
        first_list = input_list[:int((item_count + 1) / 2)]
        second_list = input_list[int((item_count + 1) / 2):]
    else:
        first_list = input_list[:int(item_count / 2)]
        second_list = input_list[int(item_count / 2):]

    return [first_list, second_list]
    

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])