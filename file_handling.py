class FileHandling:
    
    def export_users(users_dict, file_name):
        with open(file_name, 'w') as file:
            for user_id, data in users_dict.items():
                borrowed_books = ','.join(data['Borrowed Books'])
                file.write(f"User ID: {user_id}, Name: {data['Name']}, Borrowed Books: [{borrowed_books}]\n")

    def export_books(books_dict, file_name):
        with open(file_name, 'w') as file:
            for title, data in books_dict.items():
                file.write(f"Title: {title}, Author: {data['Author']}, Genre: {data['Genre']}, Published On: {data['Published On']}, Availability: {data['Availability']}\n")

    def export_authors(authors_dict, file_name):
        with open(file_name, 'w') as file:
            for name, bio in authors_dict.items():
                file.write(f"Author: {name}, Bio: {bio['Bio']}\n")
    
    def import_databases():
        global users, books, authors
        with open('users.txt', 'r+') as users_file, open('books.txt', 'r+') as books_file, open('authors.txt', 'r+') as authors_file:
            user_file_contents = users_file.readlines()
            books_file_contents = books_file.readlines()
            authors_file_contents = authors_file.readlines()

            for line in user_file_contents:
                user_line_groups = re.search(r"User ID: ([0-9]+), Name: ([A-Za-z -.']{1,747}), Borrowed Books: \[(.*)\]", line)
                if user_line_groups:
                    user_id = int(user_line_groups.group(1))
                    name = user_line_groups.group(2)
                    borrowed_books = [title.strip() for title in user_line_groups.group(3).split(',')] if user_line_groups.group(3) else []
                    User(name, user_id, borrowed_books)

            for line in books_file_contents:
                books_line_groups = re.search(r"Title: (.*), Author: ([A-Za-z .'-]+), Genre: ([A-Z a-z\-]+), Published On: ([0-9]{4}), Availability: (Borrowed|Available)", line)
                if books_line_groups:
                    title = books_line_groups.group(1)
                    author = books_line_groups.group(2)
                    genre = books_line_groups.group(3)
                    pub_date = books_line_groups.group(4)
                    availability = "Available" if books_line_groups.group(5) == "Available" else "Borrowed"
                    Book(title, author, genre, pub_date, availability)

            for line in authors_file_contents:
                authors_line_groups = re.search(r"Author: ([A-Za-z -.']+), Bio: (.*?)\n", line)
                if authors_line_groups:
                    author_name = authors_line_groups.group(1)
                    bio = authors_line_groups.group(2)
                    Author(author_name, bio)