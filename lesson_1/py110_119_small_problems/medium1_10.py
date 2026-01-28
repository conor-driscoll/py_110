# * P:
#     * input: int specifying number of Fibonacci digits
#     * output: returns index of first number in the seq w/ that number of digits
#     * explicit: arg is int >= 2
# * E: see below
# * D & A:
# * C:
import sys
sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(length):
    fib_cache = {1: 1, 2: 1}
    n = 3

    while True:
        fib_cache[n] = fib_cache[n - 1] + fib_cache[n - 2]
        
        if len(str(fib_cache[n])) == length:
            return n

        n += 1    


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)