# P:
# input: list of numbers
# output: list with same number of elements, and each element being a cumulative
#         sum as each element of the original list is added
# explicit: 
# implicit:
# - return an empty list for an empty list argument
# - return the same one-element list for a one-element list argument

# E:

# D: Create new_list as the desired output list

# A:
# 1. define running_total function
# 2. if the input list (number_list) is empty, return number_list
# 3. create cum_num_list with the 1st element of the number_list as its only
#    element
# 4. for each element in the number_list with index > 0:
#     1. add the element to the last element in cum_num_list
#     2. append this sum to the end of cum_num_list
# 5. return cum_num_list

# C:
def running_total(number_list):
    if not number_list:    # number_list empty
        return number_list
    
    cum_num_list = [number_list[0]]
    for idx, num in enumerate(number_list):
        if idx > 0:
            cum_num_list.append(num + cum_num_list[-1])

    return cum_num_list


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True