"""
Q24: Write a nested loop program to print the following pattern:
1 2 3 4 5  row = 1
1 2 3 4     
1 2 3
1 2
1
"""

num = int(input("Enter number: "))

for i in range(num, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()    