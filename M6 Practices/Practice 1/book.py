from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    price: float

def display_book_info(book: Book):
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Price: ${book.price}")

def update_book_price(book: Book, new_price: float):
    book.price = new_price
