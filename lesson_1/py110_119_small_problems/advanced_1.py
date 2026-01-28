# * P:
#     * input: nested lst w/ 3 sublists w/ 3 elements, representing a 3x3 matrix.
#     * output: return new nested list, representing transposed version of
#       original matrix
# * E: see below
# * D & A:
# * C:
def transpose(matrix):
    return [list(column) for column in zip(*matrix)]
    

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True