from crudmodulefile import *

while True:
    user_choice = input('''
    1. CREATE TABLE
    2. INSERT DATA IN TABLE1
    3. DISPLAY ALL THE DATA
    4. UPDATE DATA
    5. DELETE DATA
    6. EXIT PROGRAM
    Choose (1 or 2 or 3 or 4 or 5 or 6): ''')

    if user_choice == "1":
        create_table()
    elif user_choice == "2":
        insert_data()
    elif user_choice == "3":
        display_all_data()
    elif user_choice == "4":
        update_data()
    elif user_choice == "5":
        delete_data()
    elif user_choice == "6":
        print("Exiting the Program")
        break
    else:
        invalid_input()


conn.commit()
conn.close()
