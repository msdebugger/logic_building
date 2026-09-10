# Ask a number from the user, and print all the factors.

num = int(input("Enter number: "))

for i in range(1, num+1):
    if num % i == 0:
        print(i)