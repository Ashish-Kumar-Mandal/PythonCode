class A:
    var1 = "I am a class variable of class A"

    def __init__(self):
        self.data = 101
        self.var1 = "I am a instant variable of class A"
        self.special = "I am Special variable"

class B(A):
    var1 = "I am a class variable of class B"

    def __init__(self):
        super().__init__()
        self.data = 1045
        self.var1 = "I am a instant variable of class B"


a = A()
b = B()

# print(b.special)
print(b.var1)