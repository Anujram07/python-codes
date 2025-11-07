a = int(input("Enter a number between 1 and 10"))

match a:
    case 1:
        print("Hey, you won a camera")
    case 3:
        print("you won an i phone")
    case 7:
        ("you won bat")
    case _:
        print("Better luck next Time")