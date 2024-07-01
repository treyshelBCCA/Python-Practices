# Function to write items to a text file
def write_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            f.write(f"{item['name']}: {item['quantity']}\n")

# Function to read items from a text file
def read_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            name, quantity = line.strip().split(': ')
            print(f"{name} - {quantity}")

# Function to update quantity of an item and write back to file
def update_item_quantity(items, item_name, new_quantity, filename):
    for item in items:
        if item['name'] == item_name:
            item['quantity'] = new_quantity
            write_to_file(items, filename)
            return True
    return False

# Main function to demonstrate usage
def main():
    items = [
        {"name": "Apple", "quantity": 10},
        {"name": "Banana", "quantity": 5},
        {"name": "Orange", "quantity": 8}
    ]
    
    filename = "inventory.txt"
    
    # Write initial items to file
    write_to_file(items, filename)
    
    # Read items from file and print
    print("--- Current Inventory ---")
    read_from_file(filename)
    
    # Update quantity of an item
    item_name = "Banana"
    new_quantity = 7
    if update_item_quantity(items, item_name, new_quantity, filename):
        print(f"\n{item_name} quantity updated to {new_quantity}.")
        print("--- Updated Inventory ---")
        read_from_file(filename)
    else:
        print(f"\nFailed to update quantity for {item_name}. Item not found.")

if __name__ == "__main__":
    main()
