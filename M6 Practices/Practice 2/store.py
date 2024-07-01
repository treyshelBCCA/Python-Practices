from dataclasses import dataclass
from typing import List
from product import *

@dataclass
class Store:
    name: str
    location: str
    inventory: List[Product]

    def add_product(self, product: Product):
        self.inventory.append(product)

    def remove_product(self, name: str):
        for product in self.inventory:
            if product.name == name:
                self.inventory.remove(product)
                return

    def find_products_by_price_range(self, min_price: float, max_price: float) -> List[Product]:
        return [product for product in self.inventory if min_price <= product.price <= max_price]

    def find_product_by_name(self, name: str) -> Product or None:
        for product in self.inventory:
            if product.name == name:
                return product
        return None

    def update_product_quantity(self, name: str, quantity_change: int) -> bool:
        for product in self.inventory:
            if product.name == name:
                if product.quantity + quantity_change >= 0:
                    product.quantity += quantity_change
                    return True
                else:
                    return False
        return False

