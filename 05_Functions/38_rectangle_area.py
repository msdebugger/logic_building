"""
Q38: Write a function called rectangle_area that takes length and breadth as parameters and prints the area.
"""

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

def rectangle_area(a, b):
    area = 2*(length+breadth)
    print(f"Area of rectangle is: {area}")

rectangle_area(length, breadth);    