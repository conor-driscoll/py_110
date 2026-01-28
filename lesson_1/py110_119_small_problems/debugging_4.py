# Code problem(s):
# - using bracket notation and a key to look up a value within a dictionary will
#   raise a KeyError if the key isn't present in the dictionary

def get_key_value(my_dict, key):
    my_dict.get(key)

print(get_key_value({"a": 1}, "b"))