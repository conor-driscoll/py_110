statement = "The Flintstones Rock"

letter_freq_dict = {}

for letter in statement:
    
    if letter == ' ':
        continue

    if letter not in letter_freq_dict:
        letter_freq_dict[letter] = 1
    else:    
        letter_freq_dict[letter] += 1

print(letter_freq_dict)
# Pretty printed for clarity
# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }