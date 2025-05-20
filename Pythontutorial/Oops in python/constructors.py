class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the Employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

    
e1 = Employee(3500, "Yudhveer", 3)
e1.get_info()