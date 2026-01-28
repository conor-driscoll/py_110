# P:
# input: string argument consisting of a first name, a space, and a last name,
#        in that order
# output: return string of the last name, a comma, and then the first name
# explicit:
# implicit:

# E: see below

# D:

# A:

# C:
# def swap_name(string):
#     return ', '.join(string.split()[::-1])

# print(swap_name('Joe Roberts') == "Roberts, Joe")   # True


# Further exploration:
def swap_name(name):
    name_lst = name.split()

    last_name_lst = [name_lst.pop() + ',']

    return ' '.join(last_name_lst + name_lst)


print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True