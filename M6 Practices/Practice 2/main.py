from store import Store, Product

def create_store():
    # Create a store instance
    return Store(name="SuperMart", location="Downtown", inventory=[])

def add_products_to_store(store):
    # Create and add products to the store
    products = [
        Product(name="Laptop", price=999.99, quantity=5),
        Product(name="Smartphone", price=599.99, quantity=10),
        Product(name="Tablet", price=299.99, quantity=8)
    ]
    
    # add code below

def test_store_methods(store):
    # Test store methods
    
    # add code below
    pass

def main():
    # Create a store
    store = create_store()

    # Add products to the store
    add_products_to_store(store)

    # Test store methods
    test_store_methods(store)

if __name__ == '__main__':
    main()
