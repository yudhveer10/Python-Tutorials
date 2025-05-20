class Employee:

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the Employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

    
e1 = Employee(3500, "Yudhveer", 3, "BMW")
# e2 = Employee(4000, "Arun", 2, "NISSAN")

# e2.get_info()
print(e1.company)

print(Employee.company)
