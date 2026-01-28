# P:
# input: string consisting of 0 or more space-separated words
# output: dictionary showing number of words of different sizes
# explicit: words consist of any sequence of non-space characters
# implicit: words are separated by a single space character

# E:

# D:

# A:
# 1. definition statement for word_sizes(string) function
# 2. convert string into word_list
# 3. create empty word_size_dict
# 4. for every word in word_list:
#     1. determine the length of each word
#     2. if length not in word_size_dict:
#         1. add length: 1 key-value pair to dict
#     3. else word_size_dict[length] += 1
# 5. return word_size_dict

# C: 
def word_sizes(string):
    word_list = string.split()

    word_size_dict = {}
    for word in word_list:
        length = len(word)
        if length not in word_size_dict:
            word_size_dict[length] = 1
        else:
            word_size_dict[length] += 1

    return word_size_dict



# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})