# while True:
#     try:
#         a = int(input("Enter a number 1:"))
#         b = int(input("Enter a number 2:"))

#         print(f"sum is {a/b}")
#     except ValueError:
#         print("pls dont perform bad calculation")

#     except ZeroDivisionError:
#         print("zero se divide mat kar ")
#     except Exception as e:
#         print("some error occur",e)


a = int(input("Enter a number 1:"))
b = int(input("Enter a number 2:"))
if b == 0:
    raise ValueError("please dont divide by 0")
print(f"division is {a/b}")