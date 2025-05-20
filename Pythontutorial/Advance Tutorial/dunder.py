class Employee:
    company = "Dell"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.salary} and the salary is {self.salary}"

    def __repr__(self):
        return f"name:{self.name}\nSalary:{self.salary}"
        

e = Employee ("Harry", 34900)
print(e.name, e.salary)\

print(str(e))

print(repr(e))