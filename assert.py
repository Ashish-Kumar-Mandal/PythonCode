a, b = input("Enter a and b: ").split(" ")
assert int(b) != 0, "Divisible by zero is not possible. Try again..."
print(f"{a} / {b} = {int(a) / int(b)}")