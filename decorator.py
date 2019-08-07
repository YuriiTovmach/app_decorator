def decorator (func):
    def wrapper():
        print("cod befor")
        func()
        print("cod after")
    return wrapper

@decorator
def show():
    print("I am simple function")

show = decorator (show)
show()
