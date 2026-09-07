num = int(input("Enter Number: "))

if num == 0 or num == 1:
    print("Number is nor even neither odd")
elif num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
