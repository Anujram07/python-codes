def fibonacci(n):
    #base condition
    if(n==0 or n==1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)



print(fibonacci(7))

