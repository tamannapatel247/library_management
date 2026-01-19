print("Welcome In the Library")

print("Enter 1 for Librarian")
print("Enter 2 for Manager")

user = int(input("Enter choice: "))

# ---------------- LIBRARIAN ----------------
if user == 1:

    issued_books = []

    while True:
        print("\nPlease select what you want to do")
        print("1. View library books")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. Renew a book")
        print("-1. Exit")

        choice = int(input("Enter your choice: "))

        library_books = ["1.To Kill a Mockingbird","2.Pride and Prejudice", "3.The Great Gatsby", "4.1984", "5.The Lord of the Rings", "6.The Little Prince", "7.A Tale of Two Cities", "8.Dune","9.modern hits","10.The Silent Patient"]

        if choice == 1:
            for i in library_books:
                print(i)

        elif choice == 2:
            book_name = input("Enter book name to issue: ")
            issued_books.append(book_name)
            print("Book issued successfully")

        elif choice == 3:
            book_name = input("Enter book name to return: ")
            if book_name in issued_books:
                issued_books.remove(book_name)
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
            print("thank you visiting")
            break   

        else:
            print("Invalid choice")

# ---------------- MANAGER ----------------
elif user == 2:

    library_books = [
        "To Kill a Mockingbird",
        "Pride and Prejudice",
        "The Great Gatsby",
        "1984",
        "The Lord of the Rings"
    ]

    while True:
        print("\nManager Menu")
        print("1. View Total Books")
        print("2. Insert Book")
        print("3. Delete Book")
        print("-1. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            for book in library_books:
                print(book)

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
    print("Invalid user selection")
