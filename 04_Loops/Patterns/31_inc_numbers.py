"""
Q31: Write a nested loop program to print the following pattern: (Assignment)
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""
count = 1
num = int(input("Enter number: "))

for i in range(1, num+1):
    for j in range(1, i+1):
        print(count, end=" ")
        count += 1
    print()    