# * P:
#     * input: one list as arg (values will be either all int or all str)
#     * output: return new, ascending-order list sorted using the 'merge sort'
#               algorithm
#     * implicit: from the test cases (below), it is implied that all arg lists
#                 will have at least two elements
# * E: see below
# * D & A:
# * C:
def merge(lst1, lst2):
    lst1_copy, lst2_copy = lst1.copy(), lst2.copy()
    merged_lst = []
    
    while lst1_copy and lst2_copy:
        if lst1_copy[0] <= lst2_copy[0]:
            merged_lst.append(lst1_copy.pop(0))
        else:
            merged_lst.append(lst2_copy.pop(0))

    return merged_lst + lst1_copy + lst2_copy


def create_nested_structure(lst):
    len_lst = len(lst)
    if len_lst == 1:
        return lst

    mid_pt = len_lst // 2    
    return [create_nested_structure(lst[:mid_pt]),
            create_nested_structure(lst[mid_pt:])]


def sort_nested_to_flat(lst):
    if not isinstance(lst[0][0], list) and len(lst) == 1:
        return lst[0]
    
    if not isinstance(lst[0][0], list) and isinstance(lst[1][0], list):
        return merge(sort_nested_to_flat([lst[0]]),
                     sort_nested_to_flat(lst[1]))
    
    if isinstance(lst[0][0], list) and not isinstance(lst[1][0], list):
        return merge(sort_nested_to_flat(lst[0]),
                     sort_nested_to_flat([lst[1]]))

    if not isinstance(lst[0][0], list) and not isinstance(lst[1][0], list):
        return merge(lst[0], lst[1])
    
    return merge(sort_nested_to_flat(lst[0]), sort_nested_to_flat(lst[1]))

    
def merge_sort(lst):
    nested_structure = create_nested_structure(lst)
    return sort_nested_to_flat(nested_structure)
      


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)