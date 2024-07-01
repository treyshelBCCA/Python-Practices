import unittest
from main import Book  

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(title="Python Tricks", author="Dan Bader", price=29.99)

    def test_get_book_info(self):
        pass

    def test_apply_discount(self):
        pass

if __name__ == '__main__':
    unittest.main()
