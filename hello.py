# print("hello")
# print(3)
# print("hi \nhello")

# x = 10
# y = 54
# print(id(x),id(y))


# a= "hi"
# print(id(a))

# a = a+"there"
# print(id(a))

# a = [1,2,3]
# print((id(a)))
# b = a
# b.append(4)
# b = a.copy()
# print(id(a))
# print(("shirish kurariya"))


# type function

# a = 10
# print(type(type(a)))
# print(type(a))

# a = "sfede is a slkd"
# print(type(a))

# def func():
#     pass

# print(type(func()))
# '''doc string is written inside triple quotes'''

# class demo:
#     pass

# print(type(demo()))
# help()




def fact(n):
    """hello this is program for a factoial"""
    if(n==0 or n==1):
        return 1
    
    return n*fact(n-1)
    


print(fact(5))
# help(fact)
help(fact)