"""
Q42: Write a function called min_of_three that takes three numbers and returns the smallest without using any built-in function.

"""

num1 = int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

def min_of_three(a,b,c):
    if num1 < num2 and num1 < num3:
        print(f"{num1} is minimum")
    elif num2 < num1 and num2 < num3:
        print(f"{num2} is minimum")
    elif num3 < num1 and num3 < num2:
        print(f"{num3} is minimum")
    else:
        print("All are equal")    

min_of_three(num1, num2, num3)        

