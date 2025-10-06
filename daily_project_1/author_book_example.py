class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.books = []

    def write_book(self, title, year):
        book = Book(title, year, Author(self.name, self.birth_year))
        self.books.append(book)
        return book

    def get_bibliography(self):
        for book in self.books:
            print(book.title, end=' ')


class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_info(self):
        return f'{self.title} by {self.author.name}'


    def __str__(self):
        return f'{self.title} by {self.author.name}'

a = Author("George Orwell", 1903)
b = a.write_book("1984", 1949)

print(b.get_info())
print(b.author.name)
print(a.get_bibliography())