lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print([{key: value + 1 for key, value in sub_dict.items()}
                       for sub_dict in lst])