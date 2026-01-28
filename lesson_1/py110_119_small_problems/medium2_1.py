# * P: 
#     * input: string argument
#     * output: returns % of chars that are lowercase, uppercase, and neither,
#               respectively (see examples below)
#     * explicit: 
#         * each % should be a str w/ 2 decimal places
#         * arg str will always have >= 1 char
# * E: see below
# * D & A:
#     * def letter_percentages(string):
#         * initialize lowercase, uppercase, and neither variables, and set then
#           all to 0
#         * loop through all chars in the string, incrementing the appropriate
#           variable upon each iteration
#         * calculate length of str and save to length variable
#         * divide the value of each variable from above by length, and save
#           to lowercase_percentage, etc.
#         * initialize result variable and set to empty dictionary
#         * add key-value pairs of 'lowercase': lowercase_percentage (formatted
#           as a string set to 2 dec places), etc.
#         * return result dict
# * C:
def letter_percentages(string):
    lowercase, uppercase, neither = 0, 0, 0

    for char in string:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        else:
            neither += 1

    length = len(string)

    return {
    'lowercase': f'{(lowercase / length) * 100:.2f}',
    'uppercase': f'{(uppercase / length) * 100:.2f}',
    'neither'  : f'{(neither   / length) * 100:.2f}',
    }


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)