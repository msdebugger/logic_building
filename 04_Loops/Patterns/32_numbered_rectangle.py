"""
Q32: Write a nested loop program to print the following pattern: (Assignment)
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

num = int(input("Enter number: "))

for i in range(1, num+1):
    for j in range(1, num+1):
        print(j, end=" ")
    print()