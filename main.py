import json
import random

############### DATA BASE ###############
Data_Base = {  
    "eks1azy": {
        "name": "Artem",
        "surname": "Vlasiuk",
        "age": 17,
        "password": "12345"
    },
    "Vadimko555": {
        "name": "Vadim",
        "surname": "Marchenko",
        "age": 18,
        "password": "12345321"
    },
    "Vasilko": {
        "name": "Vasil",
        "surname": "Koval",
        "age": 18,
        "password": "23456"
    }
}

current_user = None

###############  JSON FUNC  ###############
def save_data(): # JSON save
     with open("database.json", "w") as f:
        json.dump(Data_Base, f, indent=4)

def load_data(): # JSON load
    global Data_Base
    try:
        with open("database.json", "r") as f:
            Data_Base = json.load(f)
    except FileNotFoundError:
        print("No database file found. Starting fresh.")

###############  MINI FUNC  ###############
def dif_password():
    while True:
        user_password = input("Enter your password: ")
        if len(user_password) <= 7 or len(user_password) >= 16:
            print("----Password need to be 8-15 sumbol----")
        else: 
            break
    return user_password

def generate_password():
    password = "!@#$%^&*()_+`*qzxcsdfpoiuytrewkjhgfd"
    dificult_password = ''.join(random.choices(password, k=10))
    print(f"Your new password is: {dificult_password}")
    return dificult_password

############### ADMIN FUNC ###############
def admin_show_users():
    print("\n--- All Users (sorted by username) ---")
    print("______________________________________________________________________")
    for username in sorted(Data_Base): 
        user = Data_Base[username]
        print(f"{username:15} | Name: {user['name']:10} | Surname: {user['surname']:10} | Age: {user['age']:5}|")
    print("______________________________________________________________________")

def admin_search_user():
    user_info = input("\nEnter a name of user: ")
    if user_info in Data_Base:
        print(Data_Base[user_info])

def admin_delete_user():
    user_delete = input("Enter a username of user to delete: ")
    user_del = user_delete
    if user_delete in Data_Base:
        really = input("Print (delete) to continue: ")
        if really == "delete":
            del Data_Base[user_delete]
            print(f"\n--User '{user_del}' was delete--")
            save_data()
        else:
            print("ERROR: something was wrong")
    else:
        print("ERROR: user was not detected")

def admin_edit_user():
    edit_user = input("\n Enter a username of user to edit data: ")
    if edit_user in Data_Base:
        print(f"1. Change {edit_user} username")
        print(f"2. Change {edit_user} name")
        print(f"3. Change {edit_user} surname")
        print(f"4. Change {edit_user} age")

        choice = input("your choice: ")

        if choice == "1":
            new_username = input("New username: ")

            if new_username in Data_Base:
                print("This username already taken")
                return
            
            editting = Data_Base[edit_user]
            del Data_Base[edit_user]
            Data_Base[new_username] = editting

            print(f"Username changed from {edit_user} to {new_username}")
            save_data()

        if choice == "2":
            new_name = input("New name: ")
            Data_Base[edit_user]["name"] = new_name

            print(f"Name changed to {new_name}")
            save_data()      

        if choice == "3":
            new_surname = input("New user surname: ")
            Data_Base[edit_user]["surname"] = new_surname

            print(f"Surname changed to {new_surname}")
            save_data()    

        if choice == "4":
            new_age = input("New user age: ")
            Data_Base[edit_user]["age"] = new_age

            print(f"Age changed to {new_age}")
            save_data()    

    else:
        print("Username not found")

###############  MAIN FUNC  ###############
def user_authorithation(): # choice = 1
    global current_user 

    print("--Authorithation--")
    username = input("Enter your username: ")

    if username in Data_Base:
        password = input("Enter your password: ")

        if password == Data_Base[username]["password"]:
            current_user = username 
            print(f"Welcome, {Data_Base[username]["name"]}")
            
        else:
            print("Wrong password")

    else:
        print("you are not loggined")

def register(): # choice = 2
    global current_user

    print("--REGISTER--")
    username = input("Enter your username: ")

    if username in Data_Base:
        print("This account already register")
    else:
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")

        while True:
            try:
                age = int(input("Enter your age: "))
            except ValueError:
                print("ERROR: your age may be only int value")
                continue
            if age >= 100 or age <= 5:
                print("----We don`t belive you----")
            else:
                break
        
        print("1. We will create password")
        print("2. You will create password")

        user_choice = input("Enter: ")

        if user_choice == "1":
            password = generate_password()
        elif user_choice == "2":
            password = dif_password()
        # password = input("Enter your password: ")

        Data_Base[username] = {
            "name": name,
            "surname": surname,
            "age": age,
            "password": password
        }

        print("Succesful register")
        current_user = username

        save_data()

