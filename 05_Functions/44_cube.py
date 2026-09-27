"""
Q44: Write a lambda function that takes a number and returns its cube. Store it in a variable and call it.
"""

num = int(input("Enter a number: "))

cube = lambda num : num * num * num

print(cube(num))