"""
Q48: Write a function tax_calculator(income) that takes annual income and returns the tax amount based on these slabs: Up to 2,50,000 -> No tax, 2,50,001 to 5,00,000 -> 5%, 5,00,001 to 10,00,000 -> 20%.
(Assignment)
"""

income = float(input("Enter income: "))

def tax_calculator(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return income * 0.05
    elif income <= 1000000:
        return income * 0.20
    else:
        return "Income is greater than 1000000"

print(tax_calculator(income))    
    