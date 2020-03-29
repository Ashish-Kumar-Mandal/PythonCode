class Employee:
    """This is a class for Employee."""
    company = "SunSarthi"
    leaves = 10

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


ak = Employee.from_dash("Ashish Kumar-8228972907")
ak.display()