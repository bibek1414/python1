students={}

while True:
    student={}
    student['name'] = input("Enter the student's name: ")
    student['age'] = int(input("Enter the student's age: "))
    student['grades'] = {}

    for i in range(3):
        subject = input(f"Enter subject {i+1} name: ")
        grade = int(input(f"Enter grade for {subject}: "))
        student['grades'][subject] = grade

    student['contacts'] = {}
    student['contacts']['email'] = input("Enter the student email address: ")
    student['contacts']['phone'] = input("Enter the student phone number: ")
    roll_number = int(input("Enter the roll number: "))
    students[roll_number] = student
    more=input("Add new Students:(yes/no) ")
    if(more.lower()!='yes'):
        break
print(students)

total_grade=0
for roll_number, student in students.items():
    total_grade = sum(student['grades'].values()) 
    print(f"Total sum of grades: {total_grade}") 
    
