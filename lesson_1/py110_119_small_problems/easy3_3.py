# P:
# input: one string argument
# output: string w/ every char doubled
# implicit:
# explicit:

# E: see below

# D:

# A:
# def repeater(string):
# 1. intialize dub_str and assign it the value of ''
# 2. for each char in string:
#     1. dub_str += char * 2
# 3. return dub_str

# C:
def repeater(string):
    dub_str = ''
    
    for char in string: 
        dub_str += char * 2

    return dub_str


print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True