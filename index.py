print("Your welcome In the library")
print("please select,what you want to do")

print("=> (1) for saw a library books")
print("=> (2) for issue a book for reading")
print("=> (3) for return a issue book ")
print("=> (4) for renew a issue book \n")

choice = int(input("plzz enter your choice here : "))
print()

library_books = ["1.To Kill a Mockingbird","2.Pride and Prejudice", "3.The Great Gatsby", "4.1984", "5.The Lord of the Rings", "6.The Little Prince", "7.A Tale of Two Cities", "8.Dune","9.modern hits","10.The Silent Patient"]

if choice == 1:
    print("\nAvailable Library Books:\n")
    for book in library_books:
        print(book)

elif choice == 2:
    issued_books = []
    book_name = input("Enter book name to issue: ")
    if book_name in library_books:
        library_books.remove(book_name)
        issued_books.append(book_name)
    else:
        print("Book not available")

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

else:
    print("Invalid choice")




