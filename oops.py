class Employee:
    """This is a class for Employee."""
    comp_name = "SunSarthi"

    def __init__(self, role, name, mob, email, add):
        self.role = role
        self.name = name
        self.mob = mob
        self.email = email
        self.add = add

    def display(self):
        print(f"Company is: {self.comp_name}\nDesination is: {self.role}\nName is: {self.name}\nMobile number is: {self.mob}\nEmail id is: {self.email}\nAddress is: {self.add}")

    # def info_display(self):
    #     print(f"Age is {self.age}\nSalary is {self.salary}\nMarital status is {self.married}\nReligion is {self.comp_name}")
    pass

obj = Employee("Programmer", "Ashish Kumar", "8228972907", "666kmandal@gmail.com", "Giridih Jharkhand")
obj.display()

print(obj.__doc__)

# rani = Employee()
# raja = Employee()

# rani.age = 105
# rani.salary = 10000
# rani.married = "yes"
#
# raja.age = 25
# raja.salary = 502400
# raja.married = "No"
# raja.role = "CEO"

# raja.info_display()

# print(rani)
# for k, v in rani.__dict__.items():
#     print(f"{k} => {v}")
#
# print(raja)
# for k, v in raja.__dict__.items():
#     print(f"{k} => {v}")
#
# print(Employee)
# for k, v in Employee.__dict__.items():
#     print(f"{k} => {v}")