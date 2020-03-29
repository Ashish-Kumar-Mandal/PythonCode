# Positional only argument function

# def my_pow(a, n):
#     """This is take exact two input only and return power of a^n."""
#     return a**n
#
# print(my_pow.__doc__)
# print(my_pow(3, 5))


# Positional_or_keyword both argument function

def my_table(*args):
    for i in range(1, 11):
        for j in args:
            print(i*j, end=" | ")
        print()

table = [2,5,6,4,8,9]
my_table(*table)


# Keyword only argument function

# def my_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} lives in {value}")
#
# d = {"Ashihs":"Giridih", "Sanjeev":"Devghar", "Babblu":"Dhanbad", "Shubham":"bokaro"}
# my_info(**d)