LOWERCASE_VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# list_of_vowels = []

# for nested_list in dict1.values():
#     for string in nested_list:
#         for char in string:
#             if char in LOWERCASE_VOWELS:
#                 list_of_vowels.append(char)

# print(list_of_vowels)


# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']


# Extra Challenge:
print([char for nested_list in dict1.values()
            for string in nested_list
            for char in string if char in LOWERCASE_VOWELS])
