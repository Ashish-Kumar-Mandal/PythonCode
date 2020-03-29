from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Square(Shape):
    type = "Square"

    def __init__(self, s):
        self.s = s

    def printarea(self):
        print(f"Area of {self.type} = {self.s * self.s}")


class Rectangle(Shape):
    type = "Rectangle"
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def printarea(self):
        print(f"Area of {self.type} = {self.l * self.b}")


class Cube(Shape):
    type = "Cube"

    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def printarea(self):
        print(f"Area of {self.type} = {self.l * self.b * self.h}")


s = Square(45)
s.printarea()

r = Rectangle(45, 69)
r.printarea()

c = Cube(45, 69, 85)
c.printarea()