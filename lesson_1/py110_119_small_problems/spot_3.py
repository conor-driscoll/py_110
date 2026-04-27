'''
Write a function that takes two strings as input, `full_text` and `search_text`,
and returns the number of times `search_text` appears in `full_text`.

P:
input: two string args, full_text & search_text
output: number of times search_text appears in full_text

E: see below

D & A:
* substr_count = 0
* search_start_idx = 0
* while True:
    * search for search_text at search_start_idx
    * if it isn't found
        * return substr_count
    * if it is found:
        * add len(search_text) to search_start_idx
return substr_count
C:
'''

def solution(full_text, search_text):
    substr_count = 0
    search_start_idx = 0
    len_substr = len(search_text)

    while True:
        substr_start_idx = full_text.find(search_text, search_start_idx)

        if substr_start_idx == -1:
            return substr_count 

        search_start_idx = substr_start_idx + len_substr
        substr_count += 1


# def solution(full_text, search_text):
#     substr_count = 0
#     search_start_idx = 0
#     len_substr = len(search_text)

#     while True:
#         if full_text.count(search_text, search_start_idx) == 0:
#             return substr_count
        
#         substr_start_idx = full_text.index(search_text, search_start_idx)
#         search_start_idx = substr_start_idx + len_substr
#         substr_count += 1


# def solution(full_text, search_text):
#     substr_count = 0
#     search_start_idx = 0
#     len_substr = len(search_text)

#     while True:
#         try:
#             substr_start_idx = full_text.index(search_text, search_start_idx)
#         except ValueError:
#             return substr_count
#         else:
#             search_start_idx = substr_start_idx + len_substr
#             substr_count += 1


    

# Examples:
print(solution('abcdeb','b') == 2) # should return 2 since 'b' shows up twice
print(solution('aaabbbcccc', 'bbb') == 1) # should return 1