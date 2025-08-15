class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
    def print(self):
        print(f"x is {self.x} and y is {self.y}")  # Direct print


    def __add__(self, p):
        return point((self.x + p.x), (self.y + p.y))

p1 = point(3, 2)
p2 = point(5, 7)

# p = p1.sum(p2)
# p.print()  # This will now display output


p = p1+p2 # we overloaded sum operator by __
p.print()