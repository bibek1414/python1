'''calculate simple INterest'''
# def simple_interest(p,t,r):
#     result= (p*t*r)/100
#     print(result) 

# principle=int(input("Enter the Principle: "))
# time=int(input("Enter the Time: "))
# rate=int(input("Enter the rate: "))
# simple_interest(principle,time,rate)

'''palindrome'''
# def palindrome(string):
#     return string==string[::-1]

# input_string=input("Enter the word : ")

# if palindrome(input_string):
#     print(f"{input_string} is the palindrome ")
# else:
#     print(f"{input_string} is not palindrome")

''' count vowel in string'''

# input_string=input("Enter the word: ").lower()

# count=0
# for x in input_string:
#     if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
#         count+=1
# print(f"The total vowel is :{count}")

'''check leap year'''

# input_year=int(input("Enter the year: "))

# if (input_year % 4==0 and input_year % 100 != 0) or (input_year%400==0):
#     print(f"{input_year } this is leap Year")
# else:
#     print(f"{input_year} this is not leap year")    

'''areea of different shapes'''
# class Area:
#     pi = 3.14159

#     def square_area(self, side):
#         return side * side

#     def rectangle_area(self, length, width):
#         return length * width

#     def circle_area(self, radius):
#         return self.pi * radius * radius

#     def triangle_area(self, base, height):
#         return 0.5 * base * height


# class Square(Area):
#     def __init__(self, side_length):
#         result = super().square_area(side_length)
#         print(f"The area of the square is {result}")


# class Rectangle(Area):
#     def __init__(self, length, width):
#         result = super().rectangle_area(length, width)
#         print(f"The area of the rectangle is {result}")


# class Circle(Area):
#     def __init__(self, radius):
#         result = super().circle_area(radius)
#         print(f"The area of the circle is {result}")


# class Triangle(Area):
#     def __init__(self, base, height):
#         result = super().triangle_area(base, height)
#         print(f"The area of the triangle is {result}")


# square = Square(4)
# rectangle = Rectangle(5, 3)
# circle = Circle(7)
# triangle = Triangle(6, 4)

'''fibonacci'''
# n = int(input("Enter the number: "))

# def fibonacci_series(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fibonacci_series(num - 1) + fibonacci_series(num - 2)

# def print_fibonacci_series(n):
#     total_sum = 0
#     for i in range(n):
#         fib_num = fibonacci_series(i)

#         if fib_num < 21:
#             print(fib_num, end=" ")
#             total_sum += fib_num
#         else:
#             break
#     print("\nSum:", total_sum)

# print_fibonacci_series(n)

'''Prime Number'''

# def prime_number(number):
#     if number <= 1:
#         print("Not Prime Number")
#         return
#     for i in range(2, number):
#         if number % i == 0:
#             print("Not Prime Number")
#             return
#     return print("Prime Number")

# input_number= int(input("Enter the Number: "))
# prime_number(input_number)

'''Multiplication table'''

input_number = int(input("Enter the number: "))

for i in range(10):
    print(f"{i+1} * {input_number} = {(i+1)*input_number}")

    









