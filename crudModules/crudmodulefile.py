import sqlite3

conn = sqlite3.connect("/home/bibek/Desktop/python1/crudModules/data.db")
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    ''')
    print("Table created successfully!")

def insert_data():
    while True:
        username = input("Enter the username: ")
        age = int(input("Enter the age: "))
        gmail = input("Enter the gmail: ")
        cursor.execute("INSERT INTO users (username, age, email) VALUES (?, ?, ?)", 
                       (username, age, gmail))
        print("Data inserted successfully!")
        another = input("Do you want to add another record? (yes/no): ")
        if another.lower() != 'yes':
            break

def display_all_data():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_data():
    try:
        update_user_input_id = int(input("Enter the id to update: "))
        cursor.execute(f'UPDATE users SET age=21 WHERE id={update_user_input_id}')
        print("Data updated successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric id.")

def delete_data():
    try:
        delete_user_input_id = int(input("Enter the id to delete: "))
        cursor.execute(f'DELETE FROM users WHERE id={delete_user_input_id}')
        print(f"Id:{delete_user_input_id} is deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid numeric id.")

def invalid_input():
    print("Invalid choice. Please choose a valid option.")
