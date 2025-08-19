def greter9(x):
    if x>9:
        return True
    else :
        return False
    

a = [4,5,2,1,9,8,7,45,14]

new = list(filter(greter9,a))
print(new)