# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

'''
P:
input: string w/ >= 1 lowercase character(s)
output: return longest alphabetical current_substring
explicit: return substring that appears 1st, if tie

E: see below

D & A: (for my first solution, which is commented below)
* return list of all alphabetic substrings
* destructive sort by length
* determine length of last item in list
* iterate through list and return 1st item with that length
'''

def longest(string):
    current_substring = ''
    saved_substring = ''

    for char in string:
        if not current_substring or char >= current_substring[-1]:
            current_substring += char
        else:
            if len(current_substring) > len(saved_substring):
                saved_substring = current_substring
            current_substring = ''
            current_substring += char

    if len(saved_substring) >= len(current_substring):
        return saved_substring
    else:
        return current_substring


# def longest(string):
#     current_substring = ''
#     substring_lst = []

#     for char in string:
#         if not current_substring or char >= current_substring[-1]:
#             current_substring += char
#         else:
#             substring_lst.append(current_substring)
#             current_substring = ''
#             current_substring += char
    
#     if (not substring_lst or current_substring != substring_lst[-1]):
#         substring_lst.append(current_substring)

#     substring_lst.sort(key=len)
#     max_len = len(substring_lst[-1])

#     for element in substring_lst:
#         if len(element) == max_len:
#             return element


print(longest('asd') == 'as')
print(longest('nab') == 'ab')
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')