f = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
a = ["Ashish", "Sanjeev"]

# f.append("Grapes")
# print(f)
# #OR
# f[len(f):] = ["Grapes"]
# print(f)
#
# f.append(a)
# print(f)

# a.extend(a)
# print(a)
# f.extend(a)
# print(f)
# f[len(f):] = a
# print(f)

# del f[0]
del f[1:3]
print(f)

# f.remove("banana")
# print(f)

# f.clear()
# print(f)
# # OR
# del f[2:4]
# print(f)

# c = f.copy()
# print(c)
# # OR
# b = f[:]   # copy of entire list
# print(b)
# b.clear()
# print(b)
# print(f)

# r = f.index("banana")
# r1 = f.index("banana", 4)
# r2 = f.index("banana", 4, 7)
# print(r)
# print(r1)
# print(r2)

# f.sort()    # Ascending order
# print(f)
# f.sort(reverse=True)    # Descending order
# print(f)