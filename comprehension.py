# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a = [x**2 for x in a]
# print(a)

x = (i**2 for i in range(30) if i%3==0)
print(x)
#
# res = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(res)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# x = [[row[i] for row in matrix] for i in range(4)]
# print(x)