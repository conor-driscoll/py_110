# P:
# input: one string argument
# output: one list of substrings, beginning with the 1st letter of the word,
#         and elements ordered from shortest to longest
# explicit:
# implicit:

# E: see below

# D:

# A:
# def leading_substrings(string):
#     1. return [string[0:end] for end in range(1, len(string))]

# C:
def leading_substrings(string):
    return [string[:end] for end in range(1, len(string) + 1)]


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])