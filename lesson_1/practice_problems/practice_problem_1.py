fruits = ("apple", "banana", "cherry", "date", "banana")
produce = []
bad_input = ''

def count_banana(my_iterable):
    # counter = 0
    
    # for element in my_iterable:
    #     if element == 'banana':
    #         counter += 1
    
    # return counter


    return my_iterable.count('banana')


print(count_banana(fruits))    # 2
print(count_banana(produce))   # 0
print(count_banana(bad_input)) # 0