class Employee:
    """This is a class for Employee."""
    company = "SunSarthi"
    leaves = 10
    public_var = "public var, all are access"
    _protected_var = "protected var, self and derived class are access"
    __private_var = "Private var, it is not access outside the class"

    def __init__(self, name, mob):
        self.name = name
        self.mob = mob

    def display(self):
        print(f"Company Name: {self.company}\nNumber of leaves: {self.leaves} days\nYour Name: {self.name}\nYour Mobile number: {self.mob}")

    @classmethod
    def new_leaves(cls, leave):
        cls.leaves = leave

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @classmethod
    def from_comma(cls, string):
        return cls(*string.split(","))

    @staticmethod
    def default_print(string):
        print(f"{string}, this is Static method in class")
        return

obj = Employee("Ashish Kumar", "8228972907")
# access of public variable
print(obj.public_var)
# access of protected variable
print(obj._protected_var)
# access of private variable
print(obj._Employee__private_var)   # It is called NameMangling