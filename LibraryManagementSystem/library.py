class Book:
    def __init__(self, title, author, is_issued=False):
        self.title = title
        self.author = author
        self.is_issued = is_issued


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book added successfully!")

    def show_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        print("\nBooks in Library:")
        for index, book in enumerate(self.books):
            status = "Issued" if book.is_issued else "Available"
            print(f"{index + 1}. {book.title} by {book.author} - {status}")

    def issue_book(self, index):
        if index < 0 or index >= len(self.books):
            print("Invalid book number.")
            return

        if self.books[index].is_issued:
            print("Book already issued.")
        else:
            self.books[index].is_issued = True
            print("Book issued successfully!")

    def return_book(self, index):
        if index < 0 or index >= len(self.books):
            print("Invalid book number.")
            return

        if not self.books[index].is_issued:
            print("Book is already available.")
        else:
            self.books[index].is_issued = False
            print("Book returned successfully!")

    def search_book(self, keyword):
        found = False

        for index, book in enumerate(self.books):
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                status = "Issued" if book.is_issued else "Available"
                print(f"{index + 1}. {book.title} by {book.author} - {status}")
                found = True

        if not found:
            print("Book not found.")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.is_issued}\n")

    def load_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    line = line.strip()

                    if line == "":
                        continue

                    title, author, status = line.split(",")

                    book = Book(title, author, status == "True")
                    self.books.append(book)

        except FileNotFoundError:
            pass