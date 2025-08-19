# produce = {
#     'apple': 'Fruit',
#     'carrot': 'Vegetable',
#     'pear': 'Fruit',
#     'broccoli': 'Vegetable',
# }

# def select_fruit(input_dict):

#     only_fruit_dict = { key: value for key, value in input_dict.items()
#                         if value == 'Fruit' }

#     return only_fruit_dict

# print(select_fruit(produce))  # {'apple': 'Fruit', 'pear': 'Fruit'}



# my_numbers = [1, 4, 3, 7, 2, 6]

# def double_numbers(numbers): # This function mutates its argument

#     # for idx, current_num in enumerate(numbers):
#     #     numbers[idx] = current_num * 2

#     for idx, _ in enumerate(numbers):
#         numbers[idx] *= 2

# print(double_numbers(my_numbers)) # None
# print(my_numbers)                 # [2, 8, 6, 14, 4, 12]



# my_numbers = [1, 4, 3, 7, 2, 6]

# def double_numbers(numbers): # This function mutates its argument

#     for idx, _ in enumerate(numbers):
#         if idx % 2 == 1:
#             numbers[idx] *= 2

# print(double_numbers(my_numbers)) # None
# print(my_numbers)                 # [2, 8, 6, 14, 4, 12]



my_numbers = [1, 4, 3, 7, 2, 6]

def multiply(numbers, factor):
    
    new_list = []

    for current_number in numbers:
        new_list.append(current_number * factor)

    return new_list

print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]