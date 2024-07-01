# Function to calculate discounted price
def calculate_discounted_price(original_price: float, discount: float) -> float:
    discounted_price = original_price * (1 - discount / 100)
    return round(discounted_price, 2)
