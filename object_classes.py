authors = {}
users = {}
books = {}

class Book:
    def __init__(self, title, author, genre, pub_date, availability="Available"):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub_date = pub_date
        self.availability = availability
        books[self.title] = {'Author': self.author, 'Genre': self.genre, 'Published On': self.pub_date, 'Availability': self.availability}

class User:
    def __init__(self, name, lib_id=None, borrowed_books=None):
        self.name = name
        self.__lib_id = lib_id if lib_id is not None else self.generate_id()
        self.borrowed_books = borrowed_books if borrowed_books is not None else []
        users[self.__lib_id] = {'Name': self.name, 'Borrowed Books': list(self.borrowed_books)}

    def get_lib_id(self):
        return self.__lib_id

    def set_lib_id(self, new_id=None):
        self.__lib_id = new_id if new_id is not None else self.generate_id()

    def generate_id(self):
        return len(users) + 1

class Author:
    def __init__(self, name, bio=None):
        self.name = name
        self.bio = bio
        authors[self.name] = {'Bio': self.bio,}

