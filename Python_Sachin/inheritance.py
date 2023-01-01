class Employee():
    def __init__(self, baseSalary, overtime, rate):
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate

    def getWage(self):
        return self.baseSalary + (self.overtime * self.rate)


# inheritance
class Engineer(Employee):
    def __init__(self, baseSalary, overtime, rate):
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate


Mark = Engineer(1000, 15, 10)
print(Mark.getWage())

Harry = Engineer(1500, 12, 15)
print(Harry.getWage())
