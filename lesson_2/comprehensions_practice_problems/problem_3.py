lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_lst = []
# for sub_lst in lst:
#     new_lst.append(sorted(sub_lst, key=str))
# print(new_lst)

print([sorted(sub_lst, key=str) for sub_lst in lst])