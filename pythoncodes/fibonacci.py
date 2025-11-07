def fibonacci(num):
    return num if num <=1 else fibonacci(num-1) + fibonacci(num-2)
nterms = 10
for num in range(nterms):
    print(fibonacci(num))