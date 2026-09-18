"""
Q30: Write a nested loop program to print the following pattern (centered diamond of stars):
      *
    * * *
  * * * * *
* * * * * * *
* * * * * * * * *
* * * * * * *
  * * * * *
    * * *
      *

"""

num = int(input("Enter number: "))

for i in range(1, num+1):
    for j in range(1, (num-i)+1):
        print(" ", end=" ")
    for k in range(1, (i*2)+1 -1):
        print("*", end=" ")
    print()    

for i in range(num-1, 0, -1):
    for j in range(1, (num-i)+1):
        print(" ", end=" ")
    for k in range(1, (i*2)+1 -1):
        print("*", end=" ")
    print()        