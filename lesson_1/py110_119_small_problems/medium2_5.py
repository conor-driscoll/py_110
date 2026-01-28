# * P:
#     * input: integer as argument
#     * output: the 1st 'featured number' greater than arg int, or error message
#               if arg int is >= 9876543201 (the largest possible featured #)
#     * explicit:
#         * featured numbers:
#             * multiples of 7
#             * odd
#             * each digit occuring once
#     * implicit: arg int will be positive (from provided test cases)
# * E: see below
# * D & A:
#     * def next_featured(input_integer):
#         * check if input_integer >= largest possible featured number
#           * if yes, return error msg
#         * current_7_multiple = (next multiple of 7 greater than
#           input_integer)
#         * check if current_7_multiple is odd and also has only one of each
#           digit (extract these checks into 2 separate helper functions)
#           * if yes, return current_7_multiple
#           * if no, current_7_multiple += 7 and loop back to double helper
#             function check
# * C:
def is_odd(current_7_multiple):
    return current_7_multiple % 2 == 1


def repeated_digits_absent(current_7_multiple):
    str_int = str(current_7_multiple)
    repeated_digits = [char for char in str_int if str_int.count(char) > 1]
    return not repeated_digits # True for empty list


def next_featured(input_integer):
    LARGEST_FEATURED = 9876543201
    ERROR_MSG = ("There is no possible number that fulfills those "
                 "requirements.")
    
    if input_integer >= LARGEST_FEATURED:
        return ERROR_MSG
    
    multiple_7_remainder = input_integer % 7
    add_to_reach_next_7_multiple = 7 - multiple_7_remainder
    current_7_multiple = input_integer + add_to_reach_next_7_multiple 
    
    while True:
        if (is_odd(current_7_multiple) and
                repeated_digits_absent(current_7_multiple)):
            return current_7_multiple

        current_7_multiple += 7

    

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True