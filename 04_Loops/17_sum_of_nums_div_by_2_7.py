# Sum of all the numbers from 1 to 100 divisible by 2 and 7
num = 0
for i in range(1,101):
    if i % 2 == 0 and i % 7 == 0:
        num += i
print(num)        
