# P:
# input: one string argument
# output: string w/ every consonant doubled
# explicit: 'a', 'e', 'i', 'o', 'u', digits, punctuation, and whitespace
#            shouldn't be doubled
# implicit:

# E: see below

# D:

# A:

# C:
VOWELS = 'aeiou'

def double_consonants(string):
    dub_str = ''
    
    for char in string: 
        if char.lower() not in VOWELS and char.isalpha():
            dub_str += char * 2
        else:
            dub_str += char

    return dub_str


# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")