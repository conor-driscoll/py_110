# * P:
#     * input: postive integer as an argument
#     * output: difference between the square of the sum of the first 'count'
#               positive integers and the sum of the squares of the first 'count'
#               positive integers
# * E: see below
# * D & A:
# * C:
def sum_square_difference(count):
    square_of_sum = sum(range(1, count + 1))**2 
    sum_of_squares = sum(integer**2 for integer in range(1, count + 1))
    return square_of_sum - sum_of_squares



print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True