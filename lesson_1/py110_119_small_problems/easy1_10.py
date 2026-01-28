# P:
# input: integer
# output: string representation of that integer
# explicit: 
# - assume positive numeric values
# - may not use Python's standard conversion functions
# implicit:

# E:

# D: make a list of digit string representations

# A:
# 1. integer_to_string(integer) definition statement
# 2. make list of digit string representations
# 3. create empty string_number string
# 3. set quotient variable to reference the same object referenced by integer
# 3. if quotient == 0, return '0'
# 4. keep dividing quotient by 10 (until quotient becomes 0), and the
#    remainder is the furthest right digit
# 5. return string_number

# C:
def integer_to_string(integer):
    DIGIT_LST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    string_number = ''
    quotient = integer

    if quotient == 0:
        return '0'

    while quotient > 0:
        quotient, remainder = divmod(quotient, 10)
        current_number = DIGIT_LST[remainder]
        string_number = current_number + string_number

    return string_number

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True