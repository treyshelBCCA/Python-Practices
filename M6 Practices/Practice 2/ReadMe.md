# Inventory Management System using Data Classes

This project demonstrates how to build an inventory management system in Python using data classes. The system utilizes `Product` and `Store` data classes to manage products within a store's inventory.

## Objective

The objective of this project is to practice using data classes in Python to model and manage structured data, such as products and their quantities in a store.

## Files

- **`store.py`**: Defines the `Product` and `Store` data classes along with methods to manipulate the store's inventory (`add_product`, `remove_product`, `find_products_by_price_range`, `find_product_by_name`, `update_product_quantity`).

- **`main.py`**: Demonstrates the creation of a `Store` instance, addition of products to its inventory, and testing of store methods (`find_products_by_price_range`, `find_product_by_name`, `update_product_quantity`).

## How to Use

1. **Define Products**:

   - Edit `store.py` to modify or add more products by creating instances of the `Product` class within the `add_products_to_store` function.

2. **Run the Program**:

   - Execute `python main.py` in your terminal or command prompt.
   - The program will create a store, add products to its inventory, and demonstrate various operations on the inventory.

3. **Testing**:
   - Modify `main.py` to add more test cases or operations on the store's inventory.
   - Use the implemented methods in `Store` class (`find_products_by_price_range`, `find_product_by_name`, `update_product_quantity`) to interact with and manipulate the inventory.

## Example

Here’s a brief example of how the system works:

```
--- Finding products by price range ($200 - $700) ---
Smartphone: $599.99 - Quantity: 10
Tablet: $299.99 - Quantity: 8
--- Finding product by name Laptop ---
Found Laptop: $999.99 - Quantity: 5
--- Updating quantity of Smartphone ---
Quantity updated successfully.
--- Final inventory after operations ---
Laptop: $999.99 - Quantity: 5
Smartphone: $599.99 - Quantity: 7
Tablet: $299.99 - Quantity: 8
```
