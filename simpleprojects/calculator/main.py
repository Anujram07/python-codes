try:
    a = int(input("Enter a 1st number:"))
    b = int(input("Enter a 2nd number:"))

    print("What type of operation you want to Perform. Press + for Addition\nPress - for Substraction\nPress * for Multiplication\nPress / for Division")

    o = input("Enter the operation:")

    match o:
        case "+":
            print(f"Result is {a+b}")
        case "-":
            print(f"Result is {a-b}")
        case "*":
            print(f"Result is {a*b}")
        case "/":
            print(f"Result is {a/b}")
        case default:
            print("There is some error")


except Exception as e:
    print("Enter  a valid value please")