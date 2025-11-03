# a = input("Enter a string: ")
# palindrome = lambda a: a == a[::-1]
# print(palindrome(a))


a = int(input("Enter a number:"))
palindrome = lambda a : str(a) == str(a)[::-1]
print(palindrome(a))