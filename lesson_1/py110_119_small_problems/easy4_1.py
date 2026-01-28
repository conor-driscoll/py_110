# P:
# input: list of integers between 0 and 19, inclusive
# output: input list sorted based on each letter's English word
# explicit:
# implicit:

# E: see below

# D:

# A:
# 1. make WORD_LIST out of provided list of English words for ints
# 2. use zip function with WORD_LIST and INPUT_LIST and pass this into
#    dict function to create constant WORD_DICT


# def english_int_word(input_int):
#     return WORD_DICT[input_int]

# def alphabetic_number_sort(INPUT_LIST):
#     1. return a list created using sorted() and english_int_word(input_int)

# C:
INPUT_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

WORD_LIST = ('zero, one, two, three, four, five, six, seven, eight, nine, '
             'ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, ' 
             'seventeen, eighteen, nineteen').split(', ')

WORD_DICT = dict(zip(INPUT_LIST, WORD_LIST))


def english_int_word(input_int):
    return WORD_DICT[input_int]

def alphabetic_number_sort(input_list):
    return sorted(input_list, key=english_int_word)


EXPECTED_RESULT = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(INPUT_LIST) == EXPECTED_RESULT)
# Prints True
    