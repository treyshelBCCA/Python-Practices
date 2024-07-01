# Python Data Classes Exercise README

## Objective

This exercise aims to help you understand and practice using data classes in Python. Data classes provide a convenient way to define and work with structured data without repetitive boilerplate code.

## Tasks

### 1. Define the `Book` Data Class (**_This is done for you_**)

Create a Python file (`book.py` for example) and define a data class named `Book` using the `@dataclass` decorator from the `dataclasses` module. Include the following attributes in your `Book` class:

- `title` (str)
- `author` (str)
- `price` (float)

### 2. Implement Helper Functions (**_This is done for you_**)

Inside the same file (`book.py`), implement two functions:

- `display_book_info(book: Book)`: This function takes a `Book` object as an argument and prints its `title`, `author`, and `price` attributes in a neat format.
- `update_book_price(book: Book, new_price: float)`: This function updates the `price` attribute of a `Book` object to the specified `new_price`.

### 3. Create Instances and Test

In your main script or another file (`main.py` for example), import the `Book` class and the helper functions from `book.py`. Create instances of the `Book` class with predefined data (e.g., `"Python Tricks"`, `"Dan Bader"`, `29.99`).

### 4. Display and Verify Information

- Call the `display_book_info` function for each instance to display their initial information.
- Use the `update_book_price` function to change the price of one book instance.
- Call `display_book_info` again to verify that the price update was successful.

## The output should be:

```
Initial Information:
Title: Python Tricks
Author: Dan Bader
Price: $29.99
---
Title: Fluent Python
Author: Luciano Ramalho
Price: $39.99
---
Updated Information:
Title: Python Tricks
Author: Dan Bader
Price: $34.99
---
Title: Fluent Python
Author: Luciano Ramalho
Price: $39.99
```
