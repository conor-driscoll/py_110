# * P:
#     * input: angles (in degrees) of a triangle as three args
#     * output: return either 'right', 'acute', 'obtuse', or 'invalid'
#               as appropriate
#     * explicit:
#         * right: one angle == 90
#         * obtuse: one angle > 90
#         * acute: all angles < 90
#         * invalid:
#             * any angle <= 0
#             * sum(all angles) == 180
#             * All angle arguments will be integer values.
# * E: see below
# * D & A:
# * C:
def is_invalid(angles):
    return any(angle <= 0 for angle in angles) or sum(angles) != 180


def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    
    if is_invalid(angles):
        return 'invalid'

    if 90 in angles:
        return 'right'

    if any(angle > 90 for angle in angles):
        return 'obtuse'

    return 'acute'
            

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True