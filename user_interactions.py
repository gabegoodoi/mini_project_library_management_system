from object_classes import *
from error_handling import *
from file_handling import *
from book_ops import *
from author_ops import *
import re

class UserOperations:
    def sign_in():
        FileHandling.import_databases()
        while True:
            selection = input("\nWelcome to the Sign In page!\n1. Log in to existing account\n2. Create new account\n3. Quit\n")
            if selection == '1':
                UserOperations.log_in()
            elif selection == '2':
                UserOperations.sign_up()
            elif selection == '3':
                FileHandling.export_users(users, "users.txt")
                FileHandling.export_books(books, "books.txt")
                FileHandling.export_authors(authors, "authors.txt")
                break
            else:
                print("\nInvalid Input: must be 1-3. Try again.")

    def log_in():
        user_id = int(input("Please enter user ID: "))
        if int(user_id) in users:
            username = users[user_id]['Name']
            borrowed_books = users[user_id]['Borrowed Books']
            print(borrowed_books)
            print(f"Hello again, {username}")
            user_object = User(username, user_id, borrowed_books)
            UserOperations.lib_menu(user_object)
        else:
            print(f"Library ID {user_id} not found")

    def sign_up():
        username = input("Creating account. Please provide your name: ")
        try:
            if len(username) < 1:
                raise LengthError             
            elif not re.match(r"^[A-Za-z \.'-]+$", username):
                    raise NameError
        except NameError as error:
            print("NAME ERROR: Input must not include punctuation, numbers, symbols, or letters not contained in the English alphabet (exception: apostrophe and dash)")
        except LengthError as le:
            print("LENGTH ERROR: Input must be at least 1 character in length.")        
        else:
            user = User(username)
            print(f"Account successfully created with following details.\nLibrary ID ----- {user.get_lib_id()}\nName ----------- {user.name}\n")
            UserOperations.lib_menu(user)

    def lib_menu(user):
        print("\nWelcome to the Library Management System!")
        while True:
            selection = input("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit\n")
            if selection == '1':
                BookOperations.book_ops_menu(user)
            elif selection == '2':
                UserOperations.user_ops_menu()
            elif selection == '3':
                AuthorOperations.author_ops_menu()
            elif selection == '4':
                FileHandling.export_users(users, "users.txt")
                FileHandling.export_books(books, "books.txt")
                FileHandling.export_authors(authors, "authors.txt")
                break
            else:
                print("\nInvalid Input: must be 1-4. Try again.")

    def user_ops_menu():
        print("\nWelcome to the User Operations Menu!")
        while True:
            selection = input("\nMain Menu:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Quit\n")
            if selection == '1':
                UserOperations.add_user()
            elif selection == '2':
                UserOperations.view_user_details()
            elif selection == '3':
                UserOperations.display_users()
            elif selection == '4':
                break
            else:
                print("\nInvalid Input: must be 1-4. Try again.")

    def add_user():
        new_username = input("Please provide new user's name: ")
        try:
            if len(new_username) < 1:
                raise LengthError             
            elif not re.match(r"^[A-Za-z \.'-]+$", new_username):
                    raise NameError
        except LengthError as le:
            print("LENGTH ERROR: Input must be at least 1 character in length.")        
        except NameError as error:
            print("NAME ERROR: Input must not include punctuation, numbers, symbols, or letters not contained in the English alphabet (exception: apostrophe and dash)")
        else:
            new_user = User(new_username)
            print(f"{new_username} added to databasewith Library ID # {new_user.get_lib_id()}.")

    def view_user_details():
        user_id = int(input("Please enter user ID: "))
        found = False
        if user_id in users:
            print(f"Library ID ----- {user_id}\nName ----------- {users[user_id]['Name']}\nBorrowed Books - {users[user_id]['Borrowed Books']}")
            found = True
        elif not found:
            print(f"{user_id} not found in library records.")

    def display_users():
        for user in users:
            print(f"\nLibrary ID ----- {user}\nName ----------- {users[user]['Name']}\nBorrowed Books - {users[user]['Borrowed Books']}\n")