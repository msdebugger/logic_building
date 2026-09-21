"""
35. Write a function that asks a number from the user and prints if that number is odd or even.
"""

num = int(input("Enter number: "))

def evenodd():
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


evenodd();            