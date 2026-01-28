# P:
# input: string argument
# output: returns True if all parentheses in the string are "properly balanced",
#         and False otherwise
# explicit: balanced pairs must start with a "("
# implicit:

# E: see below

# D:

# A:

# C:
def is_balanced_paren(string):
    if string.count('(') == string.count(')'):
        left_parenthesis_count = 0
        right_parenthesis_count = 0
        for char in string:
            if char == '(':
                left_parenthesis_count += 1
            if char == ')':
                right_parenthesis_count += 1
            if right_parenthesis_count > left_parenthesis_count:
                return False
        return True

    else:
        return False


# Further exploration:

def is_balanced_q2(string):
    return string.count('"') % 2 == 0

def is_balanced_brack(string):
    if string.count('[') == string.count(']'):
        left_parenthesis_count = 0
        right_parenthesis_count = 0
        for char in string:
            if char == '[':
                left_parenthesis_count += 1
            if char == ']':
                right_parenthesis_count += 1
            if right_parenthesis_count > left_parenthesis_count:
                return False
        return True

    else:
        return False

def is_balanced_brace(string):
    if string.count('{') == string.count('}'):
        left_parenthesis_count = 0
        right_parenthesis_count = 0
        for char in string:
            if char == '{':
                left_parenthesis_count += 1
            if char == '}':
                right_parenthesis_count += 1
            if right_parenthesis_count > left_parenthesis_count:
                return False
        return True

    else:
        return False

def is_balanced(string):
    return all([is_balanced_paren(string), is_balanced_brack(string),
               is_balanced_brace(string), is_balanced_q2(string)])



print(is_balanced('What"" (is) this?') == True)        # True
print(is_balanced('"""What][ is) this?') == False)        # True
print(is_balanced("What (is{{} this?") == False)        # True
print(is_balanced("((What) (is{}{}{}[] this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True