"""
Write a function that takes a list of words as input and returns a list of
integers. Each integer represents the count of letters in the word that occupy
their positions in the ALPHABET.

P:
input: list of words as arg
output: return list of ints (count of letters in the word that occupy
    their positions in the ALPHABET)

E: see below

D & A: (1st solution)
* create ALPHABET_IDX dict w/ lowercase letters as keys and ints as values
* count_lst = []
* iterate through each word:
    * count = 0
    * iterate through each idx, letter:
        * if idx == ALPHABET_IDX[letter.lower()]:
            * increment count by one
        * append count to count_lst
* return count_lst
C:
"""

# def solve(input_lst):
#     ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
#     ALPHABET_IDX = {letter: ALPHABET.index(letter) for letter in ALPHABET}
    
#     count_lst = []

#     for word in input_lst:
#         count = 0
        
#         for idx, letter in enumerate(word):
#             if idx == ALPHABET_IDX[letter.lower()]:
#                 count += 1
        
#         count_lst.append(count)

#     return count_lst


def solve(input_lst):
    ORD_VAL_LOWERCASE_A = 97
    
    count_lst = []

    for word in input_lst:
        count = 0
        
        for idx, letter in enumerate(word):
            if idx == ord(letter.lower()) - ORD_VAL_LOWERCASE_A:   # sets alphabet to 0-25 idx
                count += 1
        
        count_lst.append(count)

    return count_lst


# Examples:
print(solve(["abode","ABc","xyzD"]) == [4, 3, 1]) # should return [4, 3, 1]
print(solve(["abide","ABc","xyz"]) == [4, 3, 0])# should return [4, 3, 0]