LOWERCASE_VOWELS = ['a', 'e', 'i', 'o', 'u']


def count_consecutive_adjacent_consonants(string_input):

    str_no_spaces = string_input.replace(' ', '')
    maximum_adjacent_consonants = 0
    current_adjacent_consonants = 0
    previous_char_consonant = False

    for index, char in enumerate(str_no_spaces):

        if char not in LOWERCASE_VOWELS:         # char is consonant
            if previous_char_consonant:          # if char == True
                current_adjacent_consonants += 1
            else:
                last_char_index = len(str_no_spaces) - 1
                if index == last_char_index:
                    break
                next_char = str_no_spaces[index + 1]
                if next_char not in LOWERCASE_VOWELS:
                    current_adjacent_consonants += 1

            previous_char_consonant = True
            maximum_adjacent_consonants = max(maximum_adjacent_consonants,
                                              current_adjacent_consonants)
            continue

        previous_char_consonant = False
        current_adjacent_consonants = 0

    return maximum_adjacent_consonants


def sort_by_consonant_count(list_input):

    list_input_copy = list_input.copy()

    list_input_copy.sort(key=count_consecutive_adjacent_consonants,
                         reverse=True)

    return list_input_copy


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
    # ['xxxx', 'xxxb', 'xxxa']