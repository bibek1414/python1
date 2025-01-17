# def decorator1(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function call")
#         result = func(*args, **kwargs)
#         print("After the function call")
#         return result
#     return wrapper

# @decorator1
# def say_hello(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# say_hello("Alice")
# say_hello("Bob", greeting="Hi")

def greet_decorator(greeting):
    def decorator1(func):
        def wrapper(*args, **kwargs):
            print(f"{greeting} before the function call")
            result = func(*args, **kwargs)
            print("After the function call")
            return result
        return wrapper
    return decorator1

@greet_decorator("Hi")
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
say_hello("Bob")

