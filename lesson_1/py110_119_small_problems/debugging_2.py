# Problems with function:
# - changing an iterable during iteration an is not advisable
# - iterating in reverse order will be helpful


def reverse_string(string):
    new_string = ''
    
    for char in string[::-1]:
        new_string += char 

    return new_string

print(reverse_string("hello") == "olleh")