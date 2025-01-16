import csv

file_path = "/home/bibek/Desktop/python1/csvHandnling/csvcalution.csv"

while True:
    inp = input('''Enter the Operation you want to perform:
    1. Enter Data
    2. Display Data
    3. Search Data
    4. Exit
    Choice: ''')

    if inp == '1':
        with open(file_path, mode='w', newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Name', 'Age', 'Math', 'Science', 'English', 'Total'])
        
        while True:
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            math = int(input("Enter the marks in Math: "))
            science = int(input("Enter the marks in Science: "))
            english = int(input("Enter the marks in English: "))
            total = math + science + english
            data = [name, age, math, science, english, total]

            with open(file_path, mode='a', newline="") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(data)

            cont = input("Do you want to add another record? (yes/no): ").strip().lower()
            if cont != 'yes':
                break

    elif inp == '2':
        try:
            with open(file_path, mode="r", newline="") as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("No data file found. Please add data first.")

    elif inp == '3':
        try:
            search_query = input("Enter the value to search (e.g., name, age, marks, total): ").strip()
            found = False

            with open(file_path, mode="r", newline="") as f:
                csv_reader = csv.reader(f)
                header = next(csv_reader)
                print("Matching Records:")
                for row in csv_reader:
                    if search_query in row:
                        print(row)
                        found = True

            if not found:
                print("No matching records found.")

        except FileNotFoundError:
            print("No data file found. Please add data first.")

    elif inp == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
