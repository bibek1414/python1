    # def __init__(self,name):
    #     self.name=name

#     def bark(self):
#         return f"{self.name} says woof"
#     def meow(self):
#         return f"{self.name} says mmeow"
    
# my_dog=Dog("Buddy")
# print(my_dog.bark())
# print(my_dog.meow())
# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# dog_name=input("Enter the dog name: ")
# age=input("Enter the age: ")
# my_dog= Dog(dog_name,age)

# print(my_dog.name)
# print(my_dog.age)
        

# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"${amount} deposited. New balance: ${self.balance}"
#         return "Deposit amount must be positive."

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient balance."
#         self.balance -= amount
#         return f"${amount} withdrawn. New balance: ${self.balance}"

#     def check_balance(self):
#         return f"Current balance: ${self.balance}"

# # Using the class
# account = BankAccount("Alice", 500)
# print(account.deposit(300))  # Output: $300 deposited. New balance: $800
# print(account.withdraw(200))  # Output: $200 withdrawn. New balance: $600
# print(account.check_balance())  # Output: Current balance: $60
