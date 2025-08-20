def sum(*args):
    print(*args)
    total = 0
    for item in args:
        total+=item   
    return total

print(sum(4,7,8,1))