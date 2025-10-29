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




# def fact(n):
#     """hello this is program for a factoial"""
#     if(n==0 or n==1):
#         return 1
    
#     return n*fact(n-1)
    


# print(fact(5))
# # help(fact)
# help(fact)


# a = int(input("Enter a number:"))
# prime =True
# for i in range(2,a):
#     if i % a == 0:
#        print("is a prime ")
#        break;
#     else:
#        print("not a prime")
#        break;

# i = 0
# for i in range(0,100):
#     if i%2!=0:
#         print(i)

# a = int(input("Enter a number:"))
# sum = 0
# while(a>0):
#     digit = a%10
#     sum = sum + digit
#     a = a//10
# print(sum)

# a = input("Enter a number:")
# sum  = 0
# for a in str(a):
#     sum = sum + int(a)
# print(sum)

def fib(n):
    a,b = 0,1
    while(a<n):
        print(a)
        a,b = b,b+a


(fib(20))