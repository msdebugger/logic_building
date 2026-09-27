"""
Q45: Write a lambda function that takes a number and returns "Positive" or "Negative"

"""

num = int(input("Enter number: "))

result = lambda num:  "Positive" if num > 0 else "Negative"

print(result(num))