# You need to create a program to manage a list of books in a library. Each book
# has a title, an author, a publication year, and an ISBN. You need to define a
# Book class using the dataclass module that contains attributes for these properties.
#  You also need to implement a Library class that manages a list of books. The
#  Library class should allow you to add and remove books from the library, search
#   for books by title or author, and display the list of books currently in the library.


from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    isbn: str


class Library:
    books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
        #         return True
        # return False

    def search_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books if book.title == title]

    def search_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if book.author == author]

    def display_books(self) -> None:
        for book in self.books:
            print(
                f"{book.title} by {book.author}, published in {book.publication_year}, ISBN: {book.isbn}"
            )


book1 = Book("Book of year", "Bivis K.", 2023, "14 - 5689 - 1458 - 65 - 56")
book2 = Book("Zaika", "Pugacheva A.", 2022, "13 - 5879 - 3489 - 98 - 15")

library = Library()
library.add_book(book1)
library.add_book(book2)

# Library.display_books(library)
library.display_books()

print(library.search_by_title("Book of year"))
print(library.search_by_author("Pugacheva A."))

library.remove_book("14 - 5689 - 1458 - 65 - 56")

library.display_books()
