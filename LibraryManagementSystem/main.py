from library import Library

library = Library()

library.load_books()


while True:

    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


    choice = input("Enter your choice: ")


    if choice == '1':

        title = input("Enter book title: ")
        author = input("Enter book author: ")

        library.add_book(title, author)


    elif choice == '2':

        library.show_books()


    elif choice == '3':

        library.show_books()

        index = int(input("Enter book number to issue: ")) - 1

        library.issue_book(index)


    elif choice == '4':

        library.show_books()

        index = int(input("Enter book number to return: ")) - 1

        library.return_book(index)


    elif choice == '5':

        library.save_books()

        print("Goodbye!")

        break