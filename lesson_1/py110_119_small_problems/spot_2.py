"""
Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).


P:
input: int lst as arg
output: return pair count as int
explicit: each pair of equal ints must be separated by at
    least one other int

E: provided below

D & A:

1:
* iterate through int list using enumerate
* create dict with idxs as keys, and ints as values
* create copy_dict
* pair_count = 0
* iterate through key, value items
* del key-value pair in copy_dict
* if value in copy_dict and copy_dict key > key + 1:
    * increment pair_count by one
    * del key-value pair in copy_dict
* return pair_count

C:
"""
# def pairs(int_lst):
#     idx_int = {idx: num for idx, num in enumerate(int_lst)}
#     idx_int_copy = idx_int.copy()
#     pair_count = 0

#     for idx, num in idx_int.items():
#         if idx in idx_int_copy:
#             del idx_int_copy[idx]

#         if num in idx_int_copy.values():
#             for idx_copy, num_copy in idx_int_copy.items():
#                 if num == num_copy and idx_copy > idx + 1:
#                     pair_count += 1
#                     del idx_int_copy[idx_copy]
#                     break
    
#     return pair_count


# PREVIOUSLY_PAIRED_PLACEHOLDER = 'X'

# def pairs(num_lst):
#     working_lst = num_lst.copy()
#     pair_count = 0

#     while len(working_lst) > 2:
#         current_num = working_lst.pop(0)

#         for idx, element in enumerate(working_lst):
#             if idx == 0 or element == PREVIOUSLY_PAIRED_PLACEHOLDER:
#                 continue

#             if element == current_num:
#                 pair_count += 1
#                 working_lst[idx] = PREVIOUSLY_PAIRED_PLACEHOLDER

#     return pair_count


# def pairs(num_lst):
#     pair_count = 0
#     used_pair_idx_2 = []

#     for pair_idx_1 in range(len(num_lst) - 2):
        
#         for pair_idx_2 in range(pair_idx_1 + 2, len(num_lst)):
            
#             if pair_idx_2 not in used_pair_idx_2 and num_lst[pair_idx_1] == num_lst[pair_idx_2]:
#                 pair_count += 1
#                 used_pair_idx_2.append(pair_idx_2)
#                 break

#     return pair_count


# Examples:
print(pairs([1, 2, 5, 6, 5, 2]) == 2)
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2]) == 4)