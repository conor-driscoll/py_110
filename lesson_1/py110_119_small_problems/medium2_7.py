# * P:
#     * input: list with at least two elements as argument
#     * output: return same list, sorted using the 'bubble sort' algorithm
#     * implicit: 
#         * for sorting order rules, default rules are sufficient
#         * all elements of arg lists will be of the same data type
# * E: see below
# * D * A:
# * C:
def bubble_sort(lst):
    sort_potentially_complete = False
    while not sort_potentially_complete:
        sort_potentially_complete = True
        for idx in range(len(lst) - 1):
            bubble_item1 = lst[idx]
            bubble_item2 = lst[idx + 1]
            if bubble_item1 > bubble_item2:
                lst[idx] = bubble_item2
                lst[idx + 1] = bubble_item1
                sort_potentially_complete = False



lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True