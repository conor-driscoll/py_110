"""
Write a function that takes a string of integers as input and returns the
number of substrings that result in an odd number when converted to an integer.

P:
input: string of ints as arg
output: return number of substrings that result in odd number when converted to int

E: see below

D & A: (first solution)
* odd_substring_count = 0
* iterate through string digits
    * iterate through substrings starting with that first digit
        * if the final digit in substring is odd
            * increment odd_substring_count
* return odd_substring_count

C:
"""
def solve(digit_str):
    odd_substring_count = 0

    for slice_start_idx in range(len(digit_str)):
        for slice_end_idx in range(slice_start_idx + 1, len(digit_str) + 1):
            current_substring = digit_str[slice_start_idx:slice_end_idx]
            
            if int(current_substring[-1]) % 2 == 1:
                odd_substring_count += 1

    return odd_substring_count


def solve(digit_str):
    odd_substring_count = 0

    for idx, str_digit in enumerate(digit_str):
        if int(str_digit) % 2 == 1:
                odd_substring_endpoint_count = idx + 1
                odd_substring_count += odd_substring_endpoint_count

    return odd_substring_count


# Examples:
print(solve("1341") == 7) # should return 7
print(solve("1357") == 10) # should return 10