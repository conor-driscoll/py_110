# * P:
#     * input: nested lst w/ M sublists w/ N elements, representing a MxN matrix.
#     * output: return new nested list, representing transposed version of
#       original matrix
#     * implicit: input matrices will have 1 row, 1 column min
# * E: see below
# * D & A:
# * C:
def transpose(matrix):
    return [list(column) for column in zip(*matrix)]

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)