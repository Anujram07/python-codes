class employee:
    def __init__(self,salary,name,bond):
       self.salary=salary
       self.name = name
       self.bond = bond

    def get_salary(self):
      return self.salary
    
    def get_info(self):
       print(f"The name of the employee is {self.name}. Salary is {self.salary} and bond is {self.bond}")

e1 = employee(34000,"simon",4)
print(e1.get_info())