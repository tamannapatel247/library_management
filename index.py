librarians = {}
managers = {}

library_books = [
    "To Kill a Mockingbird",
    "Pride and Prejudice",
    "The Great Gatsby",
    "1984",
    "The Lord of the Rings",
    "The Little Prince",
    "A Tale of Two Cities",
    "Dune",
    "Modern Hits",
    "The Silent Patient"
]

while True:
    print("Welcome In the Library")
    print("LOGIN OR \nREGISTRATION ")
    u_v = input("ENTER HERE : ").upper()

    if u_v == "REGISTRATION":
        print("\n--- User Registration ---")

        name = input("Enter name: ")
        password = input("Enter password: ")

        print("Select category")
        print("1. Librarian")
        print("2. Manager")

        category = int(input("Enter choice: "))

        if category == 1:
            librarians[name] = password
            print("Librarian registered successfully")

        elif category == 2:
            managers[name] = password
            print("Manager registered successfully")

        else:
            print("Invalid category")
            continue

    elif u_v == "LOGIN":
        print("\n--- Login ---")

        login_name = input("Enter name: ")
        login_pass = input("Enter password: ")

        print("Login as:")
        print("1. Librarian")
        print("2. Manager")

        login_type = int(input("Enter choice: "))

        # ---------------- LIBRARIAN ----------------
        if login_type == 1:
            if login_name in librarians and librarians[login_name] == login_pass:
                print("Librarian login successful")
            else:
                print("Invalid Librarian credentials")
                continue

            issued_books = []

            while True:
                print("\nPlease select what you want to do")
                print("1. View library books")
                print("2. Issue a book")
                print("3. Return a book")
                print("4. Renew a book")
                print("-1. Exit")
                print("")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("\nAvailable Books:")
                    for i, book in enumerate(library_books, start=1):
                        print(f"{i}. {book}")

                elif choice == 2:
                    book_name = input("Enter book name to issue: ")
                    if book_name in library_books:
                        issued_books.append(book_name)
                        library_books.remove(book_name)
                        print("Book issued successfully")
                    else:
                        print("Book not found in library")

                elif choice == 3:
                    book_name = input("Enter book name to return: ")
                    if book_name in issued_books:
                        issued_books.remove(book_name)
                        library_books.append(book_name)
                        print("Book returned successfully")
                    else:
                        print("This book was not issued")

                elif choice == 4:
                    book_name = input("Enter book name to renew: ")
                    if book_name in issued_books:
                        print("Book renewed successfully")
                    else:
                        print("Book not issued, cannot renew")

                elif choice == -1:
                    print("Exiting Librarian Menu")
                    print("Thank you for visiting")
                    break

                else:
                    print("Invalid choice")

        # ---------------- MANAGER ----------------
        elif login_type == 2:
            if login_name in managers and managers[login_name] == login_pass:
                print("Manager login successful")
            else:
                print("Invalid Manager credentials")
                continue

            while True:
                print("\nManager Menu")
                print("1. View Total Books")
                print("2. Insert Book")
                print("3. Delete Book")
                print("-1. Exit")
                print("")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    for i, book in enumerate(library_books, start=1):
                        print(f"{i}. {book}")

                elif choice == 2:
                    new_book = input("Enter book name to insert: ")
                    library_books.append(new_book)
                    print("Book added successfully")

                elif choice == 3:
                    del_book = input("Enter book name to delete: ")
                    if del_book in library_books:
                        library_books.remove(del_book)
                        print("Book deleted successfully")
                    else:
                        print("Book not found")

                elif choice == -1:
                    print("Exiting Manager Menu")
                    print("thank you visiting")
                    break

                else:
                    print("Invalid choice")

    else:
        print("Invalid password , name or catagory \nOR\n if you do not please registraed your self first ")
