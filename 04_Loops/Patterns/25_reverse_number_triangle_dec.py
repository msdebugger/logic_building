"""
Q25: Write a nested loop program to print the following pattern:
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""


num = int(input("Enter number: "))



for i in range(num, 0, -1):
    for j in range(num, num - i, -1):
        print(j, end=" ")
    print()