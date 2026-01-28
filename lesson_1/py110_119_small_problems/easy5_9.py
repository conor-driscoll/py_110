# P:
# input: string argument
# output: string w/ every other char (starting w/ 1st) capitalized, and followed
#         by a lowercase or non-alphabetic char
# explicit: non-alphabetic chars shouldn't be changed, and shouldn't be counted
# as part of the every other capitalization pattern
# implict:

# E: see below

# D:

# A:
# def staggered_case(message):
#     1. return a joined list comprehension combined with a tenary statement to
#        create a new str w/ every other char capitalized

# C:
def staggered_case(message):
    new_str = ''
    upper_next = True
    
    for char in message:
        if char.isalpha() and upper_next:
            new_str += char.upper()
            upper_next = False
        elif char.isalpha() and not upper_next:
            new_str += char.lower()
            upper_next = True
        else:
            new_str += char
   
    return new_str


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True