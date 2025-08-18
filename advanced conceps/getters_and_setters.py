class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    @property
    def firstname(self):
        l = self.name.split(" ")
        return l[0]
    

    @firstname.setter
    def firstname(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = employee("jack doe", 34555)
e.projects = 6
# print(e.firstname())
# e.setfirstname("john")
# print(e.name)


print(e.firstname)
e.firstname = "john"
print(e.name)
