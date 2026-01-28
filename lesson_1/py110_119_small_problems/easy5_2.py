# P:
# input: two arguments - a dict & a list of keys (the keys of the key-value
#        pairs to be included in the new dict)
# output: new dict consisting of selected key-value pairs from the original
# explicit:
# implicit:

# E: see below

# D:

# A:
# def keep_keys(original_dict, selected_keys):
#     use a dict comprehension to grab selected key_value pairs for the new dict

# C:
def keep_keys(original_dict, selected_keys):
    return {key: value for key, value in original_dict.items()
            if key in selected_keys}


input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True