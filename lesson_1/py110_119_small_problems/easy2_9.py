# P:
# input: one list argument
# output: print each element in the list argument, alongside the frequency of
#         each element's occurrence
# explicit: function should be case sensitive
# implicit: the argument list has only strings as its elements

# E: see below

# D:

# A:
# def count_occurrences(lst):
# 1. create set_lst
# 2. for each item in the set_lst argument:
#     print an f-string in the requested format

# C:
# def count_occurrences(lst):
#     set_lst = set(lst)
    
#     for item in set_lst:
#         print(f'{item} => {lst.count(item)}')

# Further exploration:
def count_occurrences(lst):
    casefold_lst = []

    for item in lst:
        casefold_lst += [item.casefold()]

    print(casefold_lst)
    
    set_casefold_lst = set(casefold_lst)
    
    for item in set_casefold_lst:
        print(f'{item} => {casefold_lst.count(item)}')

vehicles = ['car', 'car', 'truck', 'Car', 'SUV', 'truck',
            'motorcycle', 'motOrcycle', 'car', 'truCK']

count_occurrences(vehicles)

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2