   # issued_books.append(name)
# LIBRARY.PY

books = []
issued_books = []

# ADD BOOKS
def add_books():
    name = input("Enter the name of the book: ")
    books.append(name)
    print("Book added successfully")

# SHOW BOOKS
def show_books():
    if len(books) == 0:
        print("No books available")
    else:
        print("Books Available:")
        for b in books:
            print(b)

# ISSUE BOOKS
def issue_books():
    show_books()
    name = input("Enter the book name: ")
    if name in books:
        books.remove(name)
        issued_books.append(name)   # ✅ FIXED (add to issued list)
        print("Book issued successfully")
    else:
        print("Book not available")

# RETURN BOOK
def return_books():
    name = input("Enter the name of the book: ")
    if name in issued_books:
        issued_books.remove(name)   # ✅ FIXED (function call)
        books.append(name)
        print("Book returned successfully")
    else:
        print("This book was not issued")

# MAIN FUNCTION
def library():
    while True:
        print("\n1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()   # ✅ FIXED (wrong function call)
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid Choice")

# RUN
library()