"""
Write a function that takes a string as input and counts the occurrences of each
lowercase letter in the string. Return the counts in a dictionary where the
letters are keys and their counts are values.

P:
input: string arg
output: dict w/ letters as keys and counts as values

E: see below

D & A:
* create empty letter_counts dict
* iterate through char in string
    * if char is lowercase letter:
        * if letter is not a key in letter_counts:
            * add key-value pair char-0 to dict
        * increment char's count in dict by one
* return dict

C:
"""
def letter_count(string):
    letter_count = {}

    for char in string:
        if char.islower():
            if char not in letter_count:
                letter_count[char] = 0
            letter_count[char] += 1

    return letter_count


print(letter_count('launchschool')) #=> {’a’: 1, ‘c’: 2, ‘h’: 2, ‘l’: 2, ‘o’: 2, ‘u’: 1, 'n': 1, 
                                    #    's': 1}