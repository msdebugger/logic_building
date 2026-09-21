"""
Q36: Write a function that prints all the factors of a number entered by the user.
"""

num = int(input("Enter number: "))

def factors():
    for i in range(1, num+1):
        if num % i == 0:
            print(i) 
        
factors();            