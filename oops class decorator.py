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



ak = Employee("Ashish Kumar", "8228972907")
bk = Employee("Babby Kumari", "9876541230")

bk.display()
print(bk.__dict__)

ak.new_leaves(50)
ak.display()

bk.leaves = 45
bk.display()
print(bk.__dict__)
