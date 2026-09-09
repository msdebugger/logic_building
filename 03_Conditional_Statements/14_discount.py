# A shop gives discounts based on purchase amount: Above 5000 -> 20% discount, Above 2000 ->
# 10% discount, Above 1000 -> 5% discount, 1000 or below -> no discount. (Homework)

amount = int(input("Enter amount: "))

if amount >= 5000:
    print("Discount is 20%")
elif amount >= 2000:
    print("Discount is 10%")
elif amount >= 1000:
    print("Discount is 5%")
else:
    print("No discount")    
