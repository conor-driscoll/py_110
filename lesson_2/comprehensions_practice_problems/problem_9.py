lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def all_even(input_dict):
    for nested_lst in input_dict.values():
        for integer in nested_lst:
            if integer % 2 == 1:
                return False
    
    return True


print([nested_dict for nested_dict in lst if all_even(nested_dict)])