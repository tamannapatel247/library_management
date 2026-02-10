print("Welcome In the Library")
print("LOGIN OR REGISTRATION")

u_v = input("ENTER HERE (LOGIN / REGISTRATION): ").upper()

# databases
librarians = {}
managers = {}

# ---------------- REGISTRATION ----------------
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

# ---------------- LOGIN ----------------
elif u_v == "LOGIN":
    print("\n--- Login ---")

    login_name = input("Enter name: ")
    login_pass = input("Enter password: ")

    print("Login as:")
    print("1. Librarian")
    print("2. Manager")

    login_type = int(input("Enter choice: "))

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

    # ---------------- LIBRARIAN ----------------
    if login_type == 1:
        if login_name in librarians and librarians[login_name] == login_pass:
            print("Librarian login successful")
        else:
            print("Invalid Librarian credentials")
            exit()

        issued_books = []

        while True:
            print("\n1. View Books")
            print("2. Issue Book")
            print("3. Return Book")
            print("4. Renew Book")
            print("-1. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                for i, book in enumerate(library_books, start=1):
                    print(f"{i}. {book}")

            elif choice == 2:
                book = input("Enter book name: ")
                if book in library_books:
                    library_books.remove(book)
                    issued_books.append(book)
                    print("Book issued")

            elif choice == 3:
                book = input("Enter book name: ")
                if book in issued_books:
                    issued_books.remove(book)
                    library_books.append(book)
                    print("Book returned")

            elif choice == -1:
                break

    # ---------------- MANAGER ----------------
    elif login_type == 2:
        if login_name in managers and managers[login_name] == login_pass:
            print("Manager login successful")
        else:
            print("Invalid Manager credentials")
            exit()

        while True:
            print("\n1. View Books")
            print("2. Insert Book")
            print("3. Delete Book")
            print("-1. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                for i, book in enumerate(library_books, start=1):
                    print(f"{i}. {book}")

            elif choice == 2:
                book = input("Enter book name: ")
                library_books.append(book)
                print("Book added")

            elif choice == 3:
                book = input("Enter book name: ")
                if book in library_books:
                    library_books.remove(book)
                    print("Book deleted")

            elif choice == -1:
                break

else:
    print("Please choose LOGIN or REGISTRATION")
