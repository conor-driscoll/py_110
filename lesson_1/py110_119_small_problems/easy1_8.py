# P:
# input: string of digits
# output: integer
# explicit:
# - may not use int function
# - don't worry about + or - signs, or invalid characters
# - assume all numeric characters

# E:

# D: make a dictionary with string digits as keys, and integers as values

# A:
# 1. string_to_integer(str_num) function definition statement
# 2. Create STRING_INT_DICT described above
# 3. Reverse the order of str_num and assign to rev_str_num
# 4. assign total variable to the value of 0
# 5. for idx, characters in rev_str_num:
#     1. current_digit_val = STRING_INT_DICT[char] * (10**idx)
#     2. add current_digit_val to total variable
# 6. return total

# C:
def string_to_integer(str_num):
    STRING_INT_DICT = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    rev_str_num = str_num[::-1]
    total = 0
    
    for idx, char in enumerate(rev_str_num):
        current_digit_val = STRING_INT_DICT[char] * (10**idx)
        total += current_digit_val
    
    return total


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True