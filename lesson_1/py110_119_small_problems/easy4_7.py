# P:
# input: string argument
# output: list of all substrings in a string, ordered by lower starting index
#         and shorter strings 1st
# explicit:
# implicit:

# E: see below

# D:

# A:
# def substrings(input_lst):
#     1. initialize result_lst and assign it to an empty list
#     2. pass each char of input_lst into leading_substring function, and 
#        extend result_lst with each successive return value
#     3. return result_lst

# C:
def leading_substrings(string):
    return [string[:end] for end in range(1, len(string) + 1)]


# def substrings(string):
#     result_lst = []
#     lst_of_lsts = [leading_substrings(string[start:]) for start in 
#                  range(len(string))]

#     return [element for nestd_lst in lst_of_lsts
#                     for element in nestd_lst]

def substrings(string):
    return [substring for start in range(len(string))
                      for substring in leading_substrings(string[start:])]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True