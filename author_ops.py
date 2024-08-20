class AuthorOperations:
    def author_ops_menu():
        print("\nWelcome to the Author Operations Menu!")
        while True:
            selection = input("\nMain Menu:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit\n")
            if selection == '1':
                AuthorOperations.add_author()
            elif selection == '2':
                AuthorOperations.view_author_details()
            elif selection == '3':
                AuthorOperations.display_authors()
            elif selection == '4':
                print("\nReturning to Library Management System!")
                break
            else:
                print("\nInvalid Input: must be 1-4. Try again.")

    def add_author():
        author_name = input("Please enter the author's name: ")
        try:
            if len(author_name) < 1:
                raise LengthError
            elif not re.match(r"^[A-Za-z \.'-]+$", author_name):
                raise NameError  
            else:
                for name in authors:
                    if name.lower() == author_name.lower():
                        raise DuplicateError
        except LengthError as le:
            print("LENGTH ERROR: Input must be at least 1 character in length.")
        except NameError as error:
            print("NAME ERROR: Input must not include punctuation, numbers, symbols, or letters not contained in the English alphabet (exception: apostrophe, period, dash).")
        except DuplicateError as de:
            print("DUPLICATE ERROR: Item with same name already exists in database.")
        else:
            bio = input(f"Please enter a biographical blurb for {author_name}: ")
            Author(author_name, bio)
            print(f"{author_name} added to the database")

    def view_author_details():
        author_name = input("Please enter the the author's name: ")
        found = False
        for author in authors:
            if author.lower() == author_name.lower():
                found = True
                print(f"Name: {author}\nBio: {authors[author]['Bio']}")
        if not found:
            print(f"{author_name} not found in library records.")

    def display_authors():
        for author in authors:
            print(f"\nName: {author}\nBio: {authors[author]['Bio']}\n")