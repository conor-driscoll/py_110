# Problem(s) w/ code:
# - this function modifies the same list every time it is called, leading to
#   unintended consequences

def append_to_list(value, lst=[]):
    copy_lst = list(lst)
    copy_lst.append(value)
    return copy_lst


print(append_to_list(1) == [1])
print(append_to_list(2) == [2])