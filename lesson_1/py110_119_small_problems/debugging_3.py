# Bug explanation:
# - lst isn't modified with this approach and a new lst isn't
#   created, so the argument is simply returned unchanged


def multiply_list(lst):
    new_lst = []
    
    for item in lst:
        new_lst.append(item * 2)

    return new_lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])