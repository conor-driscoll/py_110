# Code problem:
# - This code will behave unexpectedly, because a built-in function name is
#   used to name a custom function. Therefore, this custom function name
#   shadows the name sum, and when there is an attempted call of the built-in
#   sum function within the function body, there is an attempted call of the
#   custom sum function instead.  

def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)