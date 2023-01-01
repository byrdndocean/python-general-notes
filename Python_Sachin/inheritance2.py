class Employee():
    def __init__(self, baseSalary, overtime, rate):
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate

    def getWage(self):
        return self.baseSalary + (self.overtime * self.rate)


# inheritance between Enginerr and Employee
class Engineer(Employee):
    def __init__(self, baseSalary, overtime, rate):
        print(
            f"I am an Engineer and my salary is: {baseSalary + overtime * rate}")


# inheritance between Doctor and Employee
class Doctor(Employee):
    def __init__(self, baseSalary, overtime, rate):
        # print(
        #     f"I am a Doctor and my salary is: {baseSalary + overtime * rate}")

        # super class points to the Employee class
        super().__init__(baseSalary, overtime, rate)
        # we can use super in order to call the method that's inside the parent class


Ross = Doctor(2000, 23, 70)
print(Ross.getWage())

# Mark = Engineer(1000, 15, 10)
# print(Mark.getWage())

# Harry = Engineer(1500, 12, 15)
# print(Harry.getWage())
