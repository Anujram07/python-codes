def decorator(func):
    def wrapper():
        print("i am going to execute a functio .....")
        func()
        print("i have executed this  function....")
    return wrapper

@decorator
def hello():
    print("hello")

hello()

# f = decorator(hello)
# f()