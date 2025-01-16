

from calmodule import add, sub, mul, div, modulus, floordivision, exponential

ui = ''' UI
Display Options:
1. Add
2. Subtraction
3. Division
4. Multiplication
5. Exponential
6. Floordivision
7. Modulus
8. Exit'''

print(ui)

while True:
    choose_operation = input("Choose the operation you want to perform 1/2/3/4/5/6/7/8: ")

    if choose_operation == "1":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The addition result is {add(a, b)}")
            repeat = input("Do you want to add more numbers? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "2":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The subtraction result is {sub(a, b)}")
            repeat = input("Do you want to subtract more numbers? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "3":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The division result is {div(a, b)}")
            repeat = input("Do you want to divide more numbers? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "4":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The multiplication result is {mul(a, b)}")
            repeat = input("Do you want to multiply more numbers? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "5":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The exponential result is {exponential(a, b)}")
            repeat = input("Do you want to calculate more exponentials? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "6":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The floor division result is {floordivision(a, b)}")
            repeat = input("Do you want to floor divide more numbers? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "7":
        while True:
            a = int(input("Enter the number of a: "))
            b = int(input("Enter the number of b: "))
            print(f"The modulus result is {modulus(a, b)}")
            repeat = input("Do you want to calculate more modulus? (yes/no): ")
            if repeat != "yes":
                print(ui)
                break

    elif choose_operation == "8":
        print("Exiting the calculator")
        break

    else:
        print("Please choose again.")
