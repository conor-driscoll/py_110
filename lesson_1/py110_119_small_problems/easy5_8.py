# P:
# input: string argument
# output: string w/ every other char (starting w/ 1st) capitalized, and followed
#         by a lowercase or non-alphabetic char
# explicit: non-alphabetic chars shouldn't be changed, but should be counted as
#           part of the every other capitalization pattern
# implict:

# E: see below

# D:

# A:
# def staggered_case(message):
#     1. return a joined list comprehension combined with a tenary statement to
#        create a new str w/ every other char capitalized

# C:
def staggered_case(message):
    return ''.join([char.upper() if (idx % 2 == 0) else char.lower()
                    for idx, char in enumerate(message)])


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True