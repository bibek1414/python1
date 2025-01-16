# class BankAccount:
#     def __init__(self, account_name, initial_balance=0):
#         self.account_name = account_name
#         self.money = initial_balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be greater than zero.")
#             return
#         self.money += amount
#         print(f"Rs.{amount} deposited successfully. New balance: Rs.{self.money}")

#     def withdraw(self, amount):
#         if amount > self.money:
#             print("Error: Withdrawal amount exceeds current balance.")
#         elif amount <= 0:
#             print("Withdrawal amount must be greater than zero.")
#         else:
#             self.money -= amount
#             print(f"Rs.{amount} withdrawn successfully. Remaining balance: Rs.{self.money}")

#     def check_balance(self):
#         print(f"Account Name: {self.account_name}, Current Balance: Rs.{self.money}")


# class BankSystem:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self):
#         account_name = input("Enter account name: ").strip()
#         if account_name in self.accounts:
#             print(f"Account '{account_name}' already exists.")
#         else:
#             initial_balance = int(input("Enter initial deposit amount (or 0): "))
#             self.accounts[account_name] = BankAccount(account_name, initial_balance)
#             print(f"Account '{account_name}' created successfully with balance Rs.{initial_balance}.")

#     def access_account(self):
#         account_name = input("Enter account name to access: ").strip()
#         account = self.accounts.get(account_name)
#         if not account:
#             print(f"Error: Account '{account_name}' does not exist.")
#             return

#         while True:
#             print("\nChoose an option:")
#             print("1. Deposit Money")
#             print("2. Withdraw Money")
#             print("3. Check Balance")
#             print("4. Exit")
#             choice = input("Enter your choice: ").strip()

#             if choice == "1":
#                 amount = int(input("Enter amount to deposit: "))
#                 account.deposit(amount)
#             elif choice == "2":
#                 amount = int(input("Enter amount to withdraw: "))
#                 account.withdraw(amount)
#             elif choice == "3":
#                 account.check_balance()
#             elif choice == "4":
#                 print(f"Exiting account '{account_name}'.")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

#     def run(self):
#         while True:
#             print("\nWelcome to the Bank System!")
#             print("1. Create Account")
#             print("2. Access Account")
#             print("3. Exit")
#             choice = input("Enter your choice: ").strip()

#             if choice == "1":
#                 self.create_account()
#             elif choice == "2":
#                 self.access_account()
#             elif choice == "3":
#                 print("Thank you for using the Bank System. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")


# # Run the Bank System
# bank_system = BankSystem()
# bank_system.run()

