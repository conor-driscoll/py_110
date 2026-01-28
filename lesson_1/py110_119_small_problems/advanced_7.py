# * P:
#     * input: a rational number as an arg, represented using the fraction module
#     * output: return a list representing all the denominators required to
#               represent the input rational number as an Egyptian fraction
# * E: see below
# * D & A:
# * C:
from fractions import Fraction

def egyptian(rational_num):
    denominator = 1
    total = 0
    denom_lst = []
    
    while True:
        if Fraction(1, denominator) + total <= rational_num:
            total += Fraction(1, denominator)
            denom_lst.append(denominator)
            if total == rational_num:
                return denom_lst
        denominator += 1


def unegyptian(lst):
    return sum(Fraction(1, num) for num in lst)



# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))