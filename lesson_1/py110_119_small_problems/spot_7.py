"""
Write a function that takes a list of words and constructs a new word by
concatenating the nth letter from each word, where n is the position of the
word in the list.

P:
input: list of words (strings) as arg
output: return new word (string, consisting of the nth letter from each word, where n is the position of the word in the list)
implicit: words will be long enough to prevent idx errors

E: see below

D & A:
* nth_letter_str = ''
* nth_letter_idx = 0
* iterate through words in word_lst:
    * concatenate letter at nth_letter_idx to nth_letter_str
    * increment nth_letter_idx
* return nth_letter_str

C:
"""
def nth_char(word_lst):
    nth_letter_str = ''
    nth_letter_idx = 0

    for word in word_lst:
        nth_letter_str += word[nth_letter_idx]
        nth_letter_idx += 1

    return nth_letter_str

# Example:
print(nth_char(['yoda', 'best', 'has']) == 'yes') # should return 'yes'