def admin_panel():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. Show all users")
        print("2. Search user")
        print("3. Delete user")
        print("4. Edit user")
        print("0. Exit admin panel")

        admin_choice = input("Your choice: ")

        if admin_choice == "1":
            admin_show_users()
        elif admin_choice == "2":
            admin_search_user()
        elif admin_choice == "3":
            admin_delete_user()
        elif admin_choice == "4":
            admin_edit_user()
        elif admin_choice == "0":
            break
        else:
            print("Invalid option.")

###############  CHANGE FUNC  ###############
def user_change(): # choice = 3
    print("--CHANGE MENU--")
    print("1. Change account username")
    print("2. Change account password")
    print("3. Change account name")
    print("4. Change account surname")
    print("5. Change account age")

    change_choice = input("Your Choice: ")

    if change_choice == "1":
        old_username = input("Enter your username: ")

        if old_username in Data_Base:
            password = input("Enter your password: ")

            if password == Data_Base[old_username]["password"]:
                new_username = input("Enter new username: ")
                user_data = Data_Base[old_username]
                del Data_Base[old_username]
                Data_Base[new_username] = user_data
                # Data_Base[old_username] = new_username ## (NOT CORRECT , DELETE ALL USER_DATA!!!!!!!)         
            else:
                print("not correct password")

        else:
            print("Username not in Data Base")

        save_data()

    if change_choice == "2":
        username = input("Enter your username: ")

        if username in Data_Base:
            old_password = input("Enter your old password: ")
        
            if old_password == Data_Base[username]["password"]: # not IN only ==
                new_password = dif_password()

                Data_Base[username]["password"] = new_password
                print("\n --Password changed!--")

            else:
                print("nor correct password")

        else:
            print("User are not in Data Base")

        save_data()

    if change_choice == "3":
        username = input("Enter your username: ")

        if username in Data_Base:
            password = input("Your password: ")

            if password == Data_Base[username]["password"]:
                new_name = input("Enter your new name:")
                Data_Base[username]["name"] = new_name
                print("\n --Name changed!--")

        else:
            print("User are not in Data Base")

        save_data()

    if change_choice == "4":
        username = input("Enter your username: ")

        if username in Data_Base:
            password = input("Your password: ")

            if password == Data_Base[username]["password"]:
                new_surname = input("Enter your new surname:")
                Data_Base[username]["surname"] = new_surname
                print("\n --Surname changed!--")

        else:
            print("User are not in Data Base")

        save_data()

    if change_choice == "5":
        username = input("Enter your username: ")

        if username in Data_Base:
            password = input("Your password: ")

            if password == Data_Base[username]["password"]:
                try:
                    new_age = int(input("Enter your new age: "))
                    Data_Base[username]["age"] = new_age
                    print("\n --Age changed!--")
                except ValueError:
                    print("ERROR: Age must be a number")
        else:
            print("User are not in Data Base")

        save_data()

###############  INFO FUNC  ###############
def statics(): # choice = 4
    print("\n -----Statistics-----")
    ages = []

    for user in Data_Base:
        age = Data_Base[user]["age"]
        ages.append(age)
        
    average_age = sum(ages) / len(ages)
    min_age = min(ages)
    max_age = max(ages)

    print(f"Average age our client is: {average_age:.2f}") # 0.00 
    print(f"Minimal age our client is: {min_age:.2f}") # 0.00
    print(f"Maximum age our client is: {max_age:.2f}") # 0.00

def user_info(): # choice = 5
    global current_user
    if current_user is None:
        print("You are not logged in")
    else:
        print(f"Your account info, {Data_Base[current_user]["name"]}")
        print(Data_Base[current_user])

###############  DEL FUNC  ###############
def user_delete(): # choice = 6
    global current_user

    if current_user is None:
        print("\nYou need to be logged")
        user_authorithation()
        return
    
    del_choice_password = input("Write your password to delete account: ")

    if del_choice_password == Data_Base[current_user]["password"]:
        del Data_Base[current_user]
        print("Account deleted")

        current_user = None
        save_data()
    else:
        print("Incorrect password")

###############  MAIN FUNC  ###############
def main():
    global current_user
    load_data()
    while True:
        print("\n---MENU---:")
        print("1. Sign in (authorization)")
        print("2. Sign up (register)")
        print("3. Change account info")
        print("4. Statistic")
        print("5. See my account info")
        print("6. Delete account")
        print("7. Admin panel")
        print("0. Quit")

        choice = input("Your choice: ")

        if choice == "1": # sign in 
            user_authorithation()

        elif choice == "2": # sign up
            register()

        elif choice == "3": # change 
            user_change()

        elif choice == "4": # statistic
            statics()

        elif choice == "5": # see info
            user_info()

        elif choice == "6": # del acc
            user_delete()

        elif choice == "7":
            admin_password = input("Enter admin password: ")
            if admin_password == "admin":
                admin_panel()

        elif choice == "0": # exit
            save_data()
            print("bye")
            break

        elif choice == "info":
            print(current_user)

main()

