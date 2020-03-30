class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view(self):
        print(f"Your Name: {self.name} and Age: {self.age}")


class child(parent):
    def __init__(self, name, age, salary):
        parent.__init__(self, name, age)
        self.salary = salary

    def view(self):
        print(f"Your Name: {self.name} and Age: {self.age} and also Salary: {self.salary}")


c = child("Ashish", 35, 70000)
c.view()