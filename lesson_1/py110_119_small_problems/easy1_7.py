# P:
# input: string of words separated by spaces
# output: string with first and last letters swapped
# explicit:
# - every word contains at least one letter
# - string always contains at least one word
# - string contains nothing but words and spaces
# - No leading, trailing, or repeated spaces
# implicit:

# E:

# D:

# A:
# 1. swap(string) function definition statement
# 2. create words_list from string
# 3. create empty new_words_list
# 4. for word in words_list:
#     1. create empty new_word
#     2. for characters in word:
#         1. if index == 0, add the last character in word to new_word
#             1. if len(word) = 1
#                 1. continue
#         2. elif index == len(word) - 1, add the first character in the string
#         3. else, add the character to the new_word
#     3. add new_word to new_words_list
# 5. return new_words_list as a string, with the words joined by spaces

# C:
def swap(string):
    words_list = string.split()
    new_words_list = []
    
    for word in words_list:
        new_word = ''
    
        for idx, char in enumerate(word):
            if idx == 0:
                new_word += word[-1]
                if len(word) == 1:
                    continue
            elif idx == len(word) - 1:
                new_word += word[0]
            else:
                new_word += char
        
        new_words_list.append(new_word)

    return ' '.join(new_words_list)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True