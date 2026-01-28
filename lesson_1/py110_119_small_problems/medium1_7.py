# * P:
#     * input: nth (Fibonacci number)
#     * output: (nth) Fibonacci number
#     * explicit: 
#         * recursive solutions not permitted
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
        
    f_n_minus_1, f_n_minus_2 = 1, 1

    for _ in range(n - 2):
        f_n = f_n_minus_1 + f_n_minus_2
        f_n_minus_2, f_n_minus_1 = f_n_minus_1, f_n

    return f_n
            

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
print(fibonacci(0))