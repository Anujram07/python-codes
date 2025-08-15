class employee:
    company = "asus"



    def __init__(self,salary,name,bond,company):
       self.salary=salary
       self.name = name
       self.bond = bond
       self.company = company

    def get_salary(self):
      return self.salary
    
    def get_info(self):
       print(f"The name of the employee is {self.name}. Salary is {self.salary} and bond is {self.bond}")

e1 = employee(34000,"simon",4,"micro")
print(e1.company)



#object introspection

print(dir(e1))