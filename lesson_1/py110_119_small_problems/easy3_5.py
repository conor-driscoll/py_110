# P:
# input: one positive integer argument
# output: return the integer w/ digits reversed
# explicit:
# implicit:

# E: see below

# D:

# A:
# def reverse_number(positive_int):
#     1. convert positive_int to a string
#     2. use slicing to reverse the characters
#     3. convert back to int

# C:
def reverse_number(positive_int):
    return int(str(positive_int)[::-1])
    

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
