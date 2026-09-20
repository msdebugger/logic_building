"""
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1

"""

num = int(input("Enter number: "))

for i in range(1, num+1):
    for j in range(1, num+1):
        if (i + j) % 2 == 1:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()            