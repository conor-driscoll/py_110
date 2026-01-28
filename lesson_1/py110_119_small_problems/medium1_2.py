# P:
# input: number, count (from left)
# output: number w/ flagged digit extracted and placed on end
# explicit:
# implicit:

# E: see below

# D:

# A:

# C:

def rotate_rightmost_digits(number, count_from_right):
    digit_lst = list(str(number))
    one_digit_lst = [digit_lst.pop(-count_from_right)]
    final_lst = digit_lst + one_digit_lst

    return int(''.join(final_lst))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True