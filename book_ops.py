from object_classes import *
from error_handling import *
from file_handling import *
import re

class BookOperations:
    def book_ops_menu(user):
        print("\nWelcome to the Book Operations Menu!")
        while True:
            selection = input("\nMain Menu:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Quit\n")
            if selection == '1':
                BookOperations.add_book()
            elif selection == '2':
                BookOperations.borrow_book(user)
            elif selection == '3':
                BookOperations.return_book(user)
            elif selection == '4':
                BookOperations.find_book()
            elif selection == '5':
                BookOperations.display_books()
            elif selection == '6':
                print("\nReturning to Library Management System!")
                break
            else:
                print("\nInvalid Input: must be 1-6. Try again.")

    def add_book():
            title = input("Please enter the title of the book: ")
            try:
                for char in title:
                    if char in r"[,]":
                        raise CommaError
                if len(title) < 1:
                    raise LengthError 
                for book in books:
                    if book.lower() == title.lower():
                        raise DuplicateError
            except CommaError as ce:
                print("COMMA ERROR: Input must not include commas.")
            except DuplicateError as de:
                print("DUPLICATE ERROR: Item with same name already exists in database.")
            except LengthError as le:
                print("LENGTH ERROR: Input must be at least 1 character in length.")
            else:
                genre = input(f"Please enter the genre of {title}: ")
                try:
                    if len(genre) < 1:
                        raise LengthError 
                    elif not re.match(r"^[A-Za-z \.'-]+$", genre):
                        raise NameError
                except NameError as error:
                    print("NAME ERROR: Input must not include punctuation, numbers, symbols, or letters not contained in the English alphabet (exception: apostrophe and dash).")
                except LengthError as le:
                    print("LENGTH ERROR: Input must be at least 1 character in length.")
                else:
                    author = input(f"Please enter the author of {title}: ")
                    match = False
                    try:
                        if len(author) < 1:
                            raise LengthError 
                        elif not re.match(r"^[A-Za-z \.'-]+$", author):
                            raise NameError   
                    except NameError as error:
                        print("NAME ERROR: Input must not include punctuation, numbers, symbols, or letters not contained in the English alphabet (exception: apostrophe, period, dash).")
                    except LengthError as le:
                        print("LENGTH ERROR: Input must be at least 1 character in length.")
                    else:
                        for name in authors:
                            if name.lower() == author.lower():
                                match = True
                        if not match:
                            bio = input(f"Thank you for adding a book by a new author to the library, Please enter a biographical blurb for {author}: ")
                            Author(author, bio)
                            FileHandling.export_authors(authors, 'authors.txt')       
                        pub_date = input(f"Please enter the publication year of {title}: ")
                        try:
                            if not re.match(r"^[0-9]{4}$", pub_date):
                                raise YearError
                        except YearError as ye:
                            print("YEAR ERROR: Input must not exactly 4 numerical characters (0-9).")
                        else:
                            Book(title, author, genre, pub_date)
                            print(f"{title} added to library.")
                            FileHandling.export_books(books, 'books.txt')

    def borrow_book(user):
        title = input("Please enter the title of the book you'd like to borrow: ")
        found = False
        for book in books:
            if book.lower() == title.lower():
                found = True
                if books[title]['Availability'] == "Available":
                    print(f"Checking out {title}.")
                    books[title]['Availability'] = "Borrowed"
                    user.borrowed_books.append(title)
                    users[user.get_lib_id()]['Borrowed Books'].append(title)
                    FileHandling.export_books(books, 'books.txt')
                else:
                    print(f"{title} not available at the moment.")
        if not found:
            print(f"{title} not found in library records.")
    
    def return_book(user):
        title = input("Please enter the title of the book you'd like to return: ")
        found = False
        for book in user.borrowed_books:
            if book.lower() == title.lower():
                found = True
                print(f"Returning {title}.")
                books[title]['Availability'] = "Available"
                user.borrowed_books.remove(title)
                users[user.get_lib_id()]['Borrowed Books'] = user.borrowed_books.copy()
                FileHandling.export_books(books, 'books.txt')
        if not found:            
            print(f"According to our records, you did not borrow {title} from our library.")

    def find_book():
        title = input("Please enter the title of the book you'd like to find: ")
        found = False
        for book in books:
            if book.lower() == title.lower():
                print(f"Title: {book}\nAuthor: {books[book]['Author']}\nGenre: {books[book]['Genre']}\nPublished In: {books[book]['Published On']}\nAvailability: {books[book]['Availability']}")
                found = True
        if not found:            
            print(f"{title} not found in library records.")

    def display_books():
        if books:
            for book in books:
                print(f"Title: {book}\nAuthor: {books[book]['Author']}\nGenre: {books[book]['Genre']}\nPublished In: {books[book]['Published On']}\nAvailability: {books[book]['Availability']}\n")
        else:
            print("Library is empty.")