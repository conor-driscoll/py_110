# * P:
#     * input: lengths (unit-less) of triangle sides as three args
#     * output: return either 'equilateral', 'isosceles', 'scalene', or 'invalid'
#               as appropriate
#     * explicit:
#         * equilateral: all sides equal length
#         * isosceles: two sides equal length
#         * scalene: no sides equal length
#         * invalid:
#             * any side length <= 0
#             * sum(lengths two shortest sides) <= length longest side
# * E: see below
# * D & A:
# * C:
def invalid(side1, side2, side3):
    sides = [side1, side2, side3]

    if any(side <= 0 for side in sides):
        return True
            
    sides.sort()
    longest_side = sides.pop()
    if sum(sides) <= longest_side:
        return True

    return False


def triangle(side1, side2, side3):
    if invalid(side1, side2, side3):
        return 'invalid'

    if side1 == side2 == side3:
        return 'equilateral'

    if side1 != side2 and side2 != side3 and side1 != side3:
        return 'scalene'

    return 'isosceles'
            

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
