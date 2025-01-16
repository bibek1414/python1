# def factorial(n):
#     if n==0:
#         return 1
#     print(factorial(2))
#     return n*factorial(n-1)
    

# num=int(input("Enter the number: "))
# print(factorial(num))

# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibonacci(n-1)+fibonacci(n-2)
# # print(fibonacci(num))
# def print_fibonacci_series(n):
#     for i in range(n):
#         print(fibonacci(i),end=" ")
# 2

# print_fibonacci_series(num)


def is_armstrong(number):
    # Convert the number to a string to work with its digits
    digits = str(number)
    # Find the number of digits
    power = len(digits)
    # Calculate the sum of each digit raised to the power
    total = sum(int(digit) ** power for digit in digits)
    # Check if the total equals the original number
    return total == number

# Input from the user
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")



def is_palindrome(string):
    # Reverse the string and compare it with the original
    return string == string[::-1]

# Take input from the user
input_string = input("Enter a word: ")

if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome!')
else:
    print(f'"{input_string}" is not a palindrome.')
