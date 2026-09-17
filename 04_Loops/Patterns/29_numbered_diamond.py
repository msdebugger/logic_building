"""
Q29: Write a nested loop program to print the following pattern (centered numbers):
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1

"""

num = int(input("Enter number: "))

for i in range(1, num+1):
    for j in range(1, num-i+1):
        print(" ", end=" ")
    for k in range(1, (i*2)-1+1):
        print(k, end=" ")
    print()    


for i in range(num-1, 0, -1):
    for j in range(1, num-i+1):
        print(" ", end=" ")
    for k in range(1, (i*2)-1+1):
        print(k, end=" ")
    print()  