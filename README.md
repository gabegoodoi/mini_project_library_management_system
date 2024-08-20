This Repository is a mini-project for Coding Temple.

TABLE OF CONTENTS:

1.  main.py
2.  user_interactions.py
3.  book_ops.py
4.  athor_ops.py
5.  object_classes.py
6.  file_handling.py
7.  error_handling.py
8.  users.txt
9.  authors.txt
10. books.txt
11. overview.txt
12. conclusion

---------------------------

1. MAIN.PY

  The application runs through the main.py file. It does so by: 
    
    1st: importing the module from user_interactions.py. 
    2nd: calling the custom method sign_in() from the UserOperations class without any arguments.

---------------------------

2. USER_INTERACTIONS.PY

  The application's UserOperation class methods are defined in this file. In addition, the file imports multiple modules listed below:
  
      1. object_classes.py
      2. error_handling.py
      3. file_handling.py
      4. book_ops.py
      5. author_ops.py
      6. re
  
  methods of the UserOperations class:

    1. sign_in()
  
        This method takes no arguments. 
        The method first inports all data from users, authors, and book text files into their corresponding dictionaries. 
        It then prints a CLI menu directing users to select a path that will allow them to either provide the ID of an existing user, create a new user, or exit the program.

    2. log_in()

        This method takes no arguments. 
        It asks users to input an ID and if that ID is in the database it creates a User-object comprised of all that ID's data. 
        It then calls the lib_menu() method with the User-object as an argument. 

    3. sign_up()

        This method takes no arguments. 
        It prompts user to input a valid name and creates a User object with the name as an argument.
        It then calls the lib_menu() method with the User-object as an argument. 

    4. lib_menu()

        This method takes 1 argument; a user object.  
        It then prints a CLI menu directing users to select a path that will allow them to access another menu 
        (either: User Operations, Book Operations, or Author Operations)

    5. user_ops_menu()

        This method takes no arguments. 
        It then prints a CLI menu directing users to select a path that will allow them to access to either: 
        add a new user, display user details, or display all users)

    6. add_user()

        This method takes no arguments. 
        It operates much like the sign_up() method with the exception that it does not pass the User-object back to lib_menu(), 
        allowing the user to stay "logged-into" their account while adding a new user to the database.

    7. view_user_details()
    
        This method takes no arguments. 
        This method searches a user key in the user dictionary based on the operator's input. It then displays all of that key's values in a formatted manner.

    8. display_users()
    
        This method takes no arguments. 
        This method displays all key value pairs in the users dictionary in a formatted manner.
    
3. BOOK_OPS.PY

  The application's BookOperations class methods are defined in this file.        

  methods of the UserOperations class:

    1. book_ops_menu()
    
        This method takes 1 argument; a user object.  
        It then prints a CLI menu directing users to select a path that will allow them to activate one of the 5 other methods of this class.

    2. add_book()

        This method takes no arguments. 
        It asks users to input several variables which it validates. 
        It then creates a Book object using the input variables as arguments. 
        If the author variable is not already a key in the authors dictionary, it prompts one additional input and creates an Author object. 
        Finally, it exports the books dictionary to the books.txt file.

    3. borrow_book()

        This meethod takes 1 argument; a user object.
        This method searches a book key in the books dictionary, if found and that book key has an "Available" value to it's "Availability" key, 
        then the key is changed from "Available" to "Borrowed"
        Additionally that book is appended to the User object's borrowed_books attribute.
        Finally, it exports the books dictionary to the books.txt file.

    4. return_book()
    
        This meethod takes 1 argument; a user object.
        This method searches a book key in the books dictionary, if found and that book key has an "Borrowed" value to it's "Availability" key, 
        then the key is changed from "Borrowed" to "Available"
        Additionally that book is removed from the User object's borrowed_books attribute.
        Finally, it exports the books dictionary to the books.txt file.

    5. find_book()

        This method takes no arguments. 
        This method searches a book key in the books dictionary based on the operator's input. It then displays all of that key's values in a formatted manner.

    6. display_books()

        This method takes no arguments. 
        This method displays all key value pairs in the books dictionary in a formatted manner.

4. AUTHOR_OPS.PY

  The application's AuthorOperations class methods are defined in this file.        

  methods of the UserOperations class:

    1. author_ops_menu()
    
        This method takes no arguments. 
        It then prints a CLI menu directing users to select a path that will allow them to activate one of the 3 other methods of this class.

    2. add_author()

        This method takes no arguments. 
        It asks users to input 2 variables which it validates. 
        It then creates an Author object using the input variables as arguments. 

    3. view_author_details()

        This method takes no arguments. 
        This method searches a author key in the authors dictionary based on the operator's input. It then displays that key's values in a formatted manner.

    4. display_authors()
        
        This method takes no arguments. 
        This method displays all key value pairs in the authors dictionary in a formatted manner.

    
5. OBJECT_CLASSES.PY

  The application's Author, Book, and User object classes are defined in this file.
  Additionally, the users, authors, & books dictionaries are initialized (as empty) in this file.

  each object's initializing also triggers their addition to their corresponding dictionaries
  
  Finally, 3 User class methods are defined:
        
    1. get_lib_id()
    
        This method takes no arguments.
        It is a getter that allows operators to access the private self.__lib_id attribute.
        
    2. set_lib_id()

        This method takes self and an ID as arguments (though it defaults the ID to None). 
        It is a setter that allows operators to alter the private self.__lib_id attribute.
        If the ID argument is at its default value, the method will alter the private attribute with the return value of a triggered generate_id() method.

    3. generate_id()

        This method takes self as its sole argument. 
        Returns a number that is one greater than the length of the users dictionary. It's purpose is to generate a new ID # for User objects.
  
6. FILE_HANDLING.PY

  The application's FileHandling class and its 4 methods are defined in this file.
  The application's text files are imported from this file to their corresponding dictionaries.
  Additionally, the applications' updated dictionaries are written onto the files before the program is quit.

      1. export_users()
      2. export_books()
      3. export_authors()
      4. import_databases()

7. ERROR_HANDLING.PY

  The application's five custom Exception classes are defined in this file. Each of these classes inherits the Exception class.

      1. NameError
      2. CommaError
      3. DuplicateError
      4. YearError
      5. LengthError

8 - 10. BOOKS.TXT, USERS.TXT, AUTHORS.TXT

  The application's permanent databases are stored in these files
  
11. OVERVIEW

  This file contains the prompts for the assignment.

12. CONCLUSION

  I'm pretty happy with how this turned out. My only major issue is that I need to understand more about how exporting and importing class objects affect their attributes. 
  I found myself subconsciously shying away from solutions that would put me in a position where the class object attributes were too relied upon.


