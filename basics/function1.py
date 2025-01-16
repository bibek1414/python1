# def my_function():
#     x=10
#     print("Inside function",x)

# my_function()

# print("OutSiee funtion",x)    


# y=20
# def my_function1():
#     print("Inside function",y)
# my_function1()

# print("OutSiee funtion",y)
    

z=30

def update_global():
    global z
    print("Inside Function",z)
    z=z+5

update_global()
print("Outside Function",z)


    