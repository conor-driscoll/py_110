"""
Write a function that takes a lowercase string as input and returns the
length of the longest substring that consists entirely of vowels (a, e, i, o, u).

P:
input: lowercase string as arg
output: length of longest vowel substring

E: see below

D & A: (1st solution)
* intialize VOWELS constant string
* current_substring_len = 0
* saved_substring_len = 0
* iterate through input_str:
    * if letter is vowel:
        * increment current_substring_len
    * else:
        if current_substring_len > saved_substring_len:
            saved_substring_len = current_substring_len
        current_substring_len = 0
* return max(saved_substring_len, current_substring_len)
C:
"""

# def solve(input_str):
#     VOWELS = 'aeiou'
    
#     current_substring_len = 0
#     saved_substring_len = 0

#     for letter in input_str:
#         if letter in VOWELS:
#             current_substring_len += 1
#         else:
#             if current_substring_len > saved_substring_len:
#                 saved_substring_len = current_substring_len
#             current_substring_len = 0
    
#     return max(saved_substring_len, current_substring_len)


def solve(input_str):
    VOWELS = 'aeiou'

    consonants_replaced_by_spaces = ''

    for letter in input_str:
        if letter not in VOWELS:
            consonants_replaced_by_spaces += ' '
        else:
            consonants_replaced_by_spaces += letter
    
    vowel_only_substrings = consonants_replaced_by_spaces.split()
    vowel_only_substrings_lengths = [len(substring) for substring in vowel_only_substrings]

    return max(vowel_only_substrings_lengths)


# Examples:
print(solve("roadwarriors") == 2) # should return 2
print(solve("suoidea") == 3) # should return 3