# P: 
# input: string passed to is_palindrome function
# output: function returns True if the string argument is a palindrome,
#         else False
# explicit: case and all characters matter
# implicit: don't worry about bad inputs

# E:

# D:

# A:
# 1. define the function
# 2. for every character (char) in the 1st 1/2 of the input string (not
#    including the middle character of strings with odd number lengths) with 
#    check to see if it is the same as the character that is the same number of
#    positions from the end of string, as it is from the beginning
#         1. If any one of the characters doesn't match its counterpart
#             1. return False
# 3. If the string made it through this entire for loop without returning
#    False, it is a palindrome, so return True

# C:

def is_palindrome(string):
    last_index_to_check = (len(string) // 2) - 1

    for index, char in enumerate(string):
        if index <= last_index_to_check:
            if char != string[(index * -1) - 1]:
                return False

    return True


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)