#class ka use krenge isme

class Employee:
    company = "Dell"

    def get_salary(self):
        print(self)
        return 34000
    
e = Employee() #An object of class employee is created
print(e.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)