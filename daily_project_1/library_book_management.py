import pandas as pd
import os

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)
        print(f'New member {member.name} added.')


    def add_book(self, book):
        self.books.append(book)
        print(f'Added {book.title} by {book.author}')

    def book_checkout(self, title, member_id):
        for book in self.books:
            if book.title == title:
                book.availability = 'Not Available'
                member_name = next((member.name for member in self.members if member.m_id == member_id), "")
                print(f'Book {title} checked out to {member_name}')
                return
        print(f'Book {title} not checked out')

    def book_return(self, title):
        for book in self.books:
            if book.title == title:
                book.availability = 'Available.'
                print(f'Book {title} returned.')
                return
        print(f'Book {title} not returned')

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'Removed {book.title} by {book.author}')
                return
        print(f'Book {title} not found.')

    def search_book(self, keyword):
        searched_book = [book for book in self.books if book.title.lower() == keyword.lower() or
                         book.author.lower() == keyword.lower()]

        if searched_book:
            print(f'Found {len(searched_book)} book matched.')
            for book in searched_book:
                book.get_books()
        else:
            print('Books not found.')

    def display_books(self):
        for index, book in enumerate(self.books):
            print(f'{index + 1}. {book.title} Genre: {book.genre} by {book.author} (ISBN: {book.isbn} - {book.availability})')


class Book:
    def __init__(self, title, author, isbn, genre, availability='Available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

    def get_books(self):
        print(f'{self.title} by {self.author} (ISBN: {self.isbn} - {self.availability})')


class Member:
    def __init__(self, m_id, name):
        self.m_id = m_id
        self.name = name

class Store:
    @staticmethod
    def save(books):
        data = []
        for book in books:
            data.append({
                'title': book.title,
                'author': book.author,
                'isbn': book.isbn,
                'genre': book.genre,
                'availability': book.availability,
            })

        df = pd.DataFrame(data)

        if not os.path.exists('files/library.csv'):
            df.to_csv('files/library.csv', index=False)
        else:
            df.to_csv('files/library.csv', header=False, mode='a', index=False)

        print('Data successfully saved.')

    @staticmethod
    def update(title):
        df = pd.read_csv('files/library.csv')
        df.loc[df['title'] == title, 'availability'] = 'Not Available'
        df.to_csv('files/library.csv', index=False)

        print('Data successfully updated.')

library = Library()

library.add_book(Book('Book1', 'Author1', 'ISBN1', 'Crime'))
library.add_book(Book('Book2', 'Author3', 'ISBN2', 'Drama'))
library.add_book(Book('Book3', 'Author3', 'ISBN3', 'Romance'))
print()

Store.save(library.books)
print()

library.display_books()
print()

library.add_member(Member(1, 'Chandu'))
library.add_member(Member(2, 'Methuja'))
library.add_member(Member(3, 'Pranali'))
print()

library.book_checkout('Book1', 2)
print()

Store.update('Book1')




