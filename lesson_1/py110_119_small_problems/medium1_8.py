# * P:
#     * input: nth (Fibonacci number)
#     * output: (nth) Fibonacci number
#     * explicit: 
#         * must be a recursive solution
#         * F(1) = 1
#           F(2) = 1
#           F(n) = F(n - 1) + F(n - 2)    (where n > 2)
# * E: see below
# * D & A:
# * C:
def fibonacci(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError(f'Invalid input: {n!r}. Inputs must be positive '
                          'integers.')
    
    if n in (1, 2):
        return 1
        
    return fibonacci(n - 1) + fibonacci(n - 2)    
    
    
    # n = 5
    # return f(4)               + f(3)
    # return f(3)        + f(2) + f(2) + f(1)
    # return f(2) + f(1) + 1    + 1    + 1

    # n = 6
    # f(5)                             + f(4)
    # f(4)               + f(3)        + f(3)        + f(2)
    # f(3)        + f(2) + f(2) + f(1) + f(2) + f(1) + 1
    # f(2) + f(1) + 1    + 1    + 1    + 1    + 1    + 1


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(0))