# P:
# input: 6 numbers from the user
# output: message that describes whether the 6th number appears among the 
#         first 5
# explicit:
# - 
# implicit:
# - all numbers will be integers from the user
# - don't worry about bad inputs

# E:

# D: Will add first 5 numbers collected from the user to a list, and check if
#    the 6th number is present in this list

# A: 
# 1. Use the input function 6 times to collect 6 numbers, keep them as
#    strings, and assign them to the variables number_1,...,number_5, 
#    last_number.
# 2. Create five_number_list with the 1st 5 numbers
# 3. Check if last_number in five_number_list and assign is_or_isnt to the 
#    appropriate string ("is" or "isn't") based on the result
# 4. Print an f-string with the required specs, calling the join function
#    on the string object ,',', and passing in five_number_list as an
#    argument, to manipulate
#    the data in this list into the correct format for the output string.

number_1 = input('Enter the 1st number: ') 
number_2 = input('Enter the 2nd number: ') 
number_3 = input('Enter the 3rd number: ') 
number_4 = input('Enter the 4th number: ') 
number_5 = input('Enter the 5th number: ') 
last_number = input('Enter the last number: ')

five_number_list = [number_1, number_2, number_3, number_4, number_5]

if last_number in five_number_list:
    is_or_isnt = 'is'
else:
    is_or_isnt = "isn't"

print(f'{last_number} {is_or_isnt} in {','.join(five_number_list)}.')


# Further exploration:
# For the current solution to be used for the new application, the numbers
# would need to be converted to a numeric data type.

