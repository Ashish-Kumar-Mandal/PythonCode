# def my_table(*args):
#     for i in range(1, 11):
#         for j in args:
#             print(f"{i*j:{len(str(j*10))}d}", end=" | ")
#         print()
#
# lst = [2, 3, 5, 9, 5, 25, 23652, 1025634]
#
# try:
#     my_table(*lst)
# except BaseException:
#     pass

def table(a, b):
    for i in range(1, 11):
        for j in range(a, b+1):
            print(f"{i*j:{len(str(j*10))}d}", end=" | ")
        print()

a, n = input("Enter range a to n: (separated by space): ").split(" ")

try:
    table(int(a), int(n))
except BaseException:
    pass