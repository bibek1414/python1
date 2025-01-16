# def palindrome(string):
#     return string==string[::-1]

# input_string=input("Enter the word : ")

# if palindrome(input_string):
#     print(f"{input_string} is the palindrome ")
# else:
#     print(f"{input_string} is not palindrome")

# def armstrong(number):
#     total=0
#     digits=str(number)
#     power =len(digits)
#     # print(digits)
#     # print(power)
#     for d in digits:
#         d= int(d)
#         total += d ** power
#     return total == number

# num=int(input("Enter the number"))
# if armstrong(num):
#     print(f"{num} is armstrong")
# else:
#     print(f"{num} is not armstrong")

n=int(input("Enter the number: "))
def fibonacci_series(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fibonacci_series(num-1)+fibonacci_series(num-2)

def print_fibonacci_series(n):

    for i in range(n):
        print(fibonacci_series(i))
print_fibonacci_series(n)


