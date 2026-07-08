from library import Library

library = Library()

library.load_books()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author: ")

        library.add_book(title, author)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        library.show_books()

        index = int(input("Enter book number to issue: ")) - 1

        library.issue_book(index)

    elif choice == "4":
        library.show_books()

        index = int(input("Enter book number to return: ")) - 1

        library.return_book(index)

    elif choice == "5":
        keyword = input("Enter title or author to search: ")

        library.search_book(keyword)

    elif choice == "6":
        library.save_books()

        print("Data saved successfully.")
        print("Goodbye!")

        break

    else:
        print("Invalid choice. Please try again.")