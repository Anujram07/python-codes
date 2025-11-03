# square = lambda x:x*x

# x = int(input("Enter a number:"))
# y = int(input("Enter a number:"))

# sum = lambda x,y: x+y

# print(sum(5,2))
# print(square(4))

# numbers =[1,2,3,4]
# squared =list(map(lambda x: x**2, numbers))

# print(squared) # Output: [1, 4, 9, 16]

num = 12345
sum_of_digit = lambda a : sum(map(int,str(a)))

print(sum_of_digit(num))
