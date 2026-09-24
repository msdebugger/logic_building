"""
Q40: Write a function called discount_price that takes original_price and discount_percent as parameters and prints the final price after discount.
"""

org_price = int(input("Enter price: "))
discount_percent = float(input("Enter discount: "))

def discount_price(org_price, discount_percent):
    discount_price = org_price * (discount_percent/100)
    final_price = org_price - discount_price
    print(f"Final price is {final_price}")

discount_price(org_price, discount_percent)    

