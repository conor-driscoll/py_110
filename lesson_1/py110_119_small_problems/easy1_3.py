# P: 
# input: string passed to is_real_palindrome function
# output: function returns True if the string argument is a palindrome,
#         else False
# explicit: case doesn't matter and ignore all non-alphanumeric characters
# implicit: don't worry about bad inputs

# E:

# D:

# A:
# 1. Define the function
# 2. Create a lower_string with all cased characters converted to lower case
# 3. Create an empty string: alnum_string
# 4. for all characters in lower_string
#     1. if character is alphanumeric add it to alnum_string
# 5. Compare alnum_string to a complete reverse slice of alnum_string,
#    and return the result.

# C:
def is_real_palindrome(string):
    lower_string = string.lower()
    
    alnum_string = ''
    for char in lower_string:
        if char.isalnum():
            alnum_string += char

    return alnum_string == alnum_string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True