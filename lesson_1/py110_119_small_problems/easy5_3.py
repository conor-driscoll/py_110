# P:
# input: list of strings argument
# output: return a new list with vowels ('aeiou') removed (regardless of case)
# explicit:
# implicit:

# E: see below

# D: will create a string with upper and lower case vowels to check against

# A:
# 1. create vowel string
# def remove_vowels(str_lst):
#     1. create and return a list created using a nested list comprehension
#        that iterates through string element character by character

# C:
VOWEL_STR = 'aeiouAEIOU'

def remove_vowels_in_str(input_string):
    return ''.join([char for char in input_string if char not in VOWEL_STR])

def remove_vowels(str_lst):
    return [remove_vowels_in_str(string) for string in str_lst]

# def remove_vowels(str_lst):
#     new_lst = []
    
#     for string in str_lst:
#         new_str = ''
        
#         for char in string:
#             if char not in VOWEL_STR:
#                 new_str += char

#         new_lst.append(new_str)

#     return new_lst


# # All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True