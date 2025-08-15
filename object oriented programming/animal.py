class animal:
    location = "house"
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("generic animal sound")



class dog(animal):
    def speak(self):
        super().speak()
        print("woof")


d = dog("bruno")
d.speak()
print(d.location)

# a.speak()