"""
Q33: Write a nested loop program to print the following pattern (hollow square): (Assignment)
* * * * *
*       *
*       *
*       *
* * * * *

"""

num = int(input("Enter number: "))

for i in range(1, num+1):
    if i==1 or i==num:
        for j in range(1, num+1):
            print("*", end=" ")
        print()    
    else:
        for j in range(1, num+1):
            if j == 1 or j == num:
                print("*", end=" ")
            else:    
                print(" ", end=" ")        
        print()    


