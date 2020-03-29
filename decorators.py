def decorator(add):
    def decorator_exc():
        print("Decorator Executing...")
        add()
        print("Done")
    return decorator_exc

# @decorator
def add():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(f"{a}+{b} = {a+b}")

add = decorator(add)
add()
