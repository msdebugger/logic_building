"""
Q81: Product Price Lookup Construct a dictionary containing four product names and their prices. Prompt the user to enter a product name. Use the in keyword to check if it exists; if so, display its price. Otherwise, inform the user "Product not found." (Homework)
"""

products = {
    "Mobile": 20000,
    "Car": 500000,
    "Charger": 2000,
    "Bag": 1000
}

product = input("Enter product: ")
if product in products:
    print(f"Price of product is: {products[product]}")
else:
    print("Product not found")    