# * P:
#     * input: integer
#     * output: return a version of this integer that has undergone maximum
#               rotation
#     * maximum rotation:
#         * the leftmost digit is rotated to the end
#         * the new leftmost digit is held in place, and the new 2nd digit is
#           rotated to the end
#         * the two leftmost digits are held in place, and the 3rd digit is
#           rotated
#         * repeat this process len(str(digit)) - 1 times
# * E: (see below)
# * D & A:
#     * turn the number into a list of string digits (digit_lst)
#     * create an empty result_lst
#     * for _ in range(len(digit_lst)):
#         * pop off the 1st digit of digit_lst and add it to the end of digit_lst
#         * pop off the new 1st digit of digit_lst and add it to result_lst
#     * return int(joined result_lst)

# * C:
def max_rotation(number):
    digit_lst = list(str(number))
    result_lst = []
    
    for _ in range(len(digit_lst)):
        digit_lst.append(digit_lst.pop(0))
        result_lst.append(digit_lst.pop(0))

    return int(''.join(result_lst))


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

    
