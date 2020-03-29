# object introspection: is a details about object

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property   # it is used for without use () of this method.
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, eml):
        self.fname, self.lname = (eml.split("@")[0]).split(".")

    @email.deleter
    def email(self):
        self.fname, self.lname = None, None


ak = Employee("Ashish", "Kumar")
o = "This is string"

# print(type(ak))
# print(type(o))
# print(id(ak))
# print(id(o))
# print(dir(ak))
# print(dir(o))

import inspect
print(inspect.getmembers(ak))
