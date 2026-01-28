# P:
# input: dictionary argument
# output: dictionary with keys and values inverted
# explicit:
# implicit:

# E: see below

# D:

# A:
# def invert_dict(input_dict):
#     return dict(zip(input_dict.values(), input_dict.keys()))

# C:
def invert_dict(input_dict):
    return dict(zip(input_dict.values(), input_dict.keys()))


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True