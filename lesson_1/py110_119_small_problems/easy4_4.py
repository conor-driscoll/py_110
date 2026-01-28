# P:
# input: dictionary argument
# output: return keys sorted by values
# explicit:
# implicit:

# E: see below

# D:

# A:

# C:
def order_by_value(input_dict):
    
    def get_value(input_key):
        return input_dict[input_key]

    return sorted(list(input_dict.keys()), key=get_value)


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True