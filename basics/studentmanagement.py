class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f'''
        Name: {self.name}
        Age: {self.age}
        Grade: {self.grade}
        ''')

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_students(self):
        while True:
            try:
                name = input("Enter the name: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty.")
                
                age = int(input("Enter the age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive number.")
                
                grade = int(input("Enter the grade: "))
                if grade < 0 or grade > 100:
                    raise ValueError("Grade must be between 0 and 100.")
                
                student = Student(name, age, grade)
                self.students.append(student)
                print(f"Student {name} added successfully!")
                
                another = input("Do you want to add another student? (yes/no): ").strip().lower()
                if another != "yes":
                    break
            
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def display_students(self):
        if not self.students:
            print("No students in the system.")
            return
        print("Student list:")
        for i, student in enumerate(self.students, 1):
            print(f"Student {i}:")
            student.display()

    def delete_students(self):
        if not self.students:
            print("No students to delete.")
            return
        self.display_students()
        try:
            index = int(input("Enter the number of the student to delete: ")) - 1
            if 0 <= index < len(self.students):
                removed = self.students.pop(index)
                print(f"Student {removed.name} deleted successfully!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

sms = StudentManagementSystem()
while True:
    print("\n1. Add Student\n2. Display Students\n3. Delete Student\n4. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        sms.add_students()
    elif choice == "2":
        sms.display_students()
    elif choice == "3":
        sms.delete_students()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
