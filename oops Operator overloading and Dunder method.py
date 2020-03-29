class Employee:
    """This is a class for Employee."""
    company = "SunSarthi"
    leaves = 10

    def __init__(self, name, mob):
        self.name = name
        self.salary = mob

    def display(self):
        print(f"Company Name: {self.company}\nNumber of leaves: {self.leaves} days\nYour Name: {self.name}\nYour Mobile number: {self.salary}")

    def __add__(self, other):   # Operator overloading adn Dunder method
        return self.salary + other.salary

    def __truediv__(self, other):   # Operator overloading
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"

    def __str__(self):
        return f"Company Name: {self.company}\nNumber of leaves: {self.leaves} days\nYour Name: {self.name}\nYour Mobile number: {self.salary}"


obj = Employee("Ashish Kumar", 120)
# obj2 = Employee("Sonam", 23)

# print(obj / obj2)
# print(obj)
# print(repr(obj))
print(str(obj))