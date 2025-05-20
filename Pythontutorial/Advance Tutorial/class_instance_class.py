class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary

    #Instance Method
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum (a, b):
        return a+b
    
    @classmethod
    def print_company(cls):
        print(cls.company)


    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company




e1 = Employee("Jackson", 32000)
e2 = Employee("Jill", 30000)

# print(Employee.company)
# e1.print_info()
# e2.print_info()
# # print(Employee.name)

# print(e2.sum(5, 23))

e1.print_company()
e1.change_company("DELL")
e1.print_company()

    