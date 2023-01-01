# Procedural Programming
# baseSalary = 30000
# overtime = 10
# rate = 20


# def getWage(baseSalary, overtime, rate):
#     return baseSalary + (overtime * rate)


# print("employee 1 total salary is {}".format(
#     getWage(baseSalary, overtime, rate)))

# ////////////////////////////////////////////////////////

# Object Oriented Programming
# class Employee():
#     baseSalary = 30000  # Attribute
#     overtime = 10  # Attribute
#     rate = 20  # Attribute

#     def getWage(self):
#         return self.baseSalary + (self.overtime * self.rate)


# employee1 = Employee()  # object of the class
# print("employee 1 total salary is {}".format(employee1.getWage()))

# /////////////////////////////////////////////////////////////////////////

# OOP
class Employee():
    baseSalary = 30000  # Attribute
    overtime = 10  # Attribute
    rate = 20  # Attribute

    def getWage(self):
        return self.baseSalary + (self.overtime * self.rate)


Mark = Employee()  # object of the class
print(f"Mark salary: {Mark.baseSalary}")

Harry = Employee()
Harry.baseSalary = 20000
print(f"Harry salary: {Harry.baseSalary}")

Mark.rate = 30000
print(Mark.rate)

employee1 = Employee()
# print(employee1.getWage())
print("employee 1 total \
salary is {}".format(employee1.getWage()))
