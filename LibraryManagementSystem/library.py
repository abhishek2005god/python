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

        print("Book added successfully")


    def show_books(self):
        if not self.books:
            print("No books available")
            return

        for index, book in enumerate(self.books):
            status = "Issued" if book.is_issued else "Available"

            print(f"{index + 1}. {book.title} by {book.author} - {status}")


    def issue_book(self, index):

        if index < 0 or index >= len(self.books):
            print("Invalid book number")
            return

        if self.books[index].is_issued:
            print("Book already issued")

        else:
            self.books[index].is_issued = True
            print("Book issued successfully")


    def return_book(self, index):

        if index < 0 or index >= len(self.books):
            print("Invalid book number")
            return

        if not self.books[index].is_issued:
            print("Book was not issued")

        else:
            self.books[index].is_issued = False
            print("Book returned successfully")


    def save_books(self):
        file = open("books.txt", "w")

        for book in self.books:
            file.write(f"{book.title},{book.author},{book.is_issued}\n")

        file.close()


    def load_books(self):
        file = open("books.txt", "r")

        for line in file:
            title, author, status = line.strip().split(",")

            book = Book(title, author, status == "True")

            self.books.append(book)

        file.close()
