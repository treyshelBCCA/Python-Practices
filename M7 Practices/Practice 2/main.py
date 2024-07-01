from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    price: float
    quantity: int

# Function to write products to a text file
def write_to_file(products: List[Product], filename: str):
    with open(filename, 'w') as f:
        for product in products:
            f.write(f"{product.name}|{product.price}|{product.quantity}\n")

# Function to read products from a text file
def read_from_file(filename: str) -> List[Product]:
    products = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            name, price, quantity = line.strip().split('|')
            products.append(Product(name=name, price=float(price), quantity=int(quantity)))
    return products

# Function to update quantity of a product and write back to file
def update_product_quantity(products: List[Product], product_name: str, new_quantity: int, filename: str) -> bool:
    for product in products:
        if product.name == product_name:
            product.quantity = new_quantity
            write_to_file(products, filename)
            return True
    return False

# Main function for example usage
def main():
    filename = "inventory.txt"
    
    # Example usage of functions
    products = [
        Product(name="Apple", price=1.99, quantity=10),
        Product(name="Banana", price=0.99, quantity=5),
        Product(name="Orange", price=2.49, quantity=8)
    ]
    
    # TODO: Implement further functionality as per the exercise tasks
    
if __name__ == "__main__":
    main()
