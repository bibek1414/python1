# while True:
#     try:
#         x=int(input("Enter the first number: "))
#         y=int(input("Enter the second number: "))
#         print("Dividing numbers")
#         result =x/y
#         print(result)
#         break
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
        
        # print(result)
#     except ValueError:
#         print("number cannot be string ")
#     finally:
#         print("Finally")
    # except Exception as e:
    #     print(e)


# x=input("Enter the value: ")
# if x.isdigit():
#         converted_to_int= int(x)
#         print("this is integer",type(converted_to_int))

# elif x.count('.')==1  and x.replace('.','').isdigit():
#     # try:
#         converted_to_float=float(x)
#         print("this is float",type(converted_to_float))
#     # except Exception as e:
#     #     print(e)
# elif x.count('.') > 1:
#     print("This is not a valid float; it contains multiple decimal points.")

# else:
#     print("This is string")

# x=int(input("Enter the age: "))
# if x<=0:
#     raise Exception("Age must be greate than zero")
    
# else:
#     print(x)


# x=int(input("enter the age: "))

# try:
#     if x<0:
#         raise negative_error("Negative nUmbers")
#     elif x==0:
#         raise zero_error("NUmber is zero")
# except negative_error as e:
#     print(e)
#     x=int(input("enter the age: "))
#     print(x)
# except zero_error as e:
#     print(e)
#     x=int(input("enter the age: "))
#     print(x)
# # print(x)
# import traceback

# class negative_error(Exception):
#     def __init__(self, message):
#         super().__init__(message)
    
# class zero_error(Exception):
#     def __init__(self, message):
#         super().__init__(message)
# class BankAccount:
#     def __init__(self,initial_balance=0):
#         self.money=initial_balance
#     def deposit(self):
#         try:
#             x=int(input("Enter the money you want to input to your bank account"))
#             if x<0:
#                 raise negative_error("Number must be positve")
#             elif x==0:
#                 raise zero_error("NUmber must be greater than 0")
#             else:
#                 self.money+=x
#                 print(f"THe deposit money is {x} and total money in your account is {self.money} ")

#         except negative_error as e:
#             print(e)
#     def withdraw(self):
#         try:
#              x=int(input("Enter the money you want to withdrawal"))
#              if x<0:
#                 raise negative_error("Number must be positve")
#              elif x==0:
#                 raise zero_error("NUmber must be greater than 0")
        
#              elif x>self.money:
#                     print("Insuffiecinet Balance")
#              else:
#                     self.money-=x
#                     print(f"THe withdrawal amout is {x} and the new balance is {self.money}")
#         except Exception as e:
#             print(e)
#             # x=int(input("Enter the money you want to withdrawal"))
#             traceback.print_exc()

# bank= BankAccount(100)
# bank.deposit()
# bank.withdraw()

class BankAccount:
    def __init__(self, initial_balance=0):
        self.money = initial_balance

    def deposit(self):
        while True:
            try:
                x = int(input("Enter the money you want to deposit into your bank account: "))
                if x < 0:
                    raise ValueError("Number must be positive")
                elif x == 0:
                    raise ValueError("Number must be greater than 0")
                else:
                    self.money += x
                    print(f"The deposit amount is {x}, and the total money in your account is {self.money}.")
                    break  
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
            except Exception as e:
                print("An unexpected error occurred.")
                break 

    def withdraw(self):
        while True:
            try:
                x = int(input("Enter the money you want to withdraw: "))
                if x < 0:
                    raise ValueError("Number must be positive")
                elif x == 0:
                    raise ValueError("Number must be greater than 0")
                elif x > self.money:
                    print("Insufficient Balance. Please try again.")
                else:
                    self.money -= x
                    print(f"The withdrawal amount is {x}, and the new balance is {self.money}.")
                    break  
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
            except Exception as e:
                print("An unexpected error occurred.")
                break  


bank = BankAccount(100)
print("\n--- Initial Account Balance: 100 ---\n")
bank.deposit()
bank.withdraw()




