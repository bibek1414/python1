def decorator1(x):
    def wrapper():
        print("0")
        print("1")
        x()
        print("2")
    return wrapper

@decorator1
def say_one():
    print("1.1")
say_one()

@decorator1
def say_two():
    print("2.1")
say_two()