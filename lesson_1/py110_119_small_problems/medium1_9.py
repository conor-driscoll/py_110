# * P:
#     * input: nth (Fibonacci number)
#     * output: (nth) Fibonacci number
#     * explicit: 
#         * must be a recursive solution using memoization
#         * F(1) = 1
#           F(2) = 1
#           F(n) = F(n - 1) + F(n - 2)    (where n > 2)
# * E: see below
# * D & A:
# * C:
# from os import system

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
    
#     if n in fibonacci_input_output:
#         return fibonacci_input_output[n]
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

# system('clear')

# while True:
#     stripped_input = input("--> Please enter a positive integer for 'n' to "
#                            "return the nth Fibonacci number.\n").strip()
#     try:
#         n = int(stripped_input)
#     except ValueError: 
#         pass
#     else:
#         if n >= 1:
#             break
    
#     system('clear')
#     print(f"Invalid input: '{stripped_input}'. Inputs must be positive "
#                "integers.\n")
    
# fibonacci_input_output = {}

# for num in range(1, n): 
#     fibonacci_input_output.setdefault(num, fibonacci(num))

# print(f'\nFibonacci number #{n}: {fibonacci(n)}.')

fibonacci_pairs = {}

def fibonacci(n):
    if n in (1, 2):
        return 1
    
    if n in fibonacci_pairs:
        return fibonacci_pairs[n]

    fibonacci_pairs[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_pairs[n]


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True