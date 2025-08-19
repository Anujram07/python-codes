def division(a,b):
    try :
        c = a/b
        print(c)
        return c
    
    except Exception as e :
        print(e)
        return None
    
    finally:
        print("this will always executed")








a = int(input("enter a number 1:"))
b = int(input("enter a number 2:"))
division(a,b)