a = 2
b = [5, 8]
lst = [a, b]
# lst = [2, [5, 8]]

lst[0] += 2
# lst = [4, [5, 8]]
lst[1][0] -= a
# 5 -= 2

print(a == 2)
print(b == [3, 8])