# P:
# input: string argument
# output: list containing every word from the string, w/ each word followed by
#         a space and the word's length
# explicit: -should return [] in the case of an empty string or no argument
#            passed
#           -every pair of words will be separated by single space
# implicit:

# E: see below

# D:

# A:
# def word_lengths(words_str=''):
#     1. create and return a list created using a list comprehension that takes
#        each word, adds a space and the word length, and adds this new str,
#        if there is a non-empty str passed into function

# C:
def word_lengths(words_str=''):
    return [word + ' ' + str(len(word)) for word in words_str.split(' ')
            if words_str != '']


# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True