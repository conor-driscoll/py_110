lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_sum(num_lst):
    return sum([num for num in num_lst if num % 2 != 0])

print(sorted(lst, key=odd_sum))
