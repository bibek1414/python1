# # def function_name(parameters):
# #     statement(S)
# #     returnvalue

# # def greet():
# #     print("Hello world")
# # greet()

# # def add_numbers(a,b):
# #     return a+b

# # result=add_numbers(5,3)
# # print(result)

# # def greet_user(name="Guest"):
# #     print(f"Hello,{name}!")
# # greet_user("Alice")
# # greet_user()

# # def add(x,y):
# #     print("Addong")
# #     resi=x+y
# #     return resi
# # print("Entering the function")
# # a=1
# # b=2
# # addition=add(a,b)
# # final=addition+10
# # print(final)

# def get_stats(numbers):
#     return min(numbers),max(numbers),sum(numbers)

# nums=[3,2,3,4,5]
# # min_num,max_num,sum=get_stats(nums)
# # print(f"MIn:{min_num}, Max:{max_num}, Sum:{sum}")
 
# result=get_stats(nums)
# # min_num= result[0]
# # max_num= result[1]
# # total_sum= result[2]
# print(result)
# # print(f"MIn:{min_num}, Max:{max_num}, Sum:{total_sum}")
# print(f"MIn:{result[0]}, Max:{result[1]}, Sum:{result[2]}")


# add= lambda a,b: a+b
# print(add(2,3))

# def greet(age, name="Guest"):
#     return f"Hello, {name}, age {age}"

# print(greet(2))


def add(*numbers):
    return sum(numbers)
# a=int(input("Enter the number: "))
# b=int(input("Enter the number: "))
# c=int(input("Enter the number: "))
# d=int(input("Enter the number: "))
# print(add(a,b,c,d))


# def show_info(**details):
#     for key, value in details.items():
#         print(f"{key}:{value}")
# show_info(name="BIbke",age=30)

# def my_function(*kids):
#     print("THe youngst child is "+kids[2])
#     for x in kids:
#         print(x)

# my_function("emil","tobia","hello")

# def my_function(**kid):
#     print(kid)

# my_function(fname="bibek",lname="redjsjs")


def my_function(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
my_function("aaple","banana",apple="fruits",price=2121121)
        


