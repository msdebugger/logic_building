"""
Q43: Write a function called absolute_value that takes a number and returns its absolute value without using the built-in abs() function.

"""
num = float(input("Enter number: "))

def absolute_value(a):
    if num < 0:
        return -1 * num
    else:
        return num



print(absolute_value(num))