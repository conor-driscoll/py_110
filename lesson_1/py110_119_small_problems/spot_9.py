"""
Write a function that generates text following a pattern where:
1) the first and last characters of each word remain in their original place
2) characters between the first and last characters are sorted alphabetically
3) punctuation should remain at the same place as it started

P:
input: string of words as arg
output: return string of words (according to rules above)

E: see below

D & A:
* def format_word(raw_word):
* if len(raw_word) in (1, 2, 3):
    * return word
* char_lst = list(raw_word)
* all_chars_alpha = True
* iterate through letter_lst
    * if char is alphabetic
        * continue
    * else:
        * all_chars_alpha = False
        * save punctuation_idx
        * remove save and punctuation 

char_lst_sorted = [char_lst[-1], (*sorted(char_lst[1:-1])), char_lst[0]]

if not all_chars_alpha:
    insert punctuation before punctuation_idx in char_lst_sorted


return ''.join(char_lst_sorted)
C:
"""
def format_word(raw_word):
    if len(raw_word) in (1, 2, 3):
        return raw_word
    
    char_lst = list(raw_word)
    all_chars_alpha = True
    for idx, char in enumerate(char_lst):
        if char.isalpha():
            continue
        else:
            all_chars_alpha = False
            punctuation_idx = idx
            punctuation = char

    if not all_chars_alpha:
        char_lst.remove(punctuation)
    
    char_lst_sorted = [char_lst[0], *sorted(char_lst[1:-1]), char_lst[-1]]

    if not all_chars_alpha:
        char_lst_sorted.insert(punctuation_idx, punctuation)
    
    return ''.join(char_lst_sorted)


def scramble_words(word_string):
    word_lst = word_string.split()
    
    return ' '.join([format_word(word) for word in word_lst])


# Examples:
print(scramble_words('professionals') == 'paefilnoorsss') # should return 'paefilnoorsss'
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.") # should return "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."