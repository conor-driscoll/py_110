# P:
# input: integer
# output: string representation of that integer
# explicit:
# - may not use Python's standard conversion functions
# implicit:

# E:

# D: make a list of digit string representations

# A:
# 1. integer_to_string(integer) definition statement
# 2. make list of digit string representations
# 3. create empty string_number string
# 4. if integer == 0, return '0'
# 5. if integer > 0, sign = '+'
# 6. if integer < 0, sign =  '-'
# 7. assign quotient variable the absolute value of integer
# 8. keep dividing quotient by 10 (until quotient becomes 0), and the
#    remainder is the furthest right digit
# 9. return sign + string_number

# C:
def signed_integer_to_string(integer):
    DIGIT_LST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    string_number = ''

    if integer == 0:
        return '0'
    elif integer > 0:
        sign = '+'
    else:
        sign = '-'

    quotient = abs(integer)

    while quotient != 0:
        quotient, remainder = divmod(quotient, 10)
        current_number = DIGIT_LST[remainder]
        string_number = current_number + string_number

    return sign + string_number


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True