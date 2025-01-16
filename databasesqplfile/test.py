import sqlite3

conn = sqlite3.connect("/home/bibek/Desktop/python1/databasesqplfile/data.db")
cursor = conn.cursor()

user_choice = input('''
1. CREATE TABLE
2. INSERT DATA IN TABLE
3. DISPLAY ALL THE DATA
4. DISPLAY THE SELECTED ID USER ONLY
5. UPDATE DATA
Choose (1 or 2 or 3 or 4 or 5): ''')

if user_choice == "1":
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    ''')
    print("Table created successfully!")

elif user_choice == "2":
    while True:
        username = input("Enter the username: ")
        age = int(input("Enter the age: "))
        gmail = input("Enter the gmail: ")
        cursor.execute("INSERT INTO users (username,age,email) VALUES (?,?,?)", 
                    (username,age,gmail))
        print("Data inserted successfully!")
        another = input("Do you want to add another record? (yes/no): ")
        if another.lower() != 'yes':
            break
elif user_choice=="3":
    cursor.execute('SELECT * FROM users ')
    # cursor.execute('SELECT * FROM users WHERE age>30')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
elif user_choice=="4":
    user_id_input=int(input("Enter the id: "))
    cursor.execute(f'SELECT * FROM users WHERE id={user_id_input}')
    rows=cursor.fetchall()
    for row in rows:
        print(row)
elif user_choice=="5":
    update_user_input_id=int(input("Enter the id: "))
    cursor.execute(f'UPDATE users SET age=21 WHERE id={update_user_input_id}')
    
    
conn.commit()
conn.close()