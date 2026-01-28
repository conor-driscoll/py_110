# P:
# input: string argument
# output: return list of all palindromic substrings of string
# explicit: substrings should be sorted by appearance order in input string
#           palindromes should be > 1 char and be case sensitive 

# E: see below

# D:

# A:
# def is_palindrome(string):
#     if len(string) == 1:
#         return False
    
#     for idx in range(int(len(string) / 2)):
#         if string[idx] != string[-(idx + 1)]:
#             return False

#     return True    

# def palindromes(string):
#     [substring for substring in substrings(string) if is_palindrome(substring)]


# C:
def leading_substrings(string):
    return [string[:end] for end in range(1, len(string) + 1)]


def substrings(string):
    return [substring for start in range(len(string))
                      for substring in leading_substrings(string[start:])]


def is_palindrome(string):
    if len(string) == 1:
        return False
    
    for idx in range(int(len(string) / 2)):
        if string[idx] != string[-(idx + 1)]:
            return False

    return True
        

def palindromes(string):
     return [substring for substring in substrings(string)
             if is_palindrome(substring)]


print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True