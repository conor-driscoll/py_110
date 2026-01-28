# * P:
#     * input: string
#     * output: return string with every occurrence of a number word converted to
#       an integer
#     * explicit: no punction in string
#     * implicit: one space between every word
# * E: see below
# * D & A:
#     * def word_to_digit(message):
#         * create dict w/words as keys and 'int's as values
#         * split string into list of words
#         * initialize empty list
#         * iterate through every word in list
#             * if word is a dict key
#                 * append corresponding 'int' to new list
#             * else:
#                 * append original word to new list
#         * return joined with one space in between(new list)
# * C:
# def word_to_digit(message):
#     WORDS_DIGITS = {
#         'zero': '0',
#         'one': '1',
#         'two': '2',
#         'three': '3',
#         'four': '4',
#         'five': '5',
#         'six': '6',
#         'seven': '7',
#         'eight': '8',
#         'nine': '9',
#     }

#     words_without_digits = message.split()
#     words_with_digits = []

#     for word in words_without_digits:
#         if word in WORDS_DIGITS:
#             words_with_digits.append(WORDS_DIGITS[word])
#         else: 
#             words_with_digits.append(word)

#     return ' '.join(words_with_digits)


# message = 'Please call me at five five five one two three four'
# print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# # Should print True


# Further exploration:
def word_to_digit(message):
    WORDS_DIGITS = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }


    words_without_digits = message.split()
    words_with_digits = []

    for word in words_without_digits:
        if word in WORDS_DIGITS:
            words_with_digits.append(WORDS_DIGITS[word])
            continue
        
        last_char_missing = word[:-1]
        last_char_only = word[-1]
        if last_char_missing in WORDS_DIGITS:
            words_with_digits.append(WORDS_DIGITS[last_char_missing] +
                                     last_char_only)
        else: 
            words_with_digits.append(word)
    
    return ' '.join(words_with_digits)


message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True