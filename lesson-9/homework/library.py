import os

class BookNotFoundException(Exception):
    def __init__(self, title):
        super().__init__(f"Book '{title}' not found in the library!")

class BookAlreadyBorrowedException(Exception):
    def __init__(self, title):
        super().__init__(f"Book '{title}' is already borrowed!")

class MemberLimitExceededException(Exception):
    def __init__(self, limit=3):
        super().__init__(f"Members can only borrow up to {limit} books!")


class Book:
    def __init__(self, title: str, author: str, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Member:
    def __init__(self, name: str, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []

    def __str__(self):
        borrowed_titles = ", ".join(book.title for book in self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f"Member: {self.name}, Books: {borrowed_titles}"

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException()
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
        else:
            raise Exception(f"{self.name} did not borrow '{book.title}'")


class Library:
    def __init__(self, filename="library_data.txt"):
        self.books = {}
        self.members = {}
        self.filename = filename
        self.load_data()

    def add_book(self, book):
        self.books[book.title] = book
        self.save_data()

    def add_member(self, member):
        self.members[member.name] = member
        self.save_data()

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(book_title)

        book = self.books[book_title]
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book_title)

        if member_name not in self.members:
            raise Exception("Member not found!")

        member = self.members[member_name]
        member.borrow_book(book)
        self.save_data()

    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            raise Exception("Member not found!")

        if book_title not in self.books:
            raise BookNotFoundException(book_title)

        member = self.members[member_name]
        book = self.books[book_title]

        member.return_book(book)
        self.save_data()

    def save_data(self):
        with open(self.filename, "w") as file:
            file.write("BOOKS\n")
            for book in self.books.values():
                file.write(f"{book.title}, {book.author}, {book.is_borrowed}\n")

            file.write("MEMBERS\n")
            for member in self.members.values():
                borrowed_books = "|".join(book.title for book in member.borrowed_books)
                file.write(f"{member.name}, {borrowed_books}\n")

    def load_data(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            section = None
            for line in file:
                line = line.strip()
                if line == "BOOKS":
                    section = "books"
                    continue
                elif line == "MEMBERS":
                    section = "members"
                    continue

                if section == "books":
                    title, author, is_borrowed = line.split(", ")
                    self.books[title] = Book(title, author, is_borrowed == "True")

                elif section == "members":
                    parts = line.split(", ")
                    name = parts[0]
                    borrowed_titles = parts[1].split("|") if len(parts) > 1 else []
                    borrowed_books = [self.books[title] for title in borrowed_titles if title in self.books]
                    self.members[name] = Member(name, borrowed_books)

    def __str__(self):
        books_list = "\n".join(str(book) for book in self.books.values())
        members_list = "\n".join(str(member) for member in self.members.values())
        return f"Library Books:\n{books_list}\n\nLibrary Members:\n{members_list}"


def main():
    library = Library()

    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            book = Book(title, author)
            library.add_book(book)
            print(f"Book '{title}' added to the library.")

        elif choice == "2":
            name = input("Enter member name: ").strip()
            member = Member(name)
            library.add_member(member)
            print(f"Member '{name}' added to the library.")

        elif choice == "3":
            member_name = input("Enter member name: ").strip()
            book_title = input("Enter book title to borrow: ").strip()
            try:
                library.borrow_book(member_name, book_title)
                print(f"'{book_title}' has been borrowed by {member_name}.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            member_name = input("Enter member name: ").strip()
            book_title = input("Enter book title to return: ").strip()
            try:
                library.return_book(member_name, book_title)
                print(f"'{book_title}' has been returned by {member_name}.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            print("Library Status:")
            print(library)

        elif choice == "6":
            print("Exiting Library System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1-6.")


if __name__ == "__main__":
    main()
