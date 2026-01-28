# * P:
#     * input: two sorted lists as two args (values will be either all int or all
#              str)
#     * output: return one, ascending-order 'merged' list (no input list mutation
#               or post-creation output list sorting allowed)
# * E: see below
# * D & A:
# * C:
def merge(lst1, lst2):
    lst1_copy, lst2_copy = lst1.copy(), lst2.copy()
    merged_lst = []
    
    while lst1_copy or lst2_copy:
        if lst1_copy and not lst2_copy:
            merged_lst.extend(lst1_copy)
            break
        if lst2_copy and not lst1_copy:
            merged_lst.extend(lst2_copy)
            break
        if lst1_copy[0] <= lst2_copy[0]:
            merged_lst.append(lst1_copy.pop(0))
        else:
            merged_lst.append(lst2_copy.pop(0))

    return merged_lst

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)