class Employee():
    def __init__(self, baseSalary, overtime, rate):
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate

    def getWage(self):
        return self.baseSalary + (self.overtime * self.rate)


employee1 = Employee(20000, 13, 20)
print("employee 1 total \
salary is {}".format(employee1.getWage()))

employee2 = Employee(20000, 12, 15)  # object 2 of class Employee
print("employee 2 total \
salary is {}".format(employee2.getWage()))
