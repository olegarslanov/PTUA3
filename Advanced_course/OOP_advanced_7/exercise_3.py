# Create a class called Book that takes title, author, and ISBN as parameters. The class
# should have __bool__, __repr__, __len__, __str__, __eq__, __add__, and __getitem__ methods defined.

# The __bool__ method should return True if the book has a title, False otherwise.
# The __repr__ method should return a string in the format "Book(title, author, ISBN)" where title,
# author and ISBN are the respective attributes of the class
# The __len__ method should return the number of pages of the book
# The __str__ method should return a string in the format "title by author (ISBN)"
# The __eq__ method should compare two books and return True if both ISBN are the same and False
# otherwise.
# The __add__ method should add two books and return a new book object that contains the contents
# of both books concatenated and the title of the new book should be the title of the first book
# The __getitem__ method should return the title of the book if the index passed is 0, and the
# author of the book if the index passed is 1.


class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        Book.pages = 1000

    def __bool__(self):
        return bool(self.title)

    def __repr__(self):
        return f"Book ({self.title}, {self.author}, {self.ISBN})"

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.ISBN})"

    def __eq__(self, other: "Book") -> bool:
        if isinstance(other, Book):
            return self.ISBN == other.ISBN
        return False

    def __add__(self, other: "Book") -> "Book":
        if isinstance(other, Book):
            return Book(self.title, self.author + other.author, self.ISBN + other.ISBN)


book1 = Book(title="Bible", author="God", ISBN="ISBN 0-7475-3269-9")
book2 = Book("Vedy", "None", "ISBN 0-7456-3631-8")
book3 = book1 + book2

print(bool(book1))
print(repr(book1))
print(len(book1))
print(len(book2))
print(str(book1))
print(book1 == book2)
print(book3.title, book3.author, book3.ISBN)
