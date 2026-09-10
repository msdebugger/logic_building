# Sum of all the numbers from 1 to 100
#Best way
for i in range(1,101):
    num = (i*(i+1))/2

print(int(num))


#solution 1
num = 0
for i in range(1,101):
    num = num + i

print(num)    