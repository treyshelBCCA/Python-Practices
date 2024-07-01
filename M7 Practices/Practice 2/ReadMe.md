# Python Practice: Data Persistence with Text Files using Data Class

## Objective

This exercise focuses on practicing data persistence in Python using text files and data classes. You will implement functions to store, retrieve, update, and manage product data in a text file.

## Requirements

1. **Define a Data Class**

   - Define a data class `Product` with the following attributes:
     - `name` (str): Name of the product.
     - `price` (float): Price of the product.
     - `quantity` (int): Quantity of the product.

2. **Write to a Text File**

   - Implement a function `write_to_file(products: List[Product], filename: str)` to write instances of the `Product` data class to a text file (`inventory.txt`). Each instance should be stored on a new line in the format `"name|price|quantity"`.

3. **Read from the Text File**

   - Implement a function `read_from_file(filename: str) -> List[Product]` to read instances of the `Product` data class from `inventory.txt` and return a list of `Product` objects.

4. **Update and Write Back**

   - Implement a function `update_product_quantity(products: List[Product], product_name: str, new_quantity: int, filename: str) -> bool` to update the quantity of a specific product in the `products` list, write the updated instances back to `inventory.txt`, and return `True` if successful, `False` otherwise.

5. **Example Usage**

   - Implement the main function to demonstrate example usage of the implemented functions:
     - Initialize a list of `Product` instances.
     - Write these instances to `inventory.txt`.
     - Read from `inventory.txt` and display the current inventory.
     - Update the quantity of a product and verify the update by reading from `inventory.txt` again.
