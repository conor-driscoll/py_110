"""
Write a function that takes a non-empty string `s` as input and finds the
minimum substring `t` and the maximum number `k`, such that the entire string
`s` is equal to `t` repeated `k` times.
P:
input: s (string)
output: return [t (min substring), k (max number)]
        (such that the entire string
        `s` is equal to `t` repeated `k` times)
explicit: str won't be empty

E: see below

D & A:
* current_substring = ''
* iterate through idx values creating progressively larger slices until 't' is found:
    * when 't' is found, return 't' and 'k' in list

C:
"""
# def min_substr_max_multiplier(string):
#     for end_pt_idx in range(1, len(string) + 1):
#         current_substring = string[:end_pt_idx]
#         multiplier = 1
#         current_substring_x_multiplier = current_substring * multiplier
        
#         while True:
#             if current_substring_x_multiplier == string:
#                 return [current_substring, multiplier]

#             if (current_substring_x_multiplier not in string or 
#                     len(current_substring_x_multiplier) > len(string)):
#                 break
            
#             multiplier += 1
#             current_substring_x_multiplier = current_substring * multiplier


def min_substr_max_multiplier(string):
    for end_pt_idx in range(1, len(string) + 1):
        current_substring = string[:end_pt_idx]
        multiplier = 1
        current_substring_x_multiplier = current_substring * multiplier
        
        while (current_substring_x_multiplier in string and 
                    len(current_substring_x_multiplier) <= len(string)):
            
            if current_substring_x_multiplier == string:
                return [current_substring, multiplier]

            multiplier += 1
            current_substring_x_multiplier = current_substring * multiplier
            

# Examples:
print(min_substr_max_multiplier("ababab") == ["ab", 3])# should return ["ab", 3]