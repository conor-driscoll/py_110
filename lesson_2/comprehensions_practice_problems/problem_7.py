lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# three_multiple_lst = []

# for sublst in lst:
#     sublst_3_multiple = []
    
#     for num in sublst:
#         if num % 3 == 0:
#             sublst_3_multiple.append(num)
    
#     three_multiple_lst.append(sublst_3_multiple)

# print(three_multiple_lst)

print([[num for num in sublst if num % 3 == 0] 
            for sublst in lst])
