# * P:
#     * input: (two separate args) sorted list (elements will be either all ints
#              or all strs), search item (will be same data type as list)
#     * output: index of item if found, -1 if not found
#     * explict: use 'binary search' algorithm
#     * implicit: list won't be empty
# * E: see below
# * D & A:
# * C:
def binary_search(lst, item):
    lower_bound_idx = 0
    upper_bound_idx = len(lst) - 1
    
    while lower_bound_idx <= upper_bound_idx:
        mid_pt_idx = (upper_bound_idx + lower_bound_idx) // 2
        mid_pt_item = lst[mid_pt_idx]
        
        if item == mid_pt_item:
            return mid_pt_idx
        if item > mid_pt_item:
            lower_bound_idx = mid_pt_idx + 1
        else:
            upper_bound_idx = mid_pt_idx - 1
        
    return -1


# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)