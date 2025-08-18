class employee:
    company = "HP"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    

    # instance method(default)
    def print_info(self):
        info =  f" The name is {self.name} and salary is {self.salary}"
        print(info)

    #static method
    @staticmethod
    def sum (a,b):
        return a + b
    #class methods
    @classmethod
    def print_company(cls):
        print(cls.company)


    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1 = employee("jack", 34000)
e2 = employee("jill", 34440)
# print(employee.company)

# e1.print_info()
# e2.print_info()

# 

print(employee.company)
e1.change_company("acer")
e1.print_company